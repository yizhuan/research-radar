# arXiv Trending AI — Friday, 2 October 2026

Seven notable papers from the latest announcement batch, led by practical agent evaluation and tools for keeping agents grounded over long tasks. The scan covers scientific-literature retrieval, cybersecurity commands, enterprise data work, visual memory, coding agents, and robot learning.[9][10][14] This is an inferred shortlist, not an official arXiv trending chart; citation evidence is especially limited for papers announced only yesterday, so the order is not a popularity or readership ranking.

Window: 2026-10-02 through 2026-10-02 (latest batch: Friday, 2 October 2026). Snapshot: 2026-10-03 00:10 UTC.

Batch-date checks: `cs.AI`, `cs.LG`, `stat.ML`.[1][2][3]
`cs.CL`, `cs.CV`, `cs.RO`.[4][5][6]
`cs.NE`, `cs.MA`.[7][8]

## Top papers (ranked)

### 1. [KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards](https://arxiv.org/abs/2610.02206)
- **Abstract:** KaliBench provides 8,504 natural-language-to-command examples across 1,642 Kali tools and reports that no tested open-weight model exceeded 42% exact-command accuracy in its unrestricted setting; the authors also use its deterministic signals to train an 8B model.[10]
- **Authors:** Pengfei Li, Naufal Suryanto, Sicheng Zhang, Muzammal Naseer[10]
- **arXiv:** `2610.02206v1` (published 2026-10-01 17:59:55 UTC; categories: `cs.CL`, `cs.AI`, `cs.CR`)[10]
- **Evidence for ranking:** The arXiv record reports acceptance to NeurIPS 2026’s Evaluations and Datasets Track; the authors link a public repository, and an independent AI Weekly alert also covered the result. These are checkable publication, artifact, and discussion signals—not readership statistics.[10][18][19]
- **Claimed contribution:** The paper introduces a fine-grained, executable benchmark for schema-free cybersecurity CLI use and a multi-stage validation pipeline; the reported experiments show that supervised fine-tuning and verifiable-reward RL improve an 8B model.[10]
- **Caveat:** The authors note that ground-truth commands inherit version drift and inconsistencies from tool manuals, while automated verification and alias extraction can leave residual errors.[10]
- **Announcement type:** new submission, arXiv announcement batch 2026-10-02[10]
- **Themes:** Evaluation & benchmarks; Safety & alignment; Training & adaptation[10]

### 2. [Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows](https://arxiv.org/abs/2610.02122)
- **Abstract:** Argo-Bench evaluates 210 analytics and operations tasks over a simulated enterprise warehouse with 235 tables and 7.5 billion rows, finding that the best of 14 tested models scored at least 95 points on only 34.8% of tasks.[13]
- **Authors:** Gabriel Tomitsuka, Arman Raayatsanati, Emma Xing, Duke Gand, Joseph J Ma[13]
- **arXiv:** `2610.02122v1` (published 2026-10-01 17:35:44 UTC; categories: `cs.CL`, `cs.AI`, `cs.DB`)[13]
- **Evidence for ranking:** The authors provide a public benchmark repository, and the paper received separate coverage from AI Weekly. Its cross-listing and end-to-end task design add relevance, but the coverage is not evidence of broad adoption.[13][22][23]
- **Claimed contribution:** The authors move beyond text-to-SQL by scoring data agents on actions and their consequences in a simulated marketplace, with executable reference solutions for each task.[13]
- **Caveat:** The reported world is one constructed food-delivery marketplace; transfer to other enterprise schemas, domains, and real operational workflows remains unestablished by this evaluation.[13]
- **Announcement type:** new submission, arXiv announcement batch 2026-10-02[13]
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Retrieval & knowledge[13]

### 3. [ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research](https://arxiv.org/abs/2610.02202)
- **Abstract:** ScholarCatalyst collects author judgments from 184 lead authors on 207 research projects and tests whether systems can retrieve earlier papers that could have advanced those projects; the strongest embedding retriever reaches 0.48 Recall@20, while agentic search reaches 0.42.[9]
- **Authors:** Sohyeon Kim, Yoonho Lee, Bo Liu, Dayoon Ko, Rulin Shao et al.[9]
- **arXiv:** `2610.02202v1` (published 2026-10-01 17:59:47 UTC; categories: `cs.AI`, `cs.CL`, `cs.IR`)[9]
- **Evidence for ranking:** The work is cross-listed in AI, language, and information retrieval; its authors publish code and benchmark materials, and the Hugging Face Papers page separately surfaces the new benchmark.[9][16][17]
  Semantic Scholar showed no citations for the checked record; the method section explains why this was not used as a positive signal.[24]
