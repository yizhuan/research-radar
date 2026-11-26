## Headline

AI, arXiv daily announcement batch 2026-11-26: 8 notable papers. The strongest recurring pattern in this selected set is evidence calibration for visual-language systems, alongside conditional computation and representation-level studies. Spoken agenda: calibrated answers, efficient allocation, and what training changes inside models. arXiv has no official trending chart; this ordering is inferred from cross-list breadth and topical relevance, not readership, and recent-paper citation evidence is limited (the Semantic Scholar source was unavailable).

## Top papers (ranked)

### 1. [FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images](https://arxiv.org/abs/2611.34128)
- **Abstract:** The paper combines pointmap geometric priors with ray-based view selection and local feature aggregation to reconstruct continuous 3D surfaces from unposed images.
- **Authors:** Shenxing Wei, Jinxi Li, Zihui Zhang, Ajay Kumar, Wei Wang, Bo Yang
- **arXiv:** `2611.34128v1` (published 2026-11-25T10:30:24Z; categories: `cs.CV`, `cs.AI`, `cs.CG`, `cs.GR`, `cs.RO`)
- **Evidence for ranking:** The signal file assigns score 1.00, entirely from its cross-list component (4 cross-lists; component 1.00), the highest score tier in this list. No paper-specific HF/HN attention match was recorded; this is a breadth signal, not popularity evidence.
- **Claimed contribution:** The authors report training one model on 9 datasets and zero-shot evaluation on 6 unseen datasets, claiming better geometric accuracy and detail preservation than their baselines.
- **Caveat:** The abstract reports the zero-shot result on six unseen datasets but does not give dataset names or metric values; the comparison remains the authors' reported evaluation.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** 3D vision & reconstruction

### 2. [Learning from Natural Images Untangles Number Sense](https://arxiv.org/abs/2611.33615)
- **Abstract:** The authors introduce a geometric analysis of numerosity and proportion representations and report that visual learning can separate the two representations, improving readout when the quantities conflict.
- **Authors:** Yechan Cho, Hyeonsu Lee, Emma Deneuville, Jaeson Jang
- **arXiv:** `2611.33615v1` (published 2026-11-25T01:41:10Z; categories: `cs.AI`, `cs.CG`, `cs.CV`, `cs.LG`, `q-bio.NC`)
- **Evidence for ranking:** Signal-file score 1.00 (4 cross-lists; cross-list component 1.00), tied for the highest score tier here. No paper-specific HF/HN attention match was recorded; recency breaks the tie with the other four-cross-list selection.
- **Claimed contribution:** The authors report that increased angular separation and reduced overlap between numerosity and proportion subspaces support more robust readout, and that separation also appears with self-supervised or synthetic-image training.
- **Caveat:** The evidence concerns the neural-network training and numerical-conflict settings examined in the paper; it does not establish that current deployed vision-language models have human-like number sense.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Interpretability; Training & adaptation

