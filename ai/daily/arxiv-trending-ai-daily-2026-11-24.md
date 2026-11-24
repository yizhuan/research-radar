# arXiv Trending AI — Daily report — 2026-11-24

## Headline

**AI papers announced 2026-11-24: 11 notable recent papers.** This batch leans toward agent evaluation and feedback-driven training, with additional work on multimodal world selection and model safety. We cover the papers, their evidence, and the unresolved tests they leave behind. This is an inferred ordering, not an official arXiv trending chart: the signal file found no candidate-level external-attention values, and citation evidence is limited because Semantic Scholar data was unavailable; cross-list breadth is therefore the primary ranking signal, not proof of popularity.

## Top papers (ranked)

### 1. [Feedback-Driven Prompt Refinement for Educational AI: Affective Trajectory Estimation and Bloom's Taxonomy Classification](https://arxiv.org/abs/2611.28293)
- **Abstract:** The authors report that a shared prompt-refinement procedure using separate affective and cognitive feedback improved held-out agreement and classification while reducing generation variability, without updating the executor model's parameters.
- **Authors:** Josh Dean, Karan Patel, Gaurangi Raul, Yu-Zheng Lin, Jesus Pacheco, et al.
- **arXiv:** `2611.28293v1` (published 2026-11-20 20:20:32Z UTC; categories: `cs.AI, cs.CL, cs.CY, cs.HC, cs.LG`)
- **Evidence for ranking:** Signal candidate score 1.00 (cross_lists=1.00; four cross-lists). This is the highest candidate score; no Hugging Face, Hacker News, or citation signal is attached to this candidate.
- **Claimed contribution:** The paper proposes feedback-driven prompt refinement for educational AI and reports improvements on held-out affective-reference and Bloom-label tasks without executor parameter updates.
- **Caveat:** The authors state that the refinement sets are small, affective references are unvalidated, and learner outcomes were not measured.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Training & adaptation, Evaluation & benchmarks

### 2. [Bridging Blind Spots With Words: Decentralized Multi-View Spatial Reasoning via Language-Constrained Communication](https://arxiv.org/abs/2611.29112)
- **Abstract:** The paper formalizes decentralized spatial reasoning across N agents with distinct views and budget-limited language exchange, introduces a multi-view benchmark, and reports that reinforcement learning with credit assignment closes the gap to its centralized baseline.
- **Authors:** Soumyabrata Chaudhuri, Joydeep Ghosh
- **arXiv:** `2611.29112v1` (published 2026-11-22 00:23:01Z UTC; categories: `cs.CV, cs.AI, cs.IR, cs.LG`)
- **Evidence for ranking:** Signal candidate score 0.75 (cross_lists=0.75; three cross-lists), among the top breadth tier; the candidate has no attached HF/HN/citation attention value.
- **Claimed contribution:** The authors contribute a general multi-agent problem formulation and benchmark, and evaluate language-constrained collaboration against centralized and oracle ceilings.
- **Caveat:** The abstract reports substantial remaining headroom relative to an oracle best-of-K ceiling; the evidence is benchmark-based and does not establish transfer to deployed embodied settings.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Agents & reasoning, Multimodal & vision-language, Evaluation & benchmarks

### 3. [ESM-Bench: A Benchmark for Evaluating Whether AI Agents Understand Earth System Model Physics and Code](https://arxiv.org/abs/2611.28477)
- **Abstract:** ESM-Bench packages 60 code-change tasks from six Earth System Model repositories to test whether AI coding agents preserve both software interfaces and scientific physics, and audits reveal failures in local patch-checking proxies.
- **Authors:** Koutian Wu, Yuxuan Cao, Gengchen Mai, Zeping Liu
- **arXiv:** `2611.28477v1` (published 2026-11-21 01:51:31Z UTC; categories: `cs.AI, cs.LG, physics.ao-ph, physics.geo-ph`)
- **Evidence for ranking:** Signal candidate score 0.75 (cross_lists=0.75; three cross-lists), placing it in the second-highest score tier; no candidate-specific HF/HN/citation signal is present.
- **Claimed contribution:** The authors release a benchmark, patch-review rubric, and diagnostic tooling for evaluating AI coding agents on Earth System Model changes.
- **Caveat:** The authors say complete expert validation, comparative agent performance, and full-model execution remain unmeasured on benchmark version 5.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Agents & reasoning, Evaluation & benchmarks

