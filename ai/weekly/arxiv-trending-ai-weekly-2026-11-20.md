# arXiv AI weekly: 7 notable papers from 14–20 November 2026

Core AI categories; latest announcement batch represented in the candidate pool: 19 November 2026. The recurring pattern is agents being improved and judged through their surrounding systems—search procedures, harnesses, simulators, and controlled evaluation. This week’s quick tour: learned exploration for LLM reasoning, self-modifying agent infrastructure, medical vision harnesses, and world models that test counterfactuals. arXiv has no official trending chart: this is an inferred ordering, and citation evidence for very recent work is limited.

## Top papers (ranked)

### 1. [MCTS Is Counting the Wrong Thing: Learning Exploration Counts for LLM Reasoning](https://arxiv.org/abs/2611.22301)
- **Abstract:** The paper studies why standard MCTS can waste exploration across textually different but strategically similar reasoning branches, and proposes a learned count that shares evidence across related branches.
- **Authors:** Xuan Zhang, Zhijian Zhou, Zicheng Hu, Yan Feng, Hongyan Hao, et al.
- **arXiv:** `2611.22301v1` (published 2026-11-17T06:57:40Z; categories: `cs.AI`)
- **Evidence for ranking:** Several separate technical explainers/reviews appeared in search, including [AI Data Base](https://ai-data-base.com/paper/2611-22301), [Moonlight](https://www.themoonlight.io/de/review/mcts-is-counting-the-wrong-thing-learning-exploration-counts-for-llm-reasoning), and [OpenTrain AI](https://www.opentrain.ai/papers/mcts-is-counting-the-wrong-thing-learning-exploration-counts-for-llm-reasoning--arxiv-2611.22301/); the paper also reports theoretical analysis and results across mathematical-reasoning and search benchmarks.
- **Claimed contribution:** The authors introduce Learned Pseudo-Count MCTS (LPC-MCTS), which estimates representation coverage with a lightweight Coin-Flipping Network and replaces exact UCT visit counts; they report gains over standard MCTS on five math and seven search benchmarks.
- **Caveat:** The reported evaluation is limited to those benchmark families and model configurations; transfer to broader, open-ended reasoning remains unestablished.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 2. [Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses](https://arxiv.org/abs/2611.22299)
- **Abstract:** The paper frames an agent’s runtime harness as an editable part of the system and proposes a modular loop for diagnosing failures, changing harness code, validating changes, and deploying them.
- **Authors:** Deep Shah, Nehal Kathrotia
- **arXiv:** `2611.22299v1` (published 2026-11-17T06:55:41Z; categories: `cs.AI`)
- **Evidence for ranking:** The topic received multiple independent technical write-ups, including [paper notes](https://mahmadmanzoor.com/blog/self-improving-agent-harnesses-paper-notes) and a [DEV Community discussion](https://dev.to/ahmad_dogar_7d098f5e48f72/harnesses-that-improve-themselves-how-an-agent-can-rewrite-its-own-runtime-without-breaking-it-1p2i); the paper gives a concrete held-out SWE-bench Lite comparison rather than only a conceptual framework.
- **Claimed contribution:** The authors organize self-improving harnesses into four runtime components and a diagnose–patch–validate–deploy loop, and report that gated modular evolution beats prompt-only reflection and ungated full rewrites on their SWE-bench Lite setup at lower token cost.
- **Caveat:** The paper’s own experiments cover 60 Python bug-fixing tasks across two repositories, so the measured performance does not establish that the framework transfers to non-coding agents or long-term deployment.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 3. [Groups of AI agents underuse resources despite shared evidence of increased capacity](https://arxiv.org/abs/2611.22632)
- **Abstract:** In controlled two-server simulations, the authors find that groups of language-model agents can leave capacity unused even after sharing evidence that a server has recovered, and test simple ways to spread requests.
- **Authors:** Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari
- **arXiv:** `2611.22632v1` (published 2026-11-17T11:50:26Z; categories: `cs.MA`)
- **Evidence for ranking:** Several third-party summaries surfaced, including [AI Models](https://www.aimodels.fyi/papers/arxiv/groups-ai-agents-underuse-resources-despite-shared), [Moonlight](https://www.themoonlight.io/fr/review/groups-of-ai-agents-underuse-resources-despite-shared-evidence-of-increased-capacity), and [ModelScope](https://www.modelscope.cn/papers/2611.22632); the paper reports controlled comparisons across multiple language models and a concrete group-level efficiency measure.
- **Claimed contribution:** The authors report that successful-request records help agents use a recovered server, while giving agents distinct numeric labels reduces synchronized demand and increases completed jobs in their simulated setting.
- **Caveat:** The evidence comes from a controlled two-server simulation with a specific recovery and retry setup; it does not yet show that the intervention works in deployed, heterogeneous infrastructure.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 4. [Visual Harness Scales General VLMs to Medical Images](https://arxiv.org/abs/2611.22815)
- **Abstract:** The paper presents a medical-image harness that lets general vision-language models inspect images iteratively, preserve evidence, check for omissions, and revise answers across multiple tasks and imaging modalities.
- **Authors:** Shaowen Wan, Hanqi Jiang, Zihao Wu, Junhao Chen, Weihang You, et al.
- **arXiv:** `2611.22815v2` (published 2026-11-18T03:49:41Z; categories: `cs.CV`)
- **Evidence for ranking:** The v2 revision landed during this week’s window, and a separate [AIDB technical overview](https://ai-data-base.com/paper/2611-22815) appeared; the paper reports evaluation on 11 tasks spanning four modalities, making its system-level results checkable across more than one narrow task.
- **Claimed contribution:** The authors’ VERA harness combines interactive visual tools, lossless evidence memory, an evidence map and verifier, and an iterative inspection loop; they report improvement on all 11 tasks for Qwen3.8-27B.
- **Caveat:** The authors state that evaluation uses public datasets, excludes real-world clinical validation, and uses smaller subsets for some API-model comparisons because of cost; they also cannot rule out training-data overlap for proprietary models.
- **Announcement type:** revision, 2026-11-18 announcement batch (v1 submitted 2026-11-17)
- **Themes:** Multimodal & vision-language; Agents & reasoning; Evaluation & benchmarks

### 5. [Counterfactual World Models: JEPAs That Reason About "What If"](https://arxiv.org/abs/2611.24778)
- **Abstract:** The authors study counterfactual action outcomes under hidden disturbances and derive a first-order correction that reuses factual transitions to estimate what an alternative action would have done.
- **Authors:** Randall Balestriero, Yann LeCun, Kerda Varaku
- **arXiv:** `2611.24778v1` (published 2026-11-18T17:24:00Z; categories: `cs.LG`, `cs.AI`, `cs.CV`, `cs.RO`, `stat.ML`)
- **Evidence for ranking:** The paper received several distinct technical summaries, including [Emergent Mind](https://www.emergentmind.com/papers/2611.24778) and [OpenTrain AI](https://www.opentrain.ai/papers/counterfactual-world-models-jepas-that-reason-about-what-if--arxiv-2611.24778/); its abstract reports formal error bounds and tests across multiple simulators and frozen encoders.
- **Claimed contribution:** The authors derive an action-difference correction for JEPA world models under separated action and disturbance forces, prove an `O(h^2)` error bound under their assumptions, and report higher counterfactual prediction accuracy in their simulator experiments.
- **Caveat:** The authors identify failure cases at discontinuities, coordinate folds, and when disturbances scale the command; the reported experiments do not remove those assumption boundaries.
- **Announcement type:** new submission, 2026-11-18 announcement batch
- **Themes:** Robotics & control; Multimodal & vision-language

### 6. [Openhagen Worlds: Calibrated Environments for Measuring and Training Scientific Discovery Agents](https://arxiv.org/abs/2611.24711)
- **Abstract:** The paper introduces procedurally generated scientific-discovery environments with explicit scoring rules, hidden truths, budgeted experiments, and deterministic answer verification.
- **Authors:** Alexander Boesgaard Lorup
- **arXiv:** `2611.24711v1` (published 2026-11-18T16:36:18Z; categories: `cs.LG`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** A [public evaluation service](https://eval.openhagen.ai/) and a [Pith paper listing](https://pith.science/paper/2611.24711) provide checkable external artifacts; the work’s 27 environment families and 178 calibrated levels give it unusually concrete evaluation scope among this week’s agent papers, while independent discussion signals were thinner than for higher-ranked entries.
- **Claimed contribution:** The authors contribute 27 environment families and 178 calibrated difficulty levels, with hidden-answer verification and controlled development/frontier splits; on 84 withheld frontier instances, the reported strongest model still trails the oracle.
- **Caveat:** These are procedurally generated benchmark environments, not evidence of improved performance in live scientific research; the paper reports that the largest remaining gap is in long campaigns of eight or more stages.
- **Announcement type:** new submission, 2026-11-18 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 7. [Do Frontier Model Ingredients Add Up? A Replicated Factorial Study of Small Language Models](https://arxiv.org/abs/2611.24540)
- **Abstract:** The authors compare combinations of five language-model design and training changes under a shared data and compute budget, repeating selected runs with a second random seed.
- **Authors:** Biswa Sengupta
- **arXiv:** `2611.24540v1` (published 2026-11-18T14:48:52Z; categories: `cs.CL`, `cs.AI`)
- **Evidence for ranking:** Two separate summaries surfaced, [SyncAI News](https://syncai.news/article/do-frontier-model-ingredients-add-up-a-replicated-factorial-study-of-small-langu-116b8f) and [Papers.cool](https://papers.cool/arxiv/2611.24540), alongside a controlled component-combination study; the independent attention trail was thinner than for the higher-ranked agent papers.
- **Claimed contribution:** The authors report that mixture-of-experts layers, Muon optimization, and a Gated DeltaNet hybrid produced the largest gains in their small-model setting, while most tested gains combined and some interactions persisted across two seeds.
- **Caveat:** The authors limit the conclusion to their small-model training setup and note that the expert models have greater total capacity; two seeds do not establish broad robustness of component rankings.
- **Announcement type:** new submission, 2026-11-18 announcement batch
- **Themes:** Training & adaptation

## Trending Research Themes

- **Agent capability is increasingly treated as a system property.** The self-improving harness framework changes the runtime around the model; VERA adds evidence-management tools to a medical VLM; and the multi-agent resource study shows that shared information alone does not ensure efficient group behavior. These are distinct settings, but together they shift attention from model weights alone to control, verification, and coordination.
- **Evaluation design is a recurring contribution, not just a reporting detail.** Openhagen Worlds calibrates hidden-answer environments; VERA tests across 11 tasks and four modalities; the resource-allocation paper varies what evidence and identifiers agents receive; and the harness paper separates development, validation, and held-out repositories. MCTS also reports math and search benchmarks. The common method is to expose failure modes through controlled tests, not a demonstrated general solution to them.
- **Search and exploration are being made representation-aware.** LPC-MCTS shares exploration evidence across similar reasoning branches rather than counting distinct text paths. This is a specific algorithmic proposal in one paper, not evidence that the broader field has converged on learned pseudo-counts.
- **Counterfactual prediction in world models is a focused signal.** The JEPA paper derives a reuse-based correction for hidden disturbances and tests it in simulators; this is notable but isolated in this selected set, so it does not establish a broader weekly shift toward counterfactual world modeling.
- **Small-model recipes are being tested compositionally.** The factorial study compares combinations under a shared budget and repeats selected runs, suggesting that interaction and replication deserve attention when combining published improvements; its conclusions remain bounded to the reported model scale and seed count.

## Open Problems and Research Directions

- **Author-stated—self-modifying harnesses:** the harness paper details risks including benchmark gaming, evaluator/log tampering, prompt bloat, and unsafe persistent memory. Follow-up evaluations should use immutable grading and audit logs, strict permission boundaries, contamination-resistant held-out tasks, and compute-matched tests across model families. [Harnesses That Improve Themselves](https://arxiv.org/abs/2611.22299)
- **Author-stated—clinical validity:** VERA’s authors report no real-world clinical evaluation and note possible proprietary-model data overlap. A next step is prospective testing on external, institutionally distinct data with clinician-reviewed outcomes and complete accounting of tool/API cost. [Visual Harness](https://arxiv.org/abs/2611.22815)
- **Author-stated—long-horizon discovery:** Openhagen Worlds reports the greatest remaining headroom in campaigns with eight or more committed stages, while expert iteration gives modest gains. Test whether training improvements persist on longer hidden-system campaigns and separate scientific inference gains from better action formatting. [Openhagen Worlds](https://arxiv.org/abs/2611.24711)
- **Author-stated—counterfactual boundary cases:** the JEPA analysis identifies discontinuities, coordinate folds, and command-scaled disturbances as failure conditions. Experiments that vary these conditions systematically, then test the correction on physical rather than only rendered environments, would clarify its practical range. [Counterfactual World Models](https://arxiv.org/abs/2611.24778)
- **Synthesis—coordination under changing capacity:** the two-server study leaves open whether request de-synchronization survives heterogeneous resources and real queue dynamics. A useful follow-up is a controlled scheduler benchmark with capacity changes, delays, and failure recovery, comparing identity randomization with explicit coordination protocols. [Groups of AI agents](https://arxiv.org/abs/2611.22632)
- **Author-stated—robust component effects:** the factorial study says its conclusions apply to a small-model setting and repeats selected conditions with a second seed. Larger seed counts and capacity-matched MoE comparisons would test whether the reported interactions and rankings persist. [Do Frontier Model Ingredients Add Up?](https://arxiv.org/abs/2611.24540)

## Takeaway

This week’s strongest recurring signal is engineering the conditions under which agents act: search statistics, self-editing runtimes, visual evidence tools, and calibrated environments. The results are promising but remain preprints with bounded benchmarks; clinical and real-world transfer, long-horizon behavior, and reproducibility across model scales remain open.

## Method and sources

- **Window:** 2026-11-14 through 2026-11-20 inclusive; first submissions or material revisions announced in this seven-calendar-day window. **Snapshot:** 2026-11-20 02:16:27 UTC. Latest candidate announcement batch in the collected pool: 2026-11-19.
- **Scope/query:** core AI categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`; one broad arXiv API category query sorted by submission date, paginated to its reported 2,791 results, then filtered to 2,385 records with first-submission dates inside the window. arXiv abstract pages were verified for all seven selected IDs; the three highest-ranked papers were also read in arXiv HTML through their introductions, reported results, and limitations/discussion.
- **Ranking method:** a qualitative ordering based first on independently hosted technical discussion located by web search, then on corroborating evidence such as breadth of evaluation, formal analysis, a substantive revision, and concrete external evaluation artifacts. No downloads, views, or unsupported social-media signals were used, and no composite numeric score was assigned. Semantic Scholar Graph coverage was incomplete: only one queried record returned (2611.24540, zero citations and 24 references), so citation counts were not used as a cross-paper ranking signal. The `web_extract` backend could not extract pages in this environment; arXiv HTML/API and indexed external sources were used instead. The arXiv `lastUpdatedDate` query was rate-limited, so revisions of papers first submitted before the window may be absent; the report includes the in-window v2 update for 2611.22815.
- **Primary sources:** arXiv abstract pages: [2611.22301](https://arxiv.org/abs/2611.22301), [2611.22299](https://arxiv.org/abs/2611.22299), [2611.22632](https://arxiv.org/abs/2611.22632), [2611.22815](https://arxiv.org/abs/2611.22815), [2611.24778](https://arxiv.org/abs/2611.24778), [2611.24711](https://arxiv.org/abs/2611.24711), [2611.24540](https://arxiv.org/abs/2611.24540). External discussion and evaluation references are linked in each entry.
