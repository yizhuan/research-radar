# arXiv Trending AI — Daily Report — 2026-11-13

## Headline

arXiv AI corpus, Friday 13 November 2026 announcement batch: 8 notable papers selected from a 348-record candidate pool; the clearest shared pattern is agents being made more reliable through better selection, verification, memory, and adaptation rather than simply generating more outputs. The report looks at agentic machine learning, verifier-aware reasoning, and multimodal design, then closes with concrete open tests. arXiv has no official trending chart: this is an inferred, relevance-ranked list, not a popularity ranking; independent attention and citation evidence is limited for papers announced today.

## Top papers (ranked)

### 1. [AgentSSL: Can MLE Agents Leverage Unlabeled Data?](https://arxiv.org/abs/2611.17323)
- **Abstract:** Frames semi-supervised learning as a program-search task for machine-learning-engineering agents, finding gains over human-designed baselines in 8 of 12 settings while identifying program selection as a major bottleneck.
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **arXiv:** `2611.17323v1` (published 2026-11-12T18:59:06Z; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** NeurIPS 2026 lists the work as a poster, providing independent venue corroboration; it spans cs.AI/cs.LG and reports matched-compute comparisons, a 16,977-program selection benchmark, and ecology-task experiments. Ranked first for breadth of empirical evidence, not readership.
- **Claimed contribution:** The authors introduce AgentSSL and ProgramSelectBench, and report up to +21.8% over the strongest human-engineered baselines in 8/12 settings; they also report that feedback-based program selection can reduce performance by as much as 47%.
- **Caveat:** The paper's discussion says SSL is not always preferable and that on the ecology tasks the supervised AgentSL baseline matches AgentSSL; the authors describe the framework as an initial baseline, not a performance ceiling.
- **Announcement type:** new submission, announcement-batch date 2026-11-13
- **Themes:** Agents & reasoning; Training & adaptation; Data & synthetic data

### 2. [Negative-Only Policy Optimization for One-Sided Verifiable Rewards](https://arxiv.org/abs/2611.17287)
- **Abstract:** Defines one-sided verifiability, where a checker can reliably reject some failures but cannot certify accepted outputs, and proposes NOPO, which updates from trusted negatives without directly rewarding non-falsified candidates.
- **Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
- **arXiv:** `2611.17287v1` (published 2026-11-12T18:52:33Z; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** The NeurIPS 2026 Spotlight listing independently corroborates the work's conference recognition; its cs.LG/cs.CL crossover and reported tests across code, logic, and math benchmarks, inference-time scaling, and cross-benchmark transfer support its relevance. The rank reflects this evidence, not popularity.
- **Claimed contribution:** The authors combine reference-relative suppression of verified negatives with a group-level non-falsified-support weight; they report improved pass@k over baselines under unit-test, constraint-check, and LLM self-verifiers.
- **Caveat:** The authors state that negative-only learning specifies what to avoid but not where probability mass should move; their results also weaken when a verifier has low negative recall, as in their OlympiadBench setup.
- **Announcement type:** new submission, announcement-batch date 2026-11-13
- **Themes:** Training & adaptation; Evaluation & benchmarks

### 3. [Learning When Diffusion Language Models Should Regenerate](https://arxiv.org/abs/2611.17320)
- **Abstract:** Introduces DiVR, a verifier that uses a diffusion language model's hidden states and trajectory outcomes to decide when to regenerate a block and which alternative to keep, improving reported accuracy on five reasoning benchmarks at additional decoding cost.
- **Authors:** Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo, et al.
- **arXiv:** `2611.17320v1` (published 2026-11-12T18:58:50Z; categories: `cs.CL`)
- **Evidence for ranking:** An independent technical explainer discusses the method, and the paper reports results on five reasoning benchmarks plus transfer to another generator family. The reported accuracy/cost comparison makes its relevance checkable; no popularity inference is made.
- **Claimed contribution:** The authors train a verifier on the final correctness of a generator's own trajectories; for an SFT LLaDA-8B-Base model they report average accuracy rising from 35.3% to 43.4% at 1.9–3.5× greedy-decoding cost, versus 3.8–7.4× for the cited search baselines.
- **Caveat:** The accuracy increase uses more inference compute than greedy decoding, and the headline result is tied to the paper's tested generators and five reasoning benchmarks.
- **Announcement type:** new submission, announcement-batch date 2026-11-13
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

### 4. [Goal Encoding in LLMs](https://arxiv.org/abs/2611.17297)
- **Abstract:** Studies goal representations in LLMs in a multi-subtask coding setting, localizing a next-subgoal encoding to sparse attention heads and testing its causal role and transfer between environments.
- **Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, et al.
- **arXiv:** `2611.17297v1` (published 2026-11-12T18:55:06Z; categories: `cs.CL`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The work has an OpenReview record and is cross-listed in three core AI categories; its causal interventions and cross-environment transplant tests provide specific evidence beyond a descriptive probing result.
- **Claimed contribution:** The authors identify attention-head outputs that encode upcoming subgoals, report causal effects on next actions, and propose a non-recurrent account in which the model rereads task goals and compares them with progress in context.
- **Caveat:** The experiments use a constructed coding setting; the abstract does not establish that the same goal encoding mechanism generalizes across broader tasks or model families.
- **Announcement type:** new submission, announcement-batch date 2026-11-13
- **Themes:** Interpretability; Agents & reasoning

### 5. [LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds](https://arxiv.org/abs/2611.17267)
- **Abstract:** Presents GeoWorld and LiveGeo, a platform and benchmark for testing whether LLM agents acquire current geographic evidence, check whether it remains valid as the world changes, and revise decisions accordingly.
- **Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, et al.
- **arXiv:** `2611.17267v1` (published 2026-11-12T18:45:58Z; categories: `cs.AI`)
- **Evidence for ranking:** Independent commentary specifically discusses the benchmark's changing-world reliability question; the paper also reports that strong static performance does not ensure dynamic reliability and releases an extensible platform. Ranked as a concrete agent-evaluation contribution, not as a measured attention leader.
- **Claimed contribution:** The authors introduce a controllable geographic environment with evolving external states and verifiable histories, and report that current agents struggle to maintain correct decisions as those states change.
- **Caveat:** Evaluation is conducted through GeoWorld/LiveGeo; the abstract does not report deployment results in live geographic operations.
- **Announcement type:** new submission, announcement-batch date 2026-11-13
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Retrieval & knowledge

### 6. [Unbundling Multimodal Vision Encoding](https://arxiv.org/abs/2611.17334)
- **Abstract:** Uses matched-compute pretraining comparisons to separate the effects of visual pretraining, dedicated vision capacity, and where that capacity enters a multimodal model, finding that jointly trained capacity matters more than a pretrained visual prior in the tested settings.
- **Authors:** Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, et al.
- **arXiv:** `2611.17334v1` (published 2026-11-12T18:59:54Z; categories: `cs.CV`, `cs.LG`)
- **Evidence for ranking:** The cs.CV/cs.LG cross-list and a controlled matched-lifetime-compute comparison address confounds that make encoder recipes hard to compare; the authors also provide a project page. Ranked for methodological relevance, not external popularity.
- **Claimed contribution:** The authors report that dedicated vision capacity is useful, that it need not be pretrained separately, and that early in-fusion vision modules can perform comparably to a pre-fusion encoder while reducing time to first token.
- **Caveat:** The claims are bounded by the paper's pretraining framework and visual-question-answering/language benchmark suite; they do not establish that the same design wins for every multimodal task or compute regime.
- **Announcement type:** new submission, announcement-batch date 2026-11-13
- **Themes:** Multimodal & vision-language; Training & adaptation; Efficient inference & systems

### 7. [CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](https://arxiv.org/abs/2611.17316)
- **Abstract:** Proposes a coding-agent framework that values repository memory by its effect on subsequent tasks and trains the actor to use memory when it saves effort, reporting improved resolution with fewer steps and cache-aware tokens on ChainSWE.
- **Authors:** Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, et al.
- **arXiv:** `2611.17316v1` (published 2026-11-12T18:58:22Z; categories: `cs.AI`, `cs.CL`, `cs.SE`)
- **Evidence for ranking:** It crosses AI, language, and software-engineering categories and reports both task-resolution and resource-use measures for a persistent coding-agent memory design. Its placement follows the broader cross-task agent and verifier work above; the result itself is on a named benchmark.
- **Claimed contribution:** The authors use prospective segment valuation, repository-location/executable-check anchors, and provenance-gated actor adaptation; on ChainSWE they report a 21.0% to 25.7% resolve-rate increase for a 27B actor, with 17% fewer steps and 11% fewer total cache-aware tokens.
- **Caveat:** The reported result is on ChainSWE with a 27B actor; the abstract does not establish that the same gains hold across other repositories, task distributions, or model scales.
- **Announcement type:** new submission, announcement-batch date 2026-11-13
- **Themes:** Agents & reasoning; Retrieval & knowledge; Efficient inference & systems

### 8. [Classical Energies Learn to Reason 1,000x Faster than Looped Models](https://arxiv.org/abs/2611.17309)
- **Abstract:** Presents CRAM, a learned Hopfield-and-Tank-style energy model that solves the paper's Sudoku-Extreme and Maze-Unique tests with low reported training time and inference FLOPs, and contrasts it with looped reasoning models.
- **Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- **arXiv:** `2611.17309v1` (published 2026-11-12T18:56:56Z; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The paper reports directly checkable accuracy, training-time, and inference-FLOP comparisons and is cross-listed in cs.AI/cs.LG. Its narrower puzzle setting and lack of independent discussion place it below work tested across broader task families.
- **Claimed contribution:** The authors report 99.996% Sudoku-Extreme and 100% Maze-Unique test accuracy, and at least 282× fewer inference FLOPs than looped baselines at matched Sudoku accuracy.
- **Caveat:** The authors explicitly caution that Sudoku and Maze may be trivially solvable benchmarks for evaluating the scalability of looped reasoning methods; the results do not establish comparable gains on harder reasoning tasks.
- **Announcement type:** new submission, announcement-batch date 2026-11-13
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

## Trending Research Themes

- **Agent systems are being evaluated on selection and continuity, not just generation.** AgentSSL makes choosing among generated programs the bottleneck; CoReMem tests whether repository memory pays off across successive coding tasks; LiveGeo asks whether an agent rechecks evidence as its environment changes. These papers share a reliability concern, but do not yet demonstrate a general-purpose agent breakthrough.
- **Reasoning work is changing the source and timing of corrective feedback.** NOPO learns from reliable negative checks without treating partial-verifier passes as ground truth, while DiVR uses trajectory outcome information to decide when diffusion generation should revisit a block. Both move away from simply rewarding a single accepted output, through distinct training-time and inference-time mechanisms.
- **Mechanistic analysis of agent behavior is a smaller, isolated signal in this batch.** Goal Encoding reports causal subgoal representations in a coding setting; this complements the behavior-level work above, but one paper is not evidence of a broad interpretability shift.
- **Vision-model design is represented by one controlled study.** Unbundling Multimodal Vision Encoding isolates visual prior, capacity, and fusion placement at matched compute. Its finding supports testing design choices independently; this batch alone does not establish a field-wide move away from pretrained encoders.
- **Category mix:** the daily candidate pool has substantial representation from computer vision and machine learning (76 and 67 records respectively with those primary categories); the selected list is deliberately cross-area and is not proportional to the pool.

## Open Problems and Research Directions

- **Open problem (authors state; AgentSSL):** Program selection can lose as much as 47% relative to the agent's own feedback metric, and the paper says stronger agents may widen the gap between the best generated program and the one selected. **Research direction (synthesis):** Compare active and unsupervised selection methods under fixed labeling budgets on ProgramSelectBench, then test the same selection policy on the ecology tasks and report calibration across program families.
- **Open problem (authors state; NOPO):** A negative-only update says which outputs to suppress, not where probability should move; low negative recall leaves little reliable supervision. **Research direction (synthesis):** Measure a recall-stratified accuracy/capability frontier and test whether uncertainty or pairwise evidence can add useful positive information without turning partial verifier passes into labels.
- **Open problem (paper evidence; DiVR):** Its reported accuracy gains require 1.9–3.5× greedy decoding cost on the stated SFT model. **Research direction (synthesis):** Compare calibrated quality-cost Pareto curves across model sizes and reasoning domains, including tasks where regeneration changes multiple dependent blocks.
- **Open problem (authors report; LiveGeo):** Agents struggle to acquire relevant evidence and preserve correctness when geographic states evolve. **Research direction (synthesis):** Ablate evidence freshness, source reliability, and update frequency separately, and evaluate whether agents know when a previously valid plan must be withdrawn.
- **Open problem (methodological boundary; CoReMem):** The reported gain is on ChainSWE with one 27B actor, leaving cross-repository transfer unestablished. **Research direction (synthesis):** Evaluate memory valuation on repositories with different structure and task recurrence, separating transfer of repository anchors from repeated-task memorization.
- **Open problem (authors state; CRAM):** Sudoku and Maze may be too easy to establish reasoning scalability. **Research direction (synthesis):** Test learned energy models on harder compositional or out-of-distribution constraint problems and compare compute at matched accuracy against looped models.

## Takeaway

Today's batch contains a credible cluster around agent reliability: selecting useful programs, learning from incomplete verification, deciding when to regenerate, and carrying forward useful repository knowledge. The strongest results are promising but remain benchmark-bounded; attention and citation data are too sparse to claim that these are arXiv's objectively hottest papers.

## Method and sources

- **Window:** Daily announcement batch, 2026-11-13 through 2026-11-13 UTC. arXiv's cs.AI and cs.LG recent pages identify the latest batch as Fri, 13 Nov 2026. The selected papers' abstract pages show first submissions on 12 Nov 2026; the announcement date is therefore one calendar day later than their submission timestamp.
- **Snapshot time:** 2026-11-13T17:08:03Z.
- **Scope/query:** Exact arXiv API search: `(cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA) AND submittedDate:[202611120000 TO 202611122359]`. It returned 348 candidate records submitted 2026-11-12 for the 2026-11-13 announcement batch. The configured categories were all represented. The pool included primary-category counts of cs.AI 61, cs.LG 67, stat.ML 5, cs.CL 38, cs.CV 76, cs.RO 40, cs.NE 2, and cs.MA 3; cross-listed papers overlap these counts.
- **Inference method:** arXiv supplies no official trend ranking. Because the batch is very recent and citation/attention evidence is sparse, this is labeled a notable-paper list and ranked by corroborated external discussion or conference listing where available, cross-area relevance, and the specificity and breadth of reported evaluation. It is not a popularity, readership, or download ranking. Semantic Scholar citation and influential-citation evidence was checked but unavailable for this snapshot; no citation totals were used.
- **arXiv sources (abstract pages verified):** [AgentSSL](https://arxiv.org/abs/2611.17323); [NOPO](https://arxiv.org/abs/2611.17287); [DiVR](https://arxiv.org/abs/2611.17320); [Goal Encoding](https://arxiv.org/abs/2611.17297); [LiveGeo](https://arxiv.org/abs/2611.17267); [Unbundling Multimodal Vision Encoding](https://arxiv.org/abs/2611.17334); [CoReMem](https://arxiv.org/abs/2611.17316); [Classical Energies/CRAM](https://arxiv.org/abs/2611.17309). Category recency pages: [cs.AI](https://arxiv.org/list/cs.AI/recent) and [cs.LG](https://arxiv.org/list/cs.LG/recent).
- **Corroborating sources:** [AgentSSL NeurIPS 2026 poster](https://neurips.cc/virtual/2026/poster/154115) and [OpenReview record](https://openreview.net/forum?id=yWxcbCZwgn); [NOPO NeurIPS 2026 Spotlight listing](https://neurips.cc/virtual/2026/poster/152610); [DiVR technical explainer](https://zerohour.day/item/f96332f5aa0d453560072145e2d8dca371330d7e); [Goal Encoding OpenReview record](https://openreview.net/forum?id=JE0EuQdwuw); [LiveGeo independent commentary](https://franklineh.com/learn/research/editorial-research-9bea9e38dd95e60ccf0d38a95fc04b5c).
