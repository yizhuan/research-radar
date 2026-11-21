# arXiv Trending AI — Friday, 20 November 2026

Daily AI shortlist: 8 papers from the 20 November announcement batch, selected from 546 unique candidates across the configured AI categories. The strongest recurring signal is a practical turn toward compact, structured control—simpler diffusion adaptation, posterior-aware distillation, and agents that diagnose their own work. Today we’ll move from diffusion and serving systems to autonomous research and robot control. arXiv has no official trending chart: this ordering is inferred from early independent technical discussion and corroborating signals, while citation evidence is exceptionally limited for a batch announced less than two days ago.

## Top papers (ranked)

### 1. [RL Post-Training in Diffusion Transformers Is Activation Steering](https://arxiv.org/abs/2611.26627)
- **Abstract:** The paper reports that fixed activation-steering vectors on frozen diffusion transformers reproduce most of the reward gains of several RL-post-trained image and video models.
- **Authors:** Tuna Han Salih Meral, Kaan Oktay, Alec Helbling, Atakan Kara, Duen Horng Chau, Pinar Yanardag
- **arXiv:** `2611.26627v1` (published 2026-11-19 18:59:53 UTC; categories: `cs.CV`, `cs.LG`)
- **Evidence for ranking:** Early discussion appears on Hugging Face Papers, an AI Crunch technical write-up, and a video analysis; it is also cross-listed in both vision and machine learning. Semantic Scholar showed 0 citations at lookup, so placement reflects corroborated discussion rather than citation momentum.
- **Claimed contribution:** The authors claim that input-independent steering vectors recover 90.0–96.3% of reward gains across six RL-tuned image models and comparable gains on two video models, with far fewer parameters than an SD3.5-M LoRA.
- **Caveat:** The demonstrated models use policy-gradient RL; preference optimization and reward backpropagation are explicitly left untested, and generality beyond the evaluated checkpoints remains open.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Training & adaptation; Efficient inference & systems

### 2. [Posterior Matching Distillation](https://arxiv.org/abs/2611.26629)
- **Abstract:** The paper introduces a stochastic diffusion-distillation objective that matches teacher posterior means to preserve conditional output diversity while supporting variable sampling steps.
- **Authors:** Hidir Yesiltepe, Julius Berner, Arash Vahdat, Pinar Yanardag
- **arXiv:** `2611.26629v1` (published 2026-11-19 18:59:57 UTC; categories: `cs.CV`)
- **Evidence for ranking:** It has early coverage on Papers with Code, ModelScope, and OpenTrain, plus a project page; these are independent technical discovery channels, not readership statistics. Citation totals were not available in the sources checked.
- **Claimed contribution:** The authors prove that matching exponentially tilted posterior means over an open neighborhood identifies the teacher posterior at zero population loss, and report best FID among four-step methods on SDXL and FLUX.2 [klein] 4B.
- **Caveat:** The paper states that training requires multiple student draws and still uses an auxiliary adversarial loss for visual realism; its posterior-identification result assumes an exact posterior-mean denoiser.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Training & adaptation; Multimodal & vision-language

### 3. [TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming](https://arxiv.org/abs/2611.26619)
- **Abstract:** TideCache coordinates heterogeneous state and attention caches on CPU–GPU superchips, streaming attention-layer prefixes to reduce GPU residency while overlapping transfers with computation.
- **Authors:** Jinbin Luo, Xiaozhe Yao, Shang Yang, Zhijian Liu, Song Han, Qinghao Hu
- **arXiv:** `2611.26619v1` (published 2026-11-19 18:58:31 UTC; categories: `cs.DC`, `cs.LG`)
- **Evidence for ranking:** Early technical commentary appeared at AI Crunch and Zhichai; the paper is cross-listed in machine learning despite its primary distributed-computing category. Semantic Scholar showed 0 citations at lookup; placement relies on the specific reported systems results and independent discussion.
- **Claimed contribution:** In SGLang tests across seven configurations on GB300 and GH200, the authors report up to 2.04× as many agent turns, 20–59% lower overall P50 per-token latency, and 1.40–3.05× better agent P50 time-to-first-token than SGLang with HiCache.
- **Caveat:** The evidence is limited to two superchip platforms and the tested SGLang/model configurations; portability to ordinary accelerators or other serving stacks is not established here.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Efficient inference & systems; Agents & reasoning

