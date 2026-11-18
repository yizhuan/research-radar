# arXiv Biology and Biomedicine — Daily, 2026-11-17

## Headline
The latest batch available today is dated 17 November 2026. Its configured category listings show 43 appearances, deduplicated to 40 arXiv IDs; 10 notable papers are selected below. The strongest recurring pattern is computational methods tied to biological measurements: antibody engineering and assay interpretation, transcriptome prediction, and spatial multi-omics. Spoken agenda: what the antibody campaigns learned about measuring molecules, where transcriptome models generalize, and what spatial omics methods still need. arXiv has no official trending chart; this is an inferred relevance ranking from an incomplete biomedical corpus, not a popularity ranking.

## Notable recent papers

### 1. [Reasoning in the loop: antibody lead optimization by probing mechanism and measurement](https://arxiv.org/abs/2611.19812)
- **Abstract:** Two antibody lead-optimization campaigns combine human researchers, a general-purpose AI agent, and assay-specific biophysical reasoning to improve leads while revising misleading thermal metrics.
- **Authors:** Samuel Stanton, Aaron Solomon, Emily Delaney, Melanie Montgomery, Crystal Humphries, Timothy Acker, Ryan Henrici, Charbel Eid, Eddie Abrams, Peyton Greenside
- **arXiv:** `2611.19812v1` (published 2026-11-15T05:55:18Z; categories: `cs.LG`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** Strong direct fit to protein engineering; the authors report two assay campaigns, seven rounds and about 1,010 variants, with perturbation tests of revised measurements.
- **Claimed contribution:** The authors report improved affinity and stability for an anti-albumin VHH and an anti-mesothelin scFv after reinterpreting scaffold-specific thermal assay signals.
- **Caveat:** The leads' key measurements rely on one or two replicates; the authors call for confirmation, higher-sensitivity affinity measurements, and further aggregation and stress testing.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine

### 2. [In-context learning predicts clinical endpoints from bulk transcriptomes across diseases and platforms](https://arxiv.org/abs/2611.18774)
- **Abstract:** PRTS uses labelled cohort examples as context to predict clinical or phenotypic outcomes from bulk RNA profiles without per-cohort training.
- **Authors:** Han Wang, Lennart Purucker, Huafeng Liu, Ziyin Luo, Junfeng Hao, Chao Zhu, Chunjie Tian
- **arXiv:** `2611.18774v1` (published 2026-11-12T10:17:13Z; categories: `q-bio.GN`)
- **Evidence for ranking:** Strong RNA/translational relevance; the paper evaluates 175 held-out RealBulk tasks and 44 TCGA tasks, and reports a 220-million-parameter model trained on six million generated tasks.
- **Claimed contribution:** The authors report a small mean-accuracy lead over their strongest pre-specified comparator, driven mainly by within-cohort prediction and TCGA survival tasks.
- **Caveat:** Across cohorts and unseen sites the model is level with the strongest comparator; retrospective benchmark results do not establish prospective clinical utility. The paper also documents a correction to earlier comparator gene selection.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** RNA & transcriptomics; Biomedical & translational medicine; Quantitative methods

### 3. [multiCAsp: Spatially Informed Canonical Association Analysis of Multi-Omic Data](https://arxiv.org/abs/2611.20580)
- **Abstract:** multiCAsp integrates spatially resolved molecular modalities by imposing a graph-Laplacian prior on shared latent factors.
- **Authors:** Ziqi Mu, Qiuyi Wu, Zhicheng Ji, Pixu Shi
- **arXiv:** `2611.20580v1` (published 2026-11-16T06:04:03Z; categories: `stat.ME`, `q-bio.QM`)
- **Evidence for ranking:** Direct multi-omics relevance; authors compare against three methods in simulations and analyze macaque cortex metabolomics/proteomics and human renal-carcinoma gene/protein data.
- **Claimed contribution:** The authors report stronger latent-factor and loading recovery in their tested simulations, plus spatially coherent factors and cross-modal prediction in the two real datasets.
- **Caveat:** Real-data demonstrations cover only two datasets; dense loadings, factor-dimension choices, and modality-specific PCA truncation complicate interpretation and generalization.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** Omics & single-cell methods; Quantitative methods

### 4. [Multi-Assay Antibody Developability Prediction with Shared Structure-Language Representations](https://arxiv.org/abs/2611.18846)
- **Abstract:** MADM combines per-residue structural descriptors, protein-language-model embeddings, and multi-assay training to predict antibody developability measurements.
- **Authors:** Daria B. Kokh
- **arXiv:** `2611.18846v1` (published 2026-11-13T19:04:39Z; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** Direct biochemistry relevance and cross-listing; the authors report evaluation across eight assays built from 29 open data sources, plus separate antibody panels.
- **Claimed contribution:** The authors report that combining structural and sequence representations gives modest accuracy gains, while multi-assay training helps on correlated assays.
- **Caveat:** Performance falls on the 80-antibody GDPa3 hold-out, and assay/source-specific measurement calibration can be entangled with sequence generalization.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 5. [From Mutation to Medication: Characterizing Failures of Clinical LLMs to Respect Genomic Resistance](https://arxiv.org/abs/2611.19339)
- **Abstract:** The authors audit whether language models endorse cancer therapies despite curated genomic evidence of resistance.
- **Authors:** Negin Ashrafi, Roxana Daneshjou
- **arXiv:** `2611.19339v1` (published 2026-11-14T11:26:01Z; categories: `cs.AI`, `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Strong genomics/oncology relevance; the study tests ten models against 1,464 curated resistance cases drawn from five knowledge bases.
- **Claimed contribution:** The authors report that apparent resistance failures vary by evidence strength and source, and that supplying correct curated evidence reduced unqualified strong recommendations in an oracle-style test.
- **Caveat:** Matched-group analysis is described as exploratory and was specified after the pre-registered analysis; curated cases and oracle-provided evidence do not reproduce real clinical retrieval or decision workflows.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** DNA & genomics; Biomedical & translational medicine

### 6. [From the possible to the optimal: differentiable optimization of gene regulatory networks](https://arxiv.org/abs/2611.20172)
- **Abstract:** jaxgrn combines differentiable programming and stochastic simulation to optimize gene-regulatory networks against biological-function constraints.
- **Authors:** Leah Friedman, Gašper Tkačik, Thomas Gregor, Paul François
- **arXiv:** `2611.20172v1` (published 2026-11-15T18:19:52Z; categories: `q-bio.MN`, `q-bio.QM`)
- **Evidence for ranking:** Direct molecular-network relevance and cross-listing; the authors describe GPU optimization of thousands of networks in embryonic-patterning case studies.
- **Claimed contribution:** The authors report recurring optimal network regimes as constraints on pattern formation and positional information change.
- **Caveat:** Findings are from mathematical modeling and stochastic simulations, not experiments demonstrating that the inferred architectures occur in embryos.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** Gene regulation & epigenetics; Quantitative methods

### 7. [Calpha: Toward Native Biomolecular Intelligence in a General-Purpose Language Model](https://arxiv.org/abs/2611.20986)
- **Abstract:** Calpha routes a language model's residue representations into a pretrained structure head to generate single-chain protein structures.
- **Authors:** Yong Liu, Zhanpeng Shi, Peicong Lin, Zhenyi Zhong, Yizhou Dang, Wendi Wu, Haoling Li, Shuangjia Zheng
- **arXiv:** `2611.20986v1` (published 2026-11-16T12:17:37Z; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** Protein-structure relevance; the authors report TM-score evaluations on FoldBench-334, CASP16 domains, and a CAMEO-style PDB set.
- **Claimed contribution:** The authors show a general-purpose LLM can emit single-chain structures from its own residue states, while explicitly leaving complex prediction and structure understanding for future work.
- **Caveat:** Comparisons differ in trainable weights, training duration, and crop length; the paper reports lower scores for longer chains and reduced accuracy on its evaluated language benchmark subset.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 8. [Arginine metabolism drives tumor immune escape by shaping an immunosuppressive microenvironment](https://arxiv.org/abs/2611.19270)
- **Abstract:** A calibrated mathematical model examines how arginine metabolism and macrophage polarization may shape tumor-immune dynamics.
- **Authors:** Chenghang Li, Haifeng Zhang, Yipu Qu, Jinzhi Lei
- **arXiv:** `2611.19270v1` (published 2026-11-14T08:58:25Z; categories: `q-bio.TO`)
- **Evidence for ranking:** Direct molecular-medicine relevance; the model is calibrated against tumor-growth data from three mouse cohorts.
- **Claimed contribution:** The authors' simulations predict tumor-growth effects of arginine administration and possible synergy between arginine depletion and checkpoint blockade.
- **Caveat:** These are model-based predictions, not reported intervention experiments or evidence of treatment benefit in animals or people.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 9. [Beyond AUC: Do Mammography Risk Models Predict When Cancer Occurs?](https://arxiv.org/abs/2611.20274)
- **Abstract:** The paper tests whether longitudinal mammography risk metrics capture time-to-diagnosis and proposes a two-stage model separating whether from when cancer occurs.
- **Authors:** Svetlana Krasnova, Andrey Krylov, Dmitry Sorokin
- **arXiv:** `2611.20274v1` (published 2026-11-15T22:08:11Z; categories: `q-bio.QM`, `cs.CV`, `eess.IV`)
- **Evidence for ranking:** Direct biomedical-imaging relevance and cross-listing; the authors re-evaluate two models on a five-year CSAW-CC setting using timing-specific metrics.
- **Claimed contribution:** The authors report that a proposed two-stage model matches LMV-Net's discrimination while improving the ranking of cancer cases by time to diagnosis in this evaluation.
- **Caveat:** This is a retrospective dataset analysis; timing performance and generalization require validation on independent cohorts and clinical settings.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 10. [Scaling large language model-assisted line-of-therapy adjudication with human-in-the-loop evidence-calibrated selection](https://arxiv.org/abs/2611.20259)
- **Abstract:** Evidence-calibrated selection prioritizes oncology treatment histories for clinician review while feeding confirmed adjudications back into model-assisted line-of-therapy assignment.
- **Authors:** Olatunji Oni, Sanhita Sengupta, Marc De Benedetti, Nathanial Eddy
- **arXiv:** `2611.20259v1` (published 2026-11-15T21:32:18Z; categories: `cs.LG`, `q-bio.QM`, `stat.AP`)
- **Evidence for ranking:** Oncology data-methods relevance; the authors report simulations based on 136 clinician-adjudicated multiple-myeloma patients.
- **Claimed contribution:** In the reported simulation, reviewing 44.6% of patients yielded 5% residual error, versus 62.2% for LLM-confidence-directed review and 81.9% for random review.
- **Caveat:** Results are simulation-based on a small, study-specific adjudicated set; operational reliability across institutions and cancer types remains untested.
- **Announcement type:** new submission, 2026-11-17
- **Themes:** Biomedical & translational medicine; Quantitative methods

## Trending Research Themes
- **Protein engineering, representation and assay interpretation (#1, #4, #7):** Two antibody papers make measurement quality and assay transfer central, while Calpha tests a language-model route to single-chain structure generation. These are distinct contributions, not independent validation of one another.
- **Learning from molecular data for biomedical tasks (#2, #5, #10):** Bulk RNA prediction, genomic-resistance auditing, and treatment-history adjudication all pair machine-learning systems with biomedical evidence. The evaluation designs differ substantially, from held-out cohorts to curated cases and simulations.
- **Spatial and regulatory systems modeling (#3, #6, #8):** Spatial multi-omics, optimized gene-regulatory networks, and tumor-metabolism dynamics connect quantitative models to tissue or cell-state questions; only the multiCAsp paper tests its method on measured tissue datasets, while the other two are computational models.
- **Measurement-aware risk evaluation (#9, with #1):** Both ask whether chosen measurements capture the intended biological or clinical property—time to cancer diagnosis in one case, antibody biophysics in the other—using different retrospective or in-vitro settings.

## Open Problems and Research Directions
- **Confirm antibody leads and assay proxies (#1):** The authors note that key lead values have one or two replicates and some affinity estimates approach assay limits. Replicate the leads, use longer-window BLI or a higher-sensitivity method such as SPR, and test aggregation with isothermal holds plus size-exclusion measurements; stress testing and mammalian expression would broaden the evidence base.
- **Test transcriptome-model transport (#2):** The authors report parity rather than a lead across cohorts and unseen sites. Evaluate on prospective or independently curated cohorts with site-held-out splits, and compare performance across platforms and clinical endpoints under pre-specified analysis.
- **Improve interpretability and generalization in spatial omics (#3):** The authors identify dense loadings, latent-dimension/PCA choices, and only two real-data settings as limitations. Follow-up could test sparse loadings, quantify factor-selection uncertainty, and validate on additional tissues, spatial resolutions, and matched three-or-more-modality datasets.
- **Stress-test evidence handling in oncology systems (#5, #10):** The current evaluations use curated knowledge or a small adjudicated set. Independent knowledge bases, deliberately incomplete or conflicting evidence, and multi-site clinician-reviewed histories could test whether reported error-control behavior persists outside the authors' settings.

## Takeaway
This batch is strongest in methods that make molecular measurements more usable: antibody engineering, bulk-transcriptome prediction, and spatial multi-omics. The leading results remain bounded by small assay replication, retrospective or simulated evaluation, and unresolved cross-site generalization. Treat the list as a relevance-focused snapshot of arXiv, not a signal of clinical readiness or field-wide popularity.

## Method and sources
- **Window:** daily batch dated 2026-11-17; start and end date 2026-11-17. Snapshot: 2026-11-18T01:20:06Z. The calendar date was 2026-11-18, so this uses the prior announcement batch.
- **Candidate collection:** recent category listings for q-bio.BM, q-bio.GN, q-bio.MN, q-bio.SC, q-bio.CB, q-bio.TO, q-bio.QM, and physics.med-ph showed 43 category appearances; deduplication by versionless arXiv ID gave 40. The configured cs.BI query returned no records for this snapshot. The broad arXiv API query used: `https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200`.
- **Selection and ranking:** the order reflects demonstrated relevance to biochemistry, DNA/RNA, genomics, and medicine, with emphasis on transparent evidence settings and biological application; cross-list breadth is a secondary signal and recency only a tie-breaker. No numeric trend score is used. The ten selected arXiv abstract pages were checked; the first three papers' introductions, results, and discussions were read from their arXiv HTML full text. Claims and limitations are attributed to the authors.
- **Primary sources:** [q-bio.BM recent](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN recent](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN recent](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC recent](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB recent](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO recent](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM recent](https://arxiv.org/list/q-bio.QM/recent), [physics.med-ph recent](https://arxiv.org/list/physics.med-ph/recent). Each paper title links to its verified arXiv abstract; full text where read: [#1](https://arxiv.org/html/2611.19812v1), [#2](https://arxiv.org/html/2611.18774v1), [#3](https://arxiv.org/html/2611.20580v1).
