# AI on arXiv — daily notable papers, 23 November 2026

This 23 November announcement batch yielded 10 notable recent AI papers, spanning agent behavior, multimodal systems, efficient inference, safety, and evaluation. The pattern is practical systems work: make models more reliable, resource-efficient, or testable in real settings. In this episode: agent-state analysis, language-to-robot specifications, privacy-aware vision-language models, memory reuse, and a few evaluation and efficiency results. arXiv publishes no official trending chart; this ordering is inferred from sparse attention signals and cross-list breadth, with limited citation evidence for such recent papers, so it is not a measure of readership or overall importance.

## Top papers (ranked)

### 1. [Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection](https://arxiv.org/abs/2611.27784)
- **Abstract:** The authors present a frozen audio-forgery detector evaluated across ten public benchmarks, multiple generators, recording conditions and languages, reporting strong results including first place on Podonos and the lowest commercial-detector equal error rate on ASVspoof5.
- **Authors:** Sivashankar Selvarajan, Piyush Verma, Sumit Kumar, Sharayu N. Deshmukh
- **arXiv:** `2611.27784v1` (published 2026-11-20T16:11:09Z; categories: `cs.SD`, cross-list: `cs.AI`)
- **Evidence for ranking:** Highest signal score in the pool (1.636): Semantic Scholar reports 1 current citation (weighted component 1.386), plus 1 cross-list (0.25). No Hugging Face or Hacker News points surfaced in this candidate's score components; the one citation is a current total, not a window gain.
- **Claimed contribution:** The authors claim a single frozen model generalizes across audio generators, channels, recording settings, and languages, with the benchmark and leaderboard results summarized above (arXiv abstract).
- **Caveat:** The abstract reports benchmark and leaderboard evaluations but does not describe prospective deployment or error rates across operational populations; the claimed generality should be read within the tested settings.
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Evaluation & benchmarks; Safety & alignment

### 2. [Towards Text-Mask Consistency in Medical Image Segmentation](https://arxiv.org/abs/2611.27050)
- **Abstract:** The authors introduce C2Seg, combining cluster-aware soft contrastive labels, bidirectional complementary attention, and KAN-based attention gating to improve text-mask consistency and segmentation accuracy on four public medical-imaging datasets.
- **Authors:** Jie Gui, Hang Tu, Wen Sha, Xiuquan Du
- **arXiv:** `2611.27050v1` (published 2026-11-20T03:19:25Z; categories: `cs.CV`)
- **Evidence for ranking:** Signal score 1.386, entirely from 1 current Semantic Scholar citation (weighted component 1.386); no cross-list contribution. No Hugging Face or Hacker News points surfaced in the candidate's score components. The arXiv record notes acceptance as an ICLR 2026 poster; this is publication context, not an attention metric.
- **Claimed contribution:** The authors attribute improved text-mask consistency and segmentation accuracy to C2Seg and report results on four public datasets (arXiv abstract).
- **Caveat:** Evidence in the abstract is limited to four public datasets; it does not establish performance across other clinical sites or deployment workflows.
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks

### 3. [Potential emergence in LLM agents: a statistical physics perspective](https://arxiv.org/abs/2611.27618)
- **Abstract:** The authors model agent states and a global potential to describe how post-training organizes LLM-agent reasoning, demonstrating the framework on safety-test selection and physics-reasoning audits using Qwen3.5-9B.
- **Authors:** Zhuo-Yang Song, Hua Xing Zhu
- **arXiv:** `2611.27618v1` (published 2026-11-20T13:46:24Z; categories: `cs.LG`, cross-lists: `cond-mat.stat-mech`, `cs.AI`, `cs.CL`, `nlin.AO`)
- **Evidence for ranking:** Signal score 1.000, entirely from 4 cross-listings (weighted component 1.000), including `cs.AI` and `cs.CL`; Semantic Scholar lists 0 citations. No Hugging Face or Hacker News points surfaced in the candidate's score components.
- **Claimed contribution:** The authors propose agent states as measurable intermediate variables and report that potential structure strengthens during post-training in their two Qwen3.5-9B tasks (arXiv abstract).
- **Caveat:** The empirical demonstration described in the abstract uses one model family and two tasks, so it does not establish that the proposed state/potential account transfers broadly.
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Agents & reasoning; Safety & alignment

