# arXiv AI: latest announcement batch — 11 November 2026

Eight notable recent papers, with a clear cluster around agents that learn from experience and are evaluated in more realistic settings. The agenda: start with compiling agent behavior and safer memory updates, then look at post-training theory, training scaffolds, evaluation, and inference efficiency. arXiv has no official trending chart; this ordering is inferred, and the batch is too recent for citation counts to establish popularity, so the list is a relevance-led shortlist rather than a measured popularity ranking.

## Top papers (ranked)

### 1. [ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows](https://arxiv.org/abs/2611.14492)
- **Abstract:** ReTrace converts SOPs and a few reasoning-and-tool-call traces into executable workflows where code chooses each next step, reporting lower runtime cost and latency with a small completion trade-off on its tested procedures.
- **Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, et al.
- **arXiv:** `2611.14492v1` (published 2026-11-10T18:49:47Z; categories: `cs.AI`, `cs.LG`, `cs.MA`)
- **Evidence for ranking:** Strongest applied evidence in this shortlist: 79 production procedures plus two public benchmarks, with the paper reporting 24% lower enterprise cost and a 170s-to-1.3s runtime change on τ²-Bench. It also has a substantive independent technical discussion ([Learn Agentic](https://learnagentic.substack.com/p/your-agent-took-170-seconds-its-compiled)).
- **Claimed contribution:** The authors extract action conditions and input sources from agent reasoning and tool records, merge them into evidence-linked rules, and compile these into executable workflows; results cover one production platform and two benchmarks.
- **Caveat:** The authors say recovered conditions are not proven correct by their construction checks; their evaluation tests new inputs to the same procedures, not transfer to new procedures, and the public tests cover only the telecom τ²-Bench domain and eight SOP-Bench domains.
- **Announcement type:** new submission, announcement batch 2026-11-11
- **Themes:** Agents & reasoning; Efficient inference & systems

### 2. [When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](https://arxiv.org/abs/2611.14326)
- **Abstract:** FGSE represents proposed agent-memory updates as hypotheses and tests transfer, counterexamples, and regression risk before committing them, reporting results across web, app, tool-use, and long-term-memory benchmarks.
- **Authors:** Runxuan Tang, Haoyu Gao, Yuyan Ding, Junyi Yao, Zihao Zheng, et al.
- **arXiv:** `2611.14326v1` (published 2026-11-10T16:52:25Z; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The paper reports multiple task settings and concrete safety-related outcomes (including 5.0% falsification failures and 1.3% regression damage); it also received independent coverage from [Grafy News](https://grafy.ai/news/fgse-wants-verifier-approval-for-agent-memory). This supports relevance, not a measured readership rank.
- **Claimed contribution:** The authors introduce a verifier-grounded commit/refine/reject gate for persistent memory updates and report reduced harmful committed updates alongside benchmark performance.
- **Caveat:** The authors frame extension to multimodal agents and settings where verifiers must be learned or approximated as future work; the reported approach assumes verifier-rich environments.
- **Announcement type:** new submission, announcement batch 2026-11-11
- **Themes:** Agents & reasoning; Safety & alignment; Training & adaptation

### 3. [A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets](https://arxiv.org/abs/2611.14467)
- **Abstract:** The paper analyzes how policy-gradient updates can lose access to high-reward responses even as reward rises, then gives coverage-preserving convergence guarantees for methods that periodically reset their KL reference.
- **Authors:** Audrey Huang, Nan Jiang, Sham M. Kakade, Sadhika Malladi, Akshay Krishnamurthy, Dylan J. Foster
- **arXiv:** `2611.14467v1` (published 2026-11-10T18:31:36Z; categories: `cs.LG`, `stat.ML`)
- **Evidence for ranking:** The paper cross-lists across two configured AI-corpus categories and directly addresses a central post-training design question; its full arXiv text lays out the theoretical argument and limitations. Ranking is by methodological relevance, not citation momentum.
- **Claimed contribution:** The authors define coverage-preserving policy optimization, describe a coverage-collapse failure for REINFORCE, and use Approximate Policy Mirror Descent/reference resets to prove global convergence for stylized PPO/GRPO and squared-loss families under stated assumptions.
- **Caveat:** The authors limit end-to-end guarantees to softmax linear policies over pretrained features and a one-shot response setting; they note that richer policies, token-sequence effects, and multi-step reasoning remain open.
- **Announcement type:** new submission, announcement batch 2026-11-11
- **Themes:** Training & adaptation; Agents & reasoning

### 4. [AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models](https://arxiv.org/abs/2611.14515)
- **Abstract:** AutoScaffold uses a frozen teacher to adapt strategies and hints from a student's RL training experience, then evaluates the student without those scaffolds across four domains.
- **Authors:** Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, et al.
- **arXiv:** `2611.14515v1` (published 2026-11-10T18:58:46Z; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** It spans four distinct training/evaluation domains and is cross-listed in machine learning and computation/language; the OpenReview listing provides a second checkable description of the approach ([OpenReview](https://openreview.net/forum?id=KPRr8wWiqO)).
- **Claimed contribution:** The authors report that students trained with adaptive strategy-level and task-level hints outperform corresponding RL baselines after the hints are removed, with reported gains in ALFWorld, QA, math, and GPU-kernel generation.
- **Caveat:** Results are limited to the four tested domains and the teacher-guided training setup; the reported comparisons do not establish transfer to broader, unseen training regimes.
- **Announcement type:** new submission, announcement batch 2026-11-11
- **Themes:** Training & adaptation; Agents & reasoning

### 5. [ARE-bench: Benchmarking Agents' Research Ability in Real-World Researcher Sessions and Workspaces](https://arxiv.org/abs/2611.14364)
- **Abstract:** ARE-bench tests whether research agents can make progress on ongoing projects while respecting prior decisions and messy existing workspaces, using 75 tasks drawn from real researcher sessions.
- **Authors:** Jiahang Lin, Wanying Ren, Wanghan Xu, Huayu Sha, Yang Shu, et al.
- **arXiv:** `2611.14364v1` (published 2026-11-10T17:21:31Z; categories: `cs.CL`)
- **Evidence for ranking:** The benchmark has concrete scale (75 tasks, seven research stages, 1,173 checklist items) and was discussed by [Agentic Design](https://agentic-design.ai/news-hub/are-bench-benchmarking-agents-research-ability-real-world-researcher-sessions-17c468), giving an independent pointer beyond its abstract.
- **Claimed contribution:** The authors introduce an evaluation set preserving prior session requirements and workspace state; they report that the strongest of seven evaluated models passes every checklist item on 66.2% of tasks.
- **Caveat:** The paper evaluates one curated set of 75 tasks from recruited researchers' projects; performance on this dataset does not by itself establish reliability across disciplines or new project environments.
- **Announcement type:** new submission, announcement batch 2026-11-11
- **Themes:** Evaluation & benchmarks; Agents & reasoning

### 6. [Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](https://arxiv.org/abs/2611.14493)
- **Abstract:** This study compares trace-based judging, text-only judging with red-teaming, and deterministic heuristics on two analytics agents, measuring repeatability, known-risk detection, and discovery of new failures.
- **Authors:** Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary, Lily Miao
- **arXiv:** `2611.14493v1` (published 2026-11-10T18:50:06Z; categories: `cs.AI`, `cs.CL`, `cs.LG`, `cs.SE`)
- **Evidence for ranking:** It is cross-listed across four configured/core-adjacent categories and its arXiv record notes acceptance to KDD 2026; its abstract reports a three-phase comparison and 24 discovered failures.
- **Claimed contribution:** The authors find trace-based judging has the strongest precision-recall balance on their known-risk set and recommend combining trace-based functional evaluation with adversarial red-teaming.
- **Caveat:** The experiment covers two analytics agents in a controlled setting using frozen traces, so its relative framework results may not transfer unchanged to other agent types or live environments.
- **Announcement type:** new submission, announcement batch 2026-11-11
- **Themes:** Evaluation & benchmarks; Safety & alignment; Agents & reasoning

### 7. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)
- **Abstract:** WikiTrace links each stored lesson to its supporting trajectory and lets an agent retrieve that evidence when a lesson is incomplete, conflicting, or based on failure; the authors report gains across five agentic benchmarks.
- **Authors:** Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
- **arXiv:** `2611.14320v1` (published 2026-11-10T16:46:59Z; categories: `cs.AI`, `cs.MA`)
- **Evidence for ranking:** The paper is cross-listed in AI and multiagent systems, reports five benchmark evaluations, and provides a public implementation ([GitHub](https://github.com/yukyeongleee/wikitrace)).
- **Claimed contribution:** The authors combine concise memory insights with summaries and raw trajectories, enabling tool-assisted evidence checks before acting; they report reduced memory-induced degradation relative to memory baselines.
- **Caveat:** The method depends on retaining and retrieving the source trajectory for each insight; the abstract reports evaluation on five agentic benchmarks, not unrestricted deployment settings.
- **Announcement type:** new submission, announcement batch 2026-11-11
- **Themes:** Agents & reasoning; Retrieval & knowledge

### 8. [REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding](https://arxiv.org/abs/2611.14399)
- **Abstract:** REAL derives an unbiased, variance-reduced loss for training speculative-decoding draft models against the actual token-acceptance process rather than surrogate distribution-overlap objectives.
- **Authors:** Yu Tian
- **arXiv:** `2611.14399v1` (published 2026-11-10T17:45:12Z; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** It is cross-listed in machine learning and language technology, reports a five-seed comparison across nine task subsets, and provides a reference implementation ([GitHub](https://github.com/King-ty/speculators/tree/real-loss)).
- **Claimed contribution:** The author derives path-weighted REAL with Rao-Blackwellization and reports higher probabilistic serving acceptance length than four compared losses in the tested Qwen3.6-35B-A3B/Domino setup.
- **Caveat:** The reported evaluation is a controlled loss-level comparison for one target/drafter configuration; it does not establish the same gains across other architectures or serving workloads.
- **Announcement type:** new submission, announcement batch 2026-11-11
- **Themes:** Efficient inference & systems; Training & adaptation

## Trending Research Themes

- **Agent experience is being made safer and more operational.** FGSE and WikiTrace both treat stored lessons as fallible: FGSE probes a proposed behavior change before committing it, while WikiTrace retrieves the underlying trajectory when a memory needs checking. ReTrace takes a different route, compiling recurring SOP behavior into code for repeated execution.
- **Post-training is getting attention at both the algorithm and data/scaffold levels.** The policy-optimization theory studies how to retain access to good responses during learning; AutoScaffold uses a teacher to turn sparse outcome feedback into temporary training guidance. These are distinct contributions, not yet evidence of one settled recipe.
- **Evaluation is shifting from isolated answers to process context and failure discovery.** ARE-bench preserves prior decisions and project files, while the comparative evaluation paper tests both known-risk detection and discovery of previously unknown failures. Their shared emphasis is on context and evaluation harness design, not just final-answer scoring.
- **Efficiency work is moving across deployment stages.** ReTrace reduces repeated planning at runtime, whereas REAL Loss targets draft-model acceptance during speculative decoding. Both claim measurable efficiency gains, but in different workloads and with different quality trade-offs.

## Open Problems and Research Directions

- **Author-stated open problem — post-training theory:** The policy-optimization guarantees cover softmax linear policies and one-shot responses, while real model outputs are token sequences and agentic tasks are multi-step. A useful next experiment would test whether reference resets preserve response coverage in full-model RL runs, then in multi-turn environments, with token-level diagnostics. [A Theory of Policy Optimization in Post-Training]
- **Author-stated open problem — memory verification:** FGSE identifies learned or approximate verifiers and multimodal settings as future extensions. Compare verifier quality and update-gate error rates as tasks become less mechanically checkable; include long-horizon tests for harmful updates that pass local probes. [When Should Agents Remember?]
- **Author-stated open problem — workflow correctness:** ReTrace says construction checks do not verify recovered conditions, and performance depends on which branches the sampled traces cover. Test branch-diverse trace selection, independent human audits of outcomes, and automated precondition checks before deployment; include SOP/tool changes and transfer to new procedures. [ReTrace]
- **Evidence-tied synthesis — contextual evaluation:** ARE-bench finds that adding historical and workspace requirements materially changes assessed performance, while the enterprise-framework study finds complementary failure discovery from functional and security tests. A follow-up could replay the same agents across multiple project domains and live or changing workspaces, measuring checklist reliability, judge disagreement, and false alarms. [ARE-bench; Comparative Analysis of Agent Evaluation Frameworks]

## Takeaway

This batch's clearest pattern is systems work around the agent lifecycle: how to learn from experience without corrupting memory, compile repeated behavior, and evaluate work in context. The strongest performance claims are still tied to specific datasets, evaluators, and simplified theory; wider replications will determine which methods travel.

## Method and sources

- **Window:** Daily latest arXiv announcement batch dated 2026-11-11; start and end date 2026-11-11. This was the latest batch, not a prior-batch fallback. The selected papers are new submissions, not revisions.
- **Snapshot:** 2026-11-12 01:10:10 UTC.
- **Corpus:** Core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`. arXiv's recent listings showed 11 November batch counts of 248, 235, 28, 112, 149, 69, 7, and 10 respectively; category totals overlap due to cross-listing and are not unique-paper counts. A broad 200-result arXiv API snapshot informed candidate discovery; each of the eight selected arXiv abstract pages was then verified individually. This is a relevance-led shortlist, not a comprehensive ranking of the entire batch.
- **Inference:** arXiv does not provide a trending or readership ranking. Papers were ordered using checkable signals: relevant category cross-listing, breadth and specificity of reported evaluations, public artifacts, independent technical discussion where found, and publication/comment metadata. Citation velocity was not used because current citation totals could not be established from the sources available at this snapshot.
- **Sources:** [arXiv cs.AI recent listings](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), [cs.MA](https://arxiv.org/list/cs.MA/recent); selected paper records are linked above. For full text, the top three papers were read via arXiv HTML: [policy-optimization theory](https://arxiv.org/html/2611.14467), [ReTrace](https://arxiv.org/html/2611.14492), and [FGSE](https://arxiv.org/html/2611.14326). Additional corroborating sources are linked in the relevant entries.
