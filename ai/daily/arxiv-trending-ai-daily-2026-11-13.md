# arXiv Trending AI — Daily — 2026-11-13

Daily AI-paper brief for the Friday, 13 November 2026 announcement batch (10 papers). The most visible pattern is agentic systems being tested for dependable work: semi-supervised ML, prompt-injection defense, dynamic-world decisions, multi-model routing, and self-development benchmarks. Also on the agenda: a controlled rethink of multimodal vision encoders, energy-based reasoning, and how LLMs represent goals. This is an inferred evidence-ranked shortlist, not an official arXiv trending chart; citation evidence for these very recent papers is limited, so the ordering is tentative and does not indicate readership or downloads.

Snapshot: 2026-11-16 01:10:09 UTC. The latest batch available at that time was 2026-11-13; this daily report therefore uses a prior announcement batch. The papers below were first submitted on 2026-11-12.

## Top papers (ranked)

### 1. [AgentSSL: Can MLE Agents Leverage Unlabeled Data?](https://arxiv.org/abs/2611.17323)
- **Abstract:** The paper frames semi-supervised learning as agentic program search, reporting wins over human-engineered baselines in 8 of 12 settings while finding that choosing among generated programs can sharply reduce performance.
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **arXiv:** `2611.17323v1` (published 2026-11-12 18:59:06 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Cross-listed in AI and ML, marked NeurIPS 2026 in the arXiv record, and discussed by multiple technical write-ups (including [EigenRadar](https://eigenradar.com/en/ai/briefs/2026-11-13/agentssl-program-selection/) and [Ken Ashe](https://kenashe.ai/blog/2026-11-13-agentssl-shows-agents-can-write-useful-semi-supervised-training-code/)); the [NeurIPS poster page](https://neurips.cc/virtual/2026/poster/154115) is a checkable venue signal.
- **Claimed contribution:** The authors introduce AgentSSL and ProgramSelectBench (16,977 programs) and report that agent-generated strategies beat the strongest human-engineered baseline in 8/12 settings, by up to 21.8%.
- **Caveat:** The authors report that on both ecology tasks their supervised AgentSL baseline matches AgentSSL, and identify unlabeled-data use and program selection as unresolved parts of the search problem.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Training & adaptation; Agents & reasoning; Evaluation & benchmarks

### 2. [CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts](https://arxiv.org/abs/2611.17115)
- **Abstract:** CapLite derives write permissions from tool schemas and user-stated arguments rather than trusting an agent model to author its own security policy, and reports no successful attack across 13,935 attacked AgentDojo episodes.
- **Authors:** Zimo Xu, Wenzhuo Liu, Hideki Nakayama
- **arXiv:** `2611.17115v1` (published 2026-11-12 17:07:22 UTC; categories: `cs.AI`, `cs.CL`, `cs.CR`)
- **Evidence for ranking:** The work has several separate technical summaries, including [AI Modeling](https://www.aimodeling.com/en/news/slug/caplite-slm-prompt-injection-defense) and [CASRAI](https://casrai.org/news/caplite-prompt-injection-defense-small-language-models-2026), alongside its unusually large reported attack evaluation. The external discussion is a visibility signal, not a readership measure.
- **Claimed contribution:** The authors' CapLite design commits writes before reading tool results and permits them only when all consequential arguments were supplied by the user; their study reports zero successful attacks in the tested episodes.
- **Caveat:** The authors state that the evaluation uses only AgentDojo's four suites; CapLite's utility under attack is 21 points below the undefended agent, and the experiments use simulated environments rather than real users or accounts.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Safety & alignment; Agents & reasoning; Evaluation & benchmarks

### 3. [Unbundling Multimodal Vision Encoding](https://arxiv.org/abs/2611.17334)
- **Abstract:** In matched-compute experiments, the authors find that dedicated vision capacity matters more than a pretrained visual prior and can be placed inside early multimodal layers rather than in a separate pre-fusion encoder.
- **Authors:** Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, et al.
- **arXiv:** `2611.17334v1` (published 2026-11-12 18:59:54 UTC; categories: `cs.CV`, `cs.LG`)
- **Evidence for ranking:** The paper is cross-listed in vision and ML and received separate technical discussion from [Sparse Notes](https://sparsenotes.com/posts/2026/11/papers/unbundling-multimodal-vision-encoding/) and the [Hugging Face paper page](https://huggingface.co/papers/2611.17334). These provide discoverable technical discussion, not citation momentum.
- **Claimed contribution:** The authors isolate visual prior, dedicated vision parameters, and pre-fusion placement under common data and matched compute; they report comparable performance for early in-fusion modules and a conventional encoder.
- **Caveat:** The authors' controlled study uses dense backbones up to 6.4B parameters and 224×224 images; they leave sparse MoE models, higher-resolution training, richer data, and video/interleaved data for future work.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Multimodal & vision-language; Training & adaptation; Efficient inference & systems

### 4. [LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds](https://arxiv.org/abs/2611.17267)
- **Abstract:** LiveGeo and its GeoWorld environment test whether agents can acquire current geographic evidence and revise decisions as locations, traffic, weather, and other world states change; the authors report substantial reliability drops in dynamic settings.
- **Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, et al.
- **arXiv:** `2611.17267v1` (published 2026-11-12 18:45:58 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Independent technical coverage appeared at [AI Understanding](https://aiunderstanding.org/news/livegeo-benchmark-tests-geographic-ai-agents-in-evolving-environments) and [CASRAI](https://casrai.org/news/livegeo-geoworld-benchmark-geographic-ai-agents-2026); the paper describes a benchmark and environment release. The coverage and an inspectable artifact support inclusion, but do not establish adoption.
- **Claimed contribution:** The authors release GeoWorld and a benchmark of 1,237 verifiable tasks across seven geographic task categories; in their matched settings, mean success falls 70.3% under task-only dynamics and 79.3% under shared dynamics relative to static settings.
- **Caveat:** The evaluation covers nine models, six cities, and 149 matched dynamic instances; the paper also finds that providing updates alone does not restore static-task performance.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Retrieval & knowledge

### 5. [Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery](https://arxiv.org/abs/2611.17241)
- **Abstract:** Ballad adaptively routes heuristic-search steps among LLMs with non-stationary rewards, reporting that it can match or beat individual models on five combinatorial optimization problems while reducing API cost by up to 65.6% against always using the strongest model.
- **Authors:** Samidha Verma, Ankit Anand, Sayan Ranu
- **arXiv:** `2611.17241v1` (published 2026-11-12 18:28:08 UTC; categories: `cs.AI`)
- **Evidence for ranking:** It has a [NeurIPS 2026 poster listing](https://neurips.cc/virtual/2026/poster/154569) and multiple technical write-ups, including [Agentic Design](https://agentic-design.ai/news-hub/ballad-bandit-based-llm-routing-automated-heuristic-discovery-521130) and [CASRAI](https://casrai.org/news/ballad-bandit-llm-routing-automated-heuristic-discovery-2026). The venue and external discussion, rather than citation counts, inform placement.
- **Claimed contribution:** The authors combine online model selection, lineage-aware credit propagation, and discounting of stale outcomes to handle changing utility during heuristic evolution.
- **Caveat:** The authors' current formulation treats each LLM as a black-box generator with a fixed prompt, leaving model-specific prompting, mutation operators, and context representations untested.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Agents & reasoning; Efficient inference & systems; Training & adaptation

### 6. [Classical Energies Learn to Reason 1,000x Faster than Looped Models](https://arxiv.org/abs/2611.17309)
- **Abstract:** The authors train a Hopfield–Tank-style energy model, CRAM, for Sudoku and maze reasoning and report very fast puzzle training and substantially fewer inference FLOPs than looped-model baselines on those tasks.
- **Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- **arXiv:** `2611.17309v1` (published 2026-11-12 18:56:56 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The paper is cross-listed in AI and ML and has generated separate technical discussion, including [Ken Ashe's analysis](https://kenashe.ai/blog/2026-11-13-cram-makes-sudoku-reasoning-look-too-easy/) and a public [CRAM implementation](https://github.com/Prefrontal-AI/CRAM). These make the method and its caveat independently inspectable.
- **Claimed contribution:** The authors introduce CRAM and report at least 1,000× faster training than the compared looped models on Sudoku-Extreme and Maze-Unique, plus at least 282× fewer inference FLOPs at matched Sudoku accuracy.
- **Caveat:** The authors explicitly caution that Sudoku and Maze are trivially solvable benchmarks and should not be used alone to assess the scalability of looped reasoning; results on these tasks do not establish general reasoning gains.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

### 7. [When Expert Disagreement Hurts: Prestige and Selectivity in LLM Decision Revision](https://arxiv.org/abs/2611.16694)
- **Abstract:** In a controlled revision audit, the authors find that expert-attributed disagreement can increase answer reversals without reliably improving accuracy, and that reversal counts alone can misrepresent whether a model corrected an error.
- **Authors:** Yupeng Tang, Mingfeng Lin
- **arXiv:** `2611.16694v1` (published 2026-11-12 12:11:03 UTC; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The arXiv record identifies NeurIPS 2026 acceptance; a matching [NeurIPS poster](https://neurips.cc/virtual/2026/poster/151259), [public code repository](https://github.com/yupengtang/when-expert-disagreement-hurts), and [Hugging Face paper page](https://huggingface.co/papers/2611.16694) corroborate the work and its reproducibility artifacts.
- **Claimed contribution:** The authors propose a paired, two-pass audit and apply it to 1,989 evidence-grounded decisions across medicine, science, and law; they report accuracy losses of up to 16.1 points under expert disagreement.
- **Caveat:** The evidence comes from five models and controlled binary decisions in three professional domains; the paper does not establish how the measured effects generalize to open-ended tasks or other revision protocols.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Evaluation & benchmarks; Safety & alignment; Agents & reasoning

### 8. [Singularity-Bench: Can Agents Build Agents?](https://arxiv.org/abs/2611.16591)
- **Abstract:** Singularity-Bench measures agent-built systems across six AI-development tasks and reports that one tested agent setup matches or exceeds human-built baselines across all six, while the rest show uneven performance.
- **Authors:** Yang Zhou, Krish Agarwal, Zhuoming Chen, Zerui Wang, Zhenyu Zhang, et al.
- **arXiv:** `2611.16591v1` (published 2026-11-12 10:24:51 UTC; categories: `cs.AI`)
- **Evidence for ranking:** The authors provide a detailed [benchmark site](https://infini-ai-lab.github.io/singularity-bench/) and a public [GitHub repository](https://github.com/Infini-AI-Lab/singularity-bench), making its six tasks, baseline choices, and red-team setup checkable. This is a public-artifact signal rather than evidence of readership.
- **Claimed contribution:** The authors introduce six end-to-end tasks and Breakwater, a Harbor extension that blocked every tested attack in their red-team evaluation; their strongest setup's Singularity-Index is 1.25.
- **Caveat:** The authors state that the task scale is smaller than that needed to measure true recursive self-improvement and that even the strongest agent leaves substantial headroom on raw task scores.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Safety & alignment

### 9. [Negative-Only Policy Optimization for One-Sided Verifiable Rewards](https://arxiv.org/abs/2611.17287)
- **Abstract:** NOPO trains from trusted verifier negatives while treating non-falsified outputs as unlabeled, and the authors report improved pass@k across code, logic, and math tasks when full correctness labels are unavailable.
- **Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
- **arXiv:** `2611.17287v1` (published 2026-11-12 18:52:33 UTC; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** The arXiv record marks it as a NeurIPS 2026 Spotlight paper, and the authors provide a [project page](https://xiaobanni.github.io/projects/nopo/) with the method, benchmark tables, and limitations. Its ML-language cross-list and visible evaluation artifacts support the inclusion.
- **Claimed contribution:** The authors combine reference-relative negative suppression with a group-level support weight and report gains over baselines across unit-test, constraint-check, and LLM self-verifiers.
- **Caveat:** NOPO depends on trustworthy negative judgments; the authors note that weak negative-class recall reduces its supervision signal and that suppressing failures alone does not specify where probability mass should move.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Training & adaptation; Evaluation & benchmarks; Safety & alignment

### 10. [Goal Encoding in LLMs](https://arxiv.org/abs/2611.17297)
- **Abstract:** The authors use causal interventions in coding tasks to identify attention-head representations of upcoming sub-goals and propose that models sustain these representations by rereading task context rather than carrying recurrent state.
- **Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, Andy Arditi, Rohit Gandikota, et al.
- **arXiv:** `2611.17297v1` (published 2026-11-12 18:55:06 UTC; categories: `cs.CL`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The paper is cross-listed in three core AI categories and has a [project page](https://goals.baulab.info/) with code and data; its OpenReview record and an independent [CASRAI overview](https://casrai.org/news/goal-encoding-in-llms-interpretability-preprint-2026) provide checkable external context.
- **Claimed contribution:** The authors report causal and transferable sub-goal encodings in sparse attention heads and test a non-recurrent goal-seeking account with targeted interventions.
- **Caveat:** The authors operationalize only pre-commitment, plasticity, and temporal persistence; they leave other goal attributes unresolved, and note that multi-token evaluation partly relies on an LLM judge.
- **Announcement type:** new submission, 2026-11-13 announcement batch
- **Themes:** Interpretability; Agents & reasoning

## Trending Research Themes

- **Agents are being evaluated in less forgiving settings.** AgentSSL studies weakly supervised program search; LiveGeo adds changing external state; Singularity-Bench measures end-to-end system-building; and Goal Encoding probes internal sub-goal representations. Together these papers broaden the unit of evaluation from a single answer to sustained decisions, code, or system behavior.
- **Reliability is shifting from “did it answer?” to “what evidence and control justified the action?”** CapLite constrains writes to user-stated arguments, LiveGeo checks evidence and state freshness, and When Expert Disagreement Hurts separates useful correction from prestige-driven reversal.
- **Training and inference efficiency are being tested through adaptive allocation.** Ballad routes among models as utility changes; CRAM uses energy descent and adaptive stopping on puzzle tasks; NOPO uses negative-only feedback under partial verification. These are distinct mechanisms, not evidence of one settled recipe.
- **Multimodal architecture gets a controlled ablation rather than a bundled-model comparison.** Unbundling Multimodal Vision Encoding isolates visual prior, dedicated vision parameters, and where they enter the model. Its findings remain bounded by the data and backbone scale in the paper.
- **The selected set is concentrated in agentic AI:** 7 of 10 papers have primary category cs.AI; the other three are primary cs.CV, cs.LG, and cs.CL. Core-category appearances also include cs.LG (5), cs.CL (4), and cs.CV (1). This reflects the shortlist and its discovered discussion signals, not the full arXiv corpus.

## Open Problems and Research Directions

- **Author-stated — selecting useful semi-supervised programs:** AgentSSL reports a large gap between the best generated program and the one selected under weak feedback, and its ecology tasks do not beat the supervised AgentSL baseline. Follow-up work could compare active and unsupervised selection under progressively stronger feedback and test whether the same selection method transfers across domains. ([AgentSSL](https://arxiv.org/abs/2611.17323))
- **Author-stated — robust multimodal scaling:** Unbundling leaves MoE backbones, higher-resolution images, video/interleaved data, and recipe-specific data mixtures open. A controlled extension could vary these factors while preserving compute-matched comparisons. ([Unbundling Multimodal Vision Encoding](https://arxiv.org/abs/2611.17334))
- **Author-stated — defense and utility outside simulated suites:** CapLite's zero-attack result is on AgentDojo, while utility is lower than for an undefended agent. Test the policy on broader tool suites and realistic user-confirmation flows, reporting both attack success and task completion. ([CapLite](https://arxiv.org/abs/2611.17115))
- **Evidence-tied synthesis — maintaining decisions as the world changes:** LiveGeo finds large drops under dynamics, including failures after agents have observed relevant updates. A useful next study would separate update discovery, evidence interpretation, and plan revision over longer horizons and more environments. ([LiveGeo](https://arxiv.org/abs/2611.17267))
- **Author-stated — trustworthy one-sided feedback:** NOPO relies on reliable negative labels and does not determine where probability mass should move; its authors suggest testing partial positive signals such as pairwise comparisons or uncertainty filters while preserving robustness. ([NOPO](https://arxiv.org/abs/2611.17287))
- **Author-stated — measuring actual recursive improvement:** Singularity-Bench's tasks are smaller than the compute and time budgets required for true recursive self-improvement. Extend the benchmark toward larger-scale, multi-generation loops and continue auditing reward-hacking defenses. ([Singularity-Bench](https://arxiv.org/abs/2611.16591))

## Takeaway

This batch's strongest recurring signal is a move toward testing agent reliability under partial feedback, changing state, and real tool or system constraints—not just static answer accuracy. The methods and benchmarks are promising but early: coverage is narrow, and several papers explicitly identify gaps between benchmark performance and deployment or broader capability.

## Method and sources

- **Window:** daily; 2026-11-13 through 2026-11-13 (announcement-batch date). The selected arXiv records show first submissions on 2026-11-12. **Snapshot:** 2026-11-16 01:10:09 UTC. The latest category recent pages then showed Fri 13 Nov as the latest batch, so this report uses a prior batch rather than an empty daily report.
- **Corpus query/scope:** core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; selected cross-listed papers only. Recent pages were checked for each category. High-volume listings expose only the first 50 entries by default, so discovery is not exhaustive; all ten retained papers' arXiv abstract pages and version/category metadata were checked.
- **Inference method:** arXiv has no official trending chart. Ordering is inferred from checkable venue records, cross-list relevance, public project/code/benchmark artifacts, and external technical discussion surfaced in web search. No author fame, institution prestige, or unsupported social-media popularity was used. Semantic Scholar citation counts and influential-citation counts could not be obtained for this snapshot; no citation velocity is claimed. The shortlist is best read as notable papers with discoverable momentum signals, not a popularity ranking.
- **arXiv primary sources:** [cs.AI recent](https://arxiv.org/list/cs.AI/recent), [cs.LG recent](https://arxiv.org/list/cs.LG/recent), [stat.ML recent](https://arxiv.org/list/stat.ML/recent), [cs.CL recent](https://arxiv.org/list/cs.CL/recent), [cs.CV recent](https://arxiv.org/list/cs.CV/recent), [cs.RO recent](https://arxiv.org/list/cs.RO/recent), [cs.NE recent](https://arxiv.org/list/cs.NE/recent), [cs.MA recent](https://arxiv.org/list/cs.MA/recent); each paper links to its canonical abstract page above.
- **Corroborating sources:** venue pages, project sites, repositories, and independent technical write-ups linked in the individual evidence fields.
- **Retrieval limitations:** the broad arXiv API query and Semantic Scholar batch lookup were rate-limited (HTTP 429); therefore the full machine-readable candidate pool and citation counts were unavailable. This is why the report discloses a first-50-listing limitation and keeps the ranking explicitly tentative.
