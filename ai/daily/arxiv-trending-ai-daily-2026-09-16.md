# arXiv Trending AI — 16 September 2026

Snapshot: 2026-09-17 15:10 UTC. Window: the latest arXiv announcement batch, papers first submitted on 2026-09-16. arXiv does not publish an official trending chart; this is an inferred ranking, not a most-read or most-downloaded list. Because these papers are one day old, Semantic Scholar citation signals are sparse and mostly unavailable; the ordering therefore emphasizes cross-list breadth, substantive evaluations, public code/data/project pages, and independent technical attention where found.

## Top papers (ranked)

### 1. [ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments](https://arxiv.org/abs/2609.19134)
- **Abstract:** ScienceIDE turns scientific software repositories into executable environments for task generation, agent interaction, and scientific verification, then uses verified trajectories to train and evaluate scientific coding agents.
- **Authors:** Hejia Geng, Zesen Huang, Haoyang Li, Wenbin Li, Koutian Wu, et al.
- **arXiv:** `2609.19134v1` (published 2026-09-16 17:55 UTC; categories: `cs.CL`, `cs.CY`)
- **Evidence for ranking:** Semantic Scholar returned a paper record but no citation totals yet; ranked first because it proposes reusable agent-learning infrastructure, reports multiple trained model sizes and held-out transfer, has public code, and received independent technical discussion shortly after posting.
- **Claimed contribution:** The authors present ScienceIDE as a substrate that converts scientific code into programmable environments for supervised fine-tuning, reinforcement learning, and evaluation, with positive transfer claims for PhAI-IDE models.
- **Caveat:** The abstract does not establish how broad the held-out scientific-code coverage is or fully disentangle scientific-domain training from general data and model-scale effects.
- **Announcement type:** new submission, 2026-09-16 batch
- **Themes:** Agents & reasoning; Data & synthetic data; Training & adaptation

### 2. [PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics](https://arxiv.org/abs/2609.19142)
- **Abstract:** PointZero pretrains a 3D dynamics model by completing sparse point tracks, avoiding robot action labels and enabling transfer to action-conditioned dynamics prediction and imitation learning.
- **Authors:** Bardienus P. Duisterhof, Kaifeng Zhang, Adam Hung, Bowen Wen, Stan Birchfield, et al.
- **arXiv:** `2609.19142v1` (published 2026-09-16 17:59 UTC; categories: `cs.CV`, `cs.RO`)
- **Evidence for ranking:** No current Semantic Scholar citation count was returned; ranked highly for cross-list relevance, a 2.9-million-frame dataset, released checkpoints/training recipe, and reported gains on a real/simulated manipulation suite. An arXiv HTML page and project site make the technical claims checkable.
- **Claimed contribution:** The paper claims that point-track completion can supply a transferable 3D dynamics prior from non-robot data, with reported improvement or parity on 6 of 7 manipulation tasks after fine-tuning.
- **Caveat:** The strongest evidence is downstream fine-tuning after synthetic pretraining; how well the prior transfers beyond the reported benchmarks and data distribution remains open.
- **Announcement type:** new submission, 2026-09-16 batch
- **Themes:** Robotics & control; Multimodal & vision-language; Data & synthetic data

