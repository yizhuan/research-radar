# arXiv biology & biomedicine — daily report, 6 November 2026

## Headline

Ten notable papers were listed in today's configured biology/biomedicine categories. The strongest pattern is a push to evaluate AI-assisted biological and biomedical methods against more explicit evidence: wet-lab follow-up, molecular dynamics, held-out genomic regions, and carefully specified imaging or simulation benchmarks. Spoken agenda: drug discovery and genomic models first, then protein/docking benchmarks, molecular kinetics, and medical-physics methods. arXiv has no official trending chart; this is an inferred relevance ranking from category listings and checkable paper/proceedings metadata, not measured readership or downloads. The arXiv corpus is incomplete for biomedical research, especially experimental and clinical preprints.

## Notable recent papers

### 1. [PharmAgents2: Towards Autonomous End-to-End Drug Discovery](https://arxiv.org/abs/2611.07653)
- **Abstract:** The authors present an agent system and benchmark for end-to-end drug-discovery workflows, reporting three investigations whose findings received human-run experimental follow-up.
- **Authors:** Haichuan Tan, Bowen Gao, Tao Huang, Jiaxin Tan, Xin Hong, Baoguo Yao, Yifei Wang, Zhichao Deng, Hanji Du, Dapeng Jiang, Yiheng Li, Weiwei Ma, Xin Ma, Yuqi Shi, Zixiang Wang, Kelin Wu, Tianxiang Wu, Wenxuan Xie, Jie Zang, Huiyu Zhang, Mojia Zhang, Yuying Zhang, Ya-Qin Zhang, Wei-Ying Ma, Yanyan Lan
- **arXiv:** `2611.07653v1` (published 2026-11-05 08:39:19 UTC; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Direct drug-discovery relevance; the authors report a 121-question benchmark and three experimental follow-ups, including LpxH inhibitor activity/binding and confirmation of a proposed target interaction. These are author-reported results, not independent attention metrics.
- **Claimed contribution:** The authors describe Paper2Skill and parallel-agent exploration as supporting scientific decisions, with experimental follow-up for three discovery scenarios; this is a prototype, not a general demonstration of autonomous drug development.
- **Caveat:** The experimental demonstrations are three selected scenarios and were carried out by people; they do not establish prospective success rates, therapeutic efficacy, or clinical utility.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 2. [MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation](https://arxiv.org/abs/2611.08086)
- **Abstract:** MUSS combines DNA-derived peak and gene representations with paired single-cell chromatin-accessibility and expression data to predict regulatory readouts, including for held-out genomic regions.
- **Authors:** Kangjie Zheng, Amirhossein Vahidi, Liying Jin, Joseph Clarke, Vijaya Baskar MS, Connor Rogerson, Mengji Zhang, Muzlifah Haniffa, Anshul Kundaje, Mo Lotfollahi
- **arXiv:** `2611.08086v1` (published 2026-11-05 14:34:07 UTC; categories: `cs.AI`, `q-bio.GN`)
- **Evidence for ranking:** Listed in today's genomics batch; arXiv records NeurIPS 2026, and the paper evaluates four paired single-cell datasets with held-out sequence and cell-type settings. [NeurIPS poster](https://nips.cc/virtual/2026/poster/150251)
- **Claimed contribution:** The authors report competitive expression prediction, enhancer–gene linking and cell-clustering results using a frozen sequence encoder plus multi-scale attention, including tests on unseen genes/peaks.
- **Caveat:** This is computational evaluation, not experimental confirmation of regulatory causality. The authors note that enhancer–gene evaluation does not establish generalization to unseen links and that exact peak attention is costly.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Omics & single-cell methods

### 3. [Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding](https://arxiv.org/abs/2611.07723)
- **Abstract:** The authors introduce a 220-case motif-scaffolding benchmark and an all-atom dynamics evaluation, finding that static refolding success often does not imply dynamic fidelity.
- **Authors:** Emile de Bruyn, Moritz Schäffler, Jannik Schneider, Sebastian R. Schmidt, Chanwoong Hwang, Aleena Siji, Utkarsh Upadhyay, Stefan Bauer, Alexander Schug, Stefan Kesselheim, Artur Yakimovich, Alina Bazarova
- **arXiv:** `2611.07723v1` (published 2026-11-05 09:38:23 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Today's biomolecules batch; accepted at NeurIPS 2026 Evaluations & Datasets Track. The authors report 220 cases across 174 PROSITE patterns and apply molecular-dynamics checks to 55 statically solved model–problem pairs. [NeurIPS poster](https://nips.cc/virtual/2026/poster/139733)
- **Claimed contribution:** The authors argue that target coverage, unique-solution yield and MD-supported dynamical fidelity should be reported separately; only 8 of 55 evaluated pairs passed all their checks.
- **Caveat:** Molecular-dynamics support is not evidence of biochemical function. The dynamics analysis used MotifBench designs rather than the new BILBY-PRO cases, and the authors describe it as a downstream check, not a sufficient functional test.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 4. [Geometric Relevance Is Not Sufficient: Evaluating Focused Post-Training Supervision in Diffusion Docking](https://arxiv.org/abs/2611.08249)
- **Abstract:** In a fixed-budget DiffDock study, geometry-focused or mixed post-training did not consistently outperform broad continuation on returned-pose success.
- **Authors:** Michael Brown, Maryam Rahimimovassagh, Mehdi Yazdani-Jahromi, Sanjeda Sara Jennifer, Ivan Garibay
- **arXiv:** `2611.08249v1` (published 2026-11-05 16:26:44 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Listed in today's biomolecules batch and accepted at the NeurIPS 2026 AI for Drug Discovery workshop. The paper separates fixed score fidelity, pose generation, best-of-10 recovery and confidence-selected Top-1 results; the full study uses 99 complexes and three training seeds.
- **Claimed contribution:** The authors report that broad continuation had the highest mean Top-1 success among the trained policies at the 5 Å threshold, while focused/mixed supervision had no consistent advantage within the tested budget.
- **Caveat:** This is one docking architecture and a bounded post-training experiment; RMSD-based pose success does not establish physical validity, interaction recovery or experimental binding.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [How Deep is the Signal? Time-Context up to 30 Years for Colorectal Cancer Prediction in a Primary-Care EHR Model](https://arxiv.org/abs/2611.07265)
- **Abstract:** A primary-care EHR model's colorectal-cancer discrimination improved with longer history up to about 18 years, then plateaued, while an XGBoost baseline reached similar performance.
- **Authors:** Achille Raviez, Lan Wang, Brendan Delaney
- **arXiv:** `2611.07265v1` (published 2026-11-05 00:34:47 UTC; categories: `cs.LG`, `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Listed in today's quantitative-biology batch and accepted at ML4H 2026 Findings. Authors report pretraining on 1.4B coded events from 3.6M patients and a frozen evaluation of 1,008 cases plus 9,582 matched controls; AUROC peaked at 0.590.
- **Claimed contribution:** The authors propose calendar-time lookback as a model-design variable distinct from token context and report that the measured signal plateaued beyond an 18-year lookback in this cohort.
- **Caveat:** This is a retrospective prediction study, not a validated screening test. The evaluation is a selected, single-region cohort, discrimination was modest, and the authors note one training run and potential coding/registration biases.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 6. [Kinetic models of a K channel with 2 stage voltage sensor activation and an opening step](https://arxiv.org/abs/2611.08354)
- **Abstract:** The paper derives a reduced kinetic description for a potassium channel with two-stage voltage-sensor activation and a separate opening step, relating effective rates to voltage-clamp rate dependence.
- **Authors:** S. R. Vaccaro
- **arXiv:** `2611.08354v1` (published 2026-11-05 17:36:25 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Listed in today's biomolecules batch and directly addresses ion-channel gating kinetics; the paper reports a 10-state formulation and a limiting case yielding an open-state probability proportional to the square of an activation variable.
- **Claimed contribution:** The author derives conditions under which a 10-state scheme reduces to simpler rate equations with voltage dependence similar to voltage-clamp rates.
- **Caveat:** The contribution is kinetic modelling; the abstract does not report new channel experiments or an independent validation dataset.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 7. [Accelerating reaction network identification via frequency-domain analysis](https://arxiv.org/abs/2611.07684)
- **Abstract:** The authors use a Fourier-domain approximation to make Bayesian identification of some stochastic intracellular reaction networks less computationally demanding.
- **Authors:** Zhou Fang, Wenying Sun, Xiaoyu Zhang, Mustafa Khammash
- **arXiv:** `2611.07684v1` (published 2026-11-05 09:11:41 UTC; categories: `q-bio.MN`)
- **Evidence for ranking:** Listed in today's molecular-networks batch and applies the method to a gene-transcription example; relevance is methodological rather than evidence of a newly discovered biological mechanism.
- **Claimed contribution:** The authors report that, for certain systems, Fourier transformation makes the measurement likelihood approximately Gaussian, enabling faster Bayesian inference.
- **Caveat:** Evidence described in the abstract is a numerical observation and one illustrative transcription example; applicability to broader network classes or measured biological datasets remains to be established.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Molecular & cell biology; Quantitative methods

### 8. [High resolution 3D localization of ultrasound sparse sources using a SAGE algorithm](https://arxiv.org/abs/2611.07966)
- **Abstract:** A SAGE source-localization method achieved 0.24 mm localization-error standard deviation in simulations and improved spatial resolution on experimental proton-induced nanodroplet-vaporization data.
- **Authors:** Sophie V. Heymans, François Rottenberg, Tatiana Gelvez-Barrera, Adrian Basarab, Barbara Nicolas
- **arXiv:** `2611.07966v1` (published 2026-11-05 13:00:19 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Listed in today's medical-physics batch; the authors report 49 simulated acquisitions with up to seven simultaneous sources and a separate experimental ultrasound-array evaluation.
- **Claimed contribution:** The authors report sub-millimeter agreement between vaporization maps and proton distributions in three spatial dimensions, suggesting a possible proton-therapy monitoring application.
- **Caveat:** The abstract describes simulations and a specific experimental setup, not a clinical validation cohort or evidence of improved treatment outcomes.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 9. [Evaluation of Image Noise from Computed Tomography in an Organ-Specific Anthropomorphic Phantom](https://arxiv.org/abs/2611.07357)
- **Abstract:** In an adult-sized anthropomorphic phantom on one CT scanner, the authors compare organ-specific image noise under ASiR-V and deep-learning reconstruction across noise-index settings and estimate dose reductions at equivalent noise.
- **Authors:** Lucas McCullum, Mojtaba Zarei, Andy Tsai, Michael J. Callahan, Peng Sun, Da Zhang
- **arXiv:** `2611.07357v1` (published 2026-11-05 02:50:41 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Listed in today's medical-physics batch; the study varies reconstruction and prescribed noise index in a physical anthropomorphic phantom and reports organ-dependent differences.
- **Claimed contribution:** The authors report a power-law relationship between noise index and CTDIvol and a maximum estimated absolute dose reduction of 1.3 mGy in the liver at one setting.
- **Caveat:** Phantom measurements and a modeled dose-equivalence calculation do not establish patient dose reduction, diagnostic non-inferiority or clinical benefit.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Medical physics & imaging

### 10. [Continuous Space-Time Finite Element Simulations for Biomedical Flows with Large Boundary Motion and Time-Periodicity](https://arxiv.org/abs/2611.07822)
- **Abstract:** An axisymmetric space-time finite-element method models periodic flow with moving boundaries and is demonstrated for an intra-aortic balloon pump inside a rigid tube.
- **Authors:** Nico Dirkes, Marek Behr
- **arXiv:** `2611.07822v1` (published 2026-11-05 11:03:41 UTC; categories: `physics.flu-dyn`, `math.NA`, `physics.comp-ph`, `physics.med-ph`)
- **Evidence for ranking:** Cross-listed in today's medical-physics batch; the authors report refinement convergence and weak-scaling tests up to 960 ranks.
- **Claimed contribution:** The method incorporates large boundary motion without remeshing and computes periodic solutions directly; its demonstration resolves jets and recirculation in a rigid-tube model.
- **Caveat:** This is a numerical-method demonstration rather than patient-specific or in-vivo evidence; the tube is rigid and does not validate clinical hemodynamic predictions.
- **Announcement type:** new submission, 2026-11-06 announcement batch
- **Themes:** Medical physics & imaging; Quantitative methods

## Trending Research Themes

- **Evidence beyond a single aggregate score.** Protein scaffolding separates target coverage, unique-solution yield and molecular-dynamics support (paper 3); docking separates score fidelity, sampling and selected-pose success (paper 4); MUSS tests held-out genomic regions and cell types (paper 2). Across this small batch, the repeated pattern is evaluation design—not a demonstrated field-wide shift.
- **AI systems linked to biological evidence.** PharmAgents2 reports experimental follow-up to three agent-led drug-discovery investigations (paper 1), while the single-cell and protein-scaffolding studies remain computational (papers 2–3). Their evidence types should not be conflated.
- **Medical-physics methods move from simulations or phantoms toward application-specific measurements.** Ultrasound localization includes a particular experimental dataset (paper 8); CT noise is evaluated in a phantom (paper 9); the biomedical-flow paper is a rigid-tube numerical demonstration (paper 10). None reports a clinical outcome study.
- **Mechanistic models remain hypothesis-generating.** The potassium-channel and reaction-network papers (papers 6–7) contribute reduced kinetic/inference models, not new wet-lab mechanism discoveries.

## Open Problems and Research Directions

- **Connect model-based success criteria to orthogonal experiments.** Protein scaffolds and docking both expose gaps between computational success metrics and physical or functional validation (papers 3–4). A concrete follow-up would select blinded designs across motif classes, run matched simulation and biochemical binding/activity assays, and report failures as well as successes; docking variants could be checked against prospective structures and interaction assays.
- **Test generalization beyond the development setting.** MUSS has held-out-region evaluations but no unseen-link evidence (paper 2); the colorectal EHR study is from one selected London cohort (paper 5); the reaction-network method is illustrated on a transcription example (paper 7). Follow-ups could use independent multi-site or multi-cohort data, explicit dataset-shift analyses, and pre-registered comparisons against simple baselines.
- **Make translational measurement claims robust to acquisition and anatomy.** Ultrasound localization and CT phantom results depend on specific measurement setups (papers 8–9). Replication across arrays, scanners, protocols, anatomies and operators—and, where appropriate, prospective patient studies—would distinguish technical improvements from broader clinical utility.

## Takeaway

Today's most compelling biology-related work is less about claiming a new biological fact than about testing where computational methods succeed and where their evidence stops. PharmAgents2 reports wet-lab follow-up, while most of the remaining papers offer computational, retrospective, simulated or phantom-based evidence. None should be treated as clinical advice or as proof of clinical effectiveness.

## Method and sources

- **Window:** daily, 2026-11-06 through 2026-11-06; latest announcement batch dated Friday 6 November 2026. The current day's batch was available, so no prior batch was substituted. Snapshot: 2026-11-06 17:11:13 UTC.
- **Candidate categories:** `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. The configured `cs.BI` listing returned an invalid-category page. The other eight category listings were traversed; 16 unique entries appeared in their 6 Nov batch listings. Two papers first submitted on 4 Nov with no in-window version/date change were excluded under the daily eligibility rule, leaving 14 eligible candidates. The 200-result API query ran through submissions dated 21 Oct, beyond the selected day; retained papers were checked on their individual arXiv abstract pages.
- **Announcement dates vs. submission timestamps:** arXiv abstract pages record these selected v1 submissions on 5 Nov UTC; their category-list announcement batch is 6 Nov. All ten listed entries are new submissions in that 6 Nov batch, not revisions.
- **Ranking:** attention evidence is sparse for a same-day batch, so these are **notable recent papers**, ordered by direct biology/biomedicine relevance and the specificity of reported evidence. No numeric trend score, downloads, or period citation gains are inferred. Checkable corroboration includes arXiv category/abstract metadata and explicit proceedings/acceptance references where present; citation velocity was not used.
- **Coverage caveat:** arXiv is not a representative index of experimental or clinical biomedical preprints; this report does not cover bioRxiv, medRxiv, or the biomedical literature as a whole.
- **Sources:** [q-bio.BM recent](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN recent](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN recent](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC recent](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB recent](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO recent](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM recent](https://arxiv.org/list/q-bio.QM/recent), [physics.med-ph recent](https://arxiv.org/list/physics.med-ph/recent), [arXiv API category query](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200). Each paper title links to its canonical arXiv abstract page.
