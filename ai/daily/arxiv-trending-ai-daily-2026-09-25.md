# arXiv Trending AI — 2026-09-25 batch

## Headline
The strongest signal in the latest AI batch is a shift from generic agent demos toward operational reliability: governed tool access, segment-level RL credit assignment, exactly-once side effects, and verifiable domain benchmarks. The ordering below is inferred, not an official arXiv ranking: arXiv publishes no official trending chart.

## Top papers (ranked)

### 1. [Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery](https://arxiv.org/abs/2609.28693)
- **Abstract:** The paper introduces skilder, which exposes tools to an LLM agent only through task-discovered, role-scoped skills and reports no unauthorized tool calls or parameter violations in its governed-call evaluation.
- **Authors:** Michael Stettler, Benjamin Girardet, Jonas Canton, Nicolas Corod
- **arXiv:** `2609.28693v1` (published 2026-09-23 18:31 UTC; categories: `cs.AI`, `cs.CR`, `cs.MA`, `eess.SY`)
- **Evidence for ranking:** Paper Radar’s 2026-09-25 AI digest placed it first among 28 “must-read” papers with a 98% model-interest score and an Agents label; it was also among 63 shortlisted papers from 312 submissions reviewed. These are external editorial/model-selection signals, not citations or readership statistics; Semantic Scholar citation data was unavailable during this check.
- **Claimed contribution:** The authors claim role-scoped capability delivery can combine deterministic governance boundaries with dynamic cross-role capability acquisition.
- **Caveat:** The abstract says aggregate task-pass rates also include discovery-protocol and response-quality misses, so they should not be interpreted as authorization failures; the evidence is a six-model, 13-task evaluation.
- **Announcement type:** new submission, 2026-09-23 announcement batch
- **Themes:** Safety & alignment; Agents & reasoning; Evaluation & benchmarks

