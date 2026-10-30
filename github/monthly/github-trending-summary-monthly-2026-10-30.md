# GitHub Trending Summary - Monthly - 2026-10-30

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-10-30 04:01 UTC |
| Scope | Monthly (month-to-date) |
| Date range | 2026-10-01 through 2026-10-30 |
| Ranking basis | Inferred monthly ranking: GitHub Search current stars among non-fork repositories created in the date range; recent pushes used as a freshness check |

## Headline

October’s standout new repositories span practical device utilities, AI inference and agent tooling, formal-math artifacts, and a conspicuous wave of Rust-native creative and productivity apps. This is an inferred snapshot, not a measured monthly star-gain chart: GitHub Search does not expose monthly star deltas, so the list uses current stars and activity recency as proxies.

## Top Repositories

1. **[Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv) - A utility for debloating Android and Google TV over Wi-Fi and replacing the home screen with a cleaner, Apple TV-style launcher.**

  **Language:** Python | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 45,631 | **Why notable:** It leads the October-created candidate set by current stars and addresses a concrete, highly visible consumer-device frustration.

2. **[deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) - DeepSeek’s high-performance inference framework, with optimized kernels, parallelism, asynchronous scheduling, and deterministic sampling described in its README.**

  **Language:** Python | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 24,290 | **Why notable:** It is the strongest infrastructure signal in the search-ranked cohort, linking model demand to production-scale inference engineering.

3. **[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) - An agent skill that builds interactive isometric illustrations of machines and complex systems using SVG, WebGL, and 3D effects.**

  **Language:** JavaScript | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 22,683 | **Why notable:** It shows agent skills expanding beyond code edits into structured visual explanation, and its README says it runs across several coding-agent environments.

4. **[google-research/harness2](https://github.com/google-research/harness2) - A plug-and-play framework for recursively improving agent harnesses against tasks not seen during harness design.**

  **Language:** Python | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 21,354 | **Why notable:** It makes the agent harness itself an optimization target, rather than treating prompts and tools as fixed scaffolding.

5. **[openai/math](https://github.com/openai/math) - A collection of mathematical manuscripts and supporting proof artifacts, with Lean formalizations being added over time.**

  **Language:** Lean | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 17,077 | **Why notable:** Its unusual mix of machine-produced research material and formal verification artifacts drew strong attention; the project explicitly says not every result is yet formalized or verified.

6. **[storytold/wordcraft](https://github.com/storytold/wordcraft) - A Rust word processor with DOCX support and desktop and browser targets; its README lists familiar document features such as styles, tables, track changes, and mail merge.**

  **Language:** Rust | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 16,635 | **Why notable:** It represents the month’s push to build ambitious, familiar productivity software as open-source native applications in Rust.

7. **[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) - A Linux boot-time tool whose project claims to unlock additional tensor throughput on supported GeForce RTX 20/30/40 cards.**

  **Language:** C | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 13,164 | **Why notable:** It connects local AI enthusiasm to GPU performance tuning; the throughput figures are project claims, not independently validated here.

8. **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) - A parametric 3D CAD application in Rust with a feature timeline, desktop and browser modes, and an MCP interface for agent-driven modeling.**

  **Language:** Rust | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 12,098 | **Why notable:** It combines a traditional engineering workflow with browser delivery and an explicit agent-automation surface.

9. **[seedds/nxnative](https://github.com/seedds/nxnative) - A project for running user-supplied Nintendo Switch game files natively on Apple devices, using a translation/HLE path and Metal graphics.**

  **Language:** Python | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 9,811 | **Why notable:** It is a high-interest example of platform-specific compatibility engineering; the README requires a recent Mac, Xcode, and user-supplied game files.

10. **[storytold/effectcraft](https://github.com/storytold/effectcraft) - A Rust motion-graphics and compositing application with layers, keyframes, effects, 3D cameras and lights, and a render queue.**

  **Language:** Rust | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 8,170 | **Why notable:** Alongside WordCraft, it illustrates the ArtCraft project family’s attempt to cover established creative-software workflows with native Rust apps; its README describes the project as young and moving fast.

## Trending Technologies and Themes

- **Agent tooling moves into the harness and the interface:** Google Research’s Harness² treats agent harnesses as recursively optimizable systems, while Anatomy packages visual explanation as a reusable agent skill; SolidCraft exposes CAD actions through MCP.
- **Rust-native creative and productivity apps:** WordCraft and EffectCraft (both from the ArtCraft family) plus SolidCraft point to continued interest in cross-platform native applications that target established office, compositing, and CAD workflows.
- **Inference performance remains a first-class engineering problem:** DeepInfer emphasizes optimized kernels, parallelism, and scheduling; gpu-unlock focuses on GPU throughput, although its performance claims have not been independently checked here.
- **Device ownership and local capability:** CleanYourTV targets control over a TV’s interface, while nxnative explores running user-provided software on Apple hardware. These are distinct projects, but both attract attention by changing what existing devices can do.
- **Languages in this ten-repository sample:** Python 4, Rust 3, JavaScript 1, Lean 1, and C 1. This is a small, star-ranked sample, not a measure of all GitHub activity.

## Takeaway

The strongest signal is not one new framework but a widening appetite for complete, locally useful products: agent infrastructure, inference optimization, device utilities, and desktop creative tools. Rust is especially visible in the latter category, while Python remains prominent in AI and device-adjacent projects. Treat the ranking as a month-to-date popularity proxy: GitHub’s current star totals and recent pushes do not establish how many stars each repository gained during October, nor do they independently validate project claims or maturity.

## Sources and Method

- **Primary source:** [GitHub Search - repositories created October 1-30, sorted by stars](https://github.com/search?q=created%3A2026-10-01..2026-10-30+stars%3A%3E100&type=repositories&s=stars&o=desc) and [GitHub Search API](https://api.github.com/search/repositories?q=created%3A2026-10-01..2026-10-30+stars%3A%3E100&sort=stars&order=desc&per_page=20).
- **Corroboration:** GitHub REST repository, README, and default-branch commit endpoints were checked for the listed repositories; Search returned 2,268 matches for the query. The ten displayed repositories are non-forks and were checked for current star totals, recent push dates, and default-branch commit SHAs.
- **Method note:** Monthly ranking is inferred from current stars among repositories created during the month, with push recency used as a freshness signal. GitHub does not provide a monthly star-gain figure in these Search results; all monthly gains are therefore reported as unavailable. README feature/performance statements are attributed to the projects and are not independent tests. No prior-month comparable snapshot was available, so no Notable Shifts section is claimed.
