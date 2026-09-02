#!/usr/bin/env python3
"""Generuje HTML grafický výstup z Markdown lekcí do graficky-vystup/<rocnik>/."""

from __future__ import annotations

import html as html_module
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import TextLexer, get_lexer_by_name

ROOT = Path(__file__).resolve().parent.parent
LEKCE_ROOT = ROOT / "lekce"
KURIKULUM_DIR = ROOT / "kurikulum"
VYSTUP_DIR = ROOT / "graficky-vystup"
FAVICON_SRC = ROOT / "assets" / "favicon.svg"

ROCNIKY = ("1-rocnik", "2-rocnik", "3-rocnik")
AUTHOR = "Ing. Jaroslav Moravec"

CSS = """
:root {
  --bg: #f8f9fb;
  --surface: #ffffff;
  --text: #1a1d26;
  --muted: #5c6370;
  --accent: #2563eb;
  --accent-soft: #eff6ff;
  --border: #e5e7eb;
  --code-bg: #0f172a;
  --code-text: #e2e8f0;
  --radius: 10px;
  --font: "Segoe UI", system-ui, -apple-system, sans-serif;
  --mono: "Cascadia Code", "Consolas", monospace;
  --sidebar-width: 384px;
  --content-max: 72rem;
  --backdrop: rgba(15, 23, 42, 0.45);
  --lineno-bg: #0b1220;
  --lineno-text: #64748b;
  --lineno-border: #1e293b;
}

html[data-theme="dark"] {
  color-scheme: dark;
  --bg: #0f1419;
  --surface: #1a2332;
  --text: #e8eaed;
  --muted: #94a3b8;
  --accent: #60a5fa;
  --accent-soft: #1e3a5f;
  --border: #2d3748;
  --code-bg: #0b1220;
  --code-text: #e2e8f0;
  --backdrop: rgba(0, 0, 0, 0.55);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  line-height: 1.65;
}

.layout {
  display: grid;
  grid-template-columns: var(--sidebar-width) minmax(0, 1fr);
  min-height: 100vh;
}

.sidebar {
  background: var(--surface);
  border-right: 1px solid var(--border);
  padding: 1.5rem 1.25rem;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}

.mobile-bar {
  display: none;
  align-items: center;
  gap: 0.75rem;
  padding: 0.65rem 1rem;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 900;
}

.mobile-bar-title {
  font-size: 0.95rem;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.nav-toggle {
  flex-shrink: 0;
  width: 2.5rem;
  height: 2.5rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 4px;
  padding: 0;
}

.nav-toggle span {
  display: block;
  width: 1.15rem;
  height: 2px;
  background: var(--text);
  border-radius: 1px;
  transition: transform 0.2s ease, opacity 0.2s ease;
}

body.nav-open .nav-toggle span:nth-child(1) {
  transform: translateY(6px) rotate(45deg);
}

body.nav-open .nav-toggle span:nth-child(2) {
  opacity: 0;
}

body.nav-open .nav-toggle span:nth-child(3) {
  transform: translateY(-6px) rotate(-45deg);
}

.sidebar-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  background: var(--backdrop);
  z-index: 1000;
  border: none;
  padding: 0;
  cursor: pointer;
}

body.nav-open .sidebar-backdrop {
  display: block;
}

.sidebar h1 {
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.sidebar .sub {
  font-size: 0.8rem;
  color: var(--muted);
  margin-bottom: 0.25rem;
}

.sidebar .author {
  font-size: 0.78rem;
  color: var(--muted);
  margin-bottom: 1.25rem;
}

.sidebar nav a {
  display: block;
  padding: 0.45rem 0.75rem;
  border-radius: 6px;
  color: var(--text);
  text-decoration: none;
  font-size: 0.9rem;
  line-height: 1.35;
  margin-bottom: 2px;
}

.sidebar nav a:hover { background: var(--bg); }
.sidebar nav a.active {
  background: var(--accent-soft);
  color: var(--accent);
  font-weight: 600;
}

.sidebar nav a .num {
  color: var(--muted);
  font-size: 0.75rem;
  margin-right: 0.35rem;
}

.sidebar .rocnik-switch {
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border);
  font-size: 0.78rem;
  color: var(--muted);
}

.sidebar .rocnik-switch a {
  font-size: 0.82rem;
  padding: 0.35rem 0.65rem;
}

.theme-switch {
  margin-bottom: 1rem;
}

.theme-toggle {
  display: inline-flex;
  align-items: center;
  padding: 0;
  border: 1px solid var(--border);
  border-radius: 999px;
  background: var(--bg);
  cursor: pointer;
  line-height: 0;
}

.theme-toggle:hover {
  border-color: var(--accent);
}

.theme-track {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  width: 4.25rem;
  height: 2rem;
  padding: 0.2rem;
}

.theme-thumb {
  position: absolute;
  top: 0.2rem;
  left: 0.2rem;
  width: calc(50% - 0.2rem);
  height: calc(100% - 0.4rem);
  border-radius: 999px;
  background: var(--surface);
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.12);
  transition: transform 0.22s ease;
  pointer-events: none;
}

html[data-theme="dark"] .theme-thumb {
  transform: translateX(100%);
}

.theme-icon {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--muted);
  transition: color 0.2s ease;
}

.theme-icon svg {
  display: block;
  width: 1rem;
  height: 1rem;
}

html:not([data-theme="dark"]) .theme-sun { color: var(--accent); }
html[data-theme="dark"] .theme-moon { color: var(--accent); }

.theme-toggle-compact {
  flex-shrink: 0;
  margin-left: auto;
}

.theme-toggle-compact .theme-track {
  width: 3.75rem;
  height: 1.85rem;
}

.main {
  padding: 2rem clamp(1.5rem, 3vw, 3rem) 4rem;
  min-width: 0;
  width: 100%;
  max-width: var(--content-max);
  margin-inline: 0 auto;
}

.breadcrumb {
  font-size: 0.85rem;
  color: var(--muted);
  margin-bottom: 1rem;
}

.breadcrumb a { color: var(--accent); text-decoration: none; }

.hero {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.75rem 2rem;
  margin-bottom: 1.5rem;
}

.hero h1 {
  font-size: 1.85rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 0.5rem;
}

.hero .meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.badge {
  font-size: 0.75rem;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  background: var(--accent-soft);
  color: var(--accent);
  font-weight: 600;
}

.tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.tab {
  padding: 0.5rem 1rem;
  border-radius: 8px;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  border: 1px solid var(--border);
  background: var(--surface);
  color: var(--text);
}

.tab.active {
  background: var(--accent);
  color: white;
  border-color: var(--accent);
}

.content {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 2rem 2.25rem;
}

.index-intro {
  margin-bottom: 1.75rem;
}

.index-heading {
  font-size: 1.2rem;
  font-weight: 700;
  margin: 0 0 0.15rem;
}

.content h2 {
  font-size: 1.35rem;
  margin: 2rem 0 0.75rem;
  padding-bottom: 0.35rem;
  border-bottom: 1px solid var(--border);
}

.content h2:first-child { margin-top: 0; }

.content h3 { font-size: 1.1rem; margin: 1.5rem 0 0.5rem; }

.content p { margin: 0.75rem 0; }

.content img {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 1.25rem auto;
  border-radius: var(--radius);
  border: 1px solid var(--border);
}

.content svg.diagram {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 1.25rem auto;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  overflow: hidden;
  background: var(--bg);
}

.content svg.diagram.themed .d-bg { fill: var(--bg); stroke: var(--border); }
.content svg.diagram.themed .d-surface { fill: var(--surface); stroke: var(--accent); }
.content svg.diagram.themed .d-soft { fill: var(--accent-soft); stroke: var(--accent); }
.content svg.diagram.themed .d-text { fill: var(--text); }
.content svg.diagram.themed .d-muted { fill: var(--muted); }
.content svg.diagram.themed .d-accent { fill: var(--accent); }
.content svg.diagram.themed .d-stroke-accent { stroke: var(--accent); fill: none; }
.content svg.diagram.themed .d-stroke-muted { stroke: var(--muted); fill: none; }
.content svg.diagram.themed .d-stroke-border { stroke: var(--border); fill: none; }

html[data-theme="dark"] .content img[src$=".svg"],
html[data-theme="dark"] .content svg.diagram:not(.themed) {
  filter: invert(0.9) hue-rotate(180deg) saturate(0.75) brightness(1.05);
}

.content ul, .content ol {
  margin: 0.75rem 0 0.75rem 1.5rem;
}

.content li { margin: 0.25rem 0; }

.content table:not(.highlighttable) {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 0.92rem;
}

.table-scroll {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 1rem 0;
}

.table-scroll table:not(.highlighttable) {
  margin: 0;
}

.content table:not(.highlighttable) th,
.content table:not(.highlighttable) td {
  border: 1px solid var(--border);
  padding: 0.55rem 0.75rem;
  text-align: left;
}

.content table:not(.highlighttable) th {
  background: var(--bg);
  font-weight: 600;
}

.content code {
  font-family: var(--mono);
  font-size: 0.88em;
  background: var(--bg);
  padding: 0.15rem 0.35rem;
  border-radius: 4px;
  font-variant-ligatures: none;
  font-feature-settings: "liga" 0, "calt" 0;
}

.content .code-block {
  margin: 1rem 0;
  border-radius: 8px;
  overflow-x: auto;
  background: var(--code-bg);
}

.content .code-block .highlight {
  margin: 0;
  background: transparent;
}

.content .highlighttable {
  width: 100%;
  border-collapse: collapse;
  margin: 0;
  font-family: var(--mono);
  font-size: 0.85rem;
  line-height: 1.5;
  font-variant-ligatures: none;
  font-feature-settings: "liga" 0, "calt" 0;
}

.content .highlighttable .linenos {
  width: 1%;
  padding: 1rem 0.85rem 1rem 1rem;
  background: var(--lineno-bg);
  color: var(--lineno-text);
  text-align: right;
  vertical-align: top;
  user-select: none;
  border-right: 1px solid var(--lineno-border);
}

.content .highlighttable .linenos pre {
  margin: 0;
  background: transparent;
  color: inherit;
  padding: 0;
  line-height: 1.5;
}

.content .highlighttable td.code {
  padding: 0;
  width: 100%;
  vertical-align: top;
}

.content .highlighttable td.code pre {
  margin: 0;
  padding: 1rem 1.15rem;
  background: transparent;
  overflow-x: auto;
  line-height: 1.5;
}

.content .highlight code {
  font-family: inherit;
  font-size: inherit;
  background: none;
  padding: 0;
  border-radius: 0;
  color: inherit;
}

.content hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 1.5rem 0;
}

.content a { color: var(--accent); }

.content blockquote {
  border-left: 3px solid var(--accent);
  padding-left: 1rem;
  color: var(--muted);
  margin: 1rem 0;
}

.content details.reseni {
  margin: 0.75rem 0 1.25rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--bg);
  overflow: hidden;
}

.content details.reseni summary {
  cursor: pointer;
  padding: 0.7rem 1rem;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--accent);
  list-style: none;
  user-select: none;
}

.content details.reseni summary::-webkit-details-marker { display: none; }

.content details.reseni summary::before {
  content: "▸ ";
  display: inline-block;
  width: 1.1em;
}

.content details.reseni[open] summary::before { content: "▾ "; }

.content details.reseni[open] summary {
  border-bottom: 1px solid var(--border);
  background: var(--accent-soft);
}

.content details.reseni .reseni-body {
  padding: 1rem 1.15rem 0.25rem;
}

.content details.reseni .reseni-body > :first-child { margin-top: 0; }
.content details.reseni .reseni-body > :last-child { margin-bottom: 0.5rem; }

.index-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1rem;
  margin-top: 1.5rem;
}

.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.25rem;
  text-decoration: none;
  color: inherit;
  transition: border-color 0.15s;
}

.card:hover { border-color: var(--accent); }

.card .num {
  font-size: 0.75rem;
  color: var(--accent);
  font-weight: 700;
}

.card h3 {
  font-size: 1rem;
  margin: 0.35rem 0 0.25rem;
}

.card p {
  font-size: 0.82rem;
  color: var(--muted);
}

.card.muted {
  opacity: 0.85;
  pointer-events: none;
}

.footer {
  margin-top: 2rem;
  font-size: 0.8rem;
  color: var(--muted);
}

.empty-state {
  background: var(--surface);
  border: 1px dashed var(--border);
  border-radius: var(--radius);
  padding: 2rem;
  color: var(--muted);
  margin-top: 1.5rem;
}

@media (max-width: 900px) {
  .mobile-bar { display: flex; }

  .layout {
    display: block;
    min-height: auto;
  }

  .sidebar {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    width: min(88vw, 320px);
    height: 100%;
    max-height: 100dvh;
    transform: translateX(-105%);
    transition: transform 0.22s ease;
    z-index: 1001;
    box-shadow: none;
  }

  body.nav-open .sidebar {
    transform: translateX(0);
    box-shadow: 4px 0 24px rgba(15, 23, 42, 0.12);
  }

  body.nav-open {
    overflow: hidden;
  }

  .main {
    padding: 1rem 1rem 3rem;
    max-width: none;
    margin-inline: 0;
  }

  .hero {
    padding: 1.25rem 1rem;
    margin-bottom: 1rem;
  }

  .hero h1 {
    font-size: 1.35rem;
    line-height: 1.3;
  }

  .content {
    padding: 1.15rem 1rem;
  }

  .content h2 { font-size: 1.15rem; }

  .content h3 { font-size: 1rem; }

  .tabs { gap: 0.35rem; }

  .tab {
    flex: 1 1 calc(33% - 0.35rem);
    min-width: 0;
    text-align: center;
    font-size: 0.82rem;
    padding: 0.45rem 0.5rem;
  }

  .index-grid {
    grid-template-columns: 1fr;
  }

  .content table:not(.highlighttable) {
    font-size: 0.82rem;
  }

  .content table:not(.highlighttable) th,
  .content table:not(.highlighttable) td {
    padding: 0.4rem 0.5rem;
  }

  .content .highlighttable {
    font-size: 0.78rem;
  }

  .content .highlighttable .linenos {
    padding: 0.75rem 0.5rem 0.75rem 0.65rem;
  }

  .content .highlighttable td.code pre {
    padding: 0.75rem 0.65rem;
  }

  .badge {
    font-size: 0.7rem;
  }
}
"""