### 3. [HumblePRM: Improving VLM Abstention in Ambiguous Situations through Process Reward Modeling](https://arxiv.org/abs/2611.33452)
- **Abstract:** HumblePRM separately rewards visual scene description and the decision about whether that evidence is sufficient, and the authors report more uncertainty-driven abstention on ambiguous images with roughly unchanged accuracy on clear images.
- **Authors:** Saket Reddy, Ke Yang, ChengXiang Zhai
- **arXiv:** `2611.33452v1` (published 2026-11-24T21:20:03Z; categories: `cs.CV`, `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Signal-file score 0.75, entirely from 3 cross-lists (component 0.75). This is the strongest cross-list tier below the two four-cross-list papers; no paper-specific HF/HN attention match was recorded.
- **Claimed contribution:** The authors propose a lightweight process reward model for separately supervising perception and confidence calibration, and report transfer of the abstention improvement to Gemma 4 E4B.
- **Caveat:** The abstract gives no effect sizes or detailed test-set scope, and the reported transfer is to one named model; broad deployment reliability is not established by this abstract.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Safety & alignment; Evaluation & benchmarks; Multimodal & vision-language

### 4. [Two Timescales of Forgetting in Fine-tuning of Language Models: Fast Behavioral Suppression and Slow Representational Drift](https://arxiv.org/abs/2611.33302)
- **Abstract:** Using controlled grammar models and a natural-language setup, the authors report that fine-tuning suppresses generation of removed rules faster than it erases the internal representations associated with them.
- **Authors:** Yilin Luo, Jin Hwa Lee, Andrew M. Saxe, Antonio Sclocchi
- **arXiv:** `2611.33302v1` (published 2026-11-24T19:00:45Z; categories: `cs.LG`, `cond-mat.dis-nn`, `cs.CL`, `stat.ML`)
- **Evidence for ranking:** Signal-file score 0.75, entirely from 3 cross-lists (component 0.75), matching the third-place score tier. No paper-specific HF/HN attention match was recorded; its placement within the tier reflects recency and fit to the representation/training theme.
- **Claimed contribution:** The authors distinguish a fast change in behavior from slower representational drift during supervised fine-tuning and report analogous effects in a natural-language setup.
- **Caveat:** The study's central mechanistic result uses a controlled grammar model; the abstract's natural-language experiment supports an analogy, not a universal claim about forgetting across model families or fine-tuning regimes.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Training & adaptation; Interpretability

### 5. [Out of Sight, Not Out of Clues: Can Video LLMs Guess from Partial Evidence?](https://arxiv.org/abs/2611.34126)
- **Abstract:** ClueProbe labels video questions as answerable, guessable, or unanswerable, and the authors report that Video LLMs often perceive clues but fail to judge whether partial evidence supports a guess.
- **Authors:** Luoxi Zhang, Jiawei Liu, Yanlin Luo, Peiyang He, Junlin Zhu, et al.
- **arXiv:** `2611.34126v1` (published 2026-11-25T10:30:08Z; categories: `cs.CV`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** Signal-file score 0.50, entirely from 2 cross-lists (component 0.50). No paper-specific HF/HN attention match was recorded; the within-tier order follows recency and direct fit to the calibration theme.
- **Claimed contribution:** The authors introduce a 1,721-question, 598-video benchmark and report that targeted supervision raises appropriate guessing from 1.6% to 40.4% without extra false refusals.
- **Caveat:** The reported benchmark and fine-tuning evidence is tied to 598 videos and the tested set of 10 models; transfer to other video domains is not established here.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language; Safety & alignment

### 6. [Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades, and Agent Orchestration](https://arxiv.org/abs/2611.34112)
- **Abstract:** This systematic review unifies token-level expert gating, query-level model cascades, and task-level agent orchestration under an inspect-then-allocate framing for conditional computation.
- **Authors:** Dat Tat Mai, Hung Tran Quy, Thai Viet Pham, James Jin Kang
- **arXiv:** `2611.34112v1` (published 2026-11-25T10:15:28Z; categories: `cs.AI`, `cs.LG`, `cs.MA`)
- **Evidence for ranking:** Signal-file score 0.50, entirely from 2 cross-lists (component 0.50). No paper-specific HF/HN attention match was recorded; it is included for its direct relevance to core AI systems and agent orchestration.
- **Claimed contribution:** The authors synthesize 2,289 studies selected from 13,884 records, identifying computational overhead as a recurring bottleneck and reporting different safeguards across token-, query-, and task-level routing.
- **Caveat:** This is a literature synthesis covering studies through September 2026, not a new controlled system comparison; conclusions depend on its study-selection and methodological coding frame.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Efficient inference & systems; Agents & reasoning

### 7. [How Much Effort Does an AI Code Reviewer Need? Evidence from Claude 5.5 Models on Plausible-but-Wrong Patches](https://arxiv.org/abs/2611.33639)
- **Abstract:** In a study of 90 agent-written Django patches, the authors compare low, medium, and high review effort and report that high effort catches more wrong patches than low effort, while medium effort is non-inferior to high for the preregistered Opus comparison at lower cost.
- **Authors:** Zax Shen, Hanling Zhang, Zixu Wang
- **arXiv:** `2611.33639v1` (published 2026-11-25T02:07:31Z; categories: `cs.AI`, `cs.LG`, `cs.SE`)
- **Evidence for ranking:** Signal-file score 0.50, entirely from 2 cross-lists (component 0.50). No paper-specific HF/HN attention match was recorded; its place in this score tier reflects recency and relevance to practical AI-agent evaluation.
- **Claimed contribution:** The authors provide preregistered evidence on the cost/quality trade-off of reviewer effort, reporting that Opus at medium effort cost 20% less than high and met their 15-percentage-point non-inferiority margin.
- **Caveat:** The comparison covers 90 Django patches and three Claude 5.5 models; medium effort was not shown non-inferior for Sonnet or Haiku, limiting generalization beyond this setting.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Evaluation & benchmarks; Agents & reasoning

### 8. [What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench](https://arxiv.org/abs/2611.33943)
- **Abstract:** The authors audit SkillsBench and reanalyse 7,554 public trials, finding that observed negative task-level skill effects were not statistically significant after pooled multiple-testing correction and were vulnerable to run-sampling noise.
- **Authors:** Haozhe Zhang, Zhen Long
- **arXiv:** `2611.33943v1` (published 2026-11-25T08:02:04Z; categories: `cs.AI`, `cs.CL`, `cs.SE`)
- **Evidence for ranking:** Signal-file score 0.50, entirely from 2 cross-lists (component 0.50). No paper-specific HF/HN attention match was recorded; it is included as an evaluation-quality counterpoint to the code-review study.
- **Claimed contribution:** The authors report a source-code audit and noise-aware reanalysis, including no statistically significant pooled task-level reductions and no significant held-out benefit for the tested skill-gating strategy.
- **Caveat:** There were at most three runs per condition in each paired cell, so small effects remain difficult to resolve; the reanalysis is bounded by the public trials and benchmark harnesses examined.
- **Announcement type:** new submission, announcement-batch date 2026-11-26
- **Themes:** Evaluation & benchmarks; Agents & reasoning

## Trending Research Themes

- Evidence sufficiency and calibrated responses recur in two visual-language papers: HumblePRM separates perception from confidence calibration, while ClueProbe distinguishes answering, guessing from partial clues, and abstaining. The shared methodological move is to supervise intermediate evidence judgments rather than only final correctness; this is a pattern in this selected batch, not evidence of a field-wide shift.
- Conditional allocation connects systems and agent evaluation. The review *Not Every Input Needs Everything* unifies routing across model layers, requests, and multi-agent tasks; the code-review study separately measures how effort budgets affect patch checking. Together they foreground compute/latency or review-cost trade-offs, but neither establishes a general optimal routing policy.
- Training and internal representations are examined directly in two different settings: *Learning from Natural Images Untangles Number Sense* measures separation between numerical representations, while *Two Timescales of Forgetting* distinguishes behavioral suppression from representational drift. Both point to the value of testing internal state changes rather than relying only on final task scores.
- Evaluation validity is an explicit concern in *How Much Effort Does an AI Code Reviewer Need?* and the *SkillsBench* audit, which use preregistration or source-level scrutiny and report limits from sample size, repeated trials, or harness design. Their results argue for stronger measurement, not for a broad conclusion that AI review or skills are effective or ineffective.
- *FoundSurface* is a separate 3D reconstruction signal in this selection: it combines pointmap priors with ray-based continuous surface estimation and reports zero-shot tests on unseen datasets. One paper is not enough to establish a wider shift toward this approach.

## Open Problems and Research Directions

- **Author-reported open problem:** ClueProbe says current binary answerable/unanswerable evaluations miss partial evidence, while HumblePRM targets abstention when visual evidence is ambiguous. **Research direction (synthesis):** evaluate both methods on a shared, distribution-shifted suite with graded evidence levels; report calibration, appropriate guessing, false refusals, and accuracy together. (ClueProbe; HumblePRM)
- **Author-reported open problem:** The conditional-computation review identifies compute overhead across routing scales and notes asymmetry in uncertainty safeguards; the code-review study finds effort settings change both errors caught and cost. **Research direction (synthesis):** compare token-, request-, and task-level allocation under matched latency/compute budgets, with calibrated uncertainty and explicit fallback behavior. (Not Every Input Needs Everything; How Much Effort Does an AI Code Reviewer Need?)
- **Author-reported open problem:** Two Timescales of Forgetting starts from uncertainty about whether behavioral suppression coincides with erasure of latent representations; the number-sense study finds representation changes under several training regimes. **Research direction (synthesis):** replicate representation probes across architectures, data mixtures, and fine-tuning schedules, then test whether internal changes predict out-of-distribution behavior. (Two Timescales of Forgetting; Learning from Natural Images Untangles Number Sense)
- **Author-reported open problem:** The SkillsBench audit notes at most three runs per condition per paired cell, while the code-review paper's conclusions depend on a 90-patch Django sample. **Research direction (synthesis):** use larger repeated trials, independent graders, and multiple codebases/harnesses to estimate uncertainty in both skill effects and reviewer-effort trade-offs. (What Does Skill Lift Actually Measure?; How Much Effort Does an AI Code Reviewer Need?)

## Takeaway

The most concrete recurring signal in this batch is careful judgment about evidence—when a model should answer, guess, or defer—paired with work on allocating computation and inspecting representations. Since the available ranking evidence is cross-list breadth rather than measured attention, treat this as a map of notable new work, not a popularity ranking.

## Method and sources

- **Window:** Daily arXiv announcement batch for 2026-11-26; submission/revision interval 2026-11-24 19:00:00 UTC through 2026-11-25 19:00:00 UTC; announced 2026-11-26 01:00:00 UTC. Snapshot time: 2026-11-26T03:07:59Z. This is the current batch, not a prior-batch fallback.
- **Scope/query:** Core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, `cs.MA`; the signal collector used the category union `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`. Candidate pool: 421 records.
- **Inference:** Ranking is inferred, not official. The supplied deterministic signal file reports no paper-specific Hugging Face or Hacker News attention matches in the candidate pool (`with_attention: 0`). The selected scores (1.00, 0.75, or 0.50) are entirely cross-list components (4, 3, or 2 cross-lists respectively); score tiers come first, then topical relevance and recency break ties. A zero or missing attention signal is not evidence of unimportance. Semantic Scholar citation data were unavailable for this collection, so no citation-based ranking was possible. No selected paper is represented as a revision; each is verified as v1/new submission.
- **Source status and verification:** Signal file: `/home/yizhuan/.research/ai/daily/arxiv-trending-ai-daily-2026-11-26.signals.json` (generated 2026-11-26T03:05:01Z; arXiv and HF/HN collection completed, Semantic Scholar unavailable). All eight selected v1 abstract pages were fetched and checked for title, authors, date, and categories. The configured `web_extract` backend was unavailable, so primary pages were checked by direct HTTP retrieval. PDF text extraction was not available in this runtime; claims and caveats above are grounded in the verified abstracts and their stated evaluation scope.
- **Selected primary sources:** [FoundSurface](https://arxiv.org/abs/2611.34128); [Learning from Natural Images Untangles Number Sense](https://arxiv.org/abs/2611.33615); [HumblePRM](https://arxiv.org/abs/2611.33452); [Two Timescales of Forgetting](https://arxiv.org/abs/2611.33302); [ClueProbe](https://arxiv.org/abs/2611.34126); [Not Every Input Needs Everything](https://arxiv.org/abs/2611.34112); [AI Code Reviewer Effort](https://arxiv.org/abs/2611.33639); [SkillsBench Audit](https://arxiv.org/abs/2611.33943).
