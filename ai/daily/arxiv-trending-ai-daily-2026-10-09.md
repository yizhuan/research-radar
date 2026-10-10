# arXiv AI papers — Friday, 9 October 2026

Eight notable papers from the latest arXiv AI announcement batch; the latest batch is used because Saturday, 10 October has no newer announcement in the checked listings. The corpus leans toward evaluation and oversight: whether monitors catch deception, judges are reliable, benchmarks measure their stated construct, and world models reproduce interactions. Today’s agenda: safety monitoring, trustworthy measurement, and multimodal/robotic models. arXiv has no official trending chart; with sparse independent attention and citation evidence for this very recent batch, the ordering below is inferred from surfaced external discussion, cross-list breadth, and concrete empirical scope—not readership or downloads.[17][18][20]

## Top papers (ranked)

### 1. [Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception](https://arxiv.org/abs/2610.12445v1)
- **Abstract:** The authors train white-box probes on a broad falsehood dataset and report strong detection of agentic and introspective deception, including 98.8% AUC on SHADE-Arena.[1]
- **Authors:** Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba, Adam Gleave, Chris Cundy
- **arXiv:** `2610.12445v1` (published 2026-10-08T17:58:13Z; categories: `cs.LG`, `cs.AI`)[1]
- **Evidence for ranking:** Cross-listed in machine learning and AI; an independent research roundup also surfaced, alongside the paper’s concrete multi-setting evaluation. This supports topical prominence, not readership claims.[1][9]
- **Claimed contribution:** The paper reports that multi-layer, multi-token white-box probes trained on FIBS can detect falsehoods in SHADE-Arena and generalize to several introspective-deception tests.[1]
- **Caveat:** The authors say FIBS is largely artificial and mostly off-policy; probe utility is also bounded by what the probed model believes and which persona is active.[1]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Safety & alignment; Evaluation & benchmarks; Interpretability

### 2. [What 30,000 Hours of Ego-centric Video Does Not Teach](https://arxiv.org/abs/2610.12464v1)
- **Abstract:** Across a 300-to-30,000-hour training ladder, the authors find that more egocentric video improves agent and object-interaction fidelity unevenly, with object dynamics remaining a bottleneck.[2]
- **Authors:** Jiahua Dong, Anurag Bagchi, Yash Jangir, Muhammad Zubair Irshad, Sergey Zakharov, et al.
- **arXiv:** `2610.12464v1` (published 2026-10-08T17:59:49Z; categories: `cs.CV`)[2]
- **Evidence for ranking:** A specialist robotics-data article discussed the result, and the paper evaluates a substantial 30,000-hour corpus on an out-of-distribution interaction benchmark. The external mention is a discovery signal, not a popularity metric.[2][10]
- **Claimed contribution:** The authors introduce an object-centric adaptive noise-scheduling supervision scheme and report that it raises object fidelity, while an interaction gap remains.[2]
- **Caveat:** The authors note that data volume and optimization budget are coupled in their scale ladder, and both training and evaluation draw on a limited collection protocol; extrapolation beyond the tested range remains uncertain.[2]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks; Robotics & control

### 3. [Cited but Not Consulted: A Counterfactual Audit of Legal Chain-of-Thought Faithfulness](https://arxiv.org/abs/2610.12361v1)
- **Abstract:** In tests across seven open-weight models and four legal-reasoning benchmarks, correct authority citations often did not mean a model’s verdict changed when that authority was counterfactually replaced.[3]
- **Authors:** Saisab Sadhu, Shreeyans Arora, Pratinav Seth
- **arXiv:** `2610.12361v1` (published 2026-10-08T17:26:17Z; categories: `cs.AI`, `cs.CL`, `cs.CY`)[3]
- **Evidence for ranking:** It spans AI, language, and cybersecurity categories and has surfaced in an OpenReview record and separate technical discussion. The ordering reflects this cross-field relevance and the paper’s multi-model counterfactual audit, not measured readership.[3][11][12]
- **Claimed contribution:** The authors propose an authority-swap test with internal commitment tracking; they report that naming the correct authority is a poor proxy for whether the verdict depends on it.[3]
- **Caveat:** The authors flag moderate sample sizes and an unresolved confound: replacing an authority can also change the question being asked. Their conclusions are behavioral and limited to the stated prompts and benchmarks.[3]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Evaluation & benchmarks; Interpretability; Safety & alignment