### 4. [Efficient Natural Language to Temporal Logic Translation for Real-Time Physical AI](https://arxiv.org/abs/2611.27489)
- **Abstract:** The authors replace free-form LLM generation with predefined-answer classification for translating natural-language instructions into linear temporal logic, reporting comparable or better accuracy than local LLMs on three benchmarks at up to an order of magnitude lower runtime and energy use.
- **Authors:** Oliver Schön, Adrien Banse, John Lygeros, Lars Lindemann
- **arXiv:** `2611.27489v1` (published 2026-11-20T11:35:56Z; categories: `cs.AI`, cross-lists: `cs.CL`, `cs.LO`, `cs.RO`, `eess.SY`)
- **Evidence for ranking:** Signal score 1.000 from 4 cross-listings (weighted component 1.000), including AI, language, and robotics categories; Semantic Scholar lists 0 citations. No Hugging Face or Hacker News points surfaced in the candidate's score components.
- **Claimed contribution:** The authors report that a System-One classifier approach matches or exceeds the best local LLMs on three benchmarks and generalizes to unseen atomic propositions and temporal patterns (arXiv abstract).
- **Caveat:** The abstract does not specify how the benchmark results translate to safety or reliability in physical deployments; the reported evidence is benchmark-based.
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Robotics & control; Efficient inference & systems

### 5. [SecretAgent: A Multi-Agent Framework for Privacy Protection against Vision Language Models](https://arxiv.org/abs/2611.26936)
- **Abstract:** SecretAgent uses LLM agents to identify image evidence that reveals private information and iteratively tune low-visibility perturbations; the authors report privacy and image-fidelity results across four applications, five datasets, and six VLMs.
- **Authors:** Minda Zhao, Yue Zhang, Mengyu Wang
- **arXiv:** `2611.26936v1` (published 2026-11-20T00:46:20Z; categories: `cs.CV`, cross-lists: `cs.AI`, `cs.CR`, `cs.LG`, `cs.MA`)
- **Evidence for ranking:** Signal score 1.000 from 4 cross-listings (weighted component 1.000), including AI, machine learning, and multiagent systems; Semantic Scholar lists 0 citations. No Hugging Face or Hacker News points surfaced in the candidate's score components.
- **Claimed contribution:** The authors claim the framework improves image fidelity while achieving state-of-the-art privacy protection in the four tested applications and transfers to other VLMs (arXiv abstract).
- **Caveat:** The abstract's evaluations cover five datasets and six VLMs; privacy against other model families, image transformations, or attacker capabilities is not established there.
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Safety & alignment; Multimodal & vision-language; Agents & reasoning

### 6. [Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs](https://arxiv.org/abs/2611.26902)
- **Abstract:** Baton maps a small VLM's visual KV cache into a larger VLM's memory for uncertain decisions, and the authors report near re-watching performance with 28–47% less compute and up to 8× less compute per escalation at 64 frames.
- **Authors:** Qiang Zhou, Jianing Deng, Siyan Dong, Jingxian Chen, Han-Yi Lin, Jingtong Hu
- **arXiv:** `2611.26902v1` (published 2026-11-19T23:32:52Z; categories: `cs.CV`, cross-lists: `cs.AI`, `cs.CL`, `cs.LG`, `cs.RO`)
- **Evidence for ranking:** Signal score 1.000 from 4 cross-listings (weighted component 1.000), spanning AI, language, learning, and robotics; Semantic Scholar lists 0 citations. No Hugging Face or Hacker News points surfaced in the candidate's score components.
- **Claimed contribution:** The authors report that a learned per-layer linear map lets the larger model reuse the smaller model's visual memory, with results on RoboMME and zero-shot transfer to OpenEQA (arXiv abstract).
- **Caveat:** The reported compute and performance results are tied to the evaluated model pairs, datasets, and escalation setup; broader deployment costs are not established in the abstract.
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Multimodal & vision-language; Efficient inference & systems; Robotics & control

### 7. [SLP-Bench: Evaluating and Improving Acoustic Claims of Reasoning Audio Language Models on Clinical Speech](https://arxiv.org/abs/2611.27810)
- **Abstract:** SLP-Bench scores acoustic claims in audio-language-model reasoning against clinician ratings across five datasets and 25 perceptual dimensions; the authors report that zero-shot claims are imperfect and unstable, while GRPO fine-tuning improves claim accuracy and agreement.
- **Authors:** Côme Hosxe, Rachid Riad, Quentin Spinat
- **arXiv:** `2611.27810v1` (published 2026-11-20T16:36:57Z; categories: `cs.AI`, cross-lists: `cs.CL`, `cs.LG`, `cs.SD`)
- **Evidence for ranking:** Signal score 0.750 from 3 cross-listings (weighted component 0.750), including AI, language, and learning; Semantic Scholar lists 0 citations. No Hugging Face or Hacker News points surfaced in the candidate's score components.
- **Claimed contribution:** The authors contribute a clinician-referenced benchmark for checking the factuality, stability, and consistency of acoustic reasoning claims, and report a GRPO fine-tuning improvement (arXiv abstract).
- **Caveat:** Dataset access is available on request and subject to the providers' approval, which may constrain independent reproduction (arXiv abstract).
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Evaluation & benchmarks; Multimodal & vision-language; Safety & alignment

