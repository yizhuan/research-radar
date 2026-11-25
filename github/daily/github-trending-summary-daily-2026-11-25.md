# GitHub Trending Summary - Daily - 2026-11-25

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-11-25 03:21 UTC (signal file generated 03:20:09 UTC) |
| Scope | Daily |
| Date range | 2026-11-25 through 2026-11-25 |
| Ranking basis | GitHub Trending daily star gains, ordered by the supplied candidate score; score components and 30-day trending days used as supporting signals |

## Headline

The strongest signal is a wave of agent-oriented developer tooling: security skills, reusable coding-agent workflows, and CLIs that make existing software usable by agents. The ten leading supplied candidates gained 703–1,826 stars in today's Trending view; each had appeared on Trending on five days in the last 30 days.

## Top Repositories

1. **[elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) - A Claude Code bundle for authorized bug hunting and red-team work, organized as skills, commands, vulnerability patterns, and reporting workflows.**

  **Language:** Python | **Stars gained in window:** +1,826 | **Total stars:** 21,629 | **Why notable:** Highest supplied candidate score (10.010), daily gain, and Trending rank (#1); its README describes a layered workflow spanning methodology, web-app hunting, enterprise attack chains, and evidence/reporting.

2. **[XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) - A cross-platform desktop downloader covering common web, streaming, peer-to-peer, and file-hosting sources.**

  **Language:** Python | **Stars gained in window:** +1,092 | **Total stars:** 17,478 | **Why notable:** Second-highest supplied score (9.497) and a broad, integrated download workflow across Windows, macOS, Linux, and Android.

3. **[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) - A toolkit and community registry for creating command-line harnesses that let AI agents operate existing software.**

  **Language:** Python | **Stars gained in window:** +1,074 | **Total stars:** 64,925 | **Why notable:** Score 9.480 and daily Trending rank #3; its README emphasizes generated software-specific CLIs plus a hub for browsing and installing community harnesses.

4. **[obra/superpowers](https://github.com/obra/superpowers) - A cross-agent software-development methodology packaged as composable skills and instructions.**

  **Language:** Shell | **Stars gained in window:** +1,003 | **Total stars:** 325,907 | **Why notable:** Score 9.412 and daily Trending rank #2; its documented flow moves from clarifying a spec and reviewing a design to planned, test-driven, subagent-led implementation.

5. **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) - Web search, scraping, crawling, and data access tools aimed at agent knowledge workflows.**

  **Language:** TypeScript | **Stars gained in window:** +991 | **Total stars:** 209,039 | **Why notable:** Score 9.400 and daily Trending rank #6; the README distinguishes a local binary/MCP/API path, a hosted service, and a self-hosted server.

6. **[zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) - An open-source AI video-clipping and content-repurposing desktop tool for turning long recordings into short-form media.**

  **Language:** Python | **Stars gained in window:** +980 | **Total stars:** 15,485 | **Why notable:** Score 9.389, daily Trending rank #16; the repository page describes automated subtitles, covers, and publishing copy for major short-video platforms.

7. **[mjmirza/app-store-compliance](https://github.com/mjmirza/app-store-compliance) - A pre-submission playbook and guard for App Store and Google Play requirements.**

  **Language:** Shell | **Stars gained in window:** +928 | **Total stars:** 5,934 | **Why notable:** Score 9.334 and daily Trending rank #12; its listing combines rejection-pattern guidance, privacy checks, regulatory deadlines, and coding-agent support.

8. **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) - A diagram-design toolkit for coding agents, with 52 diagram types built from self-contained HTML and SVG.**

  **Language:** HTML | **Stars gained in window:** +802 | **Total stars:** 72,191 | **Why notable:** Score 9.188 and daily Trending rank #9; it represents a design-tooling strand alongside the more numerous agent workflow and infrastructure projects.

9. **[jingyaogong/minimind](https://github.com/jingyaogong/minimind) - A compact, from-scratch language-model training project with a documented end-to-end training path.**

  **Language:** Python | **Stars gained in window:** +727 | **Total stars:** 70,347 | **Why notable:** Score 9.090 and daily Trending rank #4; its README describes a small model intended to make training and experimentation feasible on modest personal hardware.

10. **[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) - An agent skill that researches a topic across social, video, forum, prediction-market, and web sources.**

  **Language:** Python | **Stars gained in window:** +703 | **Total stars:** 74,314 | **Why notable:** Score 9.057 and daily Trending rank #10; it extends the agent-skill pattern from coding into multi-source research and grounded synthesis.

## Trending Technologies and Themes

- **Agent-native software access and coding workflows:** CLI-Anything turns applications into agent-facing CLIs; Superpowers and Claude-BugHunter package workflows as skills; last30days-skill applies the same skill pattern to research.
- **Agent knowledge infrastructure:** Firecrawl provides local, hosted, and self-hosted routes for scraping and search; last30days-skill combines multiple source types into research outputs.
- **Focused end-user tools:** Ghost-Downloader-3 and AutoClip show strong daily momentum for practical media and download applications, rather than only model infrastructure.
- **Specialist applications remain visible:** App-store-compliance targets release readiness, diagram-design targets agent-produced visual communication, and MiniMind targets hands-on model training.
- **Languages:** Python leads the selected set (6/10), followed by TypeScript (1), Shell (2), and HTML (1). GitHub's repository metadata supplied these primary-language labels.

## Takeaway

Today's list is led by tooling that makes agents more capable through reusable workflows, software interfaces, and access to external knowledge—not by a single model release. The set also has substantial non-agent utility momentum, especially in downloading and video repurposing. These gains are a one-day Trending signal, not evidence by themselves of long-term adoption; historical star-delta snapshots were unavailable for this run.

## Sources and Method

- **Primary source:** [GitHub Trending - daily](https://github.com/trending?since=daily); the supplied signal file is `/home/yizhuan/.research/github/daily/github-trending-summary-daily-2026-11-25.signals.json`.
- **Repository verification:** Each listed GitHub repository page and README was checked. Public GitHub Search API queries of the form `GET /search/repositories?q=repo:<owner>/<repo>&per_page=5` returned an exact repository match for all ten. GitHub REST repository and default-branch commit endpoints confirmed current stars, primary language, branch, and commit SHA for every entry.
- **Ranking and signal values:** The exact stars-gained figures, daily Trending rank, total stars-at-collection, 30-day Trending days, and supplied scores are from the matching daily signal file; results are ordered by its candidate score (score combines normalized period gain and 0.5 × days_trending_30d). Live REST totals are used for total stars above and can differ by a few stars from the signal capture.
- **Method note:** All ten selected candidates show `days_trending_30d: 5`; their supplied scores range from 10.010 to 9.057. The signal file reports daily Trending data as available (16 candidates). Snapshot deltas (`delta_1d`, `delta_7d`, `delta_30d`) are null because the star-snapshot source failed: the run's GitHub CLI was not authenticated. No prior-window comparison is available, so no Notable Shifts claim is made. DeepWiki was not needed; the five highest-ranked projects had current README content available.