### 4. [Pro$^2$ Agent: Scientific Problem Probing for Autonomous AI R&D](https://arxiv.org/abs/2611.25357)
- **Abstract:** Pro$^2$ Agent makes an evolving, evidence-backed representation of bottlenecks and candidate solutions the state that guides an autonomous AI research agent’s experiments.
- **Authors:** Yixiong Chen, Liqian Peng, Tian Tan, Ziqian Lin, Blake Jianhang Chen, et al.
- **arXiv:** `2611.25357v1` (published 2026-11-19 01:52:29 UTC; categories: `cs.AI`, `cs.CL`)
- **Evidence for ranking:** The paper has a detailed independent analysis at AGI Hunt and a CatalyzeX listing, and spans AI and language. Semantic Scholar showed 0 citations at lookup; the position is based on early technical scrutiny and the benchmark claim, not citations.
- **Claimed contribution:** The authors report matching the best published medal rate on complete MLE-Bench under 24 hours (70.7%) and reaching 76.0% with 48 hours, alongside competitive results on PostTrainBench.
- **Caveat:** The complete MLE-Bench comparison uses one run per budget; the independent AGI Hunt analysis also notes that published baselines differ in their underlying models, limiting causal attribution to the agent design.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Agents & reasoning; Evaluation & benchmarks

### 5. [Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://arxiv.org/abs/2611.26603)
- **Abstract:** Depth Pro 2 uses one scalable model to predict native-resolution metric depth for images and video, aiming to combine sharp boundaries with temporal consistency.
- **Authors:** Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, et al.
- **arXiv:** `2611.26603v1` (published 2026-11-19 18:55:41 UTC; categories: `cs.CV`, `cs.LG`)
- **Evidence for ranking:** The work is accompanied by an Apple Machine Learning Research release and an OpenReview listing, with code and weights announced; it is cross-listed in machine learning. Semantic Scholar showed 0 citations at lookup, so the signal is release/discussion visibility rather than citation momentum.
- **Claimed contribution:** The authors report a new Pareto frontier across metric accuracy, sharpness, temporal consistency, and runtime, and release a model family, code, and weights.
- **Caveat:** The abstract reports aggregate superiority but does not specify the datasets, metric margins, or operating conditions; those details need checking before treating the claimed frontier as broadly established.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Multimodal & vision-language; Evaluation & benchmarks

### 6. [AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](https://arxiv.org/abs/2611.26613)
- **Abstract:** AgentRoboCritic evaluates robot actions against each agent’s stated local intent, exposing action-level successes and failure modes across 12 manipulation benchmarks.
- **Authors:** Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo, et al.
- **arXiv:** `2611.26613v1` (published 2026-11-19 18:57:25 UTC; categories: `cs.RO`, `cs.CL`, `cs.CV`)
- **Evidence for ranking:** A public project/repository and a DEV Community technical response provide early corroboration; the paper spans robotics, language, and vision. Citation totals were not available in the sources checked.
- **Claimed contribution:** The authors analyze direct control on 12 benchmarks and report a 12,844-action dataset, a 400-action human-annotated critic test set, and improved failure-mode accuracy after fine-tuning an open critic.
- **Caveat:** The intent-grounded critic depends on policy-generated local intent, and the paper’s human-annotated validation set contains 400 actions; independent validation with externally specified intents and more physical trials would test robustness.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Robotics & control; Evaluation & benchmarks; Agents & reasoning

### 7. [One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617)
- **Abstract:** O$^{2}$LaF initializes inverse and forward dynamics from a shared video model to infer latent actions from unlabeled video and test their transfer across scenes and embodiments.
- **Authors:** Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang, et al.
- **arXiv:** `2611.26617v1` (published 2026-11-19 18:58:14 UTC; categories: `cs.CV`, `cs.AI`, `cs.LG`, `cs.RO`)
- **Evidence for ranking:** The work has a project site and a Papers with Code entry, and unusually broad cross-listing across four core AI categories. Citation totals were not available in the sources checked; this is a relevance-led placement with limited attention evidence.
- **Claimed contribution:** The authors report improved few-shot action probing and zero-shot transfer in navigation and robot manipulation, including transfer from human demonstrations to robot demonstrations.
- **Caveat:** The robot-transfer evidence is based on the reported datasets and video evaluations; physical closed-loop deployment and broader embodiment coverage remain to be established.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Robotics & control; Multimodal & vision-language; Training & adaptation

