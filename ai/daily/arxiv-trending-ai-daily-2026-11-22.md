# arXiv AI daily — announcement batch 2026-11-22 | 8 papers

This batch spans agent behavior, efficient formal instruction translation, VLM privacy and memory, and evaluation for clinical audio and multilingual vision-language models. The short agenda: what changed in agent systems, how efficiency and safety are being measured, and which evidence gaps persist. This is an inferred ranking, not an official arXiv trending chart; the collected attention feeds yielded no matched external-attention candidates, and citation evidence is limited for such recent papers.

## Top papers (ranked)

### 1. [Potential emergence in LLM agents: a statistical physics perspective](https://arxiv.org/abs/2611.27618)
- **Abstract:** The paper models agent states and a statistical-mechanical potential to track how post-training organizes LLM-agent behavior, demonstrating the measures on safety-test selection and physics-reasoning audits.
- **Authors:** Zhuo-Yang Song, Hua Xing Zhu
- **arXiv:** `2611.27618v1` (published 2026-11-20 13:46:24 UTC; categories: `cs.LG`, `cond-mat.stat-mech`, `cs.AI`, `cs.CL`, `nlin.AO`)
- **Evidence for ranking:** Collected score 1.00, entirely from 4 cross-lists (weighted component 1.00); no other positive signal is recorded for this candidate. The pool had no matched Hugging Face or Hacker News attention signals.
- **Claimed contribution:** The authors propose agent states and a partition-function framework for measuring post-training-induced structure, and report two Qwen3.5-9B task demonstrations on arXiv.
- **Caveat:** Methodological boundary: the abstract reports two tasks on one model size/family; broader model and task generality is not established there.
- **Announcement type:** new submission, announcement batch 2026-11-22
- **Themes:** Agents & reasoning; Training & adaptation

### 2. [Efficient Natural Language to Temporal Logic Translation for Real-Time Physical AI](https://arxiv.org/abs/2611.27489)
- **Abstract:** The paper replaces free-form LLM generation for natural-language-to-LTL translation with predefined-answer questions and a classifier, reporting comparable or better accuracy than local LLMs on three benchmarks at up to an order of magnitude lower runtime and energy.
- **Authors:** Oliver Schön, Adrien Banse, John Lygeros, Lars Lindemann
- **arXiv:** `2611.27489v1` (published 2026-11-20 11:35:56 UTC; categories: `cs.AI`, `cs.CL`, `cs.LO`, `cs.RO`, `eess.SY`)
- **Evidence for ranking:** Collected score 1.00, entirely from 4 cross-lists (weighted component 1.00); no other positive signal is recorded for this candidate. Its AI, language, logic, robotics, and systems cross-listing gives it broad relevance within the configured corpus.
- **Claimed contribution:** The authors formulate LTL translation as answering questions with predefined answers and use a System-One classifier; the arXiv abstract reports three-benchmark results and generalization to unseen propositions and temporal patterns.
- **Caveat:** Methodological boundary: the abstract reports three benchmarks but does not specify whether their hardware and operating conditions represent deployed robot constraints.
- **Announcement type:** new submission, announcement batch 2026-11-22
- **Themes:** Robotics & control; Efficient inference & systems

### 3. [SecretAgent: A Multi-Agent Framework for Privacy Protection against Vision Language Models](https://arxiv.org/abs/2611.26936)
- **Abstract:** SecretAgent uses LLM agents to locate privacy-revealing visual evidence and iteratively adapt perturbations, with an appearance-review agent rejecting visible artifacts; the authors report tests across four privacy applications, five datasets, and six VLMs.
- **Authors:** Minda Zhao, Yue Zhang, Mengyu Wang
- **arXiv:** `2611.26936v1` (published 2026-11-20 00:46:20 UTC; categories: `cs.CV`, `cs.AI`, `cs.CR`, `cs.LG`, `cs.MA`)
- **Evidence for ranking:** Collected score 1.00, entirely from 4 cross-lists (weighted component 1.00); no other positive signal is recorded for this candidate. The CV, AI, security, learning, and multiagent cross-lists support its placement among broadly relevant batch papers.
- **Claimed contribution:** The authors introduce gradient-based and gradient-free multi-agent perturbation methods, claiming better image-fidelity/privacy tradeoffs and transfer to other VLMs in their reported evaluation.
- **Caveat:** Methodological boundary: the evidence in the abstract is limited to the stated four applications, five datasets, and six tested VLMs; performance outside those settings is not established.
- **Announcement type:** new submission, announcement batch 2026-11-22
- **Themes:** Safety & alignment; Multimodal & vision-language

