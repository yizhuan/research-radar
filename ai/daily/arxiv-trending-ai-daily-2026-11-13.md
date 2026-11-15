# arXiv AI papers — Friday, 13 November 2026

Eight notable papers from the latest arXiv announcement batch, led by work on agents that must discover, select, verify, or execute their own reasoning. Today’s agenda: an energy-based reasoning result with unusually visible discussion, agentic semi-supervised learning, learning from incomplete verifiers, and newer work on RAG provenance, coding-agent memory, geographic agents, and agent infrastructure. arXiv has no official trending chart, so this ordering is inferred from checkable attention and quality signals plus relevance; the papers are very recent and Semantic Scholar listed zero current citations for these selected records at the snapshot, so popularity cannot be established.

The run is Sunday, 15 November; the latest arXiv announcement page showed Friday, 13 November, so this daily report uses that prior batch. All selected papers are new submissions announced in that batch, with v1 submission timestamps on 12 November UTC.

## Top papers (ranked)

### 1. [Classical Energies Learn to Reason 1,000x Faster than Looped Models](https://arxiv.org/abs/2611.17309)
- **Abstract:** The authors introduce CRAM, a learned Hopfield–Tank energy for constraint puzzles, reporting near-perfect Sudoku-Extreme and Maze-Unique accuracy with at least 1,000× faster training and 282× fewer inference FLOPs than looped baselines on the studied tasks.
- **Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- **arXiv:** `2611.17309v1` (published 2026-11-12T18:56:56Z; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The clearest independent technical discussion found for this batch is Ken Ashe’s 13 November analysis; the authors also provide a public CRAM repository. These are visible discussion and artifact signals, not readership statistics.
- **Claimed contribution:** The paper trains an explicit energy directly from solved puzzles and reports fast, data-efficient reasoning on Sudoku, maze, N-Queens, and graph-coloring tasks (arXiv abstract and paper discussion).
- **Caveat:** The authors caution that these constraint puzzles are unusually well matched to CRAM’s pairwise energy and that high scores do not establish scalability to harder tasks such as ARC-AGI; learning the latent quantities needed for harder reasoning remains open (paper discussion).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Agents & reasoning; Efficient inference & systems

### 2. [AgentSSL: Can MLE Agents Leverage Unlabeled Data?](https://arxiv.org/abs/2611.17323)
- **Abstract:** AgentSSL frames semi-supervised learning as agentic program search and reports that generated pipelines outperform human-engineered baselines in 8 of 12 settings, while program selection can lose as much as 47% when guided by the agent’s feedback metric.
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **arXiv:** `2611.17323v1` (published 2026-11-12T18:59:06Z; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Listed as a NeurIPS 2026 poster and cross-listed in two core AI categories; the paper introduces a substantial 16,977-program selection benchmark. The conference listing is a quality signal, not a popularity measure.
- **Claimed contribution:** The authors formulate semi-supervised learning as agentic search over executable SSL programs and release ProgramSelectBench to evaluate choosing among candidate programs (arXiv abstract and paper text).
- **Caveat:** The authors report that on both ecology tasks the supervised AgentSL variant matches AgentSSL, describe their search as biased toward SSL, and call reliable program selection without labels unresolved (paper discussion).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Agents & reasoning; Data & synthetic data; Evaluation & benchmarks

### 3. [Negative-Only Policy Optimization for One-Sided Verifiable Rewards](https://arxiv.org/abs/2611.17287)
- **Abstract:** The paper formalizes settings where a verifier can reliably reject failures but cannot certify apparent successes, and proposes NOPO, which updates a policy by suppressing trusted negatives rather than rewarding unverified positives.
- **Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
- **arXiv:** `2611.17287v1` (published 2026-11-12T18:52:33Z; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** The arXiv record identifies the paper as a NeurIPS 2026 Spotlight; it is cross-listed in two core AI categories. The spotlight status is a conference signal, not a direct measure of readership.
- **Claimed contribution:** NOPO combines reference-relative suppression of verifier-negative samples with a group-level weight based on non-falsified alternatives; the authors report pass@k gains across code, logic, and math evaluations with unit-test, constraint, and LLM-based verifiers (abstract and paper conclusion).
- **Caveat:** The authors state that negative-only learning identifies what to avoid but not where the removed probability mass should go; their conservative update is intended to limit this problem, while exploiting partial positive evidence remains future work (paper limitations).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Training & adaptation; Safety & alignment; Evaluation & benchmarks

### 4. [Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation](https://arxiv.org/abs/2611.17161)
- **Abstract:** Using counterfactual substitutions in retrieved passages, the authors estimate that some cited claims come from a model’s parametric memory rather than the retrieved context, and find that standard natural-language-inference checks do not reliably identify this provenance mismatch.
- **Authors:** Tanzeel Abbas, Tehseen Zia, David Windridge
- **arXiv:** `2611.17161v1` (published 2026-11-12T17:39:14Z; categories: `cs.AI`)
- **Evidence for ranking:** The paper received multiple recent third-party explainers, including Learn AI Visually and Bharat Hunt, giving it more visible outside discussion than most papers in the batch. These explainers are attention signals only, not evidence that the method is validated.
- **Claimed contribution:** The authors propose counterfactual value substitution to distinguish facts retrieved from context from facts supplied by parametric memory, and compare ten attribution methods (arXiv abstract).
- **Caveat:** The authors say their best detector is not accurate enough to act on: it measures what a model knows rather than what it actually used. The reported model set spans five sizes from one family and one comparator family (abstract).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Retrieval & knowledge; Evaluation & benchmarks; Interpretability

### 5. [LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds](https://arxiv.org/abs/2611.17267)
- **Abstract:** The authors introduce GeoWorld and LiveGeo, a controllable geographic environment and benchmark where agents must acquire relevant evidence, check whether it remains valid as the world changes, and revise decisions; their tests find that strong static performance does not ensure dynamic reliability.
- **Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, et al.
- **arXiv:** `2611.17267v1` (published 2026-11-12T18:45:58Z; categories: `cs.AI`)
- **Evidence for ranking:** Two recent secondary write-ups discuss the benchmark, alongside the arXiv release. This is a modest external-attention signal; the paper has no cross-list breadth among the core AI categories.
- **Claimed contribution:** GeoWorld provides evolving, verifiable geographic state histories, while LiveGeo tests information gathering, evidence revalidation, and replanning in that environment (arXiv abstract).
- **Caveat:** The evidence is specific to the proposed geographic benchmark and tasks; the abstract does not establish reliability in other dynamic environments or real-world deployments.
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Retrieval & knowledge

### 6. [CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](https://arxiv.org/abs/2611.17316)
- **Abstract:** CoReMem values memory by testing its effect on subsequent repository tasks and adapts coding agents to use it; on ChainSWE, the authors report higher resolution rate and fewer steps and cache-aware tokens for a 27B actor than the untrained actor without memory.
- **Authors:** Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, et al.
- **arXiv:** `2611.17316v1` (published 2026-11-12T18:58:22Z; categories: `cs.AI`, `cs.CL`, `cs.SE`)
- **Evidence for ranking:** It spans three core AI categories and reports task-resolution and token-use outcomes on a coding-agent benchmark. No independent attention signal was evident in the sources checked, so it is included as a relevant new result rather than treated as a popularity leader.
- **Claimed contribution:** The authors introduce prospective segment valuation and provenance-gated memory credit, using these to build compact repository memories and adapt an actor to use them (arXiv abstract).
- **Caveat:** The abstract reports one benchmark (ChainSWE) and one 27B actor comparison; it does not establish that the memory strategy transfers to other repositories, agents, or task distributions.
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Agents & reasoning; Retrieval & knowledge; Efficient inference & systems

### 7. [Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](https://arxiv.org/abs/2611.17294)
- **Abstract:** Metal Sandbox combines restricted per-agent workspaces, native macOS command execution, and scheduling across Macs; four Mac mini M4 tests and replayed agent traces report throughput gains and lower tool waiting under the stated workloads.
- **Authors:** Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang, et al.
- **arXiv:** `2611.17294v1` (published 2026-11-12T18:54:42Z; categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.DC`)
- **Evidence for ranking:** The paper is cross-listed across three core AI categories plus distributed computing and links public Metal Sandbox and Harbor repositories. The breadth and released code make it a useful systems result; they are not evidence of high readership.
- **Claimed contribution:** The authors combine per-instance file isolation, command-level scheduling, and migration of eligible waiting commands between Macs; their abstract reports 1.68×–2.05× throughput in concentrated-demand tests and reductions in waiting and batch time in trace replay.
- **Caveat:** The sustained-throughput estimate assumes continuously replenished sessions and unchanged mean command durations; its evaluation is on four Macs and does not establish behavior under different hardware or workload mixes (abstract).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Efficient inference & systems; Agents & reasoning

### 8. [When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems](https://arxiv.org/abs/2611.17239)
- **Abstract:** The paper distinguishes model comparisons on a shared prompt distribution from comparisons on the prompts users generate in response to each model, showing that offline benchmarks and live A/B tests can estimate different effects and sometimes reverse model rankings.
- **Authors:** Hannah Li
- **arXiv:** `2611.17239v1` (published 2026-11-12T18:26:51Z; categories: `stat.ME`, `cs.AI`)
- **Evidence for ranking:** The cross-list bridges statistical methodology and AI, and the paper gives a formal account of when offline and interactive evaluations diverge. No independent attention signal was evident in the sources checked, so this is retained for relevance rather than asserted popularity.
- **Claimed contribution:** The author defines common- and induced-distribution effects, establishes which standard estimators target them, characterizes ranking reversals, and gives a sufficient condition for rankings to agree (arXiv abstract).
- **Caveat:** The variance result is derived in a stylized linear interaction model, while the paper notes that measuring prompt composition and task-level behavior can be difficult in high-dimensional general-purpose LLM settings (abstract and discussion).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Safety & alignment

## Trending Research Themes

- **Agents are increasingly evaluated on choosing and updating, not only generating.** AgentSSL exposes the gap between discovering an ML program and selecting one without reliable labels; CoReMem measures whether stored repository knowledge helps subsequent tasks; LiveGeo tests whether an agent revises decisions as evidence changes. These are separate settings, but all make selection or adaptation central.
- **Verification is becoming a first-class research problem.** NOPO treats verifier positives as untrusted; Cited but Unused asks whether a citation actually supplied a fact; LiveGeo checks whether prior evidence remains valid; and When Both Sides Adapt shows that the prompts being evaluated can change with model behavior. This is a recurring concern in this small daily slice, not evidence that one solution has emerged.
- **Efficiency is pursued at different system layers.** CRAM reduces training and inference cost on structured puzzles, while Metal Sandbox targets GPU-command throughput for coding-agent rollouts and CoReMem aims to reduce unnecessary coding-agent steps and tokens. The papers do not share a single method, and their reported settings are narrow.
- **Category concentration in the recent API sample:** among the 200 newest records returned by the broad query, there were 82 `cs.LG`, 77 `cs.AI`, 52 `cs.CV`, 37 `cs.CL`, and 24 `cs.RO` category assignments; cross-lists make these counts overlap. The sample also contained `stat.ML`, `cs.MA`, and `cs.NE` records. This describes the retrieved recent slice, not total category announcement counts.

## Open Problems and Research Directions

- **Open problem — selecting strong agent-generated programs with weak labels.** AgentSSL reports substantial loss when selection follows a weak feedback metric and finds no ecology-task advantage over its supervised counterpart. **Research direction:** compare unsupervised selection and active label allocation across more program families and real-world datasets under equal label and compute budgets. [AgentSSL](https://arxiv.org/abs/2611.17323)
- **Open problem — safely using partial verification.** NOPO suppresses trusted failures but cannot directly tell where probability mass should move; Cited but Unused likewise finds that available citation-verification signals do not reliably identify source provenance. **Research direction:** test selective or uncertainty-aware positive evidence and provenance calibration across more verifiers, models, and base rates, while measuring false-positive costs. [NOPO](https://arxiv.org/abs/2611.17287), [Cited but Unused](https://arxiv.org/abs/2611.17161)
- **Open problem — transferring reasoning-energy results beyond constraint puzzles.** CRAM’s authors warn that the tested puzzles can be represented by simple pairwise constraints. **Research direction:** construct harder tasks requiring latent-variable discovery and compare energy-based and looped methods under matched data, compute, and stopping criteria. [CRAM](https://arxiv.org/abs/2611.17309)
- **Open problem — measuring user-induced distribution change in interactive LLM evaluation.** When Both Sides Adapt shows that offline and live estimates can target different quantities, but tracking prompt composition and task-level performance is difficult. **Research direction:** run controlled, multi-turn studies that report both common-distribution and induced-distribution effects, prompt/task mix, and uncertainty as interaction length grows. [When Both Sides Adapt](https://arxiv.org/abs/2611.17239)
- **Open problem — agent reliability in changing environments.** LiveGeo finds that static performance does not guarantee reliable decisions as geographic state evolves. **Research direction:** vary update frequency, stale-evidence rates, and replanning costs, then test whether the same failures occur in non-geographic environments. [LiveGeo](https://arxiv.org/abs/2611.17267)
- **Open problem — real-world scaling of memory and execution infrastructure.** CoReMem reports a ChainSWE/27B result, while Metal Sandbox reports four-node tests and trace replays with fixed-duration assumptions. **Research direction:** evaluate across more repositories, actor sizes, hardware types, competing workloads, and live end-to-end task distributions. [CoReMem](https://arxiv.org/abs/2611.17316), [Metal Sandbox](https://arxiv.org/abs/2611.17294)

## Takeaway

This batch’s strongest common thread is not a single model breakthrough but a shift in attention toward the reliability bottlenecks around agents: choosing among candidates, knowing what evidence actually supports an answer, and reacting when conditions change. CRAM, AgentSSL, and NOPO have the clearest conference or outside-discussion signals in this shortlist; the remaining results are useful early work, but both popularity and generalization remain uncertain.

## Method and sources

- **Window:** daily announcement batch, 2026-11-13 00:00:00–23:59:59 UTC. The run date is Sunday, 2026-11-15; the latest arXiv recent page showed Friday, 13 November, so `used_prior_batch = true`. Snapshot time: 2026-11-15T01:13:02Z.
- **Corpus:** the core AI categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`. A broad arXiv API query returned the 200 newest records; all were first submitted on 2026-11-12. Category assignments in that slice overlap because of cross-listing. The shortlist is not an exhaustive count of the full batch; each retained paper’s arXiv abstract page was checked.
- **Ranking method:** arXiv has no official trend ranking. Ordering prioritizes checkable outside discussion and conference signals, then cross-list breadth and released artifacts; recency is only a tie-breaker. Semantic Scholar Graph metadata was checked for current citation and influential-citation totals; all eight selected records showed zero at the snapshot. Those are current totals, not citations gained during this window.
- **Primary sources:** [arXiv recent cs.AI listings](https://arxiv.org/list/cs.AI/recent); [broad arXiv API query](https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:stat.ML+OR+cat:cs.CL+OR+cat:cs.CV+OR+cat:cs.RO+OR+cat:cs.NE+OR+cat:cs.MA&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200); individual arXiv abstract links above. Full text was read for the top three (CRAM and AgentSSL HTML; NOPO PDF) to check reported evidence and limitations.
- **Corroborating sources:** [Ken Ashe’s CRAM discussion](https://kenashe.ai/blog/2026-11-13-cram-makes-sudoku-reasoning-look-too-easy/); [CRAM repository](https://github.com/Prefrontal-AI/CRAM); [NeurIPS AgentSSL poster](https://neurips.cc/virtual/2026/poster/154115); [Learn AI Visually on Cited but Unused](https://learnaivisually.com/ai-explained/cited-but-unused-rag-counterfactual-value-substitution); [Bharat Hunt on Cited but Unused](https://bharathunt.org/ai/cited-but-unused-parametric-provenance-in-retrieval-augmented); [AI Hot on LiveGeo](https://aihot.tech/story/arxiv-ker5a3-livegeo-benchmarking-geographic-agents-in-continuously-evolving-worlds/); [Agentic Design on LiveGeo](https://agentic-design.ai/news-hub/livegeo-benchmarking-geographic-agents-continuously-evolving-worlds-bb7310); [Metal Sandbox repository](https://github.com/WangHaoZhe/metal-sandbox); [Harbor repository](https://github.com/WangHaoZhe/harbor).
