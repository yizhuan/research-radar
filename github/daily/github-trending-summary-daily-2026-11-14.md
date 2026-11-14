# GitHub Trending Summary - Daily - 2026-11-14

## Snapshot

| Field | Value |
| --- | --- |
| Snapshot time (UTC) | 2026-11-14 01:32 UTC |
| Scope | Daily |
| Date range | 2026-11-14 through 2026-11-14 (GitHub Trending: Today) |
| Ranking basis | GitHub Trending daily star gains, ranked descending; total stars and freshness checked against GitHub REST/Search APIs |

## Headline

Coding-agent infrastructure dominates today’s strongest organic signals: Google’s modern-web guidance and OpenAI’s security workflow are attracting rapid attention, while several projects focus on keeping humans in the review loop. The top listed repository gained 1,925 stars today, far ahead of the rest of the curated set.

## Top Repositories

1. **[GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)  - Source and evaluation toolkit for guidance that gives coding agents current web-platform practices.**

  **Language:** TypeScript | **Stars gained in window:** +1,925 | **Total stars:** 4,885 | **Why notable:** The largest daily gain in this curated snapshot; it packages browser expertise and compatibility guidance for agents rather than relying on generic model recall.

2. **[we-promise/sure](https://github.com/we-promise/sure)  - A community-maintained, self-hostable personal-finance application.**

  **Language:** Ruby | **Stars gained in window:** +925 | **Total stars:** 14,769 | **Why notable:** Second-highest gain; the repo’s README clearly identifies it as a community fork of the archived Maybe Finance project, with browser, desktop, mobile, API, and agent access paths.

3. **[openai/codex-security](https://github.com/openai/codex-security)  - Codex Security CLI and TypeScript SDK for finding, validating, and fixing software vulnerabilities.**

  **Language:** TypeScript | **Stars gained in window:** +751 | **Total stars:** 13,148 | **Why notable:** Strong security-agent momentum, with documented scan, finding-validation, patch, CI, and export workflows.

4. **[tailscale/tailcat](https://github.com/tailscale/tailcat)  - A netcat-style utility over Tailscale’s encrypted data plane, without its control plane.**

  **Language:** Go | **Stars gained in window:** +256 | **Total stars:** 9,469 | **Why notable:** A compact networking counterpoint to the agent-heavy leaders; it uses Tailscale’s WireGuard-based data plane while exchanging connection metadata out of band.

5. **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)  - An AI-assisted code-review tool combining deterministic checks with agent-based review.**

  **Language:** Go | **Stars gained in window:** +215 | **Total stars:** 50,645 | **Why notable:** Its stated differentiator is a hybrid of rules and LLM tool use, with structured line-level findings and support for configurable model endpoints.

6. **[backnotprop/plannotator](https://github.com/backnotprop/plannotator)  - A local browser-based review surface for plans, artifacts, agent messages, diffs, and pull requests.**

  **Language:** TypeScript | **Stars gained in window:** +108 | **Total stars:** 10,469 | **Why notable:** Makes human feedback a first-class step across multiple coding agents, including annotation and review feedback sent back into agent sessions.

7. **[block/buzz](https://github.com/block/buzz)  - A self-hostable collaboration workspace where people and agents share rooms, workflows, and an event log.**

  **Language:** Rust | **Stars gained in window:** +97 | **Total stars:** 37,302 | **Why notable:** Extends the agent-collaboration idea beyond chat: its README describes signed events, shared project rooms, workflow triggers, and agent identities with their own audit trail.

8. **[tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)  - A Claude Skills-based toolkit for structured market review, risk management, trade planning, and journaling.**

  **Language:** Python | **Stars gained in window:** +69 | **Total stars:** 4,185 | **Why notable:** A practical domain-specific agent workflow set; the author explicitly frames it as decision-process support, not an automated signal or promise of returns.

9. **[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)  - Chrome DevTools exposed to coding agents through MCP and a CLI.**

  **Language:** TypeScript | **Stars gained in window:** +67 | **Total stars:** 55,464 | **Why notable:** Brings live-browser inspection, automation, debugging, and performance tracing into agent workflows; it is an established project still receiving daily interest.

## Trending Technologies and Themes

- **Agent guidance and security:** GoogleChrome/modern-web-guidance-src supplies curated, token-efficient web-platform guidance; openai/codex-security applies agent workflows to vulnerability discovery and repair.
- **Human-in-the-loop agent work:** backnotprop/plannotator routes annotations and review feedback back to agents, while block/buzz models agents as workspace participants with auditable identities.
- **Developer tooling exposed to agents:** ChromeDevTools/chrome-devtools-mcp provides browser control and diagnostics, and alibaba/open-code-review combines rule-based checks with LLM-assisted review.
- **Self-hosting and control:** we-promise/sure and block/buzz emphasize self-hostable products; tailscale/tailcat provides a narrower network utility that avoids the Tailscale control plane.
- **Languages:** TypeScript is most common (4 of 9); Go appears in 2, and Ruby, Rust, and Python in 1 each. This small, selected daily list leans toward TypeScript agent tooling but also includes substantial Go and Rust projects.

## Takeaway

Today’s strongest signal is not simply “more agents”; it is the tooling around agents—fresh domain guidance, security checks, browser access, and review interfaces that preserve human oversight. Outside that cluster, self-hostable finance and collaboration apps plus a focused private-network utility show that practical user-facing and infrastructure projects still break through.

## Sources and Method

- **Primary source:** [GitHub Trending repositories, Today](https://github.com/trending?since=daily), captured 2026-11-14 01:32 UTC.
- **Corroboration:** GitHub REST repository, README, and default-branch commit endpoints for each listed repo; GitHub Search API query `stars:>1000 pushed:>2026-11-12` sorted by updated, which independently returned GoogleChrome/modern-web-guidance-src, backnotprop/plannotator, and alibaba/open-code-review among the selected repositories.
- **Method note:** Daily gains are copied from the matching GitHub Trending view; total stars, primary language, and default-branch commit were checked against GitHub REST. Repositories were sorted by displayed daily gain. Sponsor-marked Trending cards and a project making difficult-to-verify gaming-performance claims were omitted from this curated set. Counts can change after capture; no prior-window comparison was used, so no shift claim is made.
