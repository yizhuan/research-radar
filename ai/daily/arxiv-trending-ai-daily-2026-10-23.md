# arXiv AI — latest announcement batch, Friday 23 October 2026

Eight notable recent papers from the core AI categories. The dominant pattern is evidence-aware agent safety: several papers test whether agents verify, recover, or appropriately act on information before consequential actions. Also on the agenda: inference-time compute allocation, embodied evaluation, and dataset-use auditing. arXiv has no official trending chart; this ordering is inferred from weak, mixed signals, and citation evidence is limited for newly announced papers.

## Top papers (ranked)

### 1. [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650)
- **Abstract:** The authors introduce an executable benchmark of paired safe/unsafe tasks across six domains to measure how tool-using agents behave when safety-relevant evidence is omitted and whether they recover it appropriately.
- **Authors:** Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu, et al.
- **arXiv:** `2610.31650v1` (published 2026-10-22T17:57:04Z; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Search surfaced a dedicated secondary overview and an explainer; the paper is also cross-listed in two core AI categories. These are weak attention proxies, not readership metrics.
- **Claimed contribution:** The authors report that omission robustness and useful evidence recovery are distinct: recovery access reduced unsafe execution across the ten evaluated models, while models differed in whether they sought and used the missing facts.
- **Caveat:** Results come from this benchmark’s six domains and evaluated model set; the authors note that the tested model profiles do not establish general deployment behavior.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Safety & alignment; Evaluation & benchmarks; Agents & reasoning

### 2. [AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack](https://arxiv.org/abs/2610.31404)
- **Abstract:** The paper introduces an adaptive-phishing benchmark and attack-generation method to test whether LLM email agents detect persuasive phishing and refrain from complying with malicious requests.
- **Authors:** Justin Tan, Miao Li, Ding Zhao
- **arXiv:** `2610.31404v1` (published 2026-10-22T15:07:49Z; categories: `cs.CR`, `cs.AI`)
- **Evidence for ranking:** Search surfaced an AI-security digest and independent paper summaries; its cross-list connects security and core AI. These are weak attention proxies, not engagement counts.
- **Claimed contribution:** The authors report that agents safe on pre-existing phishing emails can remain vulnerable to adaptive, persuasive attacks; in their nine-agent evaluation, four had detection below 10% and malicious-request compliance above 45%.
- **Caveat:** The authors limit the evaluation to synthetic single-message attacks and selected configurations; scores cover decisions and drafted replies, not externally executed harm.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Safety & alignment; Evaluation & benchmarks; Agents & reasoning

### 3. [When Is a Memory Safe Enough to Act On? Action-Conditioned Verification for Long-Lived Agents](https://arxiv.org/abs/2610.31446)
- **Abstract:** The authors formulate action-conditioned memory verification and propose a gate that decides which remembered facts to re-check, proceed, or abstain on based on the planned action and its consequences.
- **Authors:** Yiqi Wang, Yifei Wang, Jiaqi Zhang, Zhangkai Wu, Yiqun Duan, et al.
- **arXiv:** `2610.31446v1` (published 2026-10-22T15:43:50Z; categories: `cs.MA`)
- **Evidence for ranking:** Search surfaced multiple paper-specific reviews/summaries; the work offers a concrete decision formulation and reports tests on ToolSandbox plus a gate-core transfer to AppWorld.
- **Claimed contribution:** The authors report that AMV-Guard lowers verification cost on ToolSandbox while retaining safe-proceed recall, and lowers cost in a transfer evaluation with a small reduction in recall and task success.
- **Caveat:** The paper explicitly says premise extraction is model-driven, planning is bounded to a shallow lookahead, and the simulators omit some real-world consequences; scalability and broader action-class results remain unreported.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 4. [Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](https://arxiv.org/abs/2610.31667)
- **Abstract:** The paper proposes pruning partial reasoning traces by directly maximizing the chance that at least one retained trace completes correctly, thereby balancing trace quality and diversity.
- **Authors:** Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn
- **arXiv:** `2610.31667v1` (published 2026-10-22T17:59:48Z; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** Several search-indexed technical summaries discuss the method; the paper is cross-listed in AI and language, and reports comparisons across eight open-weight reasoning models. Summary coverage is a weak signal, not a readership count.
- **Claimed contribution:** The authors report that their pass@$k$ objective outperforms the evaluated quality-only and diversity-only pruning baselines, especially when a moderate number of candidates is continued.
- **Caveat:** Evidence is limited to the eight evaluated open-weight models and tested pruning settings; the abstract does not establish gains across all reasoning tasks or inference systems.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Training & adaptation; Efficient inference & systems; Agents & reasoning

### 5. [AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments](https://arxiv.org/abs/2610.31326)
- **Abstract:** The authors replace one-shot evolutionary candidate generation with persistent LLM agents that run experiments between evaluations, reporting improved program-search results on heuristic-design and equation-discovery tasks.
- **Authors:** Ze-Yu Peng, Qing-Yu Lan, Zhan-He Wang, Jun Zhang, Yun-Song Piao
- **arXiv:** `2610.31326v1` (published 2026-10-22T14:18:21Z; categories: `cs.NE`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Search surfaced paper-specific summaries; it spans three core AI categories and directly compares the agent’s experimentation loop with an otherwise matched no-analysis configuration.
- **Claimed contribution:** The authors report better programs than No-analysis and OpenEvolve on two heuristic tasks, reaching baseline quality with fewer evaluations, and recovering more ground-truth structures on twelve equation-discovery problems.
- **Caveat:** The reported evidence is confined to the described heuristic and equation-discovery suites and three LLMs; broader scientific-search performance is not established.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 6. [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670)
- **Abstract:** The authors introduce a training-free representation-alignment metric and report that it correlates with downstream robot task success, proposing it as a low-cost filter before closed-loop evaluation.
- **Authors:** Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
- **arXiv:** `2610.31670v1` (published 2026-10-22T17:59:51Z; categories: `cs.CV`, `cs.LG`, `cs.RO`)
- **Evidence for ranking:** It is cross-listed across three core categories spanning vision, learning, and robotics, and addresses a practical evaluation-cost bottleneck; no secondary source is used as an attention signal here.
- **Claimed contribution:** The authors claim that sensorimotor alignment can prioritize embodied models and VLM backbones before costly closed-loop rollouts or VLA fine-tuning.
- **Caveat:** The abstract reports correlation, not a causal guarantee or replacement for closed-loop testing; model selection still requires downstream validation.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Robotics & control; Multimodal & vision-language; Evaluation & benchmarks

### 7. [SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing](https://arxiv.org/abs/2610.31659)
- **Abstract:** The authors embed a low-frequency image trace throughout a dataset and detect it in generated outputs to audit whether a text-to-image model used that collection for fine-tuning.
- **Authors:** Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe, Huy Nghiem, Yongkyun Lee, et al.
- **arXiv:** `2610.31659v1` (published 2026-10-22T17:59:03Z; categories: `cs.CV`, `cs.LG`)
- **Evidence for ranking:** The paper is cross-listed in vision and learning and reports multi-dataset and multi-transformation tests; no secondary source is used as an attention signal here.
- **Claimed contribution:** The authors report high detection rates under their evaluated transformations and datasets while preserving image similarity, with removal under their strongest tested adaptive attack causing substantial FID degradation.
- **Caveat:** The reported robustness is bounded by the tested datasets, architectures, and adaptive attacks; it does not establish performance against every possible transformation or removal strategy.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Data & synthetic data; Evaluation & benchmarks; Safety & alignment

### 8. [What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models](https://arxiv.org/abs/2610.31576)
- **Abstract:** The authors study learned token-commitment policies for masked diffusion language models and propose trajectory-contraction targets that trade policy overhead against generation speed and accuracy.
- **Authors:** Jinya Sakurai, Xun Xu, Jaehong Yoon
- **arXiv:** `2610.31576v1` (published 2026-10-22T17:15:04Z; categories: `cs.AI`)
- **Evidence for ranking:** The study compares teacher labels, policy inputs, and overhead, and reports results on GSM8K, MATH-500, and HumanEval; no secondary source is used as an attention signal here.
- **Claimed contribution:** The authors report an improved accuracy–NFE frontier and throughput on GSM8K for their policy, with competitive results at moderate targets on MATH-500 and HumanEval and transfer to Dream-7B-Instruct.
- **Caveat:** The main reported result is on LLaDA-8B-Instruct, with transfer evidence to one additional model; the abstract does not establish broad model-family generality.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Efficient inference & systems; Training & adaptation

## Trending Research Themes

- **Evidence-aware agent safety is the clearest recurring pattern.** EpiSEM-Bench tests missing evidence and recovery; AgentPhishing tests whether agents comply with adaptive malicious requests; and action-conditioned memory verification asks when stored facts need re-checking before an action. Together these papers emphasize behavior at the point of action, not just answer accuracy or static threat recognition.
- **Inference-time compute is being allocated more selectively.** Direct Pass@$k$ prunes redundant reasoning continuations, while the diffusion-language-model study learns when to commit predicted tokens. These are distinct mechanisms, but both make quality-versus-compute trade-offs explicit.
- **LLM agents as experimental operators are an isolated signal, not yet a corpus-wide shift.** AgenticEvolve lets persistent agents design and run experiments inside evolutionary program search; its results are promising within the paper’s limited task suites.
- **Embodied representation metrics and training-data auditing are additional, separate directions.** Sensorimotor Alignment proposes a cheaper proxy before robot rollouts; SpectralCanary audits possible use of image collections in T2I fine-tuning. Each is a single-paper signal in this selected set, not evidence of a recurring trend.
- **The candidate pool is category-skewed.** Among the 449 records with 2026-10-22 arXiv publication dates in the core-category query, primary categories were led by cs.CV (91), cs.LG (88), cs.AI (83), cs.CL (61), and cs.RO (52); cs.MA and cs.NE had two each. Counts are primary-category counts, not a popularity measure.

## Open Problems and Research Directions

- **Author-stated — adaptive agent security:** AgentPhishing identifies limits from single-message synthetic attacks, selected model configurations, scoring based on decisions/drafted replies, and model-version dependence. A follow-up could test multi-turn tool interactions and defensive interventions in a sandbox with explicit outcome and side-effect tracking. [AgentPhishing](https://arxiv.org/abs/2610.31404)
- **Author-stated — memory verification coverage:** The memory-verification paper says model-driven premise extraction caps recall, its planner uses bounded lookahead, modeled harms omit some downstream consequences, and scalability/action-class breakdowns remain open. Evaluate premise-recall ceilings, longer verification sequences, and consequence-aware outcomes across broader environments. [When Is a Memory Safe Enough to Act On?](https://arxiv.org/abs/2610.31446)
- **Synthesis — combine failure modes:** EpiSEM-Bench, AgentPhishing, and action-conditioned memory verification study missing evidence, adversarial content, and stale memory separately. A controlled factorial evaluation could combine these factors and test when agents should verify, recover, refuse, or proceed, while measuring both safety and legitimate task completion. [EpiSEM-Bench](https://arxiv.org/abs/2610.31650), [AgentPhishing](https://arxiv.org/abs/2610.31404), [memory verification](https://arxiv.org/abs/2610.31446)
- **Synthesis — compare compute allocation under matched budgets:** Direct Pass@$k$ and learned diffusion unmasking use different decoding mechanisms. Compare them under matched compute, latency, and task-quality budgets, including robustness across model families and tasks. [Direct Pass@$k$](https://arxiv.org/abs/2610.31667), [learned unmasking](https://arxiv.org/abs/2610.31576)
- **Author-stated scope / synthesis — generalize agentic search:** AgenticEvolve reports two heuristic-design tasks and twelve equation-discovery problems. Replications on held-out scientific and engineering tasks, with explicit evaluation-cost and reproducibility controls, would test how far its experimentation loop transfers. [AgenticEvolve](https://arxiv.org/abs/2610.31326)

## Takeaway

This batch’s strongest common thread is reliable agent action under uncertainty: agents need to seek or verify evidence, distinguish permitted from prohibited actions, and resist persuasive attacks. The methods are promising but early; the batch is too recent and the attention signals too sparse to justify a confident popularity ranking or broad claims of field-wide change.

## Method and sources

- **Window:** Daily; selected announcement batch 2026-10-23 (Friday), the most recent batch available on Saturday 2026-10-24. No newer batch was listed on the core-category recent pages. The batch covers papers first posted 2026-10-22 UTC; the requested announcement-date range is 2026-10-23 through 2026-10-23. Snapshot: 2026-10-24 16:05:09 UTC.
- **Scope/query:** Core corpus `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`, plus cross-listed papers with those categories. Exact query: `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`. A single broad arXiv API query returned 1,000 records; 449 had first-publication dates on 2026-10-22 and all eight configured categories were represented. All eight selected records are v1 first submissions; no selected item is a revision. Each selected abstract page was checked directly on arXiv. arXiv’s recent-page batch labels were used to map the 2026-10-22 submissions to the 2026-10-23 announcement batch.
- **Inference:** arXiv provides no trending/readership ranking. Selection and ordering are an inferred “notable recent papers” list, using weak, checkable secondary coverage where found, cross-category relevance, and the concrete evaluation or methodological evidence described in the abstracts/papers. Searches did not find outside coverage for every item. Semantic Scholar Graph API was checked for all eight papers at snapshot time: citationCount and influentialCitationCount were both 0 for each. These are current totals, not citations gained during this window; the papers’ newness makes citation evidence uninformative.
- **arXiv sources:** [cs.AI recent](https://arxiv.org/list/cs.AI/recent), [cs.LG recent](https://arxiv.org/list/cs.LG/recent), [stat.ML recent](https://arxiv.org/list/stat.ML/recent), [cs.CL recent](https://arxiv.org/list/cs.CL/recent), [cs.CV recent](https://arxiv.org/list/cs.CV/recent), [cs.RO recent](https://arxiv.org/list/cs.RO/recent), [cs.NE recent](https://arxiv.org/list/cs.NE/recent), [cs.MA recent](https://arxiv.org/list/cs.MA/recent), [availability and announcement schedule](https://info.arxiv.org/help/availability.html), and the [arXiv API query](https://export.arxiv.org/api/query?search_query=cat%3Acs.AI%2BOR%2Bcat%3Acs.LG%2BOR%2Bcat%3Astat.ML%2BOR%2Bcat%3Acs.CL%2BOR%2Bcat%3Acs.CV%2BOR%2Bcat%3Acs.RO%2BOR%2Bcat%3Acs.NE%2BOR%2Bcat%3Acs.MA&sortBy=submittedDate&sortOrder=descending&start=0&max_results=1000).
- **Corroborating coverage checked:** [EpiSEM-Bench overview](https://agentic-design.ai/news-hub/episem-bench-evaluating-safety-evidence-recovery-llm-agents-under-missing-704dd5) and its [video explainer](https://www.youtube.com/watch?v=z53JX1Ul6V0); [AgentPhishing security digest](https://deniskim1.com/writing/ai_security_digest__october_24_2026_ai_agents__vulnerabiliti/) and [paper summary](https://www.aimodels.fyi/papers/arxiv/agentphishing-benchmark-llm-email-agents-under-adaptive); [memory-verification review](https://www.aimodels.fyi/papers/arxiv/when-is-memory-safe-enough-act-action) and [independent review](https://www.themoonlight.io/es/review/when-is-a-memory-safe-enough-to-act-on-action-conditioned-verification-for-long-lived-agents); [Direct Pass@$k$ summaries](https://www.wovepaper.com/papers/2610.31667-direct-pass-k-optimization-for-thought-pruning-balancing-quality-and-diversity) and [technical overview](https://book.st-hakky.com/en/news/direct-pass-k-optimization-for-thought-pruning); [AgenticEvolve summary](https://arxivsignals.io/papers/2610.31326). These are secondary summaries, not readership statistics.