### 4. [OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport](https://arxiv.org/abs/2610.12375v1)
- **Abstract:** OnTrack compares an agent’s live steps and dependencies with prior successful traces to flag process anomalies; on SWE-bench trajectories the authors report early discrimination and compute savings from aborting likely failures.[4]
- **Authors:** Babak Barazandeh, Connor Swanson, Chinmay Kulkarni, Nikhil Mungel
- **arXiv:** `2610.12375v1` (published 2026-10-08T17:32:08Z; categories: `cs.AI`, `cs.CL`, `cs.CY`, `cs.LG`)[4]
- **Evidence for ranking:** It is cross-listed across four configured AI categories and has an independent technical write-up; the paper also reports a held-out trajectory evaluation. These are relevance/discovery signals, not a popularity count.[4][13]
- **Claimed contribution:** The authors present a streaming, structure-aware optimal-transport monitor intended to intervene during an agent run, rather than score logs only after completion.[4]
- **Caveat:** The authors explicitly distinguish process-anomaly detection from predicting task success; they report that generic signals approach chance when trajectory length is controlled, and dependency extraction remains a constraint.[4]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Agents & reasoning; Safety & alignment; Evaluation & benchmarks

### 5. [Searching for “Harmful Refusal”: A Psychometric Audit of an AI Safety Benchmark](https://arxiv.org/abs/2610.12409v1)
- **Abstract:** The authors find that HELM Safety’s HarmBench results do not support treating “harmful refusal” as one measurable dimension; multi-factor models fit better than a single score.[5]
- **Authors:** Christopher M. Stewart, Preston Botter, Natalie Sarabosing, Muye Zhang, Rachel Phinnemore, et al.
- **arXiv:** `2610.12409v1` (published 2026-10-08T17:46:43Z; categories: `cs.AI`)[5]
- **Evidence for ranking:** The paper is accompanied by a public analysis repository and examines a benchmark used to summarize safety behavior. That artifact and practical evaluation relevance support inclusion; they do not establish popularity.[5][14]
- **Claimed contribution:** The authors apply multidimensional item-response and differential-item-functioning analyses, arguing that a single aggregate score blends distinct response behaviors.[5]
- **Caveat:** The authors limit their results to the HELM Safety model pool and operationalization they tested; scores rely on two LLM judges, and they do not report a replication using HarmBench’s original classifier pipeline.[5]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Safety & alignment; Evaluation & benchmarks

### 6. [All Verdicts are Not Equal: Rethinking LLM Judge Reliability](https://arxiv.org/abs/2610.12083v1)
- **Abstract:** An audit of six judges across four benchmarks finds that repeated-run consistency, order invariance, and correctness can diverge; the paper introduces a trustworthy-verdict metric combining those properties.[6]
- **Authors:** Vineet Kumar, Darshita Rathore, Anindya Moitra
- **arXiv:** `2610.12083v1` (published 2026-10-08T14:55:29Z; categories: `cs.CL`, `cs.AI`)[6]
- **Evidence for ranking:** Cross-listed in language and AI, with a broad factorial audit over models, prompts, candidate order, temperatures, and repetitions. Given little independent attention evidence in the checked sources, this is included for demonstrated methodological scope, not claimed popularity.[6]
- **Claimed contribution:** The authors define a trustworthy-verdict rate and show how candidate-order flips impose an accuracy ceiling; they also report that holistic rubric scoring improves the metric in their comparisons.[6]
- **Caveat:** The authors test only four English-language pairwise benchmarks and closed-weight models; transfer to other languages or listwise ranking remains untested.[6]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Evaluation & benchmarks

