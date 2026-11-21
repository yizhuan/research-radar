# Biology and biomedicine — Friday, 20 November 2026 arXiv batch

## Headline

The latest arXiv announcement batch available on Saturday, 21 November is Friday, 20 November; no newer batch is listed for today. Fifteen notable recent papers are highlighted from 40 deduplicated records in the configured q-bio and medical-physics batch listings. The strongest pattern is computational methods grounded in molecular, genomic, pathology, and clinical-physics data. Spoken agenda: RNA/protein design, structural biology, multi-omics, then translational evaluation. arXiv has no official trending chart; this is an inferred relevance ranking from incomplete biomedical coverage, not a measured popularity list or a survey of bioRxiv, medRxiv, or the medical literature.

## Top papers (ranked)

Notable recent papers — ordered by biology/biomedicine relevance and reported evidence, not by measured popularity.

### 1. [ShEPhERD-score: Fast, adaptable three-dimensional alignment of molecular features](https://arxiv.org/abs/2611.25076)
- **Abstract:** A modular differentiable toolkit aligns 3D molecular representations and performs comparably to or better than matched open-source tools in eight of nine DUDE-Z virtual-screening comparisons.
- **Authors:** Nate Somers; Kento A. Abeywardane; Connor W. Coley; Masha Elkin
- **arXiv:** `2611.25076v1` (published 2026-11-18T19:17:58Z; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct molecular-design fit; the paper benchmarks 43 protein targets and reports throughput up to 1.03 million alignments per second on one GPU. Open-source implementation is linked by the authors.
- **Claimed contribution:** The authors present a unified differentiable framework for 3D molecular alignment across shape, electrostatic, and pharmacophore objectives.
- **Caveat:** Evidence is computational virtual screening and alignment performance, not experimental binding or therapeutic activity; the best scoring mode varies by target.
- **Announcement type:** new submission, 2026-11-20
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [The Montparnasse Algorithm for RNA Design](https://arxiv.org/abs/2606.07562)
- **Abstract:** The v2 paper reports a Monte Carlo inverse-folding solver that solved a median 96 of 100 Eterna100 V1 targets over five runs, versus 90 for DesiRNA under the same folding model and budget.
- **Authors:** Tristan Cazenave
- **arXiv:** `2606.07562v2` (published 2026-05-25T17:06:26Z; revised 2026-11-19T18:10:48Z; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** Direct RNA-design relevance; five-run, 100-target benchmark with ViennaRNA 1.8.5 and the Turner 1999 model held constant between solvers.
- **Claimed contribution:** The author combines nested rollout search, structural priors, local repair, and parallel workers to improve inverse RNA-folding coverage and speed.
- **Caveat:** Results are computational predictions under one secondary-structure energy model; they do not establish that designed RNAs fold as intended in biochemical assays or cells.
- **Announcement type:** revision, 2026-11-20 batch; v2 revised 2026-11-19
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis

### 3. [A General Harness for Protein Foundation Model Fitness Prediction](https://arxiv.org/abs/2609.34654)
- **Abstract:** VenusREM-Harness combines protein-model scores with evolutionary and structural evidence; the v2 paper reports rank-correlation gains across 1,211 assays and 3.1 million measured variants.
- **Authors:** Yang Tan; Qijia Tian; Gangyu Sun; Bozitao Zhong; Mingchen Li; Yuanxi Yu; Nanqing Dong; Liang Hong
- **arXiv:** `2609.34654v2` (published 2026-09-28T08:58:56Z; revised 2026-11-19T12:44:46Z; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Broad retrospective variant-benchmark evaluation across ProteinGym, VenusMutHub, and the newly curated VenusViroHub; the authors report gains across 71 model configurations.
- **Claimed contribution:** The authors propose a training-free, model-agnostic retrieval-enhanced method that adaptively combines frozen protein-model scores with MSA, structural-confidence, and solvent-exposure information.
- **Caveat:** Existing assay benchmarks do not establish performance on newly generated variants or wet-lab outcomes; gains may depend on homolog coverage and benchmark composition.
- **Announcement type:** revision, 2026-11-20 batch; v2 revised 2026-11-19
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 4. [Ab-initio cryo-EM reconstruction from moments of denoised images](https://arxiv.org/abs/2611.25525)
- **Abstract:** A method-of-moments procedure reconstructs initial 3D cryo-EM models from the first three moments of denoised images, bypassing per-image orientation estimation and initializing refinement on experimental datasets.
- **Authors:** Yunpeng Shi; Amit Singer; Yuguan Wang; Andy Zhang
- **arXiv:** `2611.25525v1` (published 2026-11-19T05:26:45Z; categories: `q-bio.QM`)
- **Evidence for ranking:** Direct structural-biology method tested on experimental cryo-EM datasets, with downstream high-resolution refinement rather than only synthetic-image evaluation.
- **Claimed contribution:** The authors report an ab-initio method that avoids explicit particle-orientation estimation and does not assume a uniform orientation distribution.
- **Caveat:** The authors identify denoising-induced bias and loss of fine structure; a low-molecular-weight example fails, making denoising quality a key boundary.
- **Announcement type:** new submission, 2026-11-20
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [An Explainable and Scalable Hierarchical Tensor Framework for Integrating Multi-Omics and Digital Pathomics](https://arxiv.org/abs/2611.25584)
- **Abstract:** HIT-Fuse combines six molecular and pathology modalities across four TCGA cancer cohorts and reports survival stratification, cohort-specific classification gains, and database-based support for some decoded features.
- **Authors:** Ahmad Hussein; Ali Anaissi; Mukesh Prasad; Ali Braytee
- **arXiv:** `2611.25584v1` (published 2026-11-19T06:27:17Z; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Four cancer cohorts and cross-checks against DepMap CRISPR screens, miRTarBase, and protein annotations are reported in the paper.
- **Claimed contribution:** The authors combine hierarchical tensor fusion, missing-modality reconstruction, and traceable attributions for integrated genomics, transcriptomics, proteomics, and digital pathology.
- **Caveat:** Retrospective TCGA evaluation is not independent clinical validation; the authors note no fusion strategy dominates every endpoint, and functional associations do not prove causality.
- **Announcement type:** new submission, 2026-11-20
- **Themes:** DNA & genomics; RNA & transcriptomics; Biomedical & translational medicine

### 6. [OpenTME: An Open Dataset of AI-powered H&E Tumor Microenvironment Profiles from TCGA](https://arxiv.org/abs/2604.12075)
- **Abstract:** The v2 release describes AI-derived tumor-microenvironment profiles for 5,268 TCGA whole-slide images across ten cancer types, with more than 20,000 quantitative readouts per slide.
- **Authors:** Maaike Galama; Nina Kozar-Gillan; Christina Embacher; Todd Dembo; Cornelius Böhm; Evelyn Ramberger; Julika Ribbat-Idel; Rosemarie Krupar; Verena Aumiller; Miriam Hägele; Kai Standvoss; Gerrit Erdmann; Blanca Pablos; Ari Angelo; Simon Schallenberg; Andrew Norgan; Viktor Mátyás; Klaus-Robert Müller; Maximilian Alber; Lukas Ruff; Frederick Klauschen
- **arXiv:** `2604.12075v2` (published 2026-04-13T21:27:29Z; revised 2026-11-19T14:52:15Z; categories: `cs.CV`, `cs.AI`, `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** Large cancer resource covering ten TCGA cancer types; the revision is listed in the 20 November q-bio replacement batch.
- **Claimed contribution:** The authors release a dataset of model-generated cell-, tissue-, and spatial-neighborhood readouts from H&E whole-slide images for computational tumor-microenvironment research.
- **Caveat:** The profiles inherit errors from the underlying AI pipeline and are derived from TCGA; the release is for non-commercial academic research and does not constitute validated biomarker measurements.
- **Announcement type:** revision, 2026-11-20 batch; v2 revised 2026-11-19
- **Themes:** Biomedical & translational medicine; Omics & single-cell methods

### 7. [Morphological Features of Murine Pulmonary Arterial Networks for Diagnosing Vascular Disease](https://arxiv.org/abs/2610.40344)
- **Abstract:** Geometry, topology, and shape-analysis methods are applied to micro-CT pulmonary arterial networks from 13 mice at four pressures to compare hypoxia-induced pulmonary hypertension with control morphology.
- **Authors:** Elliot Maceda; John M Miller; Sebastian Reyes-Roza; Megan Miller; Nick A Hill; Radmila Sazdanović; Nathaniel Josephs; Mette S Olufsen
- **arXiv:** `2610.40344v2` (published 2026-10-29T16:05:08Z; revised 2026-11-18T19:18:32Z; categories: `q-bio.TO`)
- **Evidence for ranking:** Direct vascular-disease model with animal micro-CT measurements and multi-pressure assessment; the updated version appears in the 20 November replacement list.
- **Claimed contribution:** The authors report morphological differences in hypoxia-induced hypertensive mouse arterial networks and present a feature-extraction and classification pipeline.
- **Caveat:** This is a small preclinical mouse study (13 animals), not a validated human diagnostic method; reported discriminative features need independent replication.
- **Announcement type:** revision, 2026-11-20 batch; v2 revised 2026-11-18
- **Themes:** Biomedical & translational medicine; Molecular & cell biology; Quantitative methods

### 8. [First-Passage Time Fluctuation Theorem and Thermodynamic Bound in Cooperative Biomolecular Networks](https://arxiv.org/abs/2501.09087)
- **Abstract:** A theoretical analysis derives a first-passage-time fluctuation relation and thermodynamic bound for cooperative biomolecular networks, including enzyme- and motor-protein-like systems.
- **Authors:** D. Evan Piephoff; Jianshu Cao
- **arXiv:** `2501.09087v4` (published 2025-01-15T19:13:39Z; revised 2026-11-19T00:39:00Z; categories: `physics.bio-ph`, `physics.chem-ph`, `q-bio.MN`)
- **Evidence for ranking:** Direct nonequilibrium biomolecular-network relevance; a new version in the 20 November q-bio replacement batch and a DOI are listed in arXiv metadata.
- **Claimed contribution:** The authors derive a fluctuation theorem for observable first-passage times under stated hidden-current conditions and relate its correction to a bound on kinetic directionality.
- **Caveat:** The result is theoretical and conditional on model assumptions; the proposed experimental test is not itself an experimental validation in this paper.
- **Announcement type:** revision, 2026-11-20 batch; v4 revised 2026-11-19
- **Themes:** Biochemistry & proteins; Quantitative methods

### 9. [From Sequence Uncertainty to Phenotype Hypotheses: Uncertainty-Conditioned Inference over Biomedical Knowledge Graphs](https://arxiv.org/abs/2611.25422)
- **Abstract:** An uncertainty-aware graph method maps genomic-model evidence to distributions over phenotype hypotheses and evaluates association recovery on AlzKB and Hetionet without patient-level phenotype supervision.
- **Authors:** Huixin Zhan; Jason H. Moore
- **arXiv:** `2611.25422v1` (published 2026-11-19T03:02:19Z; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Direct sequence-to-phenotype application; results include two biomedical graphs and 30 gene-holdout masks against a DistMult baseline.
- **Claimed contribution:** The authors make predictive uncertainty control the breadth of graph-supported phenotype hypotheses while preserving traceable gene–disease–phenotype paths.
- **Caveat:** This is computational hypothesis generation, not patient-validated variant interpretation. The authors note the gene-holdout advantage is concentrated in three genes and is not uniform across genes.
- **Announcement type:** new submission (cross-list), 2026-11-20
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Biomedical & translational medicine

### 10. [Dynamical Variational Theory of Stochastic Reaction Networks](https://arxiv.org/abs/2611.25491)
- **Abstract:** A Plefka-expansion variational method approximates non-Markovian reaction-network means, correlations, and responses, with computational benchmarks in gene regulation, enzyme kinetics, and infection dynamics.
- **Authors:** Moshir Harsh; Peter Sollich
- **arXiv:** `2611.25491v1` (published 2026-11-19T04:26:42Z; categories: `cond-mat.stat-mech`, `q-bio.MN`, `q-bio.PE`)
- **Evidence for ranking:** Clear biochemical and gene-regulatory applications; the paper compares transient and steady-state behavior, including fluctuation-driven effects.
- **Claimed contribution:** The authors derive a tractable dynamical variational approximation with self-consistent memory and a generalized bubble resummation.
- **Caveat:** Evaluation is numerical benchmarking against selected model systems, not direct experimental validation of a biochemical mechanism.
- **Announcement type:** new submission (cross-list), 2026-11-20
- **Themes:** Biochemistry & proteins; Gene regulation & epigenetics; Quantitative methods

### 11. [GraphEP: A Calibrated Data System and Benchmark for Learning Cardiac Electrophysiology](https://arxiv.org/abs/2611.26551)
- **Abstract:** GraphEP packages 732 simulated left-ventricular electrophysiology trajectories across 20 anatomies and benchmarks graph-based predictors of transmembrane potential.
- **Authors:** Matteo Baldan; Chiara D'Ercoli; James Rowbottom; Pietro Liò; Stefania Fresca
- **arXiv:** `2611.26551v1` (published 2026-11-19T18:23:10Z; categories: `q-bio.TO`)
- **Evidence for ranking:** Reproducible simulation/data contribution with anatomy, scar, and pacing variation; the arXiv comment identifies an AIDaR 2026 NeurIPS workshop paper.
- **Claimed contribution:** The authors report that physiology-informed models lead on complementary metrics in this graph-native benchmark.
- **Caveat:** The 732 trajectories are mechanistic simulations, not prospective patient data or direct experimental validation of learned predictions.
- **Announcement type:** new submission, 2026-11-20
- **Themes:** Molecular & cell biology; Biomedical & translational medicine; Quantitative methods

### 12. [When Foundation Models Disagree: Representational Heterogeneity for Calibrated Uncertainty in Whole-Slide Image Classification](https://arxiv.org/abs/2611.26159)
- **Abstract:** CALIFUSE uses disagreement among pathology foundation-model representations to estimate confidence and reports calibration and misclassification-detection improvements across seven whole-slide classification tasks.
- **Authors:** Yekai Shen; Yuqian Wang; Zishun Liao; Rongsheng Wang; Wenting Chen; S. Kevin Zhou; Qingsong Yao
- **arXiv:** `2611.26159v1` (published 2026-11-19T14:15:07Z; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Seven pathology tasks and comparisons with single-encoder and naive-ensemble baselines; arXiv comment reports acceptance by IEEE BIBM 2026.
- **Claimed contribution:** The authors use encoder-level representation heterogeneity and slide/chunk agreement as confidence cues without training a separate fusion model.
- **Caveat:** Evidence concerns benchmark classification and calibration; it does not establish clinical deployment or improved patient outcomes.
- **Announcement type:** new submission (cross-list), 2026-11-20
- **Themes:** Biomedical & translational medicine; Bioinformatics & sequence analysis

### 13. [Transition Dynamics Matter: Hidden Markov Scoring of Epileptogenic Channels in SEEG](https://arxiv.org/abs/2611.26142)
- **Abstract:** A channel-specific hidden Markov model scores seizure-related transition changes in stereo-EEG and is evaluated against medically validated epileptogenic-zone definitions in 30 patients.
- **Authors:** Giulia Tacconi; Federico Mason; Lorenzo Ferri; Elena Pasini; Lidia Di Vito; Matteo Martinoni; Lara Alvisi; Anna Scarabello; Luca Zanuttini; Francesca Bisulli; Andrea Zanella
- **arXiv:** `2611.26142v1` (published 2026-11-19T13:58:28Z; categories: `eess.SP`, `physics.med-ph`)
- **Evidence for ranking:** Direct biomedical signal-analysis question; a 30-patient SEEG evaluation compares the method with a benchmark and clinically validated definitions.
- **Claimed contribution:** The authors report that channel-specific latent transition probabilities can improve epileptogenic-zone localization scoring relative to an observation-space baseline.
- **Caveat:** One cohort is described; external-site and prospective validation are not reported, so this is not an established clinical decision tool.
- **Announcement type:** new submission (cross-list), 2026-11-20
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 14. [Physics-Informed Deep Learning for Shear Wave Speed Estimation in MR Elastography](https://arxiv.org/abs/2611.26111)
- **Abstract:** An end-to-end reconstruction/inversion model estimates shear-wave speed from undersampled brain MRE data, reports a 30% lower NRMSE than total-variation minimization, and is also applied to in-vivo data.
- **Authors:** Stefan Martin; Jakob Schattenfroh; Patrick Schuenke; Felix Frederik Zimmermann; Ingolf Sack; Christoph Kolbitsch; Andreas Kofler
- **arXiv:** `2611.26111v1` (published 2026-11-19T13:39:46Z; categories: `eess.IV`, `cs.LG`, `physics.med-ph`)
- **Evidence for ranking:** The arXiv comment identifies an accepted IEEE Transactions on Biomedical Engineering version (DOI: `10.1109/TBME.2026.3666306`); the abstract reports retrospective undersampling tests and an in-vivo application.
- **Claimed contribution:** The authors combine neural reconstruction with phase-gradient inversion and train the pipeline end-to-end for shear-wave-speed mapping from k-space.
- **Caveat:** The paper is an accepted article version, not an independent new validation; image/model error reduction does not establish diagnostic accuracy or patient benefit.
- **Announcement type:** new submission (cross-list), 2026-11-20
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 15. [Towards consensus on practical probabilistic evaluation metrics for clinical decision making in radiotherapy](https://arxiv.org/abs/2611.25260)
- **Abstract:** The authors apply probabilistic evaluation to 60 proton-therapy plans from three Dutch centers and interview eight radiation oncologists about feasible metrics and probability levels.
- **Authors:** Jenneke I. de Jong; Steven J. M. Habraken; Erik W. Korevaar; Mirko Unipan; Esther Kneepkens; Gloria Vilches Freixas; Yvonne L. B. Klaver; Michiel Kroesen; Alejandra Méndez Romero; Edwin Oldehinkel; Stephanie Peeters; Roel J. H. M. Steenbakkers; Karolien Verhoeven; Stefan Both; Liesbeth J. Boersma; Sebastiaan Breedveld; Mischa S. Hoogeman
- **arXiv:** `2611.25260v1` (published 2026-11-18T22:44:24Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Multi-center treatment-plan analysis and structured interviews with eight radiation oncologists provide translational evidence beyond a synthetic benchmark.
- **Claimed contribution:** The authors assess probabilistic clinical-goal metrics as a potential complement to current robustness evaluation for radiotherapy planning.
- **Caveat:** The study evaluates plans and expert preferences, not prospective decision changes or patient outcomes; validation across more centers is needed.
- **Announcement type:** new submission, 2026-11-20
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

## Trending Research Themes

- Molecular computation is a clear cluster: ShEPhERD-score standardizes differentiable 3D molecular similarity, Montparnasse targets inverse RNA folding, and VenusREM-Harness scores protein variants. These are computational benchmarks against existing datasets, not evidence that new molecules or variants have been experimentally validated.
- Data-driven structural and cancer biology spans two distinct contributions: the cryo-EM paper uses image moments to seed refinement on experimental datasets, while HIT-Fuse integrates omics/pathology and OpenTME releases AI-derived tumor profiles. The cryo-EM method, integrative prediction framework, and dataset should not be treated as replications of one finding.
- Two themes in network biology are explicit: the first-passage theorem concerns nonequilibrium biomolecular machines, and the stochastic variational method models biochemical reaction dynamics. One is theoretical; the other is numerically benchmarked.
- Translational work emphasizes external validity and uncertainty: the mouse-artery, GraphEP, CALIFUSE, SEEG, MRE, and radiotherapy papers range from animal measurements and simulations to retrospective patient data and clinician interviews. They are separate modalities and do not establish a field-wide clinical shift.

## Open Problems and Research Directions

- Test molecular-design scores against blinded biochemical experiments. For ShEPhERD-score, compare DUDE-Z-style enrichment with binding/activity assays across held-out targets; for Montparnasse, test designed RNAs with structure probing or functional assays beyond the ViennaRNA/Turner scoring model. For VenusREM-Harness, prospective variant panels would show whether retrospective rank-correlation gains transfer to new protein families and assay conditions.
- Stress-test cryo-EM initialization on low-molecular-weight targets, low signal-to-noise images, and non-uniform orientation distributions. The authors identify denoising bias; comparing raw-image moment estimators, alternative denoisers, and failure rates across independent datasets would directly address it.
- Evaluate HIT-Fuse and OpenTME on independent institutions and scanners with prespecified modality-missingness patterns. Separate prediction from biological interpretation, and test whether feature attributions remain stable under cohort shift. For sequence-to-phenotype inference, expand gene- and variant-held-out tests with per-gene calibration and independent phenotype resources.
- For the mouse vascular pipeline, validate morphological features in a larger animal cohort and then in human imaging before discussing diagnostic use. For GraphEP, compare simulated predictions with measured electrophysiology. For CALIFUSE, SEEG, and MRE, report cross-site calibration and failure modes; for probabilistic radiotherapy metrics, prospectively measure decision impact and patient-relevant trade-offs.

## Takeaway

The batch is strongest in computational molecular design and structural/genomic methods, with a second cluster of imaging and clinical-physics evaluations. Experimental data and large retrospective benchmarks make some results more grounded, but simulations, model-derived measurements, and in-silico predictions still dominate. The ranking is relevance-based because arXiv provides no official trend chart and attention signals are too sparse for a popularity claim.

## Method and sources

- **Window:** daily; announcement batch 2026-11-20 (Friday). The current date, 2026-11-21, is Saturday and the latest batch remains 20 November. Exact start and end dates: 2026-11-20 through 2026-11-20. Snapshot: 2026-11-21T17:19:02Z.
- **Candidate collection:** traversed the 20 November q-bio new, cross-submission, and replacement listings (35 entries) and physics.med-ph listings (5 entries); the two sets had no duplicate IDs. The full Computer Science new/cross/replacement listing was checked for `cs.BI` subject entries; none appeared. The candidate query was `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`. API pages at offsets 0 and 200 were checked, extending through 2026-10-21; listings additionally identify revisions that submitted-date sorting alone would miss. Versionless arXiv IDs were deduplicated. Fifteen of the 40 q-bio/medical-physics listing records were selected for direct biological or biomedical relevance.
- **Ranking:** Semantic Scholar Graph records and citation totals were checked where available. Citation evidence was sparse (the resolvable recent records had zero to very few citations), so no citation-velocity or popularity ranking is claimed; papers are ordered by subfield fit, reported empirical or computational evaluation, and relevance of recent revisions. Citation counts are point-in-time totals, not gains during the window. Independent discussion was not used as a popularity proxy.
- **Reading and evidence boundary:** all 15 selected abstract pages and version/category metadata were verified; the introduction, results, and limitations for the top three were read in arXiv full-text HTML. Claims are attributed to the authors. Computational prediction, simulation, animal data, retrospective patient cohorts, and clinical-outcome evidence are distinguished; no patient-specific advice is offered.
- **Coverage caveat:** arXiv is not a representative biomedical preprint index; many experimental and clinical preprints appear on bioRxiv or medRxiv. This report does not cover those repositories or the medical literature as a whole.
- **Sources:** [q-bio daily listings](https://arxiv.org/list/q-bio/new), [physics.med-ph daily listings](https://arxiv.org/list/physics.med-ph/new), [Computer Science daily listings](https://arxiv.org/list/cs/new), and the configured query above. Each paper links to its arXiv abstract; arXiv comments and DOI details are cited in the relevant entry. Retrieved corroboration also includes the Semantic Scholar Graph API for indexed paper metadata.
