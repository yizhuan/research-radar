# GitHub Trending Summary - Daily - 2026-09-13

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-09-13 00:40 UTC |
| Scope | Daily |
| Date range | 2026-09-12 through 2026-09-13 |
| Ranking basis | Current-momentum proxy: GitHub Search repositories pushed in the last 24 hours, ranked by total stars; GitHub Trending returned no repositories for this snapshot. |

## Headline

AI-agent infrastructure dominates the current-momentum signal: coding agents, agent skills, workflow automation, and web/data tooling account for most of the standout repositories. GitHub's daily Trending page was empty at collection time, so this is a clearly labeled API-backed proxy rather than a verified star-gain ranking.

## Top Repositories

1. **[openclaw/openclaw - Cross-platform AI assistant that acts on tasks](https://github.com/openclaw/openclaw)**

  **Language:** TypeScript | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 389529 | **Why notable:** It is the largest-starred actively pushed AI-agent project in the corroborating set.

2. **[obra/superpowers - Agentic skills framework and software-development methodology](https://github.com/obra/superpowers)**

  **Language:** Shell | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 285808 | **Why notable:** It shows strong interest in reusable agent skills and structured development workflows.

3. **[affaan-m/ECC - Agent-harness optimization system for coding tools](https://github.com/affaan-m/ECC)**

  **Language:** JavaScript | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 257119 | **Why notable:** Its topics connect agent performance, MCP, Claude Code, and developer productivity.

4. **[NousResearch/hermes-agent - An agent that grows with you](https://github.com/NousResearch/hermes-agent)**

  **Language:** Python | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 244904 | **Why notable:** It is a highly starred, actively pushed general-purpose agent framework with broad model and tool integrations.

5. **[anomalyco/opencode - Open-source coding agent](https://github.com/anomalyco/opencode)**

  **Language:** TypeScript | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 206951 | **Why notable:** Its fresh push activity and large installed-interest signal reinforce coding agents as the leading cluster.

6. **[n8n-io/n8n - Self-hostable workflow automation with native AI capabilities](https://github.com/n8n-io/n8n)**

  **Language:** TypeScript | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 204114 | **Why notable:** It combines automation, integrations, MCP, and AI in a mature developer platform.

7. **[firecrawl/firecrawl - Search, scraping, and web-interaction context API](https://github.com/firecrawl/firecrawl)**

  **Language:** TypeScript | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 179595 | **Why notable:** Agent-ready web retrieval and structured extraction remain a major supporting layer for AI applications.

8. **[langgenius/dify - Collaborative platform for agentic workflows and RAG](https://github.com/langgenius/dify)**

  **Language:** TypeScript | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 155552 | **Why notable:** It represents the productionization of agents, RAG, model access, and low-code workflows.

9. **[langflow-ai/langflow - Visual builder for AI agents and workflows](https://github.com/langflow-ai/langflow)**

  **Language:** Python | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 154678 | **Why notable:** It confirms visual, composable agent development as a parallel path to code-first frameworks.

10. **[anthropics/claude-code - Terminal-based agentic coding tool](https://github.com/anthropics/claude-code)**

  **Language:** Python | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 144864 | **Why notable:** It anchors the coding-agent trend around direct repository understanding and task execution.

## Trending Technologies and Themes

- **Agentic development:** openclaw/openclaw, obra/superpowers, affaan-m/ECC, NousResearch/hermes-agent, anomalyco/opencode, and anthropics/claude-code all focus on agents, agent skills, or coding automation.
- **AI workflow platforms:** n8n-io/n8n, langgenius/dify, and langflow-ai/langflow emphasize visual or low-code orchestration, integrations, RAG, and deployment.
- **Agent context and web data:** firecrawl/firecrawl targets search, scraping, and interaction as an infrastructure layer for model-powered applications.
- **Languages:** TypeScript leads the listed set with 6 repositories; Python follows with 3, while Shell accounts for 1.

## Notable Shifts

The strongest visible shift is from standalone model libraries toward operational agent systems: skills, harnesses, coding interfaces, workflow orchestration, and context acquisition. This snapshot also shows TypeScript-heavy productization alongside Python's continuing role in agent frameworks.

## Takeaway

Today's corroborated momentum is concentrated in the agent stack rather than in a single model release: coding agents sit at the center, with skills, workflows, web context, and deployment platforms around them. Treat the ordering as directional because GitHub's daily Trending page exposed no entries at collection time and the API does not provide daily star gains for these results.

## Sources and Method

- **Primary source:** https://github.com/trending/daily
- **Corroboration:** GitHub REST Search API query `pushed:2026-09-12..2026-09-13 stars:>1000`, sorted by stars descending: https://api.github.com/search/repositories?q=pushed%3A2026-09-12..2026-09-13%20stars%3A%3E1000&sort=stars&order=desc&per_page=30
- **Method note:** GitHub Trending returned “no trending repositories for your choices” at collection time. The ten entries therefore use a transparent current-momentum proxy based on recent push activity and total stars; daily star gains are unavailable from the corroborating API and are not inferred.
