# arXiv Trending AI — 2026-09-24 batch

The strongest signal in the latest available batch is a move toward grounded, testable control of AI systems: papers stress-test multimodal alignment, speech fact-checking, policy steering, RL post-training, and privacy leakage rather than treating benchmark scores as sufficient. arXiv has no official trending chart; this is an inferred ranking from cross-list breadth, conference-acceptance metadata, methodological reach, and the limited early citation evidence available.

## Top papers (ranked)

### 1. [Minimally Invasive Steering of Language Models](https://arxiv.org/abs/2609.30218)
- **Abstract:** The paper proposes MISVO, a Fisher/KL-geometry regularized method for steering frozen language models at test time while limiting distributional damage.
- **Authors:** Taha Entesari, Jingyu Zhang, Daniel Khashabi, Mahyar Fazlyab
- **arXiv:** `2609.30218v1` (published 2026-09-24 17:46 UTC; categories: `cs.LG`, `cs.AI`)
- **Evidence for ranking:** Semantic Scholar metrics were unavailable for this paper because the API returned rate limits; cross-listed in AI and ML, provides a formal first-order KL/Fisher analysis, and reports the highest mean reward in six of seven model–task settings across preference and code-generation tasks.
- **Claimed contribution:** The authors introduce MISVO and derive an analytic Fisher-based surrogate for position-specific steering without updating model parameters.
- **Caveat:** The evidence is from a preprint and seven model–task settings; the reported gains and diversity/coherence behavior need broader independent replication.
- **Announcement type:** new submission, latest available batch dated 2026-09-24
- **Themes:** Training & adaptation; Safety & alignment; Efficient inference & systems