- **Claimed contribution:** The authors propose literature retrieval grounded in researchers’ firsthand judgments of which prior papers could inspire or advance an early-stage project, rather than relying only on topical similarity or citation links.[9]
- **Caveat:** The authors state that the benchmark covers computer science papers from 2025–2026 with uneven field representation and relies on retrospective author judgments that may be affected by hindsight.[9]
- **Announcement type:** new submission, arXiv announcement batch 2026-10-02[9]
- **Themes:** Retrieval & knowledge; Evaluation & benchmarks; Agents & reasoning[9]

### 4. [AutoCompact: Learning When to Compact Context in Long-Horizon Coding Agents](https://arxiv.org/abs/2610.02163)
- **Abstract:** AutoCompact trains coding agents to choose when to compact their context and what state to preserve, reporting absolute pass-rate improvements of 9.2% on SWE-bench Verified and 5.0% on SWE-PolyBench Verified over its base model.[12]
- **Authors:** Xuan Zhang, Longtao Zheng, Cunxiao Du, Bo An, Xin Dong[12]
- **arXiv:** `2610.02163v1` (published 2026-10-01 17:54:34 UTC; categories: `cs.CL`)[12]
- **Evidence for ranking:** The paper has a public project page and code repository, and it surfaced in independent web coverage alongside the new arXiv record. The evidence supports interest in the method, not a measurable readership ranking.[12][20][21]
- **Claimed contribution:** The authors train context management as part of the coding-agent policy, using judge-corrected trajectories for supervised fine-tuning and joint task-success reinforcement learning.[12]
- **Caveat:** The reported evidence is limited to two software-engineering benchmarks and the evaluated coding-agent setup; the abstract does not establish gains for other agent domains or model families.[12]
- **Announcement type:** new submission, arXiv announcement batch 2026-10-02[12]
- **Themes:** Agents & reasoning; Efficient inference & systems; Training & adaptation[12]

### 5. [VISTA: A Visual Harness for Reasoning in an Interactive World](https://arxiv.org/abs/2610.02200)
- **Abstract:** VISTA gives multimodal agents a lossless store of visual observations and tools to retrieve past frames; on ARC-AGI-3 the authors report a score of 100 for Claude Opus 5.0 across all 25 public games and improvements over minimal-harness baselines on three other benchmarks.[11]
- **Authors:** Qiushi Han, Keya Hu, Linlu Qiu, Cathy Wu, Kaiming He[11]
- **arXiv:** `2610.02200v1` (published 2026-10-01 17:59:45 UTC; categories: `cs.AI`, `cs.CV`)[11]
- **Evidence for ranking:** The paper is cross-listed in AI and computer vision, reports evaluation on four benchmark families, and includes a code link. It is a notable technical result, though independent attention and citation momentum were not established in the sources checked.[11]
- **Claimed contribution:** The authors present a visual harness that preserves raw observations and lets a model revisit frames and regions during long-horizon interaction, complementing rather than changing the underlying model.[11]
- **Caveat:** The authors caution that the tested models may have seen the public games during training and recommend evaluation on novel or private games as a stronger generalization test.[11]
- **Announcement type:** new submission, arXiv announcement batch 2026-10-02[11]
- **Themes:** Multimodal & vision-language; Agents & reasoning; Efficient inference & systems[11]

