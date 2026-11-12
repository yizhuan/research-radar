# GitHub Trending Summary - Daily - 2026-11-12

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-11-12 01:38 UTC |
| Scope | Daily |
| Date range | 2026-11-11 through 2026-11-12 (UTC; GitHub daily Trending view) |
| Ranking basis | GitHub Trending daily star gains for nine repositories; two repositories created in the preceding 48 hours are appended as unranked additions |

## Headline

Meta's Astryx is the runaway daily signal at 2,776 stars, while agent-oriented developer tooling—engineering skills, browser control, and code auditing—anchors the rest of the list. Two very new projects add a robotics world-model and private meeting-notes angle, but their lifetime star counts are not comparable to Trending's daily gains.

## Top Repositories

1. **[meta/astryx](https://github.com/meta/astryx) - An open design system for React that emphasizes deep customization and workflows shared by developers and coding agents.**

  **Language:** TypeScript | **Stars gained in window:** +2,776 | **Total stars:** 25,054 | **Why notable:** The strongest daily gain by a wide margin; its README describes 150+ accessible components, themes, a CLI, and a beta built on React 19 and StyleX.

2. **[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - Engineering workflows and reusable skills for AI coding agents.**

  **Language:** JavaScript | **Stars gained in window:** +787 | **Total stars:** 115,978 | **Why notable:** A major agent-tooling signal, packaging a spec-to-ship development lifecycle into commands and skills for multiple coding agents.

3. **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) - A browser automation CLI designed for AI agents.**

  **Language:** Rust | **Stars gained in window:** +708 | **Total stars:** 49,891 | **Why notable:** Strong momentum for command-line, accessibility-tree-based browser control; the README documents a persistent browser daemon and ref-based interaction loop.

4. **[homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) - Configure and automate Home Assistant with AI assistants.**

  **Language:** Python | **Stars gained in window:** +645 | **Total stars:** 7,388 | **Why notable:** Shows agent tooling moving into smart-home operations through a Model Context Protocol integration.

5. **[shadcn/improve](https://github.com/shadcn/improve) - Uses a capable model to audit a codebase and produce plans for cheaper models to execute.**

  **Language:** N/A - not available from GitHub | **Stars gained in window:** +361 | **Total stars:** 10,915 | **Why notable:** A distinct agent workflow pattern: separate high-reasoning review and planning from lower-cost implementation.

6. **[ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) - An LLM-powered multi-market stock analysis system with market data, news, dashboards, and notifications.**

  **Language:** Python | **Stars gained in window:** +278 | **Total stars:** 70,294 | **Why notable:** A high-visibility domain-specific AI application combining financial data ingestion, analysis, and scheduled delivery.

7. **[GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) - Source for Modern Web Guidance, a set of skills embedding web-platform expertise and browser-compatibility data into coding agents.**

  **Language:** TypeScript | **Stars gained in window:** +159 | **Total stars:** 1,792 | **Why notable:** A browser-vendor-backed web platform resource is gaining attention alongside the agent-focused projects.

8. **[openai/codex-security](https://github.com/openai/codex-security) - Codex Security CLI and TypeScript SDK for finding, validating, and fixing vulnerabilities.**

  **Language:** TypeScript | **Stars gained in window:** +52 | **Total stars:** 11,767 | **Why notable:** Extends coding-agent workflows into scanning, validating findings, generating patches, and CI or SDK automation.

9. **[TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) - Implementations of algorithms in Java.**

  **Language:** Java | **Stars gained in window:** +51 | **Total stars:** 67,039 | **Why notable:** A conventional educational/reference repository provides a non-agent counterpoint in the daily list.

10. **[HybridRobotics/supermimic](https://github.com/HybridRobotics/supermimic) - Humanoid whole-body motion tracking trained with a differentiable world model.**

  **Language:** Python | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 1,034 | **Why notable:** Newly created within the preceding 48 hours and prominent in the recent-creation Search results; its README links a project page and paper and provides training and playback workflows.

11. **[FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt) - An open-source desktop app for private AI meeting notes that records without adding a meeting bot.**

  **Language:** TypeScript | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 416 | **Why notable:** Newly created within the preceding 48 hours and a fresh example of AI features packaged as a cross-platform desktop product.

## Trending Technologies and Themes

- **Agent-oriented developer tools:** Astryx, agent-skills, agent-browser, improve, and Codex Security cover agent-ready UI components, reusable engineering workflows, browser actions, delegated coding plans, and security remediation.
- **AI moving into operational domains:** ha-mcp applies assistants to home automation, while daily_stock_analysis targets market research and Yogurt packages meeting notes as a desktop app.
- **Physical AI and robotics:** SuperMimic is the day's fresh robotics counterpoint, using a differentiable world model for humanoid motion tracking.
- **Languages:** TypeScript appears in four of the eleven repositories; Python in three; JavaScript, Rust, and Java appear once each; one repository has no primary language listed by GitHub.

## Takeaway

The strongest daily signal is not a single model release but the spread of agent-facing software into the tools people already use: design systems, engineering workflows, browsers, security, home automation, and finance. The two recent additions broaden that picture into robotics and private desktop AI, though their reported lifetime stars should not be read as daily gains.

## Sources and Method

- **Primary source:** [GitHub Trending - daily](https://github.com/trending?since=daily).
- **Corroboration:** GitHub REST repository metadata and default-branch commit endpoints for listed repositories; [GitHub Search API for repositories created since 2026-11-10 with more than 100 stars](https://api.github.com/search/repositories?q=created%3A%3E%3D2026-11-10%20stars%3A%3E100&sort=stars&order=desc&per_page=10) for recent additions.
- **Method note:** The nine ranked entries are ordered by the daily star-gain figures displayed on GitHub Trending at capture time. The two recent-creation additions were verified as created in the preceding 48 hours and are appended without daily gain claims. A community-maintained fork surfaced on Trending was omitted under the noise filter. No prior-window comparison was collected, so no shift claim is made.