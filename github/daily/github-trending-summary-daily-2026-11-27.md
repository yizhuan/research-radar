# GitHub Trending Summary - Daily - 2026-11-27

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-11-27 03:26 UTC |
| Scope | Daily |
| Date range | 2026-11-27 through 2026-11-27 |
| Ranking basis | Source-provided daily candidate score (daily Trending gain plus a 0.5-weight sustained-trending component); daily star gains verified against the matching Trending view |

## Headline

Agent-centric tooling dominates this snapshot: security workflows, web research access, and repeatable coding-agent methods occupy the strongest momentum signals. The leading individual repo is Claude-BugHunter (+1,597 stars; score 10.877), followed by Firecrawl and a design skill for agent-generated diagrams.

## Top Repositories

1. **[elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) - A Claude Code skill bundle for bug hunting and authorized red-team work, combining vulnerability-class playbooks, attack-chain guidance, triage, and reporting.**

  **Language:** Python | **Stars gained in window:** +1,597 | **Total stars:** 24,780 | **Why notable:** Highest supplied candidate score (10.877; Trending rank 1) and 7 days trending in the last 30; its README describes 85 skills and 681 disclosed-report patterns. Use only for authorized testing.

2. **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) - Web scraping, crawling, and search infrastructure that turns websites into agent-ready data.**

  **Language:** TypeScript | **Stars gained in window:** +1,046 | **Total stars:** 211,039 | **Why notable:** Score 10.454 (Trending rank 6), with 7 days trending in the last 30; its README spans local scraping, a hosted service, and self-hosted infrastructure.

3. **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) - An agent skill for producing branded, self-contained HTML and SVG diagrams across 52 diagram types.**

  **Language:** HTML | **Stars gained in window:** +955 | **Total stars:** 73,949 | **Why notable:** Score 10.363 (Trending rank 9), with 7 days trending in the last 30; it turns natural-language requests into a standalone diagram file rather than relying on a hosted editor.

4. **[XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) - A cross-platform download manager covering web, video, streaming, and peer-to-peer protocols.**

  **Language:** Python | **Stars gained in window:** +889 | **Total stars:** 19,250 | **Why notable:** Score 10.291 (Trending rank 15), with 7 days trending in the last 30; the README highlights HTTP, BitTorrent, FTP, HLS/DASH, YouTube/Bilibili, and a browser extension workflow.

5. **[obra/superpowers](https://github.com/obra/superpowers) - A composable skills framework and software-development method for coding agents.**

  **Language:** Shell | **Stars gained in window:** +854 | **Total stars:** 327,581 | **Why notable:** Score 10.251 (Trending rank 2), with 7 days trending in the last 30; its workflow emphasizes specification, planning, red/green TDD, and subagent-driven implementation.

6. **[zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) - A local-first AI video clipping app that turns links, files, and live-stream replays into social-ready clips.**

  **Language:** Python | **Stars gained in window:** +774 | **Total stars:** 17,058 | **Why notable:** Score 10.153 (Trending rank 16), with 7 days trending in the last 30; the README highlights speaker tracking, captions, covers, MCP integration, and local rendering.

7. **[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) - An agent-led research skill that searches multiple public-interest sources and synthesizes a brief.**

  **Language:** Python | **Stars gained in window:** +759 | **Total stars:** 75,859 | **Why notable:** Score 10.133 (Trending rank 10), with 7 days trending in the last 30; its README describes cross-platform search and engagement-based scoring rather than editor-selected results.

8. **[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) - A project for making existing software accessible to AI agents through generated CLI harnesses and a shared registry.**

  **Language:** Python | **Stars gained in window:** +746 | **Total stars:** 66,457 | **Why notable:** Score 10.116 (Trending rank 3), with 7 days trending in the last 30; the README emphasizes reusable agent-ready interfaces and community-built software integrations.

## Trending Technologies and Themes

- **Agent workflow infrastructure:** Claude-BugHunter, Superpowers, last30days-skill, and CLI-Anything package repeatable methods or interfaces around coding and research agents.
- **Agent access to external information:** Firecrawl focuses on crawling and web data access; last30days-skill combines search across multiple public-interest sources into a synthesized brief.
- **Purpose-built creative and media tools:** diagram-design makes diagrams through agent skills, while AutoClip applies local AI to short-form video; Ghost-Downloader-3 remains a high-momentum, general-purpose download utility.
- **Languages:** Python leads with 5 of 8 entries; TypeScript, HTML, and Shell account for one each.

## Takeaway

The clearest signal is demand for practical agent extensions: projects that connect agents to information, encode a repeatable workflow, or deliver a concrete output are all prominent. At the same time, specialized end-user tools—from diagrams to video editing and downloads—show that GitHub momentum is not limited to model infrastructure. These are attention signals, not a quality or adoption audit.

## Sources and Method

- **Primary source:** [GitHub Trending - daily](https://github.com/trending?since=daily); deterministic input: `/home/yizhuan/.research/github/daily/github-trending-summary-daily-2026-11-27.signals.json`.
- **Corroboration:** GitHub repository pages and exact-name GitHub Search API queries for all eight selected repositories; each page returned successfully, each search returned one exact repository match, and current default-branch commits were recorded in the JSON sidecar.
- **Method note:** Entries are ordered by the supplied candidate score, which combines the daily gain component with a 0.5-weight `days_trending_30d` component; each listed `stars_gained` value is from the matching daily Trending view and was rechecked against its live daily row. Total-star figures are the values captured in the signal file. The star-snapshot source failed because `gh` is not authenticated, so `delta_1d`, `delta_7d`, and `delta_30d` are unavailable (null), not zero. No Notable Shifts section is included because no prior-window comparison was available.