NAV_JS = """(() => {
  const STORAGE_KEY = "course-theme";

  const applyTheme = (theme) => {
    const dark = theme === "dark";
    document.documentElement.setAttribute("data-theme", dark ? "dark" : "light");
    document.querySelectorAll(".theme-toggle").forEach((button) => {
      button.setAttribute("aria-checked", dark ? "true" : "false");
      button.setAttribute(
        "aria-label",
        dark ? "Přepnout světlý režim" : "Přepnout tmavý režim"
      );
    });
  };

  const getStoredTheme = () => {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch {
      return null;
    }
  };

  const saveTheme = (theme) => {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch {
      /* ignore */
    }
  };

  document.querySelectorAll(".theme-toggle").forEach((button) => {
    button.addEventListener("click", () => {
      const next = document.documentElement.getAttribute("data-theme") === "dark"
        ? "light"
        : "dark";
      applyTheme(next);
      saveTheme(next);
    });
  });

  const stored = getStoredTheme();
  if (stored === "dark" || stored === "light") {
    applyTheme(stored);
  }

  const toggle = document.querySelector(".nav-toggle");
  const sidebar = document.getElementById("site-sidebar");
  const backdrop = document.querySelector(".sidebar-backdrop");
  if (!toggle || !sidebar) return;

  const setOpen = (open) => {
    document.body.classList.toggle("nav-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Zavřít menu" : "Otevřít menu");
    if (backdrop) backdrop.hidden = !open;
  };

  toggle.addEventListener("click", () => {
    setOpen(!document.body.classList.contains("nav-open"));
  });

  backdrop?.addEventListener("click", () => setOpen(false));

  sidebar.querySelectorAll("nav a").forEach((link) => {
    link.addEventListener("click", () => setOpen(false));
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setOpen(false);
  });

  window.matchMedia("(min-width: 901px)").addEventListener("change", (event) => {
    if (event.matches) setOpen(false);
  });
})();
"""