### 2. [PoEM: Predicting RL Outcomes from Existing Policies](https://arxiv.org/abs/2609.30226)
- **Abstract:** PoEM predicts the policy produced by reinforcement learning on a new reward by combining models already trained on other rewards, avoiding another RL run.
- **Authors:** Kimia Hamidieh, Giannis Daras, Antonio Torralba
- **arXiv:** `2609.30226v1` (published 2026-09-24 17:50 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.CV`)
- **Evidence for ranking:** Semantic Scholar metrics were unavailable because the API returned rate limits; unusually broad four-category cross-listing, a potentially high-impact post-training shortcut, and validation on synthetic and real rewards across text and image modalities.
- **Claimed contribution:** The authors show that reward-conditioned log-policies can often occupy an approximately low-rank subspace and use this to approximate a target RL policy without additional RL training.
- **Caveat:** The low-rank relationship is empirical outside the linear-reward case; generalization to substantially different reward families and model scales remains open.
- **Announcement type:** new submission, latest available batch dated 2026-09-24
- **Themes:** Training & adaptation; Efficient inference & systems; Agents & reasoning

### 3. [The Alignment Illusion in Multimodal Large Language Models](https://arxiv.org/abs/2609.30210)
- **Abstract:** Controlled visual-stream corruption shows that common scalar visual–text alignment measures can remain high even when MLLM task accuracy collapses, motivating a principal-angle-gap diagnostic.
- **Authors:** Hong-Han Wang, Yuntao Wang, Hu Ding
- **arXiv:** `2609.30210v1` (published 2026-09-24 17:42 UTC; categories: `cs.CV`, `cs.LG`)
- **Evidence for ranking:** Semantic Scholar reports 0 citations and 0 influential citations at snapshot time; the paper is accepted to NeurIPS 2026, tests 13 MLLMs from five families, and directly challenges a widely used interpretability/evaluation assumption.
- **Claimed contribution:** The authors identify weight-induced alignment as a source of misleading similarity scores and propose the principal-angle gap, which tracks task accuracy more consistently in their experiments.
- **Caveat:** The diagnostic is evaluated on the tested architectures, corruption settings, and tasks; its behavior on other multimodal designs is not established.
- **Announcement type:** new submission, latest available batch dated 2026-09-24
- **Themes:** Multimodal & vision-language; Interpretability; Evaluation & benchmarks

### 4. [To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech](https://arxiv.org/abs/2609.30227)
- **Abstract:** VeriSpeak benchmarks spoken-claim verification and finds a text–speech modality gap, with explicit reasoning over retrieved evidence outperforming retrieval alone.
- **Authors:** Debajyoti Mazumder, Mamta, Abhirama Subramanyam Penamakuri
- **arXiv:** `2609.30227v1` (published 2026-09-24 17:50 UTC; categories: `cs.LG`, `cs.AI`, `cs.CL`, `cs.SD`)
- **Evidence for ranking:** Semantic Scholar metrics were unavailable because the API returned rate limits; four-category cross-listing, accepted to EMNLP 2026, a 3,879-claim benchmark, and a reported 86.1% accuracy for a thinking-tuned LALM with retrieval plus explicit reasoning.
- **Claimed contribution:** The authors introduce VeriSpeak and show that grounded claim–evidence comparison is needed for speech misinformation detection.
- **Caveat:** The benchmark and result depend on the selected spoken-claim distribution and model setup; 86.1% is an author-reported result, not an independently verified ranking.
- **Announcement type:** new submission, latest available batch dated 2026-09-24
- **Themes:** Evaluation & benchmarks; Retrieval & knowledge; Multimodal & vision-language

### 5. [Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning](https://arxiv.org/abs/2609.30258)
- **Abstract:** TRACE reconstructs private embodied-RL observation–action trajectories from consecutive policy gradients by exploiting temporal correlation and policy-head structure.
- **Authors:** Sudip Bhujel, Shanghao Shi, Ruiquan Huang, Ning Zhang, Yang Xiao
- **arXiv:** `2609.30258v1` (published 2026-09-24 17:59 UTC; categories: `cs.LG`)
- **Evidence for ranking:** Semantic Scholar metrics were unavailable because the API returned rate limits; accepted to NeurIPS 2026, reports 18.8 dB PSNR, near-perfect action recovery, and 3–4.5 ms per reconstructed frame across several victim architectures and modalities.
- **Claimed contribution:** The authors introduce TRACE, formalize a temporal leakage signal, and derive an exact action-recovery condition under sufficiently small entropy regularization.
- **Caveat:** The attack results are preprint claims evaluated on held-out embodied scenes; the proposed need for sequence-aware defenses requires further validation under deployed privacy mechanisms.
- **Announcement type:** new submission, latest available batch dated 2026-09-24
- **Themes:** Safety & alignment; Robotics & control; Interpretability

### 6. [Agentic Detection of Online Conspiracies](https://arxiv.org/abs/2609.30250)
- **Abstract:** An agentic, context-aware workflow uses adaptive social queries to infer the intent behind conspiracy-related Hebrew social-media posts.
- **Authors:** Lior Biton, Oren Tsur
- **arXiv:** `2609.30250v1` (published 2026-09-24 17:58 UTC; categories: `cs.CL`, `cs.LG`)
- **Evidence for ranking:** Semantic Scholar metrics were unavailable because the API returned rate limits; cross-listed in language and ML, uses a large four-year public-tweet collection, and reports that agentic context-aware workflows significantly outperform text-only and matched-context non-agentic settings.
- **Claimed contribution:** The authors frame conspiracy detection as socially embedded interpretation and supply tools for per-case evidence gathering.
- **Caveat:** The dataset is Hebrew and the evaluation is tied to its manually annotated adversarial set; transfer to other languages, platforms, and political contexts is not shown.
- **Announcement type:** new submission, latest available batch dated 2026-09-24
- **Themes:** Agents & reasoning; Evaluation & benchmarks; Retrieval & knowledge

## Trending Research Themes

- **Grounded evaluation is replacing proxy alignment signals.** The Alignment Illusion shows that internal similarity scores can decouple from task accuracy, while VeriSpeak finds that retrieval without explicit claim–evidence reasoning is insufficient.
- **Post-training is becoming more modular and cheaper.** MISVO steers frozen models with a local KL geometry, and PoEM attempts to synthesize a new reward-conditioned policy from existing post-trained policies instead of rerunning RL.
- **Agents are being evaluated as adaptive evidence-seeking systems.** Agentic Detection of Online Conspiracies reports gains from per-case social-context queries rather than a fixed context window.
- **Privacy risk is moving from parameters to learning signals.** TRACE shows that sequential gradients in embodied learning can leak trajectories and actions, extending the threat model beyond single-update attacks.

## Open Problems and Research Directions

- **Open problem — transfer of diagnostics:** The Alignment Illusion leaves open whether the principal-angle gap remains reliable across newer projector designs, video/audio inputs, and tasks where geometry and behavior diverge. A follow-up should preregister corruption tests across architectures and compare PA gap against causal ablations.
- **Open problem — reward-space coverage:** PoEM's approximate low-rank assumption may fail for discontinuous, adversarial, or distribution-shifting rewards. Test its error as a function of reward distance, basis-policy diversity, and model scale, with a held-out reward family.
- **Open problem — safe steering boundaries:** MISVO reports reward gains with near-Best-of-N diversity/coherence, but the operational boundary between useful steering and hidden capability or safety degradation is unclear. Evaluate adversarial rewards, refusal behavior, calibration, and long-horizon distribution drift.
- **Open problem — sequence-aware defenses:** TRACE suggests that protecting individual gradients may not protect trajectories. Compare temporal clipping, noise correlated across steps, secure aggregation, and representation-level defenses under a common privacy–utility budget.
- **Research direction — multimodal grounded agents:** VeriSpeak and Agentic Detection of Online Conspiracies jointly motivate agents that retrieve evidence across speech, text, and social context while exposing the evidence-to-claim comparison step for audit.

## Takeaway

The batch is notable less for one dominant model release than for a common methodological demand: AI systems should be tested against causal corruption, grounded evidence, reward changes, and information leakage. The ranking remains provisional—most papers are brand-new, and only one selected paper had an accessible Semantic Scholar record, with 0 citations at the snapshot.

## Method and sources

- Window: daily; latest available arXiv announcement/submission batch checked on 2026-09-27, with selected papers submitted 2026-09-24. Snapshot: 2026-09-27 15:10 UTC.
- Corpus: recent arXiv API results across `cs.AI`, `cs.LG`, `stat.ML`, `cs.CL`, `cs.CV`, `cs.RO`, `cs.NE`, and `cs.MA`; selected papers were verified on their arXiv abstract pages.
- Ordering: inferred, not official. Signals were cross-list breadth, conference-acceptance metadata, substantive methodological contribution, reported evaluation breadth, and Semantic Scholar citation fields where available. arXiv publishes no official trending chart; this is not a most-read or most-downloaded list.
- Sources: [TRACE](https://arxiv.org/abs/2609.30258), [Agentic Detection](https://arxiv.org/abs/2609.30250), [VeriSpeak](https://arxiv.org/abs/2609.30227), [PoEM](https://arxiv.org/abs/2609.30226), [MISVO](https://arxiv.org/abs/2609.30218), [Alignment Illusion](https://arxiv.org/abs/2609.30210).
