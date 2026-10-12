#!/usr/bin/env python3
"""Regenerate the SVG cards used by the profile README.

Pulls live numbers from the GitHub API (contribution calendar, merged
upstream PRs, pinned repo metadata) and writes static SVGs into assets/
and profile/. Standard library only, so it runs as-is in GitHub Actions.

Token: $GITHUB_TOKEN, falling back to `gh auth token` for local runs.
"""
import datetime as dt
import html
import json
import math
import os
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

USER = "Sanjays2402"
ROOT = Path(__file__).resolve().parent.parent

# Upstream projects shown as cards, in display order.
PINS = [
    "openclaw/openclaw",
    "pygments/pygments",
    "nesquena/hermes-webui",
    "fsspec/filesystem_spec",
    "apache/libcloud",
    "rclone/rclone",
]

# Palette: GitHub dark surfaces with a single gold accent.
BG, CARD, BORDER = "#0d1117", "#161b22", "#30363d"
FG, DIM, ACCENT = "#e6edf3", "#8b949e", "#f0b429"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178c6", "JavaScript": "#f1e05a",
    "Go": "#00ADD8", "Rust": "#dea584", "Swift": "#F05138", "Java": "#b07219",
}


# ---------- GitHub API ----------
def token():
    t = os.environ.get("GITHUB_TOKEN")
    if t:
        return t
    return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()


TOKEN = token()


def api(path, body=None):
    url = path if path.startswith("http") else "https://api.github.com/" + path.lstrip("/")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-builder",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def search_count(q):
    return api("search/issues?per_page=1&q=" + urllib.parse.quote(q))["total_count"]


def merged_upstream():
    """(merged PR count, distinct repo count) outside the user's own repos."""
    q = f"is:pr author:{USER} is:merged -user:{USER}"
    repos, total, page = set(), None, 1
    while True:
        res = api(f"search/issues?per_page=100&page={page}&q=" + urllib.parse.quote(q))
        total = res["total_count"]
        for item in res["items"]:
            repos.add(item["repository_url"].rsplit("/repos/", 1)[1])
        if len(res["items"]) < 100 or page * 100 >= min(total, 1000):
            break
        page += 1
    return total, len(repos)


def contributions():
    q = """query($u:String!){user(login:$u){
      contributionsCollection{totalCommitContributions totalPullRequestContributions
        totalIssueContributions totalPullRequestReviewContributions
        contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}
      repositories(ownerAffiliations:OWNER,isFork:false,privacy:PUBLIC){totalCount}}}"""
    return api("graphql", {"query": q, "variables": {"u": USER}})["data"]["user"]


# ---------- SVG helpers ----------
def esc(s):
    return html.escape(str(s), quote=True)


def fmt(n):
    return f"{n:,}"


def short(n):
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def write(rel, svg):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(svg.strip() + "\n")
    print("wrote", rel)


# ---------- header / typing / footer ----------
def header():
    # dot grid + slow-drifting glow behind the name
    dots = "".join(
        f'<circle cx="{x}" cy="{y}" r="1.2" fill="{FG}" opacity=".07"/>'
        for x in range(24, 1200, 32) for y in range(20, 260, 32))
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260" viewBox="0 0 1200 260" role="img" aria-label="Sanjay Santhanam">
  <defs>
    <radialGradient id="glow" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="{ACCENT}" stop-opacity=".22"/>
      <stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="rule" x1="0" x2="1">
      <stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/>
      <stop offset=".5" stop-color="{ACCENT}"/>
      <stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="260" rx="16" fill="{BG}"/>
  {dots}
  <ellipse cx="600" cy="120" rx="420" ry="150" fill="url(#glow)">
    <animate attributeName="rx" values="380;460;380" dur="9s" repeatCount="indefinite"/>
  </ellipse>
  <text x="600" y="118" text-anchor="middle" font-family="{SANS}" font-size="64" font-weight="700" fill="{FG}" letter-spacing="1">Sanjay Santhanam</text>
  <rect x="380" y="146" width="440" height="2" fill="url(#rule)"/>
  <text x="600" y="190" text-anchor="middle" font-family="{MONO}" font-size="20" fill="{DIM}" letter-spacing="3">BACKEND SYSTEMS · NATIVE APPS · DEVELOPER TOOLS</text>
  <rect x="0.5" y="0.5" width="1199" height="259" rx="16" fill="none" stroke="{BORDER}"/>