### 8. [PlayCraft: Designing Engaging Games from Agent Play Experience](https://arxiv.org/abs/2611.26624)
- **Abstract:** PlayCraft alternates between a vision-based player agent and a game-crafting agent that revises game rules and challenges using observed play and predicted learning progression.
- **Authors:** Weihao Cheng
- **arXiv:** `2611.26624v1` (published 2026-11-19 18:59:34 UTC; categories: `cs.AI`, `cs.CV`)
- **Evidence for ranking:** The paper has a public GitHub implementation and an AI Hot write-up; it is cross-listed in AI and vision. Semantic Scholar showed 0 citations at lookup; the placement reflects early project-level discussion, not readership evidence.
- **Claimed contribution:** The authors report larger learning gains and steeper learning slopes than initial games in most tested games, with better macro-average metrics than baselines across three player-agent intelligence settings.
- **Caveat:** Engagement and mastery are assessed through player agents and their learning metrics; human-player studies are needed to establish whether the generated games are enjoyable or teachable for people.
- **Announcement type:** new submission, announcement-batch date 2026-11-20
- **Themes:** Agents & reasoning; Evaluation & benchmarks

## Trending Research Themes

- **Simpler, distribution-aware diffusion tuning:** RL Post-Training in Diffusion Transformers Is Activation Steering argues that compact constant shifts can recover much of RL post-training’s reward gain, while Posterior Matching Distillation targets the teacher’s conditional posterior to retain diversity. These are distinct mechanisms, but both question whether more elaborate student updates are necessary.
- **Agents that diagnose before acting:** Pro$^2$ Agent tracks hypotheses about bottlenecks before allocating experiments; AgentRoboCritic scores local robot actions against stated intent; PlayCraft turns agent play into game revisions. Across these papers, feedback is becoming a first-class part of the agent loop, not merely a final score.
- **Video models as bridges from perception to action:** One Prior, Two Dynamics reuses video-generation priors to infer and predict latent actions. Alongside Depth Pro 2’s image/video depth model and AgentRoboCritic’s visual action assessment, this suggests continued convergence of vision and control, though the papers do not establish a single shared method.
- **Inference efficiency is tied to system structure:** TideCache schedules heterogeneous caches and overlaps memory transfer with computation; the diffusion papers reduce student complexity or sampling burden by changing the learning target. These are different layers of the stack, not evidence of a universal efficiency breakthrough.

## Open Problems and Research Directions

- **Does diffusion post-training need input-dependent updates?** The activation-steering paper explicitly leaves preference optimization and reward backpropagation untested. Compare fixed shifts and weight updates under these objectives, on held-out prompts, models, and human preference judgments.
- **Can posterior matching preserve diversity without sacrificing useful alignment?** Posterior Matching Distillation notes multi-draw training costs and an auxiliary adversarial realism loss; its posterior theorem assumes an exact posterior-mean denoiser. Test finite-sample recovery and quality/diversity trade-offs under guided teachers and larger model families.
- **How portable is cache streaming?** TideCache’s measurements cover GB300 and GH200 configurations. Replicate on different interconnects and accelerator generations, and measure tail latency and throughput under realistic mixed workloads.
- **Are autonomous-research gains reproducible?** Pro$^2$ Agent’s complete MLE-Bench results use one run per budget and comparisons span different underlying models. Run multiple seeds and matched-model ablations, then test whether its problem-state representation helps outside competition-style benchmarks.
- **Can intent-based robot critique remain reliable when the intent is wrong?** AgentRoboCritic uses policy-generated local intent and a 400-action human-annotated test set. Evaluate with externally specified intents, independent annotators, and prospective interventions that connect action-level critique to physical task success.
- **Do agent-derived learning measures predict human experience?** PlayCraft’s reported learning gains and slopes come from player agents. A blinded human study should compare engagement, perceived difficulty, and retention against agent-based predictions.
- **Does latent-action transfer survive real deployment?** One Prior, Two Dynamics reports video-based navigation and robot-manipulation transfer. Test the learned action interface in closed-loop physical control across new tasks and embodiments, including failure recovery.

