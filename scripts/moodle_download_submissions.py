#!/usr/bin/env python3
"""Download Moodle VPL submissions and unpack them into the local solutions folder."""

from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import sys
import tempfile
import unicodedata
import zipfile
from urllib.parse import parse_qs, urlencode, urlparse

from moodle_e2e import (
    DEFAULT_CONFIG,
    NAVIGATION_TIMEOUT_MS,
    PAGE_TIMEOUT_MS,
    course_year,
    find_task,
    load_config,
    login_to_moodle,
    log_progress,
    navigate,
    parse_task_identifier,
    wait_for_visible,
    wait_for_url,
)

ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_ROOT = ROOT / "řešení"
MAX_NESTED_ARCHIVE_DEPTH = 10


def safe_component(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", value).strip(" .")
    if not value:
        raise ValueError("Název cílové složky je po úpravě prázdný.")
    if re.fullmatch(r"(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?", value, re.I):
        value = f"_{value}"
    return value


def extract_zip_safely(archive_path: Path, destination: Path) -> int:
    """Extract regular files only, rejecting traversal and conflicting paths."""
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    files_written = 0

    with zipfile.ZipFile(archive_path) as archive:
        for info in archive.infolist():
            member_name = info.filename.replace("\\", "/")
            member = PurePosixPath(member_name)
            if (
                member.is_absolute()
                or re.match(r"^[A-Za-z]:", member_name)
                or any(part == ".." for part in member.parts)
            ):
                raise ValueError(
                    f"Archiv {archive_path.name} obsahuje nebezpečnou cestu: "
                    f"{info.filename}"
                )
            parts = tuple(part for part in member.parts if part not in {"", "."})
            if not parts:
                continue

            target = destination.joinpath(*parts)
            if not target.resolve().is_relative_to(root):
                raise ValueError(
                    f"Cesta z archivu {archive_path.name} opouští cílovou složku."
                )

            mode = info.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError(
                    f"Archiv {archive_path.name} obsahuje nepodporovaný symbolický odkaz."
                )
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue

            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info) as source, target.open("xb") as output:
                shutil.copyfileobj(source, output)
            files_written += 1

    return files_written


def extract_nested_archives(root: Path) -> tuple[int, int]:
    archive_count = 0
    files_written = 0
    for depth in range(MAX_NESTED_ARCHIVE_DEPTH + 1):
        archives = sorted(
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix.casefold() == ".zip"
        )
        if not archives:
            return archive_count, files_written
        if depth == MAX_NESTED_ARCHIVE_DEPTH:
            raise ValueError(
                f"V odevzdání jsou ZIP archivy vnořené hlouběji než "
                f"{MAX_NESTED_ARCHIVE_DEPTH} úrovní."
            )

        for archive in archives:
            files_written += extract_zip_safely(archive, archive.parent)
            archive.unlink()
            archive_count += 1

    raise RuntimeError("Rozbalování vnořených ZIP archivů nebylo dokončeno.")


def open_submissions_list(page) -> None:
    submissions_link = page.locator(
        'a.nav-link[href*="/mod/vpl/views/submissionslist.php"]'
    )
    wait_for_visible(
        page,
        'a.nav-link[href*="/mod/vpl/views/submissionslist.php"]',
        "odkaz „Submissions list“",
    )
    if submissions_link.count() != 1:
        raise RuntimeError(
            "Na stránce VPL aktivity nebyl nalezen právě jeden odkaz "
            "„Submissions list“."
        )
    log_progress("Otevírám seznam odevzdání.")
    submissions_link.click(no_wait_after=True)
    wait_for_url(
        page,
        re.compile(r"/mod/vpl/views/submissionslist\.php(?:\?|$)"),
        "seznamu odevzdání",
    )
    log_progress(f"Seznam odevzdání otevřen: {page.url}")


def open_header_download_menu(page):
    header_menu = page.locator("#action-menu-toggle-1")
    wait_for_visible(
        page,
        "#action-menu-toggle-1",
        "nabídka akcí v hlavičce odevzdání",
    )
    if header_menu.count() != 1:
        raise RuntimeError(
            "V hlavičce tabulky odevzdání nebylo nalezeno tlačítko "
            "nabídky #action-menu-toggle-1."
        )

    download_item = page.locator(
        'a[href*="/mod/vpl/views/downloadallsubmissions.php"]:not([href*="all=1"])'
    )
    log_progress("Rozbaluji nabídku akcí.")
    header_menu.click(no_wait_after=True)
    wait_for_visible(
        page,
        'a[href*="/mod/vpl/views/downloadallsubmissions.php"]:not([href*="all=1"])',
        "volba „Download submissions“",
    )
    if download_item.count() != 1:
        raise RuntimeError(
            "V nabídce hlavičky tabulky nebyla nalezena právě jedna volba "
            "„Download submissions“."
        )
    return download_item


