## Headline

Latest available announcement batch: Thursday, 19 November 2026. This report selects 13 papers, led by protein-structure and interaction evaluation, cross-modal molecular prediction, and computational cell dynamics. Spoken agenda: what was measured, what remains a model prediction, and which experiments could close that gap. arXiv has no official trending chart; this is an inferred relevance-ranked selection from incomplete biomedical coverage, not a popularity or readership ranking.

Window: daily; announcement batch 2026-11-19; snapshot 2026-11-20T01:27:12Z. No newer announcement batch was present for the current calendar day, so this uses the most recent prior batch.

## Notable recent papers (ranked by relevance; popularity evidence sparse)

### 1. [Biases and Limits of AlphaFold Predictions for Non-Globular Proteins](https://arxiv.org/abs/2611.24546)
- **Abstract:** The authors assemble experimentally validated non-globular protein cases to show how AlphaFold predictions can diverge from biologically relevant states when molecular context is missing.
- **Authors:** Maria Cristina Aspromonte, Alexander M. Monzon, Miguel A. Andrade-Navarro, Oriol Bárcenas, Viktor Bartosik, Pau Bernadó, Juan Cortés, Zsuzsanna Dosztanyi, Gabor Erdos, Isabella C. Felli, Helena Gradišar, San Hadži, Tamás Hegedűs, Khalil Joron, Pavel Kaderavek, Eitan Lerner, Dirk Linke, Pablo Mier, Ana Pantelić, Roberta Pierattelli, Salvador Ventura, Marija Vidović, Metaxia Vlassi, Lukas Zidek, Silvio C. E. Tosatto
- **arXiv:** `2611.24546v1` (published 2026-11-18T14:51:02Z; categories: `q-bio.BM`)
- **Evidence for ranking:** The paper organizes 27 experimentally validated cases into four discrepancy classes; a Biology+AI Daily technical thread also discussed it. This is a checkable discussion signal, not a popularity measure.
- **Claimed contribution:** The authors offer a framework for considering interactions and assembly, biological environment, global architecture/topology, and physical constraints when interpreting predicted structures.
- **Caveat:** This is a curated collection, not a systematic estimate of AlphaFold error rates. The authors emphasize that state selection often needs orthogonal experimental evidence, including NMR, SAXS, cryo-EM, or cross-linking.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biochemistry & proteins

