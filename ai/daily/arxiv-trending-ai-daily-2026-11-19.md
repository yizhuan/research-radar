# arXiv AI — latest announcement batch 2026-11-19: 10 papers on embodied reasoning, video understanding, and visual-model design. Quick agenda: robot reasoning/action, omni-modal video, depth, controllable video generation, and efficient inference. arXiv has no official trending chart; this inferred ordering uses attention signals, and citation evidence is limited for these recent papers.

## Top papers (ranked)

### 1. [Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation](https://arxiv.org/abs/2611.26444)
- **Abstract:** The authors introduce a 30-task simulated manipulation benchmark that separately probes history-based reasoning, precise action, and closed-loop composition, finding that even their strongest evaluated agent succeeds on only 12.0% of Mind2Act episodes.
- **Authors:** Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin, Weichen Zhang, et al.
- **arXiv:** `2611.26444v1` (published 2026-11-19 17:15:38 UTC; categories: `cs.RO`, `cs.AI`, `cs.CV`)
- **Evidence for ranking:** Highest supplied score (14.159; components: HF-upvotes 11.911, code-stars 1.748, cross-lists 0.500): 52 Hugging Face Papers upvotes, 32 linked GitHub stars and two cross-lists. Semantic Scholar listed 0 citations; no HN points/comments were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.26444)
- **Claimed contribution:** The authors provide 180 task configurations across three views and a diagnosis harness; their evaluation reports a large gap between Mind/Act performance (52.7%/39.0% for the strongest agent) and Mind2Act performance (12.0%).
- **Caveat:** The authors say the views are different tasks, not matched interventions, so longer horizons and early execution errors cannot yet be separated from a composition deficit; all tasks are simulated tabletop manipulation.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Evaluation & benchmarks; Robotics & control; Agents & reasoning

### 2. [WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding](https://arxiv.org/abs/2611.26409)
- **Abstract:** The authors present Chinese-English 2B–35B-A3B models that jointly process text, image, audio, and video with fast-instruct and reasoning modes, reporting evaluations across more than 120 benchmarks.
- **Authors:** Changli Tang, Jie Yang, Tianyi Wang, Lei Li, Daoze Zhang, et al.
- **arXiv:** `2611.26409v1` (published 2026-11-19 16:58:15 UTC; categories: `cs.CV`, `eess.AS`)
- **Evidence for ranking:** Second by the supplied score (13.853; components: HF-upvotes 11.486, code-stars 2.117, cross-lists 0.250): 45 Hugging Face Papers upvotes, 68 linked GitHub stars and one cross-list. Semantic Scholar listed 0 citations; no HN points/comments were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.26409)
- **Claimed contribution:** The authors report that WeMM-Video-35B-A3B leads their open-source comparisons on omni-modal video tasks and that the 9B variant outperforms the compared 30B open-source model; they release weights and an evaluation/reproduction pipeline.
- **Caveat:** For existing comparison models, the paper uses official scores where available and its own evaluations otherwise, so not every comparison is from a single uniform evaluation run.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Multimodal & vision-language; Training & adaptation; Evaluation & benchmarks

### 3. [Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://arxiv.org/abs/2611.26603)
- **Abstract:** The authors present a native-resolution network for metric depth from images and video, designed to combine sharp boundaries with temporal consistency and reporting a new Pareto frontier across accuracy, sharpness, consistency, and runtime.
- **Authors:** Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, et al.
- **arXiv:** `2611.26603v1` (published 2026-11-19 18:55:41 UTC; categories: `cs.CV`, `cs.LG`)
- **Evidence for ranking:** Third by the supplied score (13.765; components: HF-upvotes 10.579, code-stars 2.936, cross-lists 0.250): 33 Hugging Face Papers upvotes, 354 linked GitHub stars and one cross-list. Semantic Scholar listed 0 citations; no HN points/comments were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.26603)
- **Claimed contribution:** The paper describes a shared multi-frame transformer, multi-view consistency training, and a family of models; its abstract reports improvements over prior work in metric accuracy, boundary sharpness, and temporal consistency.
- **Caveat:** The authors note that their Temporal Alignment Error assumes a static scene and is ambiguous at occlusions; it can produce non-zero error even for ground-truth depth (Appendix B.3).
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Multimodal & vision-language; Efficient inference & systems; Training & adaptation

