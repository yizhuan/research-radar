# arXiv Giant Watch - Weekly - 2026-11-22

## Headline

This week's notable work clusters around self-improving agent harnesses, governed continual adaptation, and specification-driven evaluation, with several production-scale deployments from Google and Alibaba. A secondary thread concerns measurement rigor, from auditing image-compression gains to diagnosing representation collapse.

## Notable Papers

### 1. Self-Improvement Memory Enables Continual Recursive Self-Improvement

- arXiv: `2611.18856`
- Organizations: Google
- Attribution: verified - Google (United States), Google Cloud AI Research
- Problem: Harness optimization is typically studied with a fixed policy model and benchmark; when either changes, the optimizer lacks a record of why prior edits were made or how they performed.
- Method: Proposes Self-Improvement Memory (SIM) for the harness optimizer, grouping edits by recurring harness problem and recording rationale, predicted and observed outcomes, and evaluation context to support Continual Recursive Self-Improvement (CRSI).
- Key result: Across four domains, SIM achieves higher final scores than harness-only and root-cause-only continuation; in coding, paired continuations improve final scores by an average of 2.36 points over harness-only (p=0.003) across ten source runs.
- Caveat: Reported gains are relative to specific continuation baselines within the authors' experimental setup; no independent replication is described.
- Why it matters: Frames memory of past optimization as a first-class component for agents that must keep improving across changing models and benchmarks.

### 2. Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses

- arXiv: `2611.22299`
- Organizations: Google
- Attribution: verified - Google (United States), Google
- Problem: Static agent harnesses tuned for one model or task stall, waste tokens, or regress on others, motivating systems that inspect their own traces and rewrite their own code.
- Method: A unifying architectural framework pairing four editable runtime components (context/state, control, action interfaces, verification/recovery) with a four-stage diagnose-patch-validate-deploy loop, plus defenses against prompt bloat, benchmark gaming, and evaluator tampering.
- Key result: On SWE-bench Lite, gated modular evolution outperforms prompt reflection and full-harness rewrites across models and repositories at a fraction of the token cost.
- Caveat: Evaluation is limited to SWE-bench Lite; the framework is largely architectural and design-oriented.
- Why it matters: Provides a structured, safety-aware blueprint for self-modifying agent runtimes, complementing memory-based approaches to harness improvement.

### 3. G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands

- arXiv: `2611.17814`
- Organizations: Qwen
- Attribution: verified - Alibaba Group (China), Alibaba Group (alibaba-inc.com
- Problem: Demand drift and harness evolution in e-commerce agents cause once-trained models to fall behind, while periodic manual retraining is slow and labor-intensive.
- Method: G-CAST converts daily production evidence into reward-routed, entropy-prioritized training data with governed reward evolution and governed checkpoint transition under cumulative evaluation.
- Key result: On a real production e-commerce agent, G-CAST adapts better to newly introduced demand while better preserving previously accepted behavior than a strong autonomous post-training baseline; ablations support both data orchestration and governed reward evolution.
- Caveat: Results are from a single production deployment (Yuancai on Alibaba's 1688); generalization beyond this setting is not established.
- Why it matters: Demonstrates governed continual self-training in a live commercial agent, connecting continual learning research to deployed systems.

### 4. HardwareDx: A Foundational Graph Model System for Datacenter Machine Repairs

- arXiv: `2611.23398`
- Organizations: Google
- Attribution: verified - Google (United States), Google , Mountain View , CA , USA
- Problem: Hardware failures in hyperscale AI clusters stall expensive training workloads, making machine downtime economically costly.
- Method: A graph foundation model approach to automated datacenter hardware diagnosis, allowing a single model to diagnose many platforms and accelerate onboarding of new hardware.
- Key result: Deployed at production scale at Google, HardwareDx reduces downtime by 18.3% on GPU platforms and 16.1% on TPUs, and cuts QA time by 28.3% for GPUs and 25.1% for TPUs.
- Caveat: Reported figures are production evaluations from Google's own infrastructure; external validation is not described.
- Why it matters: Shows graph foundation models delivering measurable operational gains in AI infrastructure reliability.

### 5. LogT: Logically Think with Images for Visual Search

- arXiv: `2611.19200`
- Organizations: Meta
- Attribution: probable - https://huggingface.co/facebook
- Problem: Vision-language models struggle to combine logical reasoning with accurate and efficient tool use for fine-grained visual search.
- Method: LogT, an automated SFT data engine enforcing logic-chain-guided reasoning, generating visually grounded questions and structured tool-use traces; validated by fine-tuning Qwen2.5-VL-7B and InternVL3.5-8B.
- Key result: LogT-SFT on Qwen2.5-VL-7B outperforms a state-of-the-art SFT+RL method using 3.1x less data and >120x fewer GPU hours; a simple RL recipe on top yields a 9.59-point margin over prior complex RL setups.
- Caveat: Organization attribution is probable, not verified; results are tied to the two base models and seven benchmark test sets used.
- Why it matters: Argues that SFT data quality, not RL complexity, is the key bottleneck for tool-using visual reasoning.

### 6. FVScore: Specification-Driven Neuro-Symbolic Video Evaluation

- arXiv: `2611.22673`
- Organizations: Google
- Attribution: verified - Google (United States), Google Cloud AI Research ,
- Problem: Existing video-generation evaluators rely on holistic MLLM judgments or vision-language metrics that are hard to align with human judgments and hard to trace to specific temporal violations.
- Method: FVSCORE compiles explicit prompt propositions and implicit physical/temporal/cross-modal constraints, grounds them with specialized perceptual tools, evaluates confidence traces with soft temporal operators inspired by Linear Temporal Logic, and applies significance-aware calibration.
- Key result: Across public and complex multi-event benchmarks with strong video models, FVSCORE outperforms holistic and agent-based evaluators in human correlation while producing timestamp- and evidence-grounded feedback.
- Caveat: Correlation-based evaluation depends on the human-judgment benchmarks used; no single absolute accuracy figure is claimed.
- Why it matters: Advances interpretable, specification-driven evaluation for generative video, a prerequisite for reliable model comparison.

### 7. LIC-Audit: How Comparable Are Reported Gains in Learned Image Compression?

- arXiv: `2611.23419`
- Organizations: Google
- Attribution: verified - Google (United States), Google
- Problem: Learned image compression papers report small BD-rate gains against changing VTM reference versions, raising questions about comparability across papers.
- Method: Audits 353 released rate-distortion curves from 36 repositories and re-evaluates eight public codec releases with 28,193 encode-decode records, examining reference-version effects, measurement conventions, and per-image variability.
- Key result: Different VTM reference runs shift BD-rates by up to 3.56 percentage points; under consistent measurement a 1.00% lead becomes a 1.43% deficit, and padding changes alone can reverse method comparisons; the work also provides a versioned protocol, leaderboard, and reporting guidelines.
- Caveat: The audit covers released curves and eight codec releases, so conclusions are bounded by that corpus.
- Why it matters: Exposes fragility in small reported gains and offers infrastructure for verifiable progress claims in a subfield.

### 8. SADL: On the Demand-Supply Geometry of Representation Collapse

- arXiv: `2611.21596`
- Organizations: Qwen
- Attribution: verified - Alibaba Group (China), Alibaba Group
- Problem: In Joint-Embedding Predictive Architectures, a well-constrained projector output does not prevent representation collapse, because encoder representations are dominated by an input-shared component.
- Method: SADL (Supply And Demand Loss) keeps the original objective and constrains the encoder directly only when the representation differences the projector demands exceed what the encoder can supply, adding no auxiliary networks or parameters.
- Key result: In LeWM and INTACT experiments, SADL lowers collapse rate over ten random seeds from 50% to 0%; after one epoch, encoder effective rank is 3.4-6.4x baseline and latent prediction error falls to 1/20-1/303; INTACT exceeds 95% mean search-free control success with several demand regularizers.
- Caveat: Results are from the authors' LeWM/INTACT setups and four image datasets; broader architecture coverage is not claimed.
- Why it matters: Offers a principled, low-overhead fix for a persistent failure mode in self-supervised representation learning.

## Research Themes

- Self-improving agent harnesses and runtime adaptation (2611.18856, 2611.22299)
- Governed continual learning under distribution and capability drift (2611.17814, 2611.18856)
- Specification-driven and audited evaluation of generative outputs (2611.22673, 2611.23419)
- Production-scale deployment of learned systems (2611.23398, 2611.17814)

## Takeaway

The week's strongest signals are self-modifying agent harnesses and governed continual adaptation, with both Google and Alibaba contributing production-grounded work. A parallel emphasis on measurement rigor—auditing compression gains and grounding video evaluation in specifications—suggests growing attention to verifiable claims. Attribution for the Meta-linked LogT paper remains probable rather than confirmed.

## Sources and Method

Papers were retrieved from the public arXiv API. Organization attribution is retained only when supported by an arXiv affiliation or author-line signal; model mentions alone are excluded. DeepSeek synthesized only the supplied metadata.