### 6. [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.02204)
- **Abstract:** RPG improves a robot execution system without changing model weights by practicing skills in simulation and retaining validated prompt and skill-library revisions; the authors report success rising from 28.6% to 95.0% over 15 practice rounds on 22 manipulation tasks and success on 30 physical trials across three tasks.[14]
- **Authors:** Yen-Jen Wang, Haozhe Jiang, Shuying Deng, Haoru Xue, Weirui Ye et al.[14]
- **arXiv:** `2610.02204v1` (published 2026-10-01 17:59:50 UTC; categories: `cs.RO`, `cs.AI`, `eess.SY`)[14]
- **Evidence for ranking:** It is cross-listed across robotics, AI, and control, and reports both held-out simulation tasks and physical-robot trials. These are evidence-of-substance signals; no clear citation or independent discussion signal was found for this very recent entry.[14]
- **Claimed contribution:** The authors propose a feedback loop that diagnoses failures, develops or revises reusable symbolic skills and prompts, and cross-task tests changes before reusing them.[14]
- **Caveat:** The physical evaluation covers 30 trials on only three tasks, while the larger improvement is measured on 22 manipulation tasks in simulation; broader hardware transfer is not established by these results.[14]
- **Announcement type:** new submission, arXiv announcement batch 2026-10-02[14]
- **Themes:** Robotics & control; Agents & reasoning; Training & adaptation[14]

### 7. [Trust the Direction, Search the Step: Zero-and-First-Order Methods for LLM Fine-Tuning](https://arxiv.org/abs/2610.02190)
- **Abstract:** ZFO keeps a first-order optimizer’s proposed direction and uses two additional objective evaluations to select a curvature-aware step size, with the authors reporting theoretical convergence guarantees and gains over fixed-step baselines in evaluated settings.[15]
- **Authors:** Cristian McGee, El Houcine Bergou, Aritra Dutta[15]
- **arXiv:** `2610.02190v1` (published 2026-10-01 17:59:28 UTC; categories: `cs.LG`, `math.OC`)[15]
- **Evidence for ranking:** The arXiv record lists NeurIPS 2026 acceptance and a public code link. These provide a publication and reproducibility signal; citation or independent attention data for this fresh preprint were not established.[15]
- **Claimed contribution:** The authors combine first-order direction selection with zeroth-order step search along that direction to adapt step size without a full line search, and present theoretical results plus experiments on language models and datasets.[15]
- **Caveat:** The authors say the preferred local model and effect size depend on the objective; the abstract does not establish that one step-selection rule wins across tasks.[15]
- **Announcement type:** new submission, arXiv announcement batch 2026-10-02[15]
- **Themes:** Training & adaptation; Efficient inference & systems[15]

## Trending Research Themes

- **Agents are being evaluated as complete workflows, not just answer generators.** KaliBench isolates precise tool invocation, Argo-Bench evaluates analysis plus consequential actions, and ScholarCatalyst asks whether a system can find useful prior work.[9][10][13]
- **Harness and memory design are becoming explicit parts of capability.** VISTA keeps raw visual history available for later inspection; AutoCompact learns what textual task state to preserve; RPG iteratively updates reusable skills and prompts after simulated practice.[11][12][14]
- **Benchmarks increasingly expose operational failure modes.** Exact CLI syntax, multi-table warehouse navigation, and retrieving non-obvious scientific references each reveal a gap that a simple single-turn accuracy score can obscure.[9][10][13]
- **Learning signals are tied more closely to verifiable outcomes.** KaliBench derives rewards from command correctness, AutoCompact trains on task success after judged compaction decisions, and RPG retains changes only after cross-task checks.[10][12][14]

## Open Problems and Research Directions

- **Literature retrieval still misses useful but non-obvious connections.** ScholarCatalyst’s authors report limited retrieval recall and no benefit from agentic search over its embedding retriever, while noting that coverage is uneven and judgments are retrospective. A follow-up could test retrieval across older papers and disciplines, with forward-in-time queries and expert annotation designed to separate discoverability from hindsight effects.[9]
- **Tool benchmarks must remain aligned with changing software.** KaliBench’s authors flag manual drift, inconsistent documentation, and incomplete alias coverage. A useful next experiment is versioned evaluation against multiple Kali releases and actual tool execution, reporting separately documentation compliance, exact syntax, and operational safety.[10]
- **Public benchmark success may overstate generalization.** VISTA explicitly notes possible exposure of public games in model training. Testing on private or newly generated visual environments—and then on interactive physical tasks—would better isolate harness gains from benchmark familiarity.[11]
- **Enterprise-agent performance needs broader external validity.** Argo-Bench’s single simulated food-delivery company offers scale and consequential grading, but does not settle transfer to other schemas or live operations. Replication across different industries, warehouse designs, and action-risk levels would test that boundary.[13]
- **Agent self-improvement needs stronger real-world evidence.** RPG’s physical trials are promising but small and limited to three tasks. Larger multi-site trials across robot platforms and task families could measure regressions, recovery costs, and whether simulation-selected skill updates remain safe on hardware.[14]
- **Context-management gains should be stress-tested beyond two coding benchmarks.** AutoCompact reports pass-rate gains on SWE-bench Verified and SWE-PolyBench Verified. Evaluating long tasks with different toolchains, context-window sizes, and failure-recovery costs would show whether learned compaction generalizes rather than overfitting benchmark trajectories.[12]
- **Adaptive step-size methods need comparisons that account for objective-specific behavior.** ZFO’s authors report that results depend on the objective. Follow-up work could compare compute-matched objective-evaluation budgets and robustness across model scales, datasets, and optimizer families.[15]

