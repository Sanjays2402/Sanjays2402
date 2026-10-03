![Sanjay Santhanam — software engineer](assets/hero.svg)

## Hi, I'm Sanjay

I'm a software engineer in Seattle working on backend systems, native apps, and developer tools. I contribute upstream fixes across language tooling, developer infrastructure, and web applications.

**[Contribution history](https://github.com/pulls?q=is%3Apr+author%3ASanjays2402)** · **[Merged pull requests](https://github.com/pulls?q=is%3Apr+author%3ASanjays2402+is%3Amerged)** · **[LinkedIn](https://www.linkedin.com/in/sanjay24/)**

## Open-source contributions

### Selected merged contributions

| Project | Change merged upstream | Pull request |
| :--- | :--- | :--- |
| **[OpenClaw](https://github.com/openclaw/openclaw)** | Fixed duplicate Telegram forum-topic replies and missing transcript mirrors. | [#158054](https://github.com/openclaw/openclaw/pull/158054) |
| **[Pygments](https://github.com/pygments/pygments)** | Fixed JSX highlighting so apostrophes in element text no longer produce error tokens. | [#3214](https://github.com/pygments/pygments/pull/3214) |
| **[Ruff](https://github.com/astral-sh/ruff)** | Removed false-positive D418 diagnostics for docstrings on overloaded functions in stub files. | [#26318](https://github.com/astral-sh/ruff/pull/26318) |
| **[rclone](https://github.com/rclone/rclone)** | Stopped remote-control jobs that transfer no files from leaking stats goroutines. | [#9568](https://github.com/rclone/rclone/pull/9568) |
| **[Hermes WebUI](https://github.com/nesquena/hermes-webui)** | Fixed message submission on touch devices with external keyboards. | [#3130](https://github.com/nesquena/hermes-webui/pull/3130) |

**More of my work in these projects:** [OpenClaw](https://github.com/openclaw/openclaw/pulls?q=is%3Apr+author%3ASanjays2402) · [Pygments](https://github.com/pygments/pygments/pulls?q=is%3Apr+author%3ASanjays2402) · [Ruff](https://github.com/astral-sh/ruff/pulls?q=is%3Apr+author%3ASanjays2402) · [rclone](https://github.com/rclone/rclone/pulls?q=is%3Apr+author%3ASanjays2402) · [Hermes WebUI](https://github.com/nesquena/hermes-webui/pulls?q=is%3Apr+author%3ASanjays2402)

<details>
<summary>Additional upstream pull requests</summary>

Further work across frameworks, cloud SDKs, databases, and UI tooling:

| Project | Proposed fix | Pull request |
| :--- | :--- | :--- |
| **React Compiler** | Preserve the caller's input array in `DisjointSet.union()`. | [#37559](https://github.com/react/react/pull/37559) |
| **Google Cloud Python** | Close responses before retrying to avoid exhausting the connection pool. | [#18328](https://github.com/googleapis/google-cloud-python/pull/18328) |
| **AWS CLI** | Report a missing Session Manager plugin before starting a session, preventing a misleading permissions error. | [#10626](https://github.com/aws/aws-cli/pull/10626) |
| **Prisma ORM** | Execute column-default changes that the migration idempotency check incorrectly skipped. | [#30278](https://github.com/prisma/orm/pull/30278) |

- [facebook/hermes#2181](https://github.com/facebook/hermes/pull/2181) — `Date` was wrong for time zones whose standard offset changed over history (cached modern offset + historical DST)
- [pytorch/ao#4878](https://github.com/pytorch/ao/pull/4878) — PT2E Quick Start example now runs as documented
- [facebook/docusaurus#12430](https://github.com/facebook/docusaurus/pull/12430) — broken-anchor checker recognizes arbitrary HTML anchors
- [aws/aws-sdk-pandas#3475](https://github.com/aws/aws-sdk-pandas/pull/3475) — `emr.create_cluster` accepts bootstrap action arguments
- [aws/aws-sam-cli#9267](https://github.com/aws/aws-sam-cli/pull/9267) — `--role-arn` service role now flows to the companion stack
- [aws/aws-lambda-builders#920](https://github.com/aws/aws-lambda-builders/pull/920) — PEP 517-only projects fall back to `pyproject.toml` metadata
- [firebase/extensions#3169](https://github.com/firebase/extensions/pull/3169) — storage-resize-images rejects bogus `IMAGE_TYPE` values at startup instead of writing broken files
- [microsoft/fluentui#36725](https://github.com/microsoft/fluentui/pull/36725) — WeeklyDayPicker shows the correct week number in collapsed view
- [microsoft/vscode-json-languageservice#366](https://github.com/microsoft/vscode-json-languageservice/pull/366) — pre-2019-09 sibling `$ref`s resolve against the referencing document's base URI
- [microsoft/semantic-kernel#14448](https://github.com/microsoft/semantic-kernel/pull/14448) — `build_model_schema` keeps pydantic constraint objects out of field descriptions
- [prisma/orm#30277](https://github.com/prisma/orm/pull/30277) — clearer PSL parser diagnostic for `@@index([createdAt(sort: Desc)])`
- [atlassian-labs/connect-security-req-tester#99](https://github.com/atlassian-labs/connect-security-req-tester/pull/99) / [#100](https://github.com/atlassian-labs/connect-security-req-tester/pull/100) — referrer policy via `<meta>` tag; query strings preserved in module URLs
- [atlassian-labs/json-schema-viewer#52](https://github.com/atlassian-labs/json-schema-viewer/pull/52) — stop silently rewriting external `$ref` links from http to https

</details>

## Open-source projects I build

| Project | What it does | Built with |
| :--- | :--- | :--- |
| **[retrace](https://github.com/Sanjays2402/retrace)** | Resumes interrupted Python workflows from SQLite checkpoints, with durable retries and a live execution inspector. Zero runtime dependencies. | Python · asyncio · SQLite |
| **[ferry](https://github.com/Sanjays2402/ferry)** | Runs background tasks with priorities, retry backoff, scheduling, crash recovery, and a live dashboard. | Python · SQLite · Redis |
| **[city-friction-map](https://github.com/Sanjays2402/city-friction-map)** | Maps everyday city obstacles so neighbors can report, verify, and share them. Includes trip checks, public city feeds, and CSV/GeoJSON export. | JavaScript · Express · SQLite · Leaflet |
| **[copilot-usage-tracker](https://github.com/Sanjays2402/copilot-usage-tracker)** | Tracks enterprise Copilot usage and costs, with team attribution, budgets, trends, and per-user drill-downs. | Python · Streamlit · SQLite |
| **[Tilt](https://github.com/Sanjays2402/Tilt)** | Turns MacBook lid movement into live depth, blur, and frosted-glass effects rendered on the GPU. | Swift · SwiftUI · Metal · ScreenCaptureKit |

[Try the Retrace recovery playground →](https://sanjays2402.github.io/retrace/)

<details>
<summary>More projects</summary>

[optune](https://github.com/Sanjays2402/optune) · [snip](https://github.com/Sanjays2402/snip) · [tsk](https://github.com/Sanjays2402/tsk) · [core-stealth](https://github.com/Sanjays2402/core-stealth) · [flight-sim](https://github.com/Sanjays2402/flight-sim)

[ai-particle-simulator](https://github.com/Sanjays2402/ai-particle-simulator) · [slab](https://github.com/Sanjays2402/slab) · [clawmind](https://github.com/Sanjays2402/clawmind) · [triple-tic-tac-toe](https://github.com/Sanjays2402/triple-tic-tac-toe) · [data-forge](https://github.com/Sanjays2402/data-forge)

[ascii-webcam](https://github.com/Sanjays2402/ascii-webcam) · [devdash](https://github.com/Sanjays2402/devdash) · [memory-matrix](https://github.com/Sanjays2402/memory-matrix) · [2048-game](https://github.com/Sanjays2402/2048-game) · [snippet-dev](https://github.com/Sanjays2402/snippet-dev)

[gitsight](https://github.com/Sanjays2402/gitsight) · [clawreview](https://github.com/Sanjays2402/clawreview) · [context-clipboard](https://github.com/Sanjays2402/context-clipboard) · [signalclaw](https://github.com/Sanjays2402/signalclaw) · [clawhum](https://github.com/Sanjays2402/clawhum)

[adherence-ml](https://github.com/Sanjays2402/adherence-ml) · [codeclone](https://github.com/Sanjays2402/codeclone) · [CakePond](https://github.com/Sanjays2402/CakePond) · [sunsprout](https://github.com/Sanjays2402/sunsprout) · [gta-vibes](https://github.com/Sanjays2402/gta-vibes)

[pixel-forge](https://github.com/Sanjays2402/pixel-forge) · [url-shortener](https://github.com/Sanjays2402/url-shortener) · [secure-notes-app](https://github.com/Sanjays2402/secure-notes-app) · [realtime-log-monitor](https://github.com/Sanjays2402/realtime-log-monitor) · [personal-file-backup](https://github.com/Sanjays2402/personal-file-backup)

</details>

## Tools I work with

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

- **Backend & systems:** task queues, durable workflows, APIs, and data storage.
- **Native & web:** macOS apps, browser interfaces, and WebGL.
- **Developer tooling:** CLI/TUI tools, ML tooling, and debugging.
