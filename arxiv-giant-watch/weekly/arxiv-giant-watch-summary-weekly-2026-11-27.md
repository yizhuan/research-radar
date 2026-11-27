# arXiv Giant Watch - Weekly - 2026-11-27

## Headline

This week’s notable papers cover unified 4D world representations, agentic knowledge engineering and co-evolution benchmarks, open-weight safety auditing, and scalable medical AI evaluation. Four selections have verified affiliation matches; WorldLatent has a probable Google match via its Hugging Face organization account.

## Notable Papers

### 1. WorldLatent: A Unified 4D Latent Space for World Perception and Generation

- arXiv: `2611.31209`
- Organizations: Google
- Attribution: probable - https://huggingface.co/google
- Problem: 4D spatiotemporal vision lacks a shared representational protocol, so perception (depth, camera estimation) and generation are handled by separate one-way pipelines or unaligned single-modality spaces.
- Method: WorldLatent proposes a multimodal VAE that compresses and fuses 4D appearance, geometry, and dynamics into a single structured latent space, with perception and generation treated as complementary denoising processes over that shared space in one training loop.
- Key result: The abstract reports specialist-level zero-shot 4D perception, coherent 4D generation, and controllable editing from a single model across representative 4D benchmarks.
- Caveat: Organization attribution is probable, not confirmed; the abstract reports qualitative claims without numeric metrics, and no independent replication is indicated.
- Why it matters: It frames a common latent protocol for 4D understanding and generation, analogous to shared token representations in language models, as a foundation for general-purpose 4D spatial intelligence.

### 2. AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering

- arXiv: `2611.27734`
- Organizations: Qwen
- Attribution: verified - Alibaba DAMO Academy (China), Alibaba Group (China), Alibaba DAMO Academy , Alibaba Group
- Problem: It is unresolved whether autonomous agents can construct ontologies that help them solve real tasks, and whether such knowledge offers measurable benefits over alternative representations; existing benchmarks evaluate ontology correctness or task success in isolation.
- Method: AutoOntologyBench is a task-grounded benchmark of 19,947 audited tasks grounded in 18 real-world knowledge sources across 7 domains, with source-native verification, spanning Application, Repair, Organization, and Construction, comparing nine frontier-model agents under matched knowledge representations.
- Key result: Layered on retrieval, agent-built ontologies add 6.1 points of task success but trail an expert-derived reference by 13.0, identifying autonomous knowledge acquisition as the bottleneck.
- Caveat: The verified organization match is at the affiliation level; author-level attribution is not confirmed. Results are abstract-reported and limited to the benchmark's nine agents and seven domains.
- Why it matters: It separates the value of autonomously acquired knowledge from raw task success, giving a task-grounded measure of where agentic scientific research falls short.

### 3. CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?

- arXiv: `2611.27116`
- Organizations: Qwen
- Attribution: verified - Alibaba Group (China), Alibaba Group
- Problem: Agent performance depends on both model and harness, but existing benchmarks evaluate post-training or data research with the harness out of scope, or harness optimization with the model fixed, leaving the joint decision unmeasured.
- Method: CoEvoBench evaluates LLMs as researchers co-evolving a target agent's model and harness across five agentic domains, starting from a common base model and initial harness within a 24-hour budget and scoring submitted model-harness pairs on separate test tasks.
- Key result: Across five frontier researchers, the strongest closes more than four fifths of the gap to an instruction-tuned reference system; co-evolution succeeds on interaction tasks but rarely on long-horizon coding.
- Caveat: Organization attribution is verified at the affiliation level, not per author. The abstract reports relative gap closure without absolute scores, and the finding is limited to five researchers and five domains.
- Why it matters: It provides a controlled testbed for recursive improvement, suggesting current LLMs can make a strong first improvement but cannot yet convert feedback from an improved system into the next one.

### 4. Cleave: Severing Guardrails and Auditing Spectral Coupling in Open-Weight LLMs