### 7. [On the estimation and validity of AI time horizons—a statistical look at the METR plot](https://arxiv.org/abs/2610.12466v1)
- **Abstract:** Reanalyzing 228 tasks and 26 AI systems with splines and item-response theory, the authors find a near-flat task-difficulty region around 2–30 minutes, challenging a uniformly log-linear reading of time horizons.[7]
- **Authors:** Drew T. Nguyen, William Fithian
- **arXiv:** `2610.12466v1` (published 2026-10-08T17:59:50Z; categories: `cs.AI`)[7]
- **Evidence for ranking:** The paper addresses a widely used capability-measurement approach and also has an OpenReview record; its contribution is a statistical reanalysis with cross-validated scoring and diagnostic plots. These are relevance signals, not a citation-velocity claim.[7][15]
- **Claimed contribution:** The authors propose fitting flexible difficulty curves and recommend interpreting time-horizon estimates alongside construct-validity diagnostics.[7]
- **Caveat:** The analysis is grounded in the available task range; the authors caution that newly added, longer tasks need not preserve the currently observed curve shape.[7]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Evaluation & benchmarks

### 8. [OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning](https://arxiv.org/abs/2610.12458v1)
- **Abstract:** OmniCapBench evaluates audio-visual captions as atomic entity, shot, and event units; on 786 annotated videos, the authors report that current models struggle with long-horizon cross-modal alignment and identity persistence.[8]
- **Authors:** Zhongyu Yang, Jiale Tao, Ruitao Chen, Zuhao Yang, Yingfang Yuan, et al.
- **arXiv:** `2610.12458v1` (published 2026-10-08T17:59:21Z; categories: `cs.CV`)[8]
- **Evidence for ranking:** It is indexed on Hugging Face’s papers page and contributes a concrete, annotated benchmark for multimodal model evaluation. External attention signals are sparse, so it ranks by demonstrated evaluation relevance rather than asserted popularity.[8][16]
- **Claimed contribution:** The paper separates deterministic structural checks from localized semantic comparisons, aiming to make audio-visual caption errors easier to diagnose.[8]
- **Caveat:** The authors limit the benchmark to videos shorter than five minutes and note that annotations cannot credit every valid fact outside their reference scope; evaluator-model bias is also not fully excluded.[8]
- **Announcement type:** new submission, 2026-10-09 announcement batch
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks

## Trending Research Themes

- **Measurement is the clearest shared thread.** The METR reanalysis questions a single curve for capability horizons; the refusal audit and LLM-judge study test whether common scores measure what their labels imply.[5][6][7]
OmniCapBench replaces holistic caption judgments with localized units.[8]
- **Agent safety is shifting toward runtime and internal-state evidence in this batch.** Caught in the Act studies hidden-state probes, while OnTrack focuses on live process traces; the legal audit tests whether generated citations causally affect decisions.[1][3][4]
- **Multimodal/robotics work emphasizes interaction fidelity, not only plausible outputs.** The 30,000-hour world-model study isolates object dynamics, while OmniCapBench diagnoses timing and audio-visual links.[2][8]
- These are patterns in this selected announcement batch, not evidence of a field-wide breakthrough or trend line; the examples are the probe-monitoring, runtime-monitoring, and benchmark-validity studies above.[1][4][5]

## Open Problems and Research Directions

- **Probe generalization and persona coverage — author-stated boundary.** Caught in the Act says probes may miss behavior tied to a different active persona and calls for more work on limits of model introspection. A next test would hold model and task fixed while varying persona, hidden goals, and on-policy deployment contexts, reporting false-positive and false-negative rates.[1]
- **Isolated interaction dynamics — author-stated boundary.** The world-model paper says its data ladder couples volume with optimization and that object fidelity remains behind agent fidelity. Follow-up work could independently vary data volume and training steps, then replicate object-interaction tests across capture protocols and longer horizons.[2]
- **Causal faithfulness of explanations — author-stated boundary.** The legal audit leaves an authority-swap confound and moderate sample size. A useful follow-up would manipulate authority content while holding the question wording constant, expand authority pairs, and validate behavioral measures against activation-level causal tests.[3]
- **Monitoring unseen failure modes — author-stated boundary.** OnTrack reports weak generic signals on homogeneous traces and does not predict success. Test whether task-matched references or formal verifiers improve detection of semantically wrong but structurally normal traces, with false-stop costs reported.[4]
- **Benchmark construct validity — author-stated boundary.** The refusal audit notes model-pool and judge dependence; the judge-reliability paper is limited to English pairwise tasks. Replicate item-level construct and judge-stability analyses with human-verified labels, multilingual data, and listwise ranking protocols.[5][6]
- **Capability-curve extrapolation — author-stated boundary.** The METR reanalysis cautions that longer-task regions may bend differently. New benchmarks should publish calibration plots and evaluate flexible models as longer tasks enter the range, rather than assuming the current curve extrapolates.[7]
- **Long-form audiovisual grounding — author-stated boundary.** OmniCapBench covers videos under five minutes and a finite annotation scope. Extend it to longer clips, open-world valid details, and independent reference construction; assess whether its structured scoring stays reliable across evaluator families.[8]

