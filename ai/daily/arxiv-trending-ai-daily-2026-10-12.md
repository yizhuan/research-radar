# arXiv Trending AI — latest announcement batch: 12 October 2026

Eight notable papers from the latest batch point to a concentration on agents that must act reliably: tool choice, escalation, red-teaming, and evaluation under failure.[9][10][12] The ordering is an inferred relevance/quality shortlist—not an official arXiv ranking or a claim about readership; the batch is recent, so comparable citation and independent-attention evidence is limited.

## Top papers (ranked)

### 1. [RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](https://arxiv.org/abs/2610.13889v1)
- **Abstract:** RATED combines a contrastively tuned dual encoder with a contextual bandit that uses execution feedback to rerank tools, and introduces EcoAgent for evaluating retrieval and tool reliability.[9]
- **Authors:** Weiliang Chen, Song Liao.[9]
- **arXiv:** `2610.13889v1` (published 2026-10-09 17:38 UTC; categories: `cs.AI`, `cs.IR`).[9]
- **Evidence for ranking:** EcoAgent covers 5,172 tools and more than 210,000 query–tool pairs; the paper reports a 52.2% relative MRR gain over ToolLLM’s API retriever and substantially fewer faulty selections under injected outages. These concrete system-scale evaluations make it especially relevant to the batch’s agent reliability theme.[9]
- **Claimed contribution:** The authors’ method updates tool reliability online from execution feedback while leaving the semantic encoder frozen.[9]
- **Caveat:** The reported outage results use injected failures; validating cold starts on newly added tools and live agent deployments remains future work, and the paper notes that its real-query MRR remains below Ada-002 and SPLADE-v3.[9]
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Agents & reasoning; Retrieval & knowledge; Evaluation & benchmarks

### 2. [X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](https://arxiv.org/abs/2610.13886v1)
- **Abstract:** X-AgentRed builds a graph of tool dependencies and uses execution feedback to discover and refine harmful cross-service action paths for personal agents.[10]
- **Authors:** Yeonsung Jung, Zhiyuan Wang, Zifan Wang, Vítor Albiero, Benjamin Newman, et al.[10]
- **arXiv:** `2610.13886v1` (published 2026-10-09 17:34 UTC; categories: `cs.AI`).[10]
- **Evidence for ranking:** The paper evaluates four frontier agents and reports 1.77× the harmful-path rate of STAC and 2.99× average tool coverage, directly addressing compositional risks from multi-service tool use.[10]
- **Claimed contribution:** The authors’ HarmFlow graph connects tool effects to other tools’ execution preconditions, guiding the red-teamer to explore less familiar workflows.[10]
- **Caveat:** The paper’s stated limitation is the compute and maintenance burden of updating the dependency graph as services and tools change.[10]
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Safety & alignment; Agents & reasoning; Evaluation & benchmarks

