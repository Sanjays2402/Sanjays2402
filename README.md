![Sanjay Santhanam](assets/hero.svg)

<p align="center">
  <img src="assets/typing-dark.svg#gh-dark-mode-only" alt="typing animation" />
  <img src="assets/typing-light.svg#gh-light-mode-only" alt="typing animation" />
</p>

<p align="center">📍 Seattle</p>

---

## 🔨 Featured Projects

<sub>Click any project to expand it 👇</sub>

<details>
<summary><b>city-friction-map</b> — community-powered map of everyday city obstacles</summary>
<br>
Report, verify, save, and share local heads-ups with explainable clearance estimates. Freshness badges, moderation queue, RSS feeds, embeddable widgets.
<br><br>
<code>JavaScript</code> <code>Express</code> <code>SQLite</code> <code>Leaflet</code>
<br><br>
<a href="https://github.com/Sanjays2402/city-friction-map">→ View on GitHub</a>
</details>

<details>
<summary><b>copilot-usage-tracker</b> — enterprise GitHub Copilot usage &amp; cost tracking</summary>
<br>
AI-credit billing model, team attribution, budgets, policy-as-code, tray app + dashboard, real Windows/macOS installers.
<br><br>
<code>Python</code> <code>Streamlit</code> <code>SQLite</code>
<br><br>
<a href="https://github.com/Sanjays2402/copilot-usage-tracker">→ View on GitHub</a>
</details>

<details>
<summary><b>Tilt</b> — depth for your lid</summary>
<br>
Close the lid and watch the screen lean away into frosted glass. Idle glass, battery saver, recordable preview hotkey.
<br><br>
<code>Swift</code> <code>SwiftUI</code> <code>ScreenCaptureKit</code>
<br><br>
<a href="https://github.com/Sanjays2402/Tilt">→ View on GitHub</a>
</details>

<details>
<summary><b>ferry</b> — lightweight distributed task queue for Python</summary>
<br>
SQLite-simple, production-serious: priorities, retries, schedules, and a live dashboard.
<br><br>
<code>Python</code> <code>SQLite</code>
<br><br>
<a href="https://github.com/Sanjays2402/ferry">→ View on GitHub</a>
</details>

<details>
<summary><b>retrace</b> — crash-resumable Python workflows</summary>
<br>
SQLite checkpoints, fenced worker leases, durable retries, live execution inspector. Zero runtime dependencies.
<br><br>
<code>Python</code> <code>asyncio</code> <code>SQLite</code>
<br><br>
<a href="https://github.com/Sanjays2402/retrace">→ View on GitHub</a>
</details>

<details>
<summary><b>…and 30+ more</b></summary>
<br>
<code>optune</code> <code>snip</code> <code>tsk</code> <code>core-stealth</code> <code>flight-sim</code> <code>ai-particle-simulator</code> <code>slab</code> <code>clawmind</code> <code>triple-tic-tac-toe</code> <code>data-forge</code> <code>ascii-webcam</code> <code>devdash</code> <code>memory-matrix</code> <code>2048-game</code> <code>snippet-dev</code> <code>gitsight</code> <code>clawreview</code> <code>context-clipboard</code> <code>signalclaw</code> <code>clawhum</code> <code>adherence-ml</code> <code>codeclone</code> <code>CakePond</code> <code>sunsprout</code> <code>gta-vibes</code> <code>pixel-forge</code> <code>url-shortener</code> <code>secure-notes-app</code> <code>realtime-log-monitor</code> <code>personal-file-backup</code>
</details>

---

## 📦 Open Source Footprint

**60+ merged PRs** in projects used by millions:

- **openclaw/openclaw** — streamed-reply recovery, secrets auditing, Codex compaction auth, Discord voice, PluralKit pairing
- **nesquena/hermes-webui** — ~15 merged PRs (endless scroll, streaming timing, Docker, keyboard nav)
- **pygments/pygments** — 15 lexer/formatter fixes across Kotlin, C++, LaTeX, TS, Ruby, and more
- **astral-sh/ruff** — D418 stub-file fix
- **rclone/rclone** — goroutine leak fix, WebDAV overwrite default
- **uv**, **helix**, **goreleaser**, **pylint**, **redis-py**, **pydantic**, **chardet**, **tweepy**, **tenacity**, **mistune**, and **50+ more**

### 🔥 Recent upstream fixes

A few examples, all linked — each with a repro, a narrow fix, and tests:

- [facebook/hermes#2181](https://github.com/facebook/hermes/pull/2181) — `Date` was wrong for time zones whose standard offset changed over history (cached modern offset + historical DST)
- [react/react#37559](https://github.com/react/react/pull/37559) — React Compiler's `DisjointSet.union()` mutated its input array via `shift()`
- [pytorch/ao#4878](https://github.com/pytorch/ao/pull/4878) — PT2E Quick Start example now runs as documented
- [facebook/docusaurus#12430](https://github.com/facebook/docusaurus/pull/12430) — broken-anchor checker recognizes arbitrary HTML anchors
- [aws/aws-sdk-pandas#3475](https://github.com/aws/aws-sdk-pandas/pull/3475) — `emr.create_cluster` accepts bootstrap action arguments
- [aws/aws-cli#10626](https://github.com/aws/aws-cli/pull/10626) — `aws ssm start-session` surfaces the real plugin-not-found error instead of a misleading permissions error
- [aws/aws-sam-cli#9267](https://github.com/aws/aws-sam-cli/pull/9267) — `--role-arn` service role now flows to the companion stack
- [aws/aws-lambda-builders#920](https://github.com/aws/aws-lambda-builders/pull/920) — PEP 517-only projects fall back to `pyproject.toml` metadata
- [googleapis/google-cloud-python#18328](https://github.com/googleapis/google-cloud-python/pull/18328) — `AsyncAuthorizedSession` leaked response objects across retries
- [firebase/extensions#3169](https://github.com/firebase/extensions/pull/3169) — storage-resize-images rejects bogus `IMAGE_TYPE` values at startup instead of writing broken files
- [microsoft/fluentui#36725](https://github.com/microsoft/fluentui/pull/36725) — WeeklyDayPicker shows the correct week number in collapsed view
- [microsoft/vscode-json-languageservice#366](https://github.com/microsoft/vscode-json-languageservice/pull/366) — pre-2019-09 sibling `$ref`s resolve against the referencing document's base URI
- [microsoft/semantic-kernel#14448](https://github.com/microsoft/semantic-kernel/pull/14448) — `build_model_schema` keeps pydantic constraint objects out of field descriptions
- [prisma/orm#30278](https://github.com/prisma/orm/pull/30278) — widening `SET DEFAULT` was silently skipped as a no-op by the migration idempotency probe
- [prisma/orm#30277](https://github.com/prisma/orm/pull/30277) — clearer PSL parser diagnostic for `@@index([createdAt(sort: Desc)])`
- [atlassian-labs/connect-security-req-tester#99](https://github.com/atlassian-labs/connect-security-req-tester/pull/99) / [#100](https://github.com/atlassian-labs/connect-security-req-tester/pull/100) — referrer policy via `<meta>` tag; query strings preserved in module URLs
- [atlassian-labs/json-schema-viewer#52](https://github.com/atlassian-labs/json-schema-viewer/pull/52) — stop silently rewriting external `$ref` links from http to https

---

## 🛠 Stack

<p>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go" />
  <img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white" alt="Swift" />
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/Postgres-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="Postgres" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
</p>

Backend systems · Native macOS · Browser/WebGL · ML tooling · TUI/CLI · Developer tooling
