## Headline

The latest arXiv biology and biomedical announcement batch is Tuesday, 17 November 2026. From 27 deduplicated new-submission entries in the configured category listings, this report selects seven notable papers; the strongest pattern is data-efficient protein and transcriptome modelling, with complementary MRI measurement methods. Spoken agenda: antibody developability, RNA-based endpoint prediction, then imaging and mechanistic models. arXiv has no official trending chart; this is an inferred relevance ranking from incomplete biomedical coverage, not a popularity ranking. Snapshot: 2026-11-17T17:19:11Z; the current batch is used, not a prior batch.

## Top papers (ranked)

Notable recent papers, ranked by biology/biomedicine relevance and the specificity and type of evidence reported. No reliable attention signal supports calling these the most popular or most-read papers.

### 1. [Multi-Assay Antibody Developability Prediction with Shared Structure-Language Representations](https://arxiv.org/abs/2611.18846)
- **Abstract:** MADM combines per-residue physicochemical descriptors, protein-language-model embeddings and shared multi-assay learning to predict antibody developability measurements.
- **Authors:** Daria B. Kokh
- **arXiv:** `2611.18846v1` (published 2026-11-13T19:04:39Z; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** New q-bio.BM listing; evaluated across eight assays assembled from 29 sources, with cluster-split tests and separate antibody panels.
- **Claimed contribution:** The author reports that structural descriptors match or exceed sequence-language embeddings on some assays; combining streams gives small consistent gains, and sharing training across correlated assays improves some correlations by about 0.1.
- **Caveat:** Several assay results are weaker and vary across data sources; the 80-antibody holdout loses about 0.1 Spearman correlation for most assays. This is retrospective model evaluation, not prospective antibody discovery validation.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [In-context learning predicts clinical endpoints from bulk transcriptomes across diseases and platforms](https://arxiv.org/abs/2611.18774)
- **Abstract:** PRTS uses labelled samples as context to predict diverse endpoints from bulk RNA-seq without per-cohort model training.
- **Authors:** Han Wang, Lennart Purucker, Huafeng Liu, Ziyin Luo, Junfeng Hao, Chao Zhu, Chunjie Tian
- **arXiv:** `2611.18774v1` (published 2026-11-12T10:17:13Z; categories: `q-bio.GN`)
- **Evidence for ranking:** New genomics listing; evaluated on 175 held-out tasks and 44 TCGA tasks after pretraining on 6.0 million generated tasks; weights, code and a 1,160-cohort resource are reported as released.
- **Claimed contribution:** The authors report the highest mean accuracy among tested methods, narrowly ahead of TabPFN v3.5; the advantage is mainly within cohorts, while performance across cohorts and unseen sites is comparable to the strongest baselines.
- **Caveat:** These are retrospective public-data benchmarks, not prospective clinical validation. The paper itself reports that the advantage does not persist across cohorts or unseen sites.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Biomedical & translational medicine

### 3. [Multi-echo AxCaliberSMT: Mapping effective axon radius from restricted diffusion and radius-dependent intra-axonal T2](https://arxiv.org/abs/2611.18911)
- **Abstract:** ME-AxCaliberSMT combines diffusion and relaxation MRI contrasts to estimate effective axon radii across a broader size range than diffusion-only modelling.
- **Authors:** Kwok-Shing Chan, Yohan Jun, Aneri Bhatt, Berkin Bilgic, Susie Y. Huang, Hong-Hsi Lee
- **arXiv:** `2611.18911v1` (published 2026-11-13T20:15:16Z; categories: `physics.med-ph`)
- **Evidence for ranking:** New medical-physics listing; tested in simulations and in five healthy adults, four scanned on a second scanner. The paper reports mean cross-scanner bundle correlation of 0.73.
- **Claimed contribution:** The authors report that combining the two contrasts improved simulated radius accuracy and reproduced bundle-wise patterns on a commercial-gradient scanner, although absolute estimates differed by scanner.
- **Caveat:** The in-vivo sample is small; the authors note no histological validation or same-scanner scan-rescan data, simplifying straight-cylinder assumptions, and 66–68 minute protocols. Estimates remain model- and protocol-dependent.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 4. [Dynamic infrared thermography and computed tomography angiography fusion for DIEP flap perforator selection: a novel measurement system](https://arxiv.org/abs/2611.20545)
- **Abstract:** A workflow aligns dynamic infrared thermography hotspots with CTA-mapped perforators to combine functional perfusion signals with anatomy in DIEP flap planning.
- **Authors:** Warre Clarys, Roanne Van Steen, Simon Verspeek, Filip Thiessen, Gunther Steenackers
- **arXiv:** `2611.20545v1` (published 2026-11-16T05:24:47Z; categories: `physics.med-ph`, `eess.IV`)
- **Evidence for ranking:** New medical-physics listing; evaluated in 12 patients against 46 CTA perforators, and the arXiv record cites a 2026 IEEE Medical Measurements & Applications paper.
- **Claimed contribution:** The authors report linking 39 of 46 CTA perforators to thermal hotspots (84.8%) at a median offset of 14.74 mm, using automated one-to-one assignment to reduce subjective matching.
- **Caveat:** Only 12 patients were studied; 76.1% of detected hotspots had no CTA match, and the authors call for larger cohorts and surface validation. This validates a measurement workflow, not improved surgical outcomes.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 5. [From the possible to the optimal: differentiable optimization of gene regulatory networks](https://arxiv.org/abs/2611.20172)
- **Abstract:** jaxgrn combines differentiable programming with stochastic gene-network simulations to optimize ensembles of regulatory architectures for specified functions.
- **Authors:** Leah Friedman, Gašper Tkačik, Thomas Gregor, Paul François
- **arXiv:** `2611.20172v1` (published 2026-11-15T18:19:52Z; categories: `q-bio.MN`, `q-bio.QM`)
- **Evidence for ranking:** New molecular-networks listing, cross-listed in quantitative biology; the authors optimize thousands of networks under varying noise, precision and scaling constraints.
- **Claimed contribution:** In a morphogen-driven embryonic-patterning model, the authors report that constraints reshape which regulatory architectures support domain formation or positional information; imposing scaling narrows the solutions in some tasks.
- **Caveat:** This is a computational study of a specified model, not experimental evidence that the inferred architectures occur or function in embryos.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** Gene regulation & epigenetics; Molecular & cell biology; Quantitative methods

### 6. [Generation of protein conformations using a simple inverted transformer](https://arxiv.org/abs/2611.19321)
- **Abstract:** A Transformer variant trained on one protein’s all-atom molecular-dynamics conformations is used to generate a weighted ensemble of protein structures.
- **Authors:** Luigi Leonardo Palese
- **arXiv:** `2611.19321v1` (published 2026-11-14T10:32:49Z; categories: `q-bio.QM`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** New quantitative-biology listing, cross-listed in biomolecules; the authors compare generated conformations with molecular-dynamics and experimental structures.
- **Claimed contribution:** The author reports that generated conformations resemble sampled and experimental structures and quickly concentrate in highly populated regions of the studied protein’s conformational landscape.
- **Caveat:** Training and evaluation focus on a particular protein and its MD-derived data. The results do not establish transfer to other proteins or accurate thermodynamic sampling generally.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 7. [An Exploration of Physical and Chemical Representation in Coarse-Grained, Machine-Learned Protein Models](https://arxiv.org/abs/2611.19885)
- **Abstract:** The authors compare seven coarse-graining maps to test how spatial resolution and chemical diversity affect system-specific learned protein models.
- **Authors:** Aldo S. Pasos-Trejo, Luca Sagresti, Cecilia Clementi
- **arXiv:** `2611.19885v1` (published 2026-11-15T09:03:47Z; categories: `q-bio.BM`, `physics.bio-ph`)
- **Evidence for ranking:** New biomolecules listing, cross-listed in biological physics; the comparison varies both bead resolution and embedding type in learned coarse-grained models.
- **Claimed contribution:** The authors report that finer resolution and greater chemical diversity do not automatically improve accuracy; sufficiently expressive latent representations can support accurate protein-specific models with fewer chemical bead types.
- **Caveat:** The results concern system-specific models and the tested mapping choices; broader transfer across proteins and independent experimental validation are not established by the abstract.
- **Announcement type:** new submission, 2026-11-17 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

## Trending Research Themes

- **Protein developability and representation learning:** MADM, the inverted Transformer and coarse-grained model comparison address distinct aspects of antibody properties or protein conformational modelling. Their validation differs—assay-labelled antibody data versus model-generated conformations—so the cluster is a snapshot, not evidence of a field-wide shift.
- **Learning biological function from molecular data or models:** PRTS predicts endpoints from bulk transcriptomes, while jaxgrn searches regulatory-network architectures in simulation. One is retrospective prediction and the other in-silico mechanism exploration; neither alone demonstrates prospective biological or clinical utility.
- **Imaging and measurement methods:** ME-AxCaliberSMT estimates white-matter microstructure and the DIRT–CTA workflow maps perforators. Both include human data, but small cohorts and measurement-level endpoints limit conclusions about clinical utility.

## Open Problems and Research Directions

- **Antibody assay transfer:** The MADM paper reports weaker performance and source variation for some assays. A useful follow-up would prospectively test a blinded, diverse antibody panel across laboratories using harmonized protocols, then separate sequence novelty from assay-source effects.
- **Transcriptome model generalization:** PRTS’s lead is strongest within cohorts and narrows across cohorts or sites. Independent prospective cohorts with locked endpoints, platform-stratified evaluation and external-site holdouts would test whether its contextual advantage transfers.
- **MRI measurement validity:** ME-AxCaliberSMT authors identify a small cohort, no scan-rescan or histological validation, and long acquisition time. Larger same-scanner repeat scans, matched histology where feasible, and optimized protocols could test reproducibility and model assumptions.
- **From models to biology:** jaxgrn and the protein-conformation Transformer derive results from computational systems. Follow-ups could compare prespecified regulatory architectures with perturbation experiments and test the conformation model on held-out proteins using independent structural and kinetic measurements.
- **Surgical imaging evaluation:** The DIRT–CTA paper reports a small cohort and many unmatched thermal hotspots. Multisite cohorts, threshold sensitivity analysis and intraoperative surface validation could assess matching reliability before evaluating effects on surgical decisions.

## Takeaway

This batch combines antibody-assay prediction and transcriptome-based endpoint modelling with two protein-structure methods, a gene-network optimizer and small-cohort MRI measurement studies. The most concrete evidence comes from assay-labelled benchmarks and human imaging feasibility data, but transfer and clinical utility remain open. Treat the ranking as relevance-based, not a measure of popularity or practice-changing evidence.

## Method and sources

- **Window:** daily announcement batch dated 2026-11-17; start and end date are both 2026-11-17. **UTC snapshot:** 2026-11-17T17:19:11Z. The current Tuesday batch was available, so this does not use a prior batch.
- **Scope query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`. Current announcement listings were traversed for q-bio.BM, q-bio.GN, q-bio.MN, q-bio.SC, q-bio.CB, q-bio.TO, q-bio.QM and physics.med-ph. The cs.BI listing was unavailable, so primary cs.BI-only papers may be missing.
- **Candidate pool:** 27 deduplicated new-submission entries across the traversed category listings; seven selected for direct relevance to biomolecules, genomics, molecular networks or biomedicine. Cross-list-only papers were not treated as new submissions. Each selected arXiv abstract page was checked; the top three were also read beyond the abstracts using the available full text.
- **Ranking:** arXiv publishes no official trending or readership chart. Citation and independent-attention evidence did not support a popularity ranking, so this list is ordered by relevance and the type, specificity and validation setting of each study’s reported evidence. No downloads, views or citation gains are inferred.
- **Coverage:** arXiv is not a representative index of biomedical work. Much experimental biology and clinical preprint research appears on bioRxiv or medRxiv. This is not a systematic review, clinical guideline or clinical evidence assessment.
- **Category listings:** [q-bio.BM](https://arxiv.org/list/q-bio.BM/new), [q-bio.GN](https://arxiv.org/list/q-bio.GN/new), [q-bio.MN](https://arxiv.org/list/q-bio.MN/new), [q-bio.SC](https://arxiv.org/list/q-bio.SC/new), [q-bio.CB](https://arxiv.org/list/q-bio.CB/new), [q-bio.TO](https://arxiv.org/list/q-bio.TO/new), [q-bio.QM](https://arxiv.org/list/q-bio.QM/new), [physics.med-ph](https://arxiv.org/list/physics.med-ph/new).
- **Selected source pages:** [2611.18846](https://arxiv.org/abs/2611.18846), [2611.18774](https://arxiv.org/abs/2611.18774), [2611.18911](https://arxiv.org/abs/2611.18911), [2611.20545](https://arxiv.org/abs/2611.20545), [2611.20172](https://arxiv.org/abs/2611.20172), [2611.19321](https://arxiv.org/abs/2611.19321), [2611.19885](https://arxiv.org/abs/2611.19885). The DIRT–CTA study’s cited conference record is [IEEE MeMeA 2026](https://doi.org/10.1109/memea69746.2026.11537361).