</svg>"""


def typing(lines):
    # Each line types out via a stepped clip, holds, then hands off to the next.
    n, per = len(lines), 4.0
    total = n * per
    char_w, size, y = 13.2, 22, 38
    css, groups = [], []
    for i, line in enumerate(lines):
        chars = len(line) + 3                  # "$ " prefix + caret
        w = chars * char_w
        x0 = 450 - w / 2
        start, type_end, hold_end, end = (i * per / total * 100, (i * per + 1.6) / total * 100,
                                          (i * per + 3.4) / total * 100, ((i + 1) * per) / total * 100)
        css.append(f"""
    @keyframes t{i}{{0%,{start:.2f}%{{width:0}}{type_end:.2f}%,{hold_end:.2f}%{{width:{w+14:.0f}px}}{end:.2f}%,100%{{width:0}}}}
    #c{i}{{animation:t{i} {total}s steps(1,end) infinite;animation-timing-function:steps({chars})}}
    @keyframes o{i}{{0%,{start:.2f}%{{opacity:0}}{start+.01:.2f}%,{end-.01:.2f}%{{opacity:1}}{end:.2f}%,100%{{opacity:0}}}}
    #g{i}{{animation:o{i} {total}s linear infinite}}""")
        groups.append(f"""
  <clipPath id="k{i}"><rect id="c{i}" x="{x0:.0f}" y="10" height="40" width="0"/></clipPath>
  <g id="g{i}" opacity="0"><g clip-path="url(#k{i})">
    <text x="{x0:.0f}" y="{y}" font-family="{MONO}" font-size="{size}" fill="{FG}"><tspan fill="{ACCENT}">$ </tspan>{esc(line)}<tspan fill="{ACCENT}">▍</tspan></text>
  </g></g>""")
    alt = " ".join(lines)
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="60" viewBox="0 0 900 60" role="img" aria-label="{esc(alt)}">
  <style>{''.join(css)}
  </style>
  <!-- own dark backdrop so the light text reads on GitHub's light theme too -->
  <rect x=".5" y=".5" width="899" height="59" rx="30" fill="{BG}" stroke="{BORDER}"/>{''.join(groups)}
</svg>"""


def footer():
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="60" viewBox="0 0 1200 60" role="img" aria-hidden="true">
  <defs><linearGradient id="f" x1="0" x2="1">
    <stop offset="0" stop-color="{ACCENT}" stop-opacity="0"/><stop offset=".5" stop-color="{ACCENT}" stop-opacity=".9"/>
    <stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/></linearGradient></defs>
  <path d="M0 30 Q 150 10 300 30 T 600 30 T 900 30 T 1200 30" fill="none" stroke="url(#f)" stroke-width="2">
    <animate attributeName="d" dur="8s" repeatCount="indefinite"
      values="M0 30 Q 150 10 300 30 T 600 30 T 900 30 T 1200 30;M0 30 Q 150 50 300 30 T 600 30 T 900 30 T 1200 30;M0 30 Q 150 10 300 30 T 600 30 T 900 30 T 1200 30"/>
  </path>
</svg>"""


# ---------- skills ----------
SKILLS = [
    ("Languages", ["Python", "TypeScript", "Go", "Swift", "Rust", "Java"]),
    ("Backend & data", ["PostgreSQL", "SQLite", "Redis", "ClickHouse", "asyncio", "Express"]),
    ("Apps & UI", ["SwiftUI", "React", "Three.js / WebGL", "Browser extensions", "VS Code API", "TUI / CLI"]),
    ("Infra & tooling", ["Docker", "GitHub Actions", "Linux", "macOS", "Git", "LLM tooling"]),
]


