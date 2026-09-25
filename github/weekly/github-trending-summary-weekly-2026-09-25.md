# GitHub Trending Summary - Weekly - 2026-09-25

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-09-25 14:23 UTC |
| Scope | Weekly |
| Date range | 2026-09-18 through 2026-09-25 |
| Ranking basis | Weekly GitHub Trending star gains |

## Headline

AI-agent infrastructure dominated GitHub's weekly chart: security-audit skills, agent harnesses, parallel-agent runtimes, memory systems, and agent-native tooling all occupied the top tier. The strongest individual surge was cloudflare/security-audit-skill at +11,262 stars, while the broader list shows the trend moving from chat interfaces toward repeatable engineering workflows.

## Top Repositories

1. **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) - A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings.**

  **Language:** JavaScript | **Stars gained in window:** +11,262 | **Total stars:** 21,502 | **Why notable:** It was the week's clear star-gain leader and connects coding agents with verifiable security review.

2. **[affaan-m/ECC](https://github.com/affaan-m/ECC) - An agent-harness performance optimization system covering skills, memory, security, and research-first development.**

  **Language:** JavaScript | **Stars gained in window:** +6,193 | **Total stars:** 267,272 | **Why notable:** Its unusually large existing community and continued weekly acceleration signal sustained interest in agent engineering practices.

3. **[stablyai/orca](https://github.com/stablyai/orca) - An ADE for working with a fleet of parallel agents across desktop, mobile, and remote runtimes.**

  **Language:** TypeScript | **Stars gained in window:** +6,547 | **Total stars:** 77,982 | **Why notable:** It reflects a shift toward coordinating multiple coding agents rather than using a single assistant.

4. **[Tencent/WeKnora](https://github.com/Tencent/WeKnora) - An open-source LLM knowledge platform for RAG, autonomous reasoning, and self-maintaining wikis.**

  **Language:** Go | **Stars gained in window:** +3,749 | **Total stars:** 29,940 | **Why notable:** It combines retrieval, agents, and knowledge maintenance in one deployable platform.

5. **[vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) - Agent memory that learns.**

  **Language:** Python | **Stars gained in window:** +3,363 | **Total stars:** 28,713 | **Why notable:** Persistent, adaptive memory is emerging as a distinct infrastructure layer for agents.

6. **[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - Production-grade engineering skills for AI coding agents.**

  **Language:** JavaScript | **Stars gained in window:** +3,345 | **Total stars:** 98,991 | **Why notable:** It packages practical engineering behaviors as reusable agent capabilities.

7. **[anthropics/claude-code](https://github.com/anthropics/claude-code) - An agentic coding tool that operates in the terminal and handles coding and git workflows through natural language.**

  **Language:** TypeScript | **Stars gained in window:** +2,384 | **Total stars:** 148,042 | **Why notable:** The continued growth of a mature coding agent shows that the category is broadening beyond early adopters.

8. **[anthropics/financial-services](https://github.com/anthropics/financial-services) - An open-source Claude Cowork plugin repository for financial-services workflows.**

  **Language:** Python | **Stars gained in window:** +2,382 | **Total stars:** 37,492 | **Why notable:** Domain-specific plugins indicate agent adoption is moving into professional workflows.

9. **[paperclipai/paperclip](https://github.com/paperclipai/paperclip) - An open-source app for managing agents at work.**

  **Language:** TypeScript | **Stars gained in window:** +2,321 | **Total stars:** 83,740 | **Why notable:** It targets operational coordination and management, not only model interaction.

10. **[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) - Spec-driven development for AI coding assistants.**

  **Language:** TypeScript | **Stars gained in window:** +1,415 | **Total stars:** 70,314 | **Why notable:** It represents a push to make agent-generated changes more structured and reviewable.

11. **[superdesigndev/treg](https://github.com/superdesigndev/treg) - An OpenRouter for agent tools.**

  **Language:** Python | **Stars gained in window:** +1,406 | **Total stars:** 3,314 | **Why notable:** Tool routing and interoperability are becoming their own product layer.

12. **[TencentCloud/Octop](https://github.com/TencentCloud/Octop) - A smarter, self-hosted, multi-user, multi-agent AI assistant.**

  **Language:** Python | **Stars gained in window:** +1,608 | **Total stars:** 4,914 | **Why notable:** It brings multi-agent assistants into self-hosted and collaborative deployments.

13. **[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) - A project to make all software agent-native through command-line interfaces.**

  **Language:** Python | **Stars gained in window:** +964 | **Total stars:** 50,490 | **Why notable:** It frames CLIs as a universal control surface for software-operating agents.

14. **[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) - A CLI tool for configuring and monitoring Claude Code.**

  **Language:** Python | **Stars gained in window:** +965 | **Total stars:** 31,777 | **Why notable:** Configuration and observability are becoming necessary as agent deployments grow more complex.

15. **[cloudflare/quiche](https://github.com/cloudflare/quiche) - A Rust implementation of QUIC and HTTP/3.**

  **Language:** Rust | **Stars gained in window:** +741 | **Total stars:** 12,592 | **Why notable:** It is the main non-agent infrastructure outlier in this snapshot, representing continued interest in high-performance networking.

## Trending Technologies and Themes

- **Agent engineering infrastructure:** ECC, agent-skills, OpenSpec, claude-code-templates, and security-audit-skill treat skills, specs, security, and operations as first-class components around coding agents.
- **Multi-agent orchestration:** Orca, Paperclip, Octop, and treg focus on fleets, workplace management, multi-user assistants, or tool routing rather than one-off prompting.
- **Memory and knowledge systems:** Hindsight and WeKnora emphasize durable memory, RAG, autonomous reasoning, and self-maintaining knowledge bases.
- **Languages:** Among the 15 listed repositories, Python leads with 6 entries, followed by TypeScript with 4, JavaScript with 3, Go with 2, and Rust with 1; the language mix favors fast-moving AI tooling while retaining Go and Rust for infrastructure.

## Notable Shifts

The notable shift is from model-facing applications to agent-operating systems: reusable skills, verifiable security audits, specifications, memory, orchestration, and workplace management all appear among the leading gainers. The chart also shows domain packaging, such as financial-services plugins, alongside general-purpose agent platforms.

## Takeaway

This week's GitHub signal is less about a single model and more about the software layer required to make agents dependable and useful in production. Teams are investing in control planes, memory, tool interfaces, security checks, and domain workflows. The practical opportunity is shifting toward infrastructure that constrains, observes, and composes agents.

## Sources and Method

- **Primary source:** [GitHub Trending repositories this week](https://github.com/trending?since=weekly).
- **Corroboration:** GitHub REST API repository endpoints at `https://api.github.com/repos/{owner}/{repo}` were queried for current total stars, primary language, description, URL, and fork status.
- **Method note:** Weekly star-gain figures come from the matching GitHub Trending view captured on 2026-09-25 UTC; total-star and metadata fields were corroborated through the GitHub REST API. The ranking above is ordered by the displayed weekly star-gain signal.