### 4. [Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs](https://arxiv.org/abs/2611.26902)
- **Abstract:** Baton maps a small VLM's visual KV cache for use by a larger VLM during uncertain escalations, and the authors report matching re-watching to within about one point while using 28–47% less compute, with a larger per-escalation saving on 64-frame inputs.
- **Authors:** Qiang Zhou, Jianing Deng, Siyan Dong, Jingxian Chen, Han-Yi Lin, Jingtong Hu
- **arXiv:** `2611.26902v1` (published 2026-11-19 23:32:52 UTC; categories: `cs.CV`, `cs.AI`, `cs.CL`, `cs.LG`, `cs.RO`)
- **Evidence for ranking:** Collected score 1.00, entirely from 4 cross-lists (weighted component 1.00); no other positive signal is recorded for this candidate. Its cross-listing spans vision, language, learning, AI, and robotics.
- **Claimed contribution:** The authors propose a per-layer linear map distilled without labels from the large model's answers, and report cascade results on RoboMME and zero-shot transfer to OpenEQA on arXiv.
- **Caveat:** Methodological boundary: the abstract's evidence names RoboMME, OpenEQA, and eight model pairs from four families; it does not establish performance across all VLM architectures or embodied tasks.
- **Announcement type:** new submission, announcement batch 2026-11-22
- **Themes:** Efficient inference & systems; Multimodal & vision-language; Robotics & control

