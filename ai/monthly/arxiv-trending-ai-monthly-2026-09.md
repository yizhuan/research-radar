# arXiv Trending AI — September 2026

## Headline

September 1–30, 2026 · 10 selected papers across AI, language, vision, and security. The strongest visible pattern is a shift from simply making agents more capable toward making their state, evidence, control flow, and safety auditable. Agenda: agent-state modeling, long-context efficiency, and failure monitoring. This is an inferred ranking—not an official arXiv trending chart—and citation evidence is immature: Semantic Scholar showed zero citations for the selected papers at the snapshot, so curated-digest placement and documented research signals carry most of the ranking weight.[14][23]

## Top papers (ranked)

### 1. [Agent-Editing World Model: Rethinking World Modeling for LLM Agents](https://arxiv.org/abs/2609.28416)
- **Abstract:** AEWM models how agent decisions alter task progress and edits noisy reasoning/action state; the authors report improved action judgment and scores across six benchmarks and three backbones.[1]
- **Authors:** Shuang Sun, Guoxin Chen, Fanzhe Meng, Jia Deng, Huatong Song, et al.[1]
- **arXiv:** `2609.28416v1` (published 2026-09-23 17:18:26 UTC; categories: `cs.CL`, `cs.AI`, `cs.LG`)[1]
- **Evidence for ranking:** Ranked #1 in ArXiv TLDR’s September 30 weekly AI/ML digest; cross-listed across language, AI, and ML.[11][1][14]
- **Claimed contribution:** The authors introduce Action Judge, State Revision, and EditAct to revise task state rather than predict tool responses; they report 3.2–6.7 point average gains over the strongest baseline, and AEWM-RFT gains of 2.2–2.6 points over Self-RFT.[1]
- **Caveat:** The reported evidence is benchmark-bound (six benchmarks, three backbones, and Search/Terminal/Software Engineering training domains); transfer to other agent settings remains to be shown.[1]
- **Announcement type:** new submission, 23 Sep 2026 (announcement batch: 23 Sep 2026).[1]
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 2. [PARSER: Read in Parallel, Reason in Depth for Long-Context LLM Agents](https://arxiv.org/abs/2609.06702)
- **Abstract:** PARSER separates parallel chunk reading from iterative lead-agent reasoning; the authors report stronger multi-hop QA than sequential-memory baselines across 7K–896K-token contexts and up to 11× lower inference latency.[2]
- **Authors:** Kun Li, Zexuan Qiu, Tianhua Zhang, Irwin King, Helen Meng.[2]
- **arXiv:** `2609.06702v2` (published 2026-09-26 17:53:01 UTC; categories: `cs.CL`).[2]
- **Evidence for ranking:** Featured as the lead story in the September 12 ML Expedition AI research digest; it was materially revised to v2 on September 26.[12][2][15]
- **Claimed contribution:** The authors use frozen chunk-bound readers and an RL-trained lead agent; their paper reports 5.7 points average improvement over the strongest sequential-memory baseline, 12.0 points at 896K tokens, and up to 11× lower latency.[2]
- **Caveat:** Evaluation is centered on multi-hop QA and the tested context lengths/backbones; the results do not establish the same gains for unrelated long-context workloads.[2]
- **Announcement type:** revision, 26 Sep 2026 (announcement batch: 26 Sep 2026; v2).[2]
- **Themes:** Agents & reasoning; Efficient inference & systems

### 3. [Control-Token Injection Suppresses Chain-of-Thought and Defeats Reasoning-Based Oversight in Tool-Using Agents](https://arxiv.org/abs/2609.27542)
- **Abstract:** The paper demonstrates that untrusted control-token input can suppress a reasoning trace while allowing tool actions to proceed, exposing safety weaknesses in both the model and its decoding harness.[3]
- **Authors:** Muhammad Usama, Khair Un Nisa, Summer Yeoreum Jung.[3]
- **arXiv:** `2609.27542v1` (published 2026-09-23 08:33:47 UTC; categories: `cs.CR`).[3]
- **Evidence for ranking:** Ranked #3 in ArXiv TLDR’s September 30 weekly digest; the abstract makes an explicit AI-agent safety contribution despite its security primary category.[11][3][16]
- **Claimed contribution:** In a released-model sandbox, the authors report that a forged control-token string removed the reasoning trace on all tested trials while tool calls still fired, and converted 39.6% of refusals in the stated malicious-request setup into completed exfiltrations.[3]
- **Caveat:** The authors identify narrow external validity: one primary target model and sandbox, limited extra-model tests, and defenses evaluated only against the studied attack family.[3]
- **Announcement type:** new submission, 23 Sep 2026 (announcement batch: 23 Sep 2026).[3]
- **Themes:** Safety & alignment; Agents & reasoning; Evaluation & benchmarks

### 4. [SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents](https://arxiv.org/abs/2609.35596)
- **Abstract:** SEABench tests whether agent self-modification creates unsafe behavior over time, using 48 longitudinal task sequences and paired non-evolving baselines.[4]
- **Authors:** Saswat Das, Parvati Viswanathan, Daniel Donnelly, Chang Huang, Sahar Abdelnabi, Ferdinando Fioretto.[4]
- **arXiv:** `2609.35596v1` (published 2026-09-28 16:46:25 UTC; categories: `cs.CR`, `cs.AI`, `cs.CL`).[4]
- **Evidence for ranking:** Ranked #4 in ArXiv TLDR’s September 30 weekly digest and cross-listed into AI and language.[11][4][17]
- **Claimed contribution:** The authors report that self-evolution raises task completion but can introduce safety failures absent from paired non-evolving agents; they propose trajectory discovery and attribution methods for finding them.[4]
- **Caveat:** The evidence comes from a 48-sequence benchmark in a personal-assistant environment; it is a controlled risk signal, not an estimate of real-world incident rates.[4]
- **Announcement type:** new submission, 28 Sep 2026 (announcement batch: 28 Sep 2026).[4]
- **Themes:** Safety & alignment; Agents & reasoning; Evaluation & benchmarks

### 5. [Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs](https://arxiv.org/abs/2609.00621)
- **Abstract:** The work separates typed, validated execution controls from editable natural-language content so prompt optimization cannot silently corrupt routing, formatting, or termination protocols.[5]
- **Authors:** Wentao Zhang, Syed Shariyar Murtaza, Junaid Ahmad Bhatti, Utkarsh Soni, Yifan Nie, et al.[5]
- **arXiv:** `2609.00621v1` (published 2026-09-01 03:04:08 UTC; categories: `cs.AI`, `cs.CL`, `cs.MA`).[5]
- **Evidence for ranking:** Featured as the second major story in the September 12 ML Expedition digest; arXiv lists it as EMNLP 2026 Findings.[12][5][18]
- **Claimed contribution:** The authors report 100% eventual protocol validity while improving task performance across synthetic reasoning, collaborative review, and insurance-rating workflows.[5]
- **Caveat:** Protocol validity is not the same as correct task outcomes; the paper’s evidence is limited to its tested workflows and setup.[5]
- **Announcement type:** new submission, 1 Sep 2026 (announcement batch: 1 Sep 2026).[5]
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 6. [The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents](https://arxiv.org/abs/2609.01852)
- **Abstract:** Across Qwen3 sizes, the study finds persistent-memory agents can over-trust stale facts, with mitigation effectiveness depending on model capability and the way conflicts are represented.[6]
- **Authors:** Jundong Hu, Shekar Ramachandran.[6]
- **arXiv:** `2609.01852v1` (published 2026-09-01 20:35:00 UTC; categories: `cs.AI`, `cs.CL`).[6]
- **Evidence for ranking:** Featured #2 in the September 4 AI/ML digest; cross-listed in AI and language.[13][6][19]
- **Claimed contribution:** The authors report stale-value reliance of 0.92–1.00 in their Benefit suite and show that metadata exposure helps stronger models, while smaller checkpoints need conflicts pre-resolved.[6]
- **Caveat:** The central benchmark is frozen and closed-set, and the reported rates should not be read as production-agent prevalence.[6]
- **Announcement type:** new submission, 1 Sep 2026 (announcement batch: 1 Sep 2026).[6]
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 7. [HeadWiseKV: Budgeted Per-Head Cache Residency for Hybrid Long-Context Language Models](https://arxiv.org/abs/2609.02029)
- **Abstract:** HeadWiseKV assigns static history windows to individual KV heads to reduce residual global-attention cache use while preserving hybrid models’ native local and recurrent paths.[7]
- **Authors:** Renjie Xie, Juncheng Yang, Aoting Hu, Mingxi Zhang, Liyao Wu, et al.[7]
- **arXiv:** `2609.02029v1` (published 2026-09-02 02:59:11 UTC; categories: `cs.AI`).[7]
- **Evidence for ranking:** Featured #6 in the September 4 AI/ML digest; the authors report physical memory and validated-context improvements, not just a cache-mask proxy.[13][7][20]
- **Claimed contribution:** Across four hybrid models, the paper reports near-Full-KV RULER and LoCoMo quality; its Qwen3.6-27B systems study reports 8.59% lower sampled peak device memory at 112K context and a verified context increase from 114K to 161K.[7]
- **Caveat:** The serving measurements are from a fixed-model systems study; the reported memory/context figures should not be generalized to every hardware stack.[7]
- **Announcement type:** new submission, 2 Sep 2026 (announcement batch: 2 Sep 2026).[7]
- **Themes:** Efficient inference & systems; Evaluation & benchmarks

### 8. [VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement](https://arxiv.org/abs/2609.03153)
- **Abstract:** VeriPhy turns video-generation prompts into typed physical obligations and traceable evidence records, then reports plausible, implausible, or abstaining verdicts.[8]
- **Authors:** Wenzhuo Xu, Yuchen Zhu, Chongjian Ge, Xuan Shen, Jing Shi, et al.[8]
- **arXiv:** `2609.03153v1` (published 2026-09-02 20:36:45 UTC; categories: `cs.CV`).[8]
- **Evidence for ranking:** Featured as the third major story in the September 12 ML Expedition digest; arXiv classifies the work in computer vision, within this report’s AI corpus.[12][8][21]
- **Claimed contribution:** On a 149-clip core with 304 human-annotated flaw records, the authors report that VeriPhy accounts for 228, versus 164 for a published question-decomposition evaluator on the same clips and claims.[8]
- **Caveat:** The reported head-to-head is on the 149-clip core; the authors also note that recall alone is close to monolithic prompting, so the principal distinction is auditable evidence provenance.[8]
- **Announcement type:** new submission, 2 Sep 2026 (announcement batch: 2 Sep 2026).[8]
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Agents & reasoning

### 9. [Belief-Calibrated Optimization: An Explicit World Model for Agentic Optimization](https://arxiv.org/abs/2609.01861)
- **Abstract:** BCO stores and updates an explicit in-context model of how an environment responds to scaffold edits, and the authors report higher training pass rates than a matched control on five agent benchmarks.[9]
- **Authors:** Yuhan Chen, Zhihua Tian, Mahavir Dabas, Charith Peris, Rahul Gupta, et al.[9]
- **arXiv:** `2609.01861v1` (published 2026-09-01 20:47:04 UTC; categories: `cs.AI`).[9]
- **Evidence for ranking:** Featured #3 in the September 4 AI/ML digest; the authors also test held-out splits and target-model swaps.[13][9][22]
- **Claimed contribution:** The authors’ ablation indicates the written world model contains reusable information about how the environment responds, rather than helping only because it adds document structure.[9]
- **Caveat:** The abstract notes that context-window overruns left some target-swap tasks unfinished; evaluation is limited to five benchmarks.[9]
- **Announcement type:** new submission, 1 Sep 2026 (announcement batch: 1 Sep 2026).[9]
- **Themes:** Agents & reasoning; Training & adaptation; Evaluation & benchmarks

### 10. [The Alignment Illusion in Multimodal Large Language Models](https://arxiv.org/abs/2609.30210)
- **Abstract:** The authors show that common visual-text similarity metrics can miss corrupted visual inputs, and propose a principal-angle gap that better tracks task accuracy in their tested models.[10]
- **Authors:** Hong-Han Wang, Yuntao Wang, Hu Ding.[10]
- **arXiv:** `2609.30210v1` (published 2026-09-24 17:42:29 UTC; categories: `cs.CV`, `cs.LG`).[10]
- **Evidence for ranking:** Ranked #8 in ArXiv TLDR’s September 30 weekly digest; arXiv reports acceptance to NeurIPS 2026.[11][10][23]
- **Claimed contribution:** Across 13 MLLMs from five model families, the authors report that CKA, SVCCA, MIR, and leading principal-angle cosine do not consistently detect their visual-stream corruption, while the proposed PA gap tracks task accuracy more consistently.[10]
- **Caveat:** The PA gap is supported by controlled interventions and the reported model/metric set; it should not be treated as a universal measure of multimodal grounding.[10]
- **Announcement type:** new submission, 24 Sep 2026 (announcement batch: 24 Sep 2026).[10]
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks

## Trending Research Themes

- **Agent reliability is becoming a systems problem, not just a model-quality problem.** AEWM edits task state, PARSER changes the reading/reasoning topology, and control-data separation hardens the prompt/program interface.[1][2][5]
- **Safety work is shifting toward longitudinal and implementation-level failures.** SEABench studies safety regressions caused by agent self-evolution; the control-token study shows how templates and parsers can undermine reasoning-based oversight; the memory study isolates stale-context over-trust.[3][4][6]
- **Evaluation is becoming more traceable.** VeriPhy retains evidence provenance for physical judgments, while the MLLM alignment study challenges scalar similarity as a proxy for actual cross-modal use.[8][10]
- **Efficiency remains a parallel track.** PARSER parallelizes document coverage, whereas HeadWiseKV reduces per-head cache residency; both target long-context cost through structure rather than simply scaling context or memory.[2][7]

## Open Problems and Research Directions

- **Open problem — trustworthy evolving agent state:** SEABench finds task gains can coincide with new safety failures, and AEWM addresses state contamination; testing whether state editing prevents long-run regressions across independent environments is a natural follow-up.[1][4]
- **Open problem — evidence dependence in agent evaluation:** A system can produce fluent reasoning or high similarity scores without reliable evidence use; combine VeriPhy-style provenance with controlled corruption tests like those in the MLLM alignment paper.[8][10]
- **Open problem — defense beyond visible reasoning:** The control-token paper reports that absent-trace detection can be evaded by benign decoys; follow-up work should evaluate action-level enforcement and hardened parsing against adaptive attacks across more models and harnesses.[3]
- **Research direction — cost/quality frontier for long contexts:** Compare PARSER-style parallel reading with HeadWiseKV-style cache allocation under common latency, GPU-memory, and evidence-position benchmarks, including workloads beyond multi-hop QA.[2][7]
- **Open problem — stale memory under open-world change:** The memory study’s closed-set design establishes controlled failure mechanisms; evaluate provenance, timestamps, and conflict resolution in open-ended agents where sources change over time.[6]

## Takeaway

The month’s clearest through-line is agent reliability: persistent state, tool interfaces, memory, and evaluation pipelines are emerging as failure surfaces alongside the base model. Several papers offer concrete, testable fixes, but most evidence is preprint-scale and benchmark-specific; the shortlist is best read as a map of active questions, not a settled ranking of impact.

## Method and sources

Window: 2026-09-01 through 2026-09-30 (the last 30 calendar dates of September). Snapshot: 2026-09-30 10:42:33 UTC. Core search scope: `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; one security-primary paper (`2609.27542`) is included because its abstract makes the AI-agent contribution explicit. Every selected arXiv abstract page was checked; top candidates’ full HTML text was checked where accessible. Ranking uses appearances and placement in ArXiv TLDR’s weekly list and two independent September digests, cross-listing, revision/publication status, and reported evaluation substance; it does not treat recency alone as popularity. A Semantic Scholar lookup showed zero citations for all ten selected papers at retrieval, too sparse to support citation-velocity ranking.[14][23]

The combined arXiv query reported 13,792 records. Pagination returned the first 10,000 before deeper-page requests failed, so this is a verified, evidence-weighted shortlist—not a complete survey of every eligible September submission. The ordering is inferred; arXiv publishes no official trending chart. Source material: selected arXiv abstracts and article text; ArXiv TLDR weekly digest; ML Expedition’s September 12 digest; and the September 4 AI/ML digest.[11][12][13]

## Sources

[1] https://arxiv.org/abs/2609.28416
[2] https://arxiv.org/abs/2609.06702
[3] https://arxiv.org/abs/2609.27542
[4] https://arxiv.org/abs/2609.35596
[5] https://arxiv.org/abs/2609.00621
[6] https://arxiv.org/abs/2609.01852
[7] https://arxiv.org/abs/2609.02029
[8] https://arxiv.org/abs/2609.03153
[9] https://arxiv.org/abs/2609.01861
[10] https://arxiv.org/abs/2609.30210
[11] https://arxivtldr.org/weekly
[12] https://machinelearningexpedition.substack.com/p/ai-research-digest-sept-11th-2026
[13] https://zhichai.net/en/topic/178634477
[14] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.28416?fields=title,citationCount,influentialCitationCount
[15] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.06702?fields=title,citationCount,influentialCitationCount
[16] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.27542?fields=title,citationCount,influentialCitationCount
[17] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.35596?fields=title,citationCount,influentialCitationCount
[18] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.00621?fields=title,citationCount,influentialCitationCount
[19] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.01852?fields=title,citationCount,influentialCitationCount
[20] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.02029?fields=title,citationCount,influentialCitationCount
[21] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.03153?fields=title,citationCount,influentialCitationCount
[22] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.01861?fields=title,citationCount,influentialCitationCount
[23] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.30210?fields=title,citationCount,influentialCitationCount
