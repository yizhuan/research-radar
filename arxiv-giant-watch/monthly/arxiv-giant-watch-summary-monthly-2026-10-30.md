# arXiv Giant Watch - Monthly - 2026-10-30

## Headline

This month's notable papers span agentic geospatial reasoning, lab-in-the-loop molecular design, hardware-diverse AI training, and verification-driven or streaming agentic systems. Google, Meta, and Alibaba/Qwen each contribute work with verified affiliations.

## Notable Papers

### 1. Google Earth AI Geospatial Reasoning Agent: Capabilities and a Systematic Evaluation

- arXiv: `2610.15750`
- Organizations: Google
- Attribution: verified - Google Research, Google Geo
- Problem: Answering complex geospatial questions requires combining data, foundation models, tools, and planning, but systematic evaluation of such agents is limited.
- Method: Introduces GeoExpertQueries and GeoKTools and compares a standalone LLM, basic tools, GRA tools without upfront planning, and full GRA using Gemini 3.1 Pro and Gemini 3.8 Flash.
- Key result: GRA performs well on templated and open-ended problems; domain tools and skills provide the largest gain, and planning further improves open-ended performance enough for Flash to match or exceed Pro at lower cost.
- Caveat: Benchmark limitations include evolving ground truth and tool/data access differences.
- Why it matters: Provides a systematic evaluation framework and shows that tools, skills, and planning can let a cheaper model match or exceed a stronger one on open-ended geospatial tasks.

### 2. Aptamers as a sandbox for lab-in-the-loop agentic molecular discovery

- arXiv: `2610.24806`
- Organizations: Google
- Attribution: verified - Google Research, Google Cloud, Google DeepMind
- Problem: Tests whether LLM-based agents can improve biomolecular design through iterative wet-lab feedback.
- Method: Three design-test-improve cycles for DNA aptamer binders to alpha-thrombin and myoglobin, with about 4,400 sequenced constructs.
- Key result: Bead-corrected on-target hit rates rose to 42.1% and 33.5% in round three; agents diagnosed cross-reactivity and changed strategies, restoring myoglobin specificity to 72.4%; orthogonal titrations agreed with pooled enrichment (Pearson r=0.90).
- Caveat: Strictly de novo scaffolds remained low-micromolar binders, while preliminary nanomolar affinities involved literature-derived motifs; empirical lab feedback was more useful than computational proxies in this setting.
- Why it matters: Demonstrates a closed-loop agentic discovery workflow where wet-lab feedback drives strategy changes, while carefully separating de novo from literature-derived performance.

### 3. Architecting for Hardware Diversity: Meta's End-to-End Co-Design for High-Performance AI Training on AMD GPUs

- arXiv: `2610.22230`
- Organizations: Meta
- Attribution: verified - Meta
- Problem: Studies production training of recommendation models on AMD MI350X versus NVIDIA B200.
- Method: Combines hardware-model co-design, Origami analytical kernel selection, and agentic workflows for kernel optimization and portability.
- Key result: Across production workloads MI350X reaches a geometric-mean throughput of 101% of the B200 baseline; compared with a directly ported baseline, the methods deliver up to 1.5x end-to-end throughput; Origami predicts optimal kernels with 93% accuracy.
- Caveat: Remaining GEMM performance gaps and a focus on DLRMs rather than a full LLM-specific study.
- Why it matters: Shows end-to-end co-design can make AMD GPUs competitive with NVIDIA for production recommendation-model training, while flagging remaining gaps and scope limits.

### 4. ImageRSI: Verification-Driven Recursive Self-Improvement for Agentic Image Generation

- arXiv: `2610.32120`
- Organizations: Qwen
- Attribution: verified - Qwen Business Unit of Alibaba, Alibaba Token Hub
- Problem: Improving agentic image generation without updating the underlying generator.
- Method: Keeps the generator frozen and combines five-dimensional verification and repair, a cross-task experience library admitted only after paired A/B validation, and offline judge updating with SFT and GRPO.
- Key result: On ImageReq-Bench (961 requests) reaches 65.66% Checklist Strict Accuracy, 9.28 percentage points above the strongest baseline; on MindBench reaches 52.6%, 10.2 points above the strongest baseline.
- Caveat: Evaluation depends on checklist/judge quality and the benchmark setup, and the generator itself is not updated.
- Why it matters: Shows verification-driven self-improvement can raise agentic image-generation accuracy while keeping the generator frozen, with explicit dependence on judge quality.

### 5. SyncPro: Synchronous Reasoning and Responding for Proactive Streaming Video Understanding

- arXiv: `2610.32132`
- Organizations: Qwen
- Attribution: verified - Qwen Business Unit of Alibaba
- Problem: Proactive streaming video understanding requires reasoning and responding to proceed concurrently.
- Method: Dual-stream system with separate inner reasoning and user-facing response branches sharing causal history and activating independently; trained on 189K dual-stream examples using supervised fine-tuning and trajectory-level reinforcement learning.
- Key result: On StreamingBench achieves 41.2% accuracy within a two-second response window, 3.2 points above the strongest compared baseline; also reports gains on OVO-Bench and ProactiveVideoQA.
- Caveat: Benchmark-specific evaluation and code not yet released at submission.
- Why it matters: Introduces a concurrent reasoning-and-response architecture for proactive streaming video, with gains reported across multiple streaming benchmarks.

## Research Themes

- Agentic systems with verification and iterative feedback loops
- Tool use and planning as drivers of agent performance
- Closed-loop integration of agents with external environments (geospatial tools, wet labs, hardware kernels)
- Benchmark-specific evaluation with explicit caveats about ground truth and judge quality

## Takeaway

The selected papers center on agentic systems that improve through verification, planning, and external feedback rather than model updates alone. Google, Meta, and Alibaba/Qwen contributions all carry verified affiliations, and each paper states its own evaluation caveats. No temporal comparison is supported by the supplied metadata, so no portfolio shift is claimed.

## Sources and Method

Papers were identified from arXiv records and HTML pages; the arXiv API returned HTTP 429 during retrieval, so this report uses the accessible arXiv paper pages instead. Organization attribution is retained only where the paper itself lists an affiliation to the organization; model mentions alone are excluded. The synthesis uses the supplied paper metadata and abstracts only.
