# arXiv Biology & Biomedicine — 28 October 2026 announcement batch

Thirty unique arXiv IDs appeared across the configured category listings for the latest batch; twelve are highlighted below. Protein–glycan modelling, biomolecular simulation, RNA data resources and genomics methods form the strongest biology-centered threads. The agenda is to separate computational promise from experimental and clinical evidence. arXiv has no official trending chart, and its coverage of biomedical research is incomplete (much clinical and experimental work appears on bioRxiv or medRxiv); this is an inferred relevance ranking from one batch, not a readership or download ranking. Snapshot: 29 October 2026, 17:32:17 UTC. The current day’s batch had not yet been announced, so this report uses the prior batch dated 28 October.

## Notable recent papers (ranked)

### 1. [Accurate structural modelling of protein-glycan recognition with GlycoWeave](https://arxiv.org/abs/2610.37410)
- **Abstract:** GlycoWeave uses chemically constrained diffusion and multiscale representations to predict protein–glycan complex structures.
- **Authors:** Huifeng Zhao; Jintu Zhang; Yifei Xiao; Youqiao Qian; Silong Zhai; Zichang Jin; Li Wang; Yuchao Wang; Hang Dong; Yifan Zhao; Zhenxing Wu; Hongyan Du; Yuansheng Huang; Bowei Zhao; Xiaorui Wang; Shukai Gu; Jike Wang; Zhongjun Li; Zhongtang Li; Tingjun Hou; Yu Kang
- **arXiv:** `2610.37410v1` (published 2026-10-27 15:27:09 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** The authors benchmarked 698 protein–glycan complexes and report a 71.9% Top-25 high-quality success rate versus 19.2% for AlphaFold 3; this is a structural-prediction benchmark, not an experimental binding assay.
- **Claimed contribution:** The preprint reports that carbohydrate-specific constraints improve structural and chemical validity while sampling at 0.34 seconds per pose.
- **Caveat:** These are in-silico structural comparisons; they do not establish binding affinity, biological function, or clinical utility.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [A unified coarse-grained neural network potential for the dynamics of biomolecular complexes](https://arxiv.org/abs/2610.37606)
- **Abstract:** AMARO v2.0 is a shared heavy-atom coarse-grained neural potential for protein, ligand and ternary biomolecular-complex dynamics.
- **Authors:** Antonio Mirarchi; Stephen E. Farr; Adrià Peréz; Gianni De Fabritiis
- **arXiv:** `2610.37606v1` (published 2026-10-27 17:37:10 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** The authors report tests across 262 complexes and 11 targets; in a trypsin–benzamidine case study it reached the crystal pose in 3.3 times as many trajectories as all-atom molecular mechanics at a fixed estimated GPU-time budget.
- **Claimed contribution:** The preprint proposes one heavy-atom representation, with hydrogenation and charge conditioning, across proteins, drug-like molecules and their complexes.
- **Caveat:** This is simulation evidence. The reported free-energy estimates are more favorable than experimental references, and the paper notes failures in binding-pose recovery or site specificity for SHP2 and CDK8 and reorientation in the HIF2A complex.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [mdRNAcat: A Molecular Dynamics RNA Catalog of REST2 Conformational Ensembles](https://arxiv.org/abs/2610.35204)
- **Abstract:** mdRNAcat provides standardized coordinates, forces, structural annotations and replica-exchange metadata from enhanced-sampling simulations of 48 RNA systems.
- **Authors:** Anton E. Dorn; Emile de Bruyn; Fabrice von der Lehr; Philipp Knechtges; Stefan Kesselheim; Alexander Schug
- **arXiv:** `2610.35204v2` (published 2026-10-26 10:56:24 UTC; revised 2026-10-27 10:19:38 UTC; categories: `q-bio.BM`, `cs.LG`, `physics.bio-ph`)
- **Evidence for ranking:** The v2 revision was announced in this batch; the dataset spans 48 systems, 32 REST2 states per system and 316.8 μs total simulation time.
- **Claimed contribution:** The authors present a homogeneous HDF5 resource with coordinates, instantaneous forces and reference-Hamiltonian forces for developing data-driven RNA models.
- **Caveat:** The trajectories are simulations under a shared protocol, not experimental native ensembles; elevated-temperature samples require care in thermodynamic interpretation, and the dataset is about 699 GB.
- **Announcement type:** revision, 2026-10-28
- **Themes:** RNA & transcriptomics; Molecular & cell biology; Quantitative methods

### 4. [Structure, Not Sequence: Tracking and Validating Folding Mechanisms in ESMFold's Trunk with Sparse Autoencoders](https://arxiv.org/abs/2610.36226)
- **Abstract:** Sparse autoencoders and attribution are used to interpret how ESMFold’s internal representations build predicted protein geometry.
- **Authors:** Bohan Liu; Xiaohan Fan; Wenqian Ye; Aidong Zhang
- **arXiv:** `2610.36226v1` (published 2026-10-26 20:04:57 UTC; categories: `q-bio.QM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The authors trace learned features across model blocks to folding outputs and report that concept activations forecast the model’s own fold quality.
- **Claimed contribution:** The preprint proposes a sparse, interpretable account of the ESMFold trunk’s single- and pair-representation computations.
- **Caveat:** Interpretations and quality predictions are analyses of the model’s internal behavior; they are not experimental validation of biological mechanisms.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [HELICS: Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching](https://arxiv.org/abs/2610.36361)
- **Abstract:** HELICS learns conditional generation of genome-wide common-variant genotypes from biobank-scale data using latent flow matching.
- **Authors:** Ahmad Abdel-Azim; Xihong Lin
- **arXiv:** `2610.36361v1` (published 2026-10-26 22:25:36 UTC; categories: `q-bio.GN`, `cs.LG`)
- **Evidence for ranking:** The authors trained on more than 417,000 UK Biobank genomes and report external genotype-fidelity checks, including allele-frequency agreement and preservation of local and long-range SNP correlations.
- **Claimed contribution:** The preprint reports phasing-free synthesis across more than 600,000 SNPs, with conditioning on ancestry and genetic-liability summaries.
- **Caveat:** Synthetic-data fidelity is not a formal privacy guarantee or proof of downstream disease-prediction utility; liability-conditioning analyses do not constitute clinical evidence.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

### 6. [ACOR: incremental evidence accumulation towards real-time DNA storage reconstruction](https://arxiv.org/abs/2610.36500)
- **Abstract:** ACOR incrementally accumulates k-mer evidence and reconstructs consensus sequences as assigned DNA-storage reads arrive.
- **Authors:** Linxuan Han; Huaming Wu; Shi Jia; Guanjin Qu
- **arXiv:** `2610.36500v1` (published 2026-10-27 01:58:03 UTC; categories: `cs.IR`, `q-bio.GN`)
- **Evidence for ranking:** On the authors’ wet-lab NGS library (96,055 designs; about 17.7 million assigned read observations), the k=15 configuration reported 99.9844% exact recovery and a 20.5-second run in the full-library comparison; tests also covered public and simulated data.
- **Claimed contribution:** The preprint presents a streaming consensus method intended to overlap sequence reconstruction with ongoing DNA-storage readout.
- **Caveat:** It reconstructs already assigned read clusters, not the full end-to-end sequencing, clustering and decoding pipeline; timing depends on the tested hardware and configuration.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 7. [Enhancing Clinical Classifier Robustness with Deep Representation Learning Based OOD Detection on DNA Methylation Data](https://arxiv.org/abs/2610.36344)
- **Abstract:** The authors evaluate out-of-distribution detection for DNA-methylation tumor classifiers across sarcoma and brain-tumor data.
- **Authors:** Md Zahangir Alom; Quynh T. Tran; Breuer Alexandar; Brent A. Orr
- **arXiv:** `2610.36344v1` (published 2026-10-26 22:11:07 UTC; categories: `q-bio.GN`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Reported validation includes cross-validation, held-out samples and an independent clinical dataset; the paper reports mean AUROC 0.976 and TNR 0.935 on that independent test set.
- **Claimed contribution:** The preprint proposes an OOD quality-control layer to flag methylation-array samples outside a classifier’s training distribution.
- **Caveat:** This is retrospective model evaluation, not prospective diagnostic validation or evidence that the layer improves patient outcomes; the abstract does not state the independent test-set size.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** DNA & genomics; Biomedical & translational medicine

### 8. [HGPRGDel: GPR-Aware Learning and Ranking for Growth-Coupled Gene Deletion Design](https://arxiv.org/abs/2610.37478)
- **Abstract:** HGPRGDel ranks candidate gene deletions for microbial growth-coupled production while representing gene–protein–reaction logic.
- **Authors:** Ziwei Yang; Takeyuki Tamura
- **arXiv:** `2610.37478v1` (published 2026-10-27 16:07:02 UTC; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** Across e_coli_core, iMM904 and iML1515 models, the authors report the best macro-F1 and AUC among evaluated learning configurations and recovery of an average 90% of reference deletion genes while examining fewer candidates.
- **Claimed contribution:** The preprint separates learned intervention prioritization from downstream constraint-based assessment to reduce the search space for strain design.
- **Caveat:** Results are computational against curated/reference designs; the abstract reports no engineered-strain experiments or metabolite-production measurements.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biochemistry & proteins; Quantitative methods

### 9. [pyTransRate: 1 reference-free quality assessment of de novo transcriptome assemblies with current aligners and quantifiers](https://arxiv.org/abs/2610.37031)
- **Abstract:** pyTransRate reimplements reference-free transcriptome-assembly scoring with current alignment and quantification software.
- **Authors:** Matthew MacManes
- **arXiv:** `2610.37031v1` (published 2026-10-27 11:08:52 UTC; categories: `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** In 5,031 paired metric comparisons across 129 public assemblies, the author reports Spearman correlations of 0.94 for assembly score and 0.98 for good-mapping rate against TransRate 1.0.3.
- **Claimed contribution:** The preprint makes the assessment workflow usable with maintained dependencies and compressed inputs.
- **Caveat:** Read-based scores are not numerically interchangeable with the older implementation, and agreement with that tool is not an independent measure of assembly truth.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis

### 10. [OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents](https://arxiv.org/abs/2610.37081)
- **Abstract:** OpenGray tests whether radiotherapy-planning agents correctly submit, revise or escalate plans when dose goals are contradictory or feasible.
- **Authors:** Humza Nusrat; Kundan Thind
- **arXiv:** `2610.37081v1` (published 2026-10-27 11:42:47 UTC; categories: `cs.AI`, `physics.med-ph`)
- **Evidence for ranking:** Four systems were evaluated on 30 patients with contradiction and feasible-control tasks, alongside analysis of logs from 39 stereotactic radiosurgery runs; the benchmark exposes errors hidden by aggregate dose scores.
- **Claimed contribution:** The authors argue that planning-agent evaluation should score decision correctness and escalation behavior, not dose quality alone.
- **Caveat:** This is a small benchmark and retrospective log analysis; it does not show that an agent is safe or effective in clinical practice.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 11. [Retrospective macromolecular pool fraction mapping from conventional clinical MRI: a physics-guided self-supervised deep learning framework](https://arxiv.org/abs/2610.37213)
- **Abstract:** The authors estimate the myelin-sensitive macromolecular pool fraction from conventional brain MRI using a physics-guided self-supervised model.
- **Authors:** Jelmer van Lune; Miha Fuderer; Oscar van der Heide; Matteo Maspero; Martin B. Schilder; Jan Willem Dankbaar; Stefano Mandija; Alessandro Sbrizzi
- **arXiv:** `2610.37213v1` (published 2026-10-27 13:27:34 UTC; categories: `physics.med-ph`, `cs.CV`, `cs.LG`)
- **Evidence for ranking:** The multisite, multivendor study included 7,705 MRI sessions and 1,237 test sessions; in 70 sessions with demyelinating-disease labels, authors report MPF 35.6% lower in lesions than in normal-appearing white matter.
- **Claimed contribution:** The preprint proposes retrospective MPF mapping from T1-, T2- and FLAIR-weighted scans without paired quantitative-reference scans.
- **Caveat:** The lesion contrast is an association in a retrospective dataset, not a validated diagnostic test or clinical outcome; the labelled lesion subset is 70 sessions.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 12. [Optimization of 99mTc proton-induced production by means of cross-section measurements of technetium radioisotopes from molybdenum targets](https://arxiv.org/abs/2610.36949)
- **Abstract:** The authors measure proton-induced technetium-isotope production cross-sections from molybdenum targets to optimize a cyclotron route to 99mTc.
- **Authors:** Gaia Dellepiane; Sofia D'Uva; Lars Eggimann; Alexander Gottstein; Samuel Juillerat; Eva Kasanda; Isidre Mateu; Paola Scampoli; Ihor Kadenko; Saverio Braccini
- **arXiv:** `2610.36949v1` (published 2026-10-27 10:10:48 UTC; categories: `nucl-ex`, `physics.med-ph`)
- **Evidence for ranking:** The paper reports measured cross-sections and production tests; a roughly 16 MeV proton beam and 0.5 mm highly enriched 100Mo target yield a calculated 1.7 GBq/μA for a 10-hour irradiation while meeting stated radionuclidic-purity limits.
- **Claimed contribution:** The authors report experimental support for an accelerator-based 99mTc production route using medical cyclotrons.
- **Caveat:** The stated activity is a calculated yield from measured data and production tests, not evidence of routine commercial-scale supply or clinical outcomes.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

## Trending Research Themes

- **Chemistry-aware molecular modelling:** GlycoWeave targets glycan stereochemistry and recognition, while AMARO v2.0 models protein–ligand dynamics; ESMFold interpretability asks what protein-folding models represent. These papers are computational, with distinct methods and no shared experimental validation.
- **RNA structure and data resources:** mdRNAcat contributes simulated RNA ensembles and physical training signals. It is a revision; the resource’s value depends on subsequent model tests and comparisons with experimental restraints.
- **Genomic data methods:** HELICS synthesizes genome-wide common-variant data, the methylation OOD paper flags out-of-distribution tumor samples, and ACOR processes noisy DNA-storage reads. These are distinct tasks, not a single validated clinical pipeline.
- **Evidence and deployment boundaries in biomedicine:** HGPRGDel and pyTransRate are computational tools; OpenGray and MPF use clinical datasets; the 99mTc work reports experimental production measurements. Their evidence types differ and none alone establishes clinical benefit.

## Open Problems and Research Directions

- **Move molecular predictions toward orthogonal validation.** For GlycoWeave, test held-out protein–glycan complexes with blinded structural comparisons and biochemical binding assays; for AMARO, quantify pose recovery and free-energy estimates on independent targets with measured affinities, especially where the preprint reports off-site binding or energetic bias. For ESMFold interpretability, test whether identified features remain stable across model checkpoints and predict experimentally characterized folding errors.
- **Test RNA model utility against experiment.** For mdRNAcat, train with held-out sequence families and compare predicted ensembles with experimental structural restraints and alternative simulation protocols; report how elevated-temperature samples are reweighted for the intended task.
- **Test synthetic-genome utility and privacy separately.** For HELICS, evaluate rare variants and underrepresented ancestries in an independent biobank, test downstream association/risk analyses, and conduct formal membership-inference and attribute-inference audits rather than assuming synthesis is privacy-preserving.
- **Evaluate DNA-storage reconstruction end to end.** For ACOR, include noisy sequencing, clustering/assignment, deduplication and final decode in one controlled benchmark; report results across library sizes, sequencing platforms and independent wet-lab runs.
- **Establish external clinical robustness.** For methylation OOD and MPF mapping, report full cohort composition and sample counts, then test prospectively across institutions, scanners and disease subtypes against prespecified reference labels. For OpenGray, enlarge the contradiction/control benchmark and test escalation policies with clinicians before any workflow claim.
- **Close the model-to-experiment loop in metabolic engineering.** For HGPRGDel, build a blinded set of predicted deletion strategies and measure growth and target-metabolite output in engineered strains, comparing against constraint-based and non-GPR-aware baselines.

## Takeaway

This batch is strongest in computational molecular structure, RNA simulation resources and genomics methods, with several biomedical studies anchored by clinical-image datasets or measured production cross-sections. The reported validation is promising but uneven; no paper in this snapshot supports a practice-changing clinical claim, and the evidence does not justify calling the batch “trending” by readership.

## Method and sources

- **Window:** daily announcement batch dated 2026-10-28 (range 2026-10-28 through 2026-10-28); snapshot 2026-10-29 17:32:17 UTC. The latest batch available then was the prior day’s batch. The [arXiv schedule](https://arxiv.org/localtime) showed the next submission deadline at 18:00 UTC on 29 October and the next announcement no earlier than 00:00 UTC on 30 October.
- **Candidate pool:** the current `new` listings across the configured categories contained 33 category entries, deduplicated to 30 versionless arXiv IDs, including new submissions, cross-lists and replacement submissions. The configured `cs.BI` listing route returned an invalid-category page at snapshot, so that category-specific page could not be independently traversed. The broad query still included the configured category term.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submission date and paginated past the selected window. Cross-list duplicates were deduplicated by versionless arXiv ID; latest versions were used while retaining original submission dates.
- **Ranking:** attention evidence was too sparse for a measured popularity ranking, so entries are labeled notable recent papers and ordered by biological/biomedical relevance, cross-list breadth and reported validation setting. Semantic Scholar Graph returned zero citation and zero influential-citation counts for selected records it indexed; these are current totals, not gains during this window, and did not provide a useful popularity ordering. No downloads or views are inferred.
- **Evidence review:** all twelve selected arXiv abstract pages were checked. Introduction, results and conclusion/limitations material was reviewed for the first three papers where PDF extraction was practical. Experimental, computational and retrospective clinical evidence are distinguished in each entry.
- **Sources:** [arXiv local announcement schedule](https://arxiv.org/localtime); [q-bio.BM new](https://arxiv.org/list/q-bio.BM/new); [q-bio.GN new](https://arxiv.org/list/q-bio.GN/new); [q-bio.MN new](https://arxiv.org/list/q-bio.MN/new); [q-bio.SC new](https://arxiv.org/list/q-bio.SC/new); [q-bio.CB new](https://arxiv.org/list/q-bio.CB/new); [q-bio.TO new](https://arxiv.org/list/q-bio.TO/new); [q-bio.QM new](https://arxiv.org/list/q-bio.QM/new); [physics.med-ph new](https://arxiv.org/list/physics.med-ph/new). Paper-specific sources are linked in each title.
