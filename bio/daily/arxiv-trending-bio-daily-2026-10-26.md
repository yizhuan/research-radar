# arXiv Biology & Biomedicine — Daily — 2026-10-26

## Headline

Monday’s arXiv biology/biomedicine announcement batch contains ten selected papers spanning clone-aware single-cell analysis, pediatric tumor splicing, protein design, and biomedical signal processing. Today’s agenda: what the papers measure, how far their evidence goes, and which validations remain. arXiv has no official trending chart; this is a relevance-ranked snapshot, not a measured popularity list. Biomedical preprints on arXiv are incomplete coverage of biology and medicine, and this is not a review of bioRxiv, medRxiv, or clinical evidence as a whole.

## Notable recent papers (ranked)

### 1. [Shared clones make random cell halves look reproducible in pooled screens](https://arxiv.org/abs/2610.32962)
- **Abstract:** The paper argues that shared descendants of transduced cells can make random halves of pooled single-cell screens appear reproducible, even for null perturbations, and that clone-separated or independently transduced replicates reduce this artifact.
- **Authors:** Xuanrui Huang
- **arXiv:** `2610.32962v1` (published 2026-10-23T17:53:14Z; categories: `q-bio.QM`)
- **Evidence for ranking:** A focused methodological study using null controls, clone-aware splits, and comparisons across 16 screens; code and results are public. Semantic Scholar listed 0 citations at the snapshot.
- **Claimed contribution:** The author reports near-universal null agreement under random halves in a primary T-cell screen, versus chance-level agreement between independent replicates, and finds that more cells do not remove the shared-clone component.
- **Caveat:** The size estimates vary by screen and cell type; many source screens lack clone labels, and some downstream model comparisons cover only a limited set of states and donors.
- **Announcement type:** new submission, 2026-10-26 batch
- **Themes:** Omics & single-cell methods; Bioinformatics & sequence analysis; Molecular & cell biology

### 2. [TAPESTRY: an interactive resource for exploring tumor-enriched splice junctions in pediatric brain tumors](https://arxiv.org/abs/2610.31816)
- **Abstract:** TAPESTRY is a searchable catalog of recurrent tumor-enriched splice junctions across pediatric brain-tumor histologies, with normal-brain comparisons and annotations intended to help prioritize candidate targets.
- **Authors:** Patricia J. Sullivan, Ryan J. Corbett, Chao Di, Alex Sickler, Aylar Babaei, Meghali Goswami, Jo Lynne Rokita
- **arXiv:** `2610.31816v1` (published 2026-10-22T18:53:50Z; categories: `q-bio.GN`)
- **Evidence for ranking:** The resource covers 45,430 junctions across 19 histologies and 1,962 RNA-seq specimens, including 1,272 independent primary tumors; S2 listed 0 citations at the snapshot.
- **Claimed contribution:** The authors provide filters, expression views, downloadable data, and an API to support prioritization of tumor-enriched and oncofetal splice events.
- **Caveat:** Junction evidence does not establish stable protein production or HLA presentation. The paper notes limited pediatric normal reference cohorts and heuristic enrichment cutoffs; experimental validation remains necessary.
- **Announcement type:** new submission, 2026-10-26 batch
- **Themes:** RNA & transcriptomics; DNA & genomics; Biomedical & translational medicine

