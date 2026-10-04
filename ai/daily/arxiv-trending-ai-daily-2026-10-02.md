# arXiv AI: latest batch — Friday, 2 October 2026

Five notable papers span research-retrieval benchmarks, visual and enterprise agents, cybersecurity tool use, and embodied robotics. The thread to listen for is a move from testing model answers to testing whether an agent can find, remember, and act on the right information. This is an evidence-weighted shortlist, not a true popularity chart: arXiv has no official trending chart, and citation/attention evidence is especially thin for papers announced only two days ago.

Window: daily latest announcement batch, 2 October 2026 (the most recent batch; no newer weekend batch appeared). Snapshot: 2026-10-04 00:10:11 UTC.

## Top papers (ranked)

### 1. [KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards](https://arxiv.org/abs/2610.02206)
- **Abstract:** Introduces a benchmark of 8,504 natural-language-to-command examples across 1,642 Kali Linux tools and reports that no tested open-weight model exceeded 42% exact-command accuracy in the unrestricted setting.
- **Authors:** Pengfei Li, Naufal Suryanto, Sicheng Zhang, Muzammal Naseer
- **arXiv:** `2610.02206v1` (published 2026-10-01 17:59:55 UTC; categories: `cs.CL`, `cs.AI`, `cs.CR`)
- **Evidence for ranking:** Accepted to the NeurIPS 2026 Evaluations and Datasets Track; arXiv links a project page and code; cross-listed across language, AI, and security.
- **Claimed contribution:** The authors combine canonicalized command evaluation, sandboxed execution and human review, then use the resulting checks to construct runtime-free verifiable rewards; they report gains from SFT and RLVR for an 8B model.
- **Caveat:** The paper identifies single-turn command generation and documentation-grounded data as limitations; multi-step workflows and environment-aware use remain open.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Safety & alignment

### 2. [VISTA: A Visual Harness for Reasoning in an Interactive World](https://arxiv.org/abs/2610.02200)
- **Abstract:** Presents a visual harness that lets a multimodal model retain, retrieve, and reorganize original visual observations for long-horizon interaction; the authors report improved results on ARC-AGI-3 and three other game/puzzle benchmarks.
- **Authors:** Qiushi Han, Keya Hu, Linlu Qiu, Cathy Wu, Kaiming He
- **arXiv:** `2610.02200v1` (published 2026-10-01 17:59:45 UTC; categories: `cs.AI`, `cs.CV`)
- **Evidence for ranking:** Cross-listed in AI and vision; the arXiv record notes an earlier August 2026 version, and the authors provide a project site and code. The reported perfect ARC-AGI-3 score is on all 25 public games, not a popularity measure.
- **Claimed contribution:** The authors attribute the gains to lossless visual memory and active retrieval, reporting a Relative Human Action Efficiency score rising from 40.68 to 100 for Claude Opus 5.0 on ARC-AGI-3.
- **Caveat:** The paper calls for evaluation on more complex, realistic tasks, including embodied settings; current evidence centers on games and puzzles.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Multimodal & vision-language; Agents & reasoning; Evaluation & benchmarks

### 3. [ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research](https://arxiv.org/abs/2610.02202)
- **Abstract:** Builds a research-paper retrieval benchmark from judgments by 184 lead authors on 207 projects, and finds that agentic search does not outperform embedding retrieval at Recall@20 in the reported setup.
- **Authors:** Sohyeon Kim, Yoonho Lee, Bo Liu, Dayoon Ko, Rulin Shao et al.
- **arXiv:** `2610.02202v1` (published 2026-10-01 17:59:47 UTC; categories: `cs.AI`, `cs.CL`, `cs.IR`)
- **Evidence for ranking:** Broad cross-listing across AI, language, and information retrieval; the author-annotated benchmark covers 207 projects and a 191K-paper corpus, giving the work a directly testable scientific-agent task.
- **Claimed contribution:** The authors introduce author-provided “catalyst paper” judgments and report Recall@20 of 0.42 for agentic search versus 0.48 for embedding retrieval, with their strongest tested agent at 0.51.
- **Caveat:** The paper says its 2025–2026 computer-science projects are unevenly represented across areas and that retrospective author labels are subject to hindsight.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Retrieval & knowledge; Evaluation & benchmarks; Agents & reasoning

