# Daily arXiv Biology & Biomedicine — 11 November 2026

## Headline

Wednesday 11 November announcement batch: 14 selected papers. The leading pattern is computational molecular discovery—from protein-interaction prediction and mutation-guided protein engineering to pose ranking and virtual screening—with a second cluster in genomic inference and biomedical imaging. This is a relevance-ranked “Notable recent papers” report, not a measured popularity chart: arXiv has no official trending ranking, and its biomedical coverage is incomplete; much clinical and experimental biology appears on bioRxiv, medRxiv, and elsewhere. Snapshot: 2026-11-11 17:15:30 UTC.

## Top papers (ranked)

### 1. [Emergent Biological Capabilities in a Foundation Model for Molecular Interactions](https://arxiv.org/abs/2611.14504)
- **Abstract:** Bonbon predicts protein–ligand interaction properties from sequences; the author reports prospective dose-response hits across nine disease targets.
- **Authors:** Adi Mashiach
- **arXiv:** `2611.14504v1` (published 2026-11-10 18:53:01 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Reported prospective assays across nine targets and seven protein families, with a 61.5% dose-response hit rate; arXiv records NeurIPS 2026 Main Track Oral acceptance and the conference lists the oral. These are relevance/evaluation signals, not popularity counts.
- **Claimed contribution:** The author reports sequence-only, zero-shot interaction capabilities and novel inhibitors; up to 24 generated compounds per target were synthesized and assayed.
- **Caveat:** This is one developer-reported study, not independent replication. The paper says its interaction distinctions remain coarse and that the model does not predict organismal toxicity. Biochemical activity is not clinical efficacy.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 2. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](https://arxiv.org/abs/2611.13348)
- **Abstract:** ProTEUS combines sequence, evolutionary, and structural context with experimental feedback to rank protein variants and guide iterative engineering.
- **Authors:** Yikun Zhang, Minghao Guo, Guangxue Xu, Peter Yichen Chen, Wojciech Matusik, Wengong Jin, Jingjing Chai, Kaiyi Jiang
- **arXiv:** `2611.13348v1` (published 2026-11-09 23:19:33 UTC; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** Pretrained on 182 deep-mutational-scanning assays spanning 161 protein backgrounds; authors report two closed-loop engineering campaigns with activity gains exceeding 10-fold over wild type.
- **Claimed contribution:** A mutation-aware multimodal representation and fast physics-constrained structure predictor connect predicted mutation effects to experimental feedback in aldehyde dehydrogenase and levansucrase.
- **Caveat:** Experimental demonstrations cover two enzymes and are preliminary; broader transfer depends on assay quality and activity data, which the authors identify as noisy and limited. The abstract does not establish general performance across protein classes.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 3. [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511)
- **Abstract:** Pyrite benchmarks LLM agents that rank predicted protein–ligand poses; an LLM-guided feature-engineering approach reaches up to 74% accuracy.
- **Authors:** Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver
- **arXiv:** `2611.14511v1` (published 2026-11-10 18:56:32 UTC; categories: `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** A 1,500-pair benchmark across 285 structures; NeurIPS 2026 Agentic AI for Biological Discovery Workshop listing; independent coverage of the work.
- **Claimed contribution:** Authors report 67% peak accuracy for direct pose reasoning and 74% for LLM-generated features plus logistic regression, exceeding expert performance on their benchmark.
- **Caveat:** The benchmark uses poses from a proprietary cofolding model. Transfer to other pose generators and full screening pipelines remains untested; pair-ranking accuracy is not experimental binding validation.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 4. [ANTIOCH-VS: From Sequence to Hits with Modular, Open-Source Ensemble Virtual Screening](https://arxiv.org/abs/2611.14287)
- **Abstract:** ANTIOCH-VS links predicted protein ensembles, docking, and metadynamics to prioritize binders, reporting retrospective enrichment on two targets.
- **Authors:** Hale S. Hasdemir, Venkata Sai Sreyas Adury, Pratyush Tiwary
- **arXiv:** `2611.14287v1` (published 2026-11-10 16:27:14 UTC; categories: `physics.chem-ph`, `q-bio.BM`)
- **Evidence for ranking:** DUD-E benchmarks for JAK2 and ADRB2 report top-20 hit rates of 20% and 60%, respectively, against roughly 1–2% random expectation; code is public.
- **Claimed contribution:** The authors present an end-to-end, modular sequence-to-shortlist screening workflow using conformational ensembles.
- **Caveat:** Both campaigns are retrospective and limited to two targets; the authors identify prospective screens as the decisive test. Metadynamics triage was shown only on the soluble kinase.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [EvoSurv: Evolution-Aware Multimodal Survival Modeling Reveals Complementary Prognostic Signals](https://arxiv.org/abs/2611.13190)
- **Abstract:** EvoSurv adds genomic-evolution features to clinical and RNA data for cancer survival prediction across six TCGA cohorts.
- **Authors:** Wei Wang, Po-Yu Liang, Jun Bai
- **arXiv:** `2611.13190v1` (published 2026-11-09 20:10:37 UTC; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** Evaluated across six cancers and 2,782 TCGA patients; authors report the highest mean C-index among compared methods in each cohort and assess HNSC findings in an independent CPTAC cohort.
- **Claimed contribution:** The authors propose a 38-dimensional genomic-evolution representation that adds prognostic information beyond clinical and transcriptomic predictors in selected cancers.
- **Caveat:** This is retrospective survival modeling and association, not a validated clinical prognostic tool or causal account of tumor evolution; external prospective validation remains necessary.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** DNA & genomics; Biomedical & translational medicine; Quantitative methods

### 6. [Bridging Graph and Pairwise Learning for Gene Regulatory Network Inference from scRNA-seq Data](https://arxiv.org/abs/2611.13801)
- **Abstract:** scGPL combines global network topology with local transcription-factor/target-pair features to infer regulatory networks from single-cell RNA sequencing.
- **Authors:** Hang Li, Jiaxin Qi, Yan Cui, Yuhua Zheng, Jianqiang Huang
- **arXiv:** `2611.13801v1` (published 2026-11-10 09:34:28 UTC; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Seven benchmark datasets; authors report up to 13.7% improvement over their strongest baseline. The arXiv record says accepted to Bioinformatics.
- **Claimed contribution:** The model fuses whole-graph regulatory topology and dynamically sampled local dependencies.
- **Caveat:** Benchmark accuracy does not establish causal regulation in cells; inferred edges need perturbation-based or independent biological validation.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** RNA & transcriptomics; DNA & genomics; Bioinformatics & sequence analysis

### 7. [The Dose Makes the Poison: Exposure-Aware Evaluation of Generative Drug Design](https://arxiv.org/abs/2611.13398)
- **Abstract:** PBPK simulations re-rank PARP1 generative-design candidates by dose and predicted target exposure.
- **Authors:** Maria Franz, N. Benjamin Erichson
- **arXiv:** `2611.13398v1` (published 2026-11-10 00:20:01 UTC; categories: `q-bio.QM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Re-evaluates 60 molecules from three design pipelines; authors report seven failing exposure thresholds and predicted safety risks for 28% of the remainder. Accepted to the NeurIPS 2026 AI4DD workshop.
- **Claimed contribution:** The authors report that exposure-aware screening changes candidate ranking; 85% of candidates with achievable doses were outperformed by molecules omitted under static selection.
- **Caveat:** This is a computational PBPK evaluation for one target, not measured pharmacokinetics, toxicity, or efficacy. Prospective assay and exposure validation are needed.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biomedical & translational medicine; Biochemistry & proteins; Quantitative methods

### 8. [Detection of local recombination and mutation hotspots in bacterial genomes using neural posterior estimation](https://arxiv.org/abs/2611.13763)
- **Abstract:** A simulation-trained neural posterior method estimates gene-specific bacterial mutation and recombination rates and propagates uncertainty into hotspot calls.
- **Authors:** Haochu Liu, Richard G. Everitt, Xavier Didelot
- **arXiv:** `2611.13763v1` (published 2026-11-10 09:03:29 UTC; categories: `q-bio.GN`)
- **Evidence for ranking:** Tested on simulations and applied to datasets from Bacillus cereus, Staphylococcus aureus, and Escherichia coli.
- **Claimed contribution:** Authors report recovery of simulated rates with uncertainty intervals and a circular posterior-propagated detector for local rate elevation.
- **Caveat:** Inference assumes the specified recombination model and a fixed clonal genealogy; real-data applications do not experimentally confirm every hotspot.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 9. [When Covariance Is Not Enough: Kernel-Based Regularization for Single-Cell Counterfactuals](https://arxiv.org/abs/2611.13748)
- **Abstract:** A nonlinear kernel-independence penalty improves simulated single-cell counterfactual edits and is applied to a complex scRNA-seq dataset.
- **Authors:** Korbinian Traeuble, Edward de Brouwer, Archit Verma, Doron Haviv, Kipper Fletez-Brant
- **arXiv:** `2611.13748v1` (published 2026-11-10 08:49:33 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Controlled simulations with known nonlinear effects plus an application to a complex single-cell RNA-seq dataset.
- **Claimed contribution:** Authors report that normalized HSIC regularization separates known and unknown latent factors better than linear cross-covariance regularization in their tests.
- **Caveat:** The dataset application is in-silico; improved counterfactual profiles do not show that predicted edits reproduce real perturbation responses.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 10. [Ayurvedic Rasayana Restores Lipid Homeostasis in Liver: Insights from Systems Biology Studies](https://arxiv.org/abs/2611.13551)
- **Abstract:** Network analysis and a high-fat-diet animal study examine two Ayurvedic formulations alongside liver metabolomics and metabolic measurements.
- **Authors:** Harshit B Joshi, Anupama Vallazhath, Priyotosh Sil, Rahul Tiwari, Krishna Raghava Hebbar, Swati Sharma, Satish Rao B S, Basavaraj Hadapad, Areejit Samal, Manjunath B Joshi
- **arXiv:** `2611.13551v1` (published 2026-11-10 04:12:05 UTC; categories: `q-bio.MN`)
- **Evidence for ranking:** Combines network-based target hypotheses with animal measurements and untargeted liver metabolomics.
- **Claimed contribution:** Authors report lower high-fat-diet-associated glucose, cholesterol, liver enzymes, and steatosis after treatment, alongside changes in perturbed metabolomic pathways.
- **Caveat:** Preclinical animal evidence only; the abstract does not specify species or group sizes. Network proximity is not proof of mechanism, and no human benefit is established.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Molecular & cell biology; Biochemistry & proteins; Biomedical & translational medicine

### 11. [Improved Myelin Water Fraction Estimation and Uncertainty Mapping in Multicomponent T2 Relaxometry via NNLS Bootstrap Aggregation](https://arxiv.org/abs/2611.14395)
- **Abstract:** NNLS bootstrap aggregation estimates myelin water fraction and voxelwise variability, with simulations and scan-rescan tests in two cohorts.
- **Authors:** Erick J Canales-Rodríguez, Thomas Yu, Juan Manuel Górriz, Santiago Galdo-Álvarez, Tobias Kober, Tom Hilbert, Gian Franco Piredda, Miguel Ángel Rivas-Fernández
- **arXiv:** `2611.14395v1` (published 2026-11-10 17:43:51 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Compared across 40,000 simulated voxels and assessed across 20 white-matter regions in two cohorts comprising 13 healthy participants; authors report 36–41% lower simulated MAE than conventional NNLS.
- **Claimed contribution:** Authors report lower simulated error and improved scan-rescan repeatability, with bootstrap standard deviations as voxelwise sensitivity maps.
- **Caveat:** Small healthy-participant sample; no disease cohort or clinical outcome validation is reported in the abstract. This is not established diagnostic performance.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 12. [A first application of split conformal prediction for dose prediction in knowledge-based radiotherapy planning](https://arxiv.org/abs/2611.14438)
- **Abstract:** Split conformal prediction constructs patient-level uncertainty intervals for deep-learning dose predictions in head-and-neck radiotherapy cases.
- **Authors:** Raphaël Brodeur, Anne-Sophie Charest, Louis Archambault
- **arXiv:** `2611.14438v1` (published 2026-11-10 18:10:47 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** The authors compare patient-level and groupwise calibration constructions, reporting empirical coverage near nominal levels and narrower intervals for quantile aggregation; submitted to Physics in Medicine & Biology.
- **Claimed contribution:** The authors adapt split conformal prediction to voxel-based patient-level dose intervals and compare conservative maximum aggregation with narrower quantile aggregation.
- **Caveat:** The abstract gives no cohort size; calibration is not prospective clinical utility or improved treatment outcome, and coverage relies on sampling assumptions.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 13. [CURRENT: A Recurrent Neural Network for Concurrent Spatial and Temporal Super-Resolution of 4D Flow MRI](https://arxiv.org/abs/2611.14058)
- **Abstract:** CURRENT jointly increases spatial and temporal resolution in aortic 4D-flow MRI, trained on synthetic pairs built from computational flow simulations and in-vivo MRI backgrounds.
- **Authors:** Luuk Jacobs, Pietro Dirix, Sebastian Kozerke
- **arXiv:** `2611.14058v1` (published 2026-11-10 13:25:28 UTC; categories: `cs.CV`, `physics.med-ph`)
- **Evidence for ranking:** Compared with 4DFlowNet and sequential super-resolution baselines; authors report better spatial performance, comparable temporal performance, and more accurate relative-pressure estimates.
- **Claimed contribution:** A single recurrent architecture performs spatial and temporal super-resolution and shows promising generalization to in-vivo acquisitions.
- **Caveat:** Training is synthetic and the abstract does not give cohort size; generalization and pressure estimates need independent, larger clinical validation. Under review.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 14. [Influence of the branching geometry on SPION propagation: coupling of experiment and simulation](https://arxiv.org/abs/2611.13876)
- **Abstract:** Optical measurements in manufactured vascular bifurcations and simulations examine how geometry, flow, and magnetic actuation affect iron-oxide nanoparticle transport.
- **Authors:** Daniel Fleischhauer, Luiz C. P. Wille, Stefan Lyer, Jens Kirchner, Dietmar Drummer
- **arXiv:** `2611.13876v1` (published 2026-11-10 10:36:01 UTC; categories: `cs.ET`, `q-bio.QM`)
- **Evidence for ranking:** Couples in-situ particle-distribution measurements with Lagrangian and volume-of-fluid simulations across symmetric/asymmetric geometries and magnetic-field conditions.
- **Claimed contribution:** Authors report stratification-driven asymmetry in symmetric bifurcations and that magnetic actuation can counteract it and increase particle retention.
- **Caveat:** A controlled transport experiment and simulation, not in-vivo drug delivery or therapeutic evidence; submitted to IEEE ICC for review.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biomedical & translational medicine; Molecular & cell biology; Quantitative methods

## Trending Research Themes

Protein–ligand and protein-engineering methods make up the clearest cluster: Bonbon predicts interaction properties, ProTEUS uses mutational effects and experimental feedback, Pyrite ranks alternative poses, and ANTIOCH-VS assembles virtual-screening stages. Their evidence is not interchangeable: Bonbon and ProTEUS report biochemical experiments, while Pyrite and ANTIOCH-VS rely on computational benchmarks. The dose-aware PBPK paper adds modeled exposure, not measured pharmacology. Together these are multiple computational tasks, not independent validation of a shared drug-discovery claim.

A second cluster combines genomic and cell-state inference: scGPL integrates global and local network features, the kernel-regularized model generates single-cell counterfactuals, EvoSurv uses genomic evolution in survival prediction, and neural posterior estimation maps bacterial mutation/recombination rates. These methods make predictions or associations that require external, perturbational, or prospective validation. Medical-physics work in myelin-water estimation, radiotherapy dose intervals, and 4D-flow MRI adds explicit uncertainty or resolution objectives. The animal formulation and SPION-flow papers offer distinct preclinical measurements, not clinical evidence.

## Open Problems and Research Directions

- **Replicate protein-design gains independently:** ProTEUS reports closed-loop activity gains for two enzymes, while Bonbon reports a prospective inhibitor panel. Independent labs could reproduce these results with preregistered targets, transparent assay protocols, negative controls, and chemical/sequence holdouts; evaluate selectivity and stability as well as the target metric.
- **Bridge virtual ranking to real hit rates:** Pyrite and ANTIOCH-VS need tests with pose generators and targets beyond their current benchmarks. For Pyrite, compare multiple independent generators and test whether pose-ranking improvements improve prospective enrichment; for ANTIOCH-VS, run blinded prospective screens and report assay-confirmed hits.
- **Test predictive dose/exposure and cancer-risk signals externally:** Compare the PARP1 PBPK rankings against measured ADME/PK and dose-response data. For EvoSurv, test calibration and incremental value in external, prospectively assembled cohorts, with prespecified endpoints and subgroup analyses.
- **Validate inferred biological structure:** Test scGPL edges and single-cell counterfactual edits against perturbation-labelled datasets across donors and laboratories. For bacterial hotspots, assess sensitivity to genealogy uncertainty and model misspecification, then replicate calls across independent isolates.
- **Measure clinical and physical generalization:** Evaluate myelin-water and radiotherapy uncertainty estimates in larger external and disease cohorts, with scanner/site shifts and subgroup coverage. For CURRENT, validate on measured high-resolution 4D-flow scans; for SPION transport, examine pulsatile flow and blood-like fluids before progressing to in-vivo delivery claims.
- **Separate mechanism from association:** Replicate the Ayurvedic-formulation animal findings with reported species, group sizes, randomization/blinding, formulation composition, dose controls, and targeted tests of proposed network targets.

## Takeaway

Today’s batch is led by protein-interaction and protein-engineering AI, including two papers reporting wet-lab experiments, but the evidence ranges from biochemical tests to retrospective benchmarks and simulations. Genomic inference and biomedical imaging are the other notable clusters. None of the preprints establishes clinical efficacy; prospective external validation is the main open test.

## Method and sources

Window: daily announcement batch labeled Wednesday 2026-11-11. Batch entries span submission dates 2026-11-09 to 2026-11-10; snapshot time 2026-11-11 17:15:30 UTC. The arXiv recent pages showed a Wednesday 11 November group in the configured q-bio and medical-physics categories. One descending arXiv API query covered `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph` (200 results, extending back to 2026-10-28); current-day category-listing blocks were checked and cross-list duplicates were deduplicated. The accessible listings yielded 20 distinct entries in this batch; 14 were selected for direct biological/biomedical relevance. `cs.BI` was included in the API query, but arXiv’s recent-list page returned “Invalid archive or category” for that code. Each retained arXiv abstract page was verified. All are new submissions, not revisions.

Ranking: attention evidence is sparse for a same-day batch, so this is titled “Notable recent papers” and ranked by biological/biomedical relevance and checkable reported evidence, not popularity. Signals include arXiv cross-lists, venue comments where present, independent discussion where found, and the scope/design of reported experiments or benchmarks. No citation-velocity or readership claims are made. The arXiv biomedical corpus is incomplete; most clinical and experimental preprints may instead appear on bioRxiv, medRxiv, and elsewhere. Claims are attributed to authors; computational, animal, biochemical, and clinical evidence are distinguished.

Category query: https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200

Primary sources: linked arXiv abstract pages above; full texts were inspected for the three leading papers where extraction was practical. Corroborating sources: [NeurIPS oral listing for Bonbon](https://neurips.cc/virtual/2026/oral/149425); [independent coverage of Pyrite](https://www.bioscience.com.pk/en/subject/biology/pyrite-building-and-benchmarking-protein-ligand-pose-ranking-agents). Venue and study details otherwise come from arXiv record comments and the authors’ abstracts/full text.
