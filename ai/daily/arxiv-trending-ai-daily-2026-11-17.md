# AI papers — arXiv announcement batch, 17 November 2026

This inferred snapshot highlights five notable papers from the AI corpus; the dominant pattern is agents being evaluated on whether they gather and use evidence, with visual reasoning and robot control as active intersections. Spoken agenda: agent judgment, visual grounding, and scaling representations into action. arXiv has no official trending chart, so the ordering is inferred from checkable external coverage, project releases, and category breadth; citation evidence is limited for papers only just announced.

## Top papers (ranked)

### 1. [ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization](https://arxiv.org/abs/2611.21605)
- **Abstract:** The authors train visual agents on contrast sets of high-resolution images so success requires inspecting the changed evidence, reporting 63.3% set accuracy versus 59.3% for GRPO at maximum resolution.
- **Authors:** Huawei Lin, Jinting Liu, Tongyan Wang, Xuyang Chen, Ruihua Shi, et al.
- **arXiv:** `2611.21605v1` (published 2026-11-16T18:59:04Z; categories: `cs.CV`, `cs.AI`)
- **Evidence for ranking:** Cross-listed in vision and AI; the paper has a public [project repository](https://github.com/huawei-lin/ViRA) and a [Hugging Face Papers discussion page](https://huggingface.co/papers/2611.21605), and was covered by a separate [technical summary](https://kblip.com/research/vira-ultra-high-resolution-visual-agents-trained-via-4fxkfWF). These are corroboration signals, not readership counts.
- **Claimed contribution:** The authors introduce CrossRPO, a group-relative policy objective over image contrast sets, and release ViRA-Train, ViRA-Bench, and ViRA-Bench-Real; their reported comparison is on the stated benchmark suite.
- **Caveat:** The authors note that ViRA-Bench-Real contains only 78 photographed sets, shot indoors with one camera, and that the training/evaluation base models come from one model family.
- **Announcement type:** new submission, 17 November 2026 announcement batch
- **Themes:** Multimodal & vision-language; Training & adaptation; Evaluation & benchmarks

### 2. [SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents](https://arxiv.org/abs/2611.21541)
- **Abstract:** This paper presents an interactive thermal-measurement benchmark in which agents design experiments, reason with a potentially flawed simulator, and report calibrated intervals against exact ground truth; the authors report confident miscalibration on many simulator-mismatch tasks.
- **Authors:** Brian T. Weston, Alondra Torres Contreras, Aldair E. Gongora
- **arXiv:** `2611.21541v1` (published 2026-11-16T18:27:09Z; categories: `cs.AI`, `cs.LG`, `physics.comp-ph`)
- **Evidence for ranking:** The paper is cross-listed across AI, ML, and computational physics, and pairs its release with a public [benchmark repository](https://github.com/Btwestyo/sciresearch-eval); it also received a distinct [technical paper summary](https://papers.cool/arxiv/2611.21541). This combination gives it stronger checkable project and cross-category signals than a title-only listing.
- **Claimed contribution:** The authors contribute a benchmark combining agent-designed experiments, deliberately flawed simulators, and proper interval scoring against exact simulated truth, with a held-out evaluation of nine models.
- **Caveat:** The authors explicitly describe the benchmark as one physical domain by design; transfer to other scientific domains remains to be tested.
- **Announcement type:** new submission, 17 November 2026 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 3. [ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters](https://arxiv.org/abs/2611.21607)
- **Abstract:** ScaleVLA connects a 552B vision-language backbone to a trainable action diffusion transformer and reports gains over smaller backbones in simulation sample efficiency, generalization, and a small real-world charger-insertion evaluation.
- **Authors:** Ruixi Yu, Dairu Liu, Xuchuan Chen, Zekun Qi, Zekai Li, et al.
- **arXiv:** `2611.21607v1` (published 2026-11-16T18:59:37Z; categories: `cs.RO`)
- **Evidence for ranking:** The paper has a [project page](https://galaxygeneralrobotics.github.io/scalevla/), a [Hugging Face Papers page](https://huggingface.co/papers/2611.21607), and separate coverage from [AI Weekly](https://aiweekly.co/alerts/tsinghua-led-scalevla-scales-vision-language-action-models-to-552b-on-deepseek) and [ExplainX](https://explainx.ai/blog/scalevla-552b-vision-language-action-robot-backbone-2026). Coverage corroborates attention to the unusually large robotics experiment; it does not establish adoption or replication.
- **Claimed contribution:** The authors report a controlled 2B-to-552B backbone comparison with fixed action-side setup, plus simulation and real-robot results; their real-robot in-domain charger insertion result is 9/10 versus 4/10 for the 2B baseline.
- **Caveat:** Each trained policy uses one training seed, and the real-robot in-domain result is based on ten trials; the paper also notes the 552B model requires more hardware than smaller backbones.
- **Announcement type:** new submission, 17 November 2026 announcement batch
- **Themes:** Robotics & control; Multimodal & vision-language; Training & adaptation

### 4. [Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility](https://arxiv.org/abs/2611.21478)
- **Abstract:** Jetriever ranks stored memories by estimated usefulness to the current question rather than text similarity, reporting that it places the gold exchange first in 84.8% of 125 indirect-query tasks.
- **Authors:** Ruizhe Li, Licheng Zhang, Mingxuan Du, Zhendong Mao
- **arXiv:** `2611.21478v1` (published 2026-11-16T17:50:53Z; categories: `cs.CL`)
- **Evidence for ranking:** The proposal was surfaced in separate [Grafy coverage](https://grafy.ai/news/jetriever-replaces-similarity-search-with-utility-scoring-for-agent-memory) and a [KBLIP technical summary](https://kblip.com/research/jetriever-shifting-agent-memory-retrieval-from-similarity-zIsgRw6), in addition to its arXiv listing. These are discussion signals, not independent replications.
- **Claimed contribution:** The authors replace similarity search with full-pool utility scoring and report matched retrieval comparisons on InMind plus a sampled MemoryAgentBench evaluation.
- **Caveat:** The authors state that full-pool scoring grows with the memory store; the principal indirect-query result is based on 125 tasks, so broader and longer-running memory evaluations remain open.
- **Announcement type:** new submission, 17 November 2026 announcement batch
- **Themes:** Retrieval & knowledge; Agents & reasoning; Evaluation & benchmarks

### 5. [Latent Lattice Language Models](https://arxiv.org/abs/2611.21608)
- **Abstract:** The paper adds persistent per-layer latent streams that condition attention, cache writes, and MLP computation, reporting lower validation perplexity than a parameter-matched Transformer in its 406M-parameter, 20B-token experiment.
- **Authors:** Shivam Duggal, Zongze Wu, William T. Freeman, Antonio Torralba, Richard Zhang, Eli Shechtman
- **arXiv:** `2611.21608v1` (published 2026-11-16T18:59:38Z; categories: `cs.LG`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The paper spans three core AI categories and received multiple independently hosted technical explainers, including [DeepPaper](https://arxiv.deeppaper.ai/papers/2611.21608v1) and [Foorilla](https://foorilla.com/research/papers/latent-lattice-language-models-406531/). The signal is breadth of public discussion rather than a measured citation or usage increase.
- **Claimed contribution:** The authors introduce the Lattice of Latents as a companion set of persistent per-layer computational states and report gains across Transformer and recurrent-backbone experiments.
- **Caveat:** The headline parameter-matched language-model result is for a 406M model trained on 20B FineWeb-Edu tokens; the paper's evidence does not by itself establish how the gains scale to larger training runs or downstream deployments.
- **Announcement type:** new submission, 17 November 2026 announcement batch
- **Themes:** Training & adaptation; Efficient inference & systems

## Trending Research Themes

- **Agents judged by evidence use, not just final answers:** SciResearch-Eval scores calibrated estimates under simulator misspecification, ViRA makes contrast-set success depend on inspecting image changes, and Jetriever tests retrieval of indirectly useful memories. Together these papers foreground process-sensitive evaluation, though they address different tasks and do not establish one shared benchmark standard.
- **Visual-language representations are being pushed toward action:** ViRA focuses on evidence localization in very large images, while ScaleVLA connects pretrained visual-language representations directly to continuous robot control. This is a recurring intersection of perception and action, not evidence that one approach transfers to the other.
- **A second route to capability is changing internal computation:** Latent Lattice adds persistent per-layer states, whereas ScaleVLA increases the scale of pretrained representations. These are distinct architecture/scaling approaches; this batch does not show a general result favoring either.
- **Corpus coverage:** The selected set spans `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV`, and `cs.RO`; the day's category pages were largest for `cs.LG` (461 entries), `cs.AI` (428), and `cs.CV` (342). Category counts overlap because cross-listed papers appear in more than one list.

## Open Problems and Research Directions

- **Author-stated — scientific-domain transfer:** SciResearch-Eval is deliberately limited to thermal-property measurement. Extend the benchmark to other experimental sciences while preserving exact ground truth and controlled failure causes, then test whether the same diagnosis and calibration gaps recur.
- **Author-stated — visual benchmark realism and model coverage:** ViRA reports only 78 real photographed sets, from one indoor camera setting, and training from one base-model family. A follow-up could enlarge the real-image set across environments and objects and test CrossRPO on different architectures; compare against ViRA's current edited-image benchmarks to quantify any gap.
- **Author-stated — scaling memory retrieval:** Jetriever says full-pool scoring grows with the store. Test retrieval quality and cost as persistent memories grow, while measuring whether candidate-filtering preserves indirect evidence that similarity search misses.
- **Author-stated — robot reproducibility:** ScaleVLA's policies use one training seed and its in-domain hardware result uses ten trials. Repeat across seeds, robots, and manipulation tasks, and report task success jointly with hardware and energy cost.
- **Synthesis — architecture scaling:** Latent Lattice's reported headline comparison uses a 406M model and 20B training tokens. Test larger scales and downstream tasks with matched compute and memory budgets to separate gains from added state capacity from gains due to training or inference cost.

## Takeaway

The most coherent signal in this batch is a shift toward testing whether AI systems actually gather, preserve, and act on relevant evidence: in scientific experiments, image inspection, and memory retrieval. The papers offer promising task-specific results, but transfer, replication, and scaling remain uncertain; the external attention evidence is too sparse to support a definitive popularity ranking.

## Method and sources

- **Window:** arXiv announcement batch dated 2026-11-17 (Tuesday); selected papers were first submitted 2026-11-16 and appeared in that announcement batch. Daily window: 2026-11-17 through 2026-11-17.
- **Snapshot:** 2026-11-18 01:13:21 UTC.
- **Scope/query:** `cs.AI OR cs.LG OR stat.ML OR cs.CL OR cs.CV OR cs.RO OR cs.NE OR cs.MA`. Category recent pages showed: `cs.AI` 428, `cs.LG` 461, `stat.ML` 56, `cs.CL` 236, `cs.CV` 342, `cs.RO` 134, `cs.NE` 7, `cs.MA` 30 entries for the batch. These overlap across cross-lists.
- **Inference:** No official arXiv trend ranking exists. The five-paper ordering is an inferred, qualitative ranking based on checkable external coverage, public project releases, cross-list breadth, and the specificity of reported evaluations; recency was only a tie-breaker. Search visibility and third-party summaries are weak attention proxies, not readership or download statistics. Semantic Scholar citation metadata was not available in this snapshot, so citation momentum is not claimed.
- **Sources:** Each arXiv abstract page is linked in its heading; arXiv batch listings were checked across all eight categories. Paper text (abstracts, conclusions, and limitations where available) was checked in arXiv abstract/HTML pages. Web extraction was unavailable in the configured search-only backend, so pages were retrieved directly from arXiv; the Semantic Scholar Graph source did not return usable citation data. External coverage and project links are included in each paper's ranking evidence.
