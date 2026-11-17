## Headline

AI across cs.AI and neighboring arXiv fields — 8 highlighted papers from the 2026-11-16 announcement batch, selected from 477 records returned by the configured category/date query. The clearest shared pattern is models being trained or engineered to seek and use evidence in visual, audio, coding, and physical tasks. Agenda: first the most visible agent and robotics work, then model-internal mechanisms and open evaluation questions. This is an inferred ranking: arXiv has no official trending chart, and these papers are so recent that citation evidence is limited.

## Top papers (ranked)

### 1. [ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters](https://arxiv.org/abs/2611.21607)
- **Abstract:** The authors connect a 552B vision-language backbone to an action diffusion transformer and report improved robot sample efficiency, generalization, and real-world charger insertion compared with smaller backbones.
- **Authors:** Ruixi Yu, Dairu Liu, Xuchuan Chen, Zekun Qi, Zekai Li, et al.
- **arXiv:** `2611.21607v1` (published 2026-11-16T18:59:37Z; categories: `cs.RO`)
- **Evidence for ranking:** Contemporaneous technical summaries at [ExplainX](https://explainx.ai/blog/scalevla-552b-vision-language-action-robot-backbone-2026), [Emergent](https://emergent.sh/news/scalevla-552b-robot-model-beats-2b-baseline), and [AI Weekly](https://aiweekly.co/alerts/scalevla-wires-552b-deepseek-v41-flash-backbone-to-robot-policy), as well as a Hugging Face paper listing, make it one of the clearest externally surfaced papers in the batch.
- **Claimed contribution:** The authors introduce ScaleVLA, comparing VLM backbones from 2B to 552B under shared training and reporting improvements on several robot-policy measures.
- **Caveat:** The authors note the 552B setup requires more hardware; the real-world charger result is a small 10-trial comparison.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Robotics & control; Multimodal & vision-language; Training & adaptation

### 2. [ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization](https://arxiv.org/abs/2611.21605)
- **Abstract:** ViRA trains visual agents with contrast sets of near-identical high-resolution images so successful answers depend on reading changed evidence, reporting 63.3% set accuracy versus 59.3% for GRPO at maximum resolution.
- **Authors:** Huawei Lin, Jinting Liu, Tongyan Wang, Xuyang Chen, Ruihua Shi, et al.
- **arXiv:** `2611.21605v1` (published 2026-11-16T18:59:04Z; categories: `cs.CV`, `cs.AI`)
- **Evidence for ranking:** A contemporaneous technical analysis at [BedrockNews](https://bedrocknews.com/article/arxiv/2611.21605v1), the public [project repository](https://github.com/huawei-lin/ViRA), and cross-listing in vision and AI provide checkable visibility and relevance to visual-agent evaluation.
- **Claimed contribution:** The authors propose Cross-Input Relative Policy Optimization (CrossRPO), rewarding success across a contrast set rather than a plausible answer on one image.
- **Caveat:** The authors state the real-photo benchmark has only 78 indoor sets from one camera, the larger benchmark uses edited images, and CrossRPO was tested on one family of base models.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Multimodal & vision-language

### 3. [ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models](https://arxiv.org/abs/2611.21099)
- **Abstract:** ForceHarness gives frozen multimodal models calibrated physical summaries and self-terminating force-control primitives, reporting higher success on a real robot and two simulation benchmarks.
- **Authors:** Ke Sun, Kevin Yuchen Ma, Yike Zhang, Yanzhe Chen, Mike Zheng Shou
- **arXiv:** `2611.21099v1` (published 2026-11-16T13:44:23Z; categories: `cs.RO`)
- **Evidence for ranking:** A robotics explainer at [Physical AI News](https://physicalainews.jp/papers/2611.21099), the [project page](https://showlab.github.io/ForceHarness), and a public [HiddenPhys dataset listing](https://huggingface.co/datasets/Jack97/ForceHarness-Data) provide independent technical visibility and reproducible artifacts.
- **Claimed contribution:** The authors combine force calibration, self-terminating primitives, and physics translation, and introduce HiddenPhys to compare frozen models with force-aware policies and controllers.
- **Caveat:** The authors report that model-call delays prevent reactive coordination, the primitive menu is fixed, and ablations were run only in simulation.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Robotics & control; Agents & reasoning; Efficient inference & systems

### 4. [How VLMs Plan What's Next](https://arxiv.org/abs/2611.21600)
- **Abstract:** Through causal interventions in Qwen3-VL, the authors describe binding, relay, gaze, and language components that select image regions and track progress while generating multi-object descriptions.
- **Authors:** Rohit Gandikota, Arnab Sen Sharma, Adam Belfki, David Bau
- **arXiv:** `2611.21600v1` (published 2026-11-16T18:58:30Z; categories: `cs.CV`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** It is cross-listed in three core AI categories and has a contemporaneous technical summary at [ZeroHour](https://zerohour.day/item/2942510c8e1104575960c141ab1a4813b76d0607) alongside the authors’ [reproduction repository](https://github.com/rohitgandikota/vlm-planning/).
- **Claimed contribution:** The authors identify a causal, modular mechanism for visual selection and progress tracking, tested across input formats, photographs, languages, and Qwen3-VL sizes from 2B to 32B.
- **Caveat:** Central causal tests use a controlled synthetic retrieval task in Qwen3-VL; the paper does not establish that the same mechanism applies to other model families.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Interpretability; Multimodal & vision-language; Agents & reasoning

### 5. [Latent Lattice Language Models](https://arxiv.org/abs/2611.21608)
- **Abstract:** The paper adds recurrent per-layer latent streams that condition a language model’s residual stream and reports lower validation perplexity on FineWeb-Edu than parameter-matched Transformer baselines.
- **Authors:** Shivam Duggal, Zongze Wu, William T. Freeman, Antonio Torralba, Richard Zhang, Eli Shechtman
- **arXiv:** `2611.21608v1` (published 2026-11-16T18:59:38Z; categories: `cs.LG`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The paper spans three core categories and received a contemporaneous technical explainer at [AIModeling](https://www.aimodeling.com/en/news/slug/latent-lattice-language-models-horizontal-latent-perplexity), giving it broader independent visibility than a single-category announcement.
- **Claimed contribution:** The authors introduce persistent horizontal latent states that directly condition attention, KV-cache writes, MLP computation, and decoding, reporting gains across Transformer and state-space variants.
- **Caveat:** The headline evidence is validation perplexity after training on 20B FineWeb-Edu tokens; downstream task performance is not established by the abstract results.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Training & adaptation; Efficient inference & systems

### 6. [FaceJev: Direct Visual Decisions for Face Forgery Detection](https://arxiv.org/abs/2611.21604)
- **Abstract:** FaceJev predicts anomalies in eight facial parts from an MLLM’s answer logits, using PartForensics and FS-GRPO, and reports a 7.25-point gain over the strongest baseline on unseen manipulations.
- **Authors:** Siran Peng, Tianshuo Zhang, Yibo Xue, Ajian Liu, Haoyuan Zhang, et al.
- **arXiv:** `2611.21604v1` (published 2026-11-16T18:59:04Z; categories: `cs.CV`)
- **Evidence for ranking:** A contemporaneous explainer at [Physical AI News](https://physicalainews.jp/papers/2611.21604) and the paper’s explicitly part-labeled dataset provide checkable visibility and substance in the vision batch.
- **Claimed contribution:** The authors contribute direct part-level visual decisions, a dataset of about 160,000 images, and an optimization method that compares each part decision with its alternative.
- **Caveat:** The reported generalization result concerns the manipulation types and image collection evaluated; the abstract does not establish performance across all real-world forgery sources.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Safety & alignment

### 7. [SWE-WhatIf: Simulating Real Users of Coding Agents from Recorded Session](https://arxiv.org/abs/2611.21095)
- **Abstract:** SWE-WhatIf replays coding-agent sessions with an adaptive user simulator grounded in recorded intent, and evaluates it on 89 sessions plus a 16-person study.
- **Authors:** Tae Soo Kim, Tongshuang Wu, Juho Kim
- **arXiv:** `2611.21095v1` (published 2026-11-16T13:42:26Z; categories: `cs.CL`, `cs.AI`, `cs.HC`)
- **Evidence for ranking:** The paper is cross-listed in language, AI, and human-computer interaction and has a contemporaneous [research listing](https://foorilla.com/research/papers/swe-whatif-simulating-real-users-of-coding-agents-from-recorded-session-406092/); the 89-session evaluation is directly relevant to agent assessment.
- **Claimed contribution:** The authors model user intent, satisfaction criteria, and trigger conditions to generate replies that adapt to new agent trajectories rather than replaying fixed dialogue.
- **Caveat:** Evidence is based on 89 recorded sessions and a 16-person study; broader user populations and coding-agent settings are not established by these results.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Evaluation & benchmarks; Agents & reasoning

### 8. [Think2Listen: Evidence-Centric Learning For Agentic Audio Understanding With LALMS](https://arxiv.org/abs/2611.21083)
- **Abstract:** Think2Listen trains audio-language agents to seek discriminative acoustic evidence, revise hypotheses, and decide when to stop, reporting gains on two benchmarks spanning seven audio categories.
- **Authors:** Jin Wang, Liang Lin, Kaiwen Luo, Weiliu Wang, Yuxuan Li, et al.
- **arXiv:** `2611.21083v1` (published 2026-11-16T13:32:21Z; categories: `cs.SD`, `cs.AI`)
- **Evidence for ranking:** It is cross-listed from Sound into `cs.AI`; its two benchmark results make it a relevant example of evidence-seeking agent training. Placement here reflects corpus relevance rather than a popularity measure.
- **Claimed contribution:** The authors propose training credit based on how observations change candidate states, teaching what to ask, how to use returned evidence, and when to stop.
- **Caveat:** The abstract reports results on two benchmarks and seven audio categories; performance outside those settings remains unestablished.
- **Announcement type:** new submission, announcement-batch date 2026-11-16
- **Themes:** Agents & reasoning; Multimodal & vision-language; Evaluation & benchmarks

## Trending Research Themes

- **Agents are being trained to earn answers through evidence, not just outcomes.** ViRA uses contrast sets so a guess cannot solve every image; Think2Listen rewards evidence-seeking and revision; ForceHarness exposes force as calibrated quantities and contact primitives; SWE-WhatIf varies the simulated user’s response with agent behavior. These are related approaches, not one shared method.
- **Embodied AI is moving from semantic perception toward contact-aware control.** ScaleVLA tests whether frontier VLM representations help robot policies, while ForceHarness handles force sensing and low-level contact beneath a frozen model. This is a visible pattern in the selected robotics papers, not proof of a field-wide shift.
- **Multimodal behavior is being probed at mechanism and decision levels.** How VLMs Plan What's Next uses causal patching to identify internal visual-selection components; FaceJev makes facial-part judgments explicit prediction targets; ViRA tests whether an agent reads fine image evidence.
- **Architecture scaling and compute state form a less repeated signal.** Latent Lattice adds persistent per-layer latent streams and reports language-model perplexity gains; it is an individual architecture result in this sample, not a recurring method across the selected papers.
- **The highlighted papers skew toward vision and robotics.** Three are primarily `cs.CV`, two `cs.RO`, and one each `cs.LG`, `cs.CL`, and `cs.SD`; the full query covered all eight configured categories.

## Open Problems and Research Directions

- **ViRA — author-stated:** the real-photo evaluation has only 78 indoor sets from one camera, the larger benchmark uses edited images, and the core models use one base-model family. **Direction:** test across architectures on a larger, diverse photo benchmark with minimal location hints and naturally changing evidence.
- **ForceHarness — author-stated:** model calls take seconds, the primitive menu is fixed, and ablations are simulation-only. **Direction:** measure latency and safety under faster contact changes, then test broader primitives and hardware beyond the reported arm/tasks.
- **ScaleVLA — paper boundary:** the authors report gains with a 552B backbone but note greater hardware needs; the real charger experiment has ten trials. **Direction:** compare success, data efficiency, latency, energy, and hardware cost across more physical tasks and repeated trials.
- **How VLMs Plan What's Next — paper boundary:** causal evidence is strongest on a controlled retrieval task and Qwen3-VL. **Direction:** test the interventions on other VLM architectures and open-ended multi-step tasks.
- **SWE-WhatIf — paper boundary:** evaluation uses 89 sessions and a 16-person study, and rankings depend on how users express intent. **Direction:** replicate across more projects, user groups, task types, and interaction styles, reporting uncertainty in rankings.
- **Think2Listen — paper boundary:** evidence covers two benchmarks and seven audio categories. **Direction:** test out-of-domain sounds, tool failures, and whether stopping remains reliable when evidence is ambiguous or costly to acquire.

## Takeaway

This batch distinguishes agents that merely return plausible outputs from systems designed to inspect relevant evidence—visual, acoustic, conversational, or physical. ScaleVLA, ViRA, and ForceHarness are the most externally surfaced selected papers, but remain fresh preprints; their strongest claims need replication beyond the tested models, tasks, and datasets.

## Method and sources

- **Window:** daily report for the latest arXiv announcement batch available at the snapshot. Exact batch/date: 2026-11-16; the requested 2026-11-17 calendar date had not yet reached its next announcement batch. Start/end: 2026-11-16T00:00:00Z–2026-11-16T23:59:59Z. Snapshot: 2026-11-17T17:05:08Z.
- **Candidate query:** arXiv API `submittedDate:[202611160000 TO 202611162359]` AND `(cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA)`. It returned 477 records; cross-lists were included and primary-category counts checked. The eight selected arXiv abstract pages were individually verified for ID, version, submission timestamp, authors, abstract, and categories.
- **Inference:** Ordering is inferred from contemporaneous independent technical coverage, cross-list breadth, and corpus relevance; recency was a tie-breaker. All selected papers are v1 submissions in the same announcement date. Semantic Scholar Graph citation fields could not be verified for these new records at snapshot, so no citation totals or citation velocity were used. This is a notable-recent-paper selection, not a readership/download ranking or comprehensive field survey.
- **arXiv sources:** [ScaleVLA](https://arxiv.org/abs/2611.21607) and [PDF](https://arxiv.org/pdf/2611.21607v1); [ViRA](https://arxiv.org/abs/2611.21605) and [PDF](https://arxiv.org/pdf/2611.21605v1); [ForceHarness](https://arxiv.org/abs/2611.21099); [How VLMs Plan What's Next](https://arxiv.org/abs/2611.21600) and [full text](https://arxiv.org/html/2611.21600); [Latent Lattice](https://arxiv.org/abs/2611.21608); [FaceJev](https://arxiv.org/abs/2611.21604); [SWE-WhatIf](https://arxiv.org/abs/2611.21095); [Think2Listen](https://arxiv.org/abs/2611.21083).
- **Additional corroboration:** contemporaneous write-ups for [ScaleVLA](https://explainx.ai/blog/scalevla-552b-vision-language-action-robot-backbone-2026), [ViRA](https://bedrocknews.com/article/arxiv/2611.21605v1), [ForceHarness](https://physicalainews.jp/papers/2611.21099), [How VLMs Plan What's Next](https://zerohour.day/item/2942510c8e1104575960c141ab1a4813b76d0607), [Latent Lattice](https://www.aimodeling.com/en/news/slug/latent-lattice-language-models-horizontal-latent-perplexity), and [FaceJev](https://physicalainews.jp/papers/2611.21604). Linked repositories and data resources appear in the entries.
