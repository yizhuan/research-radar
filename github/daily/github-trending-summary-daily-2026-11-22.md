# GitHub Trending Summary - Daily - 2026-11-22

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-11-22 17:27 UTC |
| Scope | Daily |
| Date range | 2026-11-22 through 2026-11-22 |
| Ranking basis | GitHub Trending daily star gains, ranked using supplied signal scores as secondary momentum evidence; GitHub REST metadata corroborated |

## Headline

Coding-agent infrastructure and practical agent skills dominate today's list: Claude-BugHunter (+1,721; signal score 8.451), Firecrawl (+910; 7.815), and Superpowers (+785; 7.667) lead the supplied candidates. A second clear thread is turning ordinary software and media workflows into agent-usable tools, from CLI-Anything to Stitch Skills and AutoClip.

## Top Repositories

1. **[elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) — A self-contained Claude Code security skill bundle for bug hunting and authorized red-team workflows.**

  **Language:** Python | **Stars gained in window:** +1,721 | **Total stars:** 17,278 | **Signal score:** 8.451 | **Why notable:** It is the strongest momentum signal in the supplied daily candidates and combines a large catalog of security skills with structured triage and reporting. README currently says 83 skills, while the signal description says 82.

2. **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) — Web scraping, crawling and search infrastructure for AI agents, available locally, self-hosted or as a hosted service.**

  **Language:** TypeScript | **Stars gained in window:** +910 | **Total stars:** 206,778 | **Signal score:** 7.815 | **Why notable:** The #2 signal bridges agent retrieval needs with both local MCP access and a scalable hosted/search offering.

3. **[obra/superpowers](https://github.com/obra/superpowers) — A composable skills framework and development methodology for coding agents.**

  **Language:** Shell | **Stars gained in window:** +785 | **Total stars:** 323,983 | **Signal score:** 7.667 | **Why notable:** README describes a workflow from spec and design through implementation planning, test-driven development and subagent-led execution; the project supports many coding-agent harnesses.

4. **[XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) — A cross-platform download manager for web video and common file-transfer protocols.**

  **Language:** Python | **Stars gained in window:** +690 | **Total stars:** 14,960 | **Signal score:** 7.538 | **Why notable:** It is a strong non-agent counterpoint: one desktop app consolidates HTTP, BitTorrent, FTP, streaming formats and video-platform downloads.

5. **[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) — A project for making desktop and professional software controllable through agent-friendly CLIs.**

  **Language:** Python | **Stars gained in window:** +687 | **Total stars:** 62,610 | **Signal score:** 7.534 | **Why notable:** Its README pairs generated software-specific command interfaces with a hub for installing community-built CLIs, making “software for agents” a tangible workflow rather than a general claim.

6. **[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) — An agent skill that researches topics across social, video, community and web sources, then synthesizes an evidence-grounded brief.**

  **Language:** Python | **Stars gained in window:** +673 | **Total stars:** 72,556 | **Signal score:** 7.513 | **Why notable:** It packages cross-source search and engagement-based synthesis as an installable skill compatible with numerous agent hosts.

7. **[zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) — An open-source desktop tool that turns a video link into short-form edits, captions, covers and publishing copy.**

  **Language:** Python | **Stars gained in window:** +640 | **Total stars:** 13,301 | **Signal score:** 7.463 | **Why notable:** The README confirms a practical creator workflow spanning desktop editing/rendering and short-video destinations, with CLI and MCP support also noted.

8. **[mjmirza/app-store-compliance](https://github.com/mjmirza/app-store-compliance) — A playbook and pre-submission guard for common Apple App Store and Google Play rejection causes.**

  **Language:** Shell | **Stars gained in window:** +617 | **Total stars:** 3,816 | **Signal score:** 7.426 | **Why notable:** It turns platform policy knowledge into checklists and agent-tool workflows; its own README is careful that scans cannot guarantee approval.

9. **[toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) — A local-first, open-source workspace combining documents, whiteboards and planning.**

  **Language:** TypeScript | **Stars gained in window:** +537 | **Total stars:** 76,671 | **Signal score:** 7.288 | **Why notable:** It represents the established productivity-app counterpoint, differentiated by a merged document/canvas model and privacy-focused, local-first positioning.

10. **[google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) — Agent skills and plugins for Google Stitch design workflows.**

  **Language:** TypeScript | **Stars gained in window:** +516 | **Total stars:** 11,818 | **Signal score:** 7.248 | **Why notable:** Its Agent Skills-standard packaging and compatibility across coding agents point to reusable design/build capabilities becoming portable across agent ecosystems.

## Trending Technologies and Themes

- **Coding-agent skills and process:** Claude-BugHunter, Superpowers, last30days-skill and Stitch Skills package repeatable tasks for multiple agent environments; app-store-compliance applies the same pattern to release readiness.
- **Agent access to tools and information:** Firecrawl supplies web retrieval, while CLI-Anything exposes existing software through agent-oriented command interfaces. The common direction is connecting agents to tools and data rather than relying only on model capability.
- **Applied automation beyond code:** AutoClip productizes video repurposing, while Ghost-Downloader-3 consolidates a broad set of download protocols and services. These are workflow applications, not just agent frameworks.
- **Languages:** Python leads the ten selected repositories (5); TypeScript appears in 3 and Shell in 2. This count is for the selected list, not all GitHub activity.

## Takeaway

Today's attention is concentrated on reusable agent capabilities: security workflows, software-development methods, web retrieval, and interfaces that let agents operate external applications. But the list is not exclusively about agents—downloading, creator tooling and a local-first workspace also drew substantial daily gains. Signal deltas from historical snapshots were unavailable, so this is a one-day momentum snapshot, not evidence of a sustained multi-week shift.

## Sources and Method

- **Primary source:** [GitHub Trending — daily](https://github.com/trending?since=daily); pre-collected candidate data at `~/.research/github/daily/github-trending-summary-daily-2026-11-22.signals.json`.
- **Repository verification:** GitHub REST `GET /repos/{owner}/{repo}` and `GET /repos/{owner}/{repo}/commits/{default_branch}` for the ten selected repositories; current default-branch READMEs fetched from each repository's `raw.githubusercontent.com` primary content path.
- **Corroboration:** GitHub REST API responses confirmed repository identity, description/language, current total stars, default branch and commit SHA. The matching Trending view's daily `stars_gained` and supplied signal `score` are used as the ranking evidence; no historical snapshot deltas were available.
- **Method note:** Daily gains shown here are GitHub Trending's figures in the supplied signals file, not total stars. All `delta_1d`, `delta_7d` and `delta_30d` values are null because the star-snapshot collector could not authenticate (`gh auth login`/`GH_TOKEN` required). Therefore no prior-window comparison or `Notable Shifts` claim is made. Signal `days_trending_30d` is 2 for each listed entry; it indicates observed trending days within the tracked window, not necessarily consecutive days.
- **Source availability:** GitHub Trending data and selected repository pages were available; historical snapshot corroboration was unavailable. The configured web extractor could not extract pages, so README verification used the raw files on each GitHub repository's default branch.