### 8. [Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](https://arxiv.org/abs/2611.27689)
- **Abstract:** Embodied-Harness pairs an acting agent with a reflector that turns execution evidence into reusable guidance without updating model parameters; the authors report results on three benchmarks and real-world trials across three manipulation tasks.
- **Authors:** Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan, Wenqiao Zhang, Juncheng Li, et al.
- **arXiv:** `2611.27689v1` (published 2026-11-20T14:55:07Z; categories: `cs.RO`, cross-lists: `cs.AI`, `cs.CV`, `cs.MA`)
- **Evidence for ranking:** Signal score 0.750 from 3 cross-listings (weighted component 0.750), connecting robotics, AI, vision, and multiagent systems; Semantic Scholar lists 0 citations. No Hugging Face or Hacker News points surfaced in the candidate's score components.
- **Claimed contribution:** The authors report success rates of 82.4%, 76.7%, and 94.4% on RoboTwin 2.0, RoboSPA, and RMBench, plus 96.7% average success across three real-world tasks (arXiv abstract).
- **Caveat:** The abstract describes real-world evaluation on only three manipulation tasks; broader task and environment coverage remains unshown there.
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Robotics & control; Agents & reasoning

### 9. [PLoQ: A Prompt-Specific Low-Rank Basis for 4-bit Quantization of LLM Activations](https://arxiv.org/abs/2611.27092)
- **Abstract:** PLoQ estimates a prompt-specific low-rank basis during prefill, quantizes dominant activation directions separately, and restores them within the matrix multiplication; the authors report improvements over mixed-precision baselines on six Llama and Qwen models.
- **Authors:** Faraz Tahmasebi, Michael Pellauer, Hyoukjun Kwon, Sitao Huang
- **arXiv:** `2611.27092v1` (published 2026-11-20T04:07:37Z; categories: `cs.LG`, cross-lists: `cs.CL`, `cs.DC`, `cs.PF`)
- **Evidence for ranking:** Signal score 0.750 from 3 cross-listings (weighted component 0.750), spanning learning, language, and computer systems; Semantic Scholar lists 0 citations. No Hugging Face or Hacker News points surfaced in the candidate's score components.
- **Claimed contribution:** The authors report better perplexity recovery than the compared quantization method across six models from 1B to 70B parameters, with modest reported prefill and decode overhead on Llama-3.1-8B (arXiv abstract).
- **Caveat:** The reported comparison uses a particular mixed-precision setup and sequence lengths up to 8k tokens (16k for two models); results beyond those configurations are not established in the abstract.
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Efficient inference & systems; Training & adaptation

### 10. [Contexture: Runtime Context Eviction for High-Throughput Agent Serving](https://arxiv.org/abs/2611.26980)
- **Abstract:** Contexture uses tool-operation history and runtime cache state to evict superseded context from agent execution while preserving the full conversation record; the authors report higher throughput under service-level objectives across two models, two harnesses, and two benchmarks.
- **Authors:** Colin Hong, Bryan Shan, Wei Siong Pang, Chengzhi Lu, Xu Guo, et al.
- **arXiv:** `2611.26980v1` (published 2026-11-20T01:55:52Z; categories: `cs.DC`, cross-lists: `cs.AI`, `cs.MA`, `cs.OS`)
- **Evidence for ranking:** Signal score 0.750 from 3 cross-listings (weighted component 0.750), including AI and multiagent systems; Semantic Scholar lists 0 citations. No Hugging Face or Hacker News points surfaced in the candidate's score components.
- **Claimed contribution:** The authors report 20–73% throughput improvement over the best listed baselines under SLO in tested configurations and up to 11% lower GPU energy per completed session (arXiv abstract).
- **Caveat:** Live-agent experiments report a worst-case accuracy loss of 3.7 percentage points versus unloaded no-eviction, despite a 1.4-point mean gain; throughput benefits therefore need to be considered alongside accuracy (arXiv abstract).
- **Announcement type:** new submission, 2026-11-23 announcement batch
- **Themes:** Efficient inference & systems; Agents & reasoning

## Trending Research Themes

- **Agents are becoming systems to measure and engineer, not just prompts to improve.** Potential emergence treats agent states as measurable post-training variables; Embodied-Harness improves a robot-control harness from execution traces; Contexture changes the model-visible execution history; and Baton reuses visual memory during escalation. These are distinct approaches, not evidence of a single breakthrough.
- **Evaluation is moving inside model reasoning.** SLP-Bench checks individual clinical-acoustic claims rather than only final answers, while ARCAS evaluates audio detection across diverse benchmarks and C2Seg targets agreement between text and segmentation masks. Together they emphasize intermediate evidence and cross-condition testing.
- **Efficiency increasingly depends on structure and selective computation.** Baton avoids repeated visual-history encoding, PLoQ protects prompt-specific activation directions during 4-bit quantization, Contexture removes superseded context, and the temporal-logic translator replaces open-ended generation with constrained classification. These papers report different cost/performance trade-offs and are not directly comparable.
- **Safety and privacy are being treated as constraints on multimodal pipelines.** SecretAgent perturbs images to limit privacy leakage; SLP-Bench audits voice-related claims; ARCAS detects generated audio. This batch connects image and audio risks, but does not establish a unified multimodal safety solution.