### 2. [DEEPO: Dual-Entropy Enhanced Policy Optimization for Hallucination in MLLMs](https://arxiv.org/abs/2609.28570)
- **Abstract:** DEEPO combines entropy-triggered expert prefixes with advantage-sign-aware Rényi preconditioning to improve reinforcement-learning correction of hallucinations in multimodal language models.
- **Authors:** Yingxuan Zhuang, Miao Pan, Wangjie Gan, Jingxiao Yang, Fan Wang, Weiming Liu, Cheng Tan, Xuhong Zhang, Jintao Chen
- **arXiv:** `2609.28570v1` (published 2026-09-23 11:39 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Paper Radar ranked it second in the must-read group with a 97% model-interest score and a Hallucination label; Semantic Scholar citation data was unavailable during this check. The ranking reflects this signal plus recency and relevance to a central reliability problem, not proven field impact.
- **Claimed contribution:** The paper reports that DEEPO improves over GRPO components individually and that their interaction yields a statistically significant +4.0 percentage-point result on VideoMMMU, with gains elsewhere.
- **Caveat:** The abstract reports selected benchmark results and does not establish whether the method transfers broadly beyond the evaluated multimodal tasks and training setup.
- **Announcement type:** new submission, 2026-09-23 announcement batch
- **Themes:** Multimodal & vision-language; Safety & alignment; Training & adaptation

### 3. [SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL](https://arxiv.org/abs/2609.29050)
- **Abstract:** SLCA-GRPO assigns separate execution and preference advantages to tool-call and summary segments, using a schema-guided simulator to train tool-calling agents without costly real APIs.
- **Authors:** Yan Zhan, Shaobo Liu, Qiunan Liu, Yuanjun Shi, Siqi Xu, WeiYi Hou, Xiang Xu, Zekang Li, Weizhou Pan, Jiahong Yan
- **arXiv:** `2609.29050v1` (published 2026-09-24 05:31 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Paper Radar placed it third in the must-read group with a 97% model-interest score and an Agents label; the paper also provides code and a dataset link in its arXiv comments. Semantic Scholar citation data was unavailable during this check.
- **Claimed contribution:** On a 7B backbone, the authors report improvements over GRPO, ToolPO, and RLTR of +2.53 pp in-domain, +1.36 pp on BFCL, and +9.15 pp on τ²-Bench under matched budgets.
- **Caveat:** Results are reported on a simulator and selected benchmarks; real-API behavior and transfer to other tool schemas remain open questions.
- **Announcement type:** new submission, 2026-09-24 announcement batch
- **Themes:** Agents & reasoning; Training & adaptation; Efficient inference & systems

### 4. [Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents](https://arxiv.org/abs/2609.29095)
- **Abstract:** LIMBO evaluates duplicate side effects under realistic failures and finds that exactly-once behavior depends on the fault, with idempotency keys outperforming waiting or verification alone.
- **Authors:** Jiapeng Li
- **arXiv:** `2609.29095v1` (published 2026-09-24 06:24 UTC; categories: `cs.LG`, `cs.AI`, `cs.SE`)
- **Evidence for ranking:** Paper Radar placed it fourth in the must-read group with a 97% model-interest score and an Agents/Evaluation label; its unusually concrete 25,930-episode failure analysis supplies a strong technical relevance signal. Semantic Scholar citation data was unavailable during this check.
- **Claimed contribution:** The paper reports that optional idempotency keys reduce duplicate writes from 28% to 4% in its setting and that the contract, rather than the harness, explains most of the relevant variance when outcomes are not observable.
- **Caveat:** The conclusions are tied to LIMBO’s six services, fault model, contracts, nine models, and recovery conditions; production distributions may differ.
- **Announcement type:** new submission, 2026-09-24 announcement batch
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 5. [Synthetic Hospital: An Open, Verifiable, Physician-Validated Longitudinal EHR Benchmark](https://arxiv.org/abs/2609.30027)
- **Abstract:** Synthetic Hospital provides 1,268 synthetic longitudinal patients and 5,602 encounters grounded in medical ontologies and provenance, then evaluates models on realistic EHR reconstruction and summarization.
- **Authors:** Christine Park, Valerie Chen, Tim Dettmers
- **arXiv:** `2609.30027v1` (published 2026-09-24 16:00 UTC; categories: `cs.AI`, `cs.DB`)
- **Evidence for ranking:** Paper Radar placed it fifth in the must-read group with a 97% model-interest score and an Evaluation label; the benchmark’s open/verifiable design and physician-validation claim add independent relevance signals. Semantic Scholar citation data was unavailable during this check.
- **Claimed contribution:** The authors report that physicians distinguished records from real charts at near-chance rates and that the best model reached severity-weighted F1 0.73 versus 0.89 for the best physician on a matched subset.
- **Caveat:** The records are synthetic and derived from public medical-education material; realism and transfer to protected real-world EHR distributions require further validation.
- **Announcement type:** new submission, 2026-09-24 announcement batch
- **Themes:** Evaluation & benchmarks; Retrieval & knowledge; Safety & alignment

### 6. [IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis](https://arxiv.org/abs/2609.29444)
- **Abstract:** IterSynth separates planning from evidence synthesis and keeps an evolving summary as search state, while RDPO supplies role-specific reinforcement-learning credit assignment.
- **Authors:** Xingyu Wu, Yuchen Yan, Zhengxi Lu, Siqi Chen, Xin Zhang, Aiting Liu, Chao Deng, Jie Liu, Jin Ma, Jian Shao, Jun Xiao, Yongliang Shen
- **arXiv:** `2609.29444v1` (published 2026-09-24 12:02 UTC; categories: `cs.CL`, `cs.AI`)
- **Evidence for ranking:** Paper Radar included it in the must-read group with a 96% model-interest score and an Agents label; the paper reports results on five long-horizon search benchmarks and provides a code comment. Semantic Scholar citation data was unavailable during this check.
- **Claimed contribution:** The authors report IterSynth-8B average score 50.7, +4.2% over the strongest prior ≤8B agent, plus zero-shot gains over ReAct-like prompting on frontier models.
- **Caveat:** The abstract does not establish how much of the gain comes from role decomposition, summary state, or RDPO individually outside the reported ablations.
- **Announcement type:** new submission, 2026-09-24 announcement batch
- **Themes:** Agents & reasoning; Retrieval & knowledge; Training & adaptation

### 7. [ELF-REG: Scaling Continuous Diffusion Language Models to Reasoning Tasks](https://arxiv.org/abs/2609.29102)
- **Abstract:** ELF-REG uses representation alignment and entanglement with a frozen autoregressive teacher to improve fully continuous diffusion language models on math and code tasks.
- **Authors:** Zeyu Michael Li, William Xingxu Chen, Bingshuo Qian, Jiayin Liu, Xiang Cheng
- **arXiv:** `2609.29102v1` (published 2026-09-24 06:33 UTC; categories: `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Paper Radar included it in the must-read group with a 96% model-interest score and a New model label; its cross-task results make it a notable systems/method paper. Semantic Scholar citation data was unavailable during this check.
- **Claimed contribution:** The paper reports that ELF-REG-L reaches 55.96% pass@1 on GSM8K at 64 NFE and improves MATH-500 from 10.55% to 13.39% over its ELF-L baseline.
- **Caveat:** The reported comparisons are against evaluated comparable-scale diffusion models; the abstract does not show parity with leading autoregressive systems.
- **Announcement type:** new submission, 2026-09-24 announcement batch
- **Themes:** Efficient inference & systems; Training & adaptation; Agents & reasoning

### 8. [PROOF: Profiling Reliability of Object-Level Facts in Large Language Models](https://arxiv.org/abs/2609.29504)
- **Abstract:** PROOF profiles factual coverage across facts, relations, domains, prompt formulations, and decoding perturbations rather than reducing reliability to one aggregate score.
- **Authors:** Andrei Chetvergov, Mikhail Solovev, Timofei Sivoraksha, Stepan Ukolov, Valeriia Kuschenko, Alexander Evseev, Sergey Bolovtsov
- **arXiv:** `2609.29504v1` (published 2026-08-24 17:13 UTC; categories: `cs.CL`, `cs.AI`)
- **Evidence for ranking:** Paper Radar included it in the must-read group with a 96% model-interest score and an Evaluation/Hallucination label. Semantic Scholar returned 0 citations and 0 influential citations at this snapshot; the ranking therefore relies on the external shortlist and methodological relevance, not citation momentum.
- **Claimed contribution:** Across 18 open-weight deployments, the authors report large domain and formulation sensitivities, including up to 26.5 percentage points from neutral wording changes and up to 79.4% breakage under adversarial formulations.
- **Caveat:** This is a benchmark based on a frozen Wikidata snapshot and controlled prompts; its relationship to open-ended real-world factual use remains to be tested.
- **Announcement type:** new submission, earlier 2026-08-24 submission; surfaced in the 2026-09-25 digest
- **Themes:** Evaluation & benchmarks; Safety & alignment; Retrieval & knowledge

## Trending Research Themes

- **Agent reliability is becoming a systems problem.** Skilder moves authorization into capability delivery; LIMBO studies duplicate side effects; and SLCA-GRPO treats tool calls as structurally different from summaries. Together they point beyond prompt-only safeguards toward contracts, simulators, and explicit execution semantics.
- **Credit assignment is being specialized rather than broadcast.** SLCA-GRPO separates tool and summary rewards, while IterSynth assigns role-specific advantages to planning and synthesis. The common idea is that a single trajectory-level scalar is too coarse for heterogeneous agent behavior.
- **Evaluation is becoming more verifiable and domain-grounded.** Synthetic Hospital, PROOF, and LIMBO all use structured environments with explicit ground truth or ledgers, targeting failures that aggregate benchmark scores can hide.
- **Efficiency remains an active model-design axis.** ELF-REG explores continuous diffusion language models, while IterSynth reduces search-context accumulation through persistent summaries. Neither result alone establishes a replacement for autoregressive frontier models.
- **Hallucination is being treated as an optimization and measurement problem.** DEEPO targets the RL correction chain; PROOF measures intervention-sensitive factual reliability; Synthetic Hospital tests longitudinal omissions in a clinical setting.

## Open Problems and Research Directions

- **Open problem — authorization under capability discovery:** Skilder reports no unauthorized governed calls in its tested setting, but discovery-protocol failures remain part of task-pass losses. A useful follow-up is adversarial testing across long-lived sessions, changing role policies, compromised skills, and multi-tenant tool servers.
- **Open problem — exactly-once guarantees under unbounded delay:** LIMBO’s analysis says verification-only policies cannot guarantee exactly-once behavior under late commits without a bound on in-flight time. Follow-up work should test standardized idempotency-key and transaction protocols under heavier-tailed delays and partial-batch failures.
- **Open problem — credit assignment outside simulators:** SLCA-GRPO’s gains use a schema-guided simulator. The next test is transfer to real APIs with authentication, rate limits, mutable state, and tool schemas not seen during training.
- **Open problem — benchmark realism and coverage:** Synthetic Hospital and PROOF improve observability, but synthetic or frozen knowledge can miss real distribution shift. Research should pair them with privacy-preserving real-data audits and longitudinal, intervention-based evaluation.
- **Research direction — joint reliability training:** DEEPO, SLCA-GRPO, and IterSynth suggest combining uncertainty-aware correction, segment/role-specific rewards, and verifiable tool outcomes in one agent-training loop. This is a proposed synthesis, not a result established by these papers.

## Takeaway
The batch’s clearest pattern is practical: reliable AI agents need enforceable tool contracts, better credit assignment, and benchmarks with observable ground truth. The papers are very recent preprints, and the main “hotness” signal is a same-day curated shortlist rather than citations, downloads, or an official arXiv ranking; treat the empirical claims as promising but preliminary.

## Method and sources

- **Window:** daily; latest available arXiv announcement batch was 2026-09-25, used because the 2026-09-26 batch was not available at the 2026-09-26 15:10 UTC snapshot.
- **Snapshot:** 2026-09-26 15:10 UTC.
- **Scope:** AI-relevant papers across cs.AI, cs.LG, stat.ML, cs.CL, cs.CV, cs.RO, cs.NE, and cs.MA; this report selected papers surfaced in the 2026-09-25 Paper Radar digest, which states that it reviewed 312 papers and shortlisted 63, including 28 must-read papers.
- **Ranking:** inferred from the Paper Radar shortlist scores/labels, technical relevance, recency, cross-category reach, and reported evaluation detail. arXiv has no official trending chart. Paper Radar percentages are explicitly model-interest probabilities, not quality scores. Semantic Scholar was checked where available; only PROOF returned a usable result in this snapshot (0 citations, 0 influential citations), and no citation totals are interpreted as period gains.
- **Sources:** arXiv abstract pages linked in each entry; [Paper Radar — 2026-09-25](https://eliot5566.github.io/JEV-Paper-Radar/public/ai/); Semantic Scholar Graph API for the PROOF citation check.