### 5. [SLP-Bench: Evaluating and Improving Acoustic Claims of Reasoning Audio Language Models on Clinical Speech](https://arxiv.org/abs/2611.27810)
- **Abstract:** SLP-Bench evaluates whether acoustic claims in reasoning audio-language-model outputs agree with clinician ratings, and the authors report factuality, stability, and consistency results across five datasets and 25 perceptual dimensions.
- **Authors:** Côme Hosxe, Rachid Riad, Quentin Spinat
- **arXiv:** `2611.27810v1` (published 2026-11-20 16:36:57 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`, `cs.SD`)
- **Evidence for ranking:** Collected score 0.75, solely from 3 cross-lists (weighted component 0.75); no other positive signal is recorded for this candidate. The three AI/language/learning cross-lists give it broad relevance, while the benchmark directly addresses evidence quality in model-generated reasoning.
- **Claimed contribution:** The authors introduce claim-level clinician-grounded evaluation and report that GRPO fine-tuning raised claim balanced accuracy from 0.54 to 0.60 and mean kappa from 0.39 to 0.61, while preserving answer accuracy on per-dimension questions.
- **Caveat:** The authors state that SLP-Bench is available upon request and subject to approval by the providers of each dataset, which constrains immediate independent access.
- **Announcement type:** new submission, announcement batch 2026-11-22
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language

### 6. [Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](https://arxiv.org/abs/2611.27689)
- **Abstract:** Embodied-Harness uses an Actor and Reflector with hierarchical memory to refine reusable robot-execution guidance without updating model parameters; the authors report results on three benchmarks and three real-world manipulation tasks.
- **Authors:** Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan, Wenqiao Zhang, Juncheng Li, Jun Xiao, Siliang Tang, Yueting Zhuang
- **arXiv:** `2611.27689v1` (published 2026-11-20 14:55:07 UTC; categories: `cs.RO`, `cs.AI`, `cs.CV`, `cs.MA`)
- **Evidence for ranking:** Collected score 0.75, solely from 3 cross-lists (weighted component 0.75); Semantic Scholar recorded 0 citations and 0 influential citations at collection time. The robotics/AI/vision/multiagent breadth and reported real-world evaluation support relevance, not measured popularity.
- **Claimed contribution:** The authors propose evidence-based reflection and recursive harness refinement; their abstract reports benchmark success rates of 82.4%, 76.7%, and 94.4%, plus a 96.7% average over three real-world tasks.
- **Caveat:** Methodological boundary: real-world results cover three manipulation tasks; durability and transfer across broader robot platforms or environments are not established in the abstract.
- **Announcement type:** new submission, announcement batch 2026-11-22
- **Themes:** Agents & reasoning; Robotics & control

### 7. [PaMuk-Bench: A Parallel Multilingual Multitask Benchmark for Vision-Language Tasks](https://arxiv.org/abs/2611.27521)
- **Abstract:** PaMuk-Bench provides over 10,000 English prompts translated into Arabic, Danish, French, Hindi, Italian, and Romanian for five vision-language tasks, with parallel text and generated or retrieved images.
- **Authors:** Silviu-Florin Gheorghe, Radu-Stefan Popa, Adriana Valentina Costache, Adrian-Gabriel Chifu, Alessia Amelio, Paul Irofti, Anders Skaarup Johansen, Lallouani Bouchakour, Mohamed Lichouri, Khaled Lounnas, Neelu Madan, Yashvir Malik, Radu Tudor Ionescu
- **arXiv:** `2611.27521v1` (published 2026-11-20 12:13:25 UTC; categories: `cs.CV`, `cs.AI`, `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Collected score 0.75, solely from 3 cross-lists (weighted component 0.75); no other positive signal is recorded for this candidate. Its vision/language/learning/AI breadth and multilingual evaluation focus make it a relevant benchmark contribution in this batch.
- **Claimed contribution:** The authors introduce a parallel multilingual, multitask VLM benchmark and report that zero-shot English and multilingual pretrained models perform worse than fine-tuned counterparts in their experiments.
- **Caveat:** The authors describe translations as semi-automatic and cover six languages; translation quality and conclusions for languages outside that set remain open questions.
- **Announcement type:** new submission, announcement batch 2026-11-22
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language

### 8. [Run One, Get Two: Near-Free Streaming Safety Checks for Local LLMs](https://arxiv.org/abs/2611.26975)
- **Abstract:** ToRA adds a second model as an extra decoding row that shares the generator's weights and KV cache; the authors report under 4% added per-token latency on Qwen3-0.6B while improving on a hidden-state safety probe.
- **Authors:** Soheil Zibakhsh, Pedram Aghazadeh, Farinaz Koushanfar
- **arXiv:** `2611.26975v1` (published 2026-11-20 01:53:11 UTC; categories: `cs.AI`, `cs.CL`, `cs.LG`, `cs.PF`)
- **Evidence for ranking:** Collected score 0.75, solely from 3 cross-lists (weighted component 0.75); Semantic Scholar recorded 0 citations and 0 influential citations at collection time. The additional relevance signal is its direct AI/language/learning cross-listing; no measured external attention was found.
- **Claimed contribution:** The authors propose dual-row decode kernels that share weight reads and KV cache; on Qwen3-0.6B they report higher F1 than a dedicated guard on 12 of 17 benchmarks and 11.8 points more unsafe-response detection than the probe at similar cost.
- **Caveat:** Methodological boundary: the abstract reports evaluation on Qwen3-0.6B; results on larger or different local model families are not established there.
- **Announcement type:** new submission, announcement batch 2026-11-22
- **Themes:** Safety & alignment; Efficient inference & systems

## Trending Research Themes

- **Agent behavior is being made measurable and reusable.** Song and Zhu model agent states and post-training structure; Fan et al. use execution evidence and memory to update a robot-control harness; Zhao et al. use a multi-agent loop to adapt privacy perturbations. These are distinct methods, not evidence of a single established agent architecture.
- **Efficiency is moving into representation and execution choices.** Schön et al. replace general text generation with structured classification for LTL; Zhou et al. transfer visual KV memory instead of re-encoding histories; Zibakhsh et al. share decoding weights and cache for concurrent safety checks. All claim concrete runtime/compute benefits, but their evaluations are task- and model-bounded.
- **Evaluation is shifting from final outputs toward the intermediate evidence and coverage.** Hosxe et al. score acoustic claims against clinician ratings, while PaMuk-Bench makes multilingual task comparisons parallel. These works foreground evidence quality and language coverage rather than only aggregate answer scores.
- **Safety is coupled with usability constraints.** SecretAgent targets privacy without visible image artifacts; ToRA targets streaming safety without a separate full-cost guard model. Both make the protection/utility or protection/cost tradeoff explicit, but neither batch result alone establishes robust deployment safety.
- **The selected list is category-balanced across primary cs.AI (3), cs.CV (3), cs.LG (1), and cs.RO (1).** This describes these eight selected entries, not the full candidate pool.

## Open Problems and Research Directions

- **Author-reported scope — generality of agent-state measures:** Song and Zhu demonstrate their framework on two tasks with Qwen3.5-9B. A useful follow-up would test whether the proposed potential, reward, and entropy patterns replicate across model families, task types, and independently specified state representations.
- **Synthesis — robustness of natural-language-to-formal translation:** Schön et al. report three benchmarks and generalization to unseen propositions and temporal patterns. Evaluate ambiguous, underspecified, and adversarial instructions, then measure end-to-end correctness and resource use on target robot hardware.
- **Synthesis — adaptive privacy attackers:** SecretAgent reports results across several privacy applications, datasets, and VLMs. Test against attackers that know the perturbation procedure and vary image compression, resizing, or downstream transformations, while measuring both privacy leakage and task utility.
- **Synthesis — transfer and escalation policy:** Baton reports results across model pairs and transfer to OpenEQA. Test cache maps and escalation thresholds under distribution shift, longer histories, and different hardware budgets, including failure cases where the small model's representation omits critical evidence.
- **Author-reported access constraint — clinical speech evaluation:** SLP-Bench is available only on request and subject to dataset-provider approval. A reproducibility path using shareable or consented data, plus stratified audits across accents and recording conditions, would help distinguish model failures from dataset effects.
- **Synthesis — long-horizon safety of harness updates:** Embodied-Harness reports three real-world tasks. Longer repeated trials could test whether reflected guidance remains safe and improves rather than overfits, and whether changes transfer between robot embodiments.
- **Author-reported design boundary — multilingual benchmark coverage:** PaMuk-Bench uses semi-automatically translated prompts in six languages. Human validation of translations and expansion to additional low-resource languages and scripts would test whether observed gaps reflect model capability, translation artifacts, or both.
- **Synthesis — safety-check scaling:** ToRA's abstract evaluates Qwen3-0.6B. Profile the accuracy/latency tradeoff across model sizes and hardware, and test whether shared decoding remains reliable under longer contexts and varied unsafe-content distributions.

## Takeaway

This announcement batch has a clear practical thread: making agentic and multimodal AI systems cheaper to run, easier to audit, or safer without sacrificing usability. The signal-backed ordering is weak as a popularity ranking—scores are driven by cross-list breadth, not observed attention—so the strongest takeaway is the set of concrete evaluation and systems questions these preprints expose, not a claim that any result is already settled.

## Method and sources

- **Window:** daily, 2026-11-19 19:00:00 UTC through 2026-11-20 19:00:00 UTC; announcement batch date 2026-11-22 (announced 2026-11-23 01:00 UTC). This uses the latest collected batch, not a substitute older batch.
- **Snapshot:** 2026-11-23 17:05:25 UTC.
- **Corpus:** configured arXiv AI categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`. Candidate pool: 525 records; candidates in this report are all v1 new submissions within the batch window. Each selected title links to its verified arXiv abstract page, which supplied the abstract, authors, submission date, version, and categories.
- **Ranking:** arXiv has no official trending chart. The supplied signals file reports 0 candidates with matched external attention (`with_attention: 0`); Hugging Face (102 collected records) and Hacker News (29) sources were available but produced no matched pool attention. Thus this is best described as notable recent papers, not a popularity ranking. Selected scores are 1.00 for four cross-lists or 0.75 for three, and their score components are solely cross-list breadth. Semantic Scholar collection was marked `ok` for 322 of 525 candidates; only two selected candidates had candidate-specific records, both 0 citations and 0 influential citations. Those are current totals, not citations gained during the window. Missing candidate-specific citation records are not interpreted as zero. A zero score/signal is not evidence of unimportance.
- **Selection and scope:** among equal-score candidates, selection favored a range of AI/ML subfields and directly verifiable contributions; the four papers scoring 1.00 precede those scoring 0.75. The selected primary categories are cs.AI (3), cs.CV (3), cs.LG (1), and cs.RO (1). This is a focused, signal-limited sample, not comprehensive coverage.
- **Paper reading:** all eight arXiv abstract pages were checked. PDF full-text inspection was attempted for the top three, but no local PDF text-extraction utility was available; their contribution and caveat statements therefore stay within the abstract's reported scope. Caveats described as methodological boundaries are explicit limits on what the abstract's evidence demonstrates, not necessarily author-acknowledged failures.
- **Sources:** primary sources are the eight arXiv abstract pages linked above. Attention and citation fields come from `/home/yizhuan/.research/ai/daily/arxiv-trending-ai-daily-2026-11-22.signals.json`; its source statuses for arXiv, Hugging Face, Hacker News, arXiv lookup, and Semantic Scholar are all `ok`. Snapshot generation time in that file: 2026-11-23 17:05:02 UTC.
