# arXiv Trending AI — 2026-11-26

## Headline

AI, latest available arXiv announcement batch 2026-11-26: 7 papers, with multimodal visual systems and model-efficiency work most visible in the attention signals. I’ll cover medical vision-language scaling, looped and speculative decoding, agentic media, document understanding, and robot robustness. arXiv has no official trending chart; this ordering is inferred from checkable Hugging Face upvotes and Hacker News points, not a universal popularity measure, and recent citation evidence is limited.

## Top papers (ranked)

### 1. [Sage-Med: Scaling Medical Multimodal Intelligence](https://arxiv.org/abs/2611.34575)
- **Abstract:** The authors introduce a 35B-parameter medical multimodal model with 3B active parameters, trained through staged data curation and progressive supervised and reinforcement-learning stages, and report results across 238 clinical tasks.
- **Authors:** Med Team, Ming Hu, Cheng Tang, Wei Li, Rongbin Li et al.
- **arXiv:** `2611.34575v1` (published 2026-11-25T15:39:45Z; categories: `cs.CV`, `cs.AI`)
- **Evidence for ranking:** 81 Hugging Face Papers upvotes at the 2026-11-28 snapshot, the highest count among the selected entries. This is a cumulative upvote count, not upvotes gained during the announcement window.
- **Claimed contribution:** The authors report a 58.26% average score on 31 public multimodal benchmarks and describe remaining gaps in complex medical reasoning and multi-step clinical workflows.
- **Caveat:** The abstract explicitly says complex medical reasoning and multi-step clinical workflows remain substantial challenges; the reported public-benchmark average covers 31 of the 238 total tasks.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Multimodal & vision-language; Training & adaptation; Data & synthetic data

