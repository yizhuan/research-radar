# Daily arXiv Biology and Biomedicine — 2026-11-06

## Headline

The latest arXiv biology and biomedicine announcement batch, Friday 6 November 2026, contributes 10 notable papers selected from 22 eligible records (14 new submissions and 8 revisions). Single-cell genomics and computational discovery dominate, alongside protein-model evaluation and retrospective clinical prediction. Spoken agenda: drug-discovery agents, gene regulation, single-cell benchmarks, tissue and drug-response prediction, protein scaffolding, docking, and EHR/imaging methods. This is an inferred relevance ranking, not a popularity chart: arXiv has no official trending chart, and its biomedical coverage is incomplete. Sunday 8 November had no newer batch.

## Notable recent papers (ranked by relevance)

### 1. [PharmAgents2: Towards Autonomous End-to-End Drug Discovery](https://arxiv.org/abs/2611.07653)
- **Abstract:** PharmAgents2 combines literature-derived decision skills and parallel agents for drug-discovery investigations; the authors report three investigations with findings subsequently tested in human-executed experiments.
- **Authors:** Haichuan Tan, Bowen Gao, Tao Huang, Jiaxin Tan, Xin Hong, Baoguo Yao, Yifei Wang, Zhichao Deng, Hanji Du, Dapeng Jiang, Yiheng Li, Weiwei Ma, Xin Ma, Yuqi Shi, Zixiang Wang, Kelin Wu, Tianxiang Wu, Wenxuan Xie, Jie Zang, Huiyu Zhang, Mojia Zhang, Yuying Zhang, Ya-Qin Zhang, Wei-Ying Ma, Yanyan Lan
- **arXiv:** `2611.07653v1` (published 2026-11-05T08:39:19Z; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Direct drug-discovery relevance and three author-reported experimental follow-ups; these support relevance, not measured popularity.
- **Claimed contribution:** The authors introduce a 121-question benchmark and three end-to-end tasks. They report experimental follow-up for an LpxH inhibitor scaffold, JAK1 inhibitor candidates, and a proposed secondary target for a known bioactive molecule.
- **Caveat:** Human researchers performed the experiments. The findings concern early discovery assays and do not establish clinical efficacy, safety, or therapeutic utility.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** Biomedical & translational medicine; Biochemistry & proteins

### 2. [MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation](https://arxiv.org/abs/2611.08086)
- **Abstract:** MUSS joins DNA-sequence-derived representations with chromatin accessibility and paired single-cell expression data to model gene regulation across scales.
- **Authors:** Kangjie Zheng, Amirhossein Vahidi, Liying Jin, Joseph Clarke, Vijaya Baskar MS, Connor Rogerson, Mengji Zhang, Muzlifah Haniffa, Anshul Kundaje, Mo Lotfollahi
- **arXiv:** `2611.08086v1` (published 2026-11-05T14:34:07Z; categories: `cs.AI`, `q-bio.GN`)
- **Evidence for ranking:** Direct genomics fit; the arXiv record lists NeurIPS 2026. The paper evaluates four paired single-cell datasets and several downstream tasks.
- **Claimed contribution:** The authors report performance against sequence and single-cell baselines for expression prediction, enhancer–gene linking, motif-guided prioritization, and zero-shot clustering, including tests involving unseen genes and peaks.
- **Caveat:** Results are computational, not causal evidence. The authors note dependence on a frozen sequence encoder and paired multi-omic data, quadratic attention cost, and limitations in unseen-link evaluation.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Omics & single-cell methods

### 3. [Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding](https://arxiv.org/abs/2611.07723)
- **Abstract:** BILBY adds a PROSITE-derived protein-motif benchmark and molecular-dynamics checks to test whether static motif recovery predicts dynamic scaffold behavior.
- **Authors:** Emile de Bruyn, Moritz Schäffler, Jannik Schneider, Sebastian R. Schmidt, Chanwoong Hwang, Aleena Siji, Utkarsh Upadhyay, Stefan Bauer, Alexander Schug, Stefan Kesselheim, Artur Yakimovich, Alina Bazarova
- **arXiv:** `2611.07723v1` (published 2026-11-05T09:38:23Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Accepted at NeurIPS 2026 (Evaluations & Datasets Track); reports a 220-case benchmark and molecular-dynamics assessment of 55 statically solved model–problem pairs.
- **Claimed contribution:** The authors report that 31/55 designs met their MD-supported criterion and 8/55 passed all checks, indicating that static refolding does not establish full-scaffold dynamical fidelity.
- **Caveat:** The MD thresholds are heuristic; 200 ns design trajectories may miss slower instabilities. The study is computational and does not establish biochemical function.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 4. [One Method Does Not Fit All: A Large-Scale Benchmark of Imputation Methods for Single-Cell RNA Sequencing Data](https://arxiv.org/abs/2603.24626)
- **Abstract:** This revised benchmark compares 16 single-cell RNA-seq imputation methods across protocols, downstream tasks, and datasets, finding that rankings depend on the task and data.
- **Authors:** Yuichiro Iwashita, Ahtisham Fazeel Abbasi, Koichi Kise, Andreas Dengel, Muhammad Nabeel Asim
- **arXiv:** `2603.24626v3` (published 2026-03-25T02:46:51Z; updated 2026-11-05T14:26:36Z; categories: `q-bio.GN`, `cs.LG`, `stat.ML`)
- **Evidence for ranking:** v3 revision in the batch; broad evaluation across 16 methods, 10 protocols, 6 downstream tasks, and 30 benchmark datasets.
- **Claimed contribution:** The authors report that traditional methods are often more consistent across tasks, while strong numerical recovery does not necessarily improve downstream biological interpretation.
- **Caveat:** Benchmark outcomes depend on dataset, protocol, and analytical goal; the authors find no universally best method. The conclusions are comparative, not a demonstration that imputation recovers true expression in every setting.
- **Announcement type:** revision, 2026-11-06 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 5. [Querying Counterfactuals on Tissue Graphs with Supervised Disentanglement](https://arxiv.org/abs/2606.08493)
- **Abstract:** Cellina models in-silico tissue-neighborhood interventions by separating a cell’s intrinsic state from its spatial context.
- **Authors:** Abdul Moeed, Stefan Schrod, Martin Rohbeck, Marc Jan Bonder, Pavlo Lutsik, Oliver Stegle, Daniel Dimitrov
- **arXiv:** `2606.08493v4` (published 2026-06-07T07:41:00Z; updated 2026-11-05T09:36:28Z; categories: `q-bio.GN`, `cs.LG`, `stat.ML`)
- **Evidence for ranking:** v4 revision in the batch; evaluated in observational and interventional screens spanning more than 2.5 million spatially resolved cells.
- **Claimed contribution:** The authors report stronger in-silico perturbation predictions than spatial and non-spatial competitors and use the model to identify cancer subdomains with distinct predicted signaling programs.
- **Caveat:** Counterfactual outputs are model predictions, not newly performed interventions; performance across the reported benchmarks does not establish causal validity in other tissues.
- **Announcement type:** revision, 2026-11-06 batch
- **Themes:** Molecular & cell biology; Omics & single-cell methods; Quantitative methods

### 6. [Thalamus-Reasoning: A Multimodal Large Language Model for Multi-Sample Omics Reasoning](https://arxiv.org/abs/2605.06728)
- **Abstract:** Thalamus-Reasoning represents bulk or single-cell transcriptomes as continuous embeddings that can be combined with language instructions and other samples.
- **Authors:** Maciej Sypetkowski, Łukasz Smoliński, Remigiusz Kinas, Joanna Krawczyk, Bartłomiej Hofman, Aleksandra Możwiłło, Michał Pikusa, Tomasz Jetka, Rafał Powalski
- **arXiv:** `2605.06728v3` (published 2026-05-07T11:27:11Z; updated 2026-11-05T15:18:38Z; categories: `q-bio.GN`, `cs.AI`, `q-bio.CB`)
- **Evidence for ranking:** v3 revision in the batch; includes GEO-OmicsQA, a publication-disjoint benchmark of 3,000 questions, and evaluations on held-out annotation and perturbation-response tasks.
- **Claimed contribution:** The authors report leading results among tested models on multiple held-out annotation tasks and GEO-OmicsQA variants, and better average performance on PerturbQA than the compared methods.
- **Caveat:** The benchmark measures model performance on curated tasks, not experimental discovery. Some training supervision is LLM-generated with task-specific quality checks; no new biological experiments are reported.
- **Announcement type:** revision, 2026-11-06 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Bioinformatics & sequence analysis

### 7. [scTREAT: Latent Diffusion for Single-Cell Drug-Response Prediction](https://arxiv.org/abs/2510.11726)
- **Abstract:** scTREAT uses latent diffusion with explicit cell-state, drug-identity, and dose conditioning to predict single-cell drug-response profiles.
- **Authors:** Zhaokang Liang, Shuyang Zhuang, Xiaoran Jiao, Weian Mao, Hao Chen, Chunhua Shen
- **arXiv:** `2510.11726v3` (published 2025-10-08T16:17:39Z; updated 2026-11-05T09:23:34Z; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** v3 revision in the batch; evaluated on condition-level pseudobulk profiles from the Tahoe-100M atlas for unseen cell-line–drug combinations and unseen drugs.
- **Claimed contribution:** The authors report best scores on 10/12 metrics for unseen combinations and 11/12 for unseen drugs among the compared methods.
- **Caveat:** The benchmark is computational and uses condition-level pseudobulk profiles; predicted responses need independent experimental validation and should not be treated as treatment evidence.
- **Announcement type:** revision, 2026-11-06 batch
- **Themes:** RNA & transcriptomics; Biomedical & translational medicine; Quantitative methods

### 8. [How Deep is the Signal? Time-Context up to 30 Years for Colorectal Cancer Prediction in a Primary-Care EHR Model](https://arxiv.org/abs/2611.07265)
- **Abstract:** This study tests how far back a primary-care EHR model needs to look to predict incident colorectal cancer using nested calendar-time windows.
- **Authors:** Achille Raviez, Lan Wang, Brendan Delaney
- **arXiv:** `2611.07265v1` (published 2026-11-05T00:34:47Z; categories: `cs.LG`, `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Accepted at Machine Learning for Health 2026 (Findings Track); evaluates a frozen cohort of 1,008 cases and 9,582 matched controls, after pretraining on 3.6 million primary-care patients.
- **Claimed contribution:** The authors report AUROC rising from 0.551 at a two-year lookback to 0.590 at 18 years before plateauing; XGBoost reached a similar peak of 0.589.
- **Caveat:** Retrospective prediction in one North West London health system with modest discrimination; no prospective utility is shown, so this is not a validated screening test.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 9. [Resampling-based batch reweighting for ComBat harmonization of MRI radiomic features in a multi-scanner glioma cohort](https://arxiv.org/abs/2611.02156)
- **Abstract:** This revised MRI study tests whether reweighting underrepresented scanner batches before ComBat estimation reduces residual scanner effects in glioma radiomic features.
- **Authors:** Rifa Sajda Tasnim, Yushuf Sharker, Md Forhad Hossain, Rakibur Rahman, Enamul Hoque Bhuiyan
- **arXiv:** `2611.02156v2` (published 2026-11-01T19:43:22Z; updated 2026-11-05T13:40:38Z; categories: `eess.IV`, `physics.med-ph`)
- **Evidence for ranking:** v2 revision in the batch; retrospective Erasmus Glioma Database cohort of 733 patients, one center, nine scanner configurations; arXiv comments say submitted to JMRI.
- **Claimed contribution:** The authors report significant residual scanner association in 13/428 features after standard ComBat versus 8/428 after batch-augmented ComBat.
- **Caveat:** Single-center radiomics harmonization; reduced scanner association does not establish external generalization or improved patient outcomes.
- **Announcement type:** revision, 2026-11-06 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 10. [Geometric Relevance Is Not Sufficient: Evaluating Focused Post-Training Supervision in Diffusion Docking](https://arxiv.org/abs/2611.08249)
- **Abstract:** A fixed-budget DiffDock study compares broad continuation with focused torsional supervision and finds no consistent advantage for focused strategies on its reported docking endpoints.
- **Authors:** Michael Brown, Maryam Rahimimovassagh, Mehdi Yazdani-Jahromi, Sanjeda Sara Jennifer, Ivan Garibay
- **arXiv:** `2611.08249v1` (published 2026-11-05T16:26:44Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Direct molecular-docking relevance; accepted at the NeurIPS 2026 AI4DD Workshop. Evaluation separates score fidelity, generated-pose quality, best-of-10 sampling, and confidence-selected Top-1 performance.
- **Claimed contribution:** The authors report that broad continuation had the highest mean trained-policy Top-1 success below 5 Å; focused or mixed supervision did not consistently improve success under the tested budget.
- **Caveat:** This is a computational result for DiffDock under one fixed training budget; it does not establish improved docking in prospective or experimental settings.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

## Trending Research Themes

- **Single-cell genomics meets learned representations:** MUSS, Cellina, Thalamus-Reasoning, scTREAT, and the imputation benchmark all model or evaluate links among expression, regulatory context, or drug response. Their tasks and validation differ; most outputs are predictive rather than causal.
- **Evaluation is becoming more task- and context-specific within this batch:** The imputation benchmark spans 30 datasets and six tasks; BILBY tests molecular dynamics beyond static recovery; the docking paper separates pose quality from score fidelity; and the EHR study varies calendar-time context. These examples do not establish a field-wide shift.
- **Computational discovery paired with downstream checks:** PharmAgents2 reports human-run biochemical, cellular, and binding assays. By contrast, MUSS, Cellina, Thalamus-Reasoning, scTREAT, and docking primarily report computational benchmarks; they should not be described as experimentally validated biology.
- **Clinical prediction and imaging remain retrospective:** The colorectal EHR analysis is from one health system, and the MRI harmonization study is from one center. Neither demonstrates prospective clinical utility.

## Open Problems and Research Directions

- **Test predicted biology experimentally:** For MUSS enhancer–gene links, Cellina tissue-neighborhood counterfactuals, and scTREAT drug responses, pre-register predictions and test them with perturbation assays across independent cell types. Separate agreement with expression benchmarks from causal evidence.
- **Establish robustness beyond the training and benchmark settings:** Extend the scRNA-seq imputation comparisons and Thalamus-Reasoning evaluations to additional protocols, tissues, and independent cohorts; report uncertainty and task-specific errors rather than a single aggregate score.
- **Replicate agent-generated chemistry:** PharmAgents2 reports three human-executed experimental follow-ups. Independent, blinded replication, orthogonal target-engagement assays, and selectivity/toxicity panels would help determine which findings persist; none would by itself establish clinical benefit.
- **Validate clinical-data pipelines externally:** Test colorectal prediction across health systems and time periods, and MRI harmonization across independent hospitals and scanners. Prospective utility, calibration, and patient outcomes remain open.
- **Tie structural benchmarks to function:** BILBY motivates longer or replicated dynamics simulations and biochemical activity/stability assays for selected designs, since the reported MD support is not equivalent to experimental function.

## Takeaway

This batch is notable for how many papers make evaluation design central: results vary by cell type, task, dataset, temporal context, or physical criterion. PharmAgents2 provides the clearest experimental bridge, but only at early discovery-assay level. The rest are computational or retrospective findings, and the list is ranked by relevance rather than measured attention.

## Method and sources

- **Window:** Daily announcement batch dated 2026-11-06 (Friday), the latest batch available on 2026-11-08; no Sunday batch. Exact announcement window: 2026-11-06 through 2026-11-06. The new submissions and revisions included here were submitted or updated on 2026-11-05 UTC. Snapshot: 2026-11-08T17:13:04Z.
- **Candidate pool:** The configured categories were `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. The descending submitted-date query returned 200 records and extended through 2026-10-21; a second descending last-updated-date query returned 200 records and extended through 2026-10-28. Together these captured 14 first submissions and 8 revisions dated 2026-11-05. Selected papers were checked on their arXiv abstract pages; the three lead papers were also read in PDF text for methods, results, and limitations.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`. Results were sorted by submitted date and last-updated date, descending, with `max_results=200`.
- **Ranking:** Attention evidence is sparse, so the papers are labeled notable recent papers and ordered by biological/biomedical relevance and the scope/type of reported evidence. Semantic Scholar citation counts for the newest submissions were zero at this snapshot; venue status and revision status are stated where present. No downloads or views are inferred.
- **Coverage:** arXiv is an incomplete biomedical index; many clinical and experimental biology preprints appear on bioRxiv or medRxiv. This is not a systematic review or clinical evidence assessment.
- **Sources:** [arXiv q-bio.BM recent listings](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), [physics.med-ph](https://arxiv.org/list/physics.med-ph/recent); arXiv API query over the categories above; Semantic Scholar Graph API metadata queried for citation corroboration. Individual arXiv abstract links are provided in each entry.
