# arXiv AI Trending — Daily | 2026-11-09

Daily arXiv AI announcement batch (Mon, 9 Nov 2026): five ranked papers, led by agent test-time scaling and sharper safety evaluation. Spoken agenda: parallel agent teams, weight-space edits, and why familiar safety scores can mislead. Global caveat: arXiv has no official trending chart; this ordering is inferred from checkable attention and corroboration signals, and citation evidence is limited for papers this recent.

## Top papers (ranked)

### 1. [Test-Time Compute Scales Better with Parallel Agent Teams](https://arxiv.org/abs/2611.09798)
- **Abstract:** The paper proposes sampling many small collaborating agent teams in parallel and keeping the best team's result, reporting gains over independent agents and one large team on long-horizon tasks.
- **Authors:** Junlin Wang, Haozhe Chen, Ang Li, Rahul Chalamala, Zhuang Liu
- **arXiv:** `2611.09798v1` (published 2026-11-06 17:53:07 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Featured among the 10 highlights in the 9 Nov AI Paper Digest and separately surfaced by [AI Agents Info](https://www.aiagentsinfo.com/research/parallel-agent-teams-test-time-compute) and [Cool Papers](https://papers.cool/arxiv/2611.09798); its cross-source coverage is the strongest attention signal in this selection. Citation momentum was not used.
- **Claimed contribution:** The authors report that, with a 27B model and budget of 100 agents, teams of ten beat parallel individual agents on 10 of 12 tasks and beat a single 100-agent team on all four tasks tested at that size.
- **Caveat:** The paper states that run pools are small (10–11 runs per task), larger-team tests used only one to five runs per size, and experiments use one agent harness; without a verifier, choosing the best team becomes an additional problem.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Efficient inference & systems

### 2. [Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations](https://arxiv.org/abs/2611.09382)
- **Abstract:** Across 16 editing trajectories, seven benchmarks, and two model sizes, the authors find that localized weight edits can yield large but uneven gains and that candidate edits are not reliably validated.
- **Authors:** Junru Hu, Cheng Tang, Wei Li, Hongze Zhu, Chun-Mei Feng et al.
- **arXiv:** `2611.09382v1` (published 2026-11-06 12:22:24 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Featured as an AI Paper Digest highlight; the [Hugging Face paper page](https://huggingface.co/papers/2611.09382) displayed 7 upvotes at the snapshot, a directly checkable attention signal. Its two-category listing adds breadth; citation momentum was not used.
- **Claimed contribution:** The authors report held-out accuracy gains from modifying as few as 1,023 parameters, while documenting uneven cross-task transfer and six of 16 trajectories that retained the original weights when candidate gains could not be validated reliably.
- **Caveat:** Editing outcomes vary substantially across trajectories, and the reported study covers two model scales and a limited set of editing runs; reliable validation of candidate interventions remains unresolved.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Training & adaptation; Agents & reasoning; Evaluation & benchmarks

### 3. [Forcing a Letter Suppresses Refusal: Mechanistic Evidence from WMDP](https://arxiv.org/abs/2611.08639)
- **Abstract:** Using WMDP and two 8B models, the authors find that multiple-choice answer-letter selection is associated with reduced refusal signals and show that ablating relevant attention heads restores refusal in one model.
- **Authors:** Stepan Epifantsev, Anna Antipova, Oleg Chernikov, Leon Strelkov, Alexey Dontsov
- **arXiv:** `2611.08639v1` (published 2026-11-05 19:36:44 UTC; categories: `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Featured among the 9 Nov AI Paper Digest highlights, cross-listed in two core AI categories, and accepted to the [BlackboxNLP 2026 workshop](https://aclanthology.org/2026.blackboxnlp-1.27/). The venue record and category breadth corroborate the digest signal; citation momentum was not used.
- **Claimed contribution:** The authors use tuned-lens and refusal-direction analyses on Llama-3.1-8B and Qwen3-8B, plus attention-head ablation on Llama-3.1-8B, to argue that answer selection under MCQ formatting competes with refusal formation.
- **Caveat:** The study is limited to two 8B models and WMDP; the causal head-ablation finding is established on Llama-3.1-8B, while the corresponding Qwen3-8B results are weaker or do not reproduce the effect.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Safety & alignment; Evaluation & benchmarks; Interpretability

### 4. [Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents](https://arxiv.org/abs/2611.08946)
- **Abstract:** Flex-RSI benchmarks fixed-budget agent self-improvement on vision and robotics tasks by allowing agents to revise both task solutions and their harnesses, and reports that the gains and failure modes vary by model and task.
- **Authors:** Jingdong Zhang, Jionghao Wang, Zhengming Yu, Yancheng Cai, Wei Chow et al.
- **arXiv:** `2611.08946v1` (published 2026-11-06 03:51:20 UTC; categories: `cs.AI`, `cs.CV`, `cs.RO`)
- **Evidence for ranking:** Featured in the 9 Nov AI Paper Digest; its three-way cross-list across AI, vision, and robotics is the broadest in this selection, and the authors provide a [project page](https://flex-rsi.github.io/) and [benchmark repository](https://github.com/flex-rsi/rsi-bench). This is corroborating release evidence, not a citation or readership claim.
- **Claimed contribution:** The authors introduce a benchmark in which an executor improves a task solution and an improver revises the harness, with hidden-test scoring; paired runs indicate harness editing contributes to measured gains.
- **Caveat:** The evidence is bounded to fixed-budget vision and robotics tasks; benchmark gains do not by themselves establish general recursive self-improvement on other task families or deployment settings.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Robotics & control

### 5. [Not All Misalignment Is Alike: A Decomposed Benchmark for Emergent Misalignment](https://arxiv.org/abs/2611.08569)
- **Abstract:** EMERGE measures eight forms of emergent misalignment against matched benign controls while tracking capability-related confounders, finding that models with similar overall rates can show different behavioural profiles.
- **Authors:** Afonso Domingues, Mubashara Akhtar, Bhada Yun, Xin Chen, Lukas Fluri, Anna Hedström
- **arXiv:** `2611.08569v1` (published 2026-11-05 18:09:46 UTC; categories: `cs.LG`)
- **Evidence for ranking:** Included in the 9 Nov AI Paper Digest's 10 highlights and indexed by [arXivSignals](https://arxivsignals.io/papers/2611.08569). This is a limited, early editorial/discovery signal; no citation evidence was available to support a stronger popularity claim.
- **Claimed contribution:** The authors evaluate eight behaviours across eight open-weight models and 13 fine-tuning datasets, using out-of-domain prompts, matched benign controls, and separate capability, coherence, and refusal measures.
- **Caveat:** The paper notes that LLM judges are not ground truth, human validation used one annotator, each model–dataset setting used one fine-tuning seed and LoRA configuration, and evaluation-set pretraining contamination cannot be ruled out.
- **Announcement type:** new submission, 2026-11-09 announcement batch
- **Themes:** Safety & alignment; Evaluation & benchmarks

## Trending Research Themes

- Agent performance is being studied as a system-and-budget problem, not only a model capability. Parallel Agent Teams varies how inference-time compute is allocated, while Flex-RSI lets agents change their own harness; both are benchmarked on bounded tasks, so neither establishes general agent autonomy.
- Safety evaluation is shifting from aggregate scores toward format-aware and behaviour-specific diagnostics. Forcing a Letter tests whether MCQ format masks refusal mechanisms, while EMERGE decomposes a single misalignment rate into distinct behavioural changes. Together they expose complementary measurement blind spots, not a single solved evaluation standard.
- Weight-space editing is a notable isolated signal rather than a recurring theme in this five-paper sample: the WSP study reports large localized gains but also uneven transfer and unreliable validation. More independent replications are needed before treating it as a general adaptation method.
- The selected batch spans cs.AI, cs.LG, cs.CL, cs.CV, and cs.RO. This is a curated five-paper sample, not a claim that those categories dominate the complete AI announcement batch.

## Open Problems and Research Directions

- **Author-stated open problem — agent scaling evidence:** Parallel Agent Teams reports small run pools, very few large-team trials, and one harness. **Research direction (synthesis):** replicate across independent harnesses, more diverse tasks and models, with enough runs to estimate uncertainty and with tasks where the verifier is imperfect. [Parallel Agent Teams](https://arxiv.org/abs/2611.09798)
- **Author-stated open problem — trustworthy measurement of emergent misalignment:** EMERGE's authors identify judge bias, single-annotator validation, single seeds/configurations, compute limits, and possible pretraining contamination. **Research direction (synthesis):** multi-annotator validation, multi-seed fine-tuning, paraphrased prompts, and explicit contamination checks would test the stability of its behavioural profiles. [EMERGE](https://arxiv.org/abs/2611.08569)
- **Author-stated open problem — format effects and model generality:** The WMDP study covers two 8B models, with the causal ablation effect established on Llama-3.1-8B and weaker findings on Qwen3-8B. **Research direction (synthesis):** repeat the mechanistic tests on larger and more diverse models, safety domains, and answer formats, reporting per-model uncertainty before proposing standardized format-refusal metrics. [Forcing a Letter](https://arxiv.org/abs/2611.08639)
- **Author-stated open problem — reliable editing:** WSP reports trajectory variability and six of 16 runs retaining original weights when gains could not be validated. **Research direction (synthesis):** test independent search seeds and preregistered held-out validation criteria, then audit whether localized edits transfer across models and tasks. [Weight-Space Programming](https://arxiv.org/abs/2611.09382)
- **Evidence-tied extension — scope of recursive self-improvement:** Flex-RSI's evidence is on fixed-budget vision/robotics tasks, and it finds open-weight models struggle more when strict physical or exact correctness checks apply. **Research direction (synthesis):** vary budget and task family, and test whether harness edits remain beneficial under real-world feedback and stricter safety constraints. [Flex-RSI](https://arxiv.org/abs/2611.08946)

## Takeaway

The batch's strongest shared signal is that agent capability and safety behavior depend on evaluation and system design: allocating inference compute, editing harnesses, and choosing answer formats all change what a benchmark measures. The claims are promising but preliminary, with small-scale or domain-specific evaluations and little citation evidence so far.

## Method and sources

- **Window:** daily; 2026-11-09 through 2026-11-09, the latest arXiv announcement batch shown at the top of the category recent pages (Mon, 9 Nov 2026). This uses the current batch, not a prior-batch fallback; the selected papers' version-1 submission timestamps are 2026-11-05 or 2026-11-06 UTC. Snapshot: 2026-11-09 17:12:40 UTC.
- **Scope/query:** core AI categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`; machine-readable query: `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`. The arXiv recent-list pages were checked across all eight categories. A 393-paper same-day editorial digest covered only `cs.AI`, `cs.LG`, and `cs.CL` and was used as one discovery/attention signal, not as a complete corpus ranking.
- **Inference:** arXiv has no official trend or readership ranking. Papers were deduplicated by versionless arXiv ID and ranked using repeated independent paper-digest/discovery coverage, visible Hugging Face upvotes where available, category breadth, and a conference/workshop record; recency was only a tie-breaker. No numerical trend score was constructed. The selected abstracts were verified on arXiv abstract pages; PDFs for the top three were read for results and stated limitations.
- **Citation check:** Semantic Scholar was checked, but it did not provide usable citation data for this new batch at the snapshot (one resolved lookup was not yet indexed and a batch attempt was rate-limited); citation momentum was not used. Retrieval limitation is recorded here rather than in paper-ranking evidence.
- **Sources:** [arXiv recent categories](https://arxiv.org/list/cs.AI/recent), [9 Nov AI Paper Digest](https://amarcu.github.io/ai-paper-digest/archive/2026-11-09.html), [AI Agents Info — parallel teams](https://www.aiagentsinfo.com/research/parallel-agent-teams-test-time-compute), [Cool Papers — parallel teams](https://papers.cool/arxiv/2611.09798), [Hugging Face — weight-space programming](https://huggingface.co/papers/2611.09382), [BlackboxNLP/Anthology — forcing a letter](https://aclanthology.org/2026.blackboxnlp-1.27/), [Flex-RSI project](https://flex-rsi.github.io/), and [arXivSignals — EMERGE](https://arxivsignals.io/papers/2611.08569). Individual arXiv abstract links are included with each entry.