def normalize_activity_name(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    value = "".join(
        character
        for character in value
        if unicodedata.category(character) != "Mn"
    )
    return " ".join(
        "".join(character if character.isalnum() else " " for character in value).split()
    )


def find_activity_link(page, activity_name: str):
    activities = page.locator('a[href*="/mod/vpl/view.php"]')
    expected = normalize_activity_name(activity_name)
    matches = []
    names = []

    for index in range(activities.count()):
        activity = activities.nth(index)
        text = activity.inner_text().strip()
        aria_label = activity.get_attribute("aria-label") or ""
        title = activity.get_attribute("title") or ""
        searchable_name = " ".join((text, aria_label, title))
        names.append(text or aria_label or title or "(bez názvu)")
        if expected in normalize_activity_name(searchable_name):
            matches.append(activity)

    if len(matches) != 1:
        discovered = ", ".join(f"„{name}“" for name in names[:12]) or "žádná"
        if len(names) > 12:
            discovered += f", … (+{len(names) - 12})"
        raise RuntimeError(
            f"V kurzu nebyla nalezena právě jedna VPL aktivita "
            f"odpovídající „{activity_name}“ (nalezeno: {len(matches)}). "
            f"Nalezené VPL aktivity: {discovered}."
        )

    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG,
        help=f"cesta k lokální JSON konfiguraci (výchozí: {DEFAULT_CONFIG})",
    )
    parser.add_argument(
        "--class",
        dest="class_name",
        required=True,
        help="klíč třídy podle mapování 'courses' v konfiguraci",
    )
    parser.add_argument("--lesson", type=int, required=True, help="číslo lekce")
    parser.add_argument(
        "--task",
        required=True,
        help="číslo běžného úkolu nebo kód známkovaného úkolu, např. Z02",
    )
    parser.add_argument(
        "--year",
        type=int,
        choices=(1, 2, 3),
        help="ročník zdrojového úkolu (jinak se odvodí z názvu třídy)",
    )
    args = parser.parse_args()
    if args.lesson < 1:
        parser.error("--lesson musí být kladné celé číslo.")

    try:
        task_number, graded, _ = parse_task_identifier(args.task)
        config = load_config(args.config)
        course_id = config["courses"].get(args.class_name)
        if course_id is None:
            raise ValueError(
                f"Třída '{args.class_name}' není v mapování 'courses'."
            )
        year = course_year(args.class_name, args.year)
        task, activity_name, _ = find_task(
            year, args.lesson, task_number, graded=graded
        )
        folder_name = safe_component(
            f"{args.class_name} - Lekce {args.lesson:02d} - {task['title']}"
        )
    except (FileNotFoundError, KeyError, TypeError, ValueError) as error:
        parser.error(str(error))

    destination = SOLUTIONS_ROOT / folder_name
    if destination.exists():
        parser.error(
            f"Cílová složka již existuje: {destination}. "
            "Skript ji nepřepíše; přejmenujte ji nebo zvolte jiný úkol."
        )

    try:
        from playwright.sync_api import Error as PlaywrightError
        from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "Chybí Playwright. Nainstalujte závislosti příkazem "
            "'python -m pip install -r requirements-moodle.txt' a potom "
            "'python -m playwright install chromium'.",
            file=sys.stderr,
        )
        return 1

    SOLUTIONS_ROOT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=False)
        except PlaywrightError as error:
            print(f"Chromium se nepodařilo spustit: {error}", file=sys.stderr)
            return 1
        try:
            page = browser.new_page(accept_downloads=True)
            page.set_default_timeout(PAGE_TIMEOUT_MS)
            page.set_default_navigation_timeout(NAVIGATION_TIMEOUT_MS)
            login_to_moodle(page, config)

            course_url = (
                f"{config['base_url']}/course/view.php?"
                f"{urlencode({'id': course_id})}"
            )
            log_progress(f"Otevírám kurz '{args.class_name}' (ID {course_id}).")
            navigate(page, course_url)
            query = parse_qs(urlparse(page.url).query)
            if query.get("id") != [course_id]:
                raise RuntimeError(
                    f"Nepodařilo se otevřít kurz '{args.class_name}' "
                    f"(ID {course_id}); Moodle přesměroval na {page.url}."
                )
            wait_for_visible(
                page,
                'li[id^="section-"]',
                f"sekce kurzu '{args.class_name}'",
            )
            log_progress(f"Kurz otevřen: {page.url}")

            activity = find_activity_link(page, activity_name)
            log_progress(f"Otevírám aktivitu „{activity_name}“.")
            activity.click(no_wait_after=True)
            wait_for_url(
                page,
                re.compile(r"/mod/vpl/view\.php(?:\?|$)"),
                "VPL aktivity",
            )
            if "/mod/vpl/view.php" not in urlparse(page.url).path:
                raise RuntimeError("Odkaz neotevřel očekávanou VPL aktivitu.")
            log_progress(f"Aktivita otevřena: {page.url}")

            open_submissions_list(page)
            download_item = open_header_download_menu(page)

            with tempfile.TemporaryDirectory(
                prefix=".stahovani-", dir=SOLUTIONS_ROOT
            ) as temporary:
                temporary_path = Path(temporary)
                archive_path = temporary_path / "submissions.zip"
                extracted = temporary_path / "rozbaleno"
                with page.expect_download(timeout=PAGE_TIMEOUT_MS) as download_info:
                    download_item.click()
                download = download_info.value
                download.save_as(archive_path)
                if not zipfile.is_zipfile(archive_path):
                    raise RuntimeError(
                        f"Stažený soubor „{download.suggested_filename}“ "
                        "není platný ZIP archiv."
                    )

                extracted.mkdir()
                files_written = extract_zip_safely(archive_path, extracted)
                archive_path.unlink()
                nested_archives, nested_files = extract_nested_archives(extracted)
                files_written += nested_files
                if destination.exists():
                    raise RuntimeError(
                        f"Cílová složka mezitím vznikla: {destination}."
                    )
                extracted.rename(destination)

            print(
                f"Odevzdání stažena do: {destination}\n"
                f"Souborů rozbaleno: {files_written}; "
                f"vnořených ZIP archivů rozbaleno a odstraněno: "
                f"{nested_archives}."
            )
            return 0
        except (
            OSError,
            RuntimeError,
            ValueError,
            zipfile.BadZipFile,
            PlaywrightError,
        ) as error:
            print(f"Chyba při stahování odevzdání: {error}", file=sys.stderr)
            return 1
        finally:
            browser.close()


if __name__ == "__main__":
    raise SystemExit(main())