### 4. [INSEP: Refusal-Direction Inseparability as a Defense Against Abliteration](https://arxiv.org/abs/2611.28314)
- **Abstract:** INSEP fine-tunes language models to make harmful and benign activations less separable along the refusal direction, aiming to weaken the white-box abliteration attack while preserving refusal and benign-response quality.
- **Authors:** Ivan Brugere, Junqi Jiang, Saumitra Mishra, Sumitra Ganesh
- **arXiv:** `2611.28314v1` (published 2026-11-20 21:06:00Z UTC; categories: `cs.AI, cs.CL, cs.CR, cs.LG`)
- **Evidence for ranking:** Signal candidate score 0.75 (cross_lists=0.75; three cross-lists), in the second-highest breadth tier; no candidate-specific HF/HN/citation attention value is attached.
- **Claimed contribution:** The authors propose an adversarially selected, low-rank fine-tuning defense and report evaluation against six defenses, five attacks, and eight models from 1B to 14B parameters.
- **Caveat:** The reported robustness evidence is limited to the tested attack suite, model set, and evaluation measures; the abstract does not establish resistance to untested attacks or deployment conditions.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Safety & alignment, Evaluation & benchmarks, Training & adaptation

### 5. [When Being Wrong Is Right: Reverse-Capability Audio CAPTCHAs through Psychoacoustic Design](https://arxiv.org/abs/2611.28823)
- **Abstract:** The paper introduces psychoacoustic audio CAPTCHAs that accept stable human perceptual errors as the reference answer, reporting lower machine acceptance than nine prior schemes while retaining comparatively high human acceptance in its study.
- **Authors:** Mingjie Bao, Yu Dai, Guangke Chen, Guozhu Meng
- **arXiv:** `2611.28823v1` (published 2026-11-21 14:16:14Z UTC; categories: `cs.CR, cs.AI, cs.HC, cs.SD`)
- **Evidence for ranking:** Signal candidate score 0.75 (cross_lists=0.75; three cross-lists), in the second-highest score tier; no candidate-specific HF/HN/citation value is present.
- **Claimed contribution:** The authors formulate reverse-capability verification and instantiate it with classification and counting CAPTCHA tasks evaluated across seven audio-language models and eight attack strategies.
- **Caveat:** The reported machine and human acceptance rates are specific to the evaluated models, attack strategies, and study conditions; the abstract does not establish performance in broad real-world deployment.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Safety & alignment, Evaluation & benchmarks, Multimodal & vision-language

### 6. [GameAnything: From Any Inspirations to Playable Game Worlds](https://arxiv.org/abs/2611.29238)
- **Abstract:** GameAnything is an open-source agentic platform and benchmark for turning multimodal inspirations into playable extensions of existing games through iterative coding, playtesting, persistent state, and reusable experience memory.
- **Authors:** Wenyi Wu, Siqi Liu, Yuru Feng, Zixuan Song, Aayush Salvi, et al.
- **arXiv:** `2611.29238v1` (published 2026-11-22 05:17:35Z UTC; categories: `cs.AI, cs.CL, cs.LG`)
- **Evidence for ranking:** Signal candidate score 0.50 (cross_lists=0.50; two cross-lists). It shares this score tier with other selected papers; the signal file provides no candidate-specific HF/HN/citation attention value.
- **Claimed contribution:** The authors introduce GameAnything and GameAnything-Bench, and report that nine evaluated coding-agent configurations still struggle with playable interactions and precise edits.
- **Caveat:** The authors characterize gameplay testing as exploratory, and report that iterative refinement benefits vary across agents.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Agents & reasoning, Multimodal & vision-language, Evaluation & benchmarks