def skills():
    row_h, chip_h, pad = 72, 42, 28
    h = pad * 2 + row_h * len(SKILLS) - (row_h - chip_h)
    out = []
    for r, (label, items) in enumerate(SKILLS):
        y = pad + r * row_h
        out.append(f'<text x="{pad}" y="{y+27}" font-family="{MONO}" font-size="14" fill="{DIM}" letter-spacing="1.5">{esc(label.upper())}</text>')
        x = 236
        for it in items:
            w = len(it) * 9.4 + 42
            dot = LANG_COLORS.get(it, ACCENT)
            out.append(
                f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{chip_h}" rx="21" fill="{CARD}" stroke="{BORDER}"/>'
                f'<circle cx="{x+20}" cy="{y+chip_h/2}" r="5.5" fill="{dot}"/>'
                f'<text x="{x+34}" y="{y+27}" font-family="{SANS}" font-size="16.5" fill="{FG}">{esc(it)}</text>')
            x += w + 10
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="Stack: {esc(', '.join(i for _, g in SKILLS for i in g))}">
  <rect width="1200" height="{h}" rx="14" fill="{BG}" stroke="{BORDER}"/>
  {''.join(out)}
</svg>"""


# ---------- pinned upstream repo cards ----------
def pin(full, merged):
    r = api(f"repos/{full}")
    desc = (r.get("description") or "").strip()
    # wrap description to two lines of ~62 chars
    words, lines, cur = desc.split(), [], ""
    for wd in words:
        if len(cur) + len(wd) + 1 > 62:
            lines.append(cur)
            cur = wd
        else:
            cur = (cur + " " + wd).strip()
    if cur:
        lines.append(cur)
    if len(lines) > 2:
        lines = lines[:2]
        lines[1] = lines[1][:59].rstrip() + "…"
    lang = r.get("language") or "—"
    desc_svg = "".join(
        f'<text x="24" y="{78+i*20}" font-family="{SANS}" font-size="13.5" fill="{DIM}">{esc(l)}</text>'
        for i, l in enumerate(lines))
    label = "merged PR" if merged == 1 else "merged PRs"
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="580" height="160" viewBox="0 0 580 160" role="img" aria-label="{esc(full)}: {merged} {label}">
  <rect x=".5" y=".5" width="579" height="159" rx="12" fill="{CARD}" stroke="{BORDER}"/>
  <text x="24" y="44" font-family="{SANS}" font-size="18" font-weight="600" fill="{FG}"><tspan fill="{DIM}">{esc(full.split('/')[0])} / </tspan>{esc(full.split('/')[1])}</text>
  {desc_svg}
  <circle cx="30" cy="134" r="6" fill="{LANG_COLORS.get(lang, DIM)}"/>
  <text x="44" y="139" font-family="{SANS}" font-size="13" fill="{DIM}">{esc(lang)}</text>
  <text x="{60 + len(lang)*7.5:.0f}" y="139" font-family="{SANS}" font-size="13" fill="{DIM}">★ {short(r['stargazers_count'])}</text>
  <rect x="{556 - (len(str(merged)) + len(label)) * 8.2 - 30:.0f}" y="118" width="{(len(str(merged)) + len(label)) * 8.2 + 30:.0f}" height="28" rx="14" fill="{ACCENT}" fill-opacity=".14" stroke="{ACCENT}" stroke-opacity=".5"/>
  <text x="{556 - ((len(str(merged)) + len(label)) * 8.2 + 30) / 2:.0f}" y="137" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{ACCENT}">{merged} {label}</text>
</svg>"""


