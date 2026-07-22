# Sanjay Santhanam

I build things end-to-end - backends, systems, ML, developer tools, native apps, browser games, and the occasional TUI. M.S. in Computer Science, Syracuse University.

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

- [**openclaw/openclaw**](https://github.com/openclaw/openclaw) — agent runtime fixes for streamed-reply recovery ([#71467](https://github.com/openclaw/openclaw/pull/71467)), secrets auditing ([#69581](https://github.com/openclaw/openclaw/pull/69581)), Codex compaction auth ([#86418](https://github.com/openclaw/openclaw/pull/86418)), memory-core warning suppression ([#69941](https://github.com/openclaw/openclaw/pull/69941)), Discord voice session reuse ([#97746](https://github.com/openclaw/openclaw/pull/97746)), PluralKit DM pairing ([#86397](https://github.com/openclaw/openclaw/pull/86397)), omitted synthetic `maxTokens` fallbacks ([#98312](https://github.com/openclaw/openclaw/pull/98312)), and clearer plugin-install failures ([#98497](https://github.com/openclaw/openclaw/pull/98497)).
- [**HKUDS/LightRAG**](https://github.com/HKUDS/LightRAG): [#3406](https://github.com/HKUDS/LightRAG/pull/3406) exposes the thinking-token budget in role configuration.
- [**OpenAgentHQ/openagent-eval**](https://github.com/OpenAgentHQ/openagent-eval): [#170](https://github.com/OpenAgentHQ/openagent-eval/pull/170) normalizes naive staleness timestamps in corpus evaluation; [#192](https://github.com/OpenAgentHQ/openagent-eval/pull/192) includes the diagnosis step in structured error details.
- [**OpenAgentHQ/modeldock**](https://github.com/OpenAgentHQ/modeldock): [#146](https://github.com/OpenAgentHQ/modeldock/pull/146) verifies that an Ollama model exists after a pull completes.
- [**bradygaster/squad**](https://github.com/bradygaster/squad): [#1492](https://github.com/bradygaster/squad/pull/1492) prevents binary corruption when files under `.squad/` are externalized and restored.
- [**MakazhanAlpamys/Soup**](https://github.com/MakazhanAlpamys/Soup): [#315](https://github.com/MakazhanAlpamys/Soup/pull/315) runs built-in benchmark gate tasks during evaluation.
- [**turnstonelabs/turnstone**](https://github.com/turnstonelabs/turnstone): [#862](https://github.com/turnstonelabs/turnstone/pull/862) records operator skill changes in session history.
- [**repowise-dev/repowise**](https://github.com/repowise-dev/repowise): [#848](https://github.com/repowise-dev/repowise/pull/848) uses synchronous execution for webhook jobs.
- [**memtomem/memtomem**](https://github.com/memtomem/memtomem): [#1793](https://github.com/memtomem/memtomem/pull/1793) splits oversized Markdown parts during chunking.
- [**academy-agents/academy**](https://github.com/academy-agents/academy): [#433](https://github.com/academy-agents/academy/pull/433) fixes the default Academy home-directory location.
- [**garrytan/gbrain**](https://github.com/garrytan/gbrain): [#1554](https://github.com/garrytan/gbrain/pull/1554) replaces a POSIX-only postinstall shim with a cross-platform Node implementation.
- [**laceyp99/conductor-core**](https://github.com/laceyp99/conductor-core): [#20](https://github.com/laceyp99/conductor-core/pull/20) logs unsupported Google reasoning-effort values instead of silently accepting them.
- [**nesquena/hermes-webui**](https://github.com/nesquena/hermes-webui) — direct merges for an endless-scroll race ([#1949](https://github.com/nesquena/hermes-webui/pull/1949)), streaming timing ([#1599](https://github.com/nesquena/hermes-webui/pull/1599)), mobile keyboard Enter behavior ([#3130](https://github.com/nesquena/hermes-webui/pull/3130)), session-refresh polling ([#3129](https://github.com/nesquena/hermes-webui/pull/3129)), Docker guidance ([#2950](https://github.com/nesquena/hermes-webui/pull/2950)), provider-key errors ([#2949](https://github.com/nesquena/hermes-webui/pull/2949)), and transcript tool-card styling ([#2948](https://github.com/nesquena/hermes-webui/pull/2948)); release-integrated contributions for expired clarify prompts ([#4524](https://github.com/nesquena/hermes-webui/pull/4524)), bounded non-git context walks ([#4225](https://github.com/nesquena/hermes-webui/pull/4225)), paused cron grouping ([#4223](https://github.com/nesquena/hermes-webui/pull/4223)), default CLI-session visibility ([#4222](https://github.com/nesquena/hermes-webui/pull/4222)), external-session files ([#3314](https://github.com/nesquena/hermes-webui/pull/3314)), ephemeral turn fields ([#3313](https://github.com/nesquena/hermes-webui/pull/3313), [#3131](https://github.com/nesquena/hermes-webui/pull/3131)), remote gateway health ([#3312](https://github.com/nesquena/hermes-webui/pull/3312)), SSE connection handling ([#3128](https://github.com/nesquena/hermes-webui/pull/3128)), intermediate-message navigation ([#3127](https://github.com/nesquena/hermes-webui/pull/3127)), model-picker keyboard navigation ([#2952](https://github.com/nesquena/hermes-webui/pull/2952)), cross-container liveness ([#1887](https://github.com/nesquena/hermes-webui/pull/1887)), provider configuration ([#1883](https://github.com/nesquena/hermes-webui/pull/1883), [#1783](https://github.com/nesquena/hermes-webui/pull/1783)), and streaming scroll unpinning ([#1732](https://github.com/nesquena/hermes-webui/pull/1732)).
- [**outsourc-e/hermes-workspace**](https://github.com/outsourc-e/hermes-workspace) — slash-menu autocomplete ([#251](https://github.com/outsourc-e/hermes-workspace/pull/251)), a distinct gateway-auth-rejected path ([#250](https://github.com/outsourc-e/hermes-workspace/pull/250)), and a dashboard health probe integrated through a shared commit ([#289](https://github.com/outsourc-e/hermes-workspace/pull/289)).
- [**MrReasonable/sluice**](https://github.com/MrReasonable/sluice): the empty Claude Max response guard from [#33](https://github.com/MrReasonable/sluice/pull/33) landed through replacement PR #37.
- [**steipete/CodexBar**](https://github.com/steipete/CodexBar): the missing `five_hour` OAuth fallback from [#741](https://github.com/steipete/CodexBar/pull/741) was folded into a maintainer patch on `main`.
- [**huggingface/huggingface_hub**](https://github.com/huggingface/huggingface_hub) — [#4278](https://github.com/huggingface/huggingface_hub/pull/4278): fix typos in comments and a debug log message.
- [**OpenHands/software-agent-sdk**](https://github.com/OpenHands/software-agent-sdk) — [#3399](https://github.com/OpenHands/software-agent-sdk/pull/3399): pin ACP `npx` launchers to reviewed versions.
- [**OpenHands/OpenHands**](https://github.com/OpenHands/OpenHands) — [#14577](https://github.com/OpenHands/OpenHands/pull/14577): fix typos across comments, docstrings, and log messages.
- [**plastic-labs/honcho**](https://github.com/plastic-labs/honcho) — corrected the surprisal filter format for level observations ([#581](https://github.com/plastic-labs/honcho/pull/581)).
- [**dkedar7/streamlit-mcp**](https://github.com/dkedar7/streamlit-mcp) — [#63](https://github.com/dkedar7/streamlit-mcp/pull/63) accepts typed current values in schemas for widgets with non-string options.

**Language tooling & lexers**

- [**astral-sh/ruff**](https://github.com/astral-sh/ruff) — [#26318](https://github.com/astral-sh/ruff/pull/26318): skip `D418` (`overload-with-docstring`) in stub files, where overloads cannot carry the docstring on an implementation.
- [**pygments/pygments**](https://github.com/pygments/pygments): 15 lexer and formatter fixes across Kotlin ([#3178](https://github.com/pygments/pygments/pull/3178), [#3212](https://github.com/pygments/pygments/pull/3212)), C++ ([#3176](https://github.com/pygments/pygments/pull/3176)), LaTeX/TeX ([#3175](https://github.com/pygments/pygments/pull/3175), [#3204](https://github.com/pygments/pygments/pull/3204)), TypeScript ([#3172](https://github.com/pygments/pygments/pull/3172)), Ruby ([#3171](https://github.com/pygments/pygments/pull/3171)), Vala ([#3206](https://github.com/pygments/pygments/pull/3206), [#3207](https://github.com/pygments/pygments/pull/3207)), Jsonnet ([#3208](https://github.com/pygments/pygments/pull/3208)), YAML ([#3209](https://github.com/pygments/pygments/pull/3209)), SCSS ([#3210](https://github.com/pygments/pygments/pull/3210)), Kusto ([#3211](https://github.com/pygments/pygments/pull/3211)), C# ([#3213](https://github.com/pygments/pygments/pull/3213)), and JSX ([#3214](https://github.com/pygments/pygments/pull/3214)).

**Developer & infra tooling**

- [**codespell-project/codespell**](https://github.com/codespell-project/codespell): [#3975](https://github.com/codespell-project/codespell/pull/3975) scopes TOML configuration reads to `[tool.codespell]`.
- [**fsspec/filesystem_spec**](https://github.com/fsspec/filesystem_spec): [#2072](https://github.com/fsspec/filesystem_spec/pull/2072) fixes S3 parent paths in `ArrowFSWrapper`; [#2074](https://github.com/fsspec/filesystem_spec/pull/2074) fixes removal of directory symlinks in `LocalFileSystem`.
- [**shanevcantwell/llauncher**](https://github.com/shanevcantwell/llauncher): [#353](https://github.com/shanevcantwell/llauncher/pull/353) keeps same-model servers distinct by port in the UI.
- [**mila-iqia/cluv**](https://github.com/mila-iqia/cluv): [#144](https://github.com/mila-iqia/cluv/pull/144) preserves an existing results directory during initialization.
- [**ministackorg/ministack**](https://github.com/ministackorg/ministack): [#1089](https://github.com/ministackorg/ministack/pull/1089) honors `LogType` when returning Lambda invocation logs.
- [**wntrblm/nox**](https://github.com/wntrblm/nox): [#1127](https://github.com/wntrblm/nox/pull/1127) corrects `python_versions()` minimum resolution for major-only and multiple lower bounds.
- [**urwid/urwid**](https://github.com/urwid/urwid): [#1187](https://github.com/urwid/urwid/pull/1187) copies signal-handler lists before emission so mutation cannot skip callbacks.
- [**BrianPugh/cyclopts**](https://github.com/BrianPugh/cyclopts): [#860](https://github.com/BrianPugh/cyclopts/pull/860) restores zsh subcommand completion after meta positionals.
- [**rclone/rclone**](https://github.com/rclone/rclone) — goroutine leak in `NewStatsGroup` for zero-transfer rc jobs ([#9568](https://github.com/rclone/rclone/pull/9568)); `serve webdav` default `Overwrite: T` for COPY/MOVE ([#9558](https://github.com/rclone/rclone/pull/9558)).
- [**goreleaser/goreleaser**](https://github.com/goreleaser/goreleaser) — [#6684](https://github.com/goreleaser/goreleaser/pull/6684): default the winget head branch to a versioned template.
- [**astral-sh/uv**](https://github.com/astral-sh/uv) — [#19983](https://github.com/astral-sh/uv/pull/19983): explain why files are skipped during registry index parsing.
- [**helix-editor/helix**](https://github.com/helix-editor/helix) — [#15939](https://github.com/helix-editor/helix/pull/15939): editorconfig test coverage for empty alternate brace groups.
- [**prowler-cloud/prowler**](https://github.com/prowler-cloud/prowler) — [#11823](https://github.com/prowler-cloud/prowler/pull/11823): skip `MANUAL` findings in the compliance section tally to avoid a `KeyError`.
- [**1Panel-dev/1Panel**](https://github.com/1Panel-dev/1Panel) — IPv6 hosts in the self-signed SSL flow ([#12652](https://github.com/1Panel-dev/1Panel/pull/12652)) and `exec.LookPath` for cross-platform command detection ([#12651](https://github.com/1Panel-dev/1Panel/pull/12651)).
- [**sqlfluff/sqlfluff**](https://github.com/sqlfluff/sqlfluff): [#8062](https://github.com/sqlfluff/sqlfluff/pull/8062) parses ClickHouse tuple-element access on arbitrary expressions.
- [**yfosp/start-here**](https://github.com/yfosp/start-here): [#953](https://github.com/yfosp/start-here/pull/953) adds Sanjay to the contributor list.

**Python libraries**

- [**chardet/chardet**](https://github.com/chardet/chardet): [#372](https://github.com/chardet/chardet/pull/372) stops ASCII `+<digits>` text from being misdetected as UTF-7.
- [**uqfoundation/dill**](https://github.com/uqfoundation/dill): [#764](https://github.com/uqfoundation/dill/pull/764) marks `TestNamespace` as a non-test class during collection.
- [**mahmoud/boltons**](https://github.com/mahmoud/boltons): [#418](https://github.com/mahmoud/boltons/pull/418) prevents `singularize()` from mangling words ending in `ss`.
- [**redis/redis-py**](https://github.com/redis/redis-py): [#4193](https://github.com/redis/redis-py/pull/4193) restores Sentinel connection-pool capacity after failover.
- [**pydantic/pydantic-settings**](https://github.com/pydantic/pydantic-settings): [#910](https://github.com/pydantic/pydantic-settings/pull/910) parses enum names through nested annotations.
- [**pydantic/pydantic-extra-types**](https://github.com/pydantic/pydantic-extra-types): [#403](https://github.com/pydantic/pydantic-extra-types/pull/403) rejects non-ASCII digits in ABA routing numbers.
- [**jd/tenacity**](https://github.com/jd/tenacity): [#654](https://github.com/jd/tenacity/pull/654) avoids unnecessary exponential-wait computation.
- [**GrahamDumpleton/wrapt**](https://github.com/GrahamDumpleton/wrapt): [#345](https://github.com/GrahamDumpleton/wrapt/pull/345) makes `bytes()` on a proxy match the wrapped object.
- [**splintered-reality/py_trees**](https://github.com/splintered-reality/py_trees): [#505](https://github.com/splintered-reality/py_trees/pull/505) recovers memory sequences after child replacement.
- [**nose-devs/nose2**](https://github.com/nose-devs/nose2): [#674](https://github.com/nose-devs/nose2/pull/674) fixes JUnit XML timestamps for subtests.
- [**python-poetry/tomlkit**](https://github.com/python-poetry/tomlkit): [#551](https://github.com/python-poetry/tomlkit/pull/551) preserves a multiline string's leading newline when built with `string()`.
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
- [**jab/bidict**](https://github.com/jab/bidict): [#380](https://github.com/jab/bidict/pull/380) materializes `product()` inputs passed to parametrized tests.
- [**fabiocaccamo/python-benedict**](https://github.com/fabiocaccamo/python-benedict): [#583](https://github.com/fabiocaccamo/python-benedict/pull/583) handles non-string dictionary keys that contain lists in key-list and key-path traversal.
- [**more-itertools/more-itertools**](https://github.com/more-itertools/more-itertools): [#1200](https://github.com/more-itertools/more-itertools/pull/1200) rejects negative slice sizes in `sliced()`.
- [**Yakifo/amqtt**](https://github.com/Yakifo/amqtt) — [#350](https://github.com/Yakifo/amqtt/pull/350) treats empty or truncated MQTT fixed-header reads as end-of-stream.

**Web, media & apps**

- [**alphacrack/readme2demo**](https://github.com/alphacrack/readme2demo): [#134](https://github.com/alphacrack/readme2demo/pull/134) gives the step tutorial a distinct SEO title.
- [**mantinedev/mantine**](https://github.com/mantinedev/mantine): mark non-`menuitem` children inside `Menu.Dropdown` as presentational for WAI-ARIA 1.2 compliance ([#9004](https://github.com/mantinedev/mantine/pull/9004)); export the `FormProviderProps` type ([#9009](https://github.com/mantinedev/mantine/pull/9009)).
- [**suitenumerique/meet**](https://github.com/suitenumerique/meet) — standardized role terminology across localizations ([#1285](https://github.com/suitenumerique/meet/pull/1285)).
- [**Stremio/stremio-web**](https://github.com/Stremio/stremio-web) — Lithuanian ISO 639-2 language code fix ([#1230](https://github.com/Stremio/stremio-web/pull/1230)).
- [**NuvioMedia/NuvioTV**](https://github.com/NuvioMedia/NuvioTV) — restored the Android TV keyboard `Next` action ([#1453](https://github.com/NuvioMedia/NuvioTV/pull/1453)) and added a subtitle-delay reset shortcut ([#1452](https://github.com/NuvioMedia/NuvioTV/pull/1452)).
- [**Flexget/Flexget**](https://github.com/Flexget/Flexget) — recursive `exists_series` support for nested season folders ([#4987](https://github.com/Flexget/Flexget/pull/4987)) and video-only matching that skips subtitles and metadata ([#4986](https://github.com/Flexget/Flexget/pull/4986)).
- [**PaRaN01a-hash/ultra-max-addon**](https://github.com/PaRaN01a-hash/ultra-max-addon): [#15](https://github.com/PaRaN01a-hash/ultra-max-addon/pull/15) adds manifest behavior hints and ID prefixes for Nuvio compatibility.
- [**aliasvault/aliasvault**](https://github.com/aliasvault/aliasvault): [#1893](https://github.com/aliasvault/aliasvault/pull/1893) adds HTML, plain-text, and source views for email content.

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
