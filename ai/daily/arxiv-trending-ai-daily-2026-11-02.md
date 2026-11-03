# arXiv Trending AI — Daily — 2026-11-02

## Headline

**Core AI categories, 5 papers from the Monday 2026-11-02 announcement batch.** The common pattern is system-level agent reliability: better computer-use interfaces, retrieval/context handling, prompt-injection defenses, and scrutiny of evaluation validity, alongside a long-context efficiency method. Spoken agenda: agent interfaces and retrieval first, then benchmark reliability, security, and efficient attention. arXiv has no official trending chart; this ordering is inferred from a curated external shortlist and corroborating coverage, with limited citation evidence for papers this recent.

## Top papers (ranked)

### 1. [Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents](https://arxiv.org/abs/2610.41432)
- **Abstract:** HCU combines programmatic, accessibility-tree, and GUI interaction; on OSWorld 2.0, the authors report the highest Partial and Binary scores among compared systems and improved task success and efficiency across tested models.
- **Authors:** Haoqing Wang, Xiaoyi Zhang, Sicheng Fan, Zhexin Zhang, Xinjie Zhang, et al.
- **arXiv:** `2610.41432v1` (published 2026-10-30T08:38:29Z; categories: `cs.HC` (primary), `cs.CL`)
- **Evidence for ranking:** ArXiv TLDR's 2026-W45 curated shortlist placed it #2; it also appeared in Recursive Intelligence's 2026-11-02 AI/ML morning brief. Its cross-listing spans human-computer interaction and language technology. These are editorial coverage signals, not readership statistics.
- **Claimed contribution:** The authors introduce a three-channel interface with compact accessibility observations, batched actions, post-action diffs, and a skill for coordinating channels; the paper reports that evaluated models allocate work across them differently.
- **Caveat:** The performance claims are tied to OSWorld 2.0 and the tested models, platforms, and baselines; they do not establish gains for every application or workflow.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Efficient inference & systems

### 2. [ReuScope: Auditing Data Reuse and Evaluation Sensitivity in Capsule Vision 2024](https://arxiv.org/abs/2610.41835)
- **Abstract:** ReuScope separates measurements of dataset overlap from performance-sensitivity tests in Capsule Vision 2024; removal of selected training rows lowered public-validation balanced accuracy from 82.5% to 61.2%, which the authors explicitly say is not an estimate of leakage-induced inflation.
- **Authors:** Eunseob Choi, Kyeonghun Kim, Hyuk-Jae Lee, Nam-Joon Kim
- **arXiv:** `2610.41835v1` (published 2026-10-30T14:51:37Z; categories: `cs.AI` (primary), `cs.CV`)
- **Evidence for ranking:** ArXiv TLDR's 2026-W45 shortlist placed it #3; the arXiv record notes acceptance at NeurIPS 2026, Track on Evaluations and Datasets. It also spans AI and computer vision. Acceptance and cross-listing corroborate relevance/quality, not popularity.
- **Claimed contribution:** The authors propose a paired audit protocol that distinguishes observed reuse from conditional performance sensitivity, specifying the evaluation population, class support, and uncertainty unit for each conclusion.
- **Caveat:** The authors limit the audit to one benchmark and one primary training pipeline; missing cross-recording patient identifiers prevent patient-level overlap counts, and the reported intervals reflect seed variation rather than patient sampling.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Evaluation & benchmarks; Data & synthetic data

### 3. [Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic Systems with Harnesses](https://arxiv.org/abs/2610.41172)
- **Abstract:** The paper frames LLM-based knowledge compilation as an upstream supply layer for agentic retrieval; on FRAMES, claim-evidence trees reduced query tokens on average, while structural compilation did not produce a detectable accuracy gain under a competent harness.
- **Authors:** Zhichang Yu, Baining Cao, Idriss Sbaaoui, Qi Wang, Gangqiang Xu, et al.
- **arXiv:** `2610.41172v1` (published 2026-10-30T02:48:37Z; categories: `cs.IR` (primary), `cs.AI`, `cs.CL`)
- **Evidence for ranking:** ArXiv TLDR's 2026-W45 shortlist placed it #4; it is cross-listed across information retrieval, AI, and language, and was also surfaced by independent paper-summary services including EmergentMind and CatalyzeX.
- **Claimed contribution:** The authors describe a configurable ingestion pipeline that compiles documents into structures such as claim-evidence trees, graphs, and timelines, and release the RAGFlow pipeline/harness; they distinguish context supply from retriever quality.
- **Caveat:** The authors describe measurements as one-benchmark, one-compiler-model operating points, without confidence intervals or repeated seeds; FRAMES is English and Wikipedia-based, and the paper cautions against generalizing its PageIndex result beyond that scale.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Retrieval & knowledge; Agents & reasoning; Efficient inference & systems

