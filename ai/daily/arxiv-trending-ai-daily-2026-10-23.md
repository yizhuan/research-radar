# arXiv Trending AI — Daily report, Friday 23 October 2026 batch

At the 2026-10-26 17:05 UTC snapshot, the latest available announcement batch is Friday 23 October (papers submitted that day); today's Monday batch had not yet appeared. This report selects 10 notable papers across the configured AI categories. The dominant pattern is agent reliability and evaluation: tool faults, changing workspaces, and harness/model interactions are tested alongside new scientific-agent training and benchmark infrastructure. Spoken agenda: first the reliability tests, then scientific-agent scaling, and finally memory, adaptation, interpretability, and robotics. arXiv has no official trending chart; this ordering is inferred, not a popularity ranking, and citation evidence is limited for papers only days old.

## Top papers (ranked)

### 1. [Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance](https://arxiv.org/abs/2610.32555)
- **Abstract:** The authors introduce MCP-Injector, a calibrated fault-injection middleware, and report that realistic MCP faults sharply reduce task performance while the tested larger gpt-oss model does not show better fault tolerance.
- **Authors:** Antonio Ken Iannillo, Joshua Segun Owotogbe, Roberto Natella, Francesco Avallone, Kristina Kudryavtseva, Indika Kumara
- **arXiv:** `2610.32555v1` (published 2026-10-23T12:35:51Z; categories: `cs.SE`, `cs.AI`)
- **Evidence for ranking:** The arXiv record says accepted as a NeurIPS 2026 poster, and the conference has an official poster listing. The paper also reports a 1,350-cell evaluation and a fault model mined from 57,240 issue/PR threads; these are relevance and evaluation signals, not readership measures.
- **Claimed contribution:** The authors present protocol-aware MCP fault injection calibrated to public ecosystem incidents and use it to test three agent stacks and two model sizes.
- **Caveat:** The scale comparison covers two gpt-oss sizes, 25 tasks, and three seeds under a permanent-heavy stress profile; the authors identify multi-server orchestration and longer-horizon tasks as open extensions.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Efficient inference & systems