- arXiv: `2611.27426`
- Organizations: Qwen
- Attribution: verified - Alibaba Group (China), Alibaba Group , China
- Problem: Open-weight LLMs are deployed locally beyond provider control, and their embedded safety guardrails are found to rely on residual writing weights that can be directly edited.
- Method: Cleave is a training-free attack that edits residual writing weights to remove all guardrails or selectively lift only cybersecurity restrictions; a dual-stage defense combines pre-release subspace diagnostics with post-release weight-coupling audits.
- Key result: Across five open-weight LLMs from 7B to 320B parameters, Cleave reaches up to 67.97% attack success on seven safety benchmarks, boosts executable exploit generation by up to 24.0 times on 356 cybersecurity tasks and 15 live vulnerable services, and compromises up to 66.7% of targets; the defense reports 100% detection recall at 1% false-positive rate.
- Caveat: Organization attribution is verified at the affiliation level, not per author. The abstract reports attack and defense results without external validation, and selective removal retains up to a 99% refusal rate on other harmful requests, which may affect detection.
- Why it matters: It shows that open-weight guardrails can be severed by weight edits that evade behavioral spot-checks and static audits, and proposes coupled diagnostics as a countermeasure.

### 5. Scalable Evaluation of Medical AI using Evidence-based Practice Recommendations

- arXiv: `2611.27007`
- Organizations: Google
- Attribution: verified - Google (United States), Google Research ,
- Problem: Rigorous medical AI evaluation requires open-ended clinical management testing across diverse presentations and care stages, but existing benchmarks rely on manual expert authoring, limiting coverage of conditions, conditional pathways, and evolving guidelines.
- Method: An automated pipeline extracts and verifies structured clinical criteria and branching decision trees from practice recommendations to generate scenarios; applied to 436 BMJ Best Practice monographs, it yields 3,200 scenarios plus targeted regional and temporal suites, graded by a clinician-calibrated autorater on a 4-point severity-stratified rubric.
- Key result: Scaling improves Gemini adherence; web search adds 0.8 pp on average and multi-sample synthesis adds 2.2 pp, combining additively to 2.8 pp; web search narrows international gaps by 4.2 pp and improves adherence to updated guidance by 4.6 pp; in a study with 9 primary care physicians over 200 scenarios, AI assistance raises adherence from 50.5% to 70.0%.
- Caveat: Organization attribution is verified at the affiliation level, not per author. The physician study is small (n = 9), and the evaluation is tied to BMJ Best Practice monographs and Gemini models.
- Why it matters: It offers a scalable, guideline-grounded evaluation setup for medical AI and evidence that AI assistance can improve clinician decision-making, largely by reducing clinical omissions.

## Research Themes

- Unified representations and protocols spanning perception, generation, and knowledge organization
- Benchmarks that measure agentic capability end to end rather than in isolation
- Safety and evaluation rigor for deployed models, from open-weight guardrails to clinical adherence

## Daily-edition continuity

The weekly rollup covers one daily report (2026-11-25). It already featured "Unifying Partner and Environment Diversity to Improve Human-AI Coordination" (arXiv:2611.32031) at daily rank #1; it appeared once, so no paper recurred across multiple daily editions. The arXiv author metadata lists University of Washington email domains, not a tracked major AI organization. The earlier Meta match arose from the surname "Fairhall" and is not evidence of Meta affiliation, so this paper is recorded as continuity but excluded from this week’s ranked selections.

## Takeaway

The selected work links shared representations with task-grounded evaluation: a unified 4D latent space, benchmarks for ontology-building and agent co-evolution, and guideline-grounded clinical scenarios. Cleave reports a way to remove open-weight guardrails and an auditing defense. Four papers have verified affiliation matches; one has a probable Google attribution, not confirmation of every author’s affiliation.

## Sources and Method

Papers were retrieved from the public arXiv API. Organization attribution is retained only when supported by arXiv affiliation, OpenAlex affiliation, a Hugging Face organization account, or a reliable author-line signal; model mentions alone are excluded. DeepSeek synthesized only the supplied metadata.
The arXiv listing reached the 2,000-paper retrieval cap, so the candidate pool may be incomplete; rankings reflect the retrieved papers only.