### 4. [Coda-DaVinci: Reimagining Video Generation with Code2Video](https://arxiv.org/abs/2611.26595)
- **Abstract:** The authors study agent-authored 3D proxies for video generation and introduce a task-adaptive framework that selects direct or proxy-guided generation, with proxy granularity, simulation, and prompting evaluated through controlled experiments and blinded human ratings.
- **Authors:** Yiyan Ji, Qixun Wang, Yang Shi, Zhuoran Zhang, Yifan Xu, et al.
- **arXiv:** `2611.26595v1` (published 2026-11-19 18:51:58 UTC; categories: `cs.CV`)
- **Evidence for ranking:** Score 12.600 (components: HF-upvotes 10.991, code-stars 1.609): 38 Hugging Face Papers upvotes and 24 linked GitHub stars. Semantic Scholar listed 0 citations; no HN points/comments or cross-list were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.26595)
- **Claimed contribution:** The authors report that coarse proxies favor natural motion while medium-grained proxies favor consistency, and that their framework improves instruction following, scene consistency, physical plausibility, and visual realism on the evaluated comparisons.
- **Caveat:** The abstract reports remaining long-video weaknesses in transition stability and adherence to scene settings.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Agents & reasoning; Multimodal & vision-language; Evaluation & benchmarks

### 5. [Posterior Matching Distillation](https://arxiv.org/abs/2611.26629)
- **Abstract:** The authors propose Posterior Matching Distillation, which matches reweighted student-sample means to teacher posterior means to preserve the teacher’s image distribution while allowing stochastic generation at any trained timestep budget.
- **Authors:** Hidir Yesiltepe, Julius Berner, Arash Vahdat, Pinar Yanardag
- **arXiv:** `2611.26629v1` (published 2026-11-19 18:59:57 UTC; categories: `cs.CV`)
- **Evidence for ranking:** Score 12.387 (components: HF-upvotes 11.067, code-stars 1.320): 39 Hugging Face Papers upvotes and 13 linked GitHub stars. Semantic Scholar listed 0 citations; no HN points/comments or cross-list were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.26629)
- **Claimed contribution:** The authors prove a posterior-identification result under their stated conditions and report the best FID among evaluated four-step methods on SDXL and FLUX.2 [klein], with competitive prompt-alignment and perceptual scores.
- **Caveat:** The reported empirical comparison is limited to SDXL and FLUX.2 [klein] and the evaluated four-step setting; broader model and sampling-budget behavior is not established by those results.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Training & adaptation; Efficient inference & systems; Evaluation & benchmarks

### 6. [Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models](https://arxiv.org/abs/2611.26590)
- **Abstract:** The authors introduce a multimodal Jacobian lens that maps vision and language representations to a shared output-vocabulary semantic space and use interventions to study selective concept access and downstream effects in vision-language models.
- **Authors:** Jiahao Huang, Jun Wang
- **arXiv:** `2611.26590v1` (published 2026-11-19 18:46:50 UTC; categories: `cs.AI`, `cs.CV`, `cs.LG`)
- **Evidence for ranking:** Score 11.853 (components: HF-upvotes 11.353, cross-lists 0.500): 43 Hugging Face Papers upvotes and two cross-lists; no linked GitHub stars were recorded. Semantic Scholar listed 0 citations; no HN points/comments were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.26590)
- **Claimed contribution:** The paper reports that concepts are readable and selectively accessible in intermediate states, that counterfactual interventions affect downstream computation, and that its J-space metrics track cross-modal alignment across tested VLM families and sizes.
- **Caveat:** These are probe- and intervention-based findings in tested VLMs; they do not establish that the models are conscious, and conclusions depend on the lens’s decoder-vocabulary readout.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Interpretability; Multimodal & vision-language

