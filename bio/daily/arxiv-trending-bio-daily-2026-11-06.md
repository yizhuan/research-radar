# Daily arXiv Biology and Biomedicine — 2026-11-06

## Headline

Friday’s 6 November 2026 arXiv biology/biomedicine batch yielded seven notable papers from 15 eligible announcement records (14 new submissions and one revision). The dominant pattern is biological AI being evaluated against harder benchmarks, with one drug-discovery system reporting human-run experimental follow-up. Spoken agenda: agent-assisted drug discovery, protein design, single-cell genomics, docking, colorectal-risk prediction, MRI harmonization, and intracellular reaction networks. arXiv has no official trending chart; this is an inferred relevance ranking, not a popularity ranking, and arXiv’s biomedical coverage is incomplete.

## Notable recent papers (ranked by relevance)

### 1. [PharmAgents2: Towards Autonomous End-to-End Drug Discovery](https://arxiv.org/abs/2611.07653)
- **Abstract:** PharmAgents2 combines extracted scientific decision knowledge with parallel agents for drug-discovery planning; its authors report three candidate-generation studies followed by human-executed experiments.
- **Authors:** Haichuan Tan, Bowen Gao, Tao Huang, Jiaxin Tan, Xin Hong, Baoguo Yao, Yifei Wang, Zhichao Deng, Hanji Du, Dapeng Jiang, Yiheng Li, Weiwei Ma, Xin Ma, Yuqi Shi, Zixiang Wang, Kelin Wu, Tianxiang Wu, Wenxuan Xie, Jie Zang, Huiyu Zhang, Mojia Zhang, Yuying Zhang, Ya-Qin Zhang, Wei-Ying Ma, Yanyan Lan
- **arXiv:** `2611.07653v1` (published 2026-11-05T08:39:19Z; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Strong direct drug-discovery relevance; the authors report biochemical, cellular, and binding-assay follow-up in three studies. These are contribution and relevance signals, not popularity measures.
- **Claimed contribution:** The authors report a 121-question benchmark and three end-to-end tasks. In follow-up, 63 purchased LpxH candidates yielded an inhibitor with enzyme-inhibition and biophysical binding evidence; 34 JAK1 candidates were tested in cytokine-signalling assays; and SPR supported binding of a proposed secondary target for another molecule.
- **Caveat:** These were experiments executed by human researchers, not autonomous lab work. The paper says the proposed LpxH site and mechanism remain under validation; the findings do not establish therapeutic efficacy, safety, or clinical utility.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** Biomedical & translational medicine; Biochemistry & proteins

### 2. [Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding](https://arxiv.org/abs/2611.07723)
- **Abstract:** BILBY adds a PROSITE-derived motif-scaffolding benchmark and molecular-dynamics checks to test whether static protein-motif recovery corresponds to dynamical stability.
- **Authors:** Emile de Bruyn, Moritz Schäffler, Jannik Schneider, Sebastian R. Schmidt, Chanwoong Hwang, Aleena Siji, Utkarsh Upadhyay, Stefan Bauer, Alexander Schug, Stefan Kesselheim, Artur Yakimovich, Alina Bazarova
- **arXiv:** `2611.07723v1` (published 2026-11-05T09:38:23Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Accepted at NeurIPS 2026 (Evaluations & Datasets Track); reports a 220-case benchmark and a dynamics evaluation on 55 statically solved model–problem pairs.
- **Claimed contribution:** The authors introduce BILBY-PRO (220 cases from 174 PROSITE motif-pattern entries) and BILBY-MD. Of 55 statically solved pairs assessed with MD, 31 met the authors’ MD-supported criterion and 8 passed all checks; they argue static refolding does not establish full-scaffold dynamical fidelity.
- **Caveat:** The MD-support thresholds are heuristic, and the 200 ns design trajectories may miss slower instabilities. The dynamics evaluation is computational, not experimental functional validation.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation](https://arxiv.org/abs/2611.08086)
- **Abstract:** MUSS integrates DNA-sequence representations with chromatin accessibility and paired single-cell expression data to model gene regulation across sequence and cell scales.
- **Authors:** Kangjie Zheng, Amirhossein Vahidi, Liying Jin, Joseph Clarke, Vijaya Baskar MS, Connor Rogerson, Mengji Zhang, Muzlifah Haniffa, Anshul Kundaje, Mo Lotfollahi
- **arXiv:** `2611.08086v1` (published 2026-11-05T14:34:07Z; categories: `cs.AI`, `q-bio.GN`)
- **Evidence for ranking:** Direct genomics fit and a `q-bio.GN` cross-list; the arXiv record gives NeurIPS 2026 as the publication venue. The paper evaluates across four paired single-cell datasets and several task types.
- **Claimed contribution:** The authors report competitive or leading results against sequence and single-cell baselines for expression prediction, enhancer–gene linking, motif-guided prioritization, and zero-shot cell clustering, including tests on unseen genes and peaks.
- **Caveat:** Results are computational, not causal or experimental validation. The authors note reliance on a frozen sequence encoder and paired multi-omic data, quadratic attention cost, and single-run estimates for some expression outcomes.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Omics & single-cell methods

### 4. [Geometric Relevance Is Not Sufficient: Evaluating Focused Post-Training Supervision in Diffusion Docking](https://arxiv.org/abs/2611.08249)
- **Abstract:** A fixed-budget DiffDock study compares broad continuation with focused torsional supervision and finds no consistent advantage for the focused strategies on the reported docking endpoints.
- **Authors:** Michael Brown, Maryam Rahimimovassagh, Mehdi Yazdani-Jahromi, Sanjeda Sara Jennifer, Ivan Garibay
- **arXiv:** `2611.08249v1` (published 2026-11-05T16:26:44Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Direct molecular-docking relevance; accepted at the NeurIPS 2026 AI4DD Workshop. The study separates score fidelity, generated-pose recovery, best-of-10 sampling, and confidence-selected Top-1 performance.
- **Claimed contribution:** In the authors’ 99-complex evaluation with three training seeds, broad continuation had the highest mean trained-policy Top-1 success below 5 Å; focused or mixed supervision did not consistently improve on broad continuation within the tested budget.
- **Caveat:** This is a computational result for one architecture, one test set, a five-epoch budget, and one sampling seed. The authors note that confidence selection and physical/external confirmation remain unresolved.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 5. [How Deep is the Signal? Time-Context up to 30 Years for Colorectal Cancer Prediction in a Primary-Care EHR Model](https://arxiv.org/abs/2611.07265)
- **Abstract:** This study tests how far back a primary-care EHR model needs to look to predict incident colorectal cancer, using nested calendar-time lookback windows.
- **Authors:** Achille Raviez, Lan Wang, Brendan Delaney
- **arXiv:** `2611.07265v1` (published 2026-11-05T00:34:47Z; categories: `cs.LG`, `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Accepted at Machine Learning for Health 2026 (Findings Track); the authors evaluate a frozen cohort of 1,008 cases and 9,582 matched controls after pretraining on 3.6 million primary-care patients.
- **Claimed contribution:** The authors report AUROC rising from 0.551 with a two-year lookback to 0.590 at 18 years before plateauing; XGBoost reached a similar peak of 0.589. They propose calendar-time context as a distinct design variable for EHR models.
- **Caveat:** This is a retrospective prediction study in one North West London health system, with modest discrimination and no prospective or clinical-utility evaluation. It is not evidence of a validated screening test.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 6. [Resampling-based batch reweighting for ComBat harmonization of MRI radiomic features in a multi-scanner glioma cohort](https://arxiv.org/abs/2611.02156)
- **Abstract:** A revised study tests whether reweighting underrepresented scanner batches before ComBat estimation reduces residual scanner effects in glioma MRI radiomic features.
- **Authors:** Rifa Sajda Tasnim, Yushuf Sharker, Md Forhad Hossain, Rakibur Rahman, Enamul Hoque Bhuiyan
- **arXiv:** `2611.02156v2` (published 2026-11-01T19:43:22Z; updated 2026-11-05T13:40:38Z; categories: `eess.IV`, `physics.med-ph`)
- **Evidence for ranking:** Substantive v2 revision in the latest announcement batch; direct medical-imaging relevance. The arXiv record says the article was submitted to the Journal of Magnetic Resonance Imaging.
- **Claimed contribution:** In a retrospective, single-centre Erasmus Glioma Database cohort of 733 patients across nine scanner configurations, the authors report that batch-augmented ComBat reduced features with significant residual scanner association from 13/428 with standard ComBat to 8/428.
- **Caveat:** This remains a single-centre radiomics harmonization analysis; the reported reduction does not establish external generalization or improved patient outcomes.
- **Announcement type:** revision, 2026-11-06 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 7. [Accelerating reaction network identification via frequency-domain analysis](https://arxiv.org/abs/2611.07684)
- **Abstract:** The authors report that Fourier-domain measurements can make likelihoods approximately Gaussian in some intracellular reaction systems, enabling faster Bayesian network inference in an illustrative transcription example.
- **Authors:** Zhou Fang, Wenying Sun, Xiaoyu Zhang, Mustafa Khammash
- **arXiv:** `2611.07684v1` (published 2026-11-05T09:11:41Z; categories: `q-bio.MN`)
- **Evidence for ranking:** Primary category `q-bio.MN` and direct relevance to intracellular reaction-network inference; the abstract describes an illustrative gene-transcription example.
- **Claimed contribution:** The authors identify a condition under which a Fourier transform approximately Gaussianizes the measurement likelihood and use it to construct an accelerated Bayesian inference algorithm.
- **Caveat:** The abstract reports one illustrative example, not broad experimental validation; the approximation is stated to apply only to certain systems.
- **Announcement type:** new submission, 2026-11-06 batch
- **Themes:** Molecular & cell biology; Quantitative methods

## Trending Research Themes

- **Evaluation beyond a single proxy:** BILBY separates static motif recovery from MD-supported dynamics; the docking study separately evaluates score fidelity, pose recovery, and confidence-selected ranking. These are methodological findings in two selected papers, not proof of a field-wide shift.
- **AI models that connect biological scales:** MUSS links DNA sequence to cell-specific chromatin and expression, while PharmAgents2 organizes decisions across drug-discovery workflows. Both are computational systems; only PharmAgents2 reports human-run experimental follow-up.
- **Prediction in real clinical data and imaging pipelines:** The colorectal EHR paper studies long calendar-time context, and the glioma MRI revision studies scanner-batch harmonization. Neither reports prospective clinical utility; the MRI study is a single-centre retrospective analysis.
- **Mechanistic inference remains model-dependent:** The reaction-network paper uses one transcription example to illustrate a frequency-domain approximation; broader biological validation is still needed.

## Open Problems and Research Directions

- **Replicate agent-generated findings and resolve mechanisms:** PharmAgents2 reports experimental activity and binding for candidate compounds, while its LpxH site/mechanism remains under validation. Independent, blinded replication and orthogonal target-engagement or mutational studies could test those claims; broader selectivity and pharmacology panels would be needed before any therapeutic inference.
- **Connect protein-design benchmarks to function:** BILBY shows that static structural recovery is not equivalent to simulated dynamical support. Longer or replicated trajectories and experimental stability/activity assays on a preselected subset could test how these computational criteria relate to function.
- **Test genomic models beyond benchmark datasets:** MUSS could be assessed on independent tissues, assays, and held-out regulatory elements, followed by perturbation experiments for prespecified enhancer–gene predictions. This would address generalization and causal evidence separately.
- **Evaluate clinical models externally:** The EHR and MRI papers motivate temporal/geographic cohort validation for colorectal prediction and scanner/site validation for radiomics harmonization. Prospective utility and patient outcomes remain untested in these reports.
- **Stress-test reaction-network assumptions:** Compare the frequency-domain inference method against particle-filtering and independent measurements across reaction topologies, noise levels, and additional cell systems before generalizing beyond the transcription example.

## Takeaway

The batch’s clearest contribution is methodological: biological AI systems need evaluation against dynamic, held-out, or externally measured outcomes, not only convenient proxy metrics. PharmAgents2 provides the strongest translational bridge in this selection because it reports human-executed assays, but these are early discovery findings—not clinical validation. The other papers are computational or retrospective studies whose claims remain bounded by their datasets and validation designs.

## Method and sources

- **Window:** daily announcement batch dated 2026-11-06 (Friday). The current date, 2026-11-08, has no newer announcement batch, so this uses the most recent prior batch. Announcement window: 2026-11-06 through 2026-11-06. New submissions were first submitted on 2026-11-05 UTC; the included revision was updated on 2026-11-05. Snapshot: 2026-11-08 01:19:00 UTC.
- **Candidate query:** arXiv API query over `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`, sorted by submitted date. The first 200 results included all 14 new-submission records dated 2026-11-05 and extended back to 2026-10-21; version metadata added one eligible revision, `2611.02156v2`. All 15 eligible announcement records’ abstract pages were checked; the seven selected papers’ versions, authors, categories, and metadata were verified. The top three papers were read in full-text HTML for methods, results, and limitations/caveats.
- **Ranking:** Papers are ordered by relevance to molecular biology and biomedicine and strength/type of reported evidence, using venue/status or substantive revision as checkable supporting signals where present. No numeric trend score is assigned.
- **Coverage:** This is not a comprehensive survey of biomedical research. Many clinical and experimental biology preprints appear on bioRxiv or medRxiv, and purely computational/retrospective results here are not practice-changing evidence.
- **Sources:** [arXiv quantitative biology new listings](https://arxiv.org/list/q-bio/new); [category query](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200); [PharmAgents2](https://arxiv.org/abs/2611.07653); [BILBY](https://arxiv.org/abs/2611.07723); [MUSS](https://arxiv.org/abs/2611.08086); [DiffDock post-training](https://arxiv.org/abs/2611.08249); [colorectal EHR model](https://arxiv.org/abs/2611.07265); [MRI harmonization revision](https://arxiv.org/abs/2611.02156); [reaction-network inference](https://arxiv.org/abs/2611.07684).