### 3. [Computational De Novo Design of Miniprotein Candidate Neutralizers Targeting the IL-23 Cytokine Subunit p19](https://arxiv.org/abs/2610.32779)
- **Abstract:** The authors computationally design short protein candidates intended to occupy the IL-23 p19 receptor-binding surface and compare design pipelines using interface-focused structural scores.
- **Authors:** Raghav Paladugu, Fardina Fathmiul Alam
- **arXiv:** `2610.32779v1` (published 2026-10-23T15:26:49Z; categories: `q-bio.BM`)
- **Evidence for ranking:** The authors report 972 conventional designs and 50 interface-optimized designs, with five leads characterized; the arXiv comment says accepted as a short paper at IEEE BIBM 2026. S2 listed 0 citations at the snapshot.
- **Claimed contribution:** Their computational comparison finds no reliable predicted interface in the conventional set, while 42/50 BindCraft designs exceed the paper’s ipSAE 0.60 threshold.
- **Caveat:** These are predictions, not measured binders or neutralizers. The paper reports no affinity assay and uses one partly modeled p19 structure; its score bands are not calibrated for de novo binders.
- **Announcement type:** new submission, 2026-10-26 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 4. [U-NeXt: General-purpose event detection for neonatal EEG](https://arxiv.org/abs/2610.32811)
- **Abstract:** U-NeXt applies a shared semantic-segmentation architecture to neonatal EEG event detection, including seizures, artifacts, and low-voltage intervals.
- **Authors:** Robert Hogan, Sean R. Mathieson, Aurel Luca, Soraia Ventura, Sean Griffin, Geraldine B. Boylan, John M. O'Toole
- **arXiv:** `2610.32811v1` (published 2026-10-23T15:47:15Z; categories: `cs.LG`, `eess.SP`, `physics.med-ph`)
- **Evidence for ranking:** The paper reports three development datasets totaling 11,000+ EEG hours and two independent held-out seizure datasets comprising 130 neonates; S2 listed 0 citations at the snapshot.
- **Claimed contribution:** U-NeXt+ reached MCC 0.862 and 0.891 on the Helsinki and Cork held-out datasets, respectively, and the authors report higher sensitivity for short events than their task-specific baseline.
- **Caveat:** This is retrospective model evaluation, not evidence of improved outcomes or prospective clinical utility; performance in other hospitals and workflows remains unestablished.
- **Announcement type:** new submission (cross-listed), 2026-10-26 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 5. [A Multiscale Kinetic Model of DNA Damage Signalling and Repair under Combined Proton and Nanoparticle Exposure](https://arxiv.org/abs/2610.29157)
- **Abstract:** This revised model links proton and gold-nanoparticle exposure to double-strand-break induction, DNA-damage signaling, and several modeled repair pathways in human fibroblasts.
- **Authors:** Mushtaq Loan
- **arXiv:** `2610.29157v2` (first published 2026-10-21T03:48:03Z; latest revision 2026-10-23T04:38:44Z; categories: `q-bio.SC`)
- **Evidence for ranking:** A substantive v2 revision appeared in the current replacement list; its scope directly connects radiation physics with DNA repair mechanisms. S2 listed 0 citations at the snapshot.
- **Claimed contribution:** The author’s model identifies the starting fraction and slower resolution of complex lesions as key drivers of persistent modeled damage under high-LET, nanoparticle-enhanced exposure.
- **Caveat:** This is a kinetic model, not a new irradiation experiment. The author flags inconsistent repair-fidelity endpoints and says repair-fate predictions need independent measurements.
- **Announcement type:** revision, 2026-10-26 batch (v2 updated 2026-10-23)
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Quantitative methods

### 6. [Kinetic Proofreading Activation Times Beyond the Weibull Limit](https://arxiv.org/abs/2610.31788)
- **Abstract:** The authors derive a first-passage description of T-cell receptor activation that retains ligand dissociation and delineates when the commonly used Weibull approximation breaks down.
- **Authors:** Thomas Mourier, Cameron Hopkinson, Kenny Wong
- **arXiv:** `2610.31788v1` (published 2026-10-22T18:29:29Z; categories: `q-bio.QM`)
- **Evidence for ranking:** The work combines an exact continuous-time Markov-chain result with stochastic simulations and reports median errors under 2% in 19 of 25 tested parameter sets; S2 listed 0 citations at the snapshot.
- **Claimed contribution:** The authors introduce a dimensionless condition for the Weibull approximation and a closed-form alternative that accounts for dissociation and repeated binding attempts.
- **Caveat:** Evidence is mathematical and simulation-based; the tested parameter grid does not establish the model’s quantitative accuracy in living immune systems.
- **Announcement type:** new submission, 2026-10-26 batch
- **Themes:** Molecular & cell biology; Quantitative methods; Biomedical & translational medicine

### 7. [Video-rate quantitative phase and polarimetric imaging (QP2I) for label-free imaging of contracting muscle cells](https://arxiv.org/abs/2610.32756)
- **Abstract:** QP2I combines single-shot quantitative phase and polarization measurements on a standard DIC microscope to image structural and anisotropic changes in contracting muscle cells.
- **Authors:** Lucas Kreiss Roohian, Nachiket Pathak, David Ripp, Mitchell Harling, Nils Kronenberg, Marcel Schubert, Malte C. Gather
- **arXiv:** `2610.32756v1` (published 2026-10-23T15:00:24Z; categories: `physics.optics`, `q-bio.QM`)
- **Evidence for ranking:** The paper reports tests on simulations, reference targets, fixed muscle tissue, and living moving cells; its q-bio cross-list makes the biomedical application explicit. S2 listed 0 citations at the snapshot.
- **Claimed contribution:** The authors report video-rate, label-free phase and retardance readouts, including sarcomere length and retardance changes during cardiomyocyte contraction.
- **Caveat:** This is an imaging-method validation, not evidence of diagnostic performance or a physiological intervention benefit; the abstract does not specify cohort-scale or clinical validation.
- **Announcement type:** new submission (cross-listed), 2026-10-26 batch
- **Themes:** Medical physics & imaging; Molecular & cell biology; Quantitative methods

### 8. [OPTARI: An open-source software framework for clinical translation of optoacoustic imaging](https://arxiv.org/abs/2610.32468)
- **Abstract:** OPTARI is a graphical application for processing and analyzing optoacoustic-ultrasound studies, combining reconstruction, annotation, segmentation, and temporal/spectral analysis tools.
- **Authors:** Moritz Schillinger, Maximilian Bader, Adrian Buehler, Felix Wachter, Ferdinand Knieling, Vasilis Ntziachristos, Katharina Breininger
- **arXiv:** `2610.32468v1` (published 2026-10-23T10:35:06Z; categories: `cs.SE`, `cs.CV`, `physics.med-ph`)
- **Evidence for ranking:** The paper is cross-listed in medical physics, provides open-source code, and reports a comparison with expert muscle-tissue labels and sub-second batch processing; S2 listed 0 citations at the snapshot.
- **Claimed contribution:** The authors describe a vendor-format-aware GUI and report tissue segmentation comparable to expert labeling, with processing reduced from minutes to under one second per scan.
- **Caveat:** Ongoing clinical studies are not outcome evidence. The abstract does not provide cohort sizes or establish generalization across vendors, tissues, or acquisition protocols.
- **Announcement type:** new submission (cross-listed), 2026-10-26 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Bioinformatics & sequence analysis

### 9. [Multilevel Stochastic Plug-and-Play for Sparse-View CT Reconstruction](https://arxiv.org/abs/2606.24567)
- **Abstract:** The revised method accelerates stochastic plug-and-play CT reconstruction through wavelet multiresolution initialization and coarse-to-fine correction steps.
- **Authors:** Antoine De Paepe, Alexandre Bousse, Dimitris Visvikis
- **arXiv:** `2606.24567v3` (first published 2026-06-23T13:34:30Z; latest revision 2026-10-23T15:03:41Z; categories: `cs.CV`, `physics.med-ph`)
- **Evidence for ranking:** The v3 revision appeared in the current medical-physics replacement list; the abstract reports comparisons on two CT datasets with 20–50 projection views. S2 listed 0 citations at the snapshot.
- **Claimed contribution:** The authors report reconstruction quality comparable to evaluated stochastic plug-and-play baselines with generally lower runtime, and give convergence conditions for the fine-level iterations.
- **Caveat:** The abstract does not establish clinical image quality, patient outcomes, or radiation-dose benefit; it describes two-dataset reconstruction experiments.
- **Announcement type:** revision, 2026-10-26 batch (v3 updated 2026-10-23)
- **Themes:** Medical physics & imaging; Quantitative methods

### 10. [Probe Before You Edit: Probing-Guided Molecular Optimization for LLM Agents in Structure-Based Drug Design](https://arxiv.org/abs/2606.00555)
- **Abstract:** PROBE uses controlled ligand edits to estimate pocket-specific responses before an LLM-agent optimization loop chooses later molecular changes.
- **Authors:** Zaifei Yang, Weiyu Chen, Yaqing Wang, James Kwok
- **arXiv:** `2606.00555v3` (first published 2026-05-30T06:06:51Z; latest revision 2026-10-23T13:42:47Z; categories: `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** The v3 replacement is cross-listed in biomolecular modeling and the arXiv comment says accepted at NeurIPS 2026. Semantic Scholar listed 1 citation and 0 influential citations at the snapshot; this is a current total, not a gain in this batch.
- **Claimed contribution:** The authors report that PROBE’s site map and edit-response manual improve benchmark performance on CrossDocked2020 and address tradeoffs between binding-score and drug-likeness objectives.
- **Caveat:** The evaluation is benchmark/docking-based; it does not establish biochemical binding, developability, or in-vivo efficacy.
- **Announcement type:** revision, 2026-10-26 batch (v3 updated 2026-10-23)
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

## Trending Research Themes

This is a small batch, so these are recurring clusters in the selected papers, not evidence of a field-wide shift.

- **Computational models and design remain bounded by experimental validation:** the IL-23 miniprotein study, PROBE, the kinetic-proofreading model, and the DNA-damage repair model all use computational design or mechanistic models. Their reported results range from structural prediction and docking to analytical/simulation checks; none substitutes for binding assays or independent biological measurements.
- **Biomedical sensing and reconstruction are moving toward richer signals and more usable pipelines:** U-NeXt, QP2I, OPTARI, and sparse-view CT reconstruction address EEG, muscle-cell imaging, optoacoustic imaging, and CT. Their evidence is chiefly held-out dataset evaluation, optical/reference validation, or workflow benchmarking—not prospective clinical benefit.
- **Data context is central to biological interpretation:** Shared-clone effects warn that cell-level splits can exaggerate reproducibility, while TAPESTRY makes tumor splice-junction context and normal references more inspectable. These papers stress experimental units and reference coverage rather than merely scaling model complexity.

## Open Problems and Research Directions

- **Test designs at the bench:** For the IL-23 candidates, the authors propose expression and affinity assays, cell-based STAT3 blockade, and structural confirmation. A useful next step is to test several predicted leads against intact IL-23/p40, with blinded negative controls and orthogonal binding measurements. For DNA-damage modeling, independently measure lesion classes, repair fidelity, and cell survival to resolve the endpoint inconsistency the author reports.
- **Make reproducibility tests independent by design:** Shared-clone findings support separate transductions, null perturbations, and clone barcodes in follow-up Perturb-seq studies. Repeating this across more cell types and perturbation modalities would test how broadly the measured inflation estimates transfer.
- **Bridge cataloged transcripts to candidate antigens:** TAPESTRY’s own limitations motivate broader developmental and pediatric normal references, followed by validation of prioritized junctions at RNA, protein, and immunopeptidome levels. Junction recurrence alone is not evidence that a target is translated or presented.
- **Evaluate tools outside their development setting:** For U-NeXt and the imaging/reconstruction tools, prospective multi-site or multi-vendor tests, pre-specified comparator baselines, and explicit failure analyses would better establish robustness. These are research proposals, not claims of clinical readiness.

## Takeaway

The clearest biological signal in this batch is methodological: trustworthy validation depends on the right experimental unit and adequate biological context. Several computational designs and imaging pipelines report promising benchmark results, but the decisive gaps remain independent replication, experimental confirmation, and validation beyond the datasets used to build or tune the methods.

## Method and sources

- **Window:** daily; announcement batch dated 2026-10-26. Exact UTC snapshot: 2026-10-26T17:18:17Z. The included new-submission first-publication timestamps span 2026-10-22 through 2026-10-23 UTC; the listed revisions have latest-version timestamps on 2026-10-23 UTC.
- **Candidate collection:** traversed the Monday `q-bio/new` and `physics.med-ph/new` listings, including cross-list and replacement sections, then queried and deduplicated the configured arXiv category corpus by versionless ID. The explicit category query was `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`; current batch candidates and revisions were checked against their arXiv abstract pages. Abstract pages and PDFs were reviewed for the three highest-ranked papers where extraction was practical.
- **Ranking:** no official arXiv popularity ranking exists. Semantic Scholar Graph API totals were 0 citations for nine selected papers and 1 for PROBE, with 0 influential citations across the ten, at the snapshot. These are current totals, not announcement-window gains; the signal is too sparse to justify calling any paper “hottest.” The list is therefore ranked by direct biology/biomedicine relevance, reported validation breadth, substantive revisions, and cross-list or acceptance signals where available—not by inferred readership.
- **Coverage caveat:** arXiv is not a representative biomedical index. Many experimental and clinical preprints appear on bioRxiv or medRxiv, and purely clinical work here is not practice-changing evidence.
- **Sources:** [arXiv Quantitative Biology new listings](https://arxiv.org/list/q-bio/new), [arXiv Medical Physics new listings](https://arxiv.org/list/physics.med-ph/new), [arXiv API](https://export.arxiv.org/api/query), [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper). Canonical arXiv abstract links are attached to each paper title above.