### 4. [SecPO: Principled Adversarial Training for Prompt Injection Security](https://arxiv.org/abs/2610.41998)
- **Abstract:** SecPO combines a loss based on an approximated injection-invariant reference with adversarially synthesized attacks; for Qwen3.6-27B, the authors report 8.8% AgentDojo attack success versus 78.8% for Meta-SecAlign under AttackerMovesSecond, with no noticeable utility reduction on nine evaluated benchmarks.
- **Authors:** Sizhe Chen, Yibo Peng, Jaewon Chang, Chawin Sitawarin, David Wagner
- **arXiv:** `2610.41998v1` (published 2026-10-30T16:43:17Z; categories: `cs.CR` (primary), `cs.AI`)
- **Evidence for ranking:** ArXiv TLDR's 2026-W45 shortlist placed it #8. The authors provide a dedicated technical site and public code, training data, and model; the security/AI cross-list and reproducible artifact release are corroborating signals, not measures of readership.
- **Claimed contribution:** The authors propose SecPO to approximate an injection-invariant, utility-preserving reference and pair it with adversarial training against stronger synthesized injections; the reported reductions are on specified adaptive attacks and benchmarks.
- **Caveat:** The headline agent result is for one model and the specified AgentDojo attack setting; the abstract does not establish robustness to all real-world injection channels or adaptive attackers.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Safety & alignment; Training & adaptation; Evaluation & benchmarks

### 5. [Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention](https://arxiv.org/abs/2610.42147)
- **Abstract:** LSA hierarchically clusters keys in a learned latent space so queries can score clusters rather than all keys; the authors report faster attention at ultra-long context with similar measured accuracy, including one-layer speedups at 10M tokens.
- **Authors:** Ales Kubicek, Andrea Caciolai, Liangzu Peng, Sukrit Sumant, Benjamin Hoover, et al.
- **arXiv:** `2610.42147v1` (published 2026-10-30T17:59:34Z; categories: `cs.AI` (primary))
- **Evidence for ranking:** ArXiv TLDR's 2026-W45 shortlist placed it #9; separate paper-summary pages at EmergentMind and Papers.cool also surfaced the work. Its reported 10M-token efficiency evaluation supports technical relevance, not a claim about readership.
- **Claimed contribution:** The authors introduce Distilled-LSA for adapting pretrained models and Native-LSA for next-token training, using hierarchical latent-space key clustering to reduce attention work at long context.
- **Caveat:** The large speed figures are per attention layer on a specified model at 10M tokens; Native-LSA is reported at 128k tokens, so these results do not by themselves establish end-to-end serving gains across model sizes or hardware.
- **Announcement type:** new submission, 2026-11-02 announcement batch
- **Themes:** Efficient inference & systems; Training & adaptation

## Trending Research Themes

- **Agent reliability is being addressed at multiple system boundaries.** Hybrid Computer Use changes how agents act on desktops; Context as Infrastructure manages the evidence entering retrieval loops; SecPO addresses hostile instructions in that context. These are complementary layers, not a single newly established architecture.
- **Evaluation validity and efficiency are becoming explicit research targets.** ReuScope distinguishes overlap from causal claims about performance sensitivity, while Hybrid Computer Use reports task success and interaction efficiency and Context as Infrastructure exposes uncertainty in small-sample operating points. This is a recurring measurement concern, not proof that any benchmark is invalid wholesale.
- **Long-context work is shifting from capacity alone toward cost control.** Context as Infrastructure reduces repeated retrieval/context handling in a bounded FRAMES setting, while Latent Sparse Attention targets key-selection cost at million-token scale. Their methods operate at different stages of the pipeline.
- **Category coverage is broad within this small ranked set:** the five papers cover cs.HC/cs.CL, cs.AI/cs.CV, cs.IR/cs.AI/cs.CL, cs.CR/cs.AI, and cs.AI. Across the full batch pool, cs.LG had the most category-page listings (198), followed by cs.AI (186); listing counts overlap because of cross-lists.

