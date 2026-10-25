# arXiv Trending AI — Friday, 23 October 2026

## Headline

AI categories, Friday’s 23 October announcement batch; five selected papers. The clearest pattern is agent reliability engineering: papers test whether agents recover missing evidence, preserve research integrity, or safely route work and oversight; a second strand trims reasoning compute. Spoken agenda: first safety and auditing, then efficient reasoning and runtime agent control, followed by unresolved evaluation questions. This is an inferred, curated ranking—not an official arXiv trending chart—and recent-paper citation evidence is limited, so “hottest” should not be read as a measured popularity claim. Because this snapshot is Sunday, 25 October, it uses the previous announcement batch (Friday, 23 October).

## Top papers (ranked)

### 1. [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650)
- **Abstract:** The authors introduce a benchmark of 300 matched safe/unsafe task pairs across six domains to test whether tool-using agents act safely when critical facts are omitted and whether they retrieve and use those facts appropriately.
- **Authors:** Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu et al.
- **arXiv:** `2610.31650v1` (published 2026-10-22 17:57:04 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The specific missing-evidence safety failure mode received secondary coverage in [an editorial explainer](https://agentic-design.ai/zh/news-hub/episem-bench-evaluating-safety-evidence-recovery-llm-agents-under-missing-704dd5) and [a research explainer](https://franklineh.com/learn/research/editorial-research-6b25a9795491abc6caed2f3643efc907). Its matched-world protocol and ten-model evaluation also make the result particularly relevant to agent safety and evaluation; these are relevance signals, not readership statistics.
- **Claimed contribution:** The paper claims EpiSEM-Bench separates unsafe execution, safety boundaries, and evidence recovery; its ten-model study finds that robustness to omissions does not by itself imply useful recovery.
- **Caveat:** The evidence is from a bounded benchmark (300 task pairs, six domains, ten model configurations, and a fixed evaluation protocol); transfer to other tools, tasks, and deployments remains to be established.
- **Announcement type:** new submission, 23 October 2026 announcement batch
- **Themes:** Safety & alignment; Evaluation & benchmarks; Agents & reasoning

### 2. [Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](https://arxiv.org/abs/2610.31667)
- **Abstract:** The authors propose selecting partial reasoning traces by directly optimizing the probability that at least one retained trace finishes correctly, balancing quality and diversity to reduce the cost of test-time scaling.
- **Authors:** Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn
- **arXiv:** `2610.31667v1` (published 2026-10-22 17:59:48 UTC; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The paper has a [technical summary listing](https://arxivtldr.org/abs/2610.31667), and reports comparisons on eight open-weight reasoning models, with the largest gains at moderate retained-pool sizes. That combination supports relevance to the current inference-compute question, but is not evidence of broad popularity.
- **Claimed contribution:** The authors’ PKTP method models correlated rollout outcomes, uses a second-order submodular approximation to pass@$k$, and greedily produces nested candidate sets; their experiments report improvements over quality-only and diversity-only pruning baselines.
- **Caveat:** The approach depends on a latent-Gaussian model of correlated rollout success and on information in partial-trace representations; the authors identify stronger representations as a direct future-work need.
- **Announcement type:** new submission, 23 October 2026 announcement batch
- **Themes:** Training & adaptation; Efficient inference & systems; Evaluation & benchmarks

### 3. [Reliable AI-Assisted Decisions via Selective Auditing](https://arxiv.org/abs/2610.31662)
- **Abstract:** This paper formulates online AI decision review as constrained optimization and presents auditing policies intended to limit the share of AI errors that escape expert review while minimizing how often review is needed.
- **Authors:** Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani, Tijana Zrnic
- **arXiv:** `2610.31662v1` (published 2026-10-22 17:59:22 UTC; categories: `stat.ML`, `cs.LG`, `stat.ME`)
- **Evidence for ranking:** The work is surfaced in a [Berkeley-hosted manuscript](https://www.stat.berkeley.edu/~ryantibs/papers/selectaudit.pdf) and a [BU CISE research profile](https://www.bu.edu/cise/tijana-zrnic/). Its provable error-control framing and evaluations in safety screening, qualitative annotation, and data labeling make it a strong reliability contribution; these institutional pages establish discoverability, not independent popularity.
- **Claimed contribution:** The authors derive online error-control methods, including one they characterize as asymptotically optimally efficient for adversarial and i.i.d. streams, and report lower auditing effort than baselines on three task types.
- **Caveat:** The discussion assumes auditors are correct and audits have equal cost; the authors leave noisy auditors and heterogeneous audit costs as future extensions. Their appendix also cautions that a capped variant can weaken error control when errors are rare.
- **Announcement type:** new submission, 23 October 2026 announcement batch
- **Themes:** Safety & alignment; Evaluation & benchmarks; Agents & reasoning

### 4. [RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention](https://arxiv.org/abs/2610.31372)
- **Abstract:** RIDAR combines a taxonomy of research-integrity violations, post-hoc trajectory detection, and runtime intervention; the authors report 85.2% F1 on a 60-trajectory annotated benchmark and 36.8% fewer violations remaining at task completion in their runtime evaluation.
- **Authors:** Jiening Siow, Amy Xin, Junjie Wang, Ziyu Tang, Zijun Yao et al.
- **arXiv:** `2610.31372v1` (published 2026-10-22 14:43:36 UTC; categories: `cs.AI`)
- **Evidence for ranking:** A [Hugging Face Papers listing](https://huggingface.co/papers/2610.31372), a [secondary research digest](https://cctest.ai/en/articles/ridar-builds-a-research-integrity-layer-for-autonomous-agents), and the [authors’ code repository](https://github.com/THU-KEG/RIDAR) surfaced for the paper. The 14-type taxonomy and results on RIV-Gold/RIV-Wild give it clear relevance to autonomous-research reliability; repository availability is a reproducibility signal, not an attention count.
- **Claimed contribution:** The authors claim a full-lifecycle taxonomy and paired post-hoc/runtime monitoring framework, reporting 3,964 detected violations across 300 trajectories and a reduction in remaining violations after runtime intervention.
- **Caveat:** The reported detection and intervention results are tied to the paper’s expert-labeled set and collected trajectories; performance on other agent architectures and independently generated research workflows is not established here.
- **Announcement type:** new submission, 23 October 2026 announcement batch
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 5. [Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery](https://arxiv.org/abs/2610.31461)
- **Abstract:** The authors treat skill granularity as a runtime control decision, routing coding agents among primitive actions, macro skills, and macro-to-micro recovery when a macro fails.
- **Authors:** Dingxuan Zhang, Yanhui Jiang, Jun Wang, Hefeng Zhou
- **arXiv:** `2610.31461v1` (published 2026-10-22 15:55:18 UTC; categories: `cs.AI`, `cs.SE`)
- **Evidence for ranking:** The runtime recovery idea received secondary coverage in [Nowness AI](https://nownessai.com/f/arxiv-2610-31461) and [AI Pulse](https://www.aipulsenews.co/article/arxiv-ai-1792728000000-di37bu). The paper’s verifier-defined task success and controlled failure-recovery experiments make it a concrete agent-systems contribution; its small pilot limits the strength of any broader trend claim.
- **Claimed contribution:** The authors report that runtime routing and explicit macro-to-micro recovery improve robustness over fixed-granularity execution in their deterministic coding-agent protocol, while selective recovery avoids some unnecessary costs.
- **Caveat:** The evaluation uses a small set of mixed coding tasks and controlled injected failures, with a few hand-written macros; the authors explicitly call for broader tasks, repositories, failure modes, and models.
- **Announcement type:** new submission, 23 October 2026 announcement batch
- **Themes:** Agents & reasoning; Efficient inference & systems; Evaluation & benchmarks

## Trending Research Themes

- **Agent safety is being reframed as evidence handling and intervention, not just policy compliance.** EpiSEM-Bench tests omitted facts and recovery; RIDAR detects and intervenes on research-integrity violations; selective auditing gives a formal mechanism for escalating uncertain decisions. These are related reliability threads, not a single shared method.
- **Evaluation is becoming more diagnostic.** EpiSEM-Bench distinguishes unsafe action from appropriate recovery; RIDAR separates detection from runtime correction; selective auditing measures the trade-off between caught errors and review load. The recurring shift is toward outcome decomposition and process-level controls.
- **Compute and execution control are moving closer to the decision loop.** PKTP prunes reasoning traces by an estimated pass@$k$ objective, while Adaptive Skill Granularity selects action abstraction and fallback based on runtime state. Both frame resource use as a control problem, but one operates during inference and the other over tool execution.
- **Corpus coverage is broad but uneven.** In the 449 records returned for the announcement-day query, the configured categories appear with overlapping tags: cs.AI 169, cs.LG 151, cs.CV 101, cs.CL 89, cs.RO 57, stat.ML 20, cs.MA 15, and cs.NE 2. These are not exclusive counts. The five selected papers lean toward cs.AI and agent reliability; this small selection should not be mistaken for the whole batch’s center of gravity.

## Open Problems and Research Directions

- **Evidence recovery without sacrificing utility — open problem (paper-reported):** EpiSEM-Bench finds that resistance to missing facts does not necessarily produce useful recovery, and reports variation by domain and task family. **Direction (synthesis):** test whether recovery policies transfer to new tool APIs and task families while jointly measuring safe restraint, legitimate task completion, and interaction cost. [EpiSEM-Bench](https://arxiv.org/abs/2610.31650)
- **Reliable pruning with weak partial-trace signals — open problem (author-stated):** PKTP’s gains depend on useful representations of partial reasoning, and the authors identify better correctness-bearing representations as future work. **Direction (synthesis):** compare learned representations and uncertainty calibration under shifts in task type and candidate-pool size, then test whether the ranking remains robust when rollout correlations are misspecified. [Direct Pass@$k$](https://arxiv.org/abs/2610.31667)
- **Auditing under imperfect reviewers and sparse errors — open problem (author-stated):** the selective-auditing analysis assumes correct auditors and equal costs; the appendix notes that capping can weaken error control when errors are rare. **Direction (synthesis):** evaluate noisy, differently priced reviewers and report finite-sample error bounds across sparse-error regimes, separating theory-backed settings from tuned variants. [Selective Auditing](https://arxiv.org/abs/2610.31662)
- **Generalizing research-integrity monitoring — open problem (synthesis from study scope):** RIDAR’s reported results rely on a finite expert-labeled set and 300 recorded trajectories. **Direction:** validate taxonomy coverage, detector calibration, and intervention side effects on independent agent stacks and longer multi-stage research runs. [RIDAR](https://arxiv.org/abs/2610.31372)
- **Choosing when to recover from a macro — open problem (author-stated):** the coding-agent study finds that recovery can rescue early failures but waste effort after late failures; the authors call for broader task and failure coverage. **Direction:** benchmark selective recovery policies across repositories and models, with realistic partial side effects and cost-sensitive verification. [Adaptive Skill Granularity](https://arxiv.org/abs/2610.31461)

## Takeaway

This batch’s strongest coherent signal is not a new model architecture but more explicit control over agent failure: expose missing evidence, detect integrity violations, escalate decisions, and recover from brittle abstractions. These approaches are promising but remain early preprint evidence, with bounded evaluations and little comparable citation data; independent replication and broader deployment settings matter more than the apparent ordering here.

## Method and sources

- **Window:** daily, Friday 23 October 2026 announcement batch; exact window start and end: 2026-10-23 to 2026-10-23. Snapshot: 2026-10-25 00:13:11 UTC. Today is Sunday, so this uses the previous arXiv batch rather than an empty same-day report.
- **Scope/query:** core categories cs.AI, cs.LG, stat.ML, cs.CL, cs.CV, cs.RO, cs.NE, cs.MA. One date-bounded arXiv API query covered 2026-10-22 through 2026-10-24; it returned 449 matching records, all with 2026-10-22 published dates. The arXiv cs.AI recent page showed Friday, 23 October as the latest announcement batch and confirmed the selected papers within that batch. The category tags overlap.
- **Verification:** each of the five selected arXiv abstract pages was opened and checked for title, abstract, version, and categories. The arXiv API supplied authors, exact published/updated UTC timestamps, and category metadata. For the leading three, full HTML papers were read for method, evaluation, and stated limitations.
- **Inference method:** arXiv publishes no official trending chart. Ordering is inferred from discoverable secondary coverage, the paper-specific evidence and breadth of evaluation, and relevance to repeated themes among this curated sample. Semantic Scholar citation metadata was not available in this snapshot; citations therefore do not drive this ordering. No downloads, reads, or view counts are claimed.
- **Primary sources:** [arXiv cs.AI recent listing](https://arxiv.org/list/cs.AI/recent); [arXiv API](https://export.arxiv.org/api/query?search_query=%28cat%3Acs.AI+OR+cat%3Acs.LG+OR+cat%3Astat.ML+OR+cat%3Acs.CL+OR+cat%3Acs.CV+OR+cat%3Acs.RO+OR+cat%3Acs.NE+OR+cat%3Acs.MA%29+AND+submittedDate%3A%5B20261022+TO+20261024%5D&sortBy=submittedDate&sortOrder=descending&start=0&max_results=2000).
- **Secondary sources used for discoverability/context:** [Agentic Design on EpiSEM-Bench](https://agentic-design.ai/zh/news-hub/episem-bench-evaluating-safety-evidence-recovery-llm-agents-under-missing-704dd5); [Franklineh explainer](https://franklineh.com/learn/research/editorial-research-6b25a9795491abc6caed2f3643efc907); [arXivTLDR on PKTP](https://arxivtldr.org/abs/2610.31667); [BU CISE profile](https://www.bu.edu/cise/tijana-zrnic/); [Hugging Face Papers on RIDAR](https://huggingface.co/papers/2610.31372); [RIDAR code](https://github.com/THU-KEG/RIDAR); [Nowness AI on Adaptive Skill Granularity](https://nownessai.com/f/arxiv-2610-31461); [AI Pulse on Adaptive Skill Granularity](https://www.aipulsenews.co/article/arxiv-ai-1792728000000-di37bu).
- **Retrieval note:** arXiv’s category recent pages were inspected in the browser because the configured page extractor did not support direct URL extraction; selected abstracts were verified on arXiv itself. The Semantic Scholar endpoint did not supply usable citation metadata. These source limitations reinforce the conservative “notable recent papers” interpretation rather than a measured popularity ranking.