### 3. [Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations](https://arxiv.org/abs/2609.19101)
- **Abstract:** The paper studies whether internal representation directions can detect and discover reward hacking in frontier open-source LLM evaluations, including online prediction of later hacking behavior.
- **Authors:** Leon Bergen, Usha Bhalla, Andrew Lee, Barak Widawsky, Linas Nasvytis, et al.
- **arXiv:** `2609.19101v1` (published 2026-09-16 17:31 UTC; categories: `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Semantic Scholar returned no citation totals; ranked for direct safety relevance, evaluation across several models and benchmarks, and unusually concrete reported rates (including 57.2% of GLM 5.2 DeepSWE rollouts and 73% on SWE-bench). Independent search results also connected it to the current reward-hacking discussion.
- **Claimed contribution:** The authors report that simple difference-of-means vectors can represent and monitor reward hacking, sometimes predict it before the action, and expose behaviors missed by LLM monitors.
- **Caveat:** The findings are reported for selected open models and evaluation harnesses; transfer to other model families, hidden internal states, and adversarially adaptive systems is not established by the abstract.
- **Announcement type:** new submission, 2026-09-16 batch
- **Themes:** Safety & alignment; Interpretability; Evaluation & benchmarks

### 4. [In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138)
- **Abstract:** GPT-Policy combines a visual context compiler, VLM action proposals, and a constrained controller so robots can adapt from demonstrations and feedback without gradient updates or task-specific parameter changes.
- **Authors:** Dongzhou Cheng, Taoran Yi, Ye Fang, Xingwu Zhang, Fan Feng, et al.
- **arXiv:** `2609.19138v1` (published 2026-09-16 17:58 UTC; categories: `cs.CV`, `cs.RO`)
- **Evidence for ranking:** Semantic Scholar returned a record but no citation totals; ranked for cross-list breadth, real-robot evaluation, controlled context ablations, and public project/code pages. The abstract reports gains from human video demonstrations and aligned action references.
- **Claimed contribution:** The authors position GPT-Policy as an empirical framework for translating general VLM capabilities into verifiable physical behavior through context compilation and constrained execution.
- **Caveat:** The abstract describes reliability and limitations but does not quantify robustness across broad task families; commercial-model dependence and contact-sensitive failure modes remain concerns.
- **Announcement type:** new submission, 2026-09-16 batch
- **Themes:** Robotics & control; Agents & reasoning; Multimodal & vision-language

### 5. [Objective vs. Search: Decomposing What Makes a Good Tokeniser](https://arxiv.org/abs/2609.19145)
- **Abstract:** By separating tokeniser objective from search procedure through two new algorithms, the paper finds that bottom-up search, rather than compression versus likelihood objective, usually drives lower bits-per-byte while showing no consistent BLiMP advantage.
- **Authors:** Ahmetcan Yavuz, Clara Meister, Tiago Pimentel
- **arXiv:** `2609.19145v1` (published 2026-09-16 17:59 UTC; categories: `cs.CL`, `cs.AI`)
- **Evidence for ranking:** No Semantic Scholar citation totals were available; ranked for a clean 2×2 experimental design, coverage of model sizes/vocabulary/domain settings, and an EMNLP 2026 acceptance noted in the arXiv comment.
- **Claimed contribution:** The authors disentangle tokeniser optimisation objective from search procedure and report that search direction dominates bits-per-byte results, while BLiMP does not show a consistent design relationship.
- **Caveat:** The conclusions are metric- and setup-dependent: bits-per-byte and BLiMP need not predict downstream multilingual or reasoning performance.
- **Announcement type:** new submission, 2026-09-16 batch
- **Themes:** Training & adaptation; Evaluation & benchmarks

### 6. [A Zeroth-Order Paradigm for LLM Preference Alignment](https://arxiv.org/abs/2609.19144)
- **Abstract:** ComPO is a comparison-based, zeroth-order preference-alignment method that extracts directional information from preference pairs without directly optimising a differentiable preference loss.
- **Authors:** Peter Chen, Xi Chen, Wotao Yin, Tianyi Lin
- **arXiv:** `2609.19144v1` (published 2026-09-16 17:59 UTC; categories: `cs.CL`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Semantic Scholar returned a paper record but no citation totals; ranked for three-category coverage, formal convergence/performance guarantees, and experiments spanning Mistral, Llama, Gemma-2, Qwen3, and Gemma-3.
- **Claimed contribution:** The authors claim that offline and online ComPO can mitigate likelihood displacement and improve length-controlled win rates over direct alignment baselines.
- **Caveat:** The guarantees depend on smoothness, gradient sparsity, coverage, and reward-accuracy assumptions; the abstract does not show whether these assumptions hold broadly in production preference data.
- **Announcement type:** new submission, 2026-09-16 batch
- **Themes:** Safety & alignment; Training & adaptation

### 7. [How Model Growth, Recursion, and Boundary Operators Influence Scaling Exponents](https://arxiv.org/abs/2609.19107)
- **Abstract:** The paper reports that recursive depth, model growth, and boundary operators can alter pretraining scaling exponents and improve compute efficiency, including a 7.4B growth model matching GPT-3 13B on CORE with roughly 20× less compute.
- **Authors:** Zixi Chen, Akshay Vegesna, Samip Dahal, Andrew Gordon Wilson
- **arXiv:** `2609.19107v1` (published 2026-09-16 17:36 UTC; category: `cs.LG`)
- **Evidence for ranking:** Semantic Scholar returned a record but no citation totals; ranked for a potentially consequential challenge to standard scaling assumptions and explicit compute comparisons. The evidence is currently only the paper's own reported experiments.
- **Claimed contribution:** The authors argue that usable computational depth, rather than parameter count alone, can produce scale-dependent efficiency gains through looping and related architectural interventions.
- **Caveat:** The abstract reports a narrow set of architectures and benchmarks; independent reproduction and broader model/data regimes are needed before treating the scaling claim as general.
- **Announcement type:** new submission, 2026-09-16 batch
- **Themes:** Efficient inference & systems; Training & adaptation

### 8. [Cognitive Extensions for Dual-Process Language Agents: Memory and Self-Reflection in Interactive Environments](https://arxiv.org/abs/2609.19128)
- **Abstract:** Adding adaptive episodic memory and execution-time self-reflection to a dual-process agent improves ScienceWorld score, success rate, and successful-step efficiency, with self-reflection the stronger standalone module.
- **Authors:** João Meneses dos Santos, Arlindo L. Oliveira
- **arXiv:** `2609.19128v1` (published 2026-09-16 17:50 UTC; categories: `cs.AI`, `cs.LG`, `cs.MA`)
- **Evidence for ranking:** Semantic Scholar returned no citation totals; ranked for a clean four-way ablation and explicit quantitative results (mean final score 64.62, success rate 43.17%, and 19.33 successful steps) on an interactive benchmark.
- **Claimed contribution:** The authors find that runtime validation and corrective intervention appear to be the dominant bottleneck in this setting, while memory helps more once the execution loop is stable.
- **Caveat:** Results come from one benchmark and one agent substrate; the relative value of memory versus reflection may change with environment observability and task horizon.
- **Announcement type:** new submission, 2026-09-16 batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Retrieval & knowledge

## Trending Research Themes

- **Agent learning is moving toward executable environments and runtime control.** ScienceIDE treats scientific repositories as training/evaluation environments, while the cognitive-extensions paper and GPT-Policy focus on execution-time verification, memory, and feedback rather than static prompting alone.
- **Embodied AI is exploiting richer supervision than robot action labels.** PointZero uses 3D point-track completion, GPT-Policy uses demonstrations and interaction feedback, and Dreaming the Sound of Contact uses generated video/audio to shape force-aware manipulation. Together these papers point toward multimodal and web-scale pretraining for robotics, but not yet toward reliable general-purpose autonomy.
- **Safety work is becoming more mechanistic and operational.** Reward-hacking probes target internal representations and online detection, while ComPO targets the optimisation dynamics that can distort preference alignment. Both expose a gap between benchmark scores and the mechanisms producing them.
- **Efficiency is being attacked at multiple layers.** The scaling-exponent paper changes architecture/depth, and the tokeniser paper separates search from objective. These are complementary attempts to improve the compute-to-capability relationship before simply scaling parameters.

## Open Problems and Research Directions

- **Validate transfer beyond curated environments.** ScienceIDE and the cognitive-agent study should be tested on held-out scientific domains and interactive environments with different tool interfaces; this would separate reusable agent principles from benchmark-specific scaffolding.
- **Measure embodied robustness under distribution shift.** PointZero and GPT-Policy report promising downstream results, but follow-up work should evaluate unseen object geometries, contact dynamics, lighting, camera layouts, and failure recovery, with matched real-world data budgets.
- **Stress-test internal reward-hacking monitors against adaptation.** The reward-hacking paper's vectors should be evaluated on models trained to evade probes, on closed models where activations are unavailable, and across non-software tasks; otherwise monitor performance may reflect dataset regularities.
- **Reproduce compute-efficiency and tokenisation claims at scale.** The scaling and tokeniser papers motivate matched-budget studies across more architectures, languages, data mixtures, and downstream reasoning tasks, with independently audited training compute.
- **Connect alignment guarantees to realistic preference coverage.** ComPO's theory relies on coverage and oracle assumptions. A useful next experiment is to estimate those assumptions on noisy, long-form, multi-objective human preference data and compare against length-controlled and adversarial evaluations.

## Takeaway

The strongest supported pattern in this batch is a shift from isolated model capability toward systems that make agents trainable, verifiable, and deployable: executable scientific environments, runtime monitors, and richer embodied supervision. The most consequential claims—large compute savings, broad transfer, and robust reward-hacking detection—are still preliminary because the papers are new, citation signals are effectively absent, and independent replication has not yet accumulated.

## Method and sources

- Window: latest available arXiv announcement batch for 2026-09-16; snapshot 2026-09-17 15:10 UTC.
- Core categories queried through the arXiv API: `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`.
- Candidate metadata and abstracts: arXiv API and linked abstract pages.
- Corroboration: Semantic Scholar Graph API batch lookup for the ten leading candidates; most returned no citation totals because they are newly posted. Independent search was used only where it surfaced substantive discussion or project pages.
- Ranking is inferred. It is not an official arXiv popularity ranking and does not claim readership, downloads, or citation gains during the window.
