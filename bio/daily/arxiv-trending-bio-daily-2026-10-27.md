# arXiv Biology & Biomedicine — Daily Brief (27 October 2026)

## Headline

The latest 27 October announcement batch contains six verifiable biology and biomedical papers in the configured arXiv categories. The clearest pattern is computational methods tied to experimental or measurement work—DNA read reconstruction, label-free live-cell imaging, and radionuclide production—alongside cardiovascular and cell-growth models. Spoken agenda: what is measured versus simulated, and which validation gaps remain. This is a relevance-ranked “notable recent papers” list, not a popularity chart: arXiv has no official trending chart, and its biomedical coverage is incomplete compared with bioRxiv, medRxiv, and the wider medical literature.

## Notable recent papers

Ranked by direct biology/biomedicine relevance and the nature of author-reported evidence, not by presumed readership. Attention signals are sparse for this very recent batch; no citation momentum or readership claim is made. New submissions and revisions are distinguished below.

### 1. [ACOR: incremental evidence accumulation towards real-time DNA storage reconstruction](https://arxiv.org/abs/2610.36500)
- **Abstract:** ACOR incrementally accumulates evidence from sequencing reads and reconstructs DNA-storage sequences at cluster closure, with tests on simulated and real datasets including the authors’ own short-read NGS library.
- **Authors:** Linxuan Han, Huaming Wu, Shi Jia, Guanjin Qu
- **arXiv:** `2610.36500v1` (published 2026-10-27 01:58:03 UTC; categories: `cs.IR` (primary), `q-bio.GN`)
- **Evidence for ranking:** Cross-listed in genomics; the paper reports real and simulated DNA-storage evaluations, including a wet-lab NGS library with 96,055 designed sequences and 17.7 million assigned read observations.
- **Claimed contribution:** The authors report 99.9844% exact reconstruction at k=15 on their full NGS library. Their streaming design stores k-mer transition and boundary evidence before a single consensus decoding step, avoiding repeated full-cluster reconstruction as reads arrive.
- **Caveat:** Current evaluations receive already-assigned clusters, known design lengths, and externally determined cluster closure; therefore they do not yet test an end-to-end live pipeline. The paper also identifies difficult long-sequence errors and reference-free parameter selection as open issues.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

### 2. [Video-rate quantitative phase and polarimetric imaging (QP2I) for label-free imaging of contracting muscle cells](https://arxiv.org/abs/2610.32756)
- **Abstract:** QP2I combines quantitative phase and polarimetric imaging in a single-shot, video-rate setup based on a differential-interference-contrast microscope and polarization camera, demonstrated on reference targets, fixed tissue, and live cardiomyocytes.
- **Authors:** Lucas Kreiss Roohian, Nachiket Pathak, David Ripp, Mitchell Harling, Nils M. Kronenberg, Marcel Schubert, Malte C. Gather
- **arXiv:** `2610.32756v3` (published 2026-10-27 10:10:06 UTC; categories: `physics.optics` (primary), `q-bio.QM`)
- **Evidence for ranking:** A substantive v3 revision in the batch; authors report validation on simulations, reference targets, fixed muscle tissue, and living cells, with video-rate acquisition reported up to 70 fps.
- **Claimed contribution:** The preprint combines a regularized phase-reconstruction method with Stokes-based retardance reconstruction to provide structural and functional optical readouts, including sarcomere length and retardance changes during contraction.
- **Caveat:** Evidence is optical-method validation and cell-level demonstration, not clinical testing. The authors note limitations including phase-gradient wrapping, ambiguities in strongly birefringent samples, and reduced effective resolution from the polarization-camera pixel arrangement.
- **Announcement type:** revision (v3; first submitted 23 October 2026), 27 October 2026 batch
- **Themes:** Medical physics & imaging; Molecular & cell biology; Quantitative methods