## Takeaway

This batch’s clearest common thread is infrastructure around agents: memory, tool execution, benchmark realism, and whether actions can be verified.[10][11][14]
The most concrete evidence comes from fresh benchmark results and controlled evaluations, not mature citation signals; replication and transfer beyond the specific test environments remain the key uncertainties.[9][15]

## Method and sources

- **Window and scope:** Daily report for the latest arXiv announcement batch, 2026-10-02. Core corpus: `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`.
- **Category batch check (AI, ML, statistics):** The Oct 2 batch was visible on the recent pages for `cs.AI`, `cs.LG`, and `stat.ML`.[1][2][3]
- **Category batch check (language, vision, robotics):** The same batch appeared for `cs.CL`, `cs.CV`, and `cs.RO`.[4][5][6]
- **Category batch check (neural/evolutionary, multiagent):** The `cs.NE` and `cs.MA` pages showed the same date.[7][8]
- **Abstract verification, first group:** Abstracts checked directly on arXiv.[9][10][11]
- **Abstract verification, second group:** Abstracts checked directly on arXiv.[12][13][14]
- **Abstract verification, final paper:** Abstract checked directly on arXiv.[15]
- **Ranking:** An editorial inference from independently checkable signals including conference acceptance, public code/data, cross-list relevance, external research discussion, and reported evaluation substance. arXiv provides no official trending chart, and this ordering does not claim most-read, most-downloaded, or highest-citation status.
- **Attention and citation limits:** The broad arXiv API request timed out. Semantic Scholar returned one record for ScholarCatalyst with zero citations, zero influential citations, and zero references; subsequent paper lookups were rate-limited, so no cross-paper citation comparison or velocity was used.[24] Since the batch is only one day old, citation evidence is too sparse to identify popularity reliably.
- **Snapshot:** 2026-10-03 00:10:10 UTC.

## Sources

[1] https://arxiv.org/list/cs.AI/recent
[2] https://arxiv.org/list/cs.LG/recent
[3] https://arxiv.org/list/stat.ML/recent
[4] https://arxiv.org/list/cs.CL/recent
[5] https://arxiv.org/list/cs.CV/recent
[6] https://arxiv.org/list/cs.RO/recent
[7] https://arxiv.org/list/cs.NE/recent
[8] https://arxiv.org/list/cs.MA/recent
[9] https://arxiv.org/abs/2610.02202
[10] https://arxiv.org/abs/2610.02206
[11] https://arxiv.org/abs/2610.02200
[12] https://arxiv.org/abs/2610.02163
[13] https://arxiv.org/abs/2610.02122
[14] https://arxiv.org/abs/2610.02204
[15] https://arxiv.org/abs/2610.02190
[16] https://huggingface.co/papers/2610.02202
[17] https://github.com/stanford-iris-lab/ScholarCatalyst
[18] https://github.com/RISys-Lab/KaliBench
[19] https://aiweekly.co/alerts/kalibench-caps-open-models-at-42-on-exact-kali-commands
[20] https://autocompact.github.io
[21] https://github.com/AutoCompact/AutoCompact
[22] https://github.com/TextQLLabs/Argo-Bench
[23] https://aiweekly.co/alerts/argo-bench-top-data-agent-clears-95-on-just-348-of-tasks
[24] https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.02202?fields=title,authors,year,citationCount,influentialCitationCount,referenceCount
