# Daily arXiv Biology and Biomedicine — 2026-11-06

## Headline

Daily arXiv biology/biomedicine, latest announcement batch Friday 6 November 2026: 12 selected papers from 15 eligible records (14 new submissions and one revision). Computational molecular discovery and evaluation is the strongest thread—agent-led drug discovery, protein motif scaffolding, and molecular docking—alongside sequence-based gene regulation and biomedical measurement. Spoken agenda: molecular design first, then genomics, clinical prediction, and imaging. arXiv has no official trending chart; this is an inferred relevance ranking from sparse attention signals and incomplete arXiv coverage, not a popularity measure or a survey of bioRxiv, medRxiv, or biomedical research overall.

## Notable recent papers (ranked by relevance)

### 1. [PharmAgents2: Towards Autonomous End-to-End Drug Discovery](https://arxiv.org/abs/2611.07653)
- **Abstract:** PharmAgents2 combines literature-derived decision knowledge and parallel agent exploration to propose drug-discovery candidates, with the authors reporting three human-executed experimental follow-ups.
- **Authors:** Haichuan Tan, Bowen Gao, Tao Huang, Jiaxin Tan, Xin Hong, Baoguo Yao, Yifei Wang, Zhichao Deng, Hanji Du, Dapeng Jiang, Yiheng Li, Weiwei Ma, Xin Ma, Yuqi Shi, Zixiang Wang, Kelin Wu, Tianxiang Wu, Wenxuan Xie, Jie Zang, Huiyu Zhang, Mojia Zhang, Yuying Zhang, Ya-Qin Zhang, Wei-Ying Ma, Yanyan Lan.
- **arXiv:** `2611.07653v1` (published 2026-11-05 08:39:19 UTC; categories: `cs.AI` primary, `q-bio.QM` cross-list).
- **Evidence for ranking:** Semantic Scholar showed 0 citations and 0 influential citations at the snapshot. One external news summary appeared the next day ([Bloomer](https://bloomer.news/stories/tsinghua-pharmagents2-autonomous-drug-discovery-wet-lab/)); this is a modest attention signal, not evidence of broad uptake. Ranked highly for direct drug-discovery relevance and reported wet-lab follow-up.
- **Claimed contribution:** The authors introduce Paper2Skill, Self-Scaling Discovery, and a 121-question/three-task benchmark; they report wet-lab-supported findings involving LpxH, JAK1, and a secondary target.
- **Caveat:** The benchmark is small and partly author-defined, and the real-world demonstrations cover three research scenarios. The experiments support specific candidate-level findings, not clinical efficacy or generalized autonomous drug discovery.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods.

### 2. [MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation](https://arxiv.org/abs/2611.08086)
- **Abstract:** MUSS combines DNA-sequence embeddings with paired single-cell chromatin-accessibility and expression data to predict regulatory relationships and cell-specific expression, including for held-out genes and regions.
- **Authors:** Kangjie Zheng, Amirhossein Vahidi, Liying Jin, Joseph Clarke, Vijaya Baskar MS, Connor Rogerson, Mengji Zhang, Muzlifah Haniffa, Anshul Kundaje, Mo Lotfollahi.
- **arXiv:** `2611.08086v1` (published 2026-11-05 14:34:07 UTC; categories: `cs.AI` primary, `q-bio.GN` cross-list).
- **Evidence for ranking:** Semantic Scholar showed 0 citations and 0 influential citations. The arXiv comment identifies NeurIPS 2026; code and checkpoints are linked from the authors' project repository. These are venue/reproducibility signals, not evidence of measured readership.
- **Claimed contribution:** The authors evaluate expression prediction, enhancer–gene linking, and zero-shot cell clustering on four paired datasets; they report strong or best/tied-best results in many settings and held-out-sequence performance.
- **Caveat:** Results are computational benchmarks on a limited set of datasets and baselines; prediction does not establish causal regulation. The paper notes that its enhancer–gene evaluation does not establish generalization to unseen links, and exact peak attention is costly.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Omics & single-cell methods.

### 3. [Static Recovery Is Not Dynamic Stability: Dynamics-Aware Benchmarking of Protein Motif Scaffolding](https://arxiv.org/abs/2611.07723)
- **Abstract:** BILBY-PRO expands protein motif-scaffolding evaluation to 220 cases, while BILBY-MD tests whether statically successful designs retain motif geometry and scaffold stability during molecular dynamics.
- **Authors:** Emile de Bruyn, Moritz Schäffler, Jannik Schneider, Sebastian R. Schmidt, Chanwoong Hwang, Aleena Siji, Utkarsh Upadhyay, Stefan Bauer, Alexander Schug, Stefan Kesselheim, Artur Yakimovich, Alina Bazarova.
- **arXiv:** `2611.07723v1` (published 2026-11-05 09:38:23 UTC; categories: `cs.LG` primary, `q-bio.BM` cross-list).
- **Evidence for ranking:** Semantic Scholar showed 0 citations and 0 influential citations. The arXiv comment says accepted to NeurIPS 2026 (Evaluations & Datasets Track), corroborated by the [NeurIPS poster page](https://neurips.cc/virtual/2026/poster/139733); this is a venue signal, not popularity evidence. The authors also discussed the result publicly, but no independent technical discussion was established.
- **Claimed contribution:** Across six scaffold generators, the authors report different target-coverage and unique-solution trade-offs; among 55 statically solved model/problem pairs examined with MD, 31 met their MD-support criterion and 8 passed all checks.
- **Caveat:** The dynamics test applies to MotifBench designs, not the new BILBY-PRO cases, and MD support does not establish biochemical function. Results depend on the simulation protocol and pass criteria.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods.

### 4. [Geometric Relevance Is Not Sufficient: Evaluating Focused Post-Training Supervision in Diffusion Docking](https://arxiv.org/abs/2611.08249)
- **Abstract:** A fixed-budget DiffDock study compares broad continuation training with focused torsional supervision and finds no consistent docking-success advantage from focused supervision under the tested conditions.
- **Authors:** Michael Brown, Maryam Rahimimovassagh, Mehdi Yazdani-Jahromi, Sanjeda Sara Jennifer, Ivan Garibay.
- **arXiv:** `2611.08249v1` (published 2026-11-05 16:26:44 UTC; categories: `cs.LG` primary, `q-bio.BM` cross-list).
- **Evidence for ranking:** Semantic Scholar showed 0 citations and 0 influential citations. The arXiv comment reports acceptance to the NeurIPS 2026 AI4DD Workshop. The paper separates score fidelity, sampling, and selected-pose success; it ranks for molecular-docking relevance, not measured popularity.
- **Claimed contribution:** The authors report that broad continuation had the highest mean Top-1 success among the trained policies at the <5 Å threshold, while focused or mixed supervision had no consistent advantage within the tested budget.
- **Caveat:** This is a fixed-budget comparison on DiffDock; conclusions depend on the model, training budget, and evaluation setup. Pose success does not establish physical validity or experimental binding.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods.

### 5. [How Deep is the Signal? Time-Context up to 30 Years for Colorectal Cancer Prediction in a Primary-Care EHR Model](https://arxiv.org/abs/2611.07265)
- **Abstract:** A primary-care EHR model's colorectal-cancer discrimination improved as the lookback period expanded to 18 years, then plateaued, with the authors finding a similar peak AUROC for XGBoost.
- **Authors:** Achille Raviez, Lan Wang, Brendan Delaney.
- **arXiv:** `2611.07265v1` (published 2026-11-05 00:34:47 UTC; categories: `cs.LG` primary, `cs.AI`, `q-bio.QM` cross-lists).
- **Evidence for ranking:** Semantic Scholar showed 0 citations and 0 influential citations. The arXiv comment identifies acceptance to the ML4H 2026 Findings Track. Inclusion is based on biomedical relevance and the long longitudinal evaluation, not measured popularity.
- **Claimed contribution:** The authors pretrained on 1.4 billion coded events from 3.6 million North West London primary-care patients and evaluated 1,008 cases with 9,582 matched controls across 15 lookback windows; AUROC rose from 0.551 at two years to 0.590 at 18 years.
- **Caveat:** The frozen evaluation cohort is from one health system, discrimination remains modest, and the study does not establish clinical utility, calibration, or prospective benefit. This is not a clinical screening recommendation.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Biomedical & translational medicine; Quantitative methods.

### 6. [Resampling-based batch reweighting for ComBat harmonization of MRI radiomic features in a multi-scanner glioma cohort](https://arxiv.org/abs/2611.02156)
- **Abstract:** This revised study tests whether resampling underrepresented scanner batches before ComBat harmonization reduces residual scanner effects in MRI radiomic features while retaining tumor-grade information.
- **Authors:** Rifa Sajda Tasnim, Yushuf Sharker, Md Forhad Hossain, Rakibur Rahman, Enamul Hoque Bhuiyan.
- **arXiv:** `2611.02156v2` (latest revision 2026-11-05 13:40:38 UTC; first submitted 2026-11-01 19:43:22 UTC; categories: `eess.IV` primary, `physics.med-ph` cross-list).
- **Evidence for ranking:** Version 2 was announced in this batch; the arXiv comment says the manuscript was submitted to the Journal of Magnetic Resonance Imaging, not accepted. Included for its direct glioma-imaging application and cohort-based comparison.
- **Claimed contribution:** In 733 patients from one center and nine vendor/field-strength batches, batch-augmented ComBat reduced features with significant residual scanner association from 13/428 to 8/428 compared with standard ComBat; the authors call the evidence exploratory with confirmatory tests.
- **Caveat:** Retrospective, single-center data and imbalanced scanner batches limit transportability. Reduced scanner association alone does not prove preservation of all clinically relevant signal or improved patient outcomes.
- **Announcement type:** revision, 2026-11-06 batch (v2; first submission 2026-11-01).
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods.

### 7. [Leveraging deep generative modelling at the agent level in discrete-event simulations](https://arxiv.org/abs/2611.07995)
- **Abstract:** A conditional generative emulator replaces one component of a multi-disease agent-based simulation, reducing runtime while approximately recovering the modeled disability-adjusted-life-year trajectory.
- **Authors:** Margherita Molaro, Matthew M. Graham, Oliver Watson, Rachel E. Murray-Watson, Martin Chalkley, Joseph H. Collins, Bingling She, Asif U. Tamuri, Timothy B. Hallett.
- **arXiv:** `2611.07995v1` (published 2026-11-05 13:23:39 UTC; categories: `q-bio.QM` primary, `q-bio.PE` cross-list).
- **Evidence for ranking:** The arXiv comment says accepted for publication by the Journal of the Royal Society Interface. The authors report an 86.6% runtime reduction with a bootstrap interval and recovery of the cause-specific mean outcome within 13%; these are model-method results, not external attention measures.
- **Claimed contribution:** The authors replace the road-traffic-injury component of Thanzi La Onse with a conditional tabular GAN while retaining the full multi-disease simulation framework.
- **Caveat:** The demonstration concerns one modeled cause with low assumed fatal incidence and one simulation framework. It validates computational approximation, not real-world disease-burden estimates or public-health interventions.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Biomedical & translational medicine; Quantitative methods.

### 8. [Kinetic models of a K channel with 2 stage voltage sensor activation and an opening step](https://arxiv.org/abs/2611.08354)
- **Abstract:** The paper derives a reduced kinetic description for a potassium channel with two-stage voltage-sensor activation and a separate opening step, relating effective rates to voltage-clamp rate dependence.
- **Authors:** S. R. Vaccaro.
- **arXiv:** `2611.08354v1` (published 2026-11-05 17:36:25 UTC; categories: `q-bio.BM` primary).
- **Evidence for ranking:** Semantic Scholar showed 0 citations and 0 influential citations. It is directly relevant to molecular biophysics; the abstract describes a 10-state formulation and a limiting case yielding open-state probability proportional to the square of an activation variable.
- **Claimed contribution:** The author derives conditions under which a 10-state scheme reduces to simpler rate equations with voltage dependence similar to voltage-clamp rates.
- **Caveat:** This is kinetic modeling; the abstract reports no new channel experiments or independent validation dataset.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Biochemistry & proteins; Quantitative methods.

### 9. [Accelerating reaction network identification via frequency-domain analysis](https://arxiv.org/abs/2611.07684)
- **Abstract:** The authors use a Fourier-domain approximation to make Bayesian identification of some stochastic intracellular reaction networks less computationally demanding.
- **Authors:** Zhou Fang, Wenying Sun, Xiaoyu Zhang, Mustafa Khammash.
- **arXiv:** `2611.07684v1` (published 2026-11-05 09:11:41 UTC; categories: `q-bio.MN` primary).
- **Evidence for ranking:** Semantic Scholar showed 0 citations and 0 influential citations. The paper applies its method to a gene-transcription example; relevance is methodological rather than evidence of a newly discovered biological mechanism.
- **Claimed contribution:** The authors report that, for certain systems, Fourier transformation makes the measurement likelihood approximately Gaussian, enabling faster Bayesian inference.
- **Caveat:** The abstract describes a numerical observation and one illustrative example; applicability to broader network classes or measured biological datasets remains to be established.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Molecular & cell biology; Quantitative methods.

### 10. [High resolution 3D localization of ultrasound sparse sources using a SAGE algorithm](https://arxiv.org/abs/2611.07966)
- **Abstract:** A SAGE-based method estimates positions and waveforms of sparse ultrasound sources, reporting 0.24 mm simulation precision and proof-of-concept agreement in proton-induced nanodroplet-vaporization experiments.
- **Authors:** Sophie V. Heymans, François Rottenberg, Tatiana Gelvez-Barrera, Adrian Basarab, Barbara Nicolas.
- **arXiv:** `2611.07966v1` (published 2026-11-05 13:00:19 UTC; categories: `physics.med-ph` primary).
- **Evidence for ranking:** Semantic Scholar showed 0 citations and 0 influential citations. No independent attention signal was established; included for its direct medical-physics application and simulation-plus-experimental evaluation.
- **Claimed contribution:** Across 49 simulated acquisitions with up to seven simultaneous sources, the authors report 0.24 mm standard deviation in total localization error; phantom experiments show improved spatial resolution over beamforming and submillimeter agreement with the proton distribution.
- **Caveat:** The experimental work is a water-based phantom proof of concept without ground truth for individual vaporization events. Tissue effects and dense source clouds need further testing.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods.

### 11. [Evaluation of Image Noise from Computed Tomography in an Organ-Specific Anthropomorphic Phantom](https://arxiv.org/abs/2611.07357)
- **Abstract:** In an adult-sized anthropomorphic phantom on one CT scanner, the authors compare organ-specific image noise under ASiR-V and deep-learning reconstruction across noise-index settings and estimate dose reductions at equivalent noise.
- **Authors:** Lucas McCullum, Mojtaba Zarei, Andy Tsai, Michael J. Callahan, Peng Sun, Da Zhang.
- **arXiv:** `2611.07357v1` (published 2026-11-05 02:50:41 UTC; categories: `physics.med-ph` primary).
- **Evidence for ranking:** Semantic Scholar showed 0 citations and 0 influential citations. Inclusion is for the phantom-based, organ-specific comparison in medical physics; no independent attention signal was found.
- **Claimed contribution:** The authors report a power-law relationship between noise index and CTDIvol and a maximum estimated absolute dose reduction of 1.3 mGy in the liver at one setting.
- **Caveat:** Phantom measurements and modeled dose equivalence do not establish patient dose reduction, diagnostic non-inferiority, or clinical benefit.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Medical physics & imaging; Quantitative methods.

### 12. [Continuous Space-Time Finite Element Simulations for Biomedical Flows with Large Boundary Motion and Time-Periodicity](https://arxiv.org/abs/2611.07822)
- **Abstract:** An axisymmetric space-time finite-element method models periodic flow with moving boundaries and is demonstrated for an intra-aortic balloon pump inside a rigid tube.
- **Authors:** Nico Dirkes, Marek Behr.
- **arXiv:** `2611.07822v1` (published 2026-11-05 11:03:41 UTC; categories: `physics.flu-dyn` primary, `math.NA`, `physics.comp-ph`, `physics.med-ph` cross-lists).
- **Evidence for ranking:** Cross-listed in the medical-physics batch; the authors report refinement convergence and weak scaling up to 960 ranks. Included for its biomedical-flow application and computational validation, not measured popularity.
- **Claimed contribution:** The method incorporates large boundary motion without remeshing and computes periodic solutions directly; its demonstration resolves jets and recirculation in a rigid-tube model.
- **Caveat:** This is a numerical-method demonstration, not patient-specific or in-vivo evidence; the tube is rigid and does not validate clinical hemodynamic predictions.
- **Announcement type:** new submission, 2026-11-06 batch.
- **Themes:** Medical physics & imaging; Quantitative methods.

## Trending Research Themes

The clearest cluster is computational molecular discovery and evaluation: PharmAgents2 reports three experimentally followed drug-discovery scenarios, BILBY tests static protein-motif designs against molecular-dynamics behavior, and the DiffDock study finds that geometrically focused post-training did not consistently improve returned-pose success. These are distinct contributions and evidence types, not independent validations of a common system; only PharmAgents2 reports wet-lab follow-up, while BILBY and DiffDock are computational evaluations.

A second thread is representation and measurement in biomedical data. MUSS aligns sequence-derived representations with single-cell assays; the EHR study varies calendar lookback; and ComBat, SAGE, and CT studies examine scanner or acquisition effects. These papers use different datasets and endpoints, so this sample does not establish a field-wide shift.

A third, smaller group develops mechanistic or computational models: the K-channel paper derives kinetic reductions, reaction-network identification uses a frequency-domain approximation, and the disease-simulation paper accelerates one component of a multi-disease agent-based model. Each remains conditional on its model assumptions and validation setting.

## Open Problems and Research Directions

- **Connect computational design success to orthogonal experiments.** PharmAgents2's selected wet-lab scenarios could be followed by preregistered, blinded studies across targets and assay types, with external laboratories and accounting for failed proposals. For BILBY and DiffDock, prospective assays and structural comparisons would test whether MD or docking criteria predict physical function.
- **Test biological and clinical portability.** MUSS needs independent cell types, assay platforms, and perturbation datasets; CRISPR perturbations could separate predictive enhancer–gene associations from causal regulation. The EHR result would benefit from external health-system validation, calibration, decision-utility analysis, and prospective evaluation; its modest AUROC should remain explicit.
- **Validate medical measurements across settings.** ComBat could be tested on multi-center cohorts with scanner/vendor holdouts and explicit checks for preserved grade/outcome signal. SAGE needs tissue-mimicking or in-vivo tests with known source locations and varying source density; CT reconstruction/dose relationships need multi-scanner and diagnostic-task studies. These are proposed follow-ups, not clinical advice.
- **Stress-test model-based simulations.** The agent-level disease simulator, reaction-network inference, K-channel kinetics, and biomedical-flow solver could be compared with independent datasets and measured parameter ranges, including sensitivity to assumptions and failure cases. These would test whether computational speed or explanatory fit transfers beyond the showcased examples.

## Takeaway

The batch is strongest in computational molecular-design evaluation, with additional single-cell, longitudinal EHR, and medical-physics methods. PharmAgents2 reports limited wet-lab follow-up; most other selected results are computational, retrospective, simulated, or phantom-based. Citation evidence was sparse at the snapshot, so this is a relevance-ranked reading list—not a claim these were the most-read or most-popular papers.

## Method and sources

- **Window:** daily; announcement batch dated Friday 2026-11-06. The batch was released at 20:00 US Eastern on Thursday 5 November, i.e. 2026-11-06 01:00 UTC. As the snapshot was Saturday 2026-11-07 01:25:09 UTC, this is the most recent batch; the daily report uses the prior batch because there was no Saturday batch. Window start and end: 2026-11-06 through 2026-11-06 (announcement date). Snapshot: 2026-11-07 01:25:09 UTC.
- **Candidate pool:** traversed the recent listings for `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph`; a broad API query also included `cs.BI`. The dated category listings contained 16 unique records; two older cross-listed records had no first-submission or version/date change in the window and were excluded. A separate version check found one eligible v2 revision announced in the batch, for 15 eligible records total (14 new submissions and one revision). Twelve directly relevant papers are selected here; less directly relevant collective-motion, vegetation, and single-agent behavior models were not used to pad the report. Selected abstract pages were verified individually.
- **API query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date descending. The combined arXiv API was paginated at offsets 0 and 200 (400 records checked, with page 2 reaching 2026-10-06), beyond the selected batch.
- **Ranking:** arXiv has no official trend/readership ranking. Papers are ordered by biological/biomedical relevance, reported method/evaluation strength, and checkable venue or external-discussion signals where present. Semantic Scholar returned current citation and influential-citation totals of zero for nine queried papers; no citation velocity was used. Citation totals are not gains during the batch. For the remaining entries, ranking does not rely on a citation count. One external news summary for PharmAgents2 was found; no independent technical discussion was established for most entries.
- **Coverage caveat:** arXiv is an incomplete biomedical corpus; many experimental and clinical preprints are on bioRxiv or medRxiv. This is neither a comprehensive survey nor clinical guidance.
- **Sources:** [arXiv announcement schedule](https://info.arxiv.org/help/availability.html); [q-bio recent listings](https://arxiv.org/list/q-bio/recent), [medical-physics recent listing](https://arxiv.org/list/physics.med-ph/recent), and the individual canonical arXiv abstract pages linked above; [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch); PharmAgents2 coverage at [Bloomer](https://bloomer.news/stories/tsinghua-pharmagents2-autonomous-drug-discovery-wet-lab/); BILBY's [NeurIPS poster](https://neurips.cc/virtual/2026/poster/139733).