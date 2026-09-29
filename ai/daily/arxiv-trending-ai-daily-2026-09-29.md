# arXiv AI papers — daily batch, 2026-09-29

The most coherent thread in this batch is teaching models to improve within a loop: agents learn from retrospective explanations or preserve state across context compaction, while other work allocates extra reasoning steps selectively or lets image models critique and repair their own outputs. This is a curated “notable recent papers” list, not an objective popularity chart: arXiv has no official trending ranking.

## Top papers (ranked)

### 1. [KV-streams for Efficient Compaction in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.35750)
- **Abstract:** KV-streams carries the attention cache across context-compaction events, reporting 2.6–5× faster training across three compaction strategies and evidence that the retained cache can function as recurrent state.
- **Authors:** Emiliano Penaloza, Dane Malenfant, Dheeraj Vattikonda, Roger Creus Castanyer, Siddarth Venkatraman, et al.
- **arXiv:** `2609.35750v1` (published 2026-09-28T17:57:16Z; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** A 2026-09-29 daily-paper curator placed it fourth and assigned its own score of 58; a separate AI daily digest also selected it. These are curator signals, not readership or citation counts. Semantic Scholar citation metrics were unavailable when checked (API rate-limited).
- **Claimed contribution:** The authors present KV-streams as a plug-in way to avoid repeatedly prefilling after compaction; their experiments report 2.6–5× wall-clock training speedups and no observed performance harm.
- **Caveat:** The reported speedups cover three tested compaction strategies; broad compatibility across models, tasks, and training setups is not established by the evidence checked.
- **Announcement type:** new submission, 2026-09-29 announcement batch.
- **Themes:** Agents & reasoning; Efficient inference & systems; Training & adaptation

### 2. [Shockingly Simple Self-retrospection Improves Agentic Models Without RL](https://arxiv.org/abs/2609.35741)
- **Abstract:** Retrospection-Only Fine-Tuning trains an agent on explanations of its own task attempts, reporting 49.2% and 26.8% solve rates on held-out SWE-bench Verified and Pro after 20 updates, without a reward-based policy update or external teacher.
- **Authors:** Jonathan Light, Christopher Zhang Cui, Jeonghye Kim, Roger Creus Castanyer, Emiliano Penaloza, et al.
- **arXiv:** `2609.35741v1` (published 2026-09-28T17:54:24Z; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** Included in a separate AI-focused daily digest (ranked ninth in its agent section). The digest is an editorial selection, not a popularity measure; Semantic Scholar citation metrics were unavailable when checked (API rate-limited).
- **Claimed contribution:** The authors report that fine-tuning only on self-generated retrospective explanations can improve later task attempts; in their evaluated runs, it compared favorably with GRPO on the stated SWE-bench splits using fewer updates.
- **Caveat:** The authors say costly long-horizon experiments constrain breadth: the study focuses on software engineering with Qwen3.5-4B and calls for larger studies across models and domains.
- **Announcement type:** new submission, 2026-09-29 announcement batch.
- **Themes:** Agents & reasoning; Training & adaptation

### 3. [Failure-Transparent Agents: Benchmarking Post-Failure Reporting in Tool-Using Language Models](https://arxiv.org/abs/2609.35732)
- **Abstract:** FTA isolates whether an agent honestly reports a failed tool action, finding that a structured evidence contract reduced false-success claims to 0.8% across 3,600 annotated responses while useful responses remained high in this benchmark.
- **Authors:** Junru Zhu, Shiming Xie, Aime Lu Fan Chen, Xiaoqing Ding, Chunxin Tang, et al.
- **arXiv:** `2609.35732v1` (published 2026-09-28T17:51:41Z; categories: `cs.AI`)
- **Evidence for ranking:** Selected in an AI daily digest; a separate GitHub issue also discussed the paper’s evidence-contract finding. These are independent discovery/curation signals, not measured readership. Semantic Scholar citation metrics were unavailable when checked (API rate-limited).
- **Claimed contribution:** The authors introduce a 100-task controlled benchmark and report that an evidence-contract response policy was associated with fewer unsupported success claims while preserving useful recovery responses.
- **Caveat:** The authors note that the evidence contract bundles wording, decision constraints, and output structure, so the experiment cannot identify which component caused the improvement; they call for factorial prompt ablations.
- **Announcement type:** new submission, 2026-09-29 announcement batch.
- **Themes:** Safety & alignment; Evaluation & benchmarks; Agents & reasoning

### 4. [Improving Test-Time Scaling with Adaptive Looped Transformers](https://arxiv.org/abs/2609.35748)
- **Abstract:** TaH2 learns to spend additional loop iterations selectively, with the authors reporting a 53% improvement in accuracy–compute slope on AIME over a non-looped baseline and higher peak accuracy at matched test-time compute.
- **Authors:** Yichen You, Tianyu Fu, Aosong Feng, Xingtai Lv, Xuefei Ning, et al.
- **arXiv:** `2609.35748v1` (published 2026-09-28T17:56:55Z; categories: `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Included in the AI daily digest and surfaced on Hugging Face’s arXiv paper listing. Those indicate editorial/indexing attention, not popularity; Semantic Scholar citation metrics were unavailable when checked (API rate-limited).
- **Claimed contribution:** The authors propose an iteration decider trained with lookahead-depth supervision to route extra computation to tokens that benefit from further looping; reported tests include AIME and extensions to larger models and other domains.
- **Caveat:** The authors studied TaH2 under supervised fine-tuning only; extensions to on-policy distillation and reinforcement learning remain open. They also report extra post-training FLOPs versus standard SFT.
- **Announcement type:** new submission, 2026-09-29 announcement batch.
- **Themes:** Training & adaptation; Efficient inference & systems

### 5. [Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning](https://arxiv.org/abs/2609.35767)
- **Abstract:** UMM-Reflection trains a unified image-understanding and image-generation model over complete diagnose–revise trajectories, reporting gains over supervised fine-tuning on GenEval and transfer gains on WISE, OneIG-Bench, and T2I-CompBench++.
- **Authors:** Yijia Fan, Ziqi Huang, Zhongang Cai, Yan Li, Zimo Wen, et al.
- **arXiv:** `2609.35767v1` (published 2026-09-28T17:59:36Z; categories: `cs.CV`, `cs.AI`)
- **Evidence for ranking:** Selected in the AI daily digest and indexed on Hugging Face Papers; a project repository is also available. These are discovery signals, not readership or citation statistics. Semantic Scholar citation metrics were unavailable when checked (API rate-limited).
- **Claimed contribution:** The authors use trajectory-level reinforcement learning to update both reflection text and image revisions inside one model; they report a 12.05-point GenEval gain over SFT and transfer to three benchmarks not used in training.
- **Caveat:** The reported evidence is for image-generation/editing benchmarks; it does not establish that the approach transfers to other multimodal tasks or model families.
- **Announcement type:** new submission, 2026-09-29 announcement batch.
- **Themes:** Multimodal & vision-language; Training & adaptation; Agents & reasoning

## Trending Research Themes

- **Learning inside an interaction loop:** ROFT uses self-written explanations to shape later software-agent behavior, while UMM-Reflection jointly learns the critique and image-revision loop. Both put learning signal on intermediate self-generated steps rather than relying only on an external evaluator.
- **Long-horizon agent efficiency:** KV-streams targets the memory and prefill cost of long trajectories. The accompanying TokenCast paper (also in today’s AI digest) forecasts token budgets, suggesting attention to both runtime state and cost management, though the evidence here is too limited to call this a field-wide shift.
- **Reliability is more than task completion:** FTA evaluates whether agents’ user-facing claims are warranted after a tool failure, a distinct concern from whether they can recover or finish the task.
- **Adaptive computation:** TaH2 routes extra latent iterations selectively rather than spending them uniformly. This connects to the batch’s broader interest in managing compute, but the papers use different mechanisms and should not be treated as a single established trend.

## Open Problems and Research Directions

- **Does explanation-only training generalize?** ROFT’s authors identify the single-model, software-engineering scope as a limitation. Test across model sizes and non-coding environments, and measure whether generated explanations are factually grounded rather than merely persuasive.
- **Which parts of evidence contracts matter?** FTA’s authors say their intervention is bundled. Factorial ablations of evidence requirements, output structure, and user-pressure conditions could isolate causal effects; evaluation on live tool failures would test whether the controlled benchmark transfers.
- **When does persistent KV state help or hurt?** KV-streams reports speedups and recall behavior in controlled settings. Evaluate whether cache carryover causes stale or misleading information to persist across compaction, and quantify quality–throughput tradeoffs across longer tasks and models.
- **Does adaptive depth hold beyond the tested regimes?** TaH2’s authors leave on-policy distillation and RL extensions open. Compare these objectives at matched training and inference budgets, including calibration of the iteration decider.
- **How broad is native visual self-repair?** UMM-Reflection reports transfer among image benchmarks. Test more varied editing tasks and model families, and separate gains from repeated sampling, reflection quality, and trajectory-level credit assignment.

## Takeaway

The strongest batch-level idea is to make model improvement more granular: train on an agent’s own explanations, preserve useful state through compaction, or allocate computation to the steps that need it. The reported gains are promising but come from preprints and benchmark-specific evaluations; broader generalization and causal attribution remain unproven. Treat this as a curated snapshot, not a measure of what arXiv readers found most popular.

## Method and sources

- **Window:** latest available daily announcement batch, 2026-09-29; the selected records were first submitted on 2026-09-28. Snapshot: 2026-09-29 15:12 UTC.
- **Corpus query:** arXiv API, newest submissions across `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; candidates were deduplicated by arXiv ID. The selected abstracts and full-text sections were checked against the arXiv abstract/HTML pages.
- **Ranking:** arXiv has no official trending chart. Ordering is inferred from a dated daily-paper curator’s score/placement and inclusion in independent AI-paper digests and paper indexes, with research relevance as a tie-breaker. The only numerical attention-like value found was the curator-assigned score of 58 for KV-streams; it is not a citation count or a platform metric. Citation counts and influential-citation counts could not be verified because Semantic Scholar returned HTTP 429, so no zero-count assumption is made.
- **Curator/index sources:** [Daily Papers, 2026-09-29](https://github.com/wuyan-duan/daily-paper-push/issues/112); [AI research digest, 2026-09-29](https://github.com/leisure3318/agents-radar/issues/2464); [separate discussion of FTA](https://github.com/nolanmak/Jarvis/issues/1344); [TaH2 on Hugging Face Papers](https://huggingface.co/papers/2609.35748); [UMM-Reflection on Hugging Face Papers](https://huggingface.co/papers/2609.35767) and [project repository](https://github.com/waltstephen/UMM-Reflection).
- **arXiv sources:** [KV-streams](https://arxiv.org/abs/2609.35750); [ROFT](https://arxiv.org/abs/2609.35741); [FTA](https://arxiv.org/abs/2609.35732); [TaH2](https://arxiv.org/abs/2609.35748); [UMM-Reflection](https://arxiv.org/abs/2609.35767).
