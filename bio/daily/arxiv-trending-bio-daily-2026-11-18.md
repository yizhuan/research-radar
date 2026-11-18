# Notable recent biology and biomedicine papers on arXiv — 2026-11-18 batch

Today’s configured biology/biomedicine listings yielded **9 selected papers** for the latest announcement batch (papers have UTC submission timestamps on 2026-11-16–17). The dominant pattern is machine-learning methods for spatial transcriptomics, perturbation biology, and molecular discovery, alongside mechanistic models and experimental validation. arXiv has no official trending chart; this is an inferred, evidence-ranked list from an incomplete preprint corpus, using category relevance, cross-list breadth, external discussion, journal status, and Semantic Scholar metadata—not downloads or readership.

Snapshot: 2026-11-18 17:17 UTC. Daily reporting uses the latest available announcement batch; no 2026-11-18 UTC-submitted API records were returned at snapshot time. Because attention evidence is sparse, this is titled **Notable recent papers**, not a measured popularity ranking.

## Top papers (ranked)

### 1. [Discovery of new antiviral agents through artificial intelligence: in vitro and in vivo results](https://arxiv.org/abs/2611.22230)
- **Abstract:** A deep-reinforcement-learning platform generated 60,291 neuraminidase-targeting molecules; nine were selected for testing, and two inhibited influenza A/B neuraminidase and viral replication in cells, with activity also reported in mice.
- **Authors:** Roza Izmailyan; Mher Matevosyan; Hamlet Khachatryan; Anastasiya Shavina; Smbat Gevorgyan; Artur Ghazaryan; Irina Tirosyan; Yeva Gabrielyan; Marusya Ayvazyan; Boris Martirosyan; Vardan Harutyunyan; Hovakim Zakaryan
- **arXiv:** `2611.22230v1` (published 2026-11-17T05:22:24Z; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** Independent corroboration: PubMed record and DOI; Semantic Scholar reports 24 citations and a journal-article record.
- **Claimed contribution:** The authors report a computational-to-experimental pipeline, including enzyme, cell-based, and mouse studies; the arXiv record links an Antiviral Research 2024 article and DOI 10.1016/j.antiviral.2024.105818.
- **Caveat:** This is an accepted manuscript of a 2024 journal article rather than a new experimental result; the abstract does not establish human efficacy, safety, or clinical utility.
- **Announcement type:** new submission, announcement-batch date 2026-11-18
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 2. [Structured AI ideation yields physical strategies for epithelial barrier repair](https://arxiv.org/abs/2611.22988)
- **Abstract:** Abelio combines structured divergent/convergent AI ideation with literature search and refinement; the authors tested its proposed PEG and cholesterol-anchored complementary-DNA interventions in damaged Caco-2 monolayers.
- **Authors:** Geonho Nah; Johyun Park; Kyung-Ah Cho; Suyoung Hwang; Yoon Hee Lim; Eun-kyung Min; Seunghyun Moon; Donghyun Koh; Seungwon Kim; Jiho Park; Hojin Yoo; Myungsun Nam; Haneul Choi; Kyungsu Kim; In-Sun Hong; YunJae Jung; Minhyeong Lee
- **arXiv:** `2611.22988v1` (published 2026-11-17T16:05:22Z; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Independent attention: the full PDF is available on arXiv; Semantic Scholar indexes 67 references but reports zero citations for this new record.
- **Claimed contribution:** The paper reports benchmark comparisons against four frontier LLMs and cell-monolayer assays: PEG preserved barrier readouts, while complementary DNA produced sequence-specific and reversible effects.
- **Caveat:** The biological tests are in an in-vitro Caco-2 model; proposed PEG/DNA configurations are not directly observed, and the evaluation of scientific soundness includes an LLM judge.
- **Announcement type:** new submission, announcement-batch date 2026-11-18
- **Themes:** Molecular & cell biology; DNA & genomics; Quantitative methods

### 3. [ST-FateFlow: Continuous Gene-Spatial Reconstruction with Differentiation-Potential Learning from Time-Resolved Spatial Transcriptomics](https://arxiv.org/abs/2611.22256)
- **Abstract:** ST-FateFlow uses structure-aware transport coupling and flow matching to interpolate gene-expression and spatial dynamics between unpaired time-resolved spatial-transcriptomics snapshots and learn a differentiation-associated potential.
- **Authors:** Zhe Yu; Xiaobo Sun; Hao Wu
- **arXiv:** `2611.22256v1` (published 2026-11-17T06:00:29Z; categories: `q-bio.GN`)
- **Evidence for ranking:** Relevance signal: primary q-bio.GN listing and a dedicated arXiv paper; Semantic Scholar reports zero citations and 0 references for the newly indexed record.
- **Claimed contribution:** Across multiple public developmental and regenerative datasets, the authors report improvements in distributional and spatial interpolation metrics and consistency with known trajectories.
- **Caveat:** The method depends on cross-time coupling and registration quality and missing intermediate states; its potential is a relative ordering, not a fate probability or physical energy, and there are no new human or animal experiments.
- **Announcement type:** new submission, announcement-batch date 2026-11-18
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 4. [HoloGene: Learning to Lift Sliced Spatial Transcriptomics to Holistic 3D Gene Fields](https://arxiv.org/abs/2611.20368)
- **Abstract:** HoloGene models discontinuous spatial-transcriptomics sections as continuous 3D gene-expression fields with an anisotropic conditional implicit neural representation.
- **Authors:** Yumin Zheng; Qingtian Zhu; Ziyan Zhu; Kailu Song; Yinqiang Zheng; Jun Ding
- **arXiv:** `2611.20368v1` (published 2026-11-16T00:58:29Z; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Independent discussion: NeurIPS 2026 poster listing and a public GitHub repository; Semantic Scholar reports 30 references and zero citations.
- **Claimed contribution:** Using held-out measured sections, the authors report better reconstruction accuracy and biological-preservation metrics than general-purpose INR and adapted spatial-transcriptomics baselines; code is linked.
- **Caveat:** The output is an inferred 3D field from sliced measurements, not direct observation of unsampled tissue; performance depends on registration, data distribution, and the held-out-section validation design.
- **Announcement type:** new submission, announcement-batch date 2026-11-18
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 5. [OCCAM: Improved Single-Cell Representation Learning and Perturbation Effect Prediction](https://arxiv.org/abs/2611.21959)
- **Abstract:** OCCAM is an MLP framework that combines denoising-based cell representations with gene-interaction, text, and protein-sequence features to predict genetic-perturbation effects across cell contexts and combinations.
- **Authors:** Ihab Bendidi; Kian Kenyon-Dean; Alisandra K. Denton; Auguste Genovesio; Emmanuel Noutahi
- **arXiv:** `2611.21959v1` (published 2026-11-16T22:40:16Z; categories: `q-bio.QM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Relevance signal: cross-listed q-bio.QM/cs.AI/cs.LG and Semantic Scholar indexing with 28 references; zero citations is expected for a new submission.
- **Claimed contribution:** The authors report cross-context few-shot, held-out-cell-line, and double-perturbation comparisons against retrained competitors and simple baselines.
- **Caveat:** The paper says expression-level prediction remains challenging; reported gains are benchmark-model results, not evidence of biological or therapeutic effect in patients.
- **Announcement type:** new submission, announcement-batch date 2026-11-18
- **Themes:** Omics & single-cell methods; Bioinformatics & sequence analysis; Quantitative methods

### 6. [Diversity Preservation Recovers Transcription Factor Motifs Across Challenging Confounder Landscapes](https://arxiv.org/abs/2611.21859)
- **Abstract:** The paper combines evolvable motif length with MAP-Elites diversity archives to improve transcription-factor motif recovery under confounding sequences.
- **Authors:** Alejandro Medina; Mary Lauren Benton
- **arXiv:** `2611.21859v1` (published 2026-11-16T20:23:15Z; categories: `cs.NE`, `q-bio.GN`)
- **Evidence for ranking:** Relevance signal: q-bio.GN cross-list, five-dataset evaluation, and 35 references in Semantic Scholar; zero citations for the new record.
- **Claimed contribution:** On five liver ChIP-seq datasets, the archives recovered target signals more reliably than a survivor-selection baseline and were comparable to or more robust than MEME in the reported settings.
- **Caveat:** Motif annotation remains difficult: neither method consistently ranks targets above close relatives for HNF4A and JUND across the full width range.
- **Announcement type:** new submission, announcement-batch date 2026-11-18
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 7. [Molecular memory reduces timing noise in stochastic gene expression](https://arxiv.org/abs/2611.22554)
- **Abstract:** Analytical and stochastic-simulation results indicate that multistep mRNA production and degradation can reduce first-passage-time noise in bursty gene-expression models through different mechanisms.
- **Authors:** Kuheli Biswas; Supravat Dey; Abhyudai Singh
- **arXiv:** `2611.22554v1` (published 2026-11-17T10:43:07Z; categories: `q-bio.MN`, `cond-mat.stat-mech`)
- **Evidence for ranking:** Relevance signal: primary q-bio.MN listing and a cross-list to statistical physics; Semantic Scholar reports one reference and zero citations.
- **Claimed contribution:** The authors derive small-noise-limit statistics and compare them with stochastic simulations beyond that approximation.
- **Caveat:** The claims are model-based and the analytical results have stated regime-of-validity limits; no biochemical or cellular experiment is reported.
- **Announcement type:** new submission, announcement-batch date 2026-11-18
- **Themes:** Molecular & cell biology; Quantitative methods

### 8. [Rule-based curation and validation in batch fermentation of a genome-scale metabolic model of the mycoprotein fungus Fusarium venenatum A3/5](https://arxiv.org/abs/2611.21775)
- **Abstract:** The authors build and curate the iJL1143 genome-scale metabolic model for Fusarium venenatum A3/5 and validate it against four oxygen-enriched batch fermentations.
- **Authors:** Jaewook Lee; Thomas Vinestock; Miao Guo
- **arXiv:** `2611.21775v1` (published 2026-11-16T19:05:11Z; categories: `q-bio.MN`)
- **Evidence for ranking:** Relevance signal: primary q-bio.MN listing, fermentation experiments, and 54 references in Semantic Scholar; zero citations for the new record.
- **Claimed contribution:** Rule-based curation reduced mean final-biomass discrepancy from 20% to 6% against the draft model; adding a fitted lag time reduced biomass time-course error from 4.88 to 0.42 g/L.
- **Caveat:** Validation is limited to the reported strain, oxygen-enriched batch setting, substrates, and model comparisons; performance does not establish transfer to other feedstocks or production conditions.
- **Announcement type:** new submission, announcement-batch date 2026-11-18
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 9. [Optimising Recruitment and Sample Allocation in Multi-Site Rare Disease Studies](https://arxiv.org/abs/2611.22907)
- **Abstract:** A cardinality-optimisation framework allocates recruitment and metabolomic samples across sites while balancing yield, cost, capacity, and logistics.
- **Authors:** Farid Zare; Catherine Clancy; Tal Dattner; Martina Messina; Julian Teinert; Jack McGoldrick; Pavel Ješina; Sabine Weller Grønborg; Ute Spiekerkoetter; James J O’Byrne; Trine Tangeraas; Maria Luz Couce; José A. Cocho; Javier de las Heras; Niklas Darin; Dorothea Möslinger; Peter Witters; Ina Knerr; Giancarlo La Marca; Ans T. van der Ploeg; Hidde H. Huidekoper; Terry G. J. Derks; Francjan J. van Spronsen; Sandra D. K. Kingma; Anibh M. Das; Carlo Dionisi-Vici; Clara D. van Karnebeek; Julia B. Hennermann; Siobhán O’Sullivan; Sabine A. Fuchs; Luciana Hannibal; M. Rebecca Heiner-Fokkema; Marek J. Noga; Irene M. L. W. Körver-Keularts; Katja Benedikte Prestø Elgstøen; George J. G. Ruijter; J. J. M. Jans; Amy Harms; Thomas Hankemeier; Maurizio Scarpa; Ines Thiele; Shamima Rahman; Stefan Kölker; Ronan M. T. Fleming
- **arXiv:** `2611.22907v1` (published 2026-11-17T15:11:13Z; categories: `q-bio.QM`, `math.OC`)
- **Evidence for ranking:** Relevance signal: q-bio.QM primary listing, a concrete rare-disease application, and 34 Semantic Scholar references; zero citations for the new record.
- **Claimed contribution:** In simulated multi-centre scenarios for a project targeting 1,900 diagnosed patients across 24 centres and eight laboratories, the model maintained feasibility under constraints and reduced unconstrained metabolomic-analysis costs by about 30% versus heuristic baselines.
- **Caveat:** The evidence is simulation and operational modelling; it does not show that the allocation improves outcomes or recruitment in a completed clinical study.
- **Announcement type:** new submission, announcement-batch date 2026-11-18
- **Themes:** Biomedical & translational medicine; Omics & single-cell methods; Quantitative methods

## Trending Research Themes

- **Spatial transcriptomics as a continuous inference problem:** ST-FateFlow and HoloGene infer unobserved molecular/spatial structure from sparse or sliced measurements; both remain computational reconstructions rather than direct measurements.
- **AI-assisted perturbation and molecular discovery:** OCCAM targets cross-context perturbation prediction, while the antiviral paper combines reinforcement learning with enzyme, cell, and mouse testing; Abelio links structured ideation to Caco-2 barrier assays.
- **Mechanistic and constraint-aware modelling:** Molecular memory studies stochastic timing, the IFFL paper derives dose-ordering conditions, the Fusarium work curates a genome-scale model against fermentation, and the rare-disease paper optimises study logistics.
- **Robustness under confounding:** The motif paper explicitly tests diversity preservation across five liver ChIP-seq datasets, illustrating the field’s focus on evaluation choices and close biological confounders.

## Open Problems and Research Directions

- **Validate inferred spatial trajectories prospectively:** For ST-FateFlow and HoloGene, test on denser time points, independently collected tissues, and perturbation-defined intermediate states; report sensitivity to registration and batch effects.
- **Move AI molecular proposals beyond early validation:** For the antiviral and Abelio studies, replicate across independent laboratories, expand cell and animal cohorts with prespecified controls, and compare against strong contemporary baselines. These are research proposals, not clinical recommendations.
- **Stress-test transferability:** Evaluate OCCAM, motif recovery, and metabolic-model predictions on unseen assays, strains, tissues, feedstocks, and laboratories, with calibration and failure-case reporting.

## Takeaway

The clearest cluster today is computational biology that reconstructs, predicts, or optimises biological systems, with a smaller but important bridge to wet-lab validation. The antiviral and epithelial-barrier papers have the strongest experimental grounding; spatial-transcriptomics and perturbation papers are promising method reports but depend on benchmark design and inferred structure. None supports clinical practice changes.

## Method and sources

Window: daily; exact reporting date 2026-11-18; snapshot 2026-11-18 17:17 UTC. Candidate categories: `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. I queried the arXiv API with the explicit OR category query, checked recent category listings, deduplicated by versionless arXiv ID, and verified retained records on arXiv abstract pages. Ranking uses the disclosed evidence hierarchy; citation totals are current Semantic Scholar totals, not gains during this window.

Sources: arXiv abstract pages linked above; arXiv API (`https://export.arxiv.org/api/query`); Semantic Scholar Graph API queried with `ARXIV:<id>`; PubMed/DOI corroboration for arXiv:2611.22230 (`https://pubmed.ncbi.nlm.nih.gov/38280564/`, `https://doi.org/10.1016/j.antiviral.2024.105818`); NeurIPS listing and code link for HoloGene (`https://neurips.cc/virtual/2026/poster/152255`, `https://github.com/Szym29/HoloGene`).