### 7. [HiUni: Harmonizing Understanding and Generation in Shared Visual Space](https://arxiv.org/abs/2611.26107)
- **Abstract:** The authors extend a pretrained vision-language model with a shared language-aligned ViT and dense Transformer backbone for understanding and image generation, adding a Pixel Diffusion Head and HiGate pathway for synthesis and spatial detail.
- **Authors:** Jiahao Hu, Jingdong Du, Yichen Zhang, Yi Song, Zhenyu Zhang, et al.
- **arXiv:** `2611.26107v1` (published 2026-11-19 13:37:47 UTC; categories: `cs.CV`, `cs.AI`)
- **Evidence for ranking:** Score 11.138 (components: HF-upvotes 9.534, code-stars 1.354, cross-lists 0.250): 23 Hugging Face Papers upvotes, 14 linked GitHub stars and one cross-list. Semantic Scholar listed 0 citations; no HN points/comments were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.26107)
- **Claimed contribution:** The authors report an average understanding score similar to the pretrained VLM alongside competitive image generation and editing, and argue that one dense backbone can support both without task-specific backbone computation.
- **Caveat:** The abstract characterizes generation and editing as competitive rather than claiming uniform state-of-the-art performance; the evidence is limited to the reported tasks and comparisons.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Multimodal & vision-language; Training & adaptation

### 8. [ZeroVLN: Learning to Navigate without Supervised Fine-Tuning of the VLM Brain](https://arxiv.org/abs/2611.26414)
- **Abstract:** The authors propose a slow-fast vision-language navigation framework that leaves the VLM brain without navigation-domain supervised fine-tuning, instead using natural-language tool calls to an adapted action expert and closed-loop reinforcement learning.
- **Authors:** Zixuan Huang, Yang Zhou, Guli Zhang, Sunzhu Li, Hongyan Xie, et al.
- **arXiv:** `2611.26414v1` (published 2026-11-19 17:01:00 UTC; categories: `cs.AI`)
- **Evidence for ranking:** Score 11.035 (components: HF-upvotes 9.406, code-stars 1.629): 22 Hugging Face Papers upvotes and 25 linked GitHub stars. Semantic Scholar listed 0 citations; no HN points/comments or cross-list were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.26414)
- **Claimed contribution:** The authors report that ZeroVLN outperforms the compared SFT-based hierarchical methods on VLN-CE benchmarks while making only minor changes to the VLM brain and largely preserving its general visual capabilities.
- **Caveat:** “Zero SFT” applies to the VLM brain: the action expert is adapted and both policies are improved through RL on navigation episodes; the reported evaluation is on benchmarks, not a real-world deployment.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Agents & reasoning; Robotics & control; Training & adaptation

### 9. [EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning](https://arxiv.org/abs/2611.26380)
- **Abstract:** The authors combine video-level context with timestamped egocentric action descriptions, using 50,000 coarse-to-fine training examples and factual, coverage, and temporal-alignment rewards to refine captions.
- **Authors:** Yuqi Tang, Yang Shi, Yuran Wang, Tengfei Liu, Rundong Wang, et al.
- **arXiv:** `2611.26380v1` (published 2026-11-19 16:39:59 UTC; categories: `cs.CV`)
- **Evidence for ranking:** Score 10.814 (components: HF-upvotes 9.774, code-stars 1.040): 25 Hugging Face Papers upvotes and 7 linked GitHub stars. Semantic Scholar listed 0 citations; no HN points/comments or cross-list were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.26380)
- **Claimed contribution:** Across five egocentric benchmarks, the authors report leading results among evaluated open-source models for caption quality, caption-conditioned QA, and temporal alignment, with ablations supporting multiple reward terms and coarse-to-fine annotations.
- **Caveat:** Pose-derived motion facts are used only where sensor data are available, so that additional factual-supervision path is not present for every source video.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Training & adaptation

