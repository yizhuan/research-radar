# GitHub Trending Summary - Daily - 2026-11-10

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-11-10 17:29 UTC |
| Scope | Daily |
| Date range | 2026-11-10 through 2026-11-10 |
| Ranking basis | Daily GitHub Trending star gains; one separately labeled recent-repository Search supplement |

## Headline

AI-oriented developer tools dominate the strongest gains, led by Meta’s agent-ready Astryx design system (+3,111) and a wave of reusable agent skills. Browser and smart-home agent interfaces also have strong momentum, while Sherlock’s broad social-account search and established simulation software show interest beyond the agent ecosystem.

## Top Repositories

1. **[meta/astryx](https://github.com/meta/astryx) - An open-source, customizable design system built for developers and AI agents.**

  **Language:** TypeScript | **Stars gained in window:** +3,111 | **Total stars:** 22,193 | **Why notable:** The day's largest reported gain; its README describes 150+ accessible components, theming, and a CLI designed to serve both people and agents.

2. **[sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) - Finds public social-media accounts matching a username across 400+ networks.**

  **Language:** Python | **Stars gained in window:** +2,387 | **Total stars:** 108,637 | **Why notable:** A large one-day gain for an established, non-agent utility, suggesting today's interest is not confined to AI tooling.

3. **[anthropics/skills](https://github.com/anthropics/skills) - A public collection of reusable Agent Skills and the associated specification.**

  **Language:** Python | **Stars gained in window:** +1,676 | **Total stars:** 192,027 | **Why notable:** Strong momentum around portable, task-specific instruction bundles, from examples to document and enterprise workflows.

4. **[mattpocock/skills](https://github.com/mattpocock/skills) - A collection of composable engineering skills for coding agents.**

  **Language:** Shell | **Stars gained in window:** +1,223 | **Total stars:** 320,632 | **Why notable:** One of the largest gains; its README emphasizes small, editable, model-agnostic practices rather than a single end-to-end process framework.

5. **[homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) - An MCP server and Home Assistant integration for assistants to configure and automate a smart home.**

  **Language:** Python | **Stars gained in window:** +792 | **Total stars:** 6,463 | **Why notable:** Brings agent tooling into a real-world control domain, exposing a broad set of Home Assistant tools through an in-process integration or server workflow.

6. **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) - A browser automation CLI that lets agents inspect pages and act through compact accessibility snapshots.**

  **Language:** Rust | **Stars gained in window:** +775 | **Total stars:** 49,037 | **Why notable:** Its command-by-command loop, persistent browser session, and ref-based interaction make browser use an explicit agent tool workflow.

7. **[anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) - Deployable starter projects for developers building with the Claude API.**

  **Language:** Python | **Stars gained in window:** +530 | **Total stars:** 20,365 | **Why notable:** Complements the skills trend with practical application scaffolding and deployable API examples.

8. **[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - Production-oriented engineering skills for AI coding agents.**

  **Language:** JavaScript | **Stars gained in window:** +465 | **Total stars:** 114,960 | **Why notable:** Reinforces the skills pattern with an engineering-focused catalog aimed at production work.

9. **[google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) - A general-purpose physics simulator for multi-joint dynamics with contact.**

  **Language:** C++ | **Stars gained in window:** +453 | **Total stars:** 17,250 | **Why notable:** A current gain for mature simulation infrastructure provides a counterpoint to the day's software-agent concentration.

10. **[ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) - A context-compression plugin for long-running, token-intensive agent sessions.**

  **Language:** TypeScript | **Stars gained in window:** +374 | **Total stars:** 6,128 | **Why notable:** Targets the memory and context-management bottleneck implied by longer agent workflows; its efficiency figures are project claims, not independently benchmarked here.

11. **[huamidev/GestaltX](https://github.com/huamidev/GestaltX) - An iPhone and iPad MobileGestalt editor with device presets, backups, and plist tools.**

  **Language:** Swift | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 4,485 | **Why notable:** A separate GitHub Search signal: created on 2026-11-09 and surfaced among the top-starred repositories created and pushed in the last two days; this is not a daily Trending star-gain figure.

## Trending Technologies and Themes

- **Reusable skills for coding agents:** `anthropics/skills`, `mattpocock/skills`, and `addyosmani/agent-skills` all gained strongly, while `anthropics/claude-quickstarts` supplies adjacent application scaffolding. The shared direction is reusable, domain-specific workflow guidance, not just larger models.
- **Agents connected to tools and environments:** `homeassistant-ai/ha-mcp` applies MCP to smart-home control; `vercel-labs/agent-browser` gives agents a persistent browser control loop; `ranxianglei/billion-context` focuses on sustaining longer sessions.
- **Agent-ready interfaces:** `meta/astryx` brings agent use into component-based UI development, with components, themes, documentation, and CLI designed as a coherent system.
- **Non-agent utilities and systems remain visible:** `sherlock-project/sherlock` and `google-deepmind/mujoco` add account discovery and physics simulation to an otherwise agent-heavy set; the recent-search supplement `huamidev/GestaltX` represents native iOS tooling.
- **Languages:** Python leads with 4 of the 11 listed repositories; TypeScript appears in 2. JavaScript, Rust, C++, and Swift each appear once, alongside Shell for `mattpocock/skills`.

## Takeaway

Today's strongest signal is the move from generic coding assistants toward practical agent ecosystems: portable skills, browser and smart-home tools, agent-aware interfaces, and context management. At the same time, gains for Sherlock and MuJoCo show that established utilities and technical infrastructure can still break through. The additional fresh-repository signal is noteworthy, but GitHub Search's current star count should not be mistaken for stars gained today.

## Sources and Method

- **Primary source:** [GitHub Trending - daily](https://github.com/trending?since=daily), retrieved 2026-11-10 at 17:29 UTC. Its displayed daily star gains supplied the ranking for the first ten repositories.
- **Corroboration:** GitHub REST API repository metadata and latest default-branch commits for the listed repositories; GitHub Search API query [`created:2026-11-08..2026-11-10 pushed:2026-11-08..2026-11-10 stars:>100`](https://api.github.com/search/repositories?q=created%3A2026-11-08..2026-11-10%20pushed%3A2026-11-08..2026-11-10%20stars%3A%3E100&sort=stars&order=desc&per_page=100) identified the separately labeled `huamidev/GestaltX` supplement.
- **Method note:** The first ten entries are ordered by the daily star-gain numbers shown on the matching Trending view; total stars and commit SHAs were checked against GitHub REST API data. `GestaltX` is appended as a recent-repository Search signal and has no daily star-gain figure here. README details were checked for the repositories used to explain the main themes. No prior-window comparison was available, so no `Notable Shifts` section is included.
