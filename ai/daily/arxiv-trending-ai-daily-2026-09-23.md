# arXiv Trending AI — 2026-09-23

## Headline
Today's arXiv AI batch is unusually concentrated on making agents dependable in long-horizon, production-like settings: persistent harnesses, context compaction, runtime failure policies, world-model verification, and evaluation that measures real deployment correctness. This is an inferred list of notable papers, not an official arXiv popularity ranking.

## Top papers (ranked)

### 1. [CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents](https://arxiv.org/abs/2609.26779)
- **Abstract:** The paper proposes an autocompaction method that only truncates or drops original content, reporting up to 50% lower cost while maintaining or improving coding-agent performance on Terminal-Bench and KernelBench.
- **Authors:** Trang Nguyen, Eulrang Cho, Bingqing Chen, Tim Dettmers
- **arXiv:** `2609.26779v1` (published 2026-09-22 17:55 UTC; categories: `cs.AI`, `cs.LG`, `cs.SE`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations, as expected for a one-day-old submission. Placement is based on strong cross-list relevance, concrete cost/performance claims, reported results on Terminal-Bench and KernelBench, and an open-source API-proxy implementation; direct popularity data are unavailable.
- **Claimed contribution:** The authors claim that non-rewriting compaction avoids cumulative context drift and improves the cost/performance of test-time scaling, including reported KernelBench speedups after long runs.
- **Caveat:** The evidence is a preprint's reported benchmark evaluation; the abstract does not establish performance across all coding-agent harnesses or workloads.
- **Announcement type:** new submission, 2026-09-23 announcement batch
- **Themes:** Efficient inference & systems; Agents & reasoning; Training & adaptation

### 2. [Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents](https://arxiv.org/abs/2609.26760)
- **Abstract:** Growing Harness learns reusable executable control code from task failures, reducing repeated LLM decisions and reporting lower cost and strong results across BrowseComp-Plus and WebArena-Verified.
- **Authors:** Laizhen Li, Jiarui Li, Juanjuan Zhao, Kejiang Ye, Ye Li, Cheng-zhong Xu, Xitong Gao
- **arXiv:** `2609.26760v1` (published 2026-09-22 17:40 UTC; categories: `cs.AI`, `cs.SE`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations. Placement is based on a cross-list-relevant method for persistent agents, evaluation across 4B–120B deployment models, and unusually large reported reductions in LLM calls and inference cost; popularity signals are sparse.
- **Claimed contribution:** The authors claim that failure-guided, gated program growth moves recurring control from model context into reusable code, preserving success with smaller models.
- **Caveat:** Results are reported on two web-agent benchmarks and three deployment models; transfer beyond those settings remains unestablished.
- **Announcement type:** new submission, 2026-09-23 announcement batch
- **Themes:** Agents & reasoning; Efficient inference & systems; Training & adaptation

### 3. [SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving](https://arxiv.org/abs/2609.26777)
- **Abstract:** SWE-Serve introduces 53 repository-grounded tasks for testing agents on production inference-serving changes with hidden functional, regression, end-to-end, and performance tests.
- **Authors:** Jennifer Williams, Dave Farris, Jeff Farris, Jiantao Jiao
- **arXiv:** `2609.26777v1` (published 2026-09-22 17:54 UTC; categories: `cs.AI`, `cs.SE`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations. Placement is based on a concrete benchmark filling a stated gap between repository-level coding tests and production inference engineering, with 53 tasks, 11 models, 31 configurations, and hidden E2E evaluation; popularity signals are unavailable.
- **Claimed contribution:** The authors claim that E2E tests expose a production-correctness gap: roughly one-third of patches passing other tests fail when E2E serving tests are included.
- **Caveat:** The benchmark is derived from SGLang and runs on CPU or a single H100, so its coverage of other serving stacks and hardware is still unknown.
- **Announcement type:** new submission, 2026-09-23 announcement batch
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Efficient inference & systems

### 4. [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457)
- **Abstract:** AIDE² recursively edits and benchmarks its own research-agent code, with an eight-day run producing successive improvements that the authors report transferring to held-out engineering and weather-forecasting tasks.
- **Authors:** Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu, Zhengyao Jiang
- **arXiv:** `2609.26457v1` (published 2026-09-22 14:12 UTC; categories: `cs.AI`, `cs.LG`, `cs.SE`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations. Placement is based on a high-salience recursive-optimization setting, an eight-day autonomous run, four held-out benchmarks including an out-of-distribution domain, and a cross-list spanning AI, ML, and software engineering; external attention is not yet measurable.
- **Claimed contribution:** The authors claim that recursive self-improvement can improve research efficiency and transfer beyond the tasks used for selection, while incidentally reducing reward hacking.
- **Caveat:** The abstract reports one autonomous run and does not resolve how robust the gains are to seeds, compute budgets, or stronger independent baselines.
- **Announcement type:** new submission, 2026-09-23 announcement batch
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 5. [Dual-Frontier: When Can an Agent Trust Its World Model?](https://arxiv.org/abs/2609.26293)
- **Abstract:** Dual-Frontier formalizes failure attribution between an agent's decision rule and world model, then admits model-guided decisions only when predicted advantage exceeds a certified model-error bound.
- **Authors:** Huatai Zhu, Qiang Chen, Ziqian Kou, Wenhao Li, Fei Wang, Yichao Cao, Xiu Su, Yi Chen
- **arXiv:** `2609.26293v1` (published 2026-09-22 12:05 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations. Placement is based on a clear theoretical obstruction, a verification rule with stated guarantees, and both controlled learned-model experiments and cross-backbone tool-use benchmarks; no independent attention signal is available yet.
- **Claimed contribution:** The authors claim that passive interaction cannot identify the two sources of return loss and propose a verify-then-promote rule with non-decreasing-return guarantees for admitted decisions.
- **Caveat:** The empirical evidence is preliminary and the guarantees depend on calibration, confidence-sequence, and verification assumptions described by the authors.
- **Announcement type:** new submission, 2026-09-23 announcement batch
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 6. [JEV-as-a-Judge: Accept When Confident, Escalate When Unsure](https://arxiv.org/abs/2609.26550)
- **Abstract:** The paper evaluates a low-cost decision-only judge and a confidence-based cascade, reporting near-frontier judge accuracy at a fraction of the comparator's fee on several evaluation tasks.
- **Authors:** Yubo Li, Yidi Miao, Ramayya Krishnan, Rema Padman
- **arXiv:** `2609.26550v1` (published 2026-09-22 15:05 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations. Placement is based on blinded human adjudication, comparison with 16 judges, and a practical cost/accuracy trade-off; the paper is too recent for citation momentum or independent attention.
- **Claimed contribution:** The authors claim that confidence-based escalation retains 99% of a stronger comparator's accuracy at lower cost.
- **Caveat:** The abstract also reports larger gaps on derivation checking and resistance to elaborate wrong answers, limiting the scope of the headline accuracy claim.
- **Announcement type:** new submission, 2026-09-23 announcement batch
- **Themes:** Evaluation & benchmarks; Efficient inference & systems; Safety & alignment

### 7. [FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents](https://arxiv.org/abs/2609.26048)
- **Abstract:** FIRE applies targeted runtime instructions and action denials at states preceding failures, reporting higher repeated success on the full 87-task Terminal-Bench 2.1 suite without changing model weights.
- **Authors:** Nikita Agarwal, Nivedit Jain
- **arXiv:** `2609.26048v1` (published 2026-09-22 11:50 UTC; categories: `cs.AI`, `cs.CL`, `cs.SE`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations. Placement is based on full-suite evaluation, a randomized five-arm experiment, and a direct reliability rather than capability claim; external attention is not yet available.
- **Claimed contribution:** The authors claim runtime policies convert reachable solutions into more repeatable delivery, with the largest gains in repeated-success rather than best-of-two success.
- **Caveat:** The findings are specific to the evaluated Terminal-Bench setup, model tiers, and policy-construction procedure; generalization to other agents is not shown here.
- **Announcement type:** new submission, 2026-09-23 announcement batch
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

## Trending Research Themes

- **Agent reliability is moving into the harness.** CliffCompaction, Growing Harness, and FIRE all change context, control flow, or runtime intervention rather than model weights. Their shared claim is that dependable behavior can come from better state management and execution policy.
- **Evaluation is becoming production-shaped.** SWE-Serve tests repository-scale serving changes with hidden E2E checks, while JEV-as-a-Judge focuses on calibrated escalation and cost. Both challenge single-number local pass rates as sufficient evidence.
- **Verification is paired with action.** Dual-Frontier allocates evidence to uncertain world models; JEV escalates uncertain judgments; FIRE applies corrective policies at known failure states. The recurring pattern is selective expensive checking instead of uniform computation.
- **Persistent adaptation is an active frontier.** Growing Harness accumulates executable repairs, and AIDE² rewrites its own research-agent code. These are different mechanisms, but both treat the agent system—not only the base model—as the object of improvement.

## Open Problems and Research Directions

- **Open problem — transfer of harness improvements:** The selected papers mainly evaluate specific benchmarks and stacks. Test whether compaction, growing harnesses, and runtime policies compose and transfer across model providers, tool APIs, domains, and hardware (CliffCompaction; Growing Harness; FIRE).
- **Open problem — false confidence in selective verification:** Dual-Frontier and JEV both depend on calibrated uncertainty. Measure failure under distribution shift, adversarially persuasive errors, and miscalibrated confidence; compare escalation policies under a fixed cost budget (Dual-Frontier; JEV-as-a-Judge).
- **Open problem — self-improvement stability:** AIDE² reports one autonomous run and incidental reward-hacking reduction. Replicate across seeds and compute budgets, add regression and anti-gaming gates, and audit whether improvements preserve interpretable objectives (Recursive self-improvement).
- **Research direction — benchmark the production gap broadly:** Extend SWE-Serve's hidden E2E methodology to multiple serving frameworks, accelerators, model families, and multi-node deployments, while publishing task provenance and oracle/no-op controls (SWE-Serve).
- **Research direction — cost/reliability frontiers:** Evaluate compaction, selective judges, runtime policies, and verification as a common Pareto frontier of cost, latency, success, and repeatability rather than as isolated percentage gains (CliffCompaction; JEV-as-a-Judge; FIRE; Dual-Frontier).

## Takeaway
The strongest same-day signal is not a new model architecture but a systems shift: agents are being improved through memory, harness code, runtime policies, and selective verification. The evidence is promising but early—every selected paper is a fresh submission, and Semantic Scholar currently reports zero citations for all seven—so the ranking reflects technical salience and corroborated evaluation design, not measured readership.

## Method and sources

Window: daily; arXiv's 2026-09-23 announcement batch, inspected at 2026-09-23 15:10 UTC. The cs.AI recent page reported 240 entries in that day's batch; the scope was the configured AI corpus (`cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`), with selected papers cross-listed where applicable. arXiv has no official trending chart. Ordering is inferred from cross-list breadth, concrete evaluation and reproducibility signals, methodological relevance to current AI-agent problems, and recency; no unsupported social or download metrics were used. Semantic Scholar Graph API was checked for citation and influential-citation counts; all selected papers returned 0 and 0.

Sources: the linked arXiv abstract pages for all seven papers; arXiv recent listing at https://arxiv.org/list/cs.AI/recent; Semantic Scholar Graph API at https://api.semanticscholar.org/graph/v1/paper/batch.
