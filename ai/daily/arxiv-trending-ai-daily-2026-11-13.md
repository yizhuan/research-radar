# arXiv AI papers — Friday, 13 November 2026

Five notable papers from the latest announcement batch, with a strong thread around agentic systems that must select, verify, or efficiently execute their own work. In this briefing: verifier-aware reinforcement learning, machine-learning agents searching semi-supervised pipelines, AI peer-review audits, agent execution infrastructure, and pixel-space video generation. arXiv has no official trending chart; this ordering is inferred from visible independent coverage, conference signals, cross-list breadth, and released artifacts. These papers are only about two days old, so citation evidence is limited and does not establish readership or popularity.

This is the prior announcement batch: Saturday, 14 November had no newer daily batch at the 17:05 UTC snapshot, so the report uses Friday, 13 November 2026.

## Top papers (ranked)

### 1. [Negative-Only Policy Optimization for One-Sided Verifiable Rewards](https://arxiv.org/abs/2611.17287)
- **Abstract:** The paper formalizes one-sided verifiability, where a verifier can reliably reject failures but cannot certify positives, and proposes NOPO, which learns by suppressing trusted negatives; reported experiments improve pass@k across code, logic, and math tasks.
- **Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
- **arXiv:** `2611.17287v1` (published 2026-11-12 18:52:33 UTC; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** Accepted as a NeurIPS 2026 Spotlight; cross-listed in two core AI categories; received independent paper write-ups/listings, including OpenTrain and AI Safety Hot. Semantic Scholar listed 0 citations when checked; that is an early total, not a period gain.
- **Claimed contribution:** The authors propose reference-relative negative suppression plus a group-level update adapter, and report better pass@k under unit-test, constraint-check, and LLM self-verifiers when oracle rewards are unavailable (arXiv abstract).
- **Caveat:** Evidence is limited to the paper's reported code, logic, and math benchmarks and its one-sided-verifier setup; the abstract does not establish results in broader deployed settings.
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Training & adaptation; Evaluation & benchmarks; Safety & alignment

### 2. [AgentSSL: Can MLE Agents Leverage Unlabeled Data?](https://arxiv.org/abs/2611.17323)
- **Abstract:** AgentSSL treats semi-supervised learning as agentic program search and reports that agent-generated pipelines beat human-engineered baselines in 8 of 12 settings, while program selection can erase gains and is tested with a 16,977-program benchmark.
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **arXiv:** `2611.17323v1` (published 2026-11-12 18:59:06 UTC; categories: `cs.AI`, `cs.LG`)
- **Evidence for ranking:** NeurIPS 2026 paper and conference poster; cross-listed in two core categories; received independent analyses from BedrockNews, EigenRadar, and other research roundups. Those write-ups converge on the program-selection bottleneck, rather than providing a popularity metric.
- **Claimed contribution:** The authors frame semi-supervised learning as program search, introduce ProgramSelectBench, and report gains over human-engineered baselines in 8 of 12 controlled settings (arXiv abstract and paper text).
- **Caveat:** The authors report that AgentSL matches AgentSSL on both ecology tasks and say the search is biased toward SSL; selecting programs without reliable labels remains unresolved (paper discussion).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Agents & reasoning; Data & synthetic data; Evaluation & benchmarks

### 3. [Auditing AI peer reviewers: a benchmark on real scientific papers](https://arxiv.org/abs/2611.17052)
- **Abstract:** The authors inject objective errors into real papers to measure reviewer detection and false positives, and introduce Skepthical, a tool-using multi-agent reviewer; across 30 papers and 357 injected errors, model choice and task-specific tools materially affect detection.
- **Authors:** Íñigo Zubeldia, Boris Bolliet, Francisco Villaescusa-Navarro, Pablo Villanueva-Domingo, Miles Cranmer
- **arXiv:** `2611.17052v1` (published 2026-11-12 16:33:51 UTC; categories: `cs.CL`, `astro-ph.IM`, `cs.AI`, `cs.DL`)
- **Evidence for ranking:** Accepted at NeurIPS 2026; spans three core AI categories plus digital libraries; independently summarized by Bharat Hunt, Foorilla, and arXiv.deeppaper. Citation momentum is not established for this very recent paper.
- **Claimed contribution:** The authors provide an error-injection evaluation pipeline and Skepthical, which combines citation retrieval, computer algebra, and executed code for checking specific claims (arXiv abstract and paper text).
- **Caveat:** The authors explicitly say the benchmark measures localized objective defects, not holistic review quality; each field corpus contains only 15 papers, and the human adjudication check is limited (paper limitations).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Safety & alignment

### 4. [Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon](https://arxiv.org/abs/2611.17294)
- **Abstract:** Metal Sandbox provides isolated native macOS execution and command scheduling across Macs for GPU coding agents; experiments on four Mac mini M4 nodes report higher command throughput under concentrated demand and lower waiting in fixed-trace scheduling replays.
- **Authors:** Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang, et al.
- **arXiv:** `2611.17294v1` (published 2026-11-12 18:54:42 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.DC`)
- **Evidence for ranking:** Cross-listed in three core AI categories and distributed computing; code and Harbor integration are public; the paper has independent technical listings including arXivLens and Papers.cool. These are breadth and availability signals, not measured readership; citation evidence is sparse.
- **Claimed contribution:** The authors combine per-instance file restrictions, native command execution, and cross-Mac scheduling, reporting 1.68×–2.05× throughput in concentrated-demand tests and an 18.8% mean-wait reduction in fixed-trace replay (arXiv abstract and paper text).
- **Caveat:** The authors state that the system is not hostile multi-tenant containment and does not guarantee GPU exclusivity; the scheduling replay holds agent behavior and phase durations fixed (paper discussion and limitations).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Efficient inference & systems; Agents & reasoning; Safety & alignment

### 5. [Back to Pixels: Lifting Latent Video Diffusion into Pixel Space](https://arxiv.org/abs/2611.17336)
- **Abstract:** PixVid fine-tunes a pretrained latent video diffusion model to generate frames directly in pixel space, and the authors report higher-resolution output at the same per-frame token count, improved fast-motion control alignment, and frame-level response to actions.
- **Authors:** Yanke Song, Shuo Chen, Chris Rockwell, Guande He, Nan Liu, et al.
- **arXiv:** `2611.17336v1` (published 2026-11-12 18:59:55 UTC; categories: `cs.CV`)
- **Evidence for ranking:** The paper has a project page, independent technical summaries including AGI Hunt and Paperium, and a public author announcement. It is a useful signal from the vision category, but has no core-category cross-list or citation momentum confirmed in this snapshot.
- **Claimed contribution:** The authors replace the VAE output path with a framewise pixel-space design and report competitive VBench quality after fine-tuning from Wan2.1-14B (arXiv abstract and paper text).
- **Caveat:** The authors report 3.9× as many tokens per second of video as Wan2.1 at 480×832, making short low-resolution clips more expensive (paper conclusion).
- **Announcement type:** new submission, 13 November 2026 announcement batch
- **Themes:** Multimodal & vision-language; Efficient inference & systems; Training & adaptation

## Trending Research Themes

- **Agents are becoming pipelines, not just chat interfaces.** AgentSSL searches executable ML programs; Metal Sandbox provides native tooling and scheduling for coding agents; Skepthical delegates review checks to retrieval, code, and algebra tools. Their shared emphasis is on observable intermediate work, not simply a stronger base model.
- **Selection and verification are the bottlenecks.** AgentSSL finds program discovery easier than reliable selection; NOPO formalizes a reward setting where positive verification is unavailable; the reviewer benchmark shows detection changes by error type and model. These papers suggest evaluator quality constrains agentic progress, rather than establishing that this capability is solved.
- **Efficiency work is moving across layers.** Metal Sandbox targets execution and GPU utilization for agents, while PixVid changes the video model's output representation to improve resolution and control latency. These are distinct approaches, not evidence of one shared efficiency breakthrough.
- **Corpus concentration:** the announcement pages show the largest daily listings in cs.LG (340 entries) and cs.AI (321), followed by cs.CV (196), cs.CL (135), cs.RO (106), stat.ML (52), cs.MA (18), and cs.NE (14). Category totals overlap because of cross-listing; the selected set is not a field-wide popularity ranking.

## Open Problems and Research Directions

- **Open problem — selecting good agent-generated programs with weak labels.** AgentSSL reports selection losses up to 47% and says its ecological tasks do not establish an advantage over the supervised alternative. **Research direction:** compare active-label allocation, unsupervised selection, and supervised search under equal label and compute budgets across additional program families and real-world domains. [AgentSSL](https://arxiv.org/abs/2611.17323)
- **Open problem — measuring review quality beyond injected defects.** The peer-review benchmark excludes novelty, significance, missing controls, and interpretive judgment, and uses small field-specific corpora. **Research direction:** test larger, more diverse paper sets with blinded human assessment and separately score localized checks and holistic review judgments. [Auditing AI peer reviewers](https://arxiv.org/abs/2611.17052)
- **Open problem — generalizing scheduling and isolation claims beyond the tested Macs and fixed traces.** Metal Sandbox reports four-node experiments, while its replay fixes model behavior and phase durations and does not promise GPU exclusivity. **Research direction:** run live, multi-hardware trials with competing workloads, security threat models, and end-to-end training outcomes. [Metal Sandbox](https://arxiv.org/abs/2611.17294)
- **Open problem — the token and compute cost of pixel-space video at lower resolutions.** PixVid reports more tokens per second at 480×832 even while improving frame-level control and scaling. **Research direction:** measure quality, latency, and energy across resolutions and clip lengths under matched compute, including adaptive latent/pixel modes. [Back to Pixels](https://arxiv.org/abs/2611.17336)

## Takeaway

Today's batch suggests a practical turn toward agent systems whose reliability depends on selection, verification, and execution infrastructure. The papers offer useful benchmarks and system-specific gains, but their settings are narrow and very recent; independent citation or usage evidence is not yet enough to call them broadly established trends.

## Method and sources

- **Window:** daily; the Friday 13 November 2026 arXiv announcement batch (batch-date window 2026-11-13 00:00–23:59 UTC). Snapshot: 2026-11-14 17:05:13 UTC. Saturday had no newer announcement batch, so this uses the prior Friday batch.
- **Corpus:** core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`. The recent pages were checked for all eight categories; the pages show the Friday batch.
- **Candidate retrieval:** arXiv recent-category listings and verified abstract pages for all five selected papers. The broad arXiv API query was not available at this snapshot (HTTP 429), so listings were consulted in the browser. All five abstracts were read; HTML full text was also checked for AgentSSL, the reviewer benchmark, Metal Sandbox, and PixVid. NOPO's abstract page was available, but its HTML full text was not.
- **Inference method:** arXiv publishes no official trend ranking. Ranking is qualitative: independent, checkable coverage and visible conference signals first; cross-list breadth and public project/code artifacts next; recency only as a tie-breaker. This is a notable-paper shortlist, not a claim about reads, downloads, or comprehensive category coverage. Semantic Scholar returned a current citation total of 0 for NOPO; further paper lookups were rate-limited, so no citation-velocity comparison is made.
- **Primary sources:** [cs.AI recent](https://arxiv.org/list/cs.AI/recent), [cs.LG recent](https://arxiv.org/list/cs.LG/recent), [stat.ML recent](https://arxiv.org/list/stat.ML/recent), [cs.CL recent](https://arxiv.org/list/cs.CL/recent), [cs.CV recent](https://arxiv.org/list/cs.CV/recent), [cs.RO recent](https://arxiv.org/list/cs.RO/recent), [cs.NE recent](https://arxiv.org/list/cs.NE/recent), [cs.MA recent](https://arxiv.org/list/cs.MA/recent).
- **Paper sources:** [NOPO](https://arxiv.org/abs/2611.17287), [AgentSSL](https://arxiv.org/abs/2611.17323), [AI peer-review benchmark](https://arxiv.org/abs/2611.17052), [Metal Sandbox](https://arxiv.org/abs/2611.17294), [PixVid](https://arxiv.org/abs/2611.17336).
- **Corroborating sources:** [NeurIPS AgentSSL poster](https://neurips.cc/virtual/2026/poster/154115), [Metal Sandbox GitHub](https://github.com/WangHaoZhe/metal-sandbox), [OpenTrain NOPO summary](https://www.opentrain.ai/papers/negative-only-policy-optimization-for-one-sided-verifiable-rewards--arxiv-2611.17287/), [AI Safety Hot NOPO listing](https://aisafetyhot.com/en/items/cgbphixwfsx7gxx5n9qnovsl5), [BedrockNews AgentSSL analysis](https://bedrocknews.com/article/arxiv/2611.17323v1), [EigenRadar AgentSSL brief](https://eigenradar.com/en/ai/briefs/2026-11-13/agentssl-program-selection/), [Bharat Hunt reviewer-benchmark summary](https://bharathunt.org/ai/auditing-ai-peer-reviewers-a-benchmark-on-real-scientific-papers), [Foorilla reviewer-benchmark summary](https://foorilla.com/research/papers/auditing-ai-peer-reviewers-a-benchmark-on-real-scientific-papers-403717/), [AGI Hunt PixVid summary](https://agihunt.info/en/papers/2611.17336), [Semantic Scholar NOPO record](https://www.semanticscholar.org/paper/2135404e97888284c3ac6604b4d35b706f1141c8).