### 2. [Cardiac MRI-informed electrocardiography enables biologically grounded cardiomyopathy detection](https://arxiv.org/abs/2611.23925)
- **Abstract:** MyoECG transfers CMR-derived structural and functional information into an ECG representation for cardiomyopathy detection from ECGs alone at inference.
- **Authors:** Zhengyao Ding, Kewen Wang, Yujian Hu, Ziyu Li, Yiheng Mao, Yue Wang, Haitao Li, Dengnan Zhang, Xuanhong Liu, Yue Wang, Jing Wang, Yue Chen, Longbo Wang, Mengjia Chen, Chengchen Zhao, Xuesen Chu, Yubin Zhang, Mor Peleg, Judith Somekh, Mingxuan Yuan, Hui Yan, Yue Gu, Fan Yi, Zhilong Jia, Zhentao Tang, Xi Hu, Fei Wu, Hongkun Zhang, Ting Chen, Zhengxing Huang
- **arXiv:** `2611.23925v1` (published 2026-11-18T06:16:55Z; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Authors report 45,241 paired ECG-CMR examinations for pretraining, over 1.8 million ECGs across seven data sources, and a six-cardiologist reader study using 403 ECGs.
- **Claimed contribution:** The authors report AUROCs of 0.800–0.974 across their datasets and improved mean reader sensitivity and specificity with model assistance.
- **Caveat:** Retrospective preprint evidence is not a prospective clinical-impact study. Case mix and prevalence varied; the authors note limited positive predictive value in low-prevalence datasets and call for prospective validation.
- **Announcement type:** new submission (cross-list), 2026-11-19
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 3. [ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry](https://arxiv.org/abs/2610.26829)
- **Abstract:** ProteinGeoBench tests whether AI agents can retrieve facts about protein structures, check sequences, calculate coordinate geometry, and reason about structures.
- **Authors:** Matt Turk, Brandon L. Neel, Diana M. Lopez, Zachary D. Smith, Grace N. Johnecheck, James B. Golden
- **arXiv:** `2610.26829v2` (first submitted 2026-10-19T17:55:38Z; updated 2026-11-18T02:39:21Z; categories: `cs.AI`, `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** The revised study includes 131 tasks, 4,249 runs across four frontier models, and a 26-model subset; benchmark tasks and code are publicly linked by the authors.
- **Claimed contribution:** The authors report a gap between fact lookup and coordinate-based geometry, and show that rankings shift with network access and agent harness; the leaders were too close to order reliably under their bootstrap analysis.
- **Caveat:** Results concern a specific benchmark and tool setup, not general biological reasoning or experimental performance. The paper itself shows that access and harness configuration materially affect scores.
- **Announcement type:** revision, 2026-11-19
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 4. [SCOPE: Single-Cell Omics Prediction from Histology via RNA-Protein Prior Enhancement](https://arxiv.org/abs/2611.24104)
- **Abstract:** SCOPE combines gene-protein relationships and biological priors to predict cell-resolved RNA and protein profiles from H&E images, including markers without direct training labels.
- **Authors:** Leyang Tao, Xuan Gong, Luyuan Xie, Arjun Beniwal, Yuqi Tan, Kun-Hsing Yu
- **arXiv:** `2611.24104v1` (published 2026-11-18T09:24:45Z; categories: `cs.CV`, `q-bio.GN`)
- **Evidence for ranking:** Tested across 16 organs and two external protein cohorts; authors report mean RNA-correlation gains of 8.8% and protein-correlation gains of 9.7% for seen and 11.9% for unseen markers against the strongest stated baselines.
- **Claimed contribution:** The authors present a shared cross-omics model trained on unpaired assay sections and designed to extend predictions beyond directly supervised markers.
- **Caveat:** These remain computational predictions, not molecular assay replacements. External protein cohorts were limited in size (35 colorectal-cancer patients and 40 ORION patients), and correlation does not establish cell-level biological accuracy.
- **Announcement type:** new submission (cross-list), 2026-11-19
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Bioinformatics & sequence analysis

### 5. [Are You Learning Biological Signal or Shortcuts? Auditing and Mitigating Bias in Protein-Protein Interaction Datasets](https://arxiv.org/abs/2609.10193)
- **Abstract:** The authors audit study and technical biases in protein-interaction datasets that can let machine-learning models exploit shortcuts rather than interaction biology.
- **Authors:** Judith Bernett, Anton Spannagl, Joel Ås, Markus List, David B. Blumenthal
- **arXiv:** `2609.10193v2` (first submitted 2026-09-09T14:02:18Z; updated 2026-11-18T12:43:58Z; categories: `q-bio.MN`, `cs.LG`)
- **Evidence for ranking:** The revision compares HIPPIE, IntAct, STRING, and two PDB-derived datasets, and reports distinct shortcut signals across random and protein-overlap-controlled splits.
- **Claimed contribution:** The authors provide a Nextflow pipeline using similarity-aware splits and optimization-based negative sampling to reduce selected dataset biases.
- **Caveat:** The analysis concerns the databases, splits, and negative-sampling procedures studied; mitigation of these shortcuts does not by itself establish accurate biological interaction prediction.
- **Announcement type:** revision, 2026-11-19
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 6. [Uneven gains in protein-RNA affinity and mutation-effect prediction](https://arxiv.org/abs/2611.24739)
- **Abstract:** The study tests whether improved protein-RNA affinity estimates also improve average mutation effects, mutation ranking, and local prediction accuracy.
- **Authors:** Shangkun Sima, Tongfei Shen, Tianchi Lu
- **arXiv:** `2611.24739v1` (published 2026-11-18T16:57:14Z; categories: `cs.LG`, `cs.CE`)
- **Evidence for ranking:** It compares 11 method families, 220 mutation pairs across 20 families, and an independent test of 24 quantitative pairs from three source-matched families.
- **Claimed contribution:** Across 220 pairs, the authors report improved mean-effect accuracy but no decrease in mean-centered local error and uncertain ranking gains. In the independent set, mean-centered local error fell overall from 0.4198 to 0.3761 pKd, though one of three families had higher error.
- **Caveat:** Performance varies by family and metric; the small independent test cannot establish broad transfer. This paper is outside the configured biology-category query but is included for its direct protein-RNA biochemical focus.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biochemistry & proteins; RNA & transcriptomics; Quantitative methods

### 7. [STORM: A Lightweight Structure-Free Model for Binding Affinity Prediction](https://arxiv.org/abs/2611.23777)
- **Abstract:** STORM combines protein and molecule representations to predict small-molecule binding affinity without requiring a predicted complex structure at inference.
- **Authors:** Ayush Pandit, Rohan V. Koodli, Wei Deng, Roxana Daneshjou, Ron O. Dror
- **arXiv:** `2611.23777v1` (published 2026-11-18T03:34:08Z; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** Authors compare on multiple evaluation datasets and report accuracy comparable to or above Boltz-2 on those tests, with over five orders of magnitude faster training and inference.
- **Claimed contribution:** The authors propose similarity transfer from reference molecules as a lightweight route to affinity prediction and suggest combining historical experimental affinity data with structural and biophysical information.
- **Caveat:** This is an in-silico benchmark claim, not evidence of experimental hit rates or drug efficacy; performance on novel targets and scaffolds requires independent assessment.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 8. [Micrograph B-factor estimation via Wilson statistics](https://arxiv.org/abs/2611.24150)
- **Abstract:** The method estimates and corrects a separate B factor for each cryo-EM micrograph before three-dimensional reconstruction rather than applying one global correction afterward.
- **Authors:** Ayelet Heimowitz, Amit Singer
- **arXiv:** `2611.24150v1` (published 2026-11-18T09:55:09Z; categories: `eess.IV`, `q-bio.BM`)
- **Evidence for ranking:** Evaluated using three real-world EMPIAR datasets; for beta-galactosidase, the authors report a 0.2 Å resolution improvement after micrograph-level correction.
- **Claimed contribution:** The authors report that per-micrograph Wilson-statistics estimates can account for variable image decay and improve reconstruction resolution in their tests.
- **Caveat:** Evidence comes from three datasets and specific RELION reconstructions; the abstract does not establish that the gain generalizes across targets, acquisition protocols, or pipelines.
- **Announcement type:** new submission (cross-list), 2026-11-19
- **Themes:** Biochemistry & proteins; Medical physics & imaging

### 9. [MitoWorld: A Stochastic World Model of the Single-Cell Cycle under Genetic Perturbation](https://arxiv.org/abs/2611.23953)
- **Abstract:** MitoWorld generates single-cell image trajectories after gene knockdown and jointly models appearance changes and cell-division timing.
- **Authors:** Ting Long, Xiaojing Sun, Cheng Han, Zhicheng Ji, Yingnian Wu, Jiebo Luo, Heng Fan, Dongfang Liu
- **arXiv:** `2611.23953v1` (published 2026-11-18T06:42:32Z; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Authors report evaluation on 325 held-out MitoCheck tracks spanning 17 knockdowns and a control, with lower FID and JEDi than their strongest baselines and near-nominal 90% interval coverage.
- **Claimed contribution:** The authors model continuous image evolution with a division hazard, offering a generative tool for time-lapse perturbation screens.
- **Caveat:** Evaluation is computational and limited to MitoCheck; generated trajectories do not show that predicted perturbation effects generalize to new cell types or experimental settings.
- **Announcement type:** new submission (cross-list), 2026-11-19
- **Themes:** Omics & single-cell methods; Molecular & cell biology; Quantitative methods

### 10. [Horizontal Flow Matching for Single-Cell Spatiotemporal Dynamics](https://arxiv.org/abs/2611.24764)
- **Abstract:** HORIZON models changes in tissue state and cell abundance while factoring out common rotation and translation in spatial-transcriptomics snapshots.
- **Authors:** Zihan Wang, Jianzhe Li, Zhenyi Zhang, Peijie Zhou
- **arXiv:** `2611.24764v1` (published 2026-11-18T17:16:53Z; categories: `cs.LG`, `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Authors report coordinate-perturbation simulations and improved reconstruction plus held-out-stage interpolation on four spatial-transcriptomics time courses.
- **Claimed contribution:** The method estimates relative tissue pose and continuous tissue, expression, and abundance changes from snapshots.
- **Caveat:** Snapshot-derived distributions do not track the same living cells; inferred dynamics depend on sampling, alignment, and modeling assumptions.
- **Announcement type:** new submission (cross-list), 2026-11-19
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Quantitative methods

### 11. [Elysium: Simulation-Free Unbalanced Schrödinger Bridges](https://arxiv.org/abs/2611.24763)
- **Abstract:** Elysium learns state transitions and population changes from destructive single-cell snapshots without simulating trajectories during training.
- **Authors:** Zihan Wang, Jianzhe Li, Zhenyi Zhang, Peijie Zhou
- **arXiv:** `2611.24763v1` (published 2026-11-18T17:16:41Z; categories: `cs.LG`, `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Authors report tests against simulated benchmarks with known ground truth and single-cell time courses, including biphasic drug-response dynamics.
- **Claimed contribution:** The authors propose direct regression objectives for an unbalanced Schrödinger bridge and report recovery of the optimum under stated assumptions.
- **Caveat:** Inferred population distributions and events are not direct lineage observations; simulation-ground-truth results do not independently validate biological mechanisms.
- **Announcement type:** new submission (cross-list), 2026-11-19
- **Themes:** Omics & single-cell methods; Quantitative methods

### 12. [Unmyelinated axons alter the biological interpretation of MRI biomarkers of demyelination](https://arxiv.org/abs/2611.24487)
- **Abstract:** MRI and electron microscopy in a cuprizone mouse model indicate that unmyelinated axons contribute to white-matter metrics often interpreted as myelinated-fiber biomarkers.
- **Authors:** Ali Abdollahzadeh, Ricardo Coronado-Leija, Elizabeth Chasen, Sungheon G. Kim, Dmitry S. Novikov, Els Fieremans
- **arXiv:** `2611.24487v1` (published 2026-11-18T14:20:34Z; categories: `physics.med-ph`)
- **Evidence for ranking:** The authors combine diffusion and relaxation MRI with electron microscopy and report up to 8% negative bias in g-ratio estimates when within-voxel heterogeneity is ignored.
- **Claimed contribution:** The authors argue that short-diffusion-time axonal water fraction reflects total intra-axonal space and g-ratio estimates should include both myelinated and unmyelinated axons.
- **Caveat:** This is a mouse-model and imaging-method result; it does not validate a human diagnostic biomarker or establish clinical utility.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 13. [A structure-based model of the bacterial chemosensory array reveals how the scaffolding protein CheW tunes sensory responses](https://arxiv.org/abs/2611.23921)
- **Abstract:** A structure-based lattice model tests how CheW abundance and placement could change bacterial chemosensory-array cooperativity, sensitivity, and activity fluctuations.
- **Authors:** David Hathcock, Yingxin Zheng, Yuhai Tu
- **arXiv:** `2611.23921v1` (published 2026-11-18T06:11:15Z; categories: `physics.bio-ph`, `cond-mat.stat-mech`, `q-bio.MN`)
- **Evidence for ranking:** The model quantitatively reproduces previously reported CheW-titration effects and yields specific predictions for single-cell signaling dynamics.
- **Claimed contribution:** The authors propose that CheW tunes effective coupling and predict a crossover from relaxational to oscillatory fluctuations.
- **Caveat:** The new dynamic signatures are model predictions, not direct observations in this study; targeted single-cell measurements are needed.
- **Announcement type:** new submission (cross-list), 2026-11-19
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

## Trending Research Themes

- **Protein models meet experimental context and evaluation design:** AlphaFold's non-globular examples, ProteinGeoBench's lookup-versus-geometry tests, the PPI dataset audit, protein-RNA mutation effects, STORM affinity prediction, and per-micrograph cryo-EM correction all stress that conclusions depend on molecular context, benchmark construction, and the exact quantity measured.
- **Cross-modal prediction and reconstructed cell dynamics:** MyoECG and SCOPE transfer information from CMR or histology to more scalable signals; MitoWorld, HORIZON, and Elysium infer cell or tissue dynamics from time-lapse or destructive snapshot data. These are separate applications, not mutual validation, and predicted states are not direct assays or lineage tracking.
- **Molecular imaging and mechanistic models:** The MRI/EM study revisits what white-matter metrics represent, while the CheW model makes testable predictions about bacterial signaling. One mouse-model measurement study and one theoretical model do not establish a field-wide shift.

## Open Problems and Research Directions

- **Validate predictions against matched measurements:** For SCOPE, compare RNA/protein predictions with assays from matched sections, especially for unseen markers and across laboratories. For MyoECG, assess prospective, site-held-out cohorts with realistic prevalence, calibration, false-positive burden, and downstream clinical decisions before claiming clinical impact.
- **Test molecular-model generalization:** Extend AlphaFold's case taxonomy with blinded, condition-specific structural assays. For ProteinGeoBench, preregister tool access and harness settings and report task-specific uncertainty. For PPI and affinity models, use protein-family- or target-held-out evaluation and independent biochemical assays to distinguish biological signal from dataset shortcuts or reference-molecule similarity.
- **Ground inferred dynamics in direct time series:** Compare HORIZON and Elysium with live-cell imaging or controlled perturbation time courses, varying sampling intervals and registration error; distinguish population-level fit from lineage-level claims. For MitoWorld, test held-out knockdowns and cell types.
- **Check measurement-method transfer:** Replicate micrograph-level B-factor correction across additional targets and cryo-EM pipelines; test MRI/axon interpretations outside the cuprizone model. For CheW, measure predicted activity fluctuations across CheW levels with single-cell assays.

## Takeaway

The batch is notable for protein-model evaluation and methods that transfer information across measurements or infer hidden cellular states. The evidence ranges from curated experimental cases and large retrospective cohorts to computational benchmarks and mechanistic modeling. None removes the need for independent experimental validation, and this relevance-ranked list should not be read as a measured popularity surge.

## Method and sources

- **Window:** daily; latest batch was announced Thursday, 2026-11-19. Candidate submission or revision timestamps for the selected set fall on 2026-11-18 UTC; announcement date and submission timestamp are distinct. Snapshot: 2026-11-20T01:27:12Z. No newer batch was visible, so this uses the prior announcement batch.
- **Candidate pool:** traversed the current `new` listings for configured biology/biomedicine categories and checked the corresponding recent-date group; 26 distinct records appeared in the category listings. The broad configured query covered `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. One additional `cs.LG` submission was included because its contribution directly concerns protein-RNA affinity. Candidates were deduplicated by versionless arXiv ID; retained abstract pages and latest version metadata were verified. The top three by relevance were also read in PDF form.
- **Ranking:** arXiv has no official trending chart. No reliable citation-velocity or broad engagement ranking was established for this very recent batch; ordering emphasizes direct biological/biomedical relevance and specificity of reported evidence. A web-indexed technical thread is noted for the AlphaFold paper, but this is not a popularity measurement. No downloads, abstract views, or citation gains are inferred.
- **Coverage:** arXiv is not a representative index of biomedical research and this report does not cover bioRxiv, medRxiv, or the wider medical literature. Computational predictions, experimental assays, animal models, and human retrospective cohorts are kept distinct; this is not clinical advice.
- **Sources:** [arXiv q-bio.BM new listings](https://arxiv.org/list/q-bio.BM/new), [q-bio.GN](https://arxiv.org/list/q-bio.GN/new), [q-bio.MN](https://arxiv.org/list/q-bio.MN/new), [q-bio.CB](https://arxiv.org/list/q-bio.CB/new), [q-bio.QM](https://arxiv.org/list/q-bio.QM/new), and [physics.med-ph](https://arxiv.org/list/physics.med-ph/new); [configured arXiv API query](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200); individual abstract pages linked above; [ProteinGeoBench code and benchmark](https://github.com/Protege-AI/ProteinGeoBench); [Biology+AI Daily discussion of AlphaFold examples](https://x.com/BiologyAIDaily/status/2123392274294055062).