### 2. [SWE-Shift: Evaluating Coding Agents in Evolving Workspaces](https://arxiv.org/abs/2610.32196)
- **Abstract:** SWE-Shift compares matched clean and shifted continuations to test whether coding agents can preserve valid work and recover when task-relevant workspace changes occur mid-execution.
- **Authors:** Victor Shea-Jay Huang, Rongqing Li, Zhangyue Yin, Kelong Mao, Yaqi Zhao et al.
- **arXiv:** `2610.32196v1` (published 2026-10-23T05:47:59Z; categories: `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** It spans three core AI categories, evaluates 17 coding-agent systems on 120 scenarios and 12 change families, and has a public project repository. This is a broad, concrete reliability benchmark rather than an attention count.
- **Claimed contribution:** The authors introduce matched Clean/Shifted continuations and report lower shifted success for all 17 tested systems, with failures in state recovery, work preservation, and evidence freshness.
- **Caveat:** The authors note 120 designed scenarios (some share task roots), one update per run, uncontrolled model randomness, a fixed post-fork token budget, and diagnostic controls covering five systems.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Safety & alignment

### 3. [POSEIDON: Scaling Training Environments for Scientific Agents from Code Repositories](https://arxiv.org/abs/2610.32448)
- **Abstract:** POSEIDON mines scientific repositories into executable, verifiable agent-training tasks; the authors report a 97,659-environment collection from 7,110 repositories and gains for fine-tuned Qwen3.5 models on six scientific-agent benchmarks.
- **Authors:** Qifan Zhang, Yuhan Li, Nuo Chen, Bowen Liu, Xiao Hu et al.
- **arXiv:** `2610.32448v1` (published 2026-10-23T10:14:22Z; categories: `cs.AI`)
- **Evidence for ranking:** The paper reports a large reusable training corpus spanning 10 scientific disciplines, a matched-budget comparison with a prior pipeline, and evaluation across six benchmarks. These measurable artifacts and results support its relevance; they do not establish popularity.
- **Claimed contribution:** The authors derive Reproduction, Subflow, Completion, and Correction tasks from scientific workflows and add recursive verification/refinement; on a matched repository budget they report 9.3 times as many environments as the comparison pipeline.
- **Caveat:** The reported fine-tuning experiments use three Qwen3.5 variants and six selected benchmarks; the authors' independent manual quality audit sampled 600 tasks rather than the full corpus.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Agents & reasoning; Data & synthetic data; Evaluation & benchmarks

### 4. [SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks](https://arxiv.org/abs/2610.32441)
- **Abstract:** SCI-AGENT-EXAM evaluates scientific agents on 120 expert-curated tasks across 11 fields and seven research task types, scoring executable and textual artifacts with a hybrid protocol.
- **Authors:** Tianyun Zhong, Wei Wang, Jialin Li, Jianhong Tu, Liyao Li et al.
- **arXiv:** `2610.32441v1` (published 2026-10-23T10:06:55Z; categories: `cs.CL`)
- **Evidence for ranking:** It provides a multi-field, workflow-oriented benchmark and reports runs from 10 frontier agents; an OpenReview record independently lists the benchmark. The benchmark design and evaluation coverage, not citation counts, place it here.
- **Claimed contribution:** The authors combine deterministic checks for executable outputs with a calibrated, expert-validated LLM judge for text, and analyze solution progress and stability as well as final outcomes.
- **Caveat:** Findings are bounded to 120 curated tasks and the 10 evaluated agents; textual-output scoring partly depends on an LLM judge, even though the authors report calibration and expert validation.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Evaluation & benchmarks; Agents & reasoning

### 5. [When Agents Fail: Model or Harness--Who's to Blame?](https://arxiv.org/abs/2610.32483)
- **Abstract:** The authors propose measures for evaluating model–harness interactions and report that harness rankings vary across models and benchmarks, with valid completion and task correctness sometimes favoring different pairings.
- **Authors:** Shao Zhang, Hangfan Zhang, Yuanyuan Shi, Hao Li, Min-Le Su et al.
- **arXiv:** `2610.32483v1` (published 2026-10-23T10:57:54Z; categories: `cs.AI`, `cs.CL`, `cs.SE`)
- **Evidence for ranking:** The paper spans three core categories and reports 52,168 trajectories across 111 settings, four general-purpose harnesses, four core models, and six benchmarks. Independent technical discussion also surfaced in search; no citation count is used.
- **Claimed contribution:** The authors define five interaction-aware measures, including Valid Completion Rate and Model-Harness Fit, to separate task outcome from execution reliability and token load.
- **Caveat:** The comparisons cover four general-purpose harnesses, four core models, and six benchmarks; the paper itself finds rankings vary with the selected model and benchmark, so no single harness ordering generalizes automatically.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Efficient inference & systems

### 6. [RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms](https://arxiv.org/abs/2610.32971)
- **Abstract:** RobustRLlib unifies 17 robust online, offline, and safe RL algorithms and evaluates them over 273 perturbation configurations, mapping where tested methods retain robustness and where gaps remain.
- **Authors:** Xi Chen, Fengqi Hu, Zeyu Shen, Jiaying Xu, Shangding Gu et al.
- **arXiv:** `2610.32971v1` (published 2026-10-23T17:57:22Z; categories: `cs.LG`, `cs.AI`, `cs.RO`)
- **Evidence for ranking:** The paper cross-lists machine learning, AI, and robotics; its code, project site, and tutorial are publicly discoverable, and its 273-configuration evaluation covers humanoid and VLA tasks as well as other shifts.
- **Claimed contribution:** The authors provide a shared interface for 17 algorithms plus an extensible shift-oriented evaluation platform and capability map.
- **Caveat:** The capability map is limited to the included algorithms, tasks, and 273 declared perturbation configurations; it cannot establish robustness to untested deployment shifts.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Evaluation & benchmarks; Robotics & control; Safety & alignment

### 7. [On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models](https://arxiv.org/abs/2610.32770)
- **Abstract:** The authors use topic prompts to generate synthetic questions and privileged reasoning traces for on-policy self-training, reporting gains on language benchmarks and visual question answering without human-curated task prompts or answers.
- **Authors:** Leon Sick, Lukas Hoyer, Yannick Strümpler, Christian Reisswig, Timo Ropinski, Federico Tombari
- **arXiv:** `2610.32770v1` (published 2026-10-23T15:12:03Z; categories: `cs.CL`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The method connects three core AI categories and tests self-generated supervision across text and multimodal tasks; an OpenReview record and a Hugging Face Papers listing provide checkable external discovery signals.
- **Claimed contribution:** The authors reformulate on-policy self-distillation as a curriculum-generation and privileged-demonstration process driven by coarse topic descriptions alone.
- **Caveat:** The abstract reports standard language benchmarks and VQA, but does not establish generality beyond the evaluated tasks or that self-generated supervision is reliable in open-ended deployment.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Training & adaptation; Data & synthetic data; Multimodal & vision-language

### 8. [Interpretable sparse fine-tuning with TopKLoRA enables faithful circuit discovery](https://arxiv.org/abs/2610.32866)
- **Abstract:** TopKLoRA activates only the largest adapter latents per token; in sleeper-agent backdoor experiments, the authors report identifying and ablating circuits necessary and sufficient for the backdoor while preserving instruction-following performance.
- **Authors:** Marek Masiak, Andrzej Szablewski, Nicola Cancedda, Constantin Venhoff
- **arXiv:** `2610.32866v1` (published 2026-10-23T16:37:29Z; categories: `cs.LG`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** It cross-lists three core categories and offers a concrete safety/interpretability result with model-organism experiments on three model sizes; the contribution is a distinct methodological signal, not evidence of broad uptake.
- **Claimed contribution:** The authors extend TopKLoRA as an interpretable-by-design adapter and use sparse latents to search for circuits, then test the identified circuits by ablation and gradient routing.
- **Caveat:** The reported evidence is a sleeper-agent backdoor case study using Gemma 2 2B and Qwen2.5 1.5B/7B; broader backdoor families and larger model scales are not established by this experiment.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Interpretability; Safety & alignment; Training & adaptation

### 9. [Do VLAs Know They Will Fail? Interpretable Success and Failure Patterns in Physical AI Systems](https://arxiv.org/abs/2610.32208)
- **Abstract:** The authors use sparse-autoencoder features from OpenVLA activations to predict task failure before an unrecoverable state and interpret recurring success- and failure-associated behavior patterns.
- **Authors:** Christian A. Rogers, Qian Lin, Daniel S. Brown
- **arXiv:** `2610.32208v1` (published 2026-10-23T06:02:12Z; categories: `cs.RO`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The work cross-lists robotics, AI, and machine learning and has been accepted to the non-archival Science of Physical AI Safety Workshop at CoRL 2026. Its stated held-out-interval validation is a quality signal.
- **Claimed contribution:** The authors identify outcome-predictive SAE features and use a VLM pipeline to produce behavior descriptions, then check their correspondence with activations on held-out intervals.
- **Caveat:** The study concerns OpenVLA activations and the authors describe the workshop version as non-archival; transfer to other VLA models, robots, and environments remains unshown here.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Interpretability; Robotics & control; Safety & alignment

### 10. [ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents](https://arxiv.org/abs/2610.32752)
- **Abstract:** ActionRAG combines cautious entity indexing with query-time graph diffusion to refine evidence in long-term agent memory, reporting 55.1 average accuracy on MemoryAgentBench and a 5.4-point gain over its strongest retrieval-based baseline.
- **Authors:** Navyansh Mahla, Sashank Vandrangi
- **arXiv:** `2610.32752v1` (published 2026-10-23T14:59:37Z; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The paper connects AI and language technology and reports a quantified comparison on eight MemoryAgentBench scoring columns plus query-cost measurements. Its ranking reflects a concrete agent-memory contribution.
- **Claimed contribution:** The authors use tiered entity resolution, dual-channel retrieval, and query-conditioned graph diffusion to revise triple scores while protecting seed evidence.
- **Caveat:** Evaluation is reported on MemoryAgentBench; latency is measured on consumer Apple Silicon, and the reported p99 figure sums separately measured retrieval-side components rather than an end-to-end cross-hardware benchmark.
- **Announcement type:** new submission, Friday 23 October 2026 batch
- **Themes:** Retrieval & knowledge; Agents & reasoning; Efficient inference & systems

## Trending Research Themes

- **Agent reliability is being measured beyond final task success.** MCP fault injection, SWE-Shift, and model–harness evaluation examine operational faults, mid-run changes, valid completion, and recovery rather than treating model capability as the whole system ([MCP-Injector](https://arxiv.org/abs/2610.32555), [SWE-Shift](https://arxiv.org/abs/2610.32196), [When Agents Fail](https://arxiv.org/abs/2610.32483)). This is a visible methodological shift in the selected batch, not proof that agent failures are newly important.
- **Scientific-agent infrastructure is expanding on both sides of the loop.** POSEIDON generates training environments from repositories, while SCI-AGENT-EXAM evaluates complete research workflows with executable and textual outputs ([POSEIDON](https://arxiv.org/abs/2610.32448), [SCI-AGENT-EXAM](https://arxiv.org/abs/2610.32441)). The intersection is reusable workflow-derived supervision plus outcome evaluation.
- **Robustness and safety are being tied to interpretable signals.** RobustRLlib maps robustness over declared perturbations; TopKLoRA investigates sparse circuits for backdoor ablation; the VLA study seeks early, interpretable failure markers ([RobustRLlib](https://arxiv.org/abs/2610.32971), [TopKLoRA](https://arxiv.org/abs/2610.32866), [Do VLAs Know They Will Fail?](https://arxiv.org/abs/2610.32208)). Their settings differ, so this is a shared emphasis, not a common validated safety mechanism.
- **Adaptation spans synthetic supervision and persistent memory.** On-Policy Self-Training generates its own training curriculum, while ActionRAG refines evidence retrieved from accumulated interaction histories ([On-Policy Self-Training](https://arxiv.org/abs/2610.32770), [ActionRAG](https://arxiv.org/abs/2610.32752)). These are separate approaches to capability over time, not a single new paradigm.
- **Category concentration:** among the selected papers, primary categories are four `cs.AI`, two `cs.CL`, two `cs.LG`, one `cs.RO`, and one `cs.SE`; most are cross-listed into another configured AI category. This selection favors agent-system relevance and is not a measure of the full batch's category distribution.

## Open Problems and Research Directions

- **[Author-stated open problem]** Extend MCP-Injector to multi-server orchestration and longer-horizon tasks, then test fault-aware planning and recovery interventions against calibrated failure profiles ([MCP-Injector](https://arxiv.org/abs/2610.32555)).
- **[Author-stated open problem]** Test repeated updates in natural software-development workflows; a useful follow-up would vary update count and timing while measuring preservation, recovery, and evidence freshness ([SWE-Shift](https://arxiv.org/abs/2610.32196)).
- **[Synthesis / proposed direction]** Compare repository-derived training environments with independently authored scientific tasks and prospective research workflows, using both outcome correctness and artifact/process checks; this would test how well POSEIDON's training data transfers to SCI-AGENT-EXAM-like tasks ([POSEIDON](https://arxiv.org/abs/2610.32448), [SCI-AGENT-EXAM](https://arxiv.org/abs/2610.32441)).
- **[Synthesis / proposed direction]** Replicate model–harness findings on additional harnesses, models, and task families, and report reliability and task correctness separately so that pair-specific strengths are not collapsed into one ranking ([When Agents Fail](https://arxiv.org/abs/2610.32483), [MCP-Injector](https://arxiv.org/abs/2610.32555)).
- **[Synthesis / proposed direction]** Test whether TopKLoRA's sparse circuit localization persists across multiple poisoning mechanisms and model scales, with blinded circuit discovery and checks for collateral capability loss ([TopKLoRA](https://arxiv.org/abs/2610.32866)).
- **[Synthesis / proposed direction]** For VLA failure prediction, measure calibration and false-alarm costs, test transfer to new embodiments, and evaluate whether interventions based on early SAE signals improve recovery rather than only predicting failure ([Do VLAs Know They Will Fail?](https://arxiv.org/abs/2610.32208)).
- **[Synthesis / proposed direction]** Re-evaluate ActionRAG on independent long-history and conflict-heavy memory benchmarks, with end-to-end latency and cost measured across hardware, to test whether its reported retrieval gains persist beyond MemoryAgentBench ([ActionRAG](https://arxiv.org/abs/2610.32752)).

## Takeaway

The strongest common signal in this batch is a move toward testing AI agents as complete, failure-prone systems: evaluation now includes tool faults, changing state, harness behavior, and verifiable scientific work. Several papers provide substantial new benchmarks or infrastructure, but these are fresh preprints with limited independent citation evidence; whether their gains transfer beyond the reported task sets remains uncertain.

## Method and sources

- **Window:** the latest available daily batch at the snapshot was Friday 23 October 2026; the report covers submissions dated 2026-10-23 only. Snapshot: 2026-10-26 17:05 UTC. The Monday 26 October announcement batch was not yet available at snapshot time. All 10 selected papers are v1 new submissions, not revisions.
- **Scope/query:** core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; arXiv API query: `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`, sorted by `submittedDate` descending. The broad 1,000-record query included all eight configured categories; 537 Friday core-category memberships were observed before deduplication across cross-lists.
- **Inference:** arXiv supplies no official trending ranking. Entries were selected and ordered using checkable conference/research discussion signals where found, cross-list breadth, available code/artifacts, and paper-reported evaluation scope; recency was only a tie-breaker. No downloads/views or unsupported social metrics were inferred. Semantic Scholar citation counts were not available in the retrieved snapshot and were not used.
- **Primary sources:** each linked arXiv abstract page above is the primary source for metadata and abstract claims. Full arXiv HTML was consulted for the MCP-Injector, SWE-Shift, and POSEIDON introductions/results/limitations. Additional checkable corroboration: [NeurIPS poster listing for MCP-Injector](https://neurips.cc/virtual/2026/poster/151564); [SWE-Shift project repository](https://github.com/JeixHuang/SWE-Shift); [OpenReview record for SCI-AGENT-EXAM](https://openreview.net/forum?id=FWttsRrLIf); [technical discussion of When Agents Fail](https://syncai.news/article/when-agents-fail-model-or-harness-who-s-to-blame-f028d8); [RobustRLlib project site](https://robustrl-lib.github.io/) and [repository](https://github.com/robustrl-lib/robustrllib); [OpenReview record for On-Policy Self-Training](https://openreview.net/forum?id=ECDqq3THo7); [Hugging Face Papers listing](https://huggingface.co/papers/2610.32770).
- **Caveat:** “Notable recent papers” is the appropriate reading of this list: the batch is days old, no official arXiv trend chart exists, and independent citation evidence is too limited to establish a popularity ranking.
