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
- [**gilch/hissp**](https://github.com/gilch/hissp): [#327](https://github.com/gilch/hissp/pull/327) falls back to a higher pickle protocol when protocol 0 fails.
- [**davidhalter/parso**](https://github.com/davidhalter/parso): [#242](https://github.com/davidhalter/parso/pull/242) stops treating a walrus argument as a keyword argument.
- [**trentm/python-markdown2**](https://github.com/trentm/python-markdown2): [#719](https://github.com/trentm/python-markdown2/pull/719) treats `head` and `style` as block-level tags.
- [**PyCQA/docformatter**](https://github.com/PyCQA/docformatter): [#364](https://github.com/PyCQA/docformatter/pull/364) stops treating a bracketed string literal as an attribute docstring; [#363](https://github.com/PyCQA/docformatter/pull/363) stops splitting a summary on a period inside an inline literal; [#362](https://github.com/PyCQA/docformatter/pull/362) stops emitting stray newline tokens before a trailing comment.
- [**PyCQA/autoflake**](https://github.com/PyCQA/autoflake): [#361](https://github.com/PyCQA/autoflake/pull/361) treats interpreter builtin modules as safe imports.
- [**tconbeer/sqlfmt**](https://github.com/tconbeer/sqlfmt): [#843](https://github.com/tconbeer/sqlfmt/pull/843) stops treating semicolons inside comments as statement terminators.
- [**pylint-dev/pylint**](https://github.com/pylint-dev/pylint): [#11187](https://github.com/pylint-dev/pylint/pull/11187) fixes an `assignment-from-no-return` false positive on a trailing raise.
- [**pylint-dev/astroid**](https://github.com/pylint-dev/astroid): [#3152](https://github.com/pylint-dev/astroid/pull/3152) only adds the `_HAS_DEFAULT_FACTORY` sentinel when a `default_factory` is used.

**Developer & infra tooling**

- [**codespell-project/codespell**](https://github.com/codespell-project/codespell): [#3975](https://github.com/codespell-project/codespell/pull/3975) scopes TOML configuration reads to `[tool.codespell]`.
- [**fsspec/filesystem_spec**](https://github.com/fsspec/filesystem_spec): [#2072](https://github.com/fsspec/filesystem_spec/pull/2072) fixes S3 parent paths in `ArrowFSWrapper`; [#2074](https://github.com/fsspec/filesystem_spec/pull/2074) fixes removal of directory symlinks in `LocalFileSystem`.
- [**shanevcantwell/llauncher**](https://github.com/shanevcantwell/llauncher): [#353](https://github.com/shanevcantwell/llauncher/pull/353) keeps same-model servers distinct by port in the UI.
- [**mila-iqia/cluv**](https://github.com/mila-iqia/cluv): [#144](https://github.com/mila-iqia/cluv/pull/144) preserves an existing results directory during initialization.
- [**ministackorg/ministack**](https://github.com/ministackorg/ministack): [#1089](https://github.com/ministackorg/ministack/pull/1089) honors `LogType` when returning Lambda invocation logs.
- [**wntrblm/nox**](https://github.com/wntrblm/nox): [#1127](https://github.com/wntrblm/nox/pull/1127) corrects `python_versions()` minimum resolution for major-only and multiple lower bounds.
- [**urwid/urwid**](https://github.com/urwid/urwid): [#1187](https://github.com/urwid/urwid/pull/1187) copies signal-handler lists before emission so mutation cannot skip callbacks.
- [**BrianPugh/cyclopts**](https://github.com/BrianPugh/cyclopts): [#860](https://github.com/BrianPugh/cyclopts/pull/860) restores zsh subcommand completion after meta positionals.
- [**tomerfiliba/plumbum**](https://github.com/tomerfiliba/plumbum): [#838](https://github.com/tomerfiliba/plumbum/pull/838) ignores annotations for non-positional `main` parameters in the CLI layer.
- [**rclone/rclone**](https://github.com/rclone/rclone) — goroutine leak in `NewStatsGroup` for zero-transfer rc jobs ([#9568](https://github.com/rclone/rclone/pull/9568)); `serve webdav` default `Overwrite: T` for COPY/MOVE ([#9558](https://github.com/rclone/rclone/pull/9558)).
- [**goreleaser/goreleaser**](https://github.com/goreleaser/goreleaser) — [#6684](https://github.com/goreleaser/goreleaser/pull/6684): default the winget head branch to a versioned template.
- [**astral-sh/uv**](https://github.com/astral-sh/uv) — [#19983](https://github.com/astral-sh/uv/pull/19983): explain why files are skipped during registry index parsing.
- [**helix-editor/helix**](https://github.com/helix-editor/helix) — [#15939](https://github.com/helix-editor/helix/pull/15939): editorconfig test coverage for empty alternate brace groups.
- [**prowler-cloud/prowler**](https://github.com/prowler-cloud/prowler) — [#11823](https://github.com/prowler-cloud/prowler/pull/11823): skip `MANUAL` findings in the compliance section tally to avoid a `KeyError`.
- [**1Panel-dev/1Panel**](https://github.com/1Panel-dev/1Panel) — IPv6 hosts in the self-signed SSL flow ([#12652](https://github.com/1Panel-dev/1Panel/pull/12652)) and `exec.LookPath` for cross-platform command detection ([#12651](https://github.com/1Panel-dev/1Panel/pull/12651)).
- [**sqlfluff/sqlfluff**](https://github.com/sqlfluff/sqlfluff): [#8062](https://github.com/sqlfluff/sqlfluff/pull/8062) parses ClickHouse tuple-element access on arbitrary expressions.
- [**yfosp/start-here**](https://github.com/yfosp/start-here): [#953](https://github.com/yfosp/start-here/pull/953) adds Sanjay to the contributor list.
- [**napalm-automation/napalm**](https://github.com/napalm-automation/napalm): [#2333](https://github.com/napalm-automation/napalm/pull/2333) brackets literal IPv6 hosts when building the NX-API URL.
- [**Ericsson/codechecker**](https://github.com/Ericsson/codechecker): [#5002](https://github.com/Ericsson/codechecker/pull/5002) strips ANSI escapes from clang-tidy output when collecting mentioned files.
- [**soxoj/maigret**](https://github.com/soxoj/maigret): [#2924](https://github.com/soxoj/maigret/pull/2924) stops the `SUPPORTED_IDS` branch re-adding a rejected username in `extract_ids_from_page`.
- [**sartography/SpiffWorkflow**](https://github.com/sartography/SpiffWorkflow): [#483](https://github.com/sartography/SpiffWorkflow/pull/483) raises a clear `ValidationException` for a `ServiceTask` with no operator.
- [**casperdcl/git-fame**](https://github.com/casperdcl/git-fame): [#125](https://github.com/casperdcl/git-fame/pull/125) counts LOC and files when passing multiple repos.
- [**tqdm/shtab**](https://github.com/tqdm/shtab): [#221](https://github.com/tqdm/shtab/pull/221) treats `nargs=0` custom actions as flags in zsh; [#220](https://github.com/tqdm/shtab/pull/220) supports non-sequence choices in zsh completion.
- [**nicolargo/glances**](https://github.com/nicolargo/glances): [#3635](https://github.com/nicolargo/glances/pull/3635) resolves port alert level by severity instead of dict ordering; [#3626](https://github.com/nicolargo/glances/pull/3626) corrects the column/value mismatch for list plugins in TimescaleDB.
- [**boxed/mutmut**](https://github.com/boxed/mutmut): [#542](https://github.com/boxed/mutmut/pull/542) forwards the generator return value through the trampoline.
- [**mkb79/audible-cli**](https://github.com/mkb79/audible-cli): [#269](https://github.com/mkb79/audible-cli/pull/269) passes the config path to `click.edit` as a string.
- [**ipspace/netlab**](https://github.com/ipspace/netlab): [#3720](https://github.com/ipspace/netlab/pull/3720) catches `KeyboardInterrupt` when aborting test cleanup.
- [**MarketSquare/robotframework-robocop**](https://github.com/MarketSquare/robotframework-robocop): [#1786](https://github.com/MarketSquare/robotframework-robocop/pull/1786) marks `--ignore` values as matched for rules below `--threshold`.
- [**GothenburgBitFactory/bugwarrior**](https://github.com/GothenburgBitFactory/bugwarrior): [#1227](https://github.com/GothenburgBitFactory/bugwarrior/pull/1227) coerces the Logseq block id to an int for a stable unique key.
- [**opensteno/plover**](https://github.com/opensteno/plover): [#1857](https://github.com/opensteno/plover/pull/1857) escapes characters outside code page 1252 on RTF/CRE export.
- [**amanusk/s-tui**](https://github.com/amanusk/s-tui): [#296](https://github.com/amanusk/s-tui/pull/296) handles non-`IndexError` failures in graph and summary updates; [#295](https://github.com/amanusk/s-tui/pull/295) falls back to `/proc/device-tree/model` for the processor name.
- [**abrignoni/iLEAPP**](https://github.com/abrignoni/iLEAPP): [#1773](https://github.com/abrignoni/iLEAPP/pull/1773) skips `NoteStore.sqlite` files without the CloudKit table; [#1772](https://github.com/abrignoni/iLEAPP/pull/1772) handles alarms whose sound is a song.
- [**sipyourdrink-ltd/bernstein**](https://github.com/sipyourdrink-ltd/bernstein): [#3163](https://github.com/sipyourdrink-ltd/bernstein/pull/3163) fails loudly when no trend-scan fetcher is configured.
- [**microsoft/WinAppVSCE**](https://github.com/microsoft/WinAppVSCE): [#116](https://github.com/microsoft/WinAppVSCE/pull/116) resolves a relative `launch.json` `workingDirectory` against the workspace folder.
- [**GNS3/gns3-server**](https://github.com/GNS3/gns3-server): [#2833](https://github.com/GNS3/gns3-server/pull/2833) stops starting nodes when deleting a project; [#2831](https://github.com/GNS3/gns3-server/pull/2831) corrects an always-true state check in `DockerVM.stop()`.
- [**Kohei-Wada/taskdog**](https://github.com/Kohei-Wada/taskdog): [#1168](https://github.com/Kohei-Wada/taskdog/pull/1168) reports real statistics sections in `get_statistics`; [#1165](https://github.com/Kohei-Wada/taskdog/pull/1165) aligns the SQL `end_date` filter with whole-day semantics.
- [**doorstop-dev/doorstop**](https://github.com/doorstop-dev/doorstop): [#808](https://github.com/doorstop-dev/doorstop/pull/808) stops escaping dollar signs that delimit inline math in LaTeX export; [#802](https://github.com/doorstop-dev/doorstop/pull/802) reports links to inactive items as inactive rather than unknown.
- [**ebroecker/canmatrix**](https://github.com/ebroecker/canmatrix): [#919](https://github.com/ebroecker/canmatrix/pull/919) preserves the `NS_` new-symbols section on dbc-to-dbc conversion.
- [**mnemosyne-oss/mnemosyne**](https://github.com/mnemosyne-oss/mnemosyne): [#542](https://github.com/mnemosyne-oss/mnemosyne/pull/542) reports `memory_not_found` when invalidate matches no row.
- [**rmartin16/qbittorrent-api**](https://github.com/rmartin16/qbittorrent-api): [#644](https://github.com/rmartin16/qbittorrent-api/pull/644) preserves the cached client when slicing or copying `List` objects.
- [**ai-dynamo/aiperf**](https://github.com/ai-dynamo/aiperf): [#1195](https://github.com/ai-dynamo/aiperf/pull/1195) handles top-level JSON array responses.
- [**Bachmann1234/diff_cover**](https://github.com/Bachmann1234/diff_cover): [#612](https://github.com/Bachmann1234/diff_cover/pull/612) honors the `format` option from the config file.
- [**CodeGraphContext/CodeGraphContext**](https://github.com/CodeGraphContext/CodeGraphContext): [#1376](https://github.com/CodeGraphContext/CodeGraphContext/pull/1376) wires `PARALLEL_WORKERS` config to indexing concurrency.
- [**mstar-project/mstar**](https://github.com/mstar-project/mstar): [#190](https://github.com/mstar-project/mstar/pull/190) decodes streamed lines when `Content-Type` has no charset.
- [**carderne/signal-export**](https://github.com/carderne/signal-export): [#224](https://github.com/carderne/signal-export/pull/224) stops creating the output folder when no chats are exported.
- [**snstac/pytak**](https://github.com/snstac/pytak): [#104](https://github.com/snstac/pytak/pull/104) warns when WS TX sends raw XML to a TAK Protocol endpoint.
- [**archlinux/archinstall**](https://github.com/archlinux/archinstall): [#4670](https://github.com/archlinux/archinstall/pull/4670) adds ghostscript to the print service packages.
- [**apache/libcloud**](https://github.com/apache/libcloud): [#2173](https://github.com/apache/libcloud/pull/2173) includes IPv6 addresses in DigitalOcean node public/private IPs.
- [**common-workflow-language/cwltool**](https://github.com/common-workflow-language/cwltool): [#2316](https://github.com/common-workflow-language/cwltool/pull/2316) gives a meaningful error for an empty job order file.
- [**jorio/gitfourchette**](https://github.com/jorio/gitfourchette): [#130](https://github.com/jorio/gitfourchette/pull/130) reports Git's error instead of `NotImplementedError` on cherry-pick.
- [**papis/papis**](https://github.com/papis/papis): [#1212](https://github.com/papis/papis/pull/1212) makes YAML export appendable.

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
- [**lepture/mistune**](https://github.com/lepture/mistune) — [#462](https://github.com/lepture/mistune/pull/462): escape literal emphasis markers in `MarkdownRenderer`; [#471](https://github.com/lepture/mistune/pull/471): apply the escape flag to a user-supplied HTML renderer.
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
- [**aplbrain/grand-cypher**](https://github.com/aplbrain/grand-cypher): [#114](https://github.com/aplbrain/grand-cypher/pull/114) returns NULL from scalar functions given invalid argument types.
- [**sooperset/mcp-atlassian**](https://github.com/sooperset/mcp-atlassian): [#1550](https://github.com/sooperset/mcp-atlassian/pull/1550) surfaces the environment system field on `JiraIssue`.
- [**mpmath/mpmath**](https://github.com/mpmath/mpmath): [#1150](https://github.com/mpmath/mpmath/pull/1150) avoids spurious overflow in `fp.gammaprod`.
- [**deeplook/svglib**](https://github.com/deeplook/svglib): [#499](https://github.com/deeplook/svglib/pull/499) respects the `visibility` property on shapes; [#494](https://github.com/deeplook/svglib/pull/494) looks up unquoted font-family names containing spaces; [#493](https://github.com/deeplook/svglib/pull/493) respects `display:none` set via the `style` attribute.
- [**PyThaiNLP/pythainlp**](https://github.com/PyThaiNLP/pythainlp): [#1473](https://github.com/PyThaiNLP/pythainlp/pull/1473) romanizes royin words containing ฤ.
- [**optiland/optiland**](https://github.com/optiland/optiland): [#702](https://github.com/optiland/optiland/pull/702) adds descriptive messages to bare `ValueError` raises in paraxial.
- [**astropy/astropy**](https://github.com/astropy/astropy): [#20174](https://github.com/astropy/astropy/pull/20174) writes `solRad` and `solLum` instead of `Rsun` and `Lsun` in the CDS format.
- [**guessit-io/guessit**](https://github.com/guessit-io/guessit): [#942](https://github.com/guessit-io/guessit/pull/942) keeps the title when `alternative_title` is excluded; [#936](https://github.com/guessit-io/guessit/pull/936) keeps a leading country word that opens the title.
- [**MechanicalSoup/MechanicalSoup**](https://github.com/MechanicalSoup/MechanicalSoup): [#484](https://github.com/MechanicalSoup/MechanicalSoup/pull/484) detects HTML from raw leading bytes in `__looks_like_html`; [#483](https://github.com/MechanicalSoup/MechanicalSoup/pull/483) raises an explanatory error from `links()` when no page is loaded.
- [**gorakhargosh/watchdog**](https://github.com/gorakhargosh/watchdog): [#1183](https://github.com/gorakhargosh/watchdog/pull/1183) stops `PermissionError` killing the kqueue emitter thread on BSD.
- [**anymail/django-anymail**](https://github.com/anymail/django-anymail): [#479](https://github.com/anymail/django-anymail/pull/479) reports an unsupported feature for `merge_data` without `template_id`.
- [**pyathena-dev/PyAthena**](https://github.com/pyathena-dev/PyAthena): [#743](https://github.com/pyathena-dev/PyAthena/pull/743) returns the formatted DATE literal from `AthenaDate.process`.
- [**dynaconf/dynaconf**](https://github.com/dynaconf/dynaconf): [#1435](https://github.com/dynaconf/dynaconf/pull/1435) cleans up nested `dynaconf_merge` tokens when the parent key is new; [#1434](https://github.com/dynaconf/dynaconf/pull/1434) keeps sibling keys that share a dotted-path leaf name.
- [**invoice-x/invoice2data**](https://github.com/invoice-x/invoice2data): [#716](https://github.com/invoice-x/invoice2data/pull/716) emits a single CSV header row across all invoices.
- [**Ad-meliorael/percentify**](https://github.com/Ad-meliorael/percentify): [#35](https://github.com/Ad-meliorael/percentify/pull/35) keeps small p-values from rounding to zero in `correlate`.
- [**marcosschroh/dataclasses-avroschema**](https://github.com/marcosschroh/dataclasses-avroschema): [#964](https://github.com/marcosschroh/dataclasses-avroschema/pull/964) serializes records without fields to avro-json; [#963](https://github.com/marcosschroh/dataclasses-avroschema/pull/963) stops mutating `Meta.field_order` during schema generation.

**Web, media & apps**

- [**alphacrack/readme2demo**](https://github.com/alphacrack/readme2demo): [#134](https://github.com/alphacrack/readme2demo/pull/134) gives the step tutorial a distinct SEO title.
- [**mantinedev/mantine**](https://github.com/mantinedev/mantine): mark non-`menuitem` children inside `Menu.Dropdown` as presentational for WAI-ARIA 1.2 compliance ([#9004](https://github.com/mantinedev/mantine/pull/9004)); export the `FormProviderProps` type ([#9009](https://github.com/mantinedev/mantine/pull/9009)).
- [**suitenumerique/meet**](https://github.com/suitenumerique/meet) — standardized role terminology across localizations ([#1285](https://github.com/suitenumerique/meet/pull/1285)).
- [**Stremio/stremio-web**](https://github.com/Stremio/stremio-web) — Lithuanian ISO 639-2 language code fix ([#1230](https://github.com/Stremio/stremio-web/pull/1230)).
- [**NuvioMedia/NuvioTV**](https://github.com/NuvioMedia/NuvioTV) — restored the Android TV keyboard `Next` action ([#1453](https://github.com/NuvioMedia/NuvioTV/pull/1453)) and added a subtitle-delay reset shortcut ([#1452](https://github.com/NuvioMedia/NuvioTV/pull/1452)).
- [**Flexget/Flexget**](https://github.com/Flexget/Flexget) — recursive `exists_series` support for nested season folders ([#4987](https://github.com/Flexget/Flexget/pull/4987)) and video-only matching that skips subtitles and metadata ([#4986](https://github.com/Flexget/Flexget/pull/4986)).
- [**PaRaN01a-hash/ultra-max-addon**](https://github.com/PaRaN01a-hash/ultra-max-addon): [#15](https://github.com/PaRaN01a-hash/ultra-max-addon/pull/15) adds manifest behavior hints and ID prefixes for Nuvio compatibility.
- [**aliasvault/aliasvault**](https://github.com/aliasvault/aliasvault): [#1893](https://github.com/aliasvault/aliasvault/pull/1893) adds HTML, plain-text, and source views for email content.
- [**plotly/dash**](https://github.com/plotly/dash): [#3936](https://github.com/plotly/dash/pull/3936) uses the proxied URL as the Jupyter server URL.
- [**posit-dev/great-docs**](https://github.com/posit-dev/great-docs): [#299](https://github.com/posit-dev/great-docs/pull/299) preserves source order for sidebar subsections.
- [**Donkie/Spoolman**](https://github.com/Donkie/Spoolman): [#987](https://github.com/Donkie/Spoolman/pull/987) strips the leading `#` from filament color codes.
- [**reflex-dev/xy**](https://github.com/reflex-dev/xy): [#389](https://github.com/reflex-dev/xy/pull/389) floors the log axis lower bound when an explicit margin is set.
- [**wkentaro/labelme**](https://github.com/wkentaro/labelme): [#2425](https://github.com/wkentaro/labelme/pull/2425) degrades to stderr-only logging when the log file fails; [#2417](https://github.com/wkentaro/labelme/pull/2417) reports the decode allocation limit instead of "Allowed formats".
- [**GoogleChrome/chromium-dashboard**](https://github.com/GoogleChrome/chromium-dashboard): [#6656](https://github.com/GoogleChrome/chromium-dashboard/pull/6656) rejects milestone zero in `ChannelsAPI`.
- [**jacebrowning/memegen**](https://github.com/jacebrowning/memegen): [#1046](https://github.com/jacebrowning/memegen/pull/1046) only drops trailing blank lines when cleaning URLs.

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
