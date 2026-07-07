# Sanjay Santhanam

Software Engineer II at Microsoft. I build things end-to-end — backends, systems, ML, developer tools, native apps, browser games, and the occasional TUI.

## Experience

- **Microsoft** — Software Engineer II · Oct 2025 – present · Redmond, WA
  - Work on **agentic security** — securing AI agents and LLM-driven autonomous systems.
  - Build guardrails against prompt injection, unsafe tool use, and privilege escalation across agent workflows.
  - Design identity, permissioning, and least-privilege boundaries for agents acting on behalf of users.
  - Develop runtime policy enforcement and threat detection for multi-step agent execution.
  - Red-team agent pipelines and harden them against adversarial and jailbreak inputs.

## Education

- **Syracuse University** — M.S., Computer Science
- **Anna University, Chennai** — B.E., Computer Science & Engineering

## Recent

**Pinned projects**

- [**optune**](https://github.com/Sanjays2402/optune) — open-source Logitech Options+ replacement for macOS. Native Swift 6 + SwiftUI Liquid Glass, IOKit HID++ transport, 8 HID++ features (battery, DPI, SmartShift, button remap, host switching, onboard profiles, keyboard backlight, Fn-lock), per-app profiles, CLI + menu bar app + shared Core. Homebrew tap available.
- [**flight-sim**](https://github.com/Sanjays2402/flight-sim) — browser flight simulator with takeoff, landing, instrument HUD, and a Three.js terrain pipeline. No install, runs from `gh-pages`.
- [**snip**](https://github.com/Sanjays2402/snip) — production-grade self-hosted URL shortener. TypeScript, Postgres, Redis, ClickHouse, BullMQ. Token-bucket rate limiting, signed webhooks, workspace RBAC, CLI client.
- [**tsk**](https://github.com/Sanjays2402/tsk) — keyboard-first markdown todo manager. Go, Bubbletea TUI, atomic writes, natural-language due dates, shell completions.
- [**ai-particle-simulator**](https://github.com/Sanjays2402/ai-particle-simulator) — describe an effect, render 20K+ GPU-accelerated particles. React + Three.js + WebGL, LLM-driven prompt-to-shader pipeline.

**CLIs & dev tools**

- [**snippet-dev**](https://github.com/Sanjays2402/snippet-dev) — local-first code snippet manager with fuzzy search, tags, syntax highlighting.
- [**markdown-zen**](https://github.com/Sanjays2402/markdown-zen) — distraction-free markdown editor with focus mode and a custom in-browser parser.
- [**devdash**](https://github.com/Sanjays2402/devdash) — personal dev dashboard with glassmorphism UI, drag-and-drop widgets, Spotify and Gmail integrations.
- [**context-clipboard**](https://github.com/Sanjays2402/context-clipboard) — context-aware clipboard for Chrome, Brave, Edge, and Firefox. MV3, local-only, captures source URL + page title + surrounding paragraph, in-page command palette, OCR.
- [**gitsight**](https://github.com/Sanjays2402/gitsight) — open Git visualization for VS Code. Commit graph, blame heatmap, interactive rebase, GitHub PR review inline.
- [**clawreview**](https://github.com/Sanjays2402/clawreview) — terse, dense, keyboard-first code review UI. Severity left-rails, mono everywhere, j/k nav, ⌘K palette.
- [**clawmind**](https://github.com/Sanjays2402/clawmind) — paper-cream knowledge tool. Top composer, two-column reading, inline numbered citations.
- [**Med-Tracker**](https://github.com/Sanjays2402/Med-Tracker) — calm pharmacy app with day-rail timeline, capsule motifs, and warm pillbox tokens.
- [**regex-lab**](https://github.com/Sanjays2402/regex-lab) — live regex tester with shareable URL state.
- [**data-forge**](https://github.com/Sanjays2402/data-forge) — CSV/JSON explorer with multi-column filters and canvas-rendered charts.

**Visual & creative**

- [**pixel-forge**](https://github.com/Sanjays2402/pixel-forge) — image to retro pixel art. Floyd–Steinberg dithering, 14 palettes, SVG export.
- [**fractal-lab**](https://github.com/Sanjays2402/fractal-lab) — Mandelbrot + Julia explorer with deep zoom and palette mapping.
- [**ascii-webcam**](https://github.com/Sanjays2402/ascii-webcam) — real-time webcam to ASCII in the browser.
- [**retro-terminal**](https://github.com/Sanjays2402/retro-terminal) — CRT terminal emulator with scanlines and phosphor glow.
- [**CakePond**](https://github.com/Sanjays2402/CakePond) — ambient SwiftUI koi pond for macOS.
- [**sunsprout**](https://github.com/Sanjays2402/sunsprout) — cozy pixel village + farm simulator that runs in the browser.
- [**gta-vibes**](https://github.com/Sanjays2402/gta-vibes) — two browser games inspired by GTA. Top-down 2D and 3D Three.js, WASD, no install.
- [**shotclassify**](https://github.com/Sanjays2402/shotclassify) — broadcast-graphic screenshot classifier. Felt-green scorebug chips, ESPN-style ticker, live classification feed.

## Open source contributions

Merged PRs across upstream projects.

**AI, agents & memory**

- [**openclaw/openclaw**](https://github.com/openclaw/openclaw) — agent runtime fixes for streamed-reply recovery, secrets auditing, codex synthetic-key handling, memory-core warning suppression, Discord voice session reuse, and PluralKit DM pairing.
- [**nesquena/hermes-webui**](https://github.com/nesquena/hermes-webui) — endless-scroll prefetch race, streaming scroll-pin, custom provider config, mobile send-on-Enter with a real keyboard, and throttled session-refresh polling.
- [**outsourc-e/hermes-workspace**](https://github.com/outsourc-e/hermes-workspace) — slash-menu autocomplete, distinct gateway-auth-rejected error path.
- [**huggingface/huggingface_hub**](https://github.com/huggingface/huggingface_hub) — [#4278](https://github.com/huggingface/huggingface_hub/pull/4278): fix typos in comments and a debug log message.
- [**OpenHands/software-agent-sdk**](https://github.com/OpenHands/software-agent-sdk) — [#3399](https://github.com/OpenHands/software-agent-sdk/pull/3399): pin ACP `npx` launchers to reviewed versions.
- [**OpenHands/OpenHands**](https://github.com/OpenHands/OpenHands) — [#14577](https://github.com/OpenHands/OpenHands/pull/14577): fix typos across comments, docstrings, and log messages.
- [**plastic-labs/honcho**](https://github.com/plastic-labs/honcho) — surprisal filter format for level observations.

**Language tooling & lexers**

- [**astral-sh/ruff**](https://github.com/astral-sh/ruff) — [#26318](https://github.com/astral-sh/ruff/pull/26318): skip `D418` (`overload-with-docstring`) in stub files, where overloads cannot carry the docstring on an implementation.
- [**pygments/pygments**](https://github.com/pygments/pygments) — five lexer/formatter fixes: Kotlin nullable-type marker ([#3178](https://github.com/pygments/pygments/pull/3178)), C++ function after a namespace body ([#3176](https://github.com/pygments/pygments/pull/3176)), LaTeX embedded-lexer options ([#3175](https://github.com/pygments/pygments/pull/3175)), TypeScript `module`-keyword whitespace ([#3172](https://github.com/pygments/pygments/pull/3172)), and Ruby unterminated-heredoc duplication ([#3171](https://github.com/pygments/pygments/pull/3171)).

**Developer & infra tooling**

- [**rclone/rclone**](https://github.com/rclone/rclone) — goroutine leak in `NewStatsGroup` for zero-transfer rc jobs ([#9568](https://github.com/rclone/rclone/pull/9568)); `serve webdav` default `Overwrite: T` for COPY/MOVE ([#9558](https://github.com/rclone/rclone/pull/9558)).
- [**goreleaser/goreleaser**](https://github.com/goreleaser/goreleaser) — [#6684](https://github.com/goreleaser/goreleaser/pull/6684): default the winget head branch to a versioned template.
- [**astral-sh/uv**](https://github.com/astral-sh/uv) — [#19983](https://github.com/astral-sh/uv/pull/19983): explain why files are skipped during registry index parsing.
- [**helix-editor/helix**](https://github.com/helix-editor/helix) — [#15939](https://github.com/helix-editor/helix/pull/15939): editorconfig test coverage for empty alternate brace groups.
- [**prowler-cloud/prowler**](https://github.com/prowler-cloud/prowler) — [#11823](https://github.com/prowler-cloud/prowler/pull/11823): skip `MANUAL` findings in the compliance section tally to avoid a `KeyError`.
- [**1Panel-dev/1Panel**](https://github.com/1Panel-dev/1Panel) — IPv6 hosts in self-signed SSL flow, `exec.LookPath` for `which()` cross-platform detection.

**Python libraries**

- [**rthalley/dnspython**](https://github.com/rthalley/dnspython) — [#1279](https://github.com/rthalley/dnspython/pull/1279): raise `BadTTL` for non-decimal Unicode digits in `dns.ttl.from_text()`.
- [**lepture/mistune**](https://github.com/lepture/mistune) — [#462](https://github.com/lepture/mistune/pull/462): escape literal emphasis markers in `MarkdownRenderer`.
- [**wireservice/agate**](https://github.com/wireservice/agate) — [#813](https://github.com/wireservice/agate/pull/813): fix `Table.from_fixed` reading data as schema for a file-like `schema_path`.
- [**kvesteri/sqlalchemy-utils**](https://github.com/kvesteri/sqlalchemy-utils) — [#812](https://github.com/kvesteri/sqlalchemy-utils/pull/812): fix `PasswordType` dropping updates when the column was previously NULL.
- [**neuml/txtai**](https://github.com/neuml/txtai) — [#1125](https://github.com/neuml/txtai/pull/1125): raise `SQLError` on unterminated bracket and function clauses.
- [**dottxt-ai/outlines**](https://github.com/dottxt-ai/outlines) — [#1898](https://github.com/dottxt-ai/outlines/pull/1898): don't require a provider's optional SDK to normalize errors.
- [**marshmallow-code/webargs**](https://github.com/marshmallow-code/webargs) — [#1076](https://github.com/marshmallow-code/webargs/pull/1076): modernize the aiohttpparser docstring example.
- [**vimalloc/flask-jwt-extended**](https://github.com/vimalloc/flask-jwt-extended) — [#579](https://github.com/vimalloc/flask-jwt-extended/pull/579): replace deprecated `datetime.utcnow()`.
- [**tweepy/tweepy**](https://github.com/tweepy/tweepy) — [#2241](https://github.com/tweepy/tweepy/pull/2241): replace deprecated `datetime.utcnow()` in `MongodbCache.store`.
- [**wolph/python-progressbar**](https://github.com/wolph/python-progressbar) — [#318](https://github.com/wolph/python-progressbar/pull/318): detect color support for `xterm-*` TERM values.

**Web, media & apps**

- [**mantinedev/mantine**](https://github.com/mantinedev/mantine) — [#8971](https://github.com/mantinedev/mantine/issues/8971): mark non-`menuitem` children inside `Menu.Dropdown` (autofocus placeholder, floating arrow) as `role="presentation"` for WAI-ARIA 1.2 compliance.
- [**suitenumerique/meet**](https://github.com/suitenumerique/meet) — role terminology consistency across localizations.
- [**Stremio/stremio-web**](https://github.com/Stremio/stremio-web) — Lithuanian ISO 639-2 language code fix.
- [**NuvioMedia/NuvioTV**](https://github.com/NuvioMedia/NuvioTV) — keyboard `Next` action restored on Android TV, subtitle-delay reset shortcut.
- [**Flexget/Flexget**](https://github.com/Flexget/Flexget) — recursive `exists_series` for nested season folders, video-only matching to skip subtitles and metadata.

In flight: [**MemTensor/MemOS**](https://github.com/MemTensor/MemOS) — 5 open PRs covering retry-after handling, JSON5-tolerant config patching, partial L3 abstraction salvage, auto-recall timeout, accurate memory counts.

## Stack

Swift · Go · TypeScript · Python · Rust · Node · Postgres · Redis · ClickHouse · Docker · GCP · AWS · React · Three.js · PyTorch · TensorFlow · macOS / IOKit / SwiftUI

## Selected publications

- **Drowsiness Detection with OpenCV** — *IEEE ICESC 2021.* [10.1109/ICESC51422.2021.9532758](https://doi.org/10.1109/icesc51422.2021.9532758) · [code](https://github.com/Sanjays2402/Drowsiness-Detection-with-OpenCV)
- **Animal Detection for Road Safety using Deep Learning** — *IEEE ICCICA 2021.* [10.1109/ICCICA52458.2021.9697287](https://doi.org/10.1109/iccica52458.2021.9697287)
- **Model Proposal for a YOLO Object Detection Algorithm based Social Distancing Detection System** — *IEEE ICCICA 2021.* [10.1109/ICCICA52458.2021.9697212](https://doi.org/10.1109/iccica52458.2021.9697212)
- **Computer Vision based Road Lane Detection** — *Artificial & Computational Intelligence, 2021.*
- **Recognition of Pneumonia from X-Ray Image Patterns using Convolutional Neural Networks** — 2021. [code](https://github.com/Sanjays2402/Pneumonia_Detection)

## Research

- [Google Scholar](https://scholar.google.com/citations?user=qjNjjMYAAAAJ&hl=en)
- [ORCID 0000-0001-6339-9651](https://orcid.org/0000-0001-6339-9651)
- [IEEE](https://ieeexplore.ieee.org/author/37089308978)
- [ResearchGate](https://www.researchgate.net/profile/Sanjay-Santhanam-2)

## Contact

- Email — [sanjays2402@gmail.com](mailto:sanjays2402@gmail.com)
- LinkedIn — [linkedin.com/in/sanjay24](https://www.linkedin.com/in/sanjay24/)
