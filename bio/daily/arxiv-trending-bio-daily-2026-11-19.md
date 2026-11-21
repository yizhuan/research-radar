## Headline

The latest available arXiv biology-and-biomedicine announcement batch is dated 2026-11-19 (announced 2026-11-20 at 01:00 UTC): 13 verified papers, led by molecular-similarity and stochastic-reaction methods, with additional work in cryo-EM, multi-omics, and biomedical imaging. Spoken agenda: distinguish computational tools and model-based evidence from experimental validation, and identify where independent data are still needed. Only one candidate has a non-zero citation-derived attention signal; arXiv has no official trending chart, so this is a relevance-ranked selection from incomplete biomedical coverage, not a popularity ranking.

Window: daily, 2026-11-18 19:00 UTC through 2026-11-19 19:00 UTC. Snapshot: 2026-11-21T21:16:03Z. No newer announcement batch was present for the current day, so this uses the most recent prior batch.

## Notable recent papers (ranked by relevance; attention evidence sparse)

### 1. [ShEPhERD-score: Fast, adaptable three-dimensional alignment of molecular features](https://arxiv.org/abs/2611.25076)
- **Abstract:** ShEPhERD-score unifies differentiable 3D molecular similarity scoring and alignment, with CPU/GPU kernels for virtual screening and pairwise workflows.
- **Authors:** Nate Somers, Kento A. Abeywardane, Connor W. Coley, Masha Elkin
- **arXiv:** `2611.25076v1` (published 2026-11-18T19:17:58Z; categories: `q-bio.BM`)
- **Evidence for ranking:** Collector score 0.000; no citations, cross-lists, or matched Hugging Face/Hacker News engagement in the candidate row. Zero is no detected attention, not evidence of low importance. Relevance: direct 3D molecular-design method.
- **Claimed contribution:** The authors report comparable-or-better performance than corresponding open-source tools in 8 of 9 DUDE-Z comparisons, up to 46-fold speedups, and target-dependent best scoring modes.
- **Caveat:** This is a software and virtual-screening benchmark, not experimental hit-rate or therapeutic evidence; the paper notes no one scoring representation is best for every target and suggests target-specific calibration.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [Dynamical Variational Theory of Stochastic Reaction Networks](https://arxiv.org/abs/2611.25491)
- **Abstract:** A field-theoretic variational approximation estimates stochastic reaction-network means, correlations, responses, and steady states in low-copy-number systems.
- **Authors:** Moshir Harsh, Peter Sollich
- **arXiv:** `2611.25491v1` (published 2026-11-19T04:26:42Z; categories: `cond-mat.stat-mech`, `q-bio.MN`, `q-bio.PE`)
- **Evidence for ranking:** Collector score 0.500, from two cross-lists (0.500); Semantic Scholar recorded 0 citations and no influential citations. No matched Hugging Face/Hacker News engagement was recorded. Relevance: explicitly benchmarks biochemical reaction systems.
- **Claimed contribution:** The authors report numerical tests on gene regulation, enzyme kinetics, and infection dynamics, where their generalized self-consistent bubble resummation captures time-varying behavior and fluctuations missed by selected approximations.
- **Caveat:** This is a mathematical and numerical method, not a new wet-lab study. Its accuracy depends on the tested models and comparisons; the authors describe further numerical-solver work as an open direction.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Molecular & cell biology; Quantitative methods

### 3. [Ab-initio cryo-EM reconstruction from moments of denoised images](https://arxiv.org/abs/2611.25525)
- **Abstract:** The authors estimate an initial 3D cryo-EM model from the first three moments of denoised particle images, avoiding explicit orientation estimation at this stage.
- **Authors:** Yunpeng Shi, Amit Singer, Yuguan Wang, Andy Zhang
- **arXiv:** `2611.25525v1` (published 2026-11-19T05:26:45Z; categories: `q-bio.QM`)
- **Evidence for ranking:** Collector score 0.000; no citations, cross-lists, or matched Hugging Face/Hacker News engagement in the candidate row. Zero is not evidence of low importance. Relevance: direct structural-biology method tested on experimental cryo-EM data.
- **Claimed contribution:** The authors show moment-based models can initialize high-resolution refinement on experimental datasets without assuming uniform particle orientations.
- **Caveat:** The paper reports lower-resolution initial models than VDAM or SGD; denoising biases the estimated moments and loses fine detail, and the authors describe the results as preliminary. Refinement can still reach comparable map quality in the reported tests.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biochemistry & proteins; Quantitative methods

### 4. [Physics-Informed Deep Learning for Shear Wave Speed Estimation in MR Elastography](https://arxiv.org/abs/2611.26111)
- **Abstract:** An end-to-end model combines undersampled MRI reconstruction with wave inversion to estimate tissue shear-wave-speed maps from measured k-space data.
- **Authors:** Stefan Martin, Jakob Schattenfroh, Patrick Schuenke, Felix Frederik Zimmermann, Ingolf Sack, Christoph Kolbitsch, Andreas Kofler
- **arXiv:** `2611.26111v1` (published 2026-11-19T13:39:46Z; categories: `eess.IV`, `cs.LG`, `physics.med-ph`)
- **Evidence for ranking:** Collector score 1.886, the only positive citation-derived score: Semantic Scholar total 1 citation (0 influential) plus two cross-lists (components 1.386 and 0.500). No matched Hugging Face/Hacker News engagement was recorded. The citation is a current count, not a gain during this window.
- **Claimed contribution:** The authors report 30% lower NRMSE than total-variation minimization and accurate shear-wave-speed estimation up to acceleration factor 19; the arXiv comment identifies an accepted IEEE Transactions on Biomedical Engineering version (DOI: 10.1109/TBME.2026.3666306).
- **Caveat:** Evaluation is on retrospectively highly undersampled brain MRE data plus in-vivo application; the abstract gives no sample size and does not establish clinical impact or prospective performance.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 5. [Geometry-bridge flow matching for blind rigid-motion correction in head cone-beam CT](https://arxiv.org/abs/2611.23788)
- **Abstract:** A geometry-bridge flow-matching prior jointly supports rigid-motion correction and pose estimation in head cone-beam CT reconstruction.
- **Authors:** Sungho Yun, Seungryong Cho
- **arXiv:** `2611.23788v2` (first submitted 2026-11-18T03:51:56Z; revised 2026-11-19T05:08:07Z; categories: `physics.med-ph`, `cs.CL`, `cs.CV`)
- **Evidence for ranking:** The revision was found in the configured-category `lastUpdatedDate` query but was absent from the supplied 12-paper signal pool. A direct Semantic Scholar lookup returned 0 citations, 0 influential citations, and 28 references. No row-level Hugging Face/Hacker News signal or collector composite score is available for this added paper.
- **Claimed contribution:** On simulated 360-view scans from 30 held-out CQ500 patients, the authors report mean PSNR 37.1 dB and detector-plane reprojection error 0.27 mm; against image-linear training, the geometry bridge improved PSNR by 1.6 dB and reduced reprojection error by 33%.
- **Caveat:** The tests use simulated scans, a 30-patient held-out cohort, and nominal motion bounded at 10 mm / 10 degrees. This is not prospective clinical validation or evidence of improved patient outcomes.
- **Announcement type:** revision, 2026-11-19
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 6. [An Explainable and Scalable Hierarchical Tensor Framework for Integrating Multi-Omics and Digital Pathomics](https://arxiv.org/abs/2611.25584)
- **Abstract:** HIT-Fuse integrates six molecular and pathology modalities across four TCGA cancer cohorts, reconstructing missing latent modalities and providing tensor-based attributions.
- **Authors:** Ahmad Hussein, Ali Anaissi, Mukesh Prasad, Ali Braytee
- **arXiv:** `2611.25584v1` (published 2026-11-19T06:27:17Z; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Collector score 0.250, from one cross-list (0.250); Semantic Scholar recorded 0 citations and no influential citations. No matched Hugging Face/Hacker News engagement was recorded. Relevance: DNA methylation, RNA, microRNA, protein, and pathomics integration.
- **Claimed contribution:** The authors report survival-stratified subgroups and cohort-specific prediction gains, including a 56.4% relative weighted-F1 increase for glioma in their cohort-expansion experiment, with biological checks against DepMap, miRTarBase, and RPPA annotations.
- **Caveat:** The analyses use TCGA cohorts and reconstructed missing modalities; survival stratification and feature annotations do not establish prospective prognostic value or causal biology, and the reported gain is cohort-specific.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** DNA & genomics; RNA & transcriptomics; Omics & single-cell methods

### 7. [From Sequence Uncertainty to Phenotype Hypotheses: Uncertainty-Conditioned Inference over Biomedical Knowledge Graphs](https://arxiv.org/abs/2611.25422)
- **Abstract:** An uncertainty-conditioned path-energy method converts genomic-model outputs into distributions over graph-supported gene-disease-phenotype hypotheses without patient-level phenotype supervision.
- **Authors:** Huixin Zhan, Jason H. Moore
- **arXiv:** `2611.25422v1` (published 2026-11-19T03:02:19Z; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Collector score 0.250, from one cross-list (0.250); Semantic Scholar recorded 0 citations and no influential citations. No matched Hugging Face/Hacker News engagement was recorded. Relevance: explicit genomic variant-to-phenotype inference.
- **Claimed contribution:** On AlzKB and Hetionet, the authors report phenotype-entropy correlations with upstream uncertainty and held-out graph-recovery results; under gene hold-out, recall@10 exceeded DistMult on 24 of 30 masks, with the difference mainly attributable to three genes with many variants.
- **Caveat:** This evaluates graph-supported hypotheses, not patient diagnosis or validated phenotype prediction; the authors explicitly limit the gene-held-out result and note the concentration of gains in a few genes.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

### 8. [When Foundation Models Disagree: Representational Heterogeneity for Calibrated Uncertainty in Whole-Slide Image Classification](https://arxiv.org/abs/2611.26159)
- **Abstract:** CALIFUSE uses disagreement among pathology foundation-model representations and chunk-level evidence consistency to estimate confidence in whole-slide classifications.
- **Authors:** Yekai Shen, Yuqian Wang, Zishun Liao, Rongsheng Wang, Wenting Chen, S. Kevin Zhou, Qingsong Yao
- **arXiv:** `2611.26159v1` (published 2026-11-19T14:15:07Z; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Collector score 0.250, from one cross-list (0.250); Semantic Scholar recorded 0 citations and no influential citations. No matched Hugging Face/Hacker News engagement was recorded. The abstract reports seven WSI classification tasks; the paper comments that it was accepted by IEEE BIBM 2026.
- **Claimed contribution:** The authors report better calibration, misclassification detection, and selective prediction than a strongest single-encoder baseline and naive ensemble averaging while maintaining competitive balanced accuracy.
- **Caveat:** These are task-benchmark results; the abstract does not give cohort sizes or establish performance in clinical workflows or across new institutions.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biomedical & translational medicine; Bioinformatics & sequence analysis

### 9. [GraphEP: A Calibrated Data System and Benchmark for Learning Cardiac Electrophysiology](https://arxiv.org/abs/2611.26551)
- **Abstract:** GraphEP packages graph-native cardiac electrophysiology simulations and benchmarks neural models for predicting transmembrane-potential trajectories.
- **Authors:** Matteo Baldan, Chiara D'Ercoli, James Rowbottom, Pietro Liò, Stefania Fresca
- **arXiv:** `2611.26551v1` (published 2026-11-19T18:23:10Z; categories: `q-bio.TO`)
- **Evidence for ranking:** Collector score 0.000; Semantic Scholar recorded 0 citations, zero cross-lists, and no matched Hugging Face/Hacker News engagement. Zero means no detected external attention, not no value. The abstract describes a benchmark of 732 simulations across 20 anatomies.
- **Claimed contribution:** The authors report that physiological model structure gives the strongest inductive bias in their benchmark, with HGT-Lag and GAP2ODE leading on complementary prediction metrics.
- **Caveat:** The benchmark consists of simulations, not experimentally measured or clinical cardiac trajectories; performance on real-world recordings remains to be established.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Molecular & cell biology; Quantitative methods

### 10. [Transition Dynamics Matter: Hidden Markov Scoring of Epileptogenic Channels in SEEG](https://arxiv.org/abs/2611.26142)
- **Abstract:** A joint hidden Markov model scores stereo-EEG channels by comparing latent-state transition probabilities between interictal periods and seizure onset.
- **Authors:** Giulia Tacconi, Federico Mason, Lorenzo Ferri, Elena Pasini, Lidia Di Vito, Matteo Martinoni, Lara Alvisi, Anna Scarabello, Luca Zanuttini, Francesca Bisulli, Andrea Zanella
- **arXiv:** `2611.26142v1` (published 2026-11-19T13:58:28Z; categories: `eess.SP`, `physics.med-ph`)
- **Evidence for ranking:** Collector score 0.250, from one cross-list (0.250); Semantic Scholar recorded 0 citations and no influential citations. No matched Hugging Face/Hacker News engagement was recorded. The abstract reports an evaluation on SEEG recordings from 30 patients.
- **Claimed contribution:** The authors report improved epileptogenic-zone localization versus a benchmark without latent-state structure, measured against medically validated zone definitions.
- **Caveat:** This is a retrospective algorithm evaluation in 30 patients, not a prospective test of surgical decisions or patient outcomes.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 11. [Towards consensus on practical probabilistic evaluation metrics for clinical decision making in radiotherapy](https://arxiv.org/abs/2611.25260)
- **Abstract:** The authors assess probabilistic robustness metrics for proton radiotherapy using 60 plans from three Dutch centers and interviews with eight radiation oncologists.
- **Authors:** Jenneke I. de Jong, Steven J. M. Habraken, Erik W. Korevaar, Mirko Unipan, Esther Kneepkens, Gloria Vilches Freixas, Yvonne L. B. Klaver, Michiel Kroesen, Alejandra Méndez Romero, Edwin Oldehinkel, Stephanie Peeters, Roel J. H. M. Steenbakkers, Karolien Verhoeven, Stefan Both, Liesbeth J. Boersma, Sebastiaan Breedveld, Mischa S. Hoogeman
- **arXiv:** `2611.25260v1` (published 2026-11-18T22:44:24Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Collector score 0.000; Semantic Scholar recorded 0 citations, zero cross-lists, and no matched Hugging Face/Hacker News engagement. Zero is no detected attention, not evidence of low importance. The arXiv abstract reports 60 plans and eight clinician interviews.
- **Claimed contribution:** The authors report that interviewed radiation oncologists considered the metrics suitable and mostly an improvement over their current robustness evaluation, while preferences differed by center and treatment site.
- **Caveat:** The study uses simulated treatments and interviews, not a prospective clinical-impact trial; the authors call for further consensus and clinical validation before broad implementation.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 12. [Colloquium: Isotopes for medicine and fundamental physics](https://arxiv.org/abs/2611.25145)
- **Abstract:** This review surveys isotope separation and detection technologies and discusses proposed medical and fundamental-physics applications.
- **Authors:** V. J. Ajith, Mark G. Raizen
- **arXiv:** `2611.25145v1` (published 2026-11-18T20:24:17Z; categories: `physics.app-ph`, `physics.atom-ph`, `physics.hist-ph`, `physics.med-ph`, `quant-ph`)
- **Evidence for ranking:** Collector score 1.000, entirely from four cross-lists (1.000); Semantic Scholar recorded 0 citations and no influential citations. No matched Hugging Face/Hacker News engagement was recorded. The cross-list breadth is not itself evidence of biomedical popularity.
- **Claimed contribution:** The authors review technologies for enriching and detecting isotopes and outline possible uses of radioisotopes in cancer therapy and stable isotopes as metabolic tracers.
- **Caveat:** This is a review and outlook, not a clinical or experimental validation of the proposed disease-detection or treatment applications.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 13. [The long-term divergence exponent and the temporal structure of step-to-step perturbations: a simulation study in two passive walking models](https://arxiv.org/abs/2611.26182)
- **Abstract:** Two passive-walker models test whether gait-stability divergence exponents respond to the temporal structure of step perturbations.
- **Authors:** Philippe Terrier
- **arXiv:** `2611.26182v1` (published 2026-11-19T14:34:32Z; categories: `q-bio.QM`, `nlin.CD`, `physics.bio-ph`)
- **Evidence for ranking:** Collector score 0.500, from two cross-lists (0.500); Semantic Scholar recorded 0 citations and no influential citations. No matched Hugging Face/Hacker News engagement was recorded. The paper is relevant as a quantitative biomechanics study, but is less directly molecular than most of this selection.
- **Claimed contribution:** In two passive models, the authors report that the long-term exponent increased with perturbation temporal correlation; the relation to perturbation amplitude differed between models, and human stride-series comparisons were descriptive.
- **Caveat:** Most evidence is simulation-based; the model-dependent response and descriptive human-series correlations do not establish clinical gait outcomes or a general mechanism.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Quantitative methods; Biomedical & translational medicine

## Trending Research Themes

- **Molecular representations and reconstruction:** ShEPhERD-score tests 3D ligand-similarity objectives, while the cryo-EM method uses image moments for an initial structure. Both target computational bottlenecks, but on different tasks; neither establishes new molecular biology or therapeutic efficacy.
- **Uncertainty across heterogeneous biomedical data:** HIT-Fuse combines omics and pathology, the phenotype-graph paper carries sequence uncertainty into graph hypotheses, and CALIFUSE treats representation disagreement as a confidence cue. These are distinct benchmark studies, not independent validations of one another.
- **Models connecting hidden dynamics to observable systems:** The reaction-network theory, GraphEP, and the passive-walker study use mathematical or simulated data to study dynamical behavior. Their evidence ranges from biochemical-network simulations to synthetic cardiac data and passive gait models; it should not be conflated with wet-lab or clinical validation.
- **Medical imaging and decision-support evaluation:** MRE, head cone-beam CT motion correction, SEEG localization, and radiotherapy robustness metrics evaluate computational methods against biomedical measurements or definitions. The studies differ in data and clinical proximity, and none alone demonstrates prospective patient benefit.

## Open Problems and Research Directions

- **Test molecular-method transfer:** For ShEPhERD-score, evaluate target- and scaffold-held-out screening and prospective biochemical assays, with pre-specified calibration of scoring modes. For the cryo-EM method, test more particle sizes and acquisition conditions, improve denoising or estimate moments directly from raw images, and compare end-to-end time and reconstruction quality across pipelines.
- **Validate cross-modal and graph inference externally:** Replicate HIT-Fuse and CALIFUSE on independent institutions and cohorts, with missing-modality patterns fixed before analysis and calibration assessed on held-out data. For genomic phenotype hypotheses, test against patient-level phenotypes with blinded gene hold-outs to determine whether gains extend beyond the few high-variant genes noted by the authors.
- **Bridge simulation and clinical measurements:** Compare GraphEP predictions against independent experimental electrophysiology recordings across held-out anatomies; test head cone-beam CT motion correction on prospectively acquired scans and independent sites; assess MRE and SEEG methods prospectively, including error profiles relevant to downstream decisions. For radiotherapy metrics, a larger multi-center consensus study followed by prospective decision-impact evaluation would address the authors' stated validation gap.
- **Probe model assumptions with direct dynamics:** For stochastic reaction networks, compare predicted means and correlations against perturbation time series from low-copy-number biochemical systems. For the passive-walker result, pre-specify tests in larger human gait datasets and separate simulation-derived relationships from measured clinical outcomes.

## Takeaway

This batch has useful methods for molecular screening, stochastic reaction dynamics, cryo-EM initialization, motion correction, and multimodal biomedical inference. The collector found little direct external-attention evidence: the clearest signal is one current Semantic Scholar citation for the MRE paper, not a period gain or proof of broad popularity. Experimental and prospective validation remains uneven across the corpus.

## Method and sources

- **Window:** daily submission/revision interval 2026-11-18T19:00:00Z–2026-11-19T19:00:00Z; announcement batch date 2026-11-19, announced 2026-11-20T01:00:00Z. This is the latest available prior batch as of 2026-11-21; the broad arXiv query's newest matching records were dated 2026-11-19 and no newer batch was present for the current day. Snapshot: 2026-11-21T21:16:03Z. The attention signal file was generated at 2026-11-21T21:07:35Z.
- **Candidate pool:** started from `/home/yizhuan/.research/bio/daily/arxiv-trending-bio-daily-2026-11-19.signals.json`. The arXiv, Hugging Face, Hacker News, arXiv lookup, and Semantic Scholar sources all reported `status: ok` (signal-file counts: 12, 141, 35, 175, and 12 respectively). A broad configured-category API query returned 200 most-recent records (40,629 total), including 12 new submissions in the exact window. A separate `lastUpdatedDate` query returned 28 records for 2026-11-18–19; exact timestamp filtering found one additional in-window revision, `2611.23788v2`, omitted from the supplied signal pool. Its abstract page and revision metadata were verified, and a direct Semantic Scholar lookup returned 0 citations and 0 influential citations. Thus 13 papers qualified: 12 signal candidates plus that revision. No source error was reported; no row-level Hugging Face/Hacker News data was available for the added revision.
- **Ranking:** the collector score is its disclosed log1p-damped weighted sum. Its only non-zero citation count is one current Semantic Scholar citation for the MRE candidate; no citation gain during this window is inferred. Other positive scores are from cross-list breadth. Since attention evidence is sparse, entries are titled and ordered as notable papers by direct relevance and reported evidence, not as a popularity ranking. A zero means no attention signal was detected, not that the paper is unimportant.
- **Reading and evidence boundaries:** every selected arXiv abstract page was verified. The first three papers were also read in PDF form, including their introduction, results, and discussion/limitations where present. Author-reported in-silico, simulated, experimental, retrospective, and clinical-interview evidence is distinguished; this is not medical advice.
- **Coverage:** arXiv does not represent biomedical preprints comprehensively. This report excludes bioRxiv, medRxiv, and the broader medical literature; it is not a systematic review or clinical guideline.
- **Sources:** [configured arXiv API query](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200); [q-bio archive](https://arxiv.org/list/q-bio/current); [revisions updated Nov 18–19 in configured categories](https://export.arxiv.org/api/query?search_query=%28cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.SC+OR+cat%3Aq-bio.CB+OR+cat%3Aq-bio.TO+OR+cat%3Aq-bio.QM+OR+cat%3Acs.BI+OR+cat%3Aphysics.med-ph%29+AND+lastUpdatedDate%3A%5B202611180000+TO+202611192359%5D&sortBy=lastUpdatedDate&sortOrder=descending&start=0&max_results=200); each paper's verified abstract page is linked in its title. The signal file records the attention-source status and per-candidate scores.
