# Biology and biomedicine — Friday, 20 November 2026 arXiv batch

## Headline

12 notable recent papers. The batch’s strongest through-line is computational molecular and biomedical methods: protein/ligand and RNA design, uncertainty-aware genomics, multimodal cancer data, and medical imaging. Spoken agenda: molecular design first, then structural and genomic methods, followed by pathology and clinical-physics applications. arXiv has no official trending chart; this is an inferred, relevance-ranked selection from incomplete biomedical coverage, not a most-read or most-downloaded list. Attention evidence was sparse, so papers are ranked by relevance and reported evaluation rather than popularity.

## Top papers (ranked)

### 1. [ShEPhERD-score: Fast, adaptable three-dimensional alignment of molecular features](https://arxiv.org/abs/2611.25076)
- **Abstract:** The authors combine differentiable 3D molecular similarity representations with CPU/GPU kernels for high-throughput alignment and screening, reporting competitive DUDE-Z benchmark results and up to 1.03 million alignments per second on one GPU.
- **Authors:** Nate Somers, Kento A. Abeywardane, Connor W. Coley, Masha Elkin
- **arXiv:** `2611.25076v1` (published 2026-11-18T19:17:58Z; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct biomolecular/drug-design fit; matched results on 43 protein targets, comparable or better than reference tools in 8 of 9 cases. No Semantic Scholar record at snapshot; the benchmark, not popularity, supports its placement.
- **Claimed contribution:** The authors present a unified, modular and differentiable toolkit for 3D molecular alignment and screening; target-wise results indicate no single scoring mode wins across targets.
- **Caveat:** This is computational benchmark evidence, not prospective compound testing or experimental evidence of binding or efficacy; the best scoring mode varies by target.
- **Announcement type:** new submission, 20 November 2026 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [The Montparnasse Algorithm for RNA Design](https://arxiv.org/abs/2606.07562)
- **Abstract:** The v2 paper reports a Monte Carlo search algorithm for inverse RNA folding that solved a median 96 of 100 Eterna100 V1 targets over five runs, versus 90 for DesiRNA under the same folding model and budget.
- **Authors:** Tristan Cazenave
- **arXiv:** `2606.07562v2` (first published 2026-05-25T17:06:26Z; v2 revised 2026-11-19T18:10:48Z; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** Listed as a replacement in the 20 November batch; direct RNA-design relevance and a five-run, 100-target benchmark. Semantic Scholar reports 1 citation in total at snapshot, not a gain during this window.
- **Claimed contribution:** The author reports improved search coverage and speed on Eterna100 V1 using a shared ViennaRNA 1.8.5/Turner 1999 objective.
- **Caveat:** The result is computational folding under one energy model; it does not establish that designed RNAs fold as intended in biochemical experiments or cells.
- **Announcement type:** revision (v2), 20 November 2026 batch; revised 19 November UTC
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis

### 3. [A General Harness for Protein Foundation Model Fitness Prediction](https://arxiv.org/abs/2609.34654)
- **Abstract:** The v2 work adds MSA retrieval and structure-aware score corrections to frozen protein-model predictions, reporting improved rank correlations across three variant benchmarks covering 1,211 assays and 3.1 million measured variants.
- **Authors:** Yang Tan, Qijia Tian, Gangyu Sun, Bozitao Zhong, Mingchen Li, Yuanxi Yu, Nanqing Dong, Liang Hong
- **arXiv:** `2609.34654v2` (first published 2026-09-28T08:58:56Z; v2 revised 2026-11-19T12:44:46Z; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Protein-function relevance; replacement in the 20 November q-bio.QM batch; reported gains across ProteinGym, VenusMutHub and VenusViroHub. Semantic Scholar reports 1 citation in total at snapshot, not a period gain.
- **Claimed contribution:** The authors’ training-free VenusREM-Harness combines model scores with evolutionary and structural evidence; they report gains across 71 configurations and an average ProteinGym Spearman of 0.556 for VenusREM2.
- **Caveat:** These are retrospective benchmark results, not prospective protein-engineering experiments; performance depends on benchmark composition, homolog coverage and the chosen assays.
- **Announcement type:** revision (v2), 20 November 2026 batch; revised 19 November UTC
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 4. [Ab-initio cryo-EM reconstruction from moments of denoised images](https://arxiv.org/abs/2611.25525)
- **Abstract:** The authors use the first three moments of denoised particle images to initialize cryo-EM reconstruction without estimating each particle orientation, and report successful refinement starts on six experimental datasets.
- **Authors:** Yunpeng Shi, Amit Singer, Yuguan Wang, Andy Zhang
- **arXiv:** `2611.25525v1` (published 2026-11-19T05:26:45Z; categories: `q-bio.QM`)
- **Evidence for ranking:** Structural-biology method tested on six public experimental macromolecular datasets; the authors report high-resolution refinement comparable to established initializers. Code is public; no Semantic Scholar record at snapshot.
- **Claimed contribution:** The authors’ MoMDeni method estimates an ab-initio model from denoised-image moments, avoiding explicit orientation estimation and assuming non-uniform viewing directions.
- **Caveat:** The authors call the experimental results preliminary; denoising biases moment estimates, loses fine structure, and the method can fail for low-molecular-weight targets.
- **Announcement type:** new submission, 20 November 2026 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [An Explainable and Scalable Hierarchical Tensor Framework for Integrating Multi-Omics and Digital Pathomics](https://arxiv.org/abs/2611.25584)
- **Abstract:** HIT-Fuse combines six molecular and pathology modalities across four TCGA cancer cohorts and reports survival stratification, cohort-dependent prediction gains and database-based support for some decoded drivers.
- **Authors:** Ahmad Hussein, Ali Anaissi, Mukesh Prasad, Ali Braytee
- **arXiv:** `2611.25584v1` (published 2026-11-19T06:27:17Z; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Direct genomics and multi-omics focus; four TCGA cohorts; reported cross-checks with DepMap, miRTarBase and RPPA annotations. No Semantic Scholar record at snapshot.
- **Claimed contribution:** The authors propose hierarchical tensor fusion with missing-modality reconstruction and traceable attributions; they report a 56.4% relative weighted-F1 increase for glioma after cohort expansion.
- **Caveat:** The evaluation uses TCGA-derived cohorts and computational/database cross-checks; it is not independent clinical validation, and reconstructed modalities may affect cohort composition and performance.
- **Announcement type:** new submission, 20 November 2026 batch
- **Themes:** DNA & genomics; Omics & single-cell methods; Biomedical & translational medicine

### 6. [From Sequence Uncertainty to Phenotype Hypotheses: Uncertainty-Conditioned Inference over Biomedical Knowledge Graphs](https://arxiv.org/abs/2611.25422)
- **Abstract:** The authors propagate genomic-model uncertainty into graph-supported phenotype-hypothesis distributions and report held-out association recovery on AlzKB and Hetionet.
- **Authors:** Huixin Zhan, Jason H. Moore
- **arXiv:** `2611.25422v1` (published 2026-11-19T03:02:19Z; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Cross-listed in genomics; tests on two biomedical knowledge graphs and 30 gene-holdout masks, with recall@10 above DistMult on 24 masks. No Semantic Scholar record at snapshot.
- **Claimed contribution:** The authors introduce an uncertainty-conditioned path-energy method to allocate probability across gene–disease–phenotype routes without patient-level phenotype supervision.
- **Caveat:** This is computational hypothesis ranking, not diagnosis or clinical validation; the authors note the gene-holdout advantage is driven mainly by three genes and is not established for all genes.
- **Announcement type:** new submission, 20 November 2026 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Biomedical & translational medicine

### 7. [Dynamical Variational Theory of Stochastic Reaction Networks](https://arxiv.org/abs/2611.25491)
- **Abstract:** A Plefka-expansion variational method approximates non-Markovian dynamics and fluctuations in stochastic reaction networks, with tests on gene regulation, enzyme kinetics and infection models.
- **Authors:** Moshir Harsh, Peter Sollich
- **arXiv:** `2611.25491v1` (published 2026-11-19T04:26:42Z; categories: `cond-mat.stat-mech`, `q-bio.MN`, `q-bio.PE`)
- **Evidence for ranking:** Cross-listed in molecular networks; evaluates multiple biochemical and biological model classes, including low-copy-number fluctuations. No Semantic Scholar record at snapshot.
- **Claimed contribution:** The authors derive a tractable dynamical variational approximation for general stoichiometries and time-varying rates, including a self-consistent bubble resummation.
- **Caveat:** The reported support is numerical benchmarking against model systems, not direct experimental validation of a biochemical mechanism.
- **Announcement type:** new cross-list, 20 November 2026 batch
- **Themes:** Molecular & cell biology; Quantitative methods

### 8. [OpenTME: An Open Dataset of AI-powered H&E Tumor Microenvironment Profiles from TCGA](https://arxiv.org/abs/2604.12075)
- **Abstract:** The v2 release describes AI-derived tumor-microenvironment profiles for 5,268 TCGA whole-slide images across ten cancer types, with more than 20,000 quantitative readouts per slide.
- **Authors:** Maaike Galama, Nina Kozar-Gillan, Christina Embacher, Todd Dembo, Cornelius Böhm, Evelyn Ramberger, Julika Ribbat-Idel, Rosemarie Krupar, Verena Aumiller, Miriam Hägele, Kai Standvoss, Gerrit Erdmann, Blanca Pablos, Ari Angelo, Simon Schallenberg, Andrew Norgan, Viktor Mátyás, Klaus-Robert Müller, Maximilian Alber, Lukas Ruff, Frederick Klauschen
- **arXiv:** `2604.12075v2` (first published 2026-04-13T21:27:29Z; v2 revised 2026-11-19T14:52:15Z; categories: `cs.CV`, `cs.AI`, `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** Replacement in the 20 November q-bio.QM batch; large shared resource derived from 5,268 slides across ten cancer types. Semantic Scholar reports 3 citations in total at snapshot, not a period gain.
- **Claimed contribution:** The authors release an open-access, living dataset of model-generated cell, tissue and spatial-neighborhood readouts for computational tumor-microenvironment research.
- **Caveat:** The readouts inherit the underlying AI models’ errors; the paper notes limited cancer-type coverage and that detailed spatial coordinates are not included in the public release.
- **Announcement type:** revision (v2), 20 November 2026 batch; revised 19 November UTC
- **Themes:** Biomedical & translational medicine; Omics & single-cell methods

### 9. [When Foundation Models Disagree: Representational Heterogeneity for Calibrated Uncertainty in Whole-Slide Image Classification](https://arxiv.org/abs/2611.26159)
- **Abstract:** CALIFUSE uses disagreement among pathology foundation-model representations to estimate confidence and reports improved calibration and misclassification detection across seven whole-slide-image tasks.
- **Authors:** Yekai Shen, Yuqian Wang, Zishun Liao, Rongsheng Wang, Wenting Chen, S. Kevin Zhou, Qingsong Yao
- **arXiv:** `2611.26159v1` (published 2026-11-19T14:15:07Z; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Seven WSI classification tasks and an arXiv comment reporting acceptance at IEEE BIBM 2026; no Semantic Scholar record at snapshot.
- **Claimed contribution:** The authors use between-encoder representational heterogeneity and chunk-level evidence agreement as uncertainty cues, without training an additional fusion module.
- **Caveat:** The reported evidence is benchmark evaluation; calibration and selective prediction results do not establish clinical utility or transfer to other institutions and scanners.
- **Announcement type:** new cross-list, 20 November 2026 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 10. [GraphEP: A Calibrated Data System and Benchmark for Learning Cardiac Electrophysiology](https://arxiv.org/abs/2611.26551)
- **Abstract:** GraphEP packages 732 simulated cardiac electrophysiology trajectories across 20 anatomies and benchmarks graph and physiology-informed models for predicting transmembrane potential.
- **Authors:** Matteo Baldan, Chiara D'Ercoli, James Rowbottom, Pietro Liò, Stefania Fresca
- **arXiv:** `2611.26551v1` (published 2026-11-19T18:23:10Z; categories: `q-bio.TO`)
- **Evidence for ranking:** New q-bio.TO dataset/benchmark; 732 simulations spanning healthy and scarred substrates and multiple pacing configurations. No Semantic Scholar record at snapshot.
- **Claimed contribution:** The authors provide a reproducible graph-native dataset and report that physiology-informed models perform best on complementary prediction metrics.
- **Caveat:** The benchmark is based on mechanistic simulations rather than measured patient electrophysiology; model performance does not demonstrate clinical readiness.
- **Announcement type:** new submission, 20 November 2026 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 11. [Towards consensus on practical probabilistic evaluation metrics for clinical decision making in radiotherapy](https://arxiv.org/abs/2611.25260)
- **Abstract:** The authors evaluate probabilistic robustness metrics for proton radiotherapy using 60 treatment plans from three Dutch centers and interviews with eight radiation oncologists.
- **Authors:** Jenneke I. de Jong, Steven J. M. Habraken, Erik W. Korevaar, Mirko Unipan, Esther Kneepkens, Gloria Vilches Freixas, Yvonne L. B. Klaver, Michiel Kroesen, Alejandra Méndez Romero, Edwin Oldehinkel, Stephanie Peeters, Roel J. H. M. Steenbakkers, Karolien Verhoeven, Stefan Both, Liesbeth J. B. Boersma, Sebastiaan Breedveld, Mischa S. Hoogeman
- **arXiv:** `2611.25260v1` (published 2026-11-18T22:44:24Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Direct medical-physics study; 60 proton plans across three centers and structured interviews with eight oncologists. No Semantic Scholar record at snapshot.
- **Claimed contribution:** The authors compare probabilistic metrics with current robustness evaluation and report that interviewed oncologists considered them suitable, while metric preferences varied.
- **Caveat:** This is a plan-based evaluation plus interviews, not a trial showing improved patient outcomes; the authors call for further consensus and clinical validation before broad implementation.
- **Announcement type:** new submission, 20 November 2026 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 12. [Physics-Informed Deep Learning for Shear Wave Speed Estimation in MR Elastography](https://arxiv.org/abs/2611.26111)
- **Abstract:** An end-to-end physics-informed reconstruction and inversion method estimates shear-wave speed from undersampled MRE data, reporting a 30% NRMSE reduction versus total-variation minimization and evaluation on in-vivo data.
- **Authors:** Stefan Martin, Jakob Schattenfroh, Patrick Schuenke, Felix Frederik Zimmermann, Ingolf Sack, Christoph Kolbitsch, Andreas Kofler
- **arXiv:** `2611.26111v1` (published 2026-11-19T13:39:46Z; categories: `eess.IV`, `cs.LG`, `physics.med-ph`)
- **Evidence for ranking:** Direct medical-imaging method, accepted/published in IEEE Transactions on Biomedical Engineering (DOI: 10.1109/TBME.2026.3666306); reports acceleration factors up to 19 and in-vivo evaluation. No Semantic Scholar record at snapshot.
- **Claimed contribution:** The authors jointly train reconstruction and phase-gradient inversion to estimate tissue shear-wave speed directly from k-space.
- **Caveat:** The reported evaluation is retrospective and does not establish multi-site generalization or improved clinical decisions; no sample size for the in-vivo data is stated in the abstract.
- **Announcement type:** new cross-list, 20 November 2026 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

## Trending Research Themes

- **Molecular design and protein/RNA scoring:** ShEPhERD-score, Montparnasse and the protein-fitness harness all use computational search or model-scoring benchmarks. Their results are not wet-lab evidence of improved drug binding, RNA folding in cells or engineered-protein performance.
- **Data-driven molecular and cancer representations:** MoMDeni estimates macromolecular structure from cryo-EM image moments; HIT-Fuse combines omics with pathology; OpenTME releases AI-derived tumor-microenvironment profiles. These are different contributions—reconstruction method, integrative prediction framework and dataset—not independent replications of one result.
- **Uncertainty and structure in biomedical prediction:** The sequence-to-phenotype method allocates uncertainty over knowledge-graph hypotheses, while CALIFUSE estimates slide-level confidence from pathology-model disagreement. Neither is a clinical decision system validated for care.
- **Physics and mechanistic models:** Stochastic reaction networks and GraphEP encode biological dynamics using mechanistic structure; radiotherapy and MRE papers address uncertainty or inversion in medical-physics workflows. Evidence ranges from mathematical/simulation benchmarks to retrospective data and expert interviews.

## Open Problems and Research Directions

- **Validate design and fitness claims experimentally.** Montparnasse and the protein-fitness harness are benchmark-driven; ShEPhERD-score reports virtual-screening comparisons and target-specific scoring. A useful next step would be blinded, prospective testing on held-out RNA targets and protein families, with biochemical structure/function assays and pre-specified comparators. This is a synthesis proposal, not a claim that the studies already show experimental gains.
- **Stress-test molecular imaging under realistic noise and domain shift.** MoMDeni’s authors identify biased moments after denoising and failures on low-molecular-weight targets. Compare direct raw-image moment estimation and improved denoisers across independent cryo-EM datasets stratified by size, SNR and orientation distribution; report failure rates as well as resolution.
- **Test transfer and calibration for omics/pathology resources.** HIT-Fuse, OpenTME and CALIFUSE rely on TCGA or benchmark tasks. Independent cohorts with different sites, scanners and modality-missingness patterns could establish which predictions and uncertainty estimates transfer; measure calibration and subgroup performance before translational claims.
- **Move from simulated or retrospective imaging to external validation.** GraphEP is simulation-derived, while the MRE and radiotherapy studies use retrospective plans/data and limited expert interviews. External multi-center datasets and prospective workflow studies could test robustness and decision impact; these preprints do not establish patient benefit.

## Takeaway

The 20 November batch is strongest in computational molecular design, molecular/genomic modeling and imaging methods. The most biologically grounded evidence here includes cryo-EM tests on six experimental datasets and several large retrospective benchmarks, but none should be mistaken for broad clinical validation. Because measurable attention signals were sparse, this is a relevance-ranked snapshot, not a defensible popularity chart.

## Method and sources

- **Window:** daily announcement batch dated 2026-11-20; exact report window 2026-11-20 through 2026-11-20. Snapshot: 2026-11-20T17:17:31Z. This is not a prior batch: arXiv’s relevant `new` listings showed Friday, 20 November 2026. For revisions, the batch date is the listing date; the latest-version timestamps are shown separately and precede the batch by one UTC day.
- **Coverage:** traversed the current `new` listings for `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph`; audited the full Computer Science `new` listing for `cs.BI` (no cs.BI-tagged papers surfaced). The 20 Nov q-bio aggregate showed 35 entries: 11 new submissions, 8 cross-lists and 16 replacements. The physics.med-ph batch showed 5 entries. Cross-lists were deduplicated by arXiv ID. Selected items were checked on their arXiv abstract pages.
- **Candidate query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`. The arXiv API was used to verify paper IDs, versions, first-submission/update timestamps and categories; daily inclusion was determined from the dated announcement listings, including replacements.
- **Ranking signals:** The Semantic Scholar Graph API was checked for the selected IDs. It had no record for the nine new submissions; for the three revisions it returned current citation totals of 1 (Montparnasse), 1 (protein-fitness harness) and 3 (OpenTME), with zero influential citations. These are current totals, not gains in this window. Targeted web searches did not surface independent technical discussion; author-linked code and package materials were treated as reproducibility resources, not popularity evidence. With attention evidence sparse, papers are ordered by relevance to molecular biology/biomedicine and the scope of reported evaluation.
- **Coverage caveat:** arXiv is not a representative biomedical preprint index; much experimental and clinical biology appears on bioRxiv or medRxiv. This report does not cover those repositories or the medical literature as a whole.
- **Sources:** [q-bio daily listing](https://arxiv.org/list/q-bio/new), [q-bio.BM](https://arxiv.org/list/q-bio.BM/new), [q-bio.GN](https://arxiv.org/list/q-bio.GN/new), [q-bio.MN](https://arxiv.org/list/q-bio.MN/new), [q-bio.SC](https://arxiv.org/list/q-bio.SC/new), [q-bio.CB](https://arxiv.org/list/q-bio.CB/new), [q-bio.TO](https://arxiv.org/list/q-bio.TO/new), [q-bio.QM](https://arxiv.org/list/q-bio.QM/new), [physics.med-ph](https://arxiv.org/list/physics.med-ph/new), [Computer Science daily listing](https://arxiv.org/list/cs/new), and individual arXiv abstract/PDF links above. The MRE paper’s published version is [IEEE TBME, DOI 10.1109/TBME.2026.3666306](https://doi.org/10.1109/TBME.2026.3666306).