### 10. [TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs](https://arxiv.org/abs/2611.25387)
- **Abstract:** The authors introduce 125 programmatically generated interactive CAPTCHA tasks for spatial action, report a 25.9% failure rate for their best tested model, and show that fine-tuning Qwen3.5-9B on the environment raises success from 1.6% to 33.1%.
- **Authors:** Xuwei Ding, Skylar Zhai, Linxin Song, Jiarui Feng, Dongqi Fu, et al.
- **arXiv:** `2611.25387v1` (published 2026-11-19 02:32:10 UTC; categories: `cs.LG`)
- **Evidence for ranking:** Score 10.339 (components: HF-upvotes 9.534, code-stars 0.805): 23 Hugging Face Papers upvotes and 4 linked GitHub stars. Semantic Scholar listed 0 citations; no HN points/comments or cross-list were recorded for this entry. [Hugging Face paper signal](https://huggingface.co/papers/2611.25387)
- **Claimed contribution:** The benchmark tests five spatial abilities through clicks and drags, provides generated instances with checkers and oracles, and the authors report gains on seven out-of-distribution benchmarks after fine-tuning.
- **Caveat:** The central task set is a synthetic CAPTCHA environment; transfer to seven external benchmarks is encouraging but does not by itself establish reliability across open-ended real-world spatial interaction.
- **Announcement type:** new submission, 2026-11-19 announcement batch
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Multimodal & vision-language

## Trending Research Themes

- **Embodied systems are being assessed as closed loops, not only as perception or action modules.** Mind2Act World separates reasoning, execution, and their composition; ZeroVLN connects language decisions to an adapted action expert; TuringSpace measures perception-action correction in interactive tasks. These are different settings, but all expose the gap between isolated competence and acting on feedback.
- **Video work emphasizes temporal structure and cross-modal grounding.** WeMM-Video unifies audio-visual perception and reasoning; EgoCaptioner makes egocentric captions step-timed and rewards temporal alignment; Coda-DaVinci uses explicit 3D proxies and simulation to control generated motion. The common theme is temporal organization, not a single shared architecture.
- **Vision systems are combining capabilities that were often separated.** HiUni shares a visual backbone between understanding and generation, while Depth Pro 2 jointly processes images and video to balance sharpness and stability. MC-Lens takes a different tack by probing how visual concepts become accessible to language-model computation.
- **Efficiency claims target different bottlenecks.** Posterior Matching Distillation reduces diffusion sampling to a flexible number of trained steps; Depth Pro 2 reports model-size/runtime trade-offs; WeMM-Video offers multiple parameter scales and modes. These results are not directly comparable, and the selected set remains concentrated in vision: six of ten papers have primary category `cs.CV`.

## Open Problems and Research Directions

- **Author-stated — diagnosing composition failures:** Mind2Act World’s views use different tasks and horizons, so the authors cannot yet distinguish a composition deficit from longer-horizon difficulty or early execution failure. Run matched interventions on the same task with reasoning state, action feedback, and time budget varied independently, then verify the result beyond simulation. [Mind2Act World](https://arxiv.org/abs/2611.26444)
- **Evidence-tied synthesis — robustness of temporal grounding:** WeMM-Video targets cross-modal hallucination and EgoCaptioner evaluates factual and temporal alignment, while Coda-DaVinci reports transition and scene-setting weaknesses. Stress-test these systems with missing/noisy modalities, long clips, and unexpected scene changes, scoring factual support and event ordering separately. [WeMM-Video](https://arxiv.org/abs/2611.26409) · [EgoCaptioner](https://arxiv.org/abs/2611.26380) · [Coda-DaVinci](https://arxiv.org/abs/2611.26595)
- **Evidence-tied synthesis — generalization of action benchmarks:** TuringSpace reports transfer from synthetic CAPTCHA training to seven benchmarks, while ZeroVLN evaluates on VLN-CE. Compare both against held-out interactive environments and physical or real-world navigation, with perturbations and recovery rates reported alongside success. [TuringSpace](https://arxiv.org/abs/2611.25387) · [ZeroVLN](https://arxiv.org/abs/2611.26414)
- **Proposed follow-up — quality across distillation budgets:** Posterior Matching Distillation supports sampling budgets within its trained timestep grid, but the abstract’s best-FID comparison focuses on four-step generation for two model families. Evaluate a wider budget curve and explicit sample-diversity metrics to test where mode coverage and speed trade off. [Posterior Matching Distillation](https://arxiv.org/abs/2611.26629)

## Takeaway

The strongest visible pattern in this batch is a push toward models and benchmarks that represent temporal structure and feedback: in robot control, multimodal video, and controllable generation. Attention counts identify which new papers drew early notice, but the results remain author-reported and benchmark-bound; broader, matched, and real-world evaluation will determine how far the claims generalize.

## Method and sources

- **Window and snapshot:** Daily latest available arXiv announcement batch dated **2026-11-19**; this is a prior batch for the 2026-11-22 snapshot. The exact batch window is **2026-11-18 19:00:00 UTC to 2026-11-19 19:00:00 UTC**, announced **2026-11-20 01:00:00 UTC**. Snapshot time: **2026-11-22 17:05:02 UTC**. All ten selected records are new `v1` submissions in that batch, not revisions.
- **Corpus:** `cs.AI OR cs.LG OR stat.ML OR cs.CL OR cs.CV OR cs.RO OR cs.NE OR cs.MA`. The supplied signal file reports a 635-candidate pool, including 42 with at least one collected attention signal; its note says the listing is capped and may not exhaust very large categories. Category recent listings: [cs.AI](https://arxiv.org/list/cs.AI/recent), [cs.LG](https://arxiv.org/list/cs.LG/recent), [stat.ML](https://arxiv.org/list/stat.ML/recent), [cs.CL](https://arxiv.org/list/cs.CL/recent), [cs.CV](https://arxiv.org/list/cs.CV/recent), [cs.RO](https://arxiv.org/list/cs.RO/recent), [cs.NE](https://arxiv.org/list/cs.NE/recent), [cs.MA](https://arxiv.org/list/cs.MA/recent).
- **Ranking and signal availability:** Started from the supplied candidate scores and ranked by the collector’s deterministic log1p-damped weighted sum; per-paper score components are shown above. Weights: Hugging Face upvotes 3.0, Hacker News points 1.5, HN comments 1.0, Semantic Scholar citations 2.0, influential citations 1.0, code stars 0.5, and cross-lists 0.25. Scores are a transparent ranking aid, not an official or universal trend metric. The snapshot reports arXiv, Hugging Face, Hacker News, arXiv lookup and Semantic Scholar as `ok`; no source-level errors were reported. Selected entries have zero current Semantic Scholar citation and influential-citation totals, not evidence of no interest. No selected paper has recorded HN points/comments. HF upvotes and code-star values are snapshot totals, not gains during the announcement window.
- **Primary-page verification and paper reading:** Each selected title, author order, version, timestamp, categories, and abstract was verified on its linked arXiv abstract page. The full arXiv HTML for Mind2Act World, WeMM-Video, and Depth Pro 2 was also read for method, evaluation, and caveat context. Other contribution and caveat statements above are bounded to the verified arXiv abstracts.
- **Selected records:** [2611.26444](https://arxiv.org/abs/2611.26444) · [2611.26409](https://arxiv.org/abs/2611.26409) · [2611.26603](https://arxiv.org/abs/2611.26603) · [2611.26595](https://arxiv.org/abs/2611.26595) · [2611.26629](https://arxiv.org/abs/2611.26629) · [2611.26590](https://arxiv.org/abs/2611.26590) · [2611.26107](https://arxiv.org/abs/2611.26107) · [2611.26414](https://arxiv.org/abs/2611.26414) · [2611.26380](https://arxiv.org/abs/2611.26380) · [2611.25387](https://arxiv.org/abs/2611.25387)
- **Attention signal records:** [HF paper 2611.26444](https://huggingface.co/papers/2611.26444) · [2611.26409](https://huggingface.co/papers/2611.26409) · [2611.26603](https://huggingface.co/papers/2611.26603) · [2611.26595](https://huggingface.co/papers/2611.26595) · [2611.26629](https://huggingface.co/papers/2611.26629) · [2611.26590](https://huggingface.co/papers/2611.26590) · [2611.26107](https://huggingface.co/papers/2611.26107) · [2611.26414](https://huggingface.co/papers/2611.26414) · [2611.26380](https://huggingface.co/papers/2611.26380) · [2611.25387](https://huggingface.co/papers/2611.25387)