### 4. [Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows](https://arxiv.org/abs/2610.02122)
- **Abstract:** Introduces 210 data-science and analytics tasks in a simulated enterprise warehouse with 235 tables and 7.5 billion rows, grading agents on downstream actions as well as analysis; the strongest of 14 tested models averages 59.5 points.
- **Authors:** Gabriel Tomitsuka, Arman Raayatsanati, Emma Xing, Duke Gand, Joseph J Ma
- **arXiv:** `2610.02122v1` (published 2026-10-01 17:35:44 UTC; categories: `cs.CL`, `cs.AI`, `cs.DB`)
- **Evidence for ranking:** Cross-listed across language, AI, and databases; a project page, code, and data are linked from the paper, and its consequence-based grading extends beyond text-to-SQL.
- **Claimed contribution:** The authors build a simulated New York food-delivery company and score actions against hidden simulator state; they report that only 34.8% of tasks receive a score of at least 95 from the strongest model.
- **Caveat:** The evaluation is based on a constructed food-delivery scenario and simulated warehouse, so transfer to live enterprise systems is not established by this benchmark alone.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Retrieval & knowledge

### 5. [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.02204)
- **Abstract:** Proposes a weight-frozen robot-improvement loop that diagnoses offline data, practices related skills in simulation, and revises reusable skills and prompts; the authors report results on 22 manipulation tasks and 30 physical trials.
- **Authors:** Yen-Jen Wang, Haozhe Jiang, Shuying Deng, Haoru Xue, Weirui Ye et al.
- **arXiv:** `2610.02204v1` (published 2026-10-01 17:59:50 UTC; categories: `cs.RO`, `cs.AI`, `eess.SY`)
- **Evidence for ranking:** Cross-listed in robotics, AI, and systems/control; the abstract reports both held-out simulation evaluation and real-robot trials, making it a concrete embodied-agent result within this batch.
- **Claimed contribution:** The authors report increasing success on 22 held-out manipulation tasks from 28.6% after the first practice round to 95.0% after 15 rounds, then success in 30 physical trials across three tasks.
- **Caveat:** Physical validation is limited to 30 trials on three tasks; broader hardware, task, and environment generalization remains unshown in the abstract.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Robotics & control; Agents & reasoning; Training & adaptation

## Trending Research Themes

- **Evaluation is shifting toward consequential, multi-step work.** KaliBench checks executable CLI commands; Argo-Bench scores simulated business actions; ScholarCatalyst asks whether retrieval surfaces work that could actually inform a research project. All three expose capability gaps that answer-only tests can miss.
- **Agent scaffolds are becoming research objects in their own right.** VISTA studies visual memory and retrieval without changing the underlying model, while the robotics paper practices and revises skills and prompts rather than model weights. These are distinct methods, but both test whether better context and control loops unlock latent capability.
- **Embodied and specialized tool use remain difficult to generalize.** VISTA's game results, the robot trials, and KaliBench's exact-command results are promising within their tested settings; none alone establishes broad real-world reliability.

## Open Problems and Research Directions

- **Open problem — retrieval quality and label coverage:** ScholarCatalyst reports uneven subject coverage and retrospective labels; its best reported Recall@20 is still 0.51. A useful next test is prospective annotation across underrepresented CS areas, with agreement checks and held-out time periods.
- **Open problem — beyond single-turn tool calls:** KaliBench explicitly centers single-turn command generation and documentation-grounded examples. Extend it to multi-step, stateful workflows with retrieval and environment feedback, then measure whether gains survive unseen tools and changed system state.
- **Open problem — realism and transfer:** Argo-Bench uses one simulated enterprise domain, VISTA emphasizes games/puzzles, and the robotics paper has only 30 physical trials across three tasks. Follow-up studies should add multiple domains and hardware, report failure rates, and test transfer without task-specific recalibration.

## Takeaway

This batch's clearest common signal is evaluation moving from isolated answers to full loops: retrieve relevant work, preserve useful observations, issue valid tools, and see whether actions help. The results are promising but narrow; prospective tests, new domains, and independent replication matter more than the headline scores.

## Method and sources

Daily window: latest arXiv announcement batch published Friday 2026-10-02; the current UTC date was Sunday 2026-10-04, so the report uses the prior batch. Snapshot: 2026-10-04 00:10:11 UTC. Candidate coverage checked the recent listings for `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; the ordering is inferred, not supplied by arXiv. Since these submissions were only days old, citation and independent-attention evidence was insufficient for a popularity ranking; cited totals are not used. Selection favors checkable peer-review/artifact signals, cross-category relevance, and concrete evaluation rather than recency alone. Paper claims and caveats were checked against arXiv abstracts; full text was inspected for the first three papers.

Recent-category listings: [cs.AI](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), [cs.MA](https://arxiv.org/list/cs.MA/recent). Individual arXiv abstract links are attached to each title. KaliBench's NeurIPS acceptance and code/project links appear on its [arXiv record](https://arxiv.org/abs/2610.02206).