### 2. [Mixture-of-Loops Transformer](https://arxiv.org/abs/2611.34923)
- **Abstract:** MoLT uses key-value memory across repeated Transformer loops and introduces a U-shaped variant intended to balance model quality, token efficiency, and decoding cost.
- **Authors:** Lianghui Zhu, Shijie Wang, Xinggang Wang, Jinze Bai, Bo Wang, Xiang Bai
- **arXiv:** `2611.34923v1` (published 2026-11-25T18:58:53Z; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** 74 Hugging Face Papers upvotes at the 2026-11-28 snapshot. The paper also has a public code repository; the upvote count is cumulative, not a period gain.
- **Claimed contribution:** In author-reported experiments, U-MoLT achieves 1.7× validation cross-entropy token efficiency at 700M parameters and similar latency to non-looped OLMo3 in a small-model decoding test.
- **Caveat:** The results are bounded by the reported 700M/1.5B dense and 3B MoE pretraining experiments, one 0.8B continued-pretraining backbone, and a small-model latency test.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Efficient inference & systems; Training & adaptation

### 3. [VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation](https://arxiv.org/abs/2611.34237)
- **Abstract:** VibeVideoAgent lets coding agents inspect short previews of rendered video and audio during production, returning grounded findings that guide iterative edits without filling the coder’s context with raw media.
- **Authors:** Xuanyu Zheng, Luoyuan Zhang, Yancheng Long, Haoyang Xu, Muxi Diao et al.
- **arXiv:** `2611.34237v1` (published 2026-11-25T11:59:44Z; categories: `cs.CV`)
- **Evidence for ranking:** 58 Hugging Face Papers upvotes at the 2026-11-28 snapshot. This cumulative count is the third-highest among the selected papers.
- **Claimed contribution:** On 239 VibeVideoBench tasks, the authors report improved audiovisual quality for three tested coding-agent models under matched runtimes and a fixed perception model.
- **Caveat:** The evaluation uses a fixed perception model, and trajectory audits report a trade-off between code-edit granularity, rubric compliance, and perceptual quality.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Agents & reasoning; Multimodal & vision-language; Evaluation & benchmarks

### 4. [Improving and Expanding Video Editing Capabilities Without Videos](https://arxiv.org/abs/2611.34941)
- **Abstract:** Image-to-Video Transfer uses an image editor to guide a pretrained video editor using single images, aiming to expand video-editing capabilities without collecting paired edited videos.
- **Authors:** Ji Xie, Yanhao Jia, Xiangpeng Yang, Martin Q. Ma, Sihan Xu et al.
- **arXiv:** `2611.34941v1` (published 2026-11-25T18:59:55Z; categories: `cs.CV`)
- **Evidence for ranking:** 46 Hugging Face Papers upvotes at the 2026-11-28 snapshot; the count is cumulative rather than a window gain.
- **Claimed contribution:** Across three video editors, the authors report improved performance on OpenVE-Bench and their extended OpenVE++ suite, which adds four video-editing tasks.
- **Caveat:** The abstract reports tests on three video editors and two related benchmarks; it does not establish generalization to other editing systems or task distributions.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Multimodal & vision-language; Training & adaptation

### 5. [DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding](https://arxiv.org/abs/2611.34420)
- **Abstract:** DocSEAM enriches each document page’s visual tokens with information from adjacent pages using anchored masked attention, while keeping the visual token count unchanged.
- **Authors:** Hoang-Nhat Nguyen, Chen Change Loy
- **arXiv:** `2611.34420v1` (published 2026-11-25T14:11:06Z; categories: `cs.CV`, `cs.CL`)
- **Evidence for ranking:** 28 Hugging Face Papers upvotes at the 2026-11-28 snapshot; this is a cumulative count.
- **Claimed contribution:** The authors report state-of-the-art results among evaluated open-weight models up to 10B parameters on five multi-page document VQA benchmarks, with reduced re-pagination sensitivity and improved cross-page span localization.
- **Caveat:** The reported comparison is limited to a 9B model, the tested open-weight systems up to 10B parameters, and five multi-page VQA benchmarks.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks

### 6. [HOG-WAM: Improving Visual Robustness through Future Gradient Prediction](https://arxiv.org/abs/2611.34811)
- **Abstract:** HOG-WAM adds training-only future histogram-of-oriented-gradients prediction to a world-action model to improve the visual representations used for robot control under observation corruption.
- **Authors:** Boxuan Dong, Yupeng Qian, Ying Wu, Heshuai Li, Junhao Tan et al.
- **arXiv:** `2611.34811v1` (published 2026-11-25T17:59:24Z; categories: `cs.CV`, `cs.AI`, `cs.RO`)
- **Evidence for ranking:** 23 Hugging Face Papers upvotes at the 2026-11-28 snapshot; the count is cumulative.
- **Claimed contribution:** The authors report higher success than compared policies under four controlled observation corruptions, with additional results on LIBERO Plus and four Franka tasks.
- **Caveat:** Evidence is bounded by the listed corruption settings, LIBERO Plus, and four Franka tasks; the abstract does not establish robustness across broader sensors, robots, or deployment conditions.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Robotics & control; Training & adaptation

### 7. [Looped Models are Fast Multi-Token Predictors](https://arxiv.org/abs/2611.33896)
- **Abstract:** Floodgates adapts shallow loops in looped language models to draft multiple future tokens in parallel, enabling self-speculative decoding that verifies with deeper computation.
- **Authors:** Ayhan Suleymanzade, Sean McLeish, Sehoon Kim, Jinwoo Kim, Antoine Bosselut
- **arXiv:** `2611.33896v1` (published 2026-11-25T07:16:56Z; categories: `cs.LG`, `cs.CL`)
- **Evidence for ranking:** The Hacker News discussion received 13 points and 0 comments (item 50657370). Hacker News points are not numerically comparable to Hugging Face upvotes, so this paper is listed after the Hugging Face-ranked entries as a separate attention signal.
- **Claimed contribution:** Across seven models and five benchmarks, the authors report that Floodgates is the fastest lossless decoding method in most tested cases, with up to 7.5× acceleration.
- **Caveat:** The speedup claim is scoped to the evaluated models, benchmarks, batch sizes, and decoding settings; the maximum reported acceleration is not an across-the-board result.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Efficient inference & systems; Training & adaptation

## Trending Research Themes

- **Multimodal visual systems draw most of the selected-paper attention.** Five of seven selected papers have primary category `cs.CV`: Sage-Med, VibeVideoAgent, Image-to-Video Transfer, DocSEAM, and HOG-WAM. Their work ranges from medical understanding to page-boundary context and robust robot perception; this concentration describes the selected attention-ranked sample, not the full AI corpus.
- **Systems are reusing structure or intermediate computation to improve efficiency.** MoLT reuses key-value state across loops, while Floodgates converts shallow loop computation into multi-token drafts. Both target inference efficiency, but their evidence comes from different model families and experimental setups.
- **Perception is being placed inside an action or editing feedback loop.** VibeVideoAgent inspects audiovisual previews before committing edits, and HOG-WAM shapes robot-control features with future visual structure. These are distinct approaches, not evidence of a unified new paradigm.
- **Data-efficient transfer is a recurring practical goal.** Image-to-Video Transfer tries to extend video editing from image-level supervision, while Sage-Med reports staged curation and training over large medical data collections. The application and methods differ; both seek capability gains without simply scaling paired task-specific data.

## Open Problems and Research Directions

- **Author-stated open problem — Sage-Med:** Complex medical reasoning and multi-step clinical workflows remain difficult. **Research direction (synthesis):** report task-specific error analyses on longitudinal or multi-step clinical workflows, with external-site and modality-shift evaluation. ([Sage-Med](https://arxiv.org/abs/2611.34575))
- **Author-stated boundary — VibeVideoAgent:** Edit granularity affects the trade-off between rubric compliance and perceptual quality, and the benchmark used a fixed perception model. **Research direction (synthesis):** test adaptive preview/edit granularity and repeat the study with multiple perception models and independently rated outputs. ([VibeVideoAgent](https://arxiv.org/abs/2611.34237))
- **Evaluation boundary — HOG-WAM and Image-to-Video Transfer:** HOG-WAM covers a bounded set of simulated corruptions and robot tasks; Image-to-Video Transfer evaluates three video editors on two related benchmark suites. **Research direction (synthesis):** test sensor and environment shifts for HOG-WAM, and broader editing systems and temporally difficult edits for I2VT, with held-out tasks and consistent human assessment. ([HOG-WAM](https://arxiv.org/abs/2611.34811); [I2VT](https://arxiv.org/abs/2611.34941))
- **Method boundary — MoLT and Floodgates:** Both papers report efficiency gains, but their speed/quality results are bounded by the model sizes and decoding configurations they tested. **Research direction (synthesis):** compare them under matched hardware, model scales, batch sizes, and end-to-end latency/quality budgets, including memory use and longer contexts. ([MoLT](https://arxiv.org/abs/2611.34923); [Floodgates](https://arxiv.org/abs/2611.33896))
- **Evaluation boundary — DocSEAM:** The reported gains cover five multi-page document VQA benchmarks and open-weight models up to 10B parameters. **Research direction (synthesis):** test longer documents, cross-page evidence requiring distant references, and non-VQA document tasks under controlled re-pagination. ([DocSEAM](https://arxiv.org/abs/2611.34420))

## Takeaway

This selected batch combines strong attention for multimodal perception with practical methods for looped-model inference and agentic media generation. The results remain preprint claims, and the evidence does not establish that these methods transfer beyond their tested models, tasks, and benchmarks.

## Method and sources

- **Window and snapshot:** The latest available daily batch at snapshot time was announced at 2026-11-26T01:00:00Z and covered submissions from 2026-11-24T19:00:00Z through 2026-11-25T19:00:00Z; snapshot time was 2026-11-28T03:09:46Z. There was no newer announcement on Nov 27–28 because of the Thanksgiving schedule pause and weekend. arXiv's holiday notice says submissions received from 14:00 ET Nov 25 through 14:00 ET Nov 27 are deferred to 20:00 ET Nov 29.
- **Scope/query:** The configured core corpus was `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`. The broad arXiv API query was `(cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA) AND submittedDate:[202611241900 TO 202611251900]`; it returned 690 entries for this batch. The seven entries are new v1 submissions, not revisions.
- **Supplied signals and ranking:** The user-supplied signal file for the expected Nov 27 batch (`/home/yizhuan/.research/ai/daily/arxiv-trending-ai-daily-2026-11-27.signals.json`) had `pool_size: 0`, `with_attention: 0`, and no candidates; its arXiv source count was 0. It therefore contained no candidate scores to rank. For the prior populated batch, Hugging Face Papers supplied cumulative upvote counts for six selected papers; Hacker News supplied 13 points and 0 comments for Floodgates. The six Hugging Face entries are ordered by their displayed upvotes; Floodgates is shown separately because HN points and HF upvotes are incomparable. These are snapshot totals, not gains during the arXiv window. A zero or missing signal is not evidence of unimportance.
- **Sources unavailable:** The supplied signals file had zero Semantic Scholar records, and a separate Semantic Scholar batch lookup was rate-limited; citation counts are therefore not available here. The top three PDFs were downloaded, but no local PDF text extractor was available, so detailed PDF-section review was not practical and paper summaries rely on the verified arXiv abstracts. All selected arXiv abstract pages were directly checked for title, version, authors, submission timestamp, categories, and abstract.
- **Sources:** [arXiv API batch query](https://export.arxiv.org/api/query?search_query=%28cat%3Acs.AI%20OR%20cat%3Acs.LG%20OR%20cat%3Astat.ML%20OR%20cat%3Acs.CL%20OR%20cat%3Acs.CV%20OR%20cat%3Acs.RO%20OR%20cat%3Acs.NE%20OR%20cat%3Acs.MA%29%20AND%20submittedDate%3A%5B202611241900%20TO%20202611251900%5D&sortBy=submittedDate&sortOrder=descending&start=0&max_results=1000); [arXiv availability schedule](https://info.arxiv.org/help/availability.html); [arXiv Thanksgiving announcement notice](https://blog.arxiv.org/2026/11/25/holiday-announcement-schedule/); [Hugging Face Papers daily data](https://huggingface.co/api/daily_papers?date=2026-11-26); [Hacker News item for Floodgates](https://news.ycombinator.com/item?id=50657370); [Hacker News Algolia record](https://hn.algolia.com/api/v1/search?query=2611.33896&tags=story); [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch); arXiv abstracts linked above.
