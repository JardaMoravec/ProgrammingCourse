#!/usr/bin/env python3
"""Load a repository task and prepare a Moodle VPL activity."""

from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta
import html
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

import markdown
from generate_tasks import assignment_markdown, load_task, prepare_assignment_markdown

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = ROOT / "moodle" / "e2e.local.json"
LOGIN_TIMEOUT_MS = 300_000
PAGE_TIMEOUT_MS = 60_000
NAVIGATION_TIMEOUT_MS = 120_000
EDIT_MODE_TIMEOUT_MS = 90_000
CZECH_MONTHS = (
    "ledna",
    "února",
    "března",
    "dubna",
    "května",
    "června",
    "července",
    "srpna",
    "září",
    "října",
    "listopadu",
    "prosince",
)


def log_progress(message: str) -> None:
    print(f"[{datetime.now():%H:%M:%S}] {message}", flush=True)


def wait_for_locator(locator, description: str, timeout: int = PAGE_TIMEOUT_MS):
    from playwright.sync_api import Error as PlaywrightError
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

    log_progress(f"Čekám na {description} ({timeout // 1000} s).")
    started = time.monotonic()
    try:
        locator.wait_for(state="visible", timeout=timeout)
    except PlaywrightTimeoutError:
        elapsed = time.monotonic() - started
        log_progress(f"{description} se nenašlo po {elapsed:.1f} s.")
        raise
    except PlaywrightError as error:
        log_progress(f"Čekání na {description} selhalo: {error}")
        raise
    log_progress(f"{description} je připraveno ({time.monotonic() - started:.1f} s).")
    return locator


def wait_for_visible(
    page, selector: str, description: str, timeout: int = PAGE_TIMEOUT_MS
):
    return wait_for_locator(
        page.locator(selector).first, description, timeout=timeout
    )


_NO_WAIT_ARGUMENT = object()


def wait_for_condition(
    page,
    description: str,
    expression: str,
    *,
    timeout: int = PAGE_TIMEOUT_MS,
    arg=_NO_WAIT_ARGUMENT,
) -> None:
    from playwright.sync_api import Error as PlaywrightError
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

    log_progress(f"Čekám na {description} ({timeout // 1000} s).")
    started = time.monotonic()
    try:
        if arg is _NO_WAIT_ARGUMENT:
            page.wait_for_function(expression, timeout=timeout)
        else:
            page.wait_for_function(expression, arg=arg, timeout=timeout)
    except PlaywrightTimeoutError:
        elapsed = time.monotonic() - started
        log_progress(f"Nepodařilo se: {description} ({elapsed:.1f} s).")
        raise
    except PlaywrightError as error:
        log_progress(f"Čekání na {description} selhalo: {error}")
        raise
    log_progress(f"Hotovo: {description} ({time.monotonic() - started:.1f} s).")


def click_and_wait_for_navigation(page, locator, description: str) -> None:
    from playwright.sync_api import Error as PlaywrightError
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

    log_progress(f"Odesílám: {description}.")
    started = time.monotonic()
    try:
        with page.expect_navigation(
            wait_until="domcontentloaded",
            timeout=NAVIGATION_TIMEOUT_MS,
        ):
            locator.click(no_wait_after=True)
    except PlaywrightTimeoutError as error:
        elapsed = time.monotonic() - started
        log_progress(
            f"Po akci „{description}“ nenastala navigace "
            f"({elapsed:.1f} s, stránka {urlparse(page.url).path})."
        )
        raise RuntimeError(
            f"Po akci „{description}“ Moodle nenačetl další stránku."
        ) from error
    except PlaywrightError as error:
        log_progress(f"Akce „{description}“ selhala: {error}")
        raise
    log_progress(
        f"Stránka po akci „{description}“ je načtena "
        f"({time.monotonic() - started:.1f} s): {urlparse(page.url).path}"
    )


def click_element(locator, description: str) -> None:
    from playwright.sync_api import Error as PlaywrightError

    log_progress(f"Klikám na {description}.")
    started = time.monotonic()
    try:
        locator.click(no_wait_after=True)
    except PlaywrightError as error:
        log_progress(
            f"Kliknutí na {description} selhalo "
            f"({time.monotonic() - started:.1f} s): {error}"
        )
        raise
    log_progress(
        f"Kliknutí na {description} dokončeno "
        f"({time.monotonic() - started:.1f} s)."
    )


def navigate(page, url: str) -> None:
    from playwright.sync_api import Error as PlaywrightError

    parsed_url = urlparse(url)
    log_progress(f"Otevírám stránku {parsed_url.path}; čekám na odpověď Moodle.")
    started = time.monotonic()
    try:
        page.goto(url, wait_until="commit")
    except PlaywrightError as error:
        log_progress(
            f"Navigace na {parsed_url.path} selhala "
            f"({time.monotonic() - started:.1f} s): {error}"
        )
        raise
    log_progress(
        f"Stránka {urlparse(page.url).path} odpověděla "
        f"({time.monotonic() - started:.1f} s)."
    )


def reload_page(page, description: str) -> None:
    from playwright.sync_api import Error as PlaywrightError

    log_progress(f"Obnovuji stránku: {description}.")
    started = time.monotonic()
    try:
        page.reload(wait_until="commit")
    except PlaywrightError as error:
        log_progress(
            f"Obnovení stránky „{description}“ selhalo "
            f"({time.monotonic() - started:.1f} s): {error}"
        )
        raise
    log_progress(
        f"Stránka obnovena ({time.monotonic() - started:.1f} s): "
        f"{urlparse(page.url).path}"
    )


def wait_for_url(page, url, description: str, timeout: int = NAVIGATION_TIMEOUT_MS):
    from playwright.sync_api import Error as PlaywrightError
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

    log_progress(f"Čekám na {description} ({timeout // 1000} s).")
    started = time.monotonic()
    try:
        page.wait_for_url(url, timeout=timeout)
    except PlaywrightTimeoutError:
        log_progress(
            f"{description} se nenačetlo ({time.monotonic() - started:.1f} s, "
            f"aktuální stránka {urlparse(page.url).path})."
        )
        raise
    except PlaywrightError as error:
        log_progress(f"Navigace na {description} selhala: {error}")
        raise
    log_progress(
        f"{description} načteno ({time.monotonic() - started:.1f} s)."
    )


def login_to_moodle(page, config: dict) -> None:
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

    login_url = f"{config['base_url']}/login/index.php"
    navigate(page, login_url)

    if page.locator("body.loggedin").count() or not urlparse(page.url).path.endswith(
        "/login/index.php"
    ):
        log_progress(
            "Moodle již potvrzuje přihlášení: "
            f"{urlparse(page.url).path}"
        )
        return

    username = page.locator('input[name="username"], #username').first
    password = page.locator('input[name="password"], #password').first
    credentials_available = bool(config["username"] and config["password"])
    form_ready = False

    if credentials_available:
        try:
            wait_for_visible(
                page,
                'input[name="username"], #username',
                "pole uživatelského jména",
                timeout=15_000,
            )
        except PlaywrightTimeoutError:
            if page.locator("body.loggedin").count() or not urlparse(
                page.url
            ).path.endswith("/login/index.php"):
                log_progress(
                    "Moodle již potvrzuje přihlášení: "
                    f"{urlparse(page.url).path}"
                )
                return
            log_progress(
                "Běžné přihlašovací pole není dostupné; přihlaste se ručně "
                "přes školní SSO."
            )
        else:
            wait_for_visible(
                page,
                'input[name="password"], #password',
                "pole hesla",
                timeout=PAGE_TIMEOUT_MS,
            )
            username.fill(config["username"])
            password.fill(config["password"])
            submit = wait_for_visible(
                page,
                "#loginbtn, button[type='submit'], input[type='submit']",
                "tlačítko pro přihlášení",
                timeout=PAGE_TIMEOUT_MS,
            )
            click_element(submit, "tlačítko pro přihlášení")
            form_ready = True
    else:
        log_progress(
            "Automatické přihlášení není nakonfigurováno; přihlaste se "
            "v otevřeném okně prohlížeče."
        )

    try:
        wait_for_condition(
            page,
            "potvrzení přihlášení do Moodle",
            """() => document.body?.classList.contains('loggedin')
                || !location.pathname.endsWith('/login/index.php')""",
            timeout=LOGIN_TIMEOUT_MS,
        )
    except PlaywrightTimeoutError:
        reason = (
            "Přihlášení nebylo potvrzeno po odeslání formuláře."
            if form_ready
            else "Přihlášení nebylo potvrzeno."
        )
        raise RuntimeError(
            f"{reason} Ověřte údaje nebo dokončete přihlášení v prohlížeči."
        ) from None
    log_progress(f"Přihlášení potvrzeno: {urlparse(page.url).path}")


