# AI papers — arXiv announcement batch, 2 October 2026

Six notable recent papers point to a practical turn in AI: improving agent systems through memory, better evaluation, and tighter interaction with tools or environments. Today: scientific retrieval, cybersecurity tool use, visual reasoning, robot learning, and coding-agent context management. This is an inferred relevance ranking, not an official arXiv trending chart; the papers are only days old, so citation-based momentum is sparse and the ordering is not a popularity measurement.

## Top papers (ranked)

### 1. [ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research](https://arxiv.org/abs/2610.02202)
- **Abstract:** ScholarCatalyst collects author judgments on research-inspiring papers and finds that current retrieval systems recover only about half of those papers in their top 20, with LLM search agents not outperforming embedding retrieval.
- **Authors:** Sohyeon Kim, Yoonho Lee, Bo Liu, Dayoon Ko, Rulin Shao, et al.
- **arXiv:** `2610.02202v1` (published 2026-10-01 17:59:47 UTC; categories: `cs.AI`, `cs.CL`, `cs.IR`)
- **Evidence for ranking:** Cross-listed across AI, language, and information retrieval; the authors link a public dataset and code, and the paper has early independent coverage on [Pith Science](https://pith.science/paper/2610.02202). It is a timely benchmark contribution, not a demonstrated citation leader.
- **Claimed contribution:** The authors introduce a benchmark from 184 lead authors covering 207 recent computer-science projects, with 894 research questions and a 191K-paper retrieval corpus; they report strongest Recall@20 of 0.48 and an agent result of 0.42 when using the same retriever.
- **Caveat:** The authors note that the corpus covers 2025–2026 computer-science papers with uneven subfield representation, and that retrospective author judgments are subject to hindsight.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Retrieval & knowledge; Evaluation & benchmarks; Agents & reasoning

### 2. [KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards](https://arxiv.org/abs/2610.02206)
- **Abstract:** KaliBench evaluates natural-language-to-command generation across Kali Linux tools and reports that no tested open-weight model exceeds 42% exact-command accuracy in the unrestricted setting; training with its rewards improves an 8B model.
- **Authors:** Pengfei Li, Naufal Suryanto, Sicheng Zhang, Muzammal Naseer
- **arXiv:** `2610.02206v1` (published 2026-10-01 17:59:55 UTC; categories: `cs.CL`, `cs.AI`, `cs.CR`)
- **Evidence for ranking:** Cross-listed in AI, language, and security; the arXiv record says it was accepted to the NeurIPS 2026 Evaluations and Datasets Track, and links a public [GitHub project](https://github.com/RISys-Lab/KaliBench) and [Hugging Face paper page](https://huggingface.co/papers/2610.02206). Citation momentum is not established for this new submission.
- **Claimed contribution:** The authors provide 8,504 query-command pairs across 1,642 tools, with manuscript-grounded validation and deterministic scoring, and report fine-tuning gains that bring an 8B model to performance comparable to a 685B MoE model on their evaluation.
- **Caveat:** The authors note that tool manuals and flags change, documentation can be inconsistent, and alias extraction and automated verification are imperfect.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Evaluation & benchmarks; Safety & alignment; Training & adaptation

### 3. [VISTA: A Visual Harness for Reasoning in an Interactive World](https://arxiv.org/abs/2610.02200)
- **Abstract:** VISTA gives a multimodal model long-horizon access to raw visual observations through a retrievable, lossless visual memory; the authors report a perfect score on the 25 public ARC-AGI-3 games and gains on three other visual benchmarks.
- **Authors:** Qiushi Han, Keya Hu, Linlu Qiu, Cathy Wu, Kaiming He
- **arXiv:** `2610.02200v1` (published 2026-10-01 17:59:45 UTC; categories: `cs.AI`, `cs.CV`)
- **Evidence for ranking:** Cross-listed in AI and computer vision, includes a linked [code repository](https://github.com/joshhhhhan/VISTA), and the arXiv comment notes an earlier blog version from August. The result is notable for the benchmark scope, but is not backed here by verified citation momentum.
- **Claimed contribution:** The authors report that Claude Opus 5.0 with VISTA raises ARC-AGI-3 Relative Human Action Efficiency from 40.68 to 100 and completes all 25 public games using 57.4% fewer actions than first-time human participants.
- **Caveat:** The authors cannot rule out benchmark exposure in the models’ training data because the models post-date public benchmark release; they point to evaluation on private or novel games as a stronger generalization test.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Multimodal & vision-language; Agents & reasoning; Evaluation & benchmarks

### 4. [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.02204)
- **Abstract:** RPG iteratively improves a robot’s shared symbolic skills and system prompt through simulation practice without weight updates, reporting 95% success on 22 simulated manipulation tasks after 15 rounds and success on all 30 physical trials across three tasks.
- **Authors:** Yen-Jen Wang, Haozhe Jiang, Shuying Deng, Haoru Xue, Weirui Ye, et al.
- **arXiv:** `2610.02204v1` (published 2026-10-01 17:59:50 UTC; categories: `cs.RO`, `cs.AI`, `eess.SY`)
- **Evidence for ranking:** Cross-listed across robotics, AI, and control; the abstract reports simulation and hardware evaluations rather than a simulation-only result. Its placement reflects methodological relevance to embodied agents, not measured popularity.
- **Claimed contribution:** The authors combine offline-data task selection, simulation-based practice, execution and video-based failure diagnosis, reusable skill revision, and cross-task regression checks; they report improvement from 28.6% to 95.0% success across practice rounds.
- **Caveat:** Physical evidence is 30 trials over three tasks after calibration. The paper also reports failure on its challenging towel-folding setting, indicating that its reusable procedural skills do not yet solve deformable-object state and contact estimation.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Robotics & control; Agents & reasoning; Training & adaptation

### 5. [Agents Are Systems, Not Models: Rethinking Agentic Evaluation](https://arxiv.org/abs/2610.01618)
- **Abstract:** Across four scientific tasks, the study varies agent configuration and finds substantial run-to-run outcome variation, with task information affecting results more than time budget or model size in its experiments.
- **Authors:** Luis Wiedmann, Leander Girrbach, Cordelia Schmid, Zeynep Akata
- **arXiv:** `2610.01618v1` (published 2026-10-01 12:55:07 UTC; categories: `cs.AI`)
- **Evidence for ranking:** The paper provides an unusually concrete, systems-level agent evaluation, with a released benchmark and more than 18,000 trajectories according to its abstract. Independent discussion is visible in a recent [paper analysis](https://www.bloss0m.com/en/paper-reading/83-agents-are-systems-not-models-agentic-evaluation/); no citation-growth signal is claimed.
- **Claimed contribution:** The authors study five configuration dimensions and report that about 54% of outcome variance comes from repeating the same configuration; they also find a dedicated verification tool changes behavior more than a prompt asking for verification.
- **Caveat:** The authors limit their study to four tasks across two scientific domains; memory and multi-agent coordination are not varied, and the prompting-versus-system-design result is demonstrated for verification only.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Safety & alignment

### 6. [AutoCompact: Learning When to Compact Context in Long-Horizon Coding Agents](https://arxiv.org/abs/2610.02163)
- **Abstract:** AutoCompact trains coding agents to decide when and how to compact context, reporting absolute pass-rate improvements of 9.2% on SWE-bench Verified and 5.0% on SWE-PolyBench Verified over its base model.
- **Authors:** Xuan Zhang, Longtao Zheng, Cunxiao Du, Bo An, Xin Dong
- **arXiv:** `2610.02163v1` (published 2026-10-01 17:54:34 UTC; categories: `cs.CL`)
- **Evidence for ranking:** This is a new core-corpus language paper with test results on two repository-level coding benchmarks and a concrete long-horizon agent systems contribution. No independent citation or attention signal was verified, so it is placed as a notable, relevant paper rather than a popularity pick.
- **Claimed contribution:** The authors train context compaction as part of an agent policy using supervised fine-tuning and reinforcement learning, and report gains across evaluated inference budgets with a 256K context window that does not overflow.
- **Caveat:** The authors use 32K-token sequences for reinforcement-learning training, shorter than the 256K evaluation window, and study model-harness co-design within a single scaffold.
- **Announcement type:** new submission, announcement batch 2026-10-02
- **Themes:** Efficient inference & systems; Agents & reasoning; Training & adaptation

## Trending Research Themes

- **Agents are being evaluated and improved as complete systems.** VISTA adds visual memory and reorganization; AutoCompact learns context-management behavior; “Agents Are Systems, Not Models” varies configuration rather than treating an agent as fixed. Together, these focus on harness and runtime behavior, not just backbone capability.
- **Evaluation is moving closer to operational behavior.** KaliBench isolates exact command execution, ScholarCatalyst measures retrieval of ideas that authors say mattered, and the agent-evaluation paper tracks configuration, reliability, cost, and trajectories. These benchmarks expose failure modes that final-answer scores can hide.
- **Embodied and interactive systems are closing the loop with experience.** RPG practices and revises skills in simulation before physical deployment, while VISTA lets a multimodal model revisit visual experience while acting. Both depend on retaining useful state, but their evidence remains bounded by the tested environments and tasks.

## Open Problems and Research Directions

- **Open problem — retrieving useful ideas is not just semantic matching.** ScholarCatalyst reports weak topical similarity and limited top-20 recall, while labels are retrospective author judgments. **Direction:** test candidate-generation methods that combine citation structure, expert feedback, and explicit query-to-paper rationale, with held-out fields and independent annotation to measure transfer.
- **Open problem — command correctness and documentation drift.** KaliBench reports low unrestricted exact-command accuracy, while real CLI manuals can be inconsistent and change over time. **Direction:** rerun the benchmark against versioned tool manuals and real execution environments, separating command syntax, argument semantics, and safe execution.
- **Open problem — benchmark exposure clouds visual-agent generalization.** VISTA’s authors cannot exclude public-game exposure in model training. **Direction:** evaluate on private, procedurally varied, and physically grounded interactive environments with matched model access and action budgets.
- **Open problem — current robot skills struggle with deformable state.** RPG reports towel-folding failure despite gains on rigid-object tasks. **Direction:** add explicit contact/layer-state estimation and expand hardware trials across more object types, tasks, and operators.
- **Open problem — agent configuration effects may not generalize.** The agent-evaluation study covers four tasks and a limited set of system components. **Direction:** replicate configuration sweeps across domains, models, memory policies, and multi-agent settings while reporting variance and cost.
- **Open problem — learned compaction has a train/evaluation context gap and one-scaffold evidence.** AutoCompact trains on 32K sequences and studies a single scaffold. **Direction:** test longer-sequence training and portability to independent agent frameworks, including recovery quality after compaction rather than task success alone.

## Takeaway

The strongest common thread is systems work: remembering the right context, selecting useful prior knowledge, and making tool or environment interactions measurable. The benchmark and task-specific results are promising author-reported evidence, but independent replication and broader out-of-distribution testing are still needed.

## Method and sources

- **Window:** daily; latest arXiv announcement batch available at snapshot time, 2026-10-02 through 2026-10-02 UTC. The selected papers’ arXiv v1 timestamps are on 2026-10-01 UTC; the announcement listing labels the batch Friday, 2 October. No 5 October batch was present in the checked recent listings.
- **Snapshot:** 2026-10-05 00:10:12 UTC.
- **Scope:** recent listings for `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; each selected record was checked on its arXiv abstract page. This is a curated notable-paper selection, not comprehensive coverage of every entry in those large categories.
- **Inference:** no official arXiv trending chart exists. With the selected submissions only days old, citation evidence is limited; order is inferred from cross-category relevance, paper-specific evaluation/contribution, and checkable corroboration such as linked code, datasets, conference reference, or independent discussion. No downloads, reads, or bookmarks are claimed. Semantic Scholar citation metadata could not be retrieved at snapshot time, so no citation counts are reported.
- **arXiv category listings:** [cs.AI](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), [cs.MA](https://arxiv.org/list/cs.MA/recent).
- **Selected abstracts:** [2610.02202](https://arxiv.org/abs/2610.02202), [2610.02206](https://arxiv.org/abs/2610.02206), [2610.02200](https://arxiv.org/abs/2610.02200), [2610.02204](https://arxiv.org/abs/2610.02204), [2610.01618](https://arxiv.org/abs/2610.01618), [2610.02163](https://arxiv.org/abs/2610.02163).
- **External corroboration:** [ScholarCatalyst on Pith Science](https://pith.science/paper/2610.02202), [KaliBench GitHub](https://github.com/RISys-Lab/KaliBench) and [Hugging Face](https://huggingface.co/papers/2610.02206), [VISTA code](https://github.com/joshhhhhan/VISTA), [agent-evaluation discussion](https://www.bloss0m.com/en/paper-reading/83-agents-are-systems-not-models-agentic-evaluation/).
- **Retrieval note:** the Semantic Scholar Graph API did not return metadata (rate limit response); this is why citation counts and momentum are omitted.