THEME_INIT_SCRIPT = """<script>
(function(){try{var t=localStorage.getItem("course-theme");if(t==="dark")document.documentElement.setAttribute("data-theme","dark");else if(t==="light")document.documentElement.setAttribute("data-theme","light");}catch(e){}})();
</script>"""


RESENI_PATTERN = re.compile(r"@reseni\s*\n(.*?)\n@end", re.DOTALL)
RESENI_MARKER = "RESENI_PLACEHOLDER_{}"

CODE_BLOCK_RE = re.compile(
    r'<pre><code(?: class="language-([^"]+)")?>([\s\S]*?)</code></pre>',
    re.IGNORECASE,
)

LANG_ALIASES = {
    "py": "python",
    "sh": "bash",
    "shell": "bash",
    "js": "javascript",
    "yml": "yaml",
    "htm": "html",
}

PYGMENTS_FORMATTER = HtmlFormatter(
    style="monokai",
    cssclass="highlight",
    linenos="table",
    anchorlinenos=False,
    wrapcode=True,
)


@dataclass
class RocnikContext:
    slug: str
    num: int
    label: str
    lekce_dir: Path
    vystup_dir: Path
    kurikulum: dict[str, str] = field(default_factory=dict)
    lessons: list[Path] = field(default_factory=list)


