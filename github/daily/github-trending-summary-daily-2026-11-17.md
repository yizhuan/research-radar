# GitHub Trending Summary - Daily - 2026-11-17

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-11-17 01:47 UTC |
| Scope | Daily |
| Date range | 2026-11-17 through 2026-11-17 |
| Ranking basis | GitHub Trending daily star gains |

## Headline

Agent infrastructure dominates today's list: the strongest gains cluster around AI office tooling, code review, skill evaluation, browser control, and agent-to-user workflows. The common direction is turning coding agents from isolated chat helpers into tools that can work inside applications with feedback and guardrails.

## Top Repositories

1. **[dream-num/univer](https://github.com/dream-num/univer) -** An extensible Office SDK for editing, calculation, collaboration, and file processing, positioned for people and AI agents.

  **Language:** TypeScript | **Stars gained in window:** +1,828 | **Total stars:** 27,816 | **Why notable:** The day's largest displayed gain; it brings spreadsheet and document-style editing primitives into an extensible SDK explicitly positioned for both people and agents.

2. **[alibaba/open-code-review](https://github.com/alibaba/open-code-review) -** A Go-based AI code-review CLI combining deterministic pipelines with an LLM agent, line-level comments, built-in checks, and OpenAI/Anthropic compatibility.

  **Language:** Go | **Stars gained in window:** +951 | **Total stars:** 52,974 | **Why notable:** Second-highest daily gain; its hybrid design uses deterministic file selection and rule matching around an agent, emphasizing precise reviews over free-form coverage.

3. **[NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) -** A multi-tier framework for validating, deduplicating, and live-evaluating AI agent skills and plugins across quality, security, compatibility, and impact.

  **Language:** Python | **Stars gained in window:** +873 | **Total stars:** 2,741 | **Why notable:** A strong daily gain for a comparatively small project; the three-tier model separates deterministic checks, overlap analysis, and live task-impact evaluation.

4. **[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) -** An MCP server and CLI that let coding agents inspect, debug, automate, and profile a live Chrome browser through Chrome DevTools.

  **Language:** TypeScript | **Stars gained in window:** +841 | **Total stars:** 57,706 | **Why notable:** It turns a live browser into an agent-accessible debugging and performance surface, and ranked among today's top gainers.

5. **[tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) -** Claude Code skills for equity investors and traders, covering market analysis, charting, economic calendars, screeners, and strategy development.

  **Language:** Python | **Stars gained in window:** +837 | **Total stars:** 6,341 | **Why notable:** A high daily gain suggests demand for domain-specific agent workflows, here focused on market research and trading tasks.

6. **[ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) -** An open event-stream protocol connecting agents with user-facing apps, carrying typed events for streaming, tools, shared state, and human input.

  **Language:** TypeScript | **Stars gained in window:** +791 | **Total stars:** 19,047 | **Why notable:** Its stable 1.0 spec and generated TypeScript, Python, and .NET SDKs position it as a standard transport layer between agent frameworks and application interfaces.

7. **[backnotprop/plannotator](https://github.com/backnotprop/plannotator) -** A local browser-based review layer for coding agents, where people annotate plans and artifacts, review diffs, and send feedback back into agent sessions.

  **Language:** TypeScript | **Stars gained in window:** +696 | **Total stars:** 12,595 | **Why notable:** It makes human review asynchronous across multiple agents and artifacts; its inbox lets agents continue while users respond later.

8. **[google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) -** A library of Agent Skills for the Stitch MCP server, following the Agent Skills open standard for compatibility with several coding agents.

  **Language:** TypeScript | **Stars gained in window:** +529 | **Total stars:** 9,749 | **Why notable:** The repository reflects a move from bespoke integrations toward reusable, portable skill packages around an MCP-backed design tool.

9. **[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) -** A local video-editing toolset for coding agents: 42 FFmpeg tools, machine-readable contracts, and an MCP server for cuts, captions, reframing, and export.

  **Language:** Python | **Stars gained in window:** +367 | **Total stars:** 6,799 | **Why notable:** It applies agent tooling to a concrete media workflow and differentiates itself with local processing and no cloud/API-key requirement, per its description.

10. **[google-research/paper-orchestra](https://github.com/google-research/paper-orchestra) -** A multi-agent research-writing pipeline that turns ideas and experiment logs into LaTeX manuscripts using literature synthesis, section writing, refinement, and figure generation.

  **Language:** Python | **Stars gained in window:** +313 | **Total stars:** 1,569 | **Why notable:** A specific research-authoring application stands out amid general agent infrastructure, with a notable gain relative to its current star base.

11. **[DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map) -** An interactive historical atlas of China spanning dynasties, territory snapshots, place-name genealogy, poetry and battlefield landmarks, and a scrubbable historical timeline.

  **Language:** JavaScript | **Stars gained in window:** +288 | **Total stars:** 6,814 | **Why notable:** A non-agent counterpoint in the daily list: a richly scoped interactive historical atlas showing interest in specialized data visualization and cultural projects.

12. **[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) -** An AI-agent research skill that searches Reddit, X, YouTube, Hacker News, Polymarket, and the web before synthesizing grounded summaries.

  **Language:** Python | **Stars gained in window:** +135 | **Total stars:** 68,157 | **Why notable:** A mature research skill remains in the daily list, illustrating that cross-source evidence gathering is becoming a reusable agent capability.

## Trending Technologies and Themes

- **Agent workflow infrastructure and human oversight:** Open Code Review and SkillEvaluator add review and evaluation controls; Chrome DevTools MCP and AG-UI connect agents to browser and application surfaces; Plannotator returns human feedback into agent sessions.
- **AI-enabled product surfaces:** Univer embeds agents in office editing, while PaperOrchestra targets research authoring. The atlas is a counterpoint: a standalone interactive data-rich application also made the list.
- **Developer tooling and automation:** MCP, event protocols, CLI workflows, portable skills, and local tools recur across Chrome DevTools MCP, AG-UI, Stitch Skills, and FFmpeg Skill.
- **Languages:** TypeScript and Python lead the selected 12 repositories at five each; Go and JavaScript appear once each.

## Takeaway

Today's leaderboard favors the connective tissue around AI agents more than another standalone model: interfaces, code review, evaluation, browser access, and human feedback loops. The top gainers also include AI-augmented office and research products, while the atlas and trading-skill projects show that specialist applications can still attract sharp one-day attention. Daily star counts are volatile; the useful signal is the cluster of projects turning agents into supervised, tool-using workflows.

## Sources and Method

- **Primary source:** [GitHub Trending - Today](https://github.com/trending?since=daily).
- **Corroboration:** GitHub REST API repository and default-branch commit endpoints confirmed language, current total stars, active status, and commit SHA for listed repositories. GitHub Search API query `created:2026-11-15..2026-11-17 stars:>50 fork:false` was used to check recent arrivals; results were dominated by duplicated/noisy repos and did not yield a clear addition to the Trending list.
- **Method note:** Star gains are the values displayed by GitHub's daily Trending view at snapshot time; repositories are ordered by those gains. Total stars and default-branch commits were checked via GitHub REST API. No prior-window dataset was used, so no comparative shift is claimed.