## Takeaway
This batch is unusually evaluation-heavy: several papers probe whether safety scores, judge verdicts, legal explanations, and capability curves support the interpretations people routinely attach to them.[3][5][6]
The practical next step across these studies is replication under broader tasks, populations, and deployment conditions; none alone establishes a settled field-wide result.[1][2][4]

## Method and sources

- **Window:** daily; selected arXiv announcement batch Friday, 2026-10-09 (used because the report was run Saturday, 2026-10-10 and no newer batch appeared in the checked listings).[17][18][20]
The selected papers’ arXiv API first-publication timestamps fall on 2026-10-08 UTC; all eight are v1 submissions.[1][2][3]
- **Snapshot:** 2026-10-10T00:13:33Z.
- **Corpus:** The latest batch was checked across all eight configured AI categories. The `cs.AI`, `cs.LG`, and `stat.ML` pages show 302, 324, and 51 entries respectively.[17][18][19]
The `cs.CL`, `cs.CV`, and `cs.RO` pages show 144, 207, and 105 entries.[20][21][22]
The `cs.NE` and `cs.MA` pages show 3 and 15 entries.[23][24] Cross-list overlaps were retained only once.
- **Inference:** arXiv has no official trend ranking. I checked each selected abstract and, for the leading papers, the available full HTML text. Ranking weighs surfaced independent discussion where found, category breadth, concrete empirical scope, and topical relevance. It does not use author/institution prestige or unobserved download/view counts. Semantic Scholar citation counts were unavailable from the sources checked (the Graph API request returned HTTP 429), so no citation totals or citation momentum are claimed.
- **Sources:** arXiv abstract pages are linked in each entry. External discovery signals are linked inline in the relevant ranking evidence. The exact sources list follows.

## Sources

[1] https://arxiv.org/abs/2610.12445v1
[2] https://arxiv.org/abs/2610.12464v1
[3] https://arxiv.org/abs/2610.12361v1
[4] https://arxiv.org/abs/2610.12375v1
[5] https://arxiv.org/abs/2610.12409v1
[6] https://arxiv.org/abs/2610.12083v1
[7] https://arxiv.org/abs/2610.12466v1
[8] https://arxiv.org/abs/2610.12458v1
[9] https://www.one9founders.com/research/2610.12445
[10] https://www.humanoidsdata.com/articles/egocentric-video-world-model-object-fidelity
[11] https://openreview.net/forum?id=DB0hTly8II
[12] https://agentic-design.ai/news-hub/cited-but-not-consulted-counterfactual-audit-legal-chain-thought-faithfulness-bdc0a7
[13] https://dev.to/mech_app_ai/ontrack-real-time-agent-monitoring-via-streaming-optimal-transport-1dkp
[14] https://github.com/cmstewart/harmful-refusal-audit
[15] https://openreview.net/forum?id=IfzVLvrymT
[16] https://huggingface.co/papers/2610.12458
[17] https://arxiv.org/list/cs.AI/recent?show=1000
[18] https://arxiv.org/list/cs.LG/recent?show=1000
[19] https://arxiv.org/list/stat.ML/recent?show=1000
[20] https://arxiv.org/list/cs.CL/recent?show=1000
[21] https://arxiv.org/list/cs.CV/recent?show=1000
[22] https://arxiv.org/list/cs.RO/recent?show=1000
[23] https://arxiv.org/list/cs.NE/recent?show=1000
[24] https://arxiv.org/list/cs.MA/recent?show=1000
