# arXiv Trending AI — 2026-09-10 batch

## Headline
The strongest signal in the latest batch is a shift from raw model capability toward trustworthy deployment: papers stress evaluation contamination and awareness, serving-route measurement, tool/function-call generalization, and robustness under quantization. A second cluster applies learned world models and selective adaptation to physical control and unlearning.

arXiv has no official trending chart. This is an inferred ranking of notable papers from the latest announcement batch, using cross-list breadth, substantive benchmarks or released artifacts, independent technical discussion/search visibility, and (where available) Semantic Scholar metadata. Very recent papers have sparse citation data, so this is not a most-read or most-downloaded list.

Window: latest daily announcement batch, 2026-09-10 UTC (papers submitted 2026-09-08–10; the arXiv listing labels the batch Thu, 10 Sep 2026). Snapshot: 2026-09-11 00:10 UTC. Core categories: cs.AI, cs.LG, stat.ML, cs.CL, cs.CV, cs.RO, cs.NE, cs.MA.

## Top papers (ranked)

### 1. [IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier](https://arxiv.org/abs/2609.10494)
- **Abstract:** The paper proposes IB2, a protocol that evaluates enterprise AI by the complete serving route—weights, precision, output contract, harness, and reliability—instead of by an advertised model identifier.
- **Authors:** Blake Stenstrom, Charangan Vasantharajan, Brian Sathianathan
- **arXiv:** `2609.10494v1` (published 2026-09-09 17:31 UTC; categories: `cs.CL`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Cross-listed across three core AI categories; 42-page protocol with released algorithms, schemas, and manifests; independent search discussion; citation data unavailable because of API rate limiting and the paper is new.
- **Claimed contribution:** The authors report a gold-blind capability-binding preflight, reliability-inclusive scoring, and score-blind adjudication, plus an 11-system reference instantiation with 128 locked tasks and 987 assertions.
- **Caveat:** The sealed corpus means the procedure—not the full evaluation corpus—is the released artifact; the authors also note confounding from access mode, harness generation, and tool-call parsing.
- **Announcement type:** new submission, 2026-09-10 announcement batch
- **Themes:** Evaluation & benchmarks; Efficient inference & systems; Safety & alignment

### 2. [MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes](https://arxiv.org/abs/2609.10016)
- **Abstract:** MetroLLM-Bench is a 955-case benchmark testing language models as the policy layer of a transit kiosk across six real metro systems, structured tool calls, terminal states, and adversarial cases.
- **Authors:** Remco Hendriks
- **arXiv:** `2609.10016v1` (published 2026-09-09 10:46 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** Three-way core-category cross-list; released benchmark, harness, guide, and fine-tuned students; independent coverage; unusually concrete held-out results; citation data unavailable because of API rate limiting.
- **Claimed contribution:** The paper reports 26 evaluated models and finds a 4B Qwen 3.5 PEFT student reached 91.3 Tier-1 versus 90.6 and 90.0 for the named GPT-5.6 configurations, while a rule baseline reached 84.6.
- **Caveat:** Results are specific to the benchmark, training scale, serving configurations, and a 75/25 split; six of eight Tier-2 components use a language-model judge.
- **Announcement type:** new submission, 2026-09-10 announcement batch
- **Themes:** Evaluation & benchmarks; Agents & reasoning; Efficient inference & systems

### 3. [Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization](https://arxiv.org/abs/2609.10464)
- **Abstract:** SG-JEPA extends a JEPA world model with physics-parameter action conditioning and multi-step latent rollout training for zero-shot generalization across gravitational fields.
- **Authors:** Andy Zeyi Liu, Haoran Sun, Lucas Baker, Randall Balestriero, John Sous
- **arXiv:** `2609.10464v1` (published 2026-09-09 17:08 UTC; categories: `cs.LG`, `cs.AI`, `cs.CV`)
- **Evidence for ranking:** Three core-category cross-list; project page, code/checkpoint search results, and independent technical discussion; reported gains are substantial but citation data is unavailable because of API rate limiting.
- **Claimed contribution:** The authors report up to 2x lower open-loop prediction error on 2D data and up to 2.5x higher control success on 3D robotic data versus DINO-WM, attributing most gains to better encoder features.
- **Caveat:** The evidence is from designed dynamical tasks and independent diffusion policies; the abstract does not establish transfer to real-world physics.
- **Announcement type:** new submission, 2026-09-10 announcement batch
- **Themes:** Robotics & control; Multimodal & vision-language; Training & adaptation

### 4. [Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs](https://arxiv.org/abs/2609.10439)
- **Abstract:** FOM-UL selects transformer layers with high forget-set influence and low retain-set sensitivity to improve targeted unlearning, utility retention, and robustness after quantization.
- **Authors:** Ravi Ranjan, Olivera Kotevska, Agoritsa Polyzou
- **arXiv:** `2609.10439v1` (published 2026-09-09 16:50 UTC; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** Cross-listed in cs.LG/cs.AI; conference-paper comment, full evaluation across TOFU, KnowUnDo, and MUSE-style tests, HTML paper, and independent technical discussion; citation data unavailable because of API rate limiting.
- **Claimed contribution:** The authors report lower residual memorization than several baselines while preserving retain utility, including under 8-bit and 4-bit post-training quantization and adversarial prompting.
- **Caveat:** The paper explicitly makes no formal guarantee of erasure; results remain empirical and benchmark-dependent.
- **Announcement type:** new submission, 2026-09-10 announcement batch
- **Themes:** Safety & alignment; Training & adaptation; Efficient inference & systems

### 5. [Strangers to Themselves: What Language Models Say About Themselves Is Generic](https://arxiv.org/abs/2609.09899)
- **Abstract:** Across nine behavioral evaluations, the paper tests whether language models can predict their own behavior and finds self-reports are weak, generic-agent answers perform similarly, and first-person framing is flattering.
- **Authors:** Phil Blandfort, Urja Pawar
- **arXiv:** `2609.09899v1` (published 2026-09-09 08:56 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.CV`, `cs.CY`)
- **Evidence for ranking:** Broadest cross-list among the selected new papers, spanning four core AI categories plus cs.CY; unusually direct safety/evaluation implication; citation data unavailable because of API rate limiting.
- **Claimed contribution:** The authors report self-prediction correlation of +0.04, rising to +0.24 with exact-item information, while generic-agent prompting reaches +0.28; model scale did not produce self-specific gains.
- **Caveat:** The abstract reports nine evaluations but the generality of the finding depends on the chosen tasks, prompts, and behavioral distributions.
- **Announcement type:** new submission, 2026-09-10 announcement batch
- **Themes:** Safety & alignment; Evaluation & benchmarks; Interpretability

### 6. [A Later Test Set Is Not a New Domain: Pretraining Familiarity Survives a Contamination-Free Hold-Out](https://arxiv.org/abs/2609.10357)
- **Abstract:** A post-release time-series hold-out shows that temporal freshness removes direct test-window memorization but not domain familiarity from pretraining.
- **Authors:** Mahdi Naser Moghadasi, Faezeh Ghaderi
- **arXiv:** `2609.10357v1` (published 2026-09-09 15:52 UTC; categories: `cs.LG`)
- **Evidence for ranking:** Reproducible seven-group, five-domain evaluation with code/data fetchers; clear negative result and independent search visibility; citation data unavailable because of API rate limiting.
- **Claimed contribution:** The authors report pretrained models winning five of seven groups, with a 28% lower MASE gain on Wikipedia pageviews and a TimesFM-family advantage associated with disclosed corpus familiarity.
- **Caveat:** The result concerns the tested 13 forecasters, seven groups, and disclosed domains; it does not show that all foundation-model benchmarks are contaminated.
- **Announcement type:** new submission, 2026-09-10 announcement batch
- **Themes:** Evaluation & benchmarks; Retrieval & knowledge; Training & adaptation

### 7. [From Fixed Keys to Readable Schemas: Small Language Models for Vehicle Agent Function Calls](https://arxiv.org/abs/2609.09476)
- **Abstract:** The paper compares fixed functional tokens with schemas supplied in prompts for vehicle function calling and shows a flexibility–latency trade-off in small language models.
- **Authors:** Hamed Jafarzadeh Asl, Yuanhao Yu, Vahid Partovi Nia
- **arXiv:** `2609.09476v1` (published 2026-09-08 21:46 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`)
- **Evidence for ranking:** 9,822-example benchmark over 79 vehicle functions, four SLMs, and released-paper HTML; Semantic Scholar returned 0 citations and 0 influential citations at snapshot, so ranking rests on benchmark specificity and cross-list breadth rather than citation momentum.
- **Claimed contribution:** The authors report that schema-in-prompt generalizes to held-out functions and refuses out-of-scope requests better, while fixed tokens have zero held-out accuracy by construction; the strongest overall model was 0.6B.
- **Caveat:** Schema prompting costs memory, latency, and context length; results are limited to single-turn vehicle function calls.
- **Announcement type:** new submission, 2026-09-10 announcement batch
- **Themes:** Agents & reasoning; Efficient inference & systems; Safety & alignment

### 8. [EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models](https://arxiv.org/abs/2609.01611)
- **Abstract:** EvalDetectBench is an open pipeline for measuring whether frontier models recognize evaluation settings and whether individual benchmarks are detectable.
- **Authors:** Xinning Li, Kemunto Ochwang'i, Aryasomayajula Ram Bharadwaj, Alexandra Souly, Robert Kirk
- **arXiv:** `2609.01611v1` (published 2026-06-08 14:54 UTC; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** Not a new 10-Sep submission, but surfaced in current AI discussion/search and directly reinforces the batch's evaluation-awareness theme; code and data are linked; citation counts were unavailable because of API rate limiting.
- **Claimed contribution:** The authors report that deployment-transcript generator identity explains 11.25% of measurement variance and can reorder rankings, motivating per-model calibration and generator harmonisation.
- **Caveat:** This is an older paper included as a relevant benchmark anchor, not as a member of the 2026-09-10 announcement batch; measured awareness remains dependent on probes and transcript design.
- **Announcement type:** new submission, prior batch (2026-06-08)
- **Themes:** Evaluation & benchmarks; Safety & alignment; Interpretability

## Trending research themes

- **Evaluation is becoming a systems problem.** IBIB and MetroLLM-Bench both move beyond checkpoint scores toward complete serving routes, tool contracts, reliability, and deployment-specific behavior. EvalDetectBench adds the concern that models may detect the evaluation itself.
- **Benchmark validity is under active pressure.** The later-test-set paper shows that time-based hold-outs can still retain domain familiarity, while IBIB and EvalDetectBench identify route and evaluator effects that can change conclusions.
- **Small, targeted adaptation is competing with scale.** MetroLLM-Bench reports a 4B PEFT student outperforming named larger configurations on its deterministic tier; FOM-UL targets only selected layers; vehicle function calling shows representation design can matter more than parameter count.
- **World models are being trained for controllable generalization.** SG-JEPA conditions latent dynamics on physical parameters and evaluates out-of-distribution gravity, connecting representation learning to robotic control.

## Research opportunities

### Potential research areas
- Build benchmark suites that jointly vary model weights, serving route, quantization, tool parser, harness, and evaluator awareness, combining IBIB, MetroLLM-Bench, and EvalDetectBench.
- Study domain-holdout design for foundation models beyond time series, using the familiarity analysis in 2609.10357 as a template for language, vision, and multimodal corpora.
- Develop compact, schema-aware agents for safety-critical edge devices, linking 2609.09476's function-surface results with MetroLLM-Bench's structured terminal-state evaluation.

### Unsolved problems
- Formal or auditable guarantees for unlearning remain open: FOM-UL explicitly reports no formal erasure guarantee, especially after future fine-tuning or quantization.
- It remains unclear how to separate genuine self-knowledge from generic behavioral modeling across broader tasks and model families; 2609.09899 finds weak self-specific prediction.
- SG-JEPA's robustness outside designed physics tasks and on real-world sensors and dynamics is not established by the abstract-level evidence.

### Potential research directions
- Re-run enterprise and agent benchmarks under preregistered serving-route manifests, repeated seeds, calibrated judges, and failure-inclusive denominators, as suggested by IBIB and MetroLLM-Bench.
- Create domain-disjoint, corpus-disclosure-aware evaluation protocols for foundation models, then test whether the familiarity signal survives across domains and architectures.
- Combine layer selection, quantization-aware unlearning, and post-unlearning red-team suites to test whether targeted updates remain robust under deployment changes.
- Compare schema-in-prompt, structured decoding, and learned function tokens at equal latency and memory budgets on unseen tools and refusal cases.

## Takeaway
The notable development is methodological: researchers are questioning whether benchmark scores measure the deployed system, the intended capability, or familiarity with the test environment. The papers provide useful artifacts and concrete experiments, but most are fresh preprints with no mature citation signal; treat their numerical claims as preliminary until independently reproduced.

## Method and sources

- Window: latest daily arXiv announcement batch dated 2026-09-10 UTC; snapshot 2026-09-11 00:10 UTC. arXiv's recent cs.LG listing showed the batch as Thu, 10 Sep 2026.
- Candidate scope: cs.AI, cs.LG, stat.ML, cs.CL, cs.CV, cs.RO, cs.NE, cs.MA, with cross-listed papers retained.
- Ranking: inferred, not an official arXiv ranking. Signals were cross-list breadth, benchmark/artifact specificity, independent technical discussion or search visibility, substantive reported evidence, and one successful Semantic Scholar lookup for 2609.09476 (0 citations, 0 influential citations). Other Semantic Scholar requests were rate-limited; no citation counts were invented.
- Primary sources: the linked arXiv abstract pages for every entry. Search corroboration included the Semigroup-JEPA project/Hugging Face/GitHub pages, FOM-UL HTML and independent discussion, MetroLLM-Bench coverage, IBIB HTML and independent discussion, and EvalDetectBench's project page.
- arXiv has no official trending chart; ordering is inferred and must not be read as a readership/download ranking.
