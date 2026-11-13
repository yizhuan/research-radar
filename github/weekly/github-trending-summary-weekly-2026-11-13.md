# GitHub Trending Summary - Weekly - 2026-11-13

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-11-13 02:36 UTC |
| Scope | Weekly |
| Date range | 2026-11-06 through 2026-11-13 (GitHub Trending “This week”, rolling seven-day view) |
| Ranking basis | Weekly GitHub Trending star gains, sorted descending |

## Headline

This week’s standout signal is the move from agent prompts to agent work surfaces: reusable skill packs and tools that let agents operate browsers, desktops, security workflows and enterprise data. Cloudflare’s audit skill and OpenMausBot lead on weekly star velocity.

## Top Repositories

1. **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)  - A multi-stage coding-agent security audit skill that tracks coverage and has independent agents validate candidate findings before producing structured reports.**

  **Language:** JavaScript | **Stars gained in window:** +10,700 | **Total stars:** 71,261 | **Why notable:** +10,700 stars on GitHub Trending weekly; represents security in this snapshot.

2. **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)  - A local-first desktop/chat app for a team of AI bots, each with its own personality, model, connected apps and cloud computer.**

  **Language:** TypeScript | **Stars gained in window:** +9,104 | **Total stars:** 21,759 | **Why notable:** +9,104 stars on GitHub Trending weekly; represents agent apps in this snapshot.

3. **[mattpocock/skills](https://github.com/mattpocock/skills)  - A collection of small, composable, model-agnostic engineering skills intended to guide practical software work without imposing a single process.**

  **Language:** Shell | **Stars gained in window:** +8,731 | **Total stars:** 323,063 | **Why notable:** +8,731 stars on GitHub Trending weekly; represents agent skills in this snapshot.

4. **[vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop)  - A cross-platform computer-use CLI that exposes desktop accessibility trees as actionable references, then lets an agent re-observe to verify actions.**

  **Language:** Rust | **Stars gained in window:** +6,414 | **Total stars:** 22,773 | **Why notable:** +6,414 stars on GitHub Trending weekly; represents agent interfaces in this snapshot.

5. **[anthropics/skills](https://github.com/anthropics/skills)  - Anthropic’s example library of self-contained Claude skills—folders of instructions, scripts and resources for repeatable tasks.**

  **Language:** Python | **Stars gained in window:** +6,055 | **Total stars:** 193,730 | **Why notable:** +6,055 stars on GitHub Trending weekly; represents agent skills in this snapshot.

6. **[NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)  - A semantic context layer that uses enterprise metadata, lineage and certified definitions to ground and validate agentic analytics.**

  **Language:** Python | **Stars gained in window:** +5,802 | **Total stars:** 12,274 | **Why notable:** +5,802 stars on GitHub Trending weekly; represents grounded analytics in this snapshot.

7. **[D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)  - A Python web-scraping framework designed to scale from a single request to full crawls across modern sites.**

  **Language:** Python | **Stars gained in window:** +4,743 | **Total stars:** 102,187 | **Why notable:** +4,743 stars on GitHub Trending weekly; represents developer tools in this snapshot.

8. **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)  - A native Rust browser-automation CLI built around compact accessibility snapshots and a shell-driven observe–act–verify loop.**

  **Language:** Rust | **Stars gained in window:** +4,601 | **Total stars:** 50,358 | **Why notable:** +4,601 stars on GitHub Trending weekly; represents agent interfaces in this snapshot.

9. **[zed-industries/zed](https://github.com/zed-industries/zed)  - A high-performance collaborative code editor built in Rust.**

  **Language:** Rust | **Stars gained in window:** +2,339 | **Total stars:** 94,859 | **Why notable:** +2,339 stars on GitHub Trending weekly; represents developer tools in this snapshot.

10. **[google/skills](https://github.com/google/skills)  - Google’s repository of agent skills for its products and technologies.**

  **Language:** Python | **Stars gained in window:** +1,933 | **Total stars:** 24,080 | **Why notable:** +1,933 stars on GitHub Trending weekly; represents agent skills in this snapshot.

11. **[google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)  - A general-purpose physics simulator for multi-joint dynamics and contact.**

  **Language:** C++ | **Stars gained in window:** +1,671 | **Total stars:** 17,777 | **Why notable:** +1,671 stars on GitHub Trending weekly; represents simulation in this snapshot.

## Trending Technologies and Themes

- **Packaged agent skills:** Reusable skill directories are a major signal: anthropics/skills, mattpocock/skills and google/skills publish task-specific guidance/resources rather than another general-purpose model.
- **Agents gain browser and desktop controls:** vercel-labs/agent-browser and vercel-labs/agent-desktop share a shell-driven observe-act-observe model using accessibility references instead of opaque pixel-only actions.
- **Grounding agents in enterprise data:** NVIDIA/auto-ontology emphasizes semantic context, lineage and deterministic query validation to make agentic analytics more explainable.
- **Security workflows for coding agents:** cloudflare/security-audit-skill treats audit output as a verified pipeline with coverage tracking and machine-readable findings.
- **Personalized agent applications:** milind-soni/OpenMausBot packages multiple agents into a local-first chat product, each with an individual model, apps and computer.
- **Established developer tools remain in the mix:** D4Vinci/Scrapling, zed-industries/zed and agent-browser show interest in scraping, coding and browser automation infrastructure, not just agent prompts.
- **A non-agent outlier:** google-deepmind/mujoco is the lone physics-simulation entry among the 11 listed repositories, a useful counterpoint to the agent-heavy cluster.
- **Languages:** Python 4, Rust 3, TypeScript 1, JavaScript 1, Shell 1 and C++ 1 across the 11 listed repositories.

## Takeaway

The strongest pattern is packaged, auditable agent capability: reusable skills, controlled computer-use interfaces and verification-oriented workflows, rather than just another general agent framework. The practical differentiators are observable actions and grounding—accessibility-tree interactions, independent security checks and data provenance. MuJoCo and Zed are useful counterpoints: established simulation and developer tools still draw attention alongside the agent wave.

## Sources and Method

- **Primary source:** [GitHub Trending weekly](https://github.com/trending?since=weekly), captured 2026-11-13 02:36 UTC.
- **Corroboration:** GitHub REST repository/default-branch commit lookups succeeded for the first eight ranked repositories; the REST API began rate-limiting subsequent lookups. For the remaining three repositories, current default-branch commit SHAs were checked from GitHub repository-page `currentOid` metadata. Stars and languages were cross-checked against the Trending page and repository metadata.
- **Method note:** Weekly gains are the values shown on GitHub’s matching “This week” Trending view, sorted descending for this report. The date range labels the rolling seven-day view as observed on 2026-11-13; GitHub does not expose exact hour boundaries here. No prior-week evidence was gathered, so no shift-versus-last-week claim is made. README-based descriptions were checked for the leading eight momentum/theme representatives.