### 7. [Direct Feedback Policy Optimization for AI Coding Agents](https://arxiv.org/abs/2611.29193)
- **Abstract:** Direct Feedback Policy Optimization (DFPO) is a single-trajectory reinforcement-learning method for coding agents, and the paper reports higher task-resolution rates than GSPO under matched base models and execution harnesses.
- **Authors:** Fei Ding
- **arXiv:** `2611.29193v1` (published 2026-11-22 03:36:09Z UTC; categories: `cs.LG, cs.AI, cs.CL`)
- **Evidence for ranking:** Signal candidate score 0.50 (cross_lists=0.50; two cross-lists); this is the candidate’s only available ranking component, with no attached external-attention value.
- **Claimed contribution:** The author proposes training directly from one trajectory to address sparse terminal rewards and repeated per-task sampling in group-relative methods.
- **Caveat:** The abstract reports a comparison with GSPO under matched models and harnesses but does not specify broader task coverage or generalization beyond that evaluation.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Training & adaptation, Agents & reasoning

### 8. [VeriLogic: Reinforcement Learning over Verifiable Logical Reasoning Traces](https://arxiv.org/abs/2611.29147)
- **Abstract:** VeriLogic converts intermediate logical judgments, proofs, and final decisions into explicit verifiable learning objects, combining verifier-grounded environment construction, structured policy optimization, and iterative refinement.
- **Authors:** ZeLiang Chen, Yunyao Zhang, Xinglang Zhang, Wenbing Li, Junqing Yu, Zikai Song
- **arXiv:** `2611.29147v1` (published 2026-11-22 01:59:28Z UTC; categories: `cs.LG, cs.AI, cs.CL`)
- **Evidence for ranking:** Signal candidate score 0.50 (cross_lists=0.50; two cross-lists); no HF/HN/citation attention value is attached to the candidate.
- **Claimed contribution:** The authors propose a verifier-feedback reinforcement-learning pipeline and report average gains of 6.39% on Qwen3 and 5.00% on Llama-3.1 across six logical-reasoning benchmarks.
- **Caveat:** The reported results cover six logical-reasoning benchmarks and two named model families; broader reasoning domains and deployment settings are not established by the abstract.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Agents & reasoning, Training & adaptation, Evaluation & benchmarks

### 9. [Population-Based Post-Training for Large Language Models](https://arxiv.org/abs/2611.29014)
- **Abstract:** Population-Based Post-Training trains multiple LLMs in parallel and uses validation-driven population updates to explore hyperparameters, with reported gains over compute-matched independent RLVR learners on reasoning and interactive tool-use tasks.
- **Authors:** Yixuan Even Xu, Aleksei Petrenko, Raja Giryes, Jackson Hamburger, Kevin Chen, et al.
- **arXiv:** `2611.29014v1` (published 2026-11-21 19:50:24Z UTC; categories: `cs.CL, cs.AI, cs.LG`)
- **Evidence for ranking:** Signal candidate score 0.50 (cross_lists=0.50; two cross-lists); no candidate-specific HF/HN/citation signal is present.
- **Claimed contribution:** The authors propose population-based training as an in-run mechanism for post-training hyperparameter exploration and report recovery from poor initial settings.
- **Caveat:** The reported evidence is on the named reasoning benchmarks and tool-use environments; conclusions are bounded by those evaluations and the validation-driven setup.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Training & adaptation, Agents & reasoning, Evaluation & benchmarks

### 10. [Multimodal LLMs Know the Game but Assume the Real World](https://arxiv.org/abs/2611.28745)
- **Abstract:** RuleCraft tests 1,240 engine-verified Minecraft image questions and finds that six multimodal LLMs often answer according to real-world physics rather than game rules unless the prompt makes the game context explicit.
- **Authors:** Jianxin Gao, Bohan Chen, Runze Li, Qi Zhang
- **arXiv:** `2611.28745v1` (published 2026-11-21 11:27:17Z UTC; categories: `cs.CL, cs.AI, cs.CV`)
- **Evidence for ranking:** Signal candidate score 0.50 (cross_lists=0.50; two cross-lists); the candidate has no attached HF/HN/citation attention value.
- **Claimed contribution:** The authors contribute a benchmark separating knowledge of game rules from selecting the relevant world model, and report accuracy gains from explicitly naming the game or asking about the pictured world's rules.
- **Caveat:** The core benchmark is Minecraft-focused; the abstract reports recurrence in two additional games, but does not establish coverage of arbitrary visual environments.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Multimodal & vision-language, Evaluation & benchmarks, Agents & reasoning