def _render_md_fragment(text: str) -> str:
    return markdown.markdown(
        text,
        extensions=[TableExtension(), FencedCodeExtension()],
    )


def _reseni_details(inner_md: str) -> str:
    inner = _render_md_fragment(inner_md.strip())
    return (
        '<details class="reseni">'
        "<summary>Zobrazit řešení</summary>"
        f'<div class="reseni-body">{inner}</div>'
        "</details>"
    )


IMG_SVG_RE = re.compile(
    r"<img([^>]*?)src=\"(diagramy/[^\"]+\.svg)\"([^>]*?)/?>",
    re.IGNORECASE,
)


def _html_attr(attrs: str, name: str) -> str:
    match = re.search(rf'{name}="([^"]*)"', attrs, re.IGNORECASE)
    return match.group(1) if match else ""


def inline_diagram_svgs(html: str, vystup_dir: Path) -> str:
    """Vloží lokální SVG do HTML, aby převzala barvy světlého/tmavého režimu."""

    def repl(match: re.Match[str]) -> str:
        before, src, after = match.group(1), match.group(2), match.group(3)
        path = vystup_dir / Path(*src.split("/"))
        if not path.is_file():
            return match.group(0)
        svg = path.read_text(encoding="utf-8")
        svg = re.sub(r"<\?xml[^?]*\?>", "", svg).strip()
        stem = re.sub(r"[^a-zA-Z0-9_-]+", "-", path.stem)
        svg = re.sub(
            r'id="([^"]+)"',
            lambda m: f'id="{stem}-{m.group(1)}"',
            svg,
        )
        svg = svg.replace("url(#", f"url(#{stem}-")
        themed = 'class="d-' in svg or "class='d-" in svg
        cls = "diagram themed" if themed else "diagram"
        svg = re.sub(r"<svg\b", f'<svg class="{cls}"', svg, count=1)
        alt = _html_attr(before + after, "alt")
        if alt and "aria-label" not in svg:
            svg = re.sub(
                r"<svg\b",
                f'<svg aria-label="{html_module.escape(alt)}"',
                svg,
                count=1,
            )
        return svg

    return IMG_SVG_RE.sub(repl, html)


def md_to_html(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)

    blocks: list[str] = []

    def hold_reseni(match: re.Match[str]) -> str:
        blocks.append(_reseni_details(match.group(1)))
        return f"\n\n{RESENI_MARKER.format(len(blocks) - 1)}\n\n"

    text = RESENI_PATTERN.sub(hold_reseni, text)
    html = _render_md_fragment(text)

    for i, block in enumerate(blocks):
        marker = RESENI_MARKER.format(i)
        html = html.replace(f"<p>{marker}</p>", block)
        html = html.replace(marker, block)

    return html


def _code_lexer(lang: str | None) -> TextLexer:
    if lang:
        normalized = LANG_ALIASES.get(lang.lower(), lang.lower())
        try:
            return get_lexer_by_name(normalized, stripall=True)
        except Exception:
            pass
    return TextLexer()