## Open Problems and Research Directions

- **Open problem (author-stated):** [ReuScope](https://arxiv.org/abs/2610.41835) covers one benchmark and primary training pipeline; missing patient identifiers and seed-only uncertainty limit patient-level and population-level conclusions. **Research direction (synthesis):** replicate its split-audit protocol across datasets and pipelines with patient-level linkage where ethically available and uncertainty estimates that include sampling variation.
- **Open problem (author-stated):** [Context as Infrastructure](https://arxiv.org/abs/2610.41172) reports one benchmark/compiler setup without repeated seeds or confidence intervals, and its corpus is English/Wikipedia-based. **Research direction (synthesis):** test the compiler and harness across enterprise-like corpora, model families, repeated seeds, and measured retrieval-miss/latency trade-offs.
- **Open problem (evidence boundary):** [Hybrid Computer Use](https://arxiv.org/abs/2610.41432) reports strong results on OSWorld 2.0 and selected systems, but that evidence cannot settle which channel combinations transfer to unseen applications. **Research direction (synthesis):** use matched tasks and cost budgets across independent desktop environments, auditing stale-state recovery and channel-specific failure rates.
- **Open problem (evidence boundary):** [SecPO](https://arxiv.org/abs/2610.41998) demonstrates results on stated adaptive attacks and benchmarks; broader robustness remains unmeasured in the abstract. **Research direction (synthesis):** red-team with adaptive, multimodal, and compositional injections across model families while jointly reporting attack success, false refusals, and benign task utility.
- **Open problem (evidence boundary):** [Latent Sparse Attention](https://arxiv.org/abs/2610.42147) reports per-layer speedups in specified contexts rather than a general end-to-end serving result. **Research direction (synthesis):** benchmark end-to-end throughput, memory, quality, and hardware sensitivity across context lengths and model scales, including KV-cache costs.

## Takeaway

The batch's strongest shared signal is practical agent engineering: interface design, context delivery, and injection resistance are being treated as connected reliability problems, while evaluation audits ask whether reported gains mean what they appear to mean. The shortlist is useful for tracking these approaches, but the evidence is too early and too dependent on curated coverage to support claims of broad adoption or durable superiority.

## Method and sources

- **Window and snapshot:** Daily report for the latest available arXiv announcement batch, Monday 2026-11-02; announcement-window start and end are both 2026-11-02. The selected papers' arXiv first-submission timestamps are on 2026-10-30. This uses the prior available batch because the snapshot was 2026-11-03T01:14:23Z and no 2026-11-03 announcement batch was shown. All five selected records are v1 new submissions, not revisions.
- **Scope/query:** Core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`; query: `(cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA)`. The eight category recent pages listed 186, 198, 30, 86, 102, 72, 6, and 11 papers for the batch respectively; these overlap, yielding 508 distinct IDs after deduplication. Each selected abstract and its version/date/categories were verified on the arXiv abstract page; top-three paper HTML was reviewed for methods/results and limitations or discussion.
- **Inference:** arXiv has no official trending or readership/download chart. The five selected papers are ordered by their positions in ArXiv TLDR's curated 2026-W45 list (#2, #3, #4, #8, #9), with cross-listing, NeurIPS acceptance where applicable, public artifacts, and independent technical coverage as corroboration; this is a transparent proxy, not an arXiv popularity ranking. Semantic Scholar citation counts were not used: Graph API requests for the selected IDs returned rate limits at the snapshot, so citation totals and citation velocity are unreported.
- **arXiv category sources:** [cs.AI](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), [cs.MA](https://arxiv.org/list/cs.MA/recent).
- **Ranking and corroborating sources:** [ArXiv TLDR weekly shortlist, 2026-W45](https://arxivtldr.org/weekly/2026-W45); [Recursive Intelligence morning brief, 2026-11-02](https://recursiveintelligence.io/briefs/2026-11-02-am-ai-ml); [EmergentMind summaries for Context as Infrastructure](https://www.emergentmind.com/papers/2610.41172) and [Latent Sparse Attention](https://www.emergentmind.com/papers/2610.42147); [Papers.cool summary for Latent Sparse Attention](https://papers.cool/arxiv/2610.42147); [SecPO project site](https://sizhe-chen.github.io/SecPO-Website/).