## Open Problems and Research Directions

- **How general is the agent-state account?** The study tests safety-test selection and physics-reasoning audits on Qwen3.5-9B. As a follow-up, test whether the same state/potential measures predict behavior across model families, agent tasks, and independently varied post-training recipes (Song & Zhu, [2611.27618](https://arxiv.org/abs/2611.27618)).
- **When does efficiency-preserving context removal harm correctness?** Contexture reports a 3.7-point worst-case accuracy loss despite a 1.4-point mean gain, and Baton evaluates specific VLM pairings and escalation conditions. Follow-up work could stress-test both methods under long, adversarial, or tool-dependent histories while reporting accuracy, latency, and GPU cost together (Hong et al., [2611.26980](https://arxiv.org/abs/2611.26980); Zhou et al., [2611.26902](https://arxiv.org/abs/2611.26902)).
- **Do privacy perturbations hold under stronger or changing attackers?** SecretAgent reports transfer to other VLMs across five datasets, but the abstract does not characterize all transformations or adaptive attacks. Evaluate robustness under compression, resizing, multiple target models, and attackers aware of the protection method (Zhao et al., [2611.26936](https://arxiv.org/abs/2611.26936)).
- **Can claim-level clinical speech evaluation be independently reproduced?** SLP-Bench access depends on dataset-provider approval. A useful direction is a legally reusable evaluation subset or documented protocol that preserves clinician references and tests whether claim-level gains persist across new speakers, sites, and recording conditions (Hosxe et al., [2611.27810](https://arxiv.org/abs/2611.27810)).
- **Do text-mask gains transfer across clinical settings?** C2Seg reports four public datasets. External-site and prospective evaluations, with explicit checks of text-mask agreement under multi-site and multi-lesion descriptions, would test the boundary of its reported results (Gui et al., [2611.27050](https://arxiv.org/abs/2611.27050)).

## Takeaway

This batch is notable for methods that make AI systems more inspectable or economical at inference time: structured temporal-logic translation, reuse of model memory, runtime context eviction, and claim-level evaluation. The reported gains remain bounded by each study's evaluated models, datasets, and deployment settings; the papers do not yet establish a single approach that jointly solves efficiency, robustness, and real-world reliability.

## Method and sources

- **Window:** daily arXiv announcement batch covering first submissions from 2026-11-19 19:00:00 UTC through 2026-11-20 19:00:00 UTC; announced 2026-11-23 at 01:00:00 UTC. This is today's announcement date, not a prior-batch substitution.
- **Snapshot:** 2026-11-23 19:53:02 UTC. The supplied signal file was generated at 2026-11-23 19:52:40 UTC.
- **Corpus query:** `cs.AI OR cs.LG OR stat.ML OR cs.CL OR cs.CV OR cs.RO OR cs.NE OR cs.MA`; the supplied candidate pool contains 525 arXiv records and 150 ranked candidates. All ten selected records are first submissions in this batch; none is a revision.
- **Inference:** arXiv provides no official trending chart. Used the supplied candidate scores and components first: current Semantic Scholar citations and configured cross-list breadth, then category relevance and breadth across topics to order candidates tied on score. Citation counts are current totals. Scores for ranks 1–2 are 1.636 (1.386 citation + 0.25 cross-list) and 1.386 (citation); ranks 3–6 are 1.000 from four cross-listings; ranks 7–10 are 0.750 from three. Zero citations or missing HF/HN components are not evidence of unimportance. HF, HN, arXiv lookup, and Semantic Scholar collectors were marked `ok` in the signal file; no HF/HN score components surfaced for these ten papers.
- **Primary sources:** each selected arXiv abstract page is linked in its heading and was fetched and checked directly. Category recent pages were not separately extracted; the pre-collected arXiv pool was used. The configured `web_extract` backend could not extract URLs in this session, so primary pages were verified with direct HTTP retrieval instead.
- **Signal source:** `/home/yizhuan/.research/ai/daily/arxiv-trending-ai-daily-2026-11-23.signals.json` (schema `rrc-signals/v1`; generated 2026-11-23T19:52:40Z). Its source statuses were arXiv 525, Hugging Face 102, Hacker News 31, arXiv lookup 132, Semantic Scholar 524, all `ok`.
- **Corroborating source:** Semantic Scholar Graph records as summarized in the signal file; one current citation each for `2611.27784` and `2611.27050`, zero for the other eight. No citation count is represented as a gain during this announcement window.