def enhance_code_blocks(html: str) -> str:
    def replace(match: re.Match[str]) -> str:
        lang = match.group(1)
        code = html_module.unescape(match.group(2))
        code = code.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")
        lexer = _code_lexer(lang)
        highlighted = highlight(code, lexer, PYGMENTS_FORMATTER)
        return f'<div class="code-block">{highlighted}</div>'

    return CODE_BLOCK_RE.sub(replace, html)


def wrap_content_tables(html: str) -> str:
    return re.sub(
        r"(<table(?![^>]*class=\"highlighttable\")[^>]*>[\s\S]*?</table>)",
        r'<div class="table-scroll">\1</div>',
        html,
    )


def build_styles_css() -> str:
    pygments_css = PYGMENTS_FORMATTER.get_style_defs(".highlight")
    return f"{CSS.strip()}\n\n/* Pygments (Monokai) */\n{pygments_css}\n"


def postprocess_student_html(html: str) -> str:
    """Odstraní učitelské odkazy (.md, zdroje) — výstup pro žáky."""

    html = re.sub(
        r'href="\.\./\.\./(\d-rocnik)/(\d{2}-[a-z0-9-]+)/lekce\.md"',
        r'href="../\1/\2.html"',
        html,
    )
    html = re.sub(
        r'href="\.\./(\d{2}-[a-z0-9-]+)/lekce\.md"',
        r'href="\1.html"',
        html,
    )

    def filter_blockquote(match: re.Match[str]) -> str:
        block = match.group(0)
        if re.search(
            r"zdroje|zdroj:|\.docx|\.pptx|původní úkol|migrováno|migrován",
            block,
            re.I,
        ):
            return ""
        return block

    html = re.sub(r"<blockquote>[\s\S]*?</blockquote>", filter_blockquote, html)
    html = re.sub(r"\s*<em>\([^)]*migrováno[^)]*\)</em>", "", html, flags=re.I)
    html = re.sub(r"<p>→ viz <code>[^<]+</code></p>\s*", "", html)
    html = re.sub(r"→ viz <code>[^<]+</code>", "", html)
    html = re.sub(r"<p>→ viz `[^`]+`</p>\s*", "", html)
    html = re.sub(r"→ viz `[^`]+`", "", html)
    html = re.sub(r"(<code[^>]*>[^<]*?)\.md(</code>)", r"\1\2", html)
    html = re.sub(r'<a href="[^"]*kurikulum[^"]*">[^<]*</a>', "", html)
    html = re.sub(r'<a href="[^"]*\.yaml">[^<]*</a>', "", html)
    html = re.sub(r"<p>VPL test:[^<]*</p>\s*", "", html)
    html = re.sub(r"`ukoly/[^`]+`", "", html)
    html = enhance_code_blocks(html)
    html = wrap_content_tables(html)

    return html


OBTIZNOST_LABELS = {
    "zacatecnik": "Začátečník",
    "stredni": "Střední",
    "pokrocily": "Pokročilý",
}


def format_obtiznost(value: str) -> str:
    key = value.strip().lower()
    return OBTIZNOST_LABELS.get(key, value)


def format_lesson_hours(hodiny: str, *, card: bool = False) -> str:
    raw = (hodiny or "").strip()
    if raw in ("0", "0h"):
        return "bonus"
    if not raw:
        return "?"
    return f"{raw} hod" if card else f"{raw} h"