### 3. [Optimization of 99mTc proton-induced production by means of cross-section measurements of technetium radioisotopes from molybdenum targets](https://arxiv.org/abs/2610.36949)
- **Abstract:** The authors measure proton-induced reaction cross-sections on solid molybdenum targets and use them to assess technetium radionuclide production and optimize a cyclotron-based route to 99mTc.
- **Authors:** Dellepiane Gaia, D'Uva Sofia, Eggimann Lars, Gottstein Alexander, Juillerat Samuel, Kasanda Eva, Mateu Isidre, Scampoli Paola, Kadenko Ihor, Braccini Saverio
- **arXiv:** `2610.36949v1` (published 2026-10-27 10:10:48 UTC; categories: `nucl-ex` (primary), `physics.med-ph`)
- **Evidence for ranking:** Cross-listed in medical physics; the abstract and full paper report measured reaction cross-sections and production tests, rather than only a computational proposal.
- **Claimed contribution:** The authors identify approximately 16 MeV protons and a roughly 0.5 mm highly enriched 100Mo target as suitable conditions. They calculate about 1.7 GBq/μA after a 10-hour irradiation while estimating radionuclidic purity within European Pharmacopoeia limits.
- **Caveat:** The yield is calculated from the study’s measurements and the production tests are feasibility evidence; this does not establish routine-scale supply, clinical deployment, or patient outcomes.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 4. [Bodyseismography (BSG): Theoretical Foundation and Numerical Modeling](https://arxiv.org/abs/2610.35844)
- **Abstract:** BSG models how cardiac excitation and body/bed transmission jointly shape contactless cardiovascular vibration measurements, with participant-specific numerical modeling and controlled stroke-volume perturbations.
- **Authors:** WenZhan Song, Yuanyuan Zhang, Yuyan Wu, Sahas Biddappa, Yida Zhang, Jiayu Chen, Zixuan Zeng, Yixuan Li, Jiahui Li, Fei Dou, Zhenlin An, Hae Young Noh, Young Kwon
- **arXiv:** `2610.35844v2` (published 2026-10-27 03:59:10 UTC; categories: `eess.SP` (primary), `physics.med-ph`)
- **Evidence for ranking:** Substantive v2 revision; the numerical analysis covers 27 participants and reports matched-window waveform correlations for vertical and planar-sum channels.
- **Claimed contribution:** The authors report median Pearson correlations of 0.865 (vertical) and 0.682 (planar-sum) for waveform reconstruction; modeled transmission reversed a vertical feature association in 8 of 27 participant-specific transfer models.
- **Caveat:** This is a theoretical and numerical modeling study, not a prospective clinical validation of stroke volume, cardiac output, or blood-pressure measurement. The reported correlations concern waveform reconstruction in the modeled setting.
- **Announcement type:** revision (v2; first submitted 26 October 2026), 27 October 2026 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 5. [Multiscale MIGHT: Modeling Local and Systemic Particle Transport in the Cardiovascular System](https://arxiv.org/abs/2610.35618)
- **Abstract:** Multiscale MIGHT models signaling-molecule transport through branched local vessels and closed-loop systemic circulation, incorporating organ clearance and chemical degradation.
- **Authors:** Theofilos Symeonidis, Timo Jakumeit, Fardad Vakilipoor, Robert Schober, Maximilian Schäfer
- **arXiv:** `2610.35618v2` (published 2026-10-27 09:09:33 UTC; categories: `q-bio.QM`)
- **Evidence for ranking:** Substantive v2 revision; the authors compare the closed-loop approximation against COMSOL finite-element simulations and report whole-body simulations across transmitter locations and signaling-molecule species. The arXiv comment says the work was submitted to IEEE ICC 2027.
- **Claimed contribution:** The model joins vessel-level topology with a whole-body circulation representation. Its simulations predict that later recirculation passes become dispersed and are governed mainly by systemic organ clearance and degradation rather than local vessel geometry.
- **Caveat:** Validation is against numerical simulation, while the whole-body examples are model-based; the paper does not report biological tracer experiments. The systemic circulation is represented with lumped organ blocks outside the detailed local network.
- **Announcement type:** revision (v2; first submitted 26 October 2026), 27 October 2026 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 6. [Stationary Action Principles for Neuronal Growth](https://arxiv.org/abs/2610.36463)
- **Abstract:** The paper develops stochastic and mechanics-based variational models for axonal growth on patterned or stiffness-varying substrates, predicting most-probable paths and turning behavior at stiffness boundaries.
- **Authors:** Nathan Brodeur, Cristian Staii
- **arXiv:** `2610.36463v1` (published 2026-10-27 01:15:25 UTC; categories: `q-bio.CB` (primary), `nlin.AO`, `q-bio.NC`, `q-bio.QM`)
- **Evidence for ranking:** Cross-listed across cell behavior, quantitative biology, and neuronal research; the contribution offers explicit, testable trajectory predictions linking drift, diffusion, substrate stiffness, traction, and growth direction.
- **Claimed contribution:** The authors derive a stochastic path action for growth on periodic micropatterns and a Fermat-like action for stiffness-dependent traction, including an approximate Snell-like relation and a critical-angle condition.
- **Caveat:** These are theoretical/model-derived predictions, not new neuronal-growth experiments. The stochastic and quasi-static descriptions have distinct assumptions and validity regimes, so experimental agreement remains to be established.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Molecular & cell biology; Quantitative methods

## Trending Research Themes

These are recurring motifs in this six-paper selection, not evidence of a field-wide shift.

- **Computation paired with measurement:** ACOR is evaluated on sequencing reads from a wet-lab DNA-storage library; QP2I is tested on fixed tissue and living cardiomyocytes; and the 99mTc paper reports cross-section measurements plus production tests. The validation types differ, from sequence reconstruction metrics to optical and radionuclide-production tests.
- **Models connecting local measurements to system-level biology:** BSG examines how transmission affects cardiovascular vibration signals, while Multiscale MIGHT connects local vessel structure to whole-body signaling-molecule transport. Both are modeling contributions; BSG’s reported participant-specific fits and MIGHT’s COMSOL comparison are not equivalent to independent biological validation.
- **Mechanics as a determinant of biological trajectories or signals:** BSG and Stationary Action Principles study how mechanical transmission or substrate stiffness changes observed cardiovascular signals or axonal paths. The latter remains a theoretical proposal, so this is a shared modeling lens, not a demonstrated common biological effect.

## Open Problems and Research Directions

Several follow-ups are supported by limitations raised in the papers or by their evidence boundaries. For ACOR, test streaming end-to-end with online read assignment and cluster closure, then evaluate reference-free parameter selection and hard nanopore error cases across independent datasets. For QP2I, characterize phase-wrap and birefringence ambiguities across a larger panel of cell types, and compare long-duration sarcomere and retardance measurements against orthogonal reference assays. For the 99mTc route, independent cyclotron/target replication could quantify variation in measured cross-sections, radionuclidic purity, and realized yield under the proposed irradiation conditions. BSG would benefit from a held-out cohort with simultaneous reference hemodynamic measurements to test whether its modeled features generalize beyond waveform reconstruction. Multiscale MIGHT’s recirculation predictions could be compared with controlled tracer-transport measurements across vessel geometries and clearance conditions. Finally, controlled stiffness-gradient experiments could test the neuronal-growth model’s predicted turning paths and critical-angle behavior. These are research proposals, not clinical recommendations.

## Takeaway

Today’s batch is notable for methods that connect computation to biological or physical measurements, but their evidence spans very different levels: wet-lab sequencing, optical cell demonstrations, production tests, numerical modeling, and theory. The most promising next step across the set is independent validation under less controlled, more complete biological conditions; none of these papers can be called popular from the available attention evidence.

## Method and sources

- **Window:** daily; latest announcement batch dated 2026-10-27. Batch window: 2026-10-27 through 2026-10-27. Snapshot: 2026-10-28 01:20 UTC. This uses the latest available batch, not a prior-batch substitute. New submissions were first submitted on 27 October; revisions are labeled with their original submission dates and latest version timestamps.
- **Candidate pool:** one descending arXiv API query across the configured corpus—`q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`—returned 200 records down to 9 October, extending beyond the selected batch. Records first submitted or revised on 27 October were deduplicated by versionless ID; six relevant candidates with retrievable arXiv abstract pages were retained. One API result whose purported arXiv abstract page returned “article not found” was excluded. All retained abstract pages were checked; PDFs were read for ACOR, QP2I, and the 99mTc production study.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date descending. Category coverage is limited to this configured arXiv corpus; it is not representative of biomedical preprints generally.
- **Ranking:** arXiv has no official trending or readership ranking. Because independent discussion and verified attention/citation signals were sparse for this fresh batch, the list is ranked by direct relevance and the kind of author-reported evidence, with recency used only as context. No readership, download, or citation-momentum claim is made; no citation counts are reported.
- **Coverage caveat:** Many experimental and clinical preprints appear on bioRxiv or medRxiv instead. This report is not a comprehensive review, clinical guideline, or patient-specific advice.
- **Primary sources:** [q-bio.BM recent](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN recent](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN recent](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC recent](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB recent](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO recent](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM recent](https://arxiv.org/list/q-bio.QM/recent), [cs.BI recent](https://arxiv.org/list/cs.BI/recent), [physics.med-ph recent](https://arxiv.org/list/physics.med-ph/recent), and the linked arXiv abstract pages above. PDFs for the three papers read in depth: [ACOR](https://arxiv.org/pdf/2610.36500), [QP2I](https://arxiv.org/pdf/2610.32756), [99mTc production](https://arxiv.org/pdf/2610.36949).
