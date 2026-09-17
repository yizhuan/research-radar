# GitHub Trending Summary - Daily - 2026-09-17

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-09-17 15:40 UTC |
| Scope | Daily |
| Date range | 2026-09-17 through 2026-09-17 |
| Ranking basis | Daily GitHub Trending star gains, ordered by stars gained in the window |

## Headline

AI-agent infrastructure dominates today's list: security auditing, code review, browser control, research, knowledge work, and coding assistants occupy most of the high-momentum slots. The strongest non-agent signals are reverse engineering, local inference, desktop utilities, and AI voice tooling.

## Top Repositories

1. **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) - A coding-agent skill for multi-phase security audits with independently verified, machine-readable findings.**

  **Language:** JavaScript | **Stars gained in window:** +3,606 | **Total stars:** 9,787 | **Why notable:** Security auditing for coding agents.

2. **[alibaba/open-code-review](https://github.com/alibaba/open-code-review) - A hybrid deterministic-plus-LLM code review tool with precise line-level comments and multi-language security rules.**

  **Language:** Go | **Stars gained in window:** +3,290 | **Total stars:** 34,058 | **Why notable:** Agentic code review and application security.

3. **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) - CLI and extension that lets AI agents operate a real, logged-in browser without interrupting the user.**

  **Language:** TypeScript | **Stars gained in window:** +1,350 | **Total stars:** 3,850 | **Why notable:** Browser-use infrastructure for agents.

4. **[Tencent/WeKnora](https://github.com/Tencent/WeKnora) - An open LLM knowledge platform combining document RAG, autonomous reasoning, and a self-maintaining wiki.**

  **Language:** Go | **Stars gained in window:** +1,123 | **Total stars:** 26,116 | **Why notable:** RAG and knowledge agents.

5. **[alphaXiv/OpenResearch](https://github.com/alphaXiv/OpenResearch) - Turns coding agents into research agents.**

  **Language:** Rust | **Stars gained in window:** +940 | **Total stars:** 4,958 | **Why notable:** Agentic research workflows.

6. **[NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) - A software reverse-engineering framework.**

  **Language:** Java | **Stars gained in window:** +912 | **Total stars:** 78,296 | **Why notable:** Security and reverse engineering.

7. **[JustVugg/colibri](https://github.com/JustVugg/colibri) - A tiny pure-C engine that runs frontier mixture-of-experts models by streaming experts from disk.**

  **Language:** C | **Stars gained in window:** +872 | **Total stars:** 35,531 | **Why notable:** Local inference on constrained hardware.

8. **[abue-ammar/tinycast](https://github.com/abue-ammar/tinycast) - A native macOS launcher with hotkeys and clipboard history.**

  **Language:** Swift | **Stars gained in window:** +738 | **Total stars:** 5,999 | **Why notable:** Focused desktop productivity tooling.

9. **[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - Production-grade engineering skills for AI coding agents.**

  **Language:** JavaScript | **Stars gained in window:** +680 | **Total stars:** 95,931 | **Why notable:** Reusable agent skills and workflows.

10. **[jamiepine/voicebox](https://github.com/jamiepine/voicebox) - An open-source AI voice studio for cloning, dictation, and creation.**

  **Language:** TypeScript | **Stars gained in window:** +665 | **Total stars:** 54,806 | **Why notable:** Generative audio tooling.

11. **[anthropics/claude-code](https://github.com/anthropics/claude-code) - An agentic coding tool in the terminal for codebase work, routine tasks, explanations, and Git workflows.**

  **Language:** TypeScript | **Stars gained in window:** +538 | **Total stars:** 145,841 | **Why notable:** Terminal coding agents.

12. **[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) - Open-source plugins primarily intended for knowledge workers using Claude Cowork.**

  **Language:** Python | **Stars gained in window:** +287 | **Total stars:** 24,466 | **Why notable:** Agent plugins for knowledge work.

## Trending Technologies and Themes

- **Coding agents and agent infrastructure:** Six of the 12 listed repositories directly target coding agents, agent skills, browser use, research, or knowledge-work plugins: cloudflare/security-audit-skill, Tencent/BrowserSkill, alphaXiv/OpenResearch, addyosmani/agent-skills, anthropics/claude-code, and anthropics/knowledge-work-plugins.
- **Security and correctness:** alibaba/open-code-review, cloudflare/security-audit-skill, and NationalSecurityAgency/ghidra show security moving into both AI-assisted development and established reverse-engineering workflows.
- **Knowledge and local AI:** Tencent/WeKnora brings RAG and autonomous reasoning together, while JustVugg/colibri emphasizes running MoE models on existing hardware.
- **Languages:** TypeScript 3, Go 3, JavaScript 2, and Rust, Java, C, Swift, and Python 1 each among the 12 entries.

## Notable Shifts

The notable shift is from standalone AI applications toward operational layers around agents: auditable skills, code-review pipelines, browser control, research workflows, and plugins. Local inference and security remain visible, but today's momentum is concentrated in making agents useful and governable inside existing developer workflows.

## Takeaway

GitHub's daily signal is less about one new model than about the surrounding agent stack. Teams are competing to make agents safer, more connected to real tools and browsers, and more capable of handling specialized workflows; the continued appearance of Ghidra, local inference, and desktop utilities suggests the broader developer ecosystem is still active beyond AI agents.

## Sources and Method

- **Primary source:** https://github.com/trending?since=daily
- **Corroboration:** GitHub REST API repository metadata for each listed repository (`GET https://api.github.com/repos/{owner}/{repo}`), retrieved at 2026-09-17 15:40 UTC.
- **Method note:** The daily star-gain values and ordering come from GitHub's matching daily Trending view; current total stars, descriptions, languages, and fork status were corroborated with the REST API. Forks, mirrors, courses, and list-only repositories were excluded.