### 11. [The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates](https://arxiv.org/abs/2611.28671)
- **Abstract:** MASSys benchmarks multi-agent LLM workflows across serving substrates and load regimes, measuring task quality alongside delivery, latency, cost, resource pressure, and failure evidence.
- **Authors:** Haoyuan Zheng, Dongting Li, Hancheng Ye, Qinsi Wang, Mingyuan Ma, et al.
- **arXiv:** `2611.28671v1` (published 2026-11-21 08:50:10Z UTC; categories: `cs.MA, cs.AI, cs.LG`)
- **Evidence for ranking:** Signal candidate score 0.50 (cross_lists=0.50; two cross-lists); no candidate-specific HF/HN/citation attention value is present.
- **Claimed contribution:** The authors show that workflow rankings and effective task delivery can change with serving substrate and load, and argue for reporting operating conditions and execution failures alongside task quality.
- **Caveat:** The results are conditioned on the benchmark's five workload families and tested substrates/load regimes; they do not imply one universally best workflow.
- **Announcement type:** new submission, 2026-11-24
- **Themes:** Evaluation & benchmarks, Efficient inference & systems, Agents & reasoning

## Trending Research Themes

- **Agents are being evaluated through task execution, not answers alone.** ESM-Bench tests code edits against scientific and software constraints; GameAnything adds playtesting and gameplay quality; MASSys measures whether multi-agent outputs are delivered under real serving conditions; RuleCraft isolates whether a model applies the right world rules. These papers point to evaluation designs that test the whole interaction path, not merely final text.
- **Training feedback is becoming more granular and adaptive.** DFPO learns from one coding-agent trajectory, VeriLogic exposes intermediate proof steps to verifiers, and Population-Based Post-Training adjusts training configurations during RLVR. Feedback-driven prompt refinement (paper 1) is a distinct parameter-free route. This is a recurring methods theme in this batch, not evidence that any one approach is generally superior.
- **Multi-agent communication and systems constraints meet.** The spatial-reasoning paper studies budgeted language exchange among agents with partial views, while MASSys shows workflow orderings can flip under serving pressure. Together they motivate joint measurement of reasoning quality, communication budgets, and runtime conditions; evidence comes from two benchmark papers, not a field-wide trend estimate.
- **Safety and robustness are examined through adversarial capability.** INSEP targets a white-box alignment attack on refusal representations, while reverse-capability audio CAPTCHAs design tasks around human perceptual limits. The former is an isolated alignment-defense result; the latter is a separate human-versus-machine verification study, so this is a juxtaposition rather than a common method.

## Open Problems and Research Directions