def load_config(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(
            f"Konfigurace {path} neexistuje. Zkopírujte "
            "moodle/e2e.example.json na moodle/e2e.local.json a doplňte URL."
        )

    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Neplatný JSON v {path}: {error}") from error

    if not isinstance(config, dict):
        raise ValueError(f"Konfigurace {path} musí být JSON objekt.")

    base_url = config.get("base_url")
    if not isinstance(base_url, str):
        raise ValueError(f"V {path} chybí textová položka 'base_url'.")
    username = config.get("username", "")
    password = config.get("password", "")
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("'username' a 'password' musí být textové hodnoty.")
    if bool(username) != bool(password):
        raise ValueError("Vyplňte zároveň 'username' i 'password', nebo obě pole nechte prázdná.")
    courses = config.get("courses", {})
    if not isinstance(courses, dict):
        raise ValueError("'courses' musí být objekt mapující třídy na ID kurzů.")

    normalized_courses: dict[str, str] = {}
    for class_name, course_id in courses.items():
        if not isinstance(class_name, str) or not class_name.strip():
            raise ValueError("Názvy tříd v 'courses' musí být neprázdné texty.")
        if isinstance(course_id, bool) or not str(course_id).isdigit() or int(course_id) < 1:
            raise ValueError(f"ID kurzu pro třídu '{class_name}' musí být kladné celé číslo.")
        normalized_courses[class_name] = str(course_id)

    parsed_url = urlparse(base_url)
    if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
        raise ValueError("'base_url' musí být úplná HTTP(S) adresa Moodle.")

    return {
        "base_url": base_url.rstrip("/"),
        "username": username,
        "password": password,
        "courses": normalized_courses,
    }


def course_year(class_name: str, explicit_year: int | None) -> int:
    match = re.match(r"\s*([1-3])", class_name)
    if not match:
        raise ValueError(
            f"Ročník nelze určit z názvu třídy '{class_name}'. "
            "Název musí začínat číslem 1, 2 nebo 3."
        )
    class_year = int(match.group(1))
    if explicit_year is not None and explicit_year != class_year:
        raise ValueError(
            f"Parametr --year {explicit_year} nesouhlasí s prvním číslem "
            f"třídy '{class_name}' ({class_year})."
        )
    return class_year


def find_task(
    year: int, lesson: int, task_number: int, *, graded: bool = False
) -> tuple[dict, str, Path]:
    lesson_root = ROOT / "lekce" / f"{year}-rocnik"
    lesson_dirs = sorted(lesson_root.glob(f"{lesson:02d}-*"))
    if len(lesson_dirs) != 1:
        raise ValueError(
            f"V repozitáři nebyla nalezena právě jedna lekce {lesson:02d} "
            f"pro {year}. ročník."
        )

    tasks_root = lesson_dirs[0] / "ukoly"
    task_prefix = "z" if graded else ""
    task_dirs = sorted(
        path
        for path in tasks_root.glob(f"{task_prefix}{task_number:02d}-*")
        if path.is_dir()
    )
    if len(task_dirs) != 1:
        task_kind = "známkovaný úkol" if graded else "běžný úkol"
        raise ValueError(
            f"V lekci {lesson:02d} nebyl nalezen právě jeden {task_kind} "
            f"{'Z' if graded else ''}{task_number:02d}."
        )

    task = load_task(task_dirs[0], secret=graded)
    if task is None:
        raise ValueError(f"Nelze načíst zadání z {task_dirs[0]}.")
    if graded:
        activity_name = f"ZNÁMKOVANÝ ÚKOL - {task['title']}"
    elif year == 3:
        prefix = f"Lekce {lesson:02d} - "
        activity_name = (
            f"{prefix}Úkol {task_number:02d} — {task['title']} "
            f"({'★' * int(task['stars'])}{'☆' * (3 - int(task['stars']))})"
        )
    else:
        activity_name = (
            f"Úkol {task_number:02d} — {task['title']} "
            f"({'★' * int(task['stars'])}{'☆' * (3 - int(task['stars']))})"
        )
    return task, activity_name, task_dirs[0]


def due_date_label(value: date) -> str:
    return f"{value.day}. {CZECH_MONTHS[value.month - 1]} {value.year}"


def task_description_html(task: dict, year: int, due_date: date) -> str:
    assignment = assignment_markdown(task, str(year))
    assignment = re.sub(r"^# .*(?:\r?\n)+", "", assignment, count=1)
    body = markdown.markdown(
        prepare_assignment_markdown(assignment),
        extensions=["tables", "fenced_code", "attr_list"],
    )
    due_date_html = (
        '<p><i class="fa fa-calendar-check-o "></i> '
        "<strong>Datum odevzdání</strong>: "
        f"{html.escape(due_date_label(due_date))}</p>"
    )
    return f"{due_date_html}\n<p><strong>Zadání:</strong></p>\n{body}"


def ensure_vpl_editor_file(page, filename: str) -> str:
    wait_for_condition(
        page,
        f"načtení VPL editoru souborů při hledání {filename}",
        """() => {
            const save = document.getElementById('vpl_ide_save');
            const tabs = document.querySelectorAll('#vpl_tabs_ul li');
            const dialog = document.querySelector(
                '.ui-dialog[aria-describedby="vpl_ide_dialog_new"]'
            );
            const dialogVisible = dialog
                && dialog.getClientRects().length > 0
                && getComputedStyle(dialog).visibility !== 'hidden';
            return !!save && (tabs.length > 0 || dialogVisible);
        }""",
        timeout=PAGE_TIMEOUT_MS,
    )
    file_tabs = page.locator("#vpl_tabs_ul li").filter(
        has_text=re.compile(rf"^\s*{re.escape(filename)}\s*$")
    )
    new_dialog = page.locator(
        '.ui-dialog[aria-describedby="vpl_ide_dialog_new"]'
    )
    if file_tabs.count() > 1:
        raise RuntimeError(f"V editoru VPL je soubor {filename} uveden vícekrát.")
    if file_tabs.count() == 0:
        if not new_dialog.is_visible():
            more_button = page.locator("#vpl_ide_more")
            wait_for_locator(more_button, "tlačítko dalších souborů VPL")
            if not new_dialog.is_visible():
                new_button = page.locator("#vpl_ide_new")
                if not new_button.is_visible():
                    click_element(more_button, "další soubory VPL")
                if not new_dialog.is_visible():
                    wait_for_locator(new_button, "tlačítko pro vytvoření souboru VPL")
                    click_element(new_button, "vytvoření nového souboru VPL")
        wait_for_locator(new_dialog, f"dialog pro vytvoření {filename}")
        new_dialog.locator("#vpl_ide_input_newfilename").fill(filename)
        confirm = new_dialog.get_by_role("button", name="OK", exact=True)
        if confirm.count() != 1:
            raise RuntimeError(
                f"V dialogu editoru VPL nebylo nalezeno potvrzení pro {filename}."
            )
        click_element(confirm, f"potvrzení vytvoření souboru {filename}")
        wait_for_condition(
            page,
            f"vytvoření souboru {filename} v editoru",
            "name => [...document.querySelectorAll('#vpl_tabs_ul li')]"
            ".filter(tab => tab.innerText.trim() === name).length === 1",
            arg=filename,
            timeout=PAGE_TIMEOUT_MS,
        )
        file_tabs = page.locator("#vpl_tabs_ul li").filter(
            has_text=re.compile(rf"^\s*{re.escape(filename)}\s*$")
        )

    editor_id = file_tabs.get_attribute("aria-controls")
    if not editor_id or not re.fullmatch(r"vpl_file\d+", editor_id):
        raise RuntimeError(f"Nelze určit editor souboru {filename}.")
    click_element(file_tabs.locator("a"), f"otevření souboru {filename}")
    wait_for_condition(
        page,
        f"inicializaci editoru ACE pro {filename}",
        "id => window.ace && document.getElementById(id) "
        "&& ace.edit(document.getElementById(id))",
        arg=editor_id,
        timeout=PAGE_TIMEOUT_MS,
    )
    return editor_id


def save_vpl_editor_file(page, filename: str, editor_id: str, content: str) -> None:
    current_content = page.evaluate(
        "id => ace.edit(document.getElementById(id)).getValue()",
        arg=editor_id,
    )
    if current_content == content:
        return
    page.evaluate(
        "({id, content}) => "
        "ace.edit(document.getElementById(id)).setValue(content)",
        {"id": editor_id, "content": content},
    )
    wait_for_condition(
        page,
        f"povolení uložení souboru {filename}",
        "!document.getElementById('vpl_ide_save')?.classList"
        ".contains('ui-button-disabled')",
        timeout=PAGE_TIMEOUT_MS,
    )
    click_element(page.locator("#vpl_ide_save"), f"uložení souboru {filename}")
    wait_for_condition(
        page,
        f"dokončení ukládání souboru {filename}",
        "document.getElementById('vpl_ide_save')?.classList"
        ".contains('ui-button-disabled')",
        timeout=PAGE_TIMEOUT_MS,
    )
    reload_page(page, f"editor souboru {filename}")
    file_tabs = page.locator("#vpl_tabs_ul li").filter(
        has_text=re.compile(rf"^\s*{re.escape(filename)}\s*$")
    )
    wait_for_condition(
        page,
        f"opětovné načtení editoru souboru {filename}",
        """() => {
            const save = document.getElementById('vpl_ide_save');
            const tabs = document.querySelectorAll('#vpl_tabs_ul li');
            const dialog = document.querySelector(
                '.ui-dialog[aria-describedby="vpl_ide_dialog_new"]'
            );
            const dialogVisible = dialog
                && dialog.getClientRects().length > 0
                && getComputedStyle(dialog).visibility !== 'hidden';
            return !!save && (tabs.length > 0 || dialogVisible);
        }""",
        timeout=PAGE_TIMEOUT_MS,
    )
    wait_for_condition(
        page,
        f"ověření existence uloženého souboru {filename}",
        "name => [...document.querySelectorAll('#vpl_tabs_ul li')]"
        ".filter(tab => tab.innerText.trim() === name).length === 1",
        arg=filename,
        timeout=PAGE_TIMEOUT_MS,
    )
    saved_editor_id = file_tabs.get_attribute("aria-controls")
    if not saved_editor_id or not re.fullmatch(r"vpl_file\d+", saved_editor_id):
        raise RuntimeError(f"Nelze ověřit uložený soubor {filename}.")
    click_element(file_tabs.locator("a"), f"ověření souboru {filename}")
    wait_for_condition(
        page,
        f"inicializaci editoru ACE pro uložený soubor {filename}",
        "id => window.ace && document.getElementById(id) "
        "&& ace.edit(document.getElementById(id))",
        arg=saved_editor_id,
        timeout=PAGE_TIMEOUT_MS,
    )
    if page.evaluate(
        "id => ace.edit(document.getElementById(id)).getValue()",
        arg=saved_editor_id,
    ) != content:
        raise RuntimeError(f"Soubor {filename} se nepodařilo uložit.")


def replace_vpl_editor_content(page, editor_id: str, content: str) -> None:
    page.locator(f"#{editor_id}").evaluate("element => ace.edit(element).focus()")
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    page.keyboard.insert_text(content)
    if page.evaluate(
        "id => ace.edit(document.getElementById(id)).getValue()",
        arg=editor_id,
    ) != content:
        raise RuntimeError("Obsah testovacího souboru se nepodařilo vyplnit.")


def configure_submission_period(
    page, start: datetime | None, end: datetime | None
) -> None:
    submission_period_toggle = page.locator(
        'a[data-bs-toggle="collapse"][href="#id_submissionperiodcontainer"]'
    )
    wait_for_locator(submission_period_toggle, "skupinu Submission period")
    if submission_period_toggle.count() != 1:
        raise RuntimeError(
            "Ve formuláři nebyla nalezena skupina „Submission period“."
        )
    if submission_period_toggle.get_attribute("aria-expanded") != "true":
        click_element(submission_period_toggle, "rozbalení Submission period")

    for field_name, value in (("startdate", start), ("duedate", end)):
        enabled = page.locator(f'input[name="{field_name}[enabled]"]')
        wait_for_locator(enabled, f"přepínač {field_name}[enabled]")
        if enabled.count() != 1:
            raise RuntimeError(
                f"Ve formuláři chybí přepínač {field_name}[enabled]."
            )
        enabled.set_checked(value is not None)
        if enabled.is_checked() != (value is not None):
            raise RuntimeError(f"Nepodařilo se nastavit období {field_name}.")
        if value is None:
            continue

        for component, component_value in (
            ("day", value.day),
            ("month", value.month),
            ("year", value.year),
            ("hour", value.hour),
        ):
            selector = page.locator(
                f'select[name="{field_name}[{component}]"]'
            )
            wait_for_locator(selector, f"pole {field_name}[{component}]")
            if selector.count() != 1:
                raise RuntimeError(
                    f"Ve formuláři chybí pole {field_name}[{component}]."
                )
            options = selector.locator("option").evaluate_all(
                "options => options.map(option => option.value)"
            )
            matching_options = [
                option
                for option in options
                if option.isdigit() and int(option) == component_value
            ]
            if not matching_options:
                raise RuntimeError(
                    f"Pole {field_name}[{component}] nenabízí hodnotu "
                    f"{component_value}."
                )
            selector.select_option(matching_options[0])
            if int(selector.input_value()) != component_value:
                raise RuntimeError(
                    f"Nepodařilo se nastavit {field_name}[{component}]."
                )

        minute_selector = page.locator(
            f'select[name="{field_name}[minute]"]'
        )
        wait_for_locator(minute_selector, f"pole {field_name}[minute]")
        if minute_selector.count() != 1:
            raise RuntimeError(
                f"Ve formuláři chybí pole {field_name}[minute]."
            )
        minute_options = minute_selector.locator("option").evaluate_all(
            "options => options.map(option => option.value)"
        )
        numeric_minutes = sorted(
            {int(option) for option in minute_options if option.isdigit()}
        )
        if not numeric_minutes:
            raise RuntimeError(
                f"Pole {field_name}[minute] nemá platné časové možnosti."
            )
        selected_minute = min(
            numeric_minutes,
            key=lambda minute: (abs(minute - value.minute), minute),
        )
        selected_minute_option = next(
            option
            for option in minute_options
            if option.isdigit() and int(option) == selected_minute
        )
        minute_selector.select_option(selected_minute_option)
        if int(minute_selector.input_value()) != selected_minute:
            raise RuntimeError(
                f"Nepodařilo se nastavit {field_name}[minute]."
            )


def configure_graded_task_access(page, available_after: datetime) -> None:
    show_description = page.locator("#id_showdescription")
    wait_for_locator(show_description, "volbu zobrazení popisu v kurzu")
    if show_description.count() != 1:
        raise RuntimeError(
            "Ve formuláři nebyla nalezena volba zobrazení popisu v kurzu."
        )
    show_description.set_checked(False)

    panel = page.locator("#id_availabilityconditionsheader")
    wait_for_locator(panel, "sekci Omezení přístupu")
    if panel.count() != 1:
        raise RuntimeError("Ve formuláři chybí sekce „Omezit přístup“.")
    toggle = panel.locator('a[data-bs-toggle="collapse"]')
    wait_for_locator(toggle, "ovládání rozbalení Omezení přístupu")
    if toggle.count() != 1:
        raise RuntimeError(
            "V sekci „Omezit přístup“ nebylo nalezeno ovládání rozbalení."
        )
    if toggle.get_attribute("aria-expanded") != "true":
        click_element(toggle, "rozbalení Omezení přístupu")
    wait_for_visible(
        page,
        "#id_availabilityconditionsheadercontainer",
        "panel Omezení přístupu",
    )

    conditions_field = page.locator("#id_availabilityconditionsjson")
    try:
        conditions = json.loads(conditions_field.input_value())
    except json.JSONDecodeError as error:
        raise RuntimeError("Omezení přístupu obsahuje neplatný JSON.") from error
    if not isinstance(conditions, dict) or conditions.get("c") != []:
        raise RuntimeError(
            "Nový známkovaný úkol již obsahuje omezení přístupu; "
            "nelze bezpečně přidat další automaticky."
        )

    add_restriction = panel.get_by_role(
        "button", name="Přidat omezení ...", exact=True
    )
    wait_for_locator(add_restriction, "tlačítko Přidat omezení")
    if add_restriction.count() != 1:
        raise RuntimeError(
            "V sekci „Omezit přístup“ nebylo nalezeno tlačítko "
            "„Přidat omezení“."
        )
    click_element(add_restriction, "Přidat omezení")
    date_option = page.locator("#availability_addrestriction_date")
    wait_for_locator(date_option, "volbu omezení Datum")
    if date_option.count() != 1:
        raise RuntimeError(
            "V nabídce „Přidat omezení“ nebyla nalezena právě jedna volba "
            "„Datum“."
        )
    click_element(date_option, "volbu omezení Datum")

    direction = panel.locator('select[name="direction"]')
    wait_for_locator(direction, "typ datumové podmínky")
    if direction.count() != 1:
        raise RuntimeError("V omezení přístupu chybí typ datumové podmínky.")
    direction.select_option(">=")
    if direction.input_value() != ">=":
        raise RuntimeError(
            "Datumové omezení přístupu se nepodařilo nastavit na „od“."
        )

    for component, component_value in (
        ("day", available_after.day),
        ("month", available_after.month),
        ("year", available_after.year),
        ("hour", available_after.hour),
        ("minute", available_after.minute),
    ):
        selector = panel.locator(f'select[name="x[{component}]"]')
        wait_for_locator(selector, f"datumové pole {component}")
        if selector.count() != 1:
            raise RuntimeError(
                f"V datumovém omezení přístupu chybí pole {component}."
            )
        options = selector.locator("option").evaluate_all(
            "options => options.map(option => option.value)"
        )
        matching_options = [
            option
            for option in options
            if option.isdigit() and int(option) == component_value
        ]
        if not matching_options:
            raise RuntimeError(
                f"Datumové omezení přístupu nenabízí hodnotu "
                f"{component_value} pro {component}."
            )
        selector.select_option(matching_options[0])
        if int(selector.input_value()) != component_value:
            raise RuntimeError(
                f"Datumové omezení přístupu se nepodařilo nastavit "
                f"({component})."
            )

    condition_visibility_toggle = panel.locator(
        ".availability-item > a.availability-eye"
    )
    wait_for_locator(
        condition_visibility_toggle, "ovládání viditelnosti datumového omezení"
    )
    if condition_visibility_toggle.count() != 1:
        raise RuntimeError(
            "U datumového omezení nelze určit, zda se omezená aktivita "
            "má skrýt."
        )
    visibility_title = condition_visibility_toggle.get_attribute("title") or ""
    if "Klepnutím skryjete" in visibility_title:
        click_element(condition_visibility_toggle, "skrytí omezené aktivity")

    try:
        conditions = json.loads(conditions_field.input_value())
    except json.JSONDecodeError as error:
        raise RuntimeError("Moodle vytvořil neplatné datumové omezení.") from error
    expected_timestamp = int(available_after.timestamp())
    if (
        not isinstance(conditions, dict)
        or conditions.get("op") != "&"
        or len(conditions.get("c", [])) != 1
        or conditions["c"][0].get("type") != "date"
        or conditions["c"][0].get("d") != ">="
        or conditions["c"][0].get("t") != expected_timestamp
        or conditions.get("showc") != [False]
    ):
        raise RuntimeError(
            "Datumové omezení se nepodařilo uložit jako skryté do "
            f"{available_after:%d.%m.%Y %H:%M} (stav: "
            f"{json.dumps(conditions, ensure_ascii=False)})."
        )


def configure_vpl_activity(
    page,
    base_url: str,
    activity_id: str,
    cases_content: str | None,
    execution_files: dict[str, str],
    requested_filename: str,
) -> None:
    if cases_content is not None:
        log_progress("Otevírám konfiguraci testovacích souborů VPL.")
        navigate(
            page,
            f"{base_url}/mod/vpl/forms/testcasesfile.php?"
            f"{urlencode({'id': activity_id})}",
        )
        log_progress("Čekám na editor testovacích souborů.")
        wait_for_condition(
            page,
            "načtení karet souborů testů",
            "document.getElementById('vpl_ide_save') "
            "&& document.querySelectorAll('#vpl_tabs a').length > 0",
            timeout=PAGE_TIMEOUT_MS,
        )
        test_tabs = page.locator("#vpl_tabs a")
        wait_for_visible(page, "#vpl_tabs a", "karta souboru testů")
        cases_tab = test_tabs.filter(
            has_text=re.compile(r"^\s*vpl_evaluate\.cases\s*$")
        )
        if cases_tab.count() != 1:
            raise RuntimeError(
                "V části „Tests configuration“ nebyl nalezen právě jeden "
                "soubor vpl_evaluate.cases."
            )
        tab_target = cases_tab.get_attribute("href")
        editor_id = tab_target.rsplit("#", 1)[-1] if tab_target and "#" in tab_target else ""
        if not re.fullmatch(r"vpl_file\d+", editor_id):
            raise RuntimeError(
                "Nelze určit editor pro soubor vpl_evaluate.cases."
            )
        click_element(cases_tab, "otevření souboru testů")
        wait_for_condition(
            page,
            "inicializaci editoru ACE pro soubor testů",
            "id => window.ace && document.getElementById(id) "
            "&& ace.edit(document.getElementById(id))",
            arg=editor_id,
            timeout=PAGE_TIMEOUT_MS,
        )
        replace_vpl_editor_content(page, editor_id, cases_content)
        wait_for_condition(
            page,
            "povolení uložení souboru testů",
            "!document.getElementById('vpl_ide_save')?.classList"
            ".contains('ui-button-disabled')",
            timeout=PAGE_TIMEOUT_MS,
        )
        click_element(page.locator("#vpl_ide_save"), "uložení souboru testů")
        wait_for_condition(
            page,
            "dokončení ukládání souboru testů",
            "document.getElementById('vpl_ide_save')?.classList"
            ".contains('ui-button-disabled')",
            timeout=PAGE_TIMEOUT_MS,
        )
        reload_page(page, "uložená konfigurace testů")
        wait_for_condition(
            page,
            "načtení uložených karet souborů testů",
            "document.getElementById('vpl_ide_save') "
            "&& document.querySelectorAll('#vpl_tabs a').length > 0",
            timeout=PAGE_TIMEOUT_MS,
        )
        cases_tab = page.locator("#vpl_tabs a").filter(
            has_text=re.compile(r"^\s*vpl_evaluate\.cases\s*$")
        )
        wait_for_condition(
            page,
            "nalezení uložené karty vpl_evaluate.cases",
            "name => [...document.querySelectorAll('#vpl_tabs a')]"
            ".filter(tab => tab.innerText.trim() === name).length === 1",
            arg="vpl_evaluate.cases",
            timeout=PAGE_TIMEOUT_MS,
        )
        tab_target = cases_tab.get_attribute("href")
        saved_editor_id = (
            tab_target.rsplit("#", 1)[-1]
            if tab_target and "#" in tab_target
            else ""
        )
        if not re.fullmatch(r"vpl_file\d+", saved_editor_id):
            raise RuntimeError(
                "Nelze znovu určit editor pro soubor vpl_evaluate.cases."
            )
        click_element(cases_tab, "ověření uloženého souboru testů")
        wait_for_condition(
            page,
            "inicializaci editoru ACE pro uložené testy",
            "id => window.ace && document.getElementById(id) "
            "&& ace.edit(document.getElementById(id))",
            arg=saved_editor_id,
            timeout=PAGE_TIMEOUT_MS,
        )
        if page.evaluate(
            "id => ace.edit(document.getElementById(id)).getValue()",
            arg=saved_editor_id,
        ) != cases_content:
            raise RuntimeError(
                "Soubor testů *.cases se v části „Tests configuration“ "
                "nepodařilo uložit."
            )

    log_progress("Otevírám nastavení Execution options.")
    navigate(
        page,
        f"{base_url}/mod/vpl/forms/executionoptions.php?"
        f"{urlencode({'id': activity_id})}",
    )
    for field in ("run", "evaluate"):
        selector = wait_for_visible(
            page,
            f"#id_{field}",
            f"volba Execution options {field}",
        )
        if selector.count() != 1:
            raise RuntimeError(
                f"V „Execution options“ nebyla nalezena volba {field}."
            )
        selector.select_option(label="Ano")
    save_options = wait_for_visible(
        page, "#id_saveoptions", "tlačítko pro uložení Execution options"
    )
    click_and_wait_for_navigation(page, save_options, "uložení Execution options")
    log_progress("Znovu ověřuji uložené Execution options.")
    navigate(
        page,
        f"{base_url}/mod/vpl/forms/executionoptions.php?"
        f"{urlencode({'id': activity_id})}",
    )
    saved_options = {}
    for field in ("run", "evaluate"):
        selector = wait_for_visible(
            page,
            f"#id_{field}",
            f"uložená volba Execution options {field}",
        )
        saved_options[field] = selector.input_value()
    if any(value != "1" for value in saved_options.values()):
        raise RuntimeError(
            "Volby Run a Evaluate se v „Execution options“ nepodařilo uložit."
        )

    log_progress("Otevírám Requested files.")
    navigate(
        page,
        f"{base_url}/mod/vpl/forms/requiredfiles.php?"
        f"{urlencode({'id': activity_id})}",
    )
    file_id = ensure_vpl_editor_file(page, requested_filename)
    if requested_filename.endswith(".py"):
        file_content = page.evaluate(
            "id => ace.edit(document.getElementById(id)).getValue()",
            arg=file_id,
        )
        if not file_content.splitlines() or file_content.splitlines()[0] != (
            "# Zde napište svůj kód"
        ):
            file_content = "# Zde napište svůj kód\n" + file_content
            save_vpl_editor_file(page, requested_filename, file_id, file_content)

    if execution_files:
        log_progress("Otevírám Execution files.")
        navigate(
            page,
            f"{base_url}/mod/vpl/forms/executionfiles.php?"
            f"{urlencode({'id': activity_id})}",
        )
        for filename, content in execution_files.items():
            editor_id = ensure_vpl_editor_file(page, filename)
            save_vpl_editor_file(page, filename, editor_id, content)


def ensure_section(
    page,
    lesson: int,
    section_title: re.Pattern,
    predecessor_title: re.Pattern,
):
    section = page.locator('li[id^="section-"]').filter(has_text=section_title)
    if section.count() == 1:
        log_progress(f"Sekce lekce {lesson:02d} byla nalezena.")
        return section
    if section.count() > 1:
        raise RuntimeError(
            f"V kurzu je více sekcí odpovídajících lekci {lesson:02d}."
        )

    if lesson == 1:
        predecessor = page.locator("#section-0")
    else:
        predecessor = page.locator('li[id^="section-"]').filter(
            has_text=predecessor_title
        )
    if predecessor.count() != 1:
        raise RuntimeError(
            f"Sekci před lekcí {lesson:02d} se nepodařilo jednoznačně "
            f"určit podle názvu „{predecessor_title.pattern}“ "
            f"(nalezeno: {predecessor.count()})."
        )
    predecessor_id = predecessor.get_attribute("id")
    predecessor_match = re.fullmatch(r"section-(\d+)", predecessor_id or "")
    if not predecessor_match:
        raise RuntimeError(
            "Nelze určit pořadí sekce před lekcí "
            f"{lesson:02d} (ID: {predecessor_id!r})."
        )
    section_number = int(predecessor_match.group(1)) + 1
    section = page.locator(f"#section-{section_number}")

    if section.count() == 1:
        log_progress(
            f"Sekce lekce {lesson:02d} existuje jako nová; připravuji její název."
        )
        quick_edit = section.locator("a.quickeditlink")
        if quick_edit.count() != 1:
            raise RuntimeError(
                f"Nelze bezpečně určit název sekce {lesson:02d}."
            )
        default_name = quick_edit.inner_text().strip()
        if default_name != "Nová sekce":
            raise RuntimeError(
                f"Sekce {lesson:02d} již existuje pod jiným názvem "
                f"„{default_name}“."
            )
        if section.locator("li.activity").count():
            raise RuntimeError(
                f"Nová sekce {lesson:02d} již obsahuje aktivity."
            )
    else:
        add_section = predecessor.locator('a[data-action="addSection"]')
        if add_section.count() != 1:
            raise RuntimeError(
                f"Sekce před lekcí {lesson:02d} nemá právě jeden odkaz "
                "pro přidání sekce."
            )
        section_url = add_section.get_attribute("href")
        if not section_url:
            raise RuntimeError("Odkaz pro přidání sekce nemá cílovou adresu.")
        log_progress(f"Vytvářím sekci pro lekci {lesson:02d}.")
        navigate(page, section_url)
        section = page.locator(f"#section-{section_number}")
        wait_for_visible(
            page,
            f"#section-{section_number}",
            f"nová sekce pro lekci {lesson:02d}",
        )

    if section.locator("li.activity").count():
        raise RuntimeError(
            f"Sekce {lesson:02d} obsahuje aktivity, nelze ji bezpečně přejmenovat."
        )
    edit_link = section.locator('a[href*="/course/editsection.php"]')
    if edit_link.count() != 1:
        raise RuntimeError(
            f"Sekce {lesson:02d} nemá právě jeden odkaz na úpravu nastavení."
        )
    edit_url = edit_link.get_attribute("href")
    if not edit_url:
        raise RuntimeError("Odkaz na nastavení sekce nemá cílovou adresu.")
    log_progress(f"Otevírám nastavení názvu sekce lekce {lesson:02d}.")
    navigate(page, edit_url)
    name_field = page.locator("#id_name")
    wait_for_visible(page, "#id_name", f"název sekce lekce {lesson:02d}")
    name_field.fill(f"Lekce {lesson:02d} - úkoly")
    submit_section = wait_for_visible(
        page,
        "#id_submitbutton",
        f"tlačítko pro uložení sekce lekce {lesson:02d}",
    )
    click_and_wait_for_navigation(
        page, submit_section, f"uložení názvu sekce lekce {lesson:02d}"
    )

    wait_for_visible(
        page,
        'li[id^="section-"]',
        f"sekce kurzu po uložení lekce {lesson:02d}",
    )
    section = page.locator('li[id^="section-"]').filter(has_text=section_title)
    if section.count() != 1:
        raise RuntimeError(
            f"Sekci lekce {lesson:02d} se nepodařilo pojmenovat "
            "nebo ověřit po uložení."
        )
    return section


def parse_task_identifier(value: str) -> tuple[int, bool, str]:
    match = re.fullmatch(r"\s*(z)?(\d+)\s*", value, re.IGNORECASE)
    if not match or int(match.group(2)) < 1:
        raise ValueError(
            "--task musí být kladné číslo běžného úkolu nebo kód "
            "známkovaného úkolu, například Z01."
        )
    graded = bool(match.group(1))
    task_number = int(match.group(2))
    task_label = f"{'Z' if graded else ''}{task_number:02d}"
    return task_number, graded, task_label


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
    parser.add_argument(
        "--lesson",
        type=int,
        required=True,
        help="číslo lekce v kurzu",
    )
    parser.add_argument(
        "--task",
        required=True,
        help="číslo běžného úkolu nebo kód známkovaného úkolu (např. Z01)",
    )
    parser.add_argument(
        "--year",
        type=int,
        choices=(1, 2, 3),
        help="ročník zdrojového úkolu (jinak se odvodí z názvu kurzu)",
    )
    parser.add_argument(
        "--pause",
        action="store_true",
        help="ponechá formulář otevřený až do zavření okna Chromium",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="uloží vyplněnou aktivitu tlačítkem „Uložit a zobrazit“",
    )
    args = parser.parse_args()
    if args.lesson < 1:
        parser.error("--lesson musí být kladné celé číslo.")
    try:
        task_number, graded_task, task_label = parse_task_identifier(args.task)
    except ValueError as error:
        parser.error(str(error))

    try:
        config = load_config(args.config)
    except (FileNotFoundError, ValueError) as error:
        parser.error(str(error))

    course_id = config["courses"].get(args.class_name)
    if course_id is None:
        parser.error(
            f"Třída '{args.class_name}' není v 'courses' nastavena v {args.config}."
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

    with sync_playwright() as playwright:
        log_progress("Spouštím Chromium a otevírám Moodle.")
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_default_timeout(PAGE_TIMEOUT_MS)
        page.set_default_navigation_timeout(NAVIGATION_TIMEOUT_MS)
        try:
            login_to_moodle(page, config)
        except (PlaywrightError, RuntimeError) as error:
            print(
                f"Nepodařilo se přihlásit do Moodle: {error}",
                file=sys.stderr,
            )
            browser.close()
            return 1

        course_url = (
            f"{config['base_url']}/course/view.php?"
            f"{urlencode({'id': course_id})}"
        )
        log_progress(f"Otevírám kurz '{args.class_name}' (ID {course_id}).")
        navigate(page, course_url)
        query = parse_qs(urlparse(page.url).query)
        if query.get("id") != [course_id]:
            print(
                f"Nepodařilo se otevřít kurz '{args.class_name}' (ID {course_id}). "
                f"Moodle přesměroval na {page.url}. Ověřte přístupová práva a ID kurzu.",
                file=sys.stderr,
            )
            browser.close()
            return 1

        wait_for_visible(
            page,
            'li[id^="section-"]',
            f"sekce kurzu '{args.class_name}'",
        )
        log_progress(f"Kurz '{args.class_name}' (ID {course_id}) je otevřen: {page.url}")

        log_progress(
            f"Načítám zadání pro {args.class_name}, lekci {args.lesson:02d}, "
            f"úkol {task_label}."
        )
        try:
            year = course_year(args.class_name, args.year)
            task, activity_name, task_directory = find_task(
                year, args.lesson, task_number, graded=graded_task
            )
        except (KeyError, TypeError, ValueError) as error:
            print(f"Chyba při načítání údajů úkolu: {error}", file=sys.stderr)
            browser.close()
            return 1

        requested_filename = task.get("soubor", "main.py")
        if (
            not isinstance(requested_filename, str)
            or not requested_filename.strip()
            or "/" in requested_filename
            or "\\" in requested_filename
        ):
            print(
                "Položka 'soubor' v ukol.yaml musí být platný název "
                "požadovaného souboru bez cesty.",
                file=sys.stderr,
            )
            browser.close()
            return 1

        case_files = sorted(task_directory.glob("*.cases"))
        if len(case_files) > 1:
            print(
                f"V {task_directory} bylo nalezeno více souborů *.cases; "
                "nelze bezpečně vybrat testovací sadu.",
                file=sys.stderr,
            )
            browser.close()
            return 1
        cases_content = None
        if case_files:
            try:
                cases_content = case_files[0].read_text(encoding="utf-8")
            except OSError as error:
                print(
                    f"Testovací soubor {case_files[0]} se nepodařilo načíst: "
                    f"{error}",
                    file=sys.stderr,
                )
                browser.close()
                return 1
            if not cases_content.strip():
                print(
                    f"Testovací soubor {case_files[0]} je prázdný.",
                    file=sys.stderr,
                )
                browser.close()
                return 1

        execution_files: dict[str, str] = {}
        for test_file in sorted(task_directory.glob("vpl_*")):
            if not test_file.is_file() or test_file.suffix == ".cases":
                continue
            try:
                content = test_file.read_text(encoding="utf-8")
            except OSError as error:
                print(
                    f"Testovací soubor {test_file} se nepodařilo načíst: {error}",
                    file=sys.stderr,
                )
                browser.close()
                return 1
            if not content.strip():
                print(
                    f"Testovací soubor {test_file} je prázdný.",
                    file=sys.stderr,
                )
                browser.close()
                return 1
            execution_files[test_file.name] = content

        submission_start = None
        submission_end = None
        access_after = None
        if graded_task:
            now = datetime.now().replace(second=0, microsecond=0)
            submission_start = now + timedelta(hours=1)
            submission_end = now + timedelta(hours=2)
            access_after = datetime.combine(
                date.today() + timedelta(days=1), datetime.min.time()
            )
            due_date = submission_end.date()
        else:
            due_date = date.today() + timedelta(days=10)
        description_html = task_description_html(task, year, due_date)
        log_progress(
            f"Načteno: {year}. ročník, lekce {args.lesson:02d}, "
            f"úkol {task_label} — {task['title']}"
        )
        log_progress(f"Datum odevzdání v popisu: {due_date_label(due_date)}")
        if graded_task:
            print(
                "Submission period: otevření "
                f"{submission_start:%d.%m.%Y %H:%M}, uzavření "
                f"{submission_end:%d.%m.%Y %H:%M} "
                "(čas lze později upravit v nastavení aktivity)."
            )
            print(
                "Omezení přístupu: aktivita i zadání budou skryté do "
                f"{access_after:%d.%m.%Y %H:%M}."
            )
        if execution_files:
            log_progress(
                "Execution files k nahrání: "
                + ", ".join(execution_files)
            )

        edit_mode = page.locator('input[name="setmode"]')
        log_progress("Zapínám režim úprav kurzu a čekám na ovládací prvky.")
        try:
            wait_for_visible(
                page,
                'input[name="setmode"]',
                "přepínač režimu úprav",
            )
            wait_for_condition(
                page,
                "inicializaci přepínače režimu úprav",
                """() => document.querySelector(
                    'input[name="setmode"][data-edit-switch-initialised="1"]'
                ) !== null""",
                timeout=EDIT_MODE_TIMEOUT_MS,
            )
            if not edit_mode.is_checked():
                log_progress("Přepínám kurz do režimu úprav.")
                edit_mode.check()
            wait_for_condition(
                page,
                "potvrzení režimu úprav kurzu",
                """() => document.querySelector('input[name="setmode"]')?.checked
                    && document.body?.classList.contains('editing')""",
                timeout=EDIT_MODE_TIMEOUT_MS,
            )
            wait_for_visible(
                page,
                "button.add-content:visible",
                "tlačítko Přidat obsah",
                timeout=EDIT_MODE_TIMEOUT_MS,
            )
        except PlaywrightTimeoutError:
            switch_state = (
                edit_mode.evaluate(
                    """element => ({
                        initialized: element.dataset.editSwitchInitialised === '1',
                        checked: element.checked,
                        editing: document.body.classList.contains('editing')
                    })"""
                )
                if edit_mode.count()
                else "přepínač nebyl nalezen"
            )
            print(
                "Nepodařilo se aktivovat režim úprav kurzu: přepínač "
                f"„Režim úprav“ nebyl inicializován nebo potvrzen "
                f"(stav: {switch_state}), případně se nezobrazilo tlačítko "
                "„Přidat obsah“.",
                file=sys.stderr,
            )
            browser.close()
            return 1

        section_title = re.compile(
            rf"Lekce\s+0?{args.lesson}\s*[-–—]\s*úkoly\b",
            re.IGNORECASE,
        )
        predecessor_title = re.compile(
            rf"Lekce\s+0?{args.lesson - 1}\s*[-–—]\s*úkoly\b",
            re.IGNORECASE,
        )
        log_progress(
            f"Hledám sekci lekce {args.lesson:02d} "
            f"(název odpovídající: {section_title.pattern}); čekám nejvýše "
            f"{PAGE_TIMEOUT_MS // 1000} s."
        )
        try:
            wait_for_condition(
                page,
                f"nalezení sekce lekce {args.lesson:02d} nebo jejího předchůdce",
                """({lesson, pattern, predecessorPattern}) => {
                    const sections = [...document.querySelectorAll(
                        'li[id^="section-"]'
                    )];
                    const target = new RegExp(pattern, 'i');
                    if (sections.some(section => target.test(section.innerText))) {
                        return true;
                    }
                    const predecessor = lesson === 1
                        ? document.querySelector('#section-0')
                        : sections.find(section =>
                            new RegExp(predecessorPattern, 'i')
                                .test(section.innerText)
                        );
                    if (!predecessor) {
                        return false;
                    }
                    const predecessorNumber = Number(
                        predecessor.id.replace('section-', '')
                    );
                    const nextSection = document.getElementById(
                        `section-${predecessorNumber + 1}`
                    );
                    const quickEdit = nextSection?.querySelector(
                        'a.quickeditlink'
                    );
                    return quickEdit?.innerText.trim() === "Nová sekce"
                        || !!predecessor.querySelector(
                            'a[data-action="addSection"]'
                        );
                }""",
                arg={
                    "lesson": args.lesson,
                    "pattern": section_title.pattern,
                    "predecessorPattern": predecessor_title.pattern,
                },
                timeout=PAGE_TIMEOUT_MS,
            )
            section = ensure_section(
                page, args.lesson, section_title, predecessor_title
            )
        except (PlaywrightError, RuntimeError) as error:
            print(
                f"Nepodařilo se připravit sekci pro lekci {args.lesson:02d}: "
                f"{error}\nAktuální URL: {page.url}",
                file=sys.stderr,
            )
            if not page.is_closed():
                try:
                    section_details = page.locator(
                        'li[id^="section-"]'
                    ).evaluate_all(
                        """sections => sections.map(section => ({
                            id: section.id,
                            text: section.innerText.trim()
                                .replace(/\\s+/g, ' ')
                                .slice(0, 160)
                        }))"""
                    )
                    print(
                        "Sekce nalezené na stránce: "
                        + json.dumps(section_details, ensure_ascii=False),
                        file=sys.stderr,
                    )
                except PlaywrightError:
                    print(
                        "Seznam sekcí se z aktuální stránky nepodařilo načíst.",
                        file=sys.stderr,
                    )
            browser.close()
            return 1
        if section.count() != 1:
            print(
                f"V kurzu nebyla nalezena právě jedna sekce pro lekci "
                f"{args.lesson} (název cílové sekce: "
                f"„{section_title.pattern}“; nalezeno: {section.count()}).",
                file=sys.stderr,
            )
            browser.close()
            return 1

        if args.save:
            existing_activity = section.locator(
                'a[href*="/mod/vpl/view.php"]'
            ).filter(has_text=re.compile(re.escape(activity_name)))
            if existing_activity.count():
                print(
                    f"Aktivita „{activity_name}“ už v cílové sekci existuje; "
                    "kvůli duplicitě nebyla vytvořena další.",
                    file=sys.stderr,
                )
                browser.close()
                return 1

        add_content = section.locator("button.add-content").last
        log_progress(
            f"Sekce lekce {args.lesson:02d} je připravená; otevírám nabídku "
            "pro přidání VPL aktivity."
        )
        try:
            wait_for_locator(
                add_content,
                "tlačítko Přidat obsah v cílové sekci",
                timeout=EDIT_MODE_TIMEOUT_MS,
            )
        except PlaywrightTimeoutError:
            print(
                f"V sekci lekce {args.lesson:02d} se nezobrazilo tlačítko "
                "„Přidat obsah“.",
                file=sys.stderr,
            )
            browser.close()
            return 1
        click_element(add_content, "Přidat obsah")
        menu_option = page.locator(
            ".dropdown-menu.show:visible"
        ).get_by_text("Aktivita nebo zdroj", exact=True)
        wait_for_locator(menu_option, "položka Aktivita nebo zdroj")
        click_element(menu_option, "Aktivita nebo zdroj")

        log_progress(
            "Vybírám aktivitu nebo zdroj a následně Virtual programming lab."
        )
        chooser = page.locator(".modal.show")
        wait_for_locator(chooser, "dialog výběru aktivity")
        vpl_option = chooser.locator(
            'a[data-action="add-chooser-option"][href*="add=vpl"]:visible'
        )
        wait_for_locator(vpl_option.first, "volba Virtual programming lab")
        if vpl_option.count() != 1:
            print(
                "V nabídce aktivit nebyla nalezena právě jedna volba "
                "Virtual programming lab "
                f"(nalezeno: {vpl_option.count()}).",
                file=sys.stderr,
            )
            browser.close()
            return 1
        log_progress(
            "Volba VPL nalezena; vybírám ji "
            f"({vpl_option.get_attribute('href')})."
        )
        click_element(vpl_option, "Virtual programming lab")
        log_progress("Kliknutí na volbu VPL odesláno.")
        add_selected = chooser.get_by_role("button", name="Přidat", exact=True)
        form_url = re.compile(r"/course/modedit\.php\?.*add=vpl")
        try:
            wait_for_condition(
                page,
                "aktivaci volby VPL v dialogu",
                """() => {
                    if (
                        location.pathname.endsWith('/course/modedit.php')
                        && new URLSearchParams(location.search).get('add') === 'vpl'
                    ) {
                        return true;
                    }
                    const button = document.querySelector('.modal.show .addoption');
                    return button && !button.disabled;
                }""",
                timeout=PAGE_TIMEOUT_MS,
            )
        except PlaywrightTimeoutError:
            try:
                chooser_state = chooser.evaluate(
                    """modal => {
                        const option = modal.querySelector(
                            'a[data-action="add-chooser-option"][href*="add=vpl"]'
                        );
                        const buttons = [...modal.querySelectorAll('button')]
                            .map(button => ({
                                text: button.innerText.trim(),
                                className: button.className,
                                disabled: button.disabled,
                                ariaDisabled: button.getAttribute('aria-disabled')
                            }));
                        return {
                            option: option ? {
                                text: option.innerText.trim(),
                                className: option.className,
                                ariaSelected: option.getAttribute('aria-selected'),
                                ariaPressed: option.getAttribute('aria-pressed'),
                                href: option.getAttribute('href'),
                                html: option.outerHTML.slice(0, 800)
                            } : null,
                            buttons,
                            checkedInputs: [...modal.querySelectorAll(
                                'input[type="radio"], input[type="checkbox"]'
                            )].map(input => ({
                                type: input.type,
                                checked: input.checked,
                                value: input.value
                            }))
                        };
                    }"""
                )
            except PlaywrightError:
                chooser_state = "dialog již není dostupný"
            print(
                "Po kliknutí na volbu VPL se neaktivovalo tlačítko „Přidat“ "
                "ani se neotevřel formulář "
                f"(aktuální URL: {page.url}). Stav dialogu: "
                f"{json.dumps(chooser_state, ensure_ascii=False)}",
                file=sys.stderr,
            )
            browser.close()
            return 1
        if form_url.search(page.url):
            log_progress(
                f"Volba VPL otevřela formulář přímo ({page.url})."
            )
        else:
            log_progress("VPL je vybráno; tlačítko „Přidat“ je aktivní.")
            click_element(add_selected, "Přidat VPL")
        log_progress("Čekám na otevření formuláře nové VPL aktivity.")
        try:
            if not form_url.search(page.url):
                wait_for_url(
                    page,
                    form_url,
                    "formulář VPL",
                    timeout=PAGE_TIMEOUT_MS,
                )
        except PlaywrightTimeoutError as error:
            raise RuntimeError(
                "Po kliknutí na „Přidat“ se neotevřel formulář VPL "
                f"(aktuální URL: {page.url})."
            ) from error
        log_progress(
            f"Formulář VPL se otevřel ({page.url}); čekám na pole názvu."
        )
        name_field = page.locator("#id_name")
        try:
            wait_for_locator(name_field, "pole názvu VPL aktivity")
        except PlaywrightTimeoutError as error:
            raise RuntimeError(
                "Stránka formuláře VPL se otevřela, ale pole názvu "
                f"#id_name není viditelné (aktuální URL: {page.url})."
            ) from error
        name_field.fill(activity_name)
        log_progress("Název vyplněn; čekám na editor zadání.")
        description_editor = page.frame_locator("#id_introeditor_ifr").locator("body")
        try:
            wait_for_locator(
                description_editor,
                "editor popisu aktivity",
                timeout=PAGE_TIMEOUT_MS,
            )
        except PlaywrightTimeoutError as error:
            raise RuntimeError(
                "Pole názvu formuláře je připravené, ale editor zadání "
                f"není viditelný (aktuální URL: {page.url})."
            ) from error
        log_progress("Editor zadání je viditelný; čekám na inicializaci TinyMCE.")
        try:
            wait_for_condition(
                page,
                "inicializaci editoru TinyMCE",
                "window.tinyMCE?.get('id_introeditor')?.initialized === true",
                timeout=PAGE_TIMEOUT_MS,
            )
        except PlaywrightTimeoutError as error:
            raise RuntimeError(
                "Editor zadání se zobrazil, ale TinyMCE se neinicializoval "
                f"(aktuální URL: {page.url})."
            ) from error
        log_progress("Vyplňuji název, zadání a nastavení odevzdání.")
        page.evaluate(
            "html => window.tinyMCE.get('id_introeditor').setContent(html)",
            description_html,
        )

        configure_submission_period(
            page, submission_start, submission_end
        )
        if access_after is not None:
            configure_graded_task_access(page, access_after)

        if page.locator("#id_name").input_value() != activity_name:
            raise RuntimeError("Název aktivity se do formuláře nepodařilo vyplnit.")
        editor_html = description_editor.inner_html()
        if (
            "Datum odevzdání" not in editor_html
            or due_date_label(due_date) not in editor_html
            or 'class="fa fa-calendar-check-o "' not in editor_html
            or "<strong>" not in editor_html
            or "&lt;p&gt;" in editor_html
        ):
            raise RuntimeError(
                "Formátovaný termín a zadání se do popisu nepodařilo vyplnit."
            )
        expected_period_enabled = graded_task
        if any(
            page.locator(f'input[name="{field}[enabled]"]').is_checked()
            != expected_period_enabled
            for field in ("startdate", "duedate")
        ):
            raise RuntimeError(
                "Období odevzdání neodpovídá typu úkolu."
            )
        if graded_task and page.locator("#id_showdescription").is_checked():
            raise RuntimeError(
                "Popis známkovaného úkolu zůstal nastavený k zobrazení "
                "na titulní straně kurzu."
            )

        if args.save:
            log_progress("Ukládám aktivitu do Moodle.")
            save_button = page.get_by_role(
                "button", name="Uložit a zobrazit", exact=True
            )
            wait_for_locator(save_button, "tlačítko Uložit a zobrazit")
            if save_button.count() != 1:
                print(
                    "Ve formuláři nebylo nalezeno právě jedno tlačítko "
                    "„Uložit a zobrazit“; aktivitu nelze uložit bezpečně.",
                    file=sys.stderr,
                )
                browser.close()
                return 1
            click_and_wait_for_navigation(
                page, save_button, "uložení aktivity VPL"
            )
            if "/course/modedit.php" in page.url:
                print(
                    "Moodle po uložení ponechal otevřený editační formulář: "
                    f"{page.url}",
                    file=sys.stderr,
                )
                browser.close()
                return 1
            wait_for_locator(
                page.get_by_text(activity_name, exact=True).first,
                "zobrazení uložené aktivity",
            )
            saved_text = page.locator("body").inner_text()
            strong_text = page.locator("strong").all_inner_texts()
            if (
                due_date_label(due_date) not in saved_text
                or "Datum odevzdání" not in strong_text
                or "Zadání:" not in strong_text
                or page.locator(
                    "div.box.py-3.generalbox > div.no-overflow"
                )
                .filter(has_text="Datum odevzdání")
                .locator("i.fa.fa-calendar-check-o")
                .count()
                != 1
            ):
                raise RuntimeError(
                    "Uložená aktivita nezobrazuje správně formátovaný termín "
                    "nebo zadání."
                )
            activity_id_match = re.search(r"[?&]id=(\d+)", page.url)
            if not activity_id_match:
                raise RuntimeError(
                    f"Po uložení nelze z adresy určit ID aktivity: {page.url}"
                )
            configure_vpl_activity(
                page,
                config["base_url"],
                activity_id_match.group(1),
                cases_content,
                execution_files,
                requested_filename,
            )
            log_progress("Ověřuji aktivitu v cílové sekci kurzu.")
            navigate(page, course_url)
            wait_for_visible(
                page,
                'li[id^="section-"]',
                f"sekce kurzu '{args.class_name}' po uložení",
            )
            section = page.locator('li[id^="section-"]').filter(
                has_text=section_title
            )
            activity_link = section.locator(
                'a[href*="/mod/vpl/view.php"]'
            ).filter(has_text=re.compile(re.escape(activity_name)))
            if activity_link.count() != 1:
                raise RuntimeError(
                    "Uložená aktivita nebyla nalezena právě jednou "
                    f"v sekci lekce {args.lesson:02d}."
                )
            print(
                    f"Aktivita uložena, nakonfigurována a ověřena v sekci "
                    f"lekce {args.lesson:02d}: "
                    f"{activity_name}. Datum odevzdání: {due_date_label(due_date)}."
                )
        else:
            print(
                f"Vyplněn formulář VPL pro lekci {args.lesson:02d}, "
                f"úkol {task_label}. Datum odevzdání: "
                f"{due_date_label(due_date)}. "
                + (
                    "Období odevzdání nastaveno podle známkovaného úkolu. "
                    if graded_task
                    else "Období odevzdání vypnuto. "
                )
                + f"Formulář nebyl uložen: {page.url}"
            )
        if args.pause:
            print("Formulář zůstává otevřený. Pro ukončení zavřete okno Chromium.")
            try:
                page.wait_for_event("close", timeout=30 * 60 * 1000)
            except PlaywrightTimeoutError:
                print("Časový limit vypršel, zavírám prohlížeč.")
        browser.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
