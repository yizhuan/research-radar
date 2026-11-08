# GitHub Trending Summary - Daily - 2026-11-08

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-11-08 17:45 UTC |
| Scope | Daily |
| Date range | 2026-11-08 through 2026-11-08 |
| Ranking basis | Daily Trending “stars today” gains for ranks 1–9; three repositories active in the last two days appended as supplemental entries |

## Headline

Sherlock topped today’s gain signal (+2,372 stars), but agent workflows formed the broadest technology cluster: skills, browser control, desktop bots, context management, and fresh phone/sandbox projects. Recent additions Pinky and phoneuse point toward agents operating through user-visible devices, with human approval and maturity caveats that matter.

## Top Repositories

1. **[sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) - Hunt down social media accounts by username across 400+ social networks.**

  **Language:** Python | **Stars gained in window:** +2,372 | **Total stars:** 102,746 | **Why notable:** It leads today’s Trending snapshot by a wide margin, while remaining a practical OSINT utility rather than an AI project.

2. **[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) - An open-source Grok Bot alternative with a virtual machine bots can use.**

  **Language:** TypeScript | **Stars gained in window:** +1,437 | **Total stars:** 17,974 | **Why notable:** A strong second-place gain signal for the emerging “agents as chat contacts” desktop pattern.

3. **[meta/astryx](https://github.com/meta/astryx) - An open-source design system that is customizable and agent-ready.**

  **Language:** TypeScript | **Stars gained in window:** +863 | **Total stars:** 15,926 | **Why notable:** The strongest design-system signal in today’s list, joining component libraries with agent-assisted workflows.

4. **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) - Browser automation CLI for AI agents.**

  **Language:** Rust | **Stars gained in window:** +812 | **Total stars:** 47,415 | **Why notable:** It packages browser control as a compact shell-driven workflow and is among the day’s top agent-tooling gainers.

5. **[anthropics/skills](https://github.com/anthropics/skills) - Anthropic’s public repository for Agent Skills.**

  **Language:** Python | **Stars gained in window:** +793 | **Total stars:** 189,367 | **Why notable:** Its high daily gain reflects continuing interest in reusable, task-specific agent capabilities and workflow packaging.

6. **[ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) - A context-compression plugin for long agent sessions and smaller context windows.**

  **Language:** TypeScript | **Stars gained in window:** +460 | **Total stars:** 5,011 | **Why notable:** A distinct infrastructure angle on agent growth: keep long-running coding sessions within bounded model context.

7. **[dsx-ai-factory/nvke](https://github.com/dsx-ai-factory/nvke) - A management plane for GPU Kubernetes on bare metal.**

  **Language:** Go | **Stars gained in window:** +345 | **Total stars:** 762 | **Why notable:** The clearest GPU-infrastructure entry: it manages independent Kubernetes workload clusters on NVIDIA hardware.

8. **[anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) - Deployable application examples for developers building with the Claude API.**

  **Language:** Python | **Stars gained in window:** +28 | **Total stars:** 19,289 | **Why notable:** A low-gain counterpoint to fast-rising agent frameworks: first-party starter applications emphasize concrete deployment patterns.

9. **[google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) - A general-purpose physics simulator for articulated structures and contact dynamics.**

  **Language:** C++ | **Stars gained in window:** +26 | **Total stars:** 16,274 | **Why notable:** A useful non-agent counterpoint: today’s list still includes established simulation infrastructure for robotics and embodied research.

10. **[DIYgod/pinky](https://github.com/DIYgod/pinky) - Let AI agents use your phone, with you in the loop.**

  **Language:** Go | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 674 | **Why notable:** A newly active project (created Nov 6, pushed Nov 8) that extends agent workflows from browsers and desktops to real phones.

11. **[devvmhq/devvm](https://github.com/devvmhq/devvm) - One isolated VM per project, ready for a developer or coding agent.**

  **Language:** Go | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 396 | **Why notable:** A fresh sandboxing workflow relevant to coding agents: project-specific VMs provide an isolated toolchain and workspace.

12. **[lxe/phoneuse](https://github.com/lxe/phoneuse) - Operate an unmodified iPhone from Linux via screen mirroring and Bluetooth input.**

  **Language:** C | **Stars gained in window:** N/A - not available from GitHub | **Total stars:** 362 | **Why notable:** A fresh, technically distinct device-control counterpoint: it combines AirPlay mirroring with Bluetooth HID and offers CLI/MCP access.

## Trending Technologies and Themes

- **Agent workflows and tooling:** Agent activity spans packaged skills and starter apps (anthropics/skills, anthropics/claude-quickstarts), shell-driven browser control (vercel-labs/agent-browser), multi-agent desktop chat (milind-soni/OpenMausBot), context management (ranxianglei/billion-context), and fresh sandbox/device integrations (DIYgod/pinky, devvmhq/devvm).
- **Agents move from APIs into interfaces and devices:** DIYgod/pinky and lxe/phoneuse connect agents to phones, while anthropics/claude-quickstarts includes computer-use examples. The designs differ: Pinky adds a gateway-enforced approval loop, while phoneuse uses screen mirroring plus Bluetooth input and remains experimental.
- **GPU infrastructure:** dsx-ai-factory/nvke represents bare-metal GPU operations through a Kubernetes management plane; its preview status is an important maturity caveat.
- **Agent-aware product UI:** meta/astryx pairs a React design system and reusable components with an explicit agent-ready framing; it is currently in beta.
- **Standalone OSINT utility:** sherlock-project/sherlock leads the day’s gain table, showing the snapshot is not exclusively an AI trend.
- **Robotics and physics simulation:** google-deepmind/mujoco remains a recognizable non-agent infrastructure repository in the day’s list.
- **Project-scoped development environments:** devvmhq/devvm applies VM isolation at the project level, with an explicit use case for coding agents.
- **Long-context management:** ranxianglei/billion-context focuses on reversible conversation compression for long-lived agent sessions.
- **Languages:** Python 3, Go 3, and TypeScript 3 repositories each; Rust, C++, and C appear once each in this 12-repository set.

## Takeaway

The strongest single surge is a mature OSINT utility, while much of the remaining momentum is in making agents usable and governable through tools, interfaces, and persistent context. The newer phone and VM projects are early signals rather than proven platforms; NVKE is also explicitly preview-stage. Language counts across the 12 listed repos are Python 3, Go 3, TypeScript 3, Rust 1, C++ 1, and C 1.

## Sources and Method

- **Primary source:** https://github.com/trending?since=daily
- **Corroboration:** GitHub REST repository metadata and branch commits; GitHub Search API for repositories created 2026-11-06 through 2026-11-08 and pushed since 2026-11-06; `git ls-remote` for current HEADs where REST rate limits intervened.
- **Method note:** Daily star gains are taken from the matching Trending view and ranked descending for its nine captured entries. Three verified, recently created/pushed projects are appended with unavailable daily gains. Current totals can shift after capture; no prior-window comparison was gathered, so no Notable Shifts section is claimed.