## Takeaway

This batch’s most coherent methodological signal is structured feedback: simple steering or posterior targets for diffusion models, and explicit problem/action states for agents. The results are promising but preliminary—citation evidence is near-zero or unavailable, and several headline claims depend on narrow model, hardware, or evaluation settings that need independent replication.

## Method and sources

- **Window:** Daily; announcement batch Friday 20 November 2026. The latest announcement batch is used because the snapshot was taken Saturday 21 November 2026, when no new daily batch was listed. The API’s first-submission date window for this batch is 19 November 2026 UTC; selected records were published between 01:52:29 and 18:59:57 UTC. Snapshot: 2026-11-21 17:09:14 UTC.
- **Scope/query:** Core categories `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`. Query: `(cat:cs.AI OR cat:cs.LG OR cat:stat.ML OR cat:cs.CL OR cat:cs.CV OR cat:cs.RO OR cat:cs.NE OR cat:cs.MA) AND submittedDate:[202611190000 TO 202611192359]`. The arXiv API returned 546 unique candidates; a companion last-updated-date query found no older submissions revised in this date window. All eight selected abstract pages were verified. No separate subfield filter was applied.
- **Inference:** arXiv publishes no official trending or readership ranking. The ordering prioritizes independent technical discussion and corroborating project/research listings, then cross-category relevance and concrete evaluation evidence; recency is only a tie-breaker. Semantic Scholar was checked for five selected papers; each showed 0 citations at lookup. Citation records were not available for the other three, so citation velocity and influential-citation evidence could not meaningfully rank this very recent batch. Those totals are point-in-time counts, not gains during the window. A paper’s repository, project page, or listing is not treated as a popularity statistic.
- **Reading boundary:** For the top three, arXiv HTML full text was consulted for the introduction, conclusion, and stated limitations. Other paper claims and caveats were checked against arXiv abstracts and the cited project or independent discussion pages. Retrieval caveats are confined to this method section.
- **arXiv sources:** [arXiv recent cs.AI list](https://arxiv.org/list/cs.AI/recent); [RL Post-Training in Diffusion Transformers Is Activation Steering](https://arxiv.org/abs/2611.26627); [Posterior Matching Distillation](https://arxiv.org/abs/2611.26629); [TideCache](https://arxiv.org/abs/2611.26619); [Pro$^2$ Agent](https://arxiv.org/abs/2611.25357); [Depth Pro 2](https://arxiv.org/abs/2611.26603); [AgentRoboCritic](https://arxiv.org/abs/2611.26613); [One Prior, Two Dynamics](https://arxiv.org/abs/2611.26617); [PlayCraft](https://arxiv.org/abs/2611.26624).
- **Corroborating sources:** [Hugging Face Papers](https://huggingface.co/papers/2611.26627); [AI Crunch, activation steering](https://ai-crunch.com/articles/rl-post-training-diffusion-transformers-activation-steering); [Papers with Code, PMD](https://paperswithcode.co/paper/2611.26629); [ModelScope, PMD](https://www.modelscope.cn/papers/2611.26629); [AI Crunch, TideCache](https://ai-crunch.com/articles/tidecache-efficient-hybrid-llm-serving-cache-management-layer-wise-streaming); [AGI Hunt, Pro$^2$ Agent](https://agihunt.info/en/papers/2611.25357); [Apple Research, Depth Pro 2](https://machinelearning.apple.com/research/depth-pro-2-monocular); [OpenReview, Depth Pro 2](https://openreview.net/forum?id=EE8z5PrYeN); [AgentRoboCritic repository](https://github.com/cxcscmu/AgentRoboCritic); [O$^2$LaF project](https://showlab.github.io/o2laf/); [PlayCraft repository](https://github.com/xt4d/PlayCraft).