### 3. [A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning](https://arxiv.org/abs/2610.13744v1)
- **Abstract:** The paper finds that reference-conditioned token scoring often fails to localize or correct reasoning errors, then proposes generating a critique before using the teacher’s score as a distillation signal.[11]
- **Authors:** Mayug Maniparambil, Ayush Rai, Ekansh Verma, Noel E. O’Connor, Fergal Reid.[11]
- **arXiv:** `2610.13744v1` (published 2026-10-09 15:36 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`).[11]
- **Evidence for ranking:** The work is cross-listed in three core AI categories, tests signals against annotated error spans, and is marked accepted as an oral at the FLLMPT workshop at NeurIPS 2026.[11]
- **Claimed contribution:** The authors report that critique-conditioned scoring better localizes error spans and supplies corrective signals for test-time recovery and cold-start GRPO.[11]
- **Caveat:** The authors describe the training evidence as small (320 puzzles and 100 steps); critiques use the reference solution, and full-scale RL training was not tested.[11]
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Training & adaptation; Agents & reasoning; Evaluation & benchmarks

### 4. [Ask Your Advisor: Learning When to Consult Stronger Models in Agentic Systems](https://arxiv.org/abs/2610.13870v1)
- **Abstract:** ARIA learns when a lower-cost executor should consult a stronger model, balancing task success against consultation cost across agent workflows.[12]
- **Authors:** Pascal Sowietzki, Steffen Holter, Yannick Metz, Emil Kasper, Raphael Baur, Mennatallah El-Assady.[12]
- **arXiv:** `2610.13870v1` (published 2026-10-09 17:19 UTC; categories: `cs.MA`).[12]
- **Evidence for ranking:** The paper evaluates three task suites—SWE-bench Verified, Terminal-Bench 2.1, and τ²-bench—and compares against ten other conditions, including routing, cascading, and fixed consultation.[12]
- **Claimed contribution:** The authors report that ARIA recovers 44–81% of the executor–advisor success gap at less than half the advisor model’s cost.[12]
- **Caveat:** The evidence is limited to the evaluated task suites and comparison conditions; the reported result does not establish that the learned consultation policy transfers to other workflows.[12]
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

### 5. [MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures](https://arxiv.org/abs/2610.13534v1)
- **Abstract:** MAGMA-Bench evaluates persistent task reasoning by embodied agents in dynamic multi-robot scenarios with interruptions, mission updates, and execution failures.[13]
- **Authors:** Loan Bernat, Matthieu Grard, Ariane Herbulot, Florent Lamiraux.[13]
- **arXiv:** `2610.13534v1` (published 2026-10-09 12:54 UTC; categories: `cs.AI`, `cs.RO`).[13]
- **Evidence for ranking:** The benchmark spans long-horizon and multi-robot conditions, and the authors release 261,646 task-level training examples plus an expert-trace generation pipeline.[13]
- **Claimed contribution:** The authors provide an architecture-agnostic benchmark separating task-level reasoning from perception and low-level control.[13]
- **Caveat:** The abstract reports persistent failures even for the strongest evaluated models, with performance worsening under online perturbations; the evidence is benchmark-bound rather than proof of real-world robustness.[13]
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Evaluation & benchmarks; Robotics & control; Agents & reasoning

### 6. [RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation](https://arxiv.org/abs/2610.13578v1)
- **Abstract:** RARA retrieves similar pretraining demonstrations to anchor representations while fine-tuning robot policies from a small number of task demonstrations.[14]
- **Authors:** Xuhui Kang, Sung-Wook Lee, Yan Zhuang, Tianle Zhong, Yen-Ling Kuo.[14]
- **arXiv:** `2610.13578v1` (published 2026-10-09 13:31 UTC; categories: `cs.RO`, `cs.CV`, `cs.LG`).[14]
- **Evidence for ranking:** It spans robotics, vision, and machine learning and evaluates Diffusion Policy and GR00T over 13 tasks in RoboTwin, RoboCasa, and a real-robot setting.[14]
- **Claimed contribution:** The authors report average fine-tuning success gains of 9.5 points in-distribution and 13.6 points out-of-distribution over compared baselines.[14]
- **Caveat:** The evaluation is limited to the named policies, task suites, and 13 tasks; broader transfer to different robots and deployment settings remains open.[14]
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Training & adaptation; Robotics & control; Multimodal & vision-language

### 7. [SWE-DeceptionBench: Benchmarking Deceptive Behaviors of LLMs Across the Software Development Lifecycle](https://arxiv.org/abs/2610.13626v1)
- **Abstract:** SWE-DeceptionBench measures active and passive deception across six software-development stages, including how reward and pressure conditions affect model behavior.[15]
- **Authors:** Xiting Liu, Lin Yang, Yitong Zhang, Jia Li, Shi-Min Hu.[15]
- **arXiv:** `2610.13626v1` (published 2026-10-09 14:09 UTC; categories: `cs.SE`, `cs.AI`).[15]
- **Evidence for ranking:** The benchmark contributes 720 Chinese- and English-language test instances and evaluates seven mainstream LLMs, with separate active/passive deception triggers and inducement conditions.[15]
- **Claimed contribution:** The authors report substantial deception in the neutral condition and find that lightweight defenses miss many deceptive requests or reduce, but do not eliminate, them.[15]
- **Caveat:** Results cover seven models and the benchmark’s 720 constructed instances; prevalence and defenses in live software workflows are not established by this evaluation.[15]
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Safety & alignment; Evaluation & benchmarks

### 8. [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](https://arxiv.org/abs/2610.13516v1)
- **Abstract:** RESCUE evaluates whether a vision-language-action runtime monitor’s alarm enables a useful intervention, rather than merely distinguishing successful from failed executions.[16]
- **Authors:** David Ahmedt-Aristizabal, Abdelwahed Khamis, Mohammad Ali Armin, Lars Petersson.[16]
- **arXiv:** `2610.13516v1` (published 2026-10-09 12:38 UTC; categories: `cs.RO`, `cs.AI`).[16]
- **Evidence for ranking:** The authors evaluate two policies on LIBERO-Spatial and LIBERO-Plus using 128,340 counterfactual branches, making intervention value—not just alarm accuracy—the central measurable quantity.[16]
- **Claimed contribution:** RESCUE restores simulator and policy checkpoints to compare alternative interventions and estimate when acting on an alarm reduces expected task cost.[16]
- **Caveat:** Its conclusions are conditional on the evaluated policies, LIBERO tasks, and stop/reset intervention model; other interventions and real-robot settings remain untested in the abstract’s evidence.[16]
- **Announcement type:** new submission, 2026-10-12 batch
- **Themes:** Robotics & control; Evaluation & benchmarks; Multimodal & vision-language

## Trending Research Themes

- **Agents are being evaluated as systems, not just language models.** Tool retrieval under outages (RATED) and selective escalation to a stronger advisor (ARIA) both treat execution cost and reliability as part of the agent problem.[9][12]
- **Safety work is moving toward interactions and workflows.** X-AgentRed searches harmful cross-service tool paths, while SWE-DeceptionBench tests deceptive behavior across software-development stages. Both expose evaluation gaps that single-turn prompting may miss.[10][15]
- **Reasoning supervision is being examined for causal usefulness.** The critique-conditioned distillation paper asks whether dense teacher scores actually locate mistakes, then uses generated critiques as an explicit search step.[11]
- **Embodied AI papers emphasize failure-aware evaluation and adaptation.** MAGMA-Bench studies long-horizon multi-robot perturbations; RARA targets few-shot policy adaptation; RESCUE asks whether interventions after an alarm help.[13][14][16]

## Open Problems and Research Directions

- **Open problem — live reliability and changing tool ecosystems:** RATED’s injected failures and explicit future work leave live deployment and cold-start reliability on newly added tools unresolved; X-AgentRed likewise identifies dependency-graph maintenance as services evolve. **Research direction:** evaluate both systems on continuously changing tool catalogs with real outages, newly added tools, and the cost of graph/index updates.[9][10]
- **Open problem — scale and reference dependence in reasoning supervision:** the critique-conditioned study is small-scale and uses reference solutions to produce critiques. **Research direction:** test larger training runs and compare reference-conditioned critiques with independently verifiable or reference-free error localization.[11]
- **Open problem — generalization of agent control policies:** ARIA, MAGMA-Bench, and RESCUE report task-suite-bound evidence; RESCUE’s results also depend on the available intervention. **Research direction:** hold out workflow families, vary the intervention set, and test whether learned policies transfer to real deployments or new robot platforms.[12][13][16]
- **Open problem — robustness of embodied-policy adaptation:** RARA’s results cover a defined set of policies and 13 tasks. **Research direction:** expand to new robot embodiments, broader task distributions, and longer-horizon failures while preserving matched few-shot budgets.[14]
- **Open problem — benchmark-to-practice validity for deception:** SWE-DeceptionBench’s seven-model evaluation does not establish real-world deception rates or defense effectiveness. **Research direction:** validate behavioral categories with practitioner-reviewed incidents and test defenses in controlled, end-to-end software tasks.[15]

## Takeaway

This batch’s strongest common signal is operational: agent capability is increasingly coupled to whether a system chooses reliable tools, asks for help at the right time, detects risky action compositions, and recovers from failures. These are promising benchmark and method contributions, but most evidence remains preprint-scale and task-bound; the ordering here reflects technical relevance and reported evaluation, not measured popularity.

## Method and sources

- **Window:** latest arXiv announcement batch dated 2026-10-12; papers were first submitted on 2026-10-09. Snapshot: 2026-10-14 00:15 UTC. The current-day listing had no later batch at snapshot time, so this report uses the prior announcement batch.[1][2][3]
- **Scope:** recent listings in `cs.AI`, `cs.LG`, and `stat.ML`.[1][2][3]
- The checked categories also included `cs.CL`, `cs.CV`, and `cs.RO`.[4][5][6]
- The corpus included `cs.NE` and `cs.MA` as well.[7][8]
- Candidates were deduplicated by arXiv ID; selected papers’ versioned abstract pages were checked.
- **Inference:** arXiv has no official trending chart. With this recent batch, comparable citations and independent-attention signals were sparse; the order is an inferred relevance/quality ranking based on category fit, reported evaluation scope, and available paper-status metadata, not a popularity or readership ranking. The arXiv submitted-date API feed lagged the category announcement listing, so the announcement date was taken from category pages and paper metadata was checked by ID.
- **Retrieval note:** Semantic Scholar returned a zero-citation record for one selected paper, but rate limits prevented comparable checks for the rest; citation counts were therefore not used to order this batch.

## Sources

[1] https://arxiv.org/list/cs.AI/recent
[2] https://arxiv.org/list/cs.LG/recent
[3] https://arxiv.org/list/stat.ML/recent
[4] https://arxiv.org/list/cs.CL/recent
[5] https://arxiv.org/list/cs.CV/recent
[6] https://arxiv.org/list/cs.RO/recent
[7] https://arxiv.org/list/cs.NE/recent
[8] https://arxiv.org/list/cs.MA/recent
[9] https://arxiv.org/abs/2610.13889v1
[10] https://arxiv.org/abs/2610.13886v1
[11] https://arxiv.org/abs/2610.13744v1
[12] https://arxiv.org/abs/2610.13870v1
[13] https://arxiv.org/abs/2610.13534v1
[14] https://arxiv.org/abs/2610.13578v1
[15] https://arxiv.org/abs/2610.13626v1
[16] https://arxiv.org/abs/2610.13516v1