- **Author-stated — educational validity:** the educational prompt-refinement study has small refinement sets, unvalidated affective references, and no learner-outcome measurements. **Suggested follow-up:** preregister a larger classroom or training study with human-validated affect labels and direct learning outcomes, separating prompt changes from content improvements. ([paper 1](https://arxiv.org/abs/2611.28293))
- **Author-stated — science-agent correctness:** ESM-Bench v5 lacks complete expert validation, comparative agent performance, and full-model execution; its audit also shows some local pattern checks can pass invalid patches. **Suggested follow-up:** run blinded expert review and full-model regression tests, then compare coding agents on the same validated tasks. ([paper 3](https://arxiv.org/abs/2611.28477))
- **Author-stated — multi-view reasoning headroom:** the decentralized spatial-reasoning study reports a remaining gap to an oracle best-of-K ceiling. **Suggested follow-up:** test whether credit assignment remains effective as agent count, communication budget, view overlap, and domain shift vary. ([paper 2](https://arxiv.org/abs/2611.29112))
- **Synthesis — robustness outside benchmark suites:** [INSEP](https://arxiv.org/abs/2611.28314), the [audio CAPTCHA study](https://arxiv.org/abs/2611.28823), and [RuleCraft](https://arxiv.org/abs/2611.28745) each report results on finite model/attack/world sets. **Suggested follow-up:** evaluate adaptive attackers, unseen model families, and out-of-distribution environments, while preserving usability and benign-task performance.
- **Synthesis — operationally valid agent comparisons:** [GameAnything](https://arxiv.org/abs/2611.29238) and [MASSys](https://arxiv.org/abs/2611.28671) show that playability, task delivery, latency, and execution failures can change the meaning of a success score. **Suggested follow-up:** publish reproducible agent traces and evaluate the same policies across multiple substrates, loads, and end-to-end task-quality rubrics.
- **Author-stated — generalization of post-training results:** [DFPO](https://arxiv.org/abs/2611.29193) reports improvement over GSPO under matched harnesses; [VeriLogic](https://arxiv.org/abs/2611.29147) covers logical-reasoning benchmarks; [PBPT](https://arxiv.org/abs/2611.29014) evaluates named reasoning and tool-use settings. **Suggested follow-up:** compare these methods under matched compute across held-out tasks and model families, reporting variance and failure rates as well as mean resolution.

## Takeaway

This batch’s most coherent signal is a shift toward measuring agents in their full operating context: intermediate reasoning, code correctness, interaction quality, and serving constraints. But the ranking has no measured candidate-level popularity signal, so treat these as evidence-backed notable papers rather than a reliable leaderboard of what researchers are paying most attention to.

## Method and sources

- **Window:** 2026-11-20T19:00:00Z through 2026-11-23T19:00:00Z; announcement batch 2026-11-24, announced 2026-11-24T01:00:00Z. This uses today’s batch, not a prior batch. Snapshot: 2026-11-24T03:05:13Z.
- **Scope/query:** `cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA`; the provided 406-candidate pool combines the category listing and papers detected through HF/HN discussion. Only papers first submitted in this batch window were selected; all 11 are new submissions, not revisions.
- **Ranking:** The provided candidate scores and components were primary. The selected papers scored 1.00 (four cross-lists), 0.75 (three cross-lists), or 0.50 (two cross-lists); within equal-score groups, selection and order reflect direct AI relevance and the reported work’s fit to this roundup, not an arXiv popularity order. The file reports `with_attention: 0`; no selected candidate had a Hugging Face, Hacker News, citation, or code-star value. Zero does not imply lack of importance.
- **Signals:** arXiv listing (406 candidates), Hugging Face (78 source records), Hacker News (19), arXiv lookup (97); those sources were marked available in the signal file. Semantic Scholar was unavailable, so citation and influential-citation evidence could not be corroborated. The absent candidate-level attention values are not treated as negative attention evidence.
- **Verification:** Direct arXiv abstract pages were checked for all selected papers; titles, authors, versions, submission dates, and category metadata were cross-checked against the candidate file. Abstract-page evidence supports the claims and caveats above. PDF body extraction for the top three was unavailable in this environment, so no claims beyond the verified abstracts are made.
- **Primary sources:** [2611.28293](https://arxiv.org/abs/2611.28293); [2611.29112](https://arxiv.org/abs/2611.29112); [2611.28477](https://arxiv.org/abs/2611.28477); [2611.28314](https://arxiv.org/abs/2611.28314); [2611.28823](https://arxiv.org/abs/2611.28823); [2611.29238](https://arxiv.org/abs/2611.29238); [2611.29193](https://arxiv.org/abs/2611.29193); [2611.29147](https://arxiv.org/abs/2611.29147); [2611.29014](https://arxiv.org/abs/2611.29014); [2611.28745](https://arxiv.org/abs/2611.28745); [2611.28671](https://arxiv.org/abs/2611.28671).
- **Signal source:** `/home/yizhuan/.research/ai/daily/arxiv-trending-ai-daily-2026-11-24.signals.json`.