def parse_meta(meta_path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not meta_path.exists():
        return data
    for line in meta_path.read_text(encoding="utf-8").splitlines():
        if ":" in line and not line.strip().startswith("#"):
            key, _, val = line.partition(":")
            data[key.strip()] = val.strip()
    return data


def parse_kurikulum(rocnik_slug: str) -> dict[str, str]:
    path = KURIKULUM_DIR / f"{rocnik_slug}.yaml"
    data: dict[str, str] = {}
    if not path.exists():
        return data

    in_hodiny = False
    in_moduly = False
    modul_pending = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("hodiny:"):
            in_hodiny = True
            in_moduly = False
            modul_pending = False
            continue
        if stripped.startswith("moduly:"):
            in_moduly = True
            in_hodiny = False
            modul_pending = False
            continue
        if in_hodiny and ":" in stripped:
            key, _, val = stripped.partition(":")
            data[f"hodiny_{key.strip()}"] = val.strip()
            continue
        if in_moduly and stripped.startswith("- id:"):
            modul_pending = True
            continue
        if in_moduly and modul_pending and stripped.startswith("nazev:"):
            _, _, val = stripped.partition("nazev:")
            data["modul_nazev"] = val.strip()
            in_moduly = False
            continue
        if re.match(r"^\w+:", stripped):
            in_hodiny = False
            in_moduly = False
            modul_pending = False
            key, _, val = stripped.partition(":")
            data[key.strip()] = val.strip()
    return data


def lesson_dirs(lekce_dir: Path) -> list[Path]:
    if not lekce_dir.is_dir():
        return []
    dirs = [d for d in lekce_dir.iterdir() if d.is_dir() and re.match(r"\d{2}-", d.name)]
    return sorted(dirs, key=lambda p: p.name)


def expected_lesson_html_names(lesson_dir: Path) -> set[str]:
    """Soubory HTML, které build pro lekci vytváří."""
    lid = lesson_dir.name
    names = {f"{lid}.html"}
    if (lesson_dir / "cviceni.md").is_file():
        names.add(f"{lid}-cviceni.html")
    ukoly_root = lesson_dir / "ukoly"
    if ukoly_root.is_dir() and any(
        (p / "ukol.yaml").is_file() for p in ukoly_root.iterdir() if p.is_dir()
    ):
        names.add(f"{lid}-ukoly.html")
    return names


def cleanup_stale_lesson_html(ctx: RocnikContext) -> None:
    """Odstraní HTML lekcí, které už v MD zdrojích neexistují (např. po přejmenování složky)."""
    if not ctx.vystup_dir.is_dir():
        return
    expected: set[str] = {"index.html"}
    for lesson_dir in ctx.lessons:
        expected |= expected_lesson_html_names(lesson_dir)
    for path in ctx.vystup_dir.glob("*.html"):
        if path.name not in expected:
            path.unlink()
    diagramy_root = ctx.vystup_dir / "diagramy"
    if diagramy_root.is_dir():
        expected_diagram_dirs = {d.name for d in ctx.lessons}
        for child in diagramy_root.iterdir():
            if child.is_dir() and child.name not in expected_diagram_dirs:
                shutil.rmtree(child, ignore_errors=True)


def rocnik_label(num: int) -> str:
    return f"{num}. ročník"


def rocnik_tema(ctx: RocnikContext) -> str:
    k = ctx.kurikulum
    return k.get("nazev") or k.get("modul_nazev") or ctx.label


def rocnik_jazyk(ctx: RocnikContext) -> str:
    return ctx.kurikulum.get("jazyk", "Python" if ctx.num <= 2 else "HTML/CSS")


def rocnik_uvod_html(ctx: RocnikContext) -> str:
    path = ctx.lekce_dir / "uvod.md"
    if not path.is_file():
        return ""
    html = postprocess_student_html(md_to_html(path.read_text(encoding="utf-8")))
    return f'<article class="content index-intro">{html}</article>'


def total_hours(lessons: list[Path]) -> int:
    total = 0
    for d in lessons:
        hodiny = parse_meta(d / "meta.yaml").get("hodiny", "0")
        try:
            total += int(hodiny)
        except ValueError:
            pass
    return total


def css_href(ctx: RocnikContext) -> str:
    return "../styles.css"


def js_href(ctx: RocnikContext | None) -> str:
    return "../nav.js" if ctx else "nav.js"


def favicon_href(ctx: RocnikContext | None) -> str:
    return "../favicon.svg" if ctx else "favicon.svg"


THEME_ICONS = """<span class="theme-icon theme-sun" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg></span>
        <span class="theme-thumb" aria-hidden="true"></span>
        <span class="theme-icon theme-moon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg></span>"""


def theme_toggle_html(*, compact: bool = False) -> str:
    cls = "theme-toggle theme-toggle-compact" if compact else "theme-toggle"
    wrap_open = "" if compact else '<div class="theme-switch">'
    wrap_close = "" if compact else "</div>"
    return f"""{wrap_open}<button type="button" class="{cls}" role="switch" aria-checked="false" aria-label="Přepnout tmavý režim">
        <span class="theme-track">{THEME_ICONS}</span>
      </button>{wrap_close}"""


def layout_html(sidebar_inner: str, body: str) -> str:
    return f"""  <button type="button" class="sidebar-backdrop" hidden aria-label="Zavřít menu"></button>
  <header class="mobile-bar">
    <button type="button" class="nav-toggle" aria-label="Otevřít menu" aria-expanded="false" aria-controls="site-sidebar">
      <span></span><span></span><span></span>
    </button>
    <span class="mobile-bar-title">Kurz programování</span>
    {theme_toggle_html(compact=True)}
  </header>
  <div class="layout">
    <aside class="sidebar" id="site-sidebar">
      {sidebar_inner}
    </aside>
    <main class="main">
      {body}
    </main>
  </div>"""


def document_shell(
    title: str,
    sidebar_inner: str,
    body: str,
    *,
    ctx: RocnikContext | None = None,
    page_title: str | None = None,
) -> str:
    window_title = page_title or f"{title} — Kurz programování"
    return f"""<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="{AUTHOR}">
  <title>{window_title}</title>
  <link rel="icon" href="{favicon_href(ctx)}" type="image/svg+xml">
  <link rel="stylesheet" href="{css_href(ctx) if ctx else "styles.css"}">
  {THEME_INIT_SCRIPT}
</head>
<body>
{layout_html(sidebar_inner, body)}
  <script src="{js_href(ctx)}"></script>
</body>
</html>"""


def rocnik_switch_html(ctx: RocnikContext) -> str:
    links = []
    for slug in ROCNIKY:
        num = int(slug[0])
        label = rocnik_label(num)
        if slug == ctx.slug:
            links.append(f"<strong>{label}</strong>")
        else:
            links.append(f'<a href="../{slug}/index.html">{label}</a>')
    return (
        '<div class="rocnik-switch">'
        "<div>Ročníky</div>"
        + "".join(f"<div>{link}</div>" for link in links)
        + '<div style="margin-top:0.75rem"><a href="../index.html">← Všechny ročníky</a></div>'
        "</div>"
    )


def sidebar_html(ctx: RocnikContext, active_id: str = "") -> str:
    links = [f'<a href="index.html"><strong>Přehled ročníku</strong></a>']
    for d in ctx.lessons:
        lid = d.name
        meta = parse_meta(d / "meta.yaml")
        nazev = meta.get("nazev", lid)
        num = lid[:2]
        cls = ' class="active"' if lid == active_id else ""
        links.append(
            f'<a href="{lid}.html"{cls}><span class="num">{num}</span>{nazev}</a>'
        )
    return "\n".join(links) + rocnik_switch_html(ctx)


def sidebar_header_html(subtitle: str) -> str:
    return f"""<h1>Kurz programování</h1>
      <p class="sub">{subtitle}</p>
      <p class="author">{AUTHOR}</p>
      {theme_toggle_html()}"""


def page_shell(ctx: RocnikContext, title: str, body: str, active_id: str = "") -> str:
    sidebar_inner = f"""{sidebar_header_html(f"{ctx.label} · {rocnik_jazyk(ctx)}")}
      <nav>{sidebar_html(ctx, active_id)}</nav>"""
    return document_shell(title, sidebar_inner, body, ctx=ctx)


def build_rocnik_index(ctx: RocnikContext) -> None:
    tema = rocnik_tema(ctx)
    hodiny = total_hours(ctx.lessons)
    if not ctx.lessons:
        try:
            hodiny = int(ctx.kurikulum.get("hodiny_celkem") or 0)
        except ValueError:
            hodiny = 0
    uvod = rocnik_uvod_html(ctx)

    badges = [f'<span class="badge">{rocnik_jazyk(ctx)}</span>']
    if hodiny:
        badges.append(f'<span class="badge">{hodiny} hodin</span>')
    if ctx.lessons:
        badges.append(f'<span class="badge">{len(ctx.lessons)} lekcí</span>')
    else:
        badges.append('<span class="badge">Připravuje se</span>')

    if ctx.lessons:
        cards = []
        for d in ctx.lessons:
            meta = parse_meta(d / "meta.yaml")
            nazev = meta.get("nazev", d.name)
            hod = format_lesson_hours(meta.get("hodiny", "?"), card=True)
            cards.append(f"""
        <a class="card" href="{d.name}.html">
          <div class="num">Lekce {d.name[:2]}</div>
          <h3>{nazev}</h3>
          <p>{hod} · {format_obtiznost(meta.get('obtiznost', ''))}</p>
        </a>""")
        lekce_block = f"""
      <h2 class="index-heading">Lekce</h2>
      <div class="index-grid">{"".join(cards)}</div>"""
    else:
        lekce_block = """
      <div class="empty-state">
        <p>Karty lekcí se sem doplní, až bude obsah ročníku hotový. Úvod výše platí už teď.</p>
      </div>"""

    body = f"""
      <div class="hero">
        <h1>{ctx.label} — {tema}</h1>
        <div class="meta">
          {"".join(badges)}
        </div>
      </div>
      {uvod}
      {lekce_block}
    """
    ctx.vystup_dir.mkdir(parents=True, exist_ok=True)
    (ctx.vystup_dir / "index.html").write_text(
        page_shell(ctx, f"{ctx.label} — {tema}", body),
        encoding="utf-8",
    )


def build_lesson(ctx: RocnikContext, lesson_dir: Path) -> None:
    lid = lesson_dir.name
    meta = parse_meta(lesson_dir / "meta.yaml")
    nazev = meta.get("nazev", lid)

    lekce_md = lesson_dir / "lekce.md"
    cviceni_md = lesson_dir / "cviceni.md"
    ukoly_md = lesson_dir / "ukoly.md"

    diagramy_src = lesson_dir / "diagramy"
    if diagramy_src.is_dir():
        diagramy_dst = ctx.vystup_dir / "diagramy" / lid
        diagramy_dst.mkdir(parents=True, exist_ok=True)
        for svg in diagramy_src.glob("*"):
            if svg.is_file():
                shutil.copy2(svg, diagramy_dst / svg.name)

    def lesson_html(text: str) -> str:
        html = postprocess_student_html(md_to_html(text))
        if diagramy_src.is_dir():
            html = html.replace('src="diagramy/', f'src="diagramy/{lid}/')
            html = inline_diagram_svgs(html, ctx.vystup_dir)
        return html

    lekce_html = (
        lesson_html(lekce_md.read_text(encoding="utf-8"))
        if lekce_md.exists()
        else "<p><em>Obsah lekce není k dispozici.</em></p>"
    )
    has_cviceni = cviceni_md.exists()
    cviceni_html = (
        lesson_html(cviceni_md.read_text(encoding="utf-8"))
        if has_cviceni
        else ""
    )
    has_ukoly = ukoly_md.exists()
    ukoly_html = (
        lesson_html(ukoly_md.read_text(encoding="utf-8"))
        if has_ukoly
        else ""
    )

    def tabs_html(active: str) -> str:
        links = [("lekce", f"{lid}.html", "Lekce")]
        if has_cviceni:
            links.append(("cviceni", f"{lid}-cviceni.html", "Cvičení"))
        if has_ukoly:
            links.append(("ukoly", f"{lid}-ukoly.html", "Úkoly"))
        if len(links) == 1:
            return ""
        parts = ['<div class="tabs">']
        for key, href, label in links:
            cls = " active" if key == active else ""
            parts.append(f'<a class="tab{cls}" href="{href}">{label}</a>')
        parts.append("</div>")
        return "\n      ".join(parts)

    pages: list[tuple[str, str, str]] = [
        ("lekce", "", lekce_html),
    ]
    if has_cviceni:
        pages.append(("cviceni", " — Cvičení", cviceni_html))
    if has_ukoly:
        pages.append(("ukoly", " — Úkoly", ukoly_html))

    for tab, suffix_title, content in pages:
        suffix = "" if tab == "lekce" else f"-{tab}"
        body = f"""
      <div class="breadcrumb"><a href="index.html">Přehled</a> / Lekce {lid[:2]}</div>
      <div class="hero">
        <h1>{nazev}</h1>
        <div class="meta">
          <span class="badge">{format_lesson_hours(meta.get('hodiny', '?'))}</span>
          <span class="badge">{format_obtiznost(meta.get('obtiznost', ''))}</span>
          <span class="badge">{ctx.label}</span>
        </div>
      </div>
      {tabs_html(tab)}
      <article class="content">{content}</article>
        """
        (ctx.vystup_dir / f"{lid}{suffix}.html").write_text(
            page_shell(ctx, nazev + suffix_title, body, lid),
            encoding="utf-8",
        )


def build_root_index(contexts: list[RocnikContext]) -> None:
    cards = []
    for ctx in contexts:
        tema = rocnik_tema(ctx)
        count = len(ctx.lessons)
        hodiny = total_hours(ctx.lessons)
        kurikulum_hodiny = ctx.kurikulum.get("hodiny_celkem")
        if not count and kurikulum_hodiny:
            try:
                hodiny = int(kurikulum_hodiny)
            except ValueError:
                pass
        if count:
            meta_line = f"{hodiny} hodin · {count} lekcí"
            card_class = "card"
        else:
            meta_line = "Obsah se připravuje"
            card_class = "card"

        cards.append(f"""
        <a class="{card_class}" href="{ctx.slug}/index.html">
          <div class="num">{ctx.label}</div>
          <h3>{tema}</h3>
          <p>{rocnik_jazyk(ctx)} · {meta_line}</p>
        </a>""")

    body = f"""
      <div class="hero">
        <h1>Kurz programování</h1>
        <div class="meta">
          <span class="badge">1.–3. ročník</span>
          <span class="badge">IT obor</span>
          <span class="badge">{AUTHOR}</span>
        </div>
      </div>
      <p style="color: var(--muted); max-width: 72ch;">
        Studijní materiály rozdělené podle ročníků. Vyberte ročník — každý má vlastní přehled a navigaci lekcí.
      </p>
      <div class="index-grid">{"".join(cards)}</div>
    """

    sidebar_inner = f"""{sidebar_header_html("Přehled ročníků")}
      <nav>
        <a href="index.html" class="active"><strong>Všechny ročníky</strong></a>
        {"".join(f'<a href="{ctx.slug}/index.html">{ctx.label}</a>' for ctx in contexts)}
      </nav>"""
    shell = document_shell("Přehled", sidebar_inner, body, page_title="Kurz programování")
    (VYSTUP_DIR / "index.html").write_text(shell, encoding="utf-8")


def cleanup_legacy_root_html() -> None:
    """Odstraní staré HTML lekcí z kořene graficky-vystup/ (před rozdělením na ročníky)."""
    for path in VYSTUP_DIR.glob("*.html"):
        if path.name != "index.html":
            path.unlink()


def make_context(rocnik_slug: str) -> RocnikContext:
    num = int(rocnik_slug[0])
    lekce_dir = LEKCE_ROOT / rocnik_slug
    return RocnikContext(
        slug=rocnik_slug,
        num=num,
        label=rocnik_label(num),
        lekce_dir=lekce_dir,
        vystup_dir=VYSTUP_DIR / rocnik_slug,
        kurikulum=parse_kurikulum(rocnik_slug),
        lessons=lesson_dirs(lekce_dir),
    )


def build_rocnik(ctx: RocnikContext) -> None:
    cleanup_stale_lesson_html(ctx)
    build_rocnik_index(ctx)
    for d in ctx.lessons:
        build_lesson(ctx, d)
        print(f"  ✓ {ctx.slug}/{d.name}")


def main() -> None:
    VYSTUP_DIR.mkdir(exist_ok=True)
    (VYSTUP_DIR / "styles.css").write_text(build_styles_css(), encoding="utf-8")
    (VYSTUP_DIR / "nav.js").write_text(NAV_JS.strip() + "\n", encoding="utf-8")
    if FAVICON_SRC.is_file():
        shutil.copy2(FAVICON_SRC, VYSTUP_DIR / "favicon.svg")
    cleanup_legacy_root_html()

    contexts = [make_context(slug) for slug in ROCNIKY]
    build_root_index(contexts)

    for ctx in contexts:
        print(f"\n{ctx.label}:")
        build_rocnik(ctx)

    print(f"\nGrafický výstup: {VYSTUP_DIR / 'index.html'}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("Generuji grafický výstup…")
    main()
