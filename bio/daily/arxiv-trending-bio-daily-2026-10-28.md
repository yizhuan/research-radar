# arXiv Biology & Biomedicine — Daily, 2026-10-28

## Headline
The latest announcement batch available at 2026-10-29 01:24 UTC is Wednesday, 28 October 2026; there is no 29 October batch yet. Seven notable papers made the molecular-biology/biomedicine shortlist from 30 deduplicated IDs in the configured category listings. Protein–glycan structure prediction, biomolecular simulation, RNA ensemble data, and genomics tools set the agenda. arXiv has no official trending chart, so this is an inferred relevance ranking, not a measured popularity list; arXiv's biomedical coverage is incomplete and misses much work on bioRxiv, medRxiv, and elsewhere.

## Notable recent papers

### 1. [Accurate structural modelling of protein-glycan recognition with GlycoWeave](https://arxiv.org/abs/2610.37410)
- **Abstract:** GlycoWeave uses chemically constrained diffusion and multiscale molecular representations to predict protein-bound glycan conformations, reporting a 71.9% Top-25 high-quality success rate on 698 complexes versus 19.2% for AlphaFold 3.
- **Authors:** Huifeng Zhao, Jintu Zhang, Yifei Xiao, Youqiao Qian, Silong Zhai, Zichang Jin, Li Wang, Yuchao Wang, Hang Dong, Yifan Zhao, Zhenxing Wu, Hongyan Du, Yuansheng Huang, Bowei Zhao, Xiaorui Wang, Shukai Gu, Jike Wang, Zhongjun Li, Zhongtang Li, Tingjun Hou, Yu Kang
- **arXiv:** `2610.37410v1` (published 2026-10-27 15:27:09 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct fit to biomolecular structure research; the authors report a 698-complex benchmark and an explicit AlphaFold 3 comparison. These are relevance/evaluation signals, not readership measures.
- **Claimed contribution:** The authors say internal-coordinate diffusion preserves glycan connectivity and stereochemistry while combining atom- and monosaccharide-level context; they report 0.34 seconds per sampled pose.
- **Caveat:** This is structure-prediction benchmarking, not prospective binding or biochemical validation; training supervision also includes computationally refined structures.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [A unified coarse-grained neural network potential for the dynamics of biomolecular complexes](https://arxiv.org/abs/2610.37606)
- **Abstract:** AMARO v2.0 is a heavy-atom coarse-grained neural potential for proteins, drug-like molecules, and their complexes, evaluated across 262 complexes and selected binding case studies.
- **Authors:** Antonio Mirarchi, Stephen E. Farr, Adrià Peréz, Gianni De Fabritiis
- **arXiv:** `2610.37606v1` (published 2026-10-27 17:37:10 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct biomolecular-dynamics relevance; reported tests span 262 complexes across 11 targets, with targeted comparisons to all-atom molecular mechanics.
- **Claimed contribution:** Authors report that the model distinguishes trypsin–benzamidine protonation states and reaches its crystal pose in 3.3 times as many trajectories as the tested all-atom baseline at a fixed estimated GPU-time budget.
- **Caveat:** Authors report an over-favorable free-energy estimate versus experiment, HIF2A interface reorientation, and remaining pose-recovery/site-specificity problems for SHP2 and CDK8. This is simulation evidence, not experimental drug validation.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [mdRNAcat: A Molecular Dynamics RNA Catalog of REST2 Conformational Ensembles](https://arxiv.org/abs/2610.35204)
- **Abstract:** mdRNAcat releases standardized coordinates, forces, annotations, and replica-exchange metadata from enhanced-sampling molecular-dynamics simulations of 48 RNA systems.
- **Authors:** Anton E. Dorn, Emile de Bruyn, Fabrice von der Lehr, Philipp Knechtges, Stefan Kesselheim, Alexander Schug
- **arXiv:** `2610.35204v2` (published 2026-10-26 10:56:24 UTC; latest revision 2026-10-27 10:19:38 UTC; categories: `q-bio.BM`, `cs.LG`, `physics.bio-ph`)
- **Evidence for ranking:** Direct RNA focus; the v2 revision was announced in this batch, and the paper supplies 48 systems across three relevant categories with 32 REST2 states per system.
- **Claimed contribution:** Authors present mdRNAcat as a homogeneous resource for learning RNA molecular models, reporting 316.8 μs total sampled time and standardized HDF5 data with coordinates and force signals.
- **Caveat:** These are simulations under a fixed protocol, not experimental measurements of native ensembles; the 48 systems are drawn from structurally available RNAs, and the dataset is large (699 GB).
- **Announcement type:** revision, 2026-10-28
- **Themes:** RNA & transcriptomics; Molecular & cell biology; Quantitative methods

### 4. [HELICS: Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching](https://arxiv.org/abs/2610.36361)
- **Abstract:** HELICS generates conditional synthetic common-variant genomes using latent flow matching trained on more than 417,000 UK Biobank genomes, with reported external allele-frequency and SNP-correlation fidelity.
- **Authors:** Ahmad Abdel-Azim, Xihong Lin
- **arXiv:** `2610.36361v1` (published 2026-10-26 22:25:36 UTC; categories: `q-bio.GN`, `cs.LG`)
- **Evidence for ranking:** Large-scale genomic modeling, a direct genomics category, and an external fidelity evaluation; the arXiv comment names NeurIPS 2026 but does not itself state acceptance.
- **Claimed contribution:** Authors report phasing-free generation across hundreds of thousands of common SNPs and conditional dosage shifts correlated with published association weights.
- **Caveat:** Genotype fidelity does not establish privacy protection or downstream research utility; the abstract emphasizes common variants and does not establish rare-variant or clinical validity.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 5. [Enhancing Clinical Classifier Robustness with Deep Representation Learning Based OOD Detection on DNA Methylation Data](https://arxiv.org/abs/2610.36344)
- **Abstract:** The authors test out-of-distribution detection for DNA-methylation tumor classifiers using public sarcoma and brain-tumor cohorts plus an independent clinical dataset.
- **Authors:** Md Zahangir Alom, Quynh T. Tran, Breuer Alexandar, Brent A. Orr
- **arXiv:** `2610.36344v1` (published 2026-10-26 22:11:07 UTC; categories: `q-bio.GN`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Direct genomic quality-control application, comparison of five OOD methods, and an independent clinical test set reported by the authors.
- **Claimed contribution:** The authors report 1D-SSA as their strongest evaluated method and a mean AUROC of 0.976 on the independent clinical test set.
- **Caveat:** The abstract does not give that test set's size or composition; this is retrospective classifier quality-control research, not prospective diagnostic-outcome evidence.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** DNA & genomics; Biomedical & translational medicine; Bioinformatics & sequence analysis

### 6. [ACOR: incremental evidence accumulation towards real-time DNA storage reconstruction](https://arxiv.org/abs/2610.36500)
- **Abstract:** ACOR incrementally reconstructs DNA-storage sequences from streaming reads, with tests on simulated/public data and the authors' short-read wet-lab library.
- **Authors:** Linxuan Han, Huaming Wu, Shi Jia, Guanjin Qu
- **arXiv:** `2610.36500v1` (published 2026-10-27 01:58:03 UTC; categories: `cs.IR`, `q-bio.GN`)
- **Evidence for ranking:** Direct DNA-sequencing application and a reported wet-lab-library evaluation covering more than ten million reads.
- **Claimed contribution:** Authors report near-complete recovery with second-scale reconstruction on their library and parallel speedups from tens to over a thousand-fold against the tested serial configurations.
- **Caveat:** Evidence concerns DNA data-storage reconstruction on the tested library and baselines; it does not establish an end-to-end production sequencing deployment or biomedical application.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 7. [pyTransRate: 1 reference-free quality assessment of de novo transcriptome assemblies with current aligners and quantifiers](https://arxiv.org/abs/2610.37031)
- **Abstract:** pyTransRate reimplements reference-free transcriptome-assembly quality scoring in Python and compares it with the original implementation across 129 public assemblies.
- **Authors:** Matthew MacManes
- **arXiv:** `2610.37031v1` (published 2026-10-27 11:08:52 UTC; categories: `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Useful genomics workflow contribution, with 5,031 paired metric comparisons and reported rank correlations against the legacy software.
- **Claimed contribution:** The author reports exact reproduction of sequence metrics and read counts, while modernizing the aligner/quantifier dependencies and supporting compressed inputs.
- **Caveat:** The author explicitly warns that updated read-based scores are not numerically interchangeable with the legacy release; assembly quality scores are not ground-truth measures of transcriptome completeness or biological function.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis

## Trending Research Themes

Two papers in this shortlist expand computational modeling of molecular structure and dynamics: GlycoWeave focuses on glycan stereochemistry and recognition, while AMARO targets chemically diverse protein–ligand complexes. This is a small batch-level cluster, not evidence of a field-wide shift. A second thread is making sequence data more usable: mdRNAcat standardizes simulated RNA ensembles, HELICS generates cohort-scale genotype data, ACOR processes DNA-storage reads, and pyTransRate updates transcriptome-assembly assessment. The methylation OOD paper adds a separate, translationally motivated robustness check for genomic classifiers. These are related method-development efforts, not independent validations of one another.

## Open Problems and Research Directions

The selected papers support several concrete next tests. For GlycoWeave, evaluate structurally withheld, chemically diverse glycan complexes and compare predicted poses with biochemical binding or structural measurements. For AMARO, calibrate predicted free energies against a larger independent affinity panel and probe off-site binding across additional targets. For mdRNAcat, train RNA models with held-out sequence families and compare their ensembles with experimental structural restraints and alternative simulation protocols. For HELICS, test rare variants, ancestry-diverse external cohorts, privacy attacks, and downstream association bias before treating synthetic cohorts as substitutes for restricted data. For methylation OOD detection, report cohort sizes and composition and assess performance prospectively across additional tumor classes. These are research proposals grounded in the reported methods and evidence boundaries, not clinical advice.

## Takeaway
This batch is best read as a set of modeling and data-infrastructure advances, not new clinical evidence. GlycoWeave and AMARO bring richer chemistry to molecular modeling; mdRNAcat contributes simulation data for RNA; HELICS, methylation OOD, ACOR, and pyTransRate target different genomic-data bottlenecks. Independent validation and out-of-distribution tests will matter more than the headline benchmark numbers. The ordering reflects relevance within this batch, not measured popularity.

## Method and sources
- **Window:** daily batch, 2026-10-28 through 2026-10-28. At the 2026-10-29 snapshot there was no later 29 October batch, so the latest batch (28 October) was used.
- **Snapshot:** 2026-10-29T01:24:05Z.
- **Listings checked:** full `new` listings for [q-bio.BM](https://arxiv.org/list/q-bio.BM/new), [q-bio.GN](https://arxiv.org/list/q-bio.GN/new), [q-bio.MN](https://arxiv.org/list/q-bio.MN/new), [q-bio.SC](https://arxiv.org/list/q-bio.SC/new), [q-bio.CB](https://arxiv.org/list/q-bio.CB/new), [q-bio.TO](https://arxiv.org/list/q-bio.TO/new), [q-bio.QM](https://arxiv.org/list/q-bio.QM/new), and [physics.med-ph](https://arxiv.org/list/physics.med-ph/new). These contained 33 category entries, deduplicated to 30 versionless arXiv IDs. The configured `cs.BI` API query returned no results and its listing endpoint was unavailable; verified cross-lists in current categories such as `cs.LG`, `cs.AI`, and `cs.IR` were retained from the arXiv abstract pages.
- **Candidate query:** [arXiv API query across the configured categories](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200). The newest 200 results already extended back to 9 October, past the selected daily window; daily listings were used to identify batch announcements and revisions.
- **Ranking:** arXiv has no official trend/readership ranking. Attention evidence for this fresh batch was not sufficient to claim a popularity ranking, so the list is titled **Notable recent papers** and ordered by direct molecular/biomedical relevance, cross-list breadth, substantive revision where applicable, and the reported evaluation setting. No numeric trend score is used. A Semantic Scholar Graph API request was rate-limited; no citation or influential-citation totals are claimed or used. Exact-title web searches mainly surfaced the arXiv records and summaries rather than independent technical discussion.
- **Sources:** each paper links to its verified arXiv abstract page. Full text was reviewed for the top three (GlycoWeave PDF, AMARO HTML/PDF, and mdRNAcat v2 PDF), including introduction, results, and conclusions or evidence boundaries. This is not a systematic review and does not cover bioRxiv, medRxiv, or biomedical research as a whole.
