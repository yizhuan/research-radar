# Daily arXiv Biology & Biomedicine — 2026-11-06 batch

Snapshot: 2026-11-09 01:20:04 UTC. The latest available announcement batch is Friday, 6 November 2026; this daily report uses that prior batch because Monday’s batch was not yet available. Fourteen notable papers are included: nine new submissions/cross-list entries and five substantive revisions. The dominant pattern is computational biology and AI being judged by more explicit validation—experimental follow-up, external or held-out benchmarks, model reliability, or dynamical checks. Spoken agenda: agent-led drug discovery, single-cell models and their limits, and the difference between prediction and validation. arXiv has no official trending chart; this is an inferred relevance ranking from incomplete biomedical coverage, not a readership ranking. Much clinical and experimental biology appears outside arXiv.

## Notable recent papers (ranked)

### 1. [PharmAgents2: Towards Autonomous End-to-End Drug Discovery](https://arxiv.org/abs/2611.07653)
- **Abstract:** PharmAgents2 combines literature-derived decision skills and parallel agent exploration, reports a 121-question benchmark, and describes three discovery investigations whose findings were subsequently tested by human researchers.
- **Authors:** Haichuan Tan, Bowen Gao, Tao Huang, Jiaxin Tan, Xin Hong, Baoguo Yao, Yifei Wang, Zhichao Deng, Hanji Du, Dapeng Jiang, Yiheng Li, Weiwei Ma, Xin Ma, Yuqi Shi, Zixiang Wang, Kelin Wu, Tianxiang Wu, Wenxuan Xie, Jie Zang, Huiyu Zhang, Mojia Zhang, Yuying Zhang, Ya-Qin Zhang, Wei-Ying Ma, Yanyan Lan
- **arXiv:** `2611.07653v1` (published 2026-11-05 08:39:19 UTC; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Three author-reported wet-lab follow-ups and a 121-question benchmark with three end-to-end tasks; Semantic Scholar reported 0 citations and 0 influential citations at snapshot.
- **Claimed contribution:** The authors say PharmAgents2 connects scientific decision support with parallel exploration; reported scenarios include LpxH inhibition, JAK1 candidate testing, and experimental support for a secondary-target binding result.
- **Caveat:** These are early research scenarios, not clinical evidence. The authors say JAK1 selectivity and binding modes need further validation; the LpxH site and mechanism remain to be established.
- **Announcement type:** New cross-list entry, 2026-11-06 batch
- **Themes:** Biomedical & translational medicine; Biochemistry & proteins

### 2. [Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding](https://arxiv.org/abs/2611.07723)
- **Abstract:** BILBY-PRO broadens motif-scaffold evaluation to 220 PROSITE-derived cases, while BILBY-MD tests whether static designs retain motif and scaffold behavior in molecular-dynamics simulations.
- **Authors:** Emile de Bruyn, Moritz Schäffler, Jannik Schneider, Sebastian R. Schmidt, Chanwoong Hwang, Aleena Siji, Utkarsh Upadhyay, Stefan Bauer, Alexander Schug, Stefan Kesselheim, Artur Yakimovich, Alina Bazarova
- **arXiv:** `2611.07723v1` (published 2026-11-05 09:38:23 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Accepted at NeurIPS 2026 (Evaluations & Datasets Track); evaluates six generators and 220 benchmark cases, then dynamically assesses 55 static solves. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report 31/55 model–problem solves met their MD-support threshold, but only 8/55 passed all checks, showing static recovery does not establish whole-scaffold dynamical fidelity.
- **Caveat:** The authors call the MD thresholds heuristic and note 200 ns trajectories may miss slower instability; MD support does not establish biochemical function.
- **Announcement type:** New cross-list entry, 2026-11-06 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation](https://arxiv.org/abs/2611.08086)
- **Abstract:** MUSS combines DNA-derived peak and gene representations with paired single-cell chromatin-accessibility and expression data to predict regulatory readouts, including for unseen genomic regions.
- **Authors:** Kangjie Zheng, Amirhossein Vahidi, Liying Jin, Joseph Clarke, Vijaya Baskar MS, Connor Rogerson, Mengji Zhang, Muzlifah Haniffa, Anshul Kundaje, Mo Lotfollahi
- **arXiv:** `2611.08086v1` (published 2026-11-05 14:34:07 UTC; categories: `cs.AI`, `q-bio.GN`)
- **Evidence for ranking:** Journal reference: NeurIPS 2026. Evaluates gene-expression prediction on four paired datasets and tests held-out sequences/cell types plus other regulatory tasks. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report strong results against sequence and single-cell baselines, including prediction for held-out genes and peaks, using a frozen AlphaGenome encoder and multiscale peak–gene interactions.
- **Caveat:** This is benchmark-based computational evidence, not direct experimental confirmation of regulatory mechanisms. The authors note encoder dependence, paired-data requirements, quadratic attention cost, and limited multi-seed testing.
- **Announcement type:** New cross-list entry, 2026-11-06 batch
- **Themes:** DNA & genomics; RNA & transcriptomics; Gene regulation & epigenetics

### 4. [Thalamus-Reasoning: A Multimodal Large Language Model for Multi-Sample Omics Reasoning](https://arxiv.org/abs/2605.06728)
- **Abstract:** The revised Thalamus-Reasoning model encodes bulk or single-cell transcriptomes as continuous embeddings for language-guided analysis across multiple samples.
- **Authors:** Maciej Sypetkowski, Łukasz Smoliński, Remigiusz Kinas, Joanna Krawczyk, Bartłomiej Hofman, Aleksandra Możwiłło, Michał Pikusa, Tomasz Jetka, Rafał Powalski
- **arXiv:** `2605.06728v3` (published 2026-05-07 11:27:11 UTC; revised 2026-11-05 15:18:38 UTC; categories: `q-bio.GN`, `cs.AI`, `q-bio.CB`)
- **Evidence for ranking:** Substantive v3 revision in this batch; GEO-OmicsQA has 3,000 publication-disjoint questions. Semantic Scholar currently reports 1 citation and 0 influential citations (total, not a gain in this window).
- **Claimed contribution:** The authors report leading results on several held-out annotation tasks and GEO-OmicsQA variants, plus best average performance on PerturbQA among compared methods.
- **Caveat:** Evaluation is on curated computational tasks, not experimental discovery; some training supervision is LLM-generated, with task-specific quality checks.
- **Announcement type:** Revision, 2026-11-06 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Bioinformatics & sequence analysis

### 5. [scTREAT: Latent Diffusion for Single-Cell Drug-Response Prediction](https://arxiv.org/abs/2510.11726)
- **Abstract:** The revised scTREAT model uses latent diffusion with explicit cell-state, drug-identity, and dose conditioning to predict single-cell drug-response profiles.
- **Authors:** Zhaokang Liang, Shuyang Zhuang, Xiaoran Jiao, Weian Mao, Hao Chen, Chunhua Shen
- **arXiv:** `2510.11726v3` (published 2025-10-08 16:17:39 UTC; revised 2026-11-05 09:23:34 UTC; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** Substantive v3 revision; evaluated on Tahoe-100M condition-level profiles. Semantic Scholar currently reports 8 citations and 0 influential citations (total, not period gains).
- **Claimed contribution:** The authors report best scores on 10/12 metrics for unseen cell-line–drug combinations and 11/12 for unseen drugs among tested methods.
- **Caveat:** This is computational evaluation on condition-level pseudobulk profiles; predicted responses require independent experimental validation and are not treatment evidence.
- **Announcement type:** Revision, 2026-11-06 batch
- **Themes:** RNA & transcriptomics; Biomedical & translational medicine; Quantitative methods

### 6. [One Method Does Not Fit All: A Large-Scale Benchmark of Imputation Methods for Single-Cell RNA Sequencing Data](https://arxiv.org/abs/2603.24626)
- **Abstract:** The revised benchmark compares 16 scRNA-seq imputation methods across protocols, tasks, and datasets, finding that relative performance depends on the analytical setting.
- **Authors:** Yuichiro Iwashita, Ahtisham Fazeel Abbasi, Koichi Kise, Andreas Dengel, Muhammad Nabeel Asim
- **arXiv:** `2603.24626v3` (published 2026-03-25 02:46:51 UTC; revised 2026-11-05 14:26:36 UTC; categories: `q-bio.GN`, `cs.LG`, `stat.ML`)
- **Evidence for ranking:** Substantive v3 revision; covers 16 methods, 10 protocols, six downstream tasks, and 30 benchmark datasets. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report that traditional methods are often more consistent across tasks, and better numerical recovery does not necessarily improve biological interpretation.
- **Caveat:** The authors find no universally best method; benchmark comparisons do not show that imputation recovers true expression in every setting.
- **Announcement type:** Revision, 2026-11-06 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 7. [Querying Counterfactuals on Tissue Graphs with Supervised Disentanglement](https://arxiv.org/abs/2606.08493)
- **Abstract:** Cellina separates intrinsic cell state from spatial context to model in-silico tissue-neighborhood interventions.
- **Authors:** Abdul Moeed, Stefan Schrod, Martin Rohbeck, Marc Jan Bonder, Pavlo Lutsik, Oliver Stegle, Daniel Dimitrov
- **arXiv:** `2606.08493v4` (published 2026-06-07 07:41:00 UTC; revised 2026-11-05 09:36:28 UTC; categories: `q-bio.GN`, `cs.LG`, `stat.ML`)
- **Evidence for ranking:** Substantive v4 revision; benchmarks span over 2.5 million spatially resolved cells in observational and interventional screens. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report stronger in-silico perturbation predictions than spatial and non-spatial competitors and identify cancer subdomains with distinct predicted signaling programs.
- **Caveat:** Counterfactual outputs are predictions, not newly performed interventions; benchmark performance does not establish causal validity in other tissues.
- **Announcement type:** Revision, 2026-11-06 batch
- **Themes:** Molecular & cell biology; Omics & single-cell methods; Quantitative methods

### 8. [Reclassification Is All You Missed: Surfacing Variant Reinterpretation Need in Online Health Communities at Population Scale](https://arxiv.org/abs/2611.07054)
- **Abstract:** PRISM screens public health-community posts for possible genetic-variant reinterpretation needs and drafts—but does not send—outreach after checking later ClinVar classifications.
- **Authors:** Kamalakkannan Ravi, Mengshu Nie, Annapurna Poduri, Cong Liu
- **arXiv:** `2611.07054v1` (published 2026-11-04 19:13:45 UTC; categories: `cs.CL`, `cs.AI`, `cs.CY`, `q-bio.GN`)
- **Evidence for ranking:** Analyzes 3.9 million posts across 32 communities; a clinician assessed 30 held-out drafts, judging 27 factually grounded and 15 fit to send. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** PRISM surfaced 123 candidate classification differences, five from uncertain to pathogenic or likely pathogenic, in a no-contact dry run.
- **Caveat:** This is not a clinical service or evidence that recontact improves outcomes; factual grounding alone did not make all drafted messages suitable to send.
- **Announcement type:** New cross-list entry, 2026-11-06 batch
- **Themes:** DNA & genomics; Biomedical & translational medicine

### 9. [A low-rank decoder bottleneck bounds reliability in foundation-model perturbation prediction](https://arxiv.org/abs/2611.05849)
- **Abstract:** An audit of perturbation-response models finds a low-rank decoder and proposes nearest-neighbor distance from predicted responses as a confidence signal for prediction accuracy.
- **Authors:** Zheyu Zhang, Yuanhao Huang, Fan Feng, Jie Liu
- **arXiv:** `2611.05849v1` (published 2026-11-04 02:39:03 UTC; categories: `cs.LG`, `q-bio.QM`, `stat.ML`)
- **Evidence for ranking:** Accepted at NeurIPS 2026; tested across three encoders and four CRISPRi cell lines, with reported mean absolute Spearman correlation 0.81 between the proposed score and per-perturbation Pearson delta correlation. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors propose predicted-nearest-neighbor distance as a per-prediction reliability estimate and report transfer across the evaluated encoders and cell lines.
- **Caveat:** Tests cover a limited set of models and perturbation settings; confidence-score correlation does not validate predictions experimentally or establish performance in new biological settings.
- **Announcement type:** New cross-list entry, 2026-11-06 batch
- **Themes:** Omics & single-cell methods; Quantitative methods

### 10. [High resolution 3D localization of ultrasound sparse sources using a SAGE algorithm](https://arxiv.org/abs/2611.07966)
- **Abstract:** A SAGE-based estimator localizes simultaneous sparse ultrasound sources, reporting 0.24 mm error in simulations and improved resolution on proton-induced nanodroplet-vaporization data.
- **Authors:** Sophie V. Heymans, François Rottenberg, Tatiana Gelvez-Barrera, Adrian Basarab, Barbara Nicolas
- **arXiv:** `2611.07966v1` (published 2026-11-05 13:00:19 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Includes 49 simulated acquisitions and experimental ultrasound-array data, with sub-millimeter agreement reported against the proton distribution. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors propose parametric localization for transient simultaneous sources and report better spatial resolution than beamforming in their experiment.
- **Caveat:** The evidence is simulation plus a specific experimental dataset, not a patient study or clinical validation of proton-therapy monitoring.
- **Announcement type:** New submission, 2026-11-06 batch
- **Themes:** Medical physics & imaging; Quantitative methods

### 11. [How Deep is the Signal? Time-Context up to 30 Years for Colorectal Cancer Prediction in a Primary-Care EHR Model](https://arxiv.org/abs/2611.07265)
- **Abstract:** A North West London primary-care study finds colorectal-cancer discrimination rises modestly as an EHR model's lookback expands to 18 years, then plateaus.
- **Authors:** Achille Raviez, Lan Wang, Brendan Delaney
- **arXiv:** `2611.07265v1` (published 2026-11-05 00:34:47 UTC; categories: `cs.LG`, `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Accepted at ML4H 2026 Findings; evaluates a frozen cohort of 1,008 cases and 9,582 matched controls. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report AUROC rising from 0.551 at two years to 0.590 at 18 years, then plateauing; XGBoost reached 0.589.
- **Caveat:** Retrospective single-region evaluation with modest discrimination; no prospective utility is shown, so this is not a validated screening test.
- **Announcement type:** New cross-list entry, 2026-11-06 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 12. [Resampling-based batch reweighting for ComBat harmonization of MRI radiomic features in a multi-scanner glioma cohort](https://arxiv.org/abs/2611.02156)
- **Abstract:** This revised MRI study tests whether reweighting underrepresented scanner batches before ComBat estimation reduces residual scanner association in glioma radiomic features.
- **Authors:** Rifa Sajda Tasnim, Yushuf Sharker, Md Forhad Hossain, Rakibur Rahman, Enamul Hoque Bhuiyan
- **arXiv:** `2611.02156v2` (published 2026-11-01 19:43:22 UTC; revised 2026-11-05 13:40:38 UTC; categories: `eess.IV`, `physics.med-ph`)
- **Evidence for ranking:** Substantive v2 revision; retrospective 733-patient, single-center cohort across nine scanner configurations; journal reference to JMRI 2026. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report residual scanner association in 13/428 features after standard ComBat versus 8/428 after batch-augmented ComBat.
- **Caveat:** Single-center harmonization results do not establish external generalization or improved patient outcomes.
- **Announcement type:** Revision, 2026-11-06 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 13. [Geometric Relevance Is Not Sufficient: Evaluating Focused Post-Training Supervision in Diffusion Docking](https://arxiv.org/abs/2611.08249)
- **Abstract:** A fixed-budget DiffDock study finds focused supervision on geometrically consequential corrections does not consistently improve pose success over broad continuation.
- **Authors:** Michael Brown, Maryam Rahimimovassagh, Mehdi Yazdani-Jahromi, Sanjeda Sara Jennifer, Ivan Garibay
- **arXiv:** `2611.08249v1` (published 2026-11-05 16:26:44 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Accepted at the NeurIPS 2026 AI4DD Workshop; compares multiple supervision policies and distinct pose-quality measures. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report that broad continuation had the highest mean trained-policy Top-1 success below 5 Å; focused or mixed supervision showed no consistent gain under the tested budget.
- **Caveat:** This result is specific to DiffDock and the tested supervision choices and budget; it does not show focused supervision cannot help elsewhere.
- **Announcement type:** New cross-list entry, 2026-11-06 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 14. [Accelerating reaction network identification via frequency-domain analysis](https://arxiv.org/abs/2611.07684)
- **Abstract:** For certain stochastic reaction systems, the authors find Fourier-domain likelihoods can be approximately Gaussian and use that observation to speed Bayesian network inference.
- **Authors:** Zhou Fang, Wenying Sun, Xiaoyu Zhang, Mustafa Khammash
- **arXiv:** `2611.07684v1` (published 2026-11-05 09:11:41 UTC; categories: `q-bio.MN`)
- **Evidence for ranking:** New q-bio.MN submission; the abstract reports a gene-transcription example demonstrating the method. Semantic Scholar: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors present frequency-domain inference intended to reduce the computational burden of particle-filter-based Bayesian identification for a subset of systems.
- **Caveat:** The abstract demonstrates one gene-transcription example; behavior across broader reaction-system classes remains to be established.
- **Announcement type:** New submission, 2026-11-06 batch
- **Themes:** Molecular & cell biology; Quantitative methods

## Trending Research Themes

- **Single-cell models increasingly represent or evaluate more than a gene list.** MUSS grounds peak and gene features in DNA sequence; Thalamus-Reasoning and scTREAT integrate transcriptomic profiles with language or drug context; the imputation benchmark compares methods across 30 datasets; and Cellina models spatial context. These papers are distinct computational approaches, not independent evidence for one biological mechanism.
- **Evaluation criteria are becoming part of the scientific claim.** BILBY tests dynamics beyond static protein recovery; the docking study separates score fidelity from pose success; the perturbation audit asks when a prediction is reliable; and the imputation benchmark finds task-dependent method rankings. Across this corpus, a single aggregate score can obscure important failure modes.
- **Validation levels vary sharply.** PharmAgents2 reports wet-lab follow-up; the ultrasound paper pairs simulations with a specific experiment; PRISM uses clinician review but sends no messages. MUSS, Cellina, scTREAT and the other model benchmarks are computational, while the colorectal and MRI studies are retrospective. These are not equivalent forms of validation.

## Open Problems and Research Directions

1. **Replicate agent-generated hypotheses independently.** PharmAgents2 reports three human-executed experiments, but authors say the JAK1 selectivity/binding modes and the LpxH site/mechanism need further validation. Follow-up could preregister blinded concentration-response assays, orthogonal target-engagement tests, off-target panels, and independent-laboratory replication.
2. **Measure portability of single-cell predictions.** MUSS, Cellina, Thalamus-Reasoning, scTREAT, and the imputation benchmark cover diverse tasks, but remain tied to their evaluated datasets and protocols. Freeze models and thresholds, then test unseen donors, labs, cell types, perturbation mechanisms, tissues, and sequencing platforms against independent assays.
3. **Connect protein-design scores to function.** BILBY notes heuristic MD thresholds and finite trajectories, and MD support alone does not establish biochemical activity. A staged follow-up could compare longer matched-reference simulations with experimental folding, binding, or catalytic assays across motif and context classes.
4. **Set governance before genetic recontact.** PRISM is a no-contact dry run and only half of its 30 clinician-reviewed drafts were judged fit to send. Before prospective use, test privacy and consent safeguards, clinician-led escalation, correction channels, and message comprehension in an independently reviewed external cohort.
5. **Test clinical-data portability before use claims.** The colorectal model's AUROC plateau and near-equal XGBoost baseline motivate evaluation across health systems and time periods; MRI harmonization needs independent hospitals and scanners. Prospective utility, subgroup calibration, and patient outcomes remain open.

## Takeaway

This batch's strongest signal is methodological: papers test when predictions survive broader datasets, alternative metrics, physical simulation, or experimental checks. PharmAgents2 reports the clearest wet-lab bridge, while the single-cell and medical-model updates remain computational or retrospective. These preprints do not establish clinical benefit; independent replication and external validation are the next tests.

## Method and sources

- **Window:** Daily, 2026-11-06 only (start 2026-11-06, end 2026-11-06). Snapshot: 2026-11-09 01:20:04 UTC. The latest available announcement batch was Friday, 6 November; Monday's batch was not yet available.
- **Scope:** `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. Computational biology papers cross-listed into these archives were included when clearly relevant; `q-bio.NC` and `q-bio.PE` were excluded absent a material molecular or biomedical focus.
- **Collection:** Traversed latest announcement listings for all configured q-bio archives and `physics.med-ph`; verified selected metadata and abstracts on their arXiv abstract pages. Five revised papers are labeled as revisions and retain their first-submission dates. The `cs.BI` browse path did not resolve, and the broad arXiv API query was rate-limited in this run, so eligible records not cross-listed in the traversed archives may be missing; this is not a complete inventory. HTML full text was reviewed for the three lead papers.
- **Ranking:** Semantic Scholar Graph batch lookup returned current citation totals of 8 for scTREAT and 1 for Thalamus-Reasoning, and 0 for the other 12; influential-citation counts were 0 for all 14. These are current totals, not citations gained in this window, and do not support a measured popularity ranking. Therefore the list is titled “Notable recent papers” and ordered by biological/biomedical relevance, scope and type of reported evidence, benchmark breadth, experimental/clinical-review evidence, venue or journal-reference signals, and revision scope. No downloads or views are inferred.
- **Evidence boundaries:** Experimental, computational, observational, and clinical evidence are distinguished in each entry. The clinical prediction studies are retrospective and do not establish diagnostic performance or patient benefit. Claims are attributed to the authors.
- **Sources:** [q-bio.BM new](https://arxiv.org/list/q-bio.BM/new), [q-bio.GN new](https://arxiv.org/list/q-bio.GN/new), [q-bio.MN new](https://arxiv.org/list/q-bio.MN/new), [q-bio.SC new](https://arxiv.org/list/q-bio.SC/new), [q-bio.CB new](https://arxiv.org/list/q-bio.CB/new), [q-bio.TO new](https://arxiv.org/list/q-bio.TO/new), [q-bio.QM new](https://arxiv.org/list/q-bio.QM/new), [physics.med-ph new](https://arxiv.org/list/physics.med-ph/new); individual arXiv abstract pages are linked above. Citation metadata: [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch?fields=title%2Cauthors%2Cyear%2CcitationCount%2CinfluentialCitationCount%2CreferenceCount%2CpublicationTypes%2CfieldsOfStudy%2CexternalIds).