# ---------- activity: isometric contribution graph, stats, streak ----------
def calendar_days(user):
    weeks = user["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [[(d["date"], d["contributionCount"]) for d in w["contributionDays"]] for w in weeks]


def contrib3d(weeks, total):
    tile, rise = 14, 0.52                       # iso tile half-width and height
    peak = max(c for w in weeks for _, c in w) or 1
    nw = len(weeks)
    ox, oy = 600 - (nw - 7) / 2 * tile, 170     # centre the strip horizontally
    H = int(oy + (nw + 7) * tile * 0.5 + 60)
    cols = ["#1c2128", "#4a3b12", "#7a5c12", "#b8860b", ACCENT]
    shapes = []

    def level(c):
        if c == 0:
            return 0
        return min(4, 1 + int(3.999 * math.sqrt(c / peak)))

    for wi, week in enumerate(weeks):
        for di, (_, c) in enumerate(week):
            # isometric projection: week runs right-down, weekday runs left-down
            x = ox + (wi - di) * tile
            y = oy + (wi + di) * tile * 0.5
            hgt = 3 + 120 * math.sqrt(c / peak) if c else 3
            col = cols[level(c)]
            top = f"{x},{y-hgt} {x+tile},{y-hgt+tile*rise} {x},{y-hgt+tile*rise*2} {x-tile},{y-hgt+tile*rise}"
            left = f"{x-tile},{y-hgt+tile*rise} {x},{y-hgt+tile*rise*2} {x},{y+tile*rise*2} {x-tile},{y+tile*rise}"
            right = f"{x+tile},{y-hgt+tile*rise} {x},{y-hgt+tile*rise*2} {x},{y+tile*rise*2} {x+tile},{y+tile*rise}"
            shapes.append(
                f'<polygon points="{left}" fill="{col}" filter="url(#dk1)"/>'
                f'<polygon points="{right}" fill="{col}" filter="url(#dk2)"/>'
                f'<polygon points="{top}" fill="{col}"/>')
    ly = H - 36
    legend = "".join(
        f'<rect x="{1010+i*22}" y="{ly}" width="16" height="16" rx="3" fill="{c}"/>' for i, c in enumerate(cols))
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{H}" viewBox="0 0 1200 {H}" role="img" aria-label="{fmt(total)} contributions in the last year">
  <defs>
    <filter id="dk1"><feColorMatrix type="matrix" values=".62 0 0 0 0  0 .62 0 0 0  0 0 .62 0 0  0 0 0 1 0"/></filter>
    <filter id="dk2"><feColorMatrix type="matrix" values=".78 0 0 0 0  0 .78 0 0 0  0 0 .78 0 0  0 0 0 1 0"/></filter>
  </defs>
  <rect width="1200" height="{H}" rx="14" fill="{BG}" stroke="{BORDER}"/>
  <text x="36" y="58" font-family="{SANS}" font-size="38" font-weight="700" fill="{FG}">{fmt(total)}</text>
  <text x="36" y="86" font-family="{MONO}" font-size="14" fill="{DIM}" letter-spacing="1.5">CONTRIBUTIONS IN THE LAST YEAR</text>
  {''.join(shapes)}
  <text x="960" y="{ly+13}" font-family="{MONO}" font-size="12" fill="{DIM}">less</text>{legend}
  <text x="1124" y="{ly+13}" font-family="{MONO}" font-size="12" fill="{DIM}">more</text>
</svg>"""


def stats_card(user, merged, merged_repos):
    c = user["contributionsCollection"]
    rows = [
        ("Commits (last year)", c["totalCommitContributions"]),
        ("Pull requests opened", c["totalPullRequestContributions"]),
        ("Reviews", c["totalPullRequestReviewContributions"]),
        ("Merged upstream PRs", merged),
        ("Upstream repos merged into", merged_repos),
        ("Public repos (non-fork)", user["repositories"]["totalCount"]),
    ]
    body = "".join(
        f'<text x="28" y="{86+i*32}" font-family="{SANS}" font-size="15" fill="{DIM}">{esc(k)}</text>'
        f'<text x="552" y="{86+i*32}" text-anchor="end" font-family="{MONO}" font-size="15" fill="{FG}" font-weight="600">{fmt(v)}</text>'
        for i, (k, v) in enumerate(rows))
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="580" height="290" viewBox="0 0 580 290" role="img" aria-label="GitHub stats">
  <rect x=".5" y=".5" width="579" height="289" rx="12" fill="{CARD}" stroke="{BORDER}"/>
  <text x="28" y="44" font-family="{SANS}" font-size="18" font-weight="600" fill="{ACCENT}">GitHub stats</text>
  {body}
</svg>"""


def streaks(weeks):
    days = [(d, c) for w in weeks for d, c in w]
    longest = run = 0
    best_end = None
    for d, c in days:
        run = run + 1 if c else 0
        if run > longest:
            longest, best_end = run, d
    # current streak: today may still be empty, so start from yesterday in that case
    cur = 0
    seq = days[::-1]
    if seq and seq[0][1] == 0:
        seq = seq[1:]
    for _, c in seq:
        if not c:
            break
        cur += 1
    active = sum(1 for _, c in days if c)
    return cur, longest, best_end, active, len(days)


def streak_card(weeks):
    cur, longest, best_end, active, n = streaks(weeks)
    best = dt.date.fromisoformat(best_end).strftime("%b %-d, %Y") if best_end else "—"
    cols = [("Current streak", f"{cur} days", "ending today"),
            ("Longest streak", f"{longest} days", f"ending {best}"),
            ("Active days", f"{active}", f"of the last {n}")]
    body = ""
    for i, (k, v, sub) in enumerate(cols):
        cx = 97 + i * 193
        hl = ACCENT if i == 0 else FG
        body += (f'<text x="{cx}" y="140" text-anchor="middle" font-family="{SANS}" font-size="34" font-weight="700" fill="{hl}">{esc(v.split()[0])}</text>'
                 f'<text x="{cx}" y="172" text-anchor="middle" font-family="{SANS}" font-size="14" fill="{FG}">{esc(k)}</text>'
                 f'<text x="{cx}" y="194" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{DIM}">{esc(sub)}</text>')
        if i:
            body += f'<line x1="{cx-96}" y1="96" x2="{cx-96}" y2="206" stroke="{BORDER}"/>'
    if cur:
        # pulsing ring around the current streak
        body += (f'<circle cx="97" cy="128" r="46" fill="none" stroke="{ACCENT}" stroke-opacity=".5" stroke-width="2">'
                 f'<animate attributeName="stroke-opacity" values=".15;.6;.15" dur="3s" repeatCount="indefinite"/></circle>')
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="580" height="290" viewBox="0 0 580 290" role="img" aria-label="Current streak {cur} days, longest {longest} days">
  <rect x=".5" y=".5" width="579" height="289" rx="12" fill="{CARD}" stroke="{BORDER}"/>
  <text x="28" y="44" font-family="{SANS}" font-size="18" font-weight="600" fill="{ACCENT}">Contribution streak</text>
  {body}
  <text x="290" y="262" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{DIM}">updated {dt.date.today().isoformat()}</text>
</svg>"""


def main():
    user = contributions()
    weeks = calendar_days(user)
    total = user["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    merged, merged_repos = merged_upstream()

    write("assets/header.svg", header())
    write("assets/typing.svg", typing([
        "Building backend systems, native apps and dev tools.",
        f"{merged}+ PRs merged into {merged_repos} open-source repos.",
        "Shipping Slab: an offline PDF studio in Rust.",
    ]))
    write("assets/skills.svg", skills())
    write("assets/footer.svg", footer())
    for full in PINS:
        n = search_count(f"is:pr author:{USER} is:merged repo:{full}")
        write(f"profile/pin-{full.split('/')[1].lower()}.svg", pin(full, n))
    write("profile/contrib-3d.svg", contrib3d(weeks, total))
    write("profile/stats.svg", stats_card(user, merged, merged_repos))
    write("profile/streak.svg", streak_card(weeks))


if __name__ == "__main__":
    main()
