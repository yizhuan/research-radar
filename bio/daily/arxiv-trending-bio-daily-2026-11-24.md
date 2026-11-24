# arXiv Biology and Biomedicine — 2026-11-24 announcement batch

Ten notable recent papers span protein annotation, genome computing, molecular biophysics, antimicrobial resistance, and biomedical measurement and imaging. The ranking below is relevance-oriented, not a measured popularity chart: arXiv publishes no official trending ranking, this batch had no detected Hugging Face or Hacker News engagement for its candidates, and arXiv covers only part of biomedical research (much clinical and experimental work appears on bioRxiv or medRxiv).

## Top papers (ranked)

### 1. [General-purpose language models are neurosymbolic reasoners able to annotate proteins from sequence](https://arxiv.org/abs/2611.28529)
- **Abstract:** The authors tested general-purpose language models on protein-annotation tasks, including Pfam domains, catalytic-residue loss, and structure or activity prediction, reporting above-chance performance.
- **Authors:** Christopher J. Mungall; Marcin P. Joachimiak
- **arXiv:** `2611.28529v1` (published 2026-11-21 03:32:51 UTC; categories: `q-bio.GN`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** Signal score 0.50, entirely from 2 cross-lists; no HF upvotes or HN points/comments were recorded for this candidate.
- **Claimed contribution:** The preprint argues that generalist models can combine sequence and symbolic reasoning for protein annotation; its tests were above chance, and the authors report confident hallucinations as well as correct calls.
- **Caveat:** The authors did not benchmark against specialized tools, and the paper reports model predictions rather than experimental validation of protein function.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 2. [VEGA: A Scalable Software-Hardware Co-design for Genome Alignment using RVV Extension](https://arxiv.org/abs/2611.28741)
- **Abstract:** VEGA combines RISC-V vector instructions and a software-hardware design to accelerate dynamic-programming genome alignment, reporting up to 15.1× and 9.7× speedups for Edit Distance and Smith–Waterman versus the Ara2-RVV vector baseline.
- **Authors:** Weihong Xu; Shijie Xu; Qunyou Liu; Giovanni Ansaloni; Cheng Zhuo; David Atienza
- **arXiv:** `2611.28741v1` (published 2026-11-21 11:22:43 UTC; categories: `eess.SP`, `cs.AR`, `q-bio.GN`)
- **Evidence for ranking:** Signal score 0.50, entirely from 2 cross-lists; no HF upvotes or HN points/comments were recorded for this candidate.
- **Claimed contribution:** The preprint reports algorithm benchmarks and post-synthesis hardware results, including 1.0% area overhead against a standard RISC-V core.
- **Caveat:** These are computational and synthesis evaluations, not biological validation; the reported speedups are relative to the stated vector baseline.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 3. [Nonequilibrium fluctuations could explain the hot mitochondria paradox](https://arxiv.org/abs/2611.28225)
- **Abstract:** The authors propose that nonequilibrium cellular fluctuations and frequency-sensitive molecular thermometers could produce apparent mitochondrial temperature elevations without a true steady-state 10 K gradient.
- **Authors:** Matthew P. Leighton; Benjamin B. Machta
- **arXiv:** `2611.28225v1` (published 2026-11-20 19:00:47 UTC; categories: `cond-mat.stat-mech`, `physics.bio-ph`, `q-bio.SC`)
- **Evidence for ranking:** Signal score 0.50, entirely from 2 cross-lists; no HF upvotes or HN points/comments were recorded for this candidate.
- **Claimed contribution:** The preprint offers a physical explanation for previously reported apparent mitochondrial temperature differences, arguing that probe response to nonequilibrium fluctuations could account for them at biologically attainable power.
- **Caveat:** This is a theoretical proposal, not a new measurement or experimental test of the proposed probe mechanism.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** Molecular & cell biology; Quantitative methods

### 4. [FastCREST: GPU-Accelerated CREST Conformer Searches with Consistent Energies and Gradients](https://arxiv.org/abs/2611.28599)
- **Abstract:** FastCREST distributes and GPU-accelerates CREST molecular conformer searches, reporting faster evaluations and close agreement with CREST 3.0.2 for energies, gradients, and tested conformer searches.
- **Authors:** Supantha Dey; Nilusha L Kariyawasam; Ratul Chowdhury
- **arXiv:** `2611.28599v1` (published 2026-11-21 06:12:30 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Signal score 0.00, with 0 cross-lists and no detected HF or HN engagement. Zero indicates no collected attention signal, not lack of scientific importance; its placement reflects direct biochemical-method relevance.
- **Claimed contribution:** The preprint reports a complete 274-atom gallium(III)-peptide search taking 54.3 hours versus 321.5 hours for the stated CREST 3.0.2 run, with hardware differences noted by the authors.
- **Caveat:** The evidence is computational benchmarking on a limited set of molecules; speed and numerical agreement do not establish improved agreement with experimental conformations.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [Towards Edge Artificial Intelligence for Predicting Antimicrobial Resistance in Mycobacterium tuberculosis](https://arxiv.org/abs/2611.29143)
- **Abstract:** The authors combine 4-mer whole-genome features and a Random Forest to predict resistance across 20 antibiotics, reporting mean ROC AUC 0.82 on an independent test set.
- **Authors:** Nishat Tasnim; Faisal Ahmed; Rokan Uddin Faruqui
- **arXiv:** `2611.29143v1` (published 2026-11-22 01:51:43 UTC; categories: `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.25, entirely from 1 cross-list; no HF upvotes or HN points/comments were recorded for this candidate. The arXiv comment says it was accepted and presented at IEEE CSDE 2026.
- **Claimed contribution:** The preprint presents a lightweight genomic prediction pipeline intended for resource-constrained devices and reports the independent-test AUC above.
- **Caveat:** The abstract does not give cohort size or external-site composition; this is a model evaluation, not prospective clinical validation or evidence of improved treatment outcomes.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Biomedical & translational medicine

### 6. [A scalar arterial input function does not uniquely determine the perfusion residue: Theory and phantom MRI](https://arxiv.org/abs/2611.28378)
- **Abstract:** A flow model and 3 T straight-tube phantom experiment show that the same cross-sectionally averaged arterial input function can correspond to different tracer curves and perfusion residues.
- **Authors:** Yuyang Gan; Dominick Romano; Maneesh John; Renjiu Hu; Qihao Zhang; Benjamin Weppner; Alexey V. Dimov; Pascal Spincemaille; Yi Wang
- **arXiv:** `2611.28378v1` (published 2026-11-20 22:36:59 UTC; categories: `physics.med-ph`, `physics.flu-dyn`)
- **Evidence for ranking:** Signal score 0.25, entirely from 1 cross-list; no HF upvotes or HN points/comments were recorded for this candidate.
- **Claimed contribution:** The preprint derives the residue under stated flow assumptions and reports phantom enhancement differences at all 11 measurement stations across three boluses, with model-dependent tissue curves differing by up to 23.3% of the uniform-inlet peak.
- **Caveat:** The validation is a straight-tube phantom plus an idealized model, not a patient study; the authors' conclusion challenges interpretation of the scalar-input model rather than demonstrating a clinical effect.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** Medical physics & imaging; Quantitative methods

### 7. [MRI-Driven Dual-Energy CT Synthesis via Conditional Denoising Diffusion Probabilistic Models for MRI-only Radiotherapy and Protontherapy](https://arxiv.org/abs/2611.28294)
- **Abstract:** A conditional diffusion model synthesizes high- and low-energy CT images from MRI and, in retrospective paired head-and-neck proton-therapy data, outperformed two GAN baselines on reported image-quality measures.
- **Authors:** Juan Manuel Molina-Maza Chih-Wei Chang; David Viar-Hernandez; Zach Eidex; Mojtaba Safari; Shaoyan Pan; Juan Maria Perez-Moreno; Norberto Malpica; Angel Torrado-Carvajal; Borja Rodriguez-Vila; Xiaofeng Yang
- **arXiv:** `2611.28294v1` (published 2026-11-20 20:20:50 UTC; categories: `physics.med-ph`, `cs.AI`)
- **Evidence for ranking:** Signal score 0.25, entirely from 1 cross-list; no HF upvotes or HN points/comments were recorded for this candidate.
- **Claimed contribution:** The preprint reports mean absolute errors of 36.29±5.25 HU and 43.72±6.77 HU for the synthesized high- and low-energy CT, respectively, and compares against Pix2PixGAN and CycleGAN.
- **Caveat:** The abstract does not state cohort size and describes retrospective image validation, not prospective workflow or patient-outcome testing.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 8. [High-Resolution 3D Micro-CT Database of Transcranial Magnetic Stimulation (TMS) Coils for More Accurate Modelling, Technology Benchmarking, and Progress in Coil Design](https://arxiv.org/abs/2611.29051)
- **Abstract:** The authors use high-resolution micro-CT and electrical measurements to create a modelling dataset for 17 commercial TMS coils and demonstrate a CT-derived coil model in simulation.
- **Authors:** Maryam Farahmandrad; Max Koehler; Mahdi Bayati; Denis Goldnik; Sergiy Antonyuk; Stephan Goetz
- **arXiv:** `2611.29051v1` (published 2026-11-21 21:28:21 UTC; categories: `physics.med-ph`, `q-bio.NC`)
- **Evidence for ranking:** Signal score 0.25, entirely from 1 cross-list; no HF upvotes or HN points/comments were recorded for this candidate.
- **Claimed contribution:** The preprint provides coil geometry and impedance data, with micro-CT at 0.0495 mm resolution and a simulation example reporting differences from an existing SimNIBS coil model.
- **Caveat:** This is a hardware characterization and simulation resource; it does not test TMS effectiveness or safety outcomes in people.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** Medical physics & imaging; Quantitative methods

### 9. [Multi-Sensor Fusion for False-Alarm Reduction by Timed Electromechanical Corroboration](https://arxiv.org/abs/2611.29025)
- **Abstract:** In ECG recordings with injected beat-shaped artifacts, the authors report that adding mechanically sensed contraction timing reduced artifact acceptance while retaining most true beats.
- **Authors:** Zixuan Fu; Anthony Raffaele; Unnikrishna Pillai
- **arXiv:** `2611.29025v1` (published 2026-11-21 20:20:33 UTC; categories: `eess.SP`, `physics.med-ph`)
- **Evidence for ranking:** Signal score 0.25, entirely from 1 cross-list; no HF upvotes or HN points/comments were recorded for this candidate. The comment says it was submitted to IEEE Journal of Biomedical and Health Informatics.
- **Claimed contribution:** The preprint reports 6.2% of injected artifacts passing and 95% of true beats retained with a selected two-sensor setup, and says integer microcontroller decisions matched software.
- **Caveat:** The authors explicitly state that natural motion and clinical events remain untested; injected-artifact performance is not evidence of patient-monitor alarm performance.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 10. [Linking vascular pathways to organ anatomical structures in the Human Reference Atlas](https://arxiv.org/abs/2611.29215v1)
- **Abstract:** The authors add machine-readable crosswalks linking blood and lymphatic vascular pathways with anatomy, cataloguing 349 vessels and 663 links to 295 structures across 20 organs or body regions.
- **Authors:** Katherine Gustilo; Quinlan Cuddy; Avinash Boppana; Bruce W. Herr; Katy Börner; Griffin M Weber
- **arXiv:** `2611.29215v1` (published 2026-11-22 04:31:16 UTC; categories: `q-bio.TO`)
- **Evidence for ranking:** Signal score 0.00, with 0 cross-lists and no detected HF or HN engagement. Zero indicates no collected attention signal, not lack of scientific importance; its placement reflects direct relevance as a biomedical reference resource.
- **Claimed contribution:** The preprint reports algorithmic checks and review by 11 organ experts for the crosswalk tables and diagrams.
- **Caveat:** This is an anatomical knowledge and data-modeling contribution; it documents and organizes existing knowledge rather than experimentally validating vascular function.
- **Announcement type:** new submission, 2026-11-24 batch
- **Themes:** Biomedical & translational medicine

## Trending Research Themes

- **Computational methods are crossing biological scales.** Protein-sequence annotation with generalist language models (1), accelerated molecular conformer search (4), vectorized genome alignment (2), and edge-oriented tuberculosis resistance prediction (5) all make biological computation more accessible or faster. These are distinct evaluations, not a shared benchmark or evidence that one method class is generally superior.
- **Imaging papers focus on measurement and model fidelity.** The arterial-input-function analysis (6), MRI-to-dual-energy-CT synthesis (7), and TMS coil characterization (8) address assumptions or missing information that can affect downstream modeling. Their evidence ranges from a tube phantom to retrospective patient images and hardware-derived simulation; none establishes patient benefit.
- **Biomedical datasets and signal fusion offer infrastructure, not outcomes.** The ECG sensor-fusion study (9) uses injected artifacts, while the Human Reference Atlas crosswalk (10) organizes anatomical relationships. These may support later validation but do not themselves show improved clinical outcomes.
- **A theoretical explanation is proposed for mitochondrial temperature measurements.** Leighton and Machta (3) connect nonequilibrium fluctuations to probe response; experimental corroboration remains a separate step.

## Open Problems and Research Directions

- **Test sequence-model annotation against established tools and blinded assays.** Mungall and Joachimiak (1) note no comparison with specialized tools and report confident hallucinations. A useful next evaluation would use a held-out, experimentally characterized protein set, compare calibrated predictions with specialist pipelines, and audit false-positive confidence.
- **Establish transportability for tuberculosis resistance prediction.** Tasnim et al. (5) report an independent test set but the abstract does not specify cohort size or composition. Follow-up could test geographically and temporally separate isolates, report per-drug calibration and subgroup performance, and measure end-to-end edge-device latency; prospective use would require separate clinical evaluation.
- **Validate image-model assumptions beyond controlled or retrospective settings.** The perfusion phantom (6) motivates testing inlet tracer profiles under more realistic vascular conditions; the MRI-to-DECT model (7) needs external-site and prospective dose-calculation evaluation; the TMS coil dataset (8) can be assessed through independent field measurements. These are research proposals, not claims of readiness.
- **Probe the proposed mitochondrial mechanism directly.** Leighton and Machta (3) offer a theoretical account. Experiments could vary probe frequency response and cellular metabolic conditions while measuring heat transfer independently, to distinguish actual temperature gradients from frequency-dependent apparent signals.

## Takeaway

This batch contains several technically specific computational and measurement contributions, but the attention evidence does not support a popularity ranking: no candidate had detected HF or HN engagement, and citation corroboration was unavailable. Treat these as relevant new preprints with early computational, theoretical, phantom, or retrospective evidence—not established clinical findings.

## Method and sources

- **Window:** Daily; arXiv submission window 2026-11-20 19:00:00 UTC through 2026-11-23 19:00:00 UTC. Latest announcement batch: 2026-11-24 at 01:00 UTC. This is the current batch, not a prior-batch fallback. Snapshot taken 2026-11-24 03:09:05 UTC.
- **Candidate corpus:** The supplied signals file `arxiv-trending-bio-daily-2026-11-24.signals.json`; 13 candidates collected from the configured category listing and window-discussion pool. Category query: `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`. The selected papers were individually checked against their arXiv abstract pages and API metadata; pages for IDs 2611.29219 and 2611.29215 required the explicit v1 URL during verification.
- **Ranking:** Signals file reports `with_attention: 0`. Its selected-candidate scores are cited per paper and derive only from listed cross-list breadth (0.50 for two, 0.25 for one, 0.00 for none); no HF upvotes or HN points/comments were recorded for these candidates. Zero is not evidence of unimportance. With no detected external attention, the list is labeled and ordered by relevance to the requested biology/biomedicine scope, using cross-list breadth only as a secondary signal. No numeric trend score is introduced here.
- **Sources and availability:** arXiv listing and lookup status were `ok` (13 window candidates; 97 lookups). Hugging Face and Hacker News collectors returned `ok` (78 and 19 collected records respectively), but none of these candidates had a recorded attention value. Semantic Scholar returned an HTTP 400 error, so citation counts and influential-citation corroboration were unavailable and are not treated as zero. arXiv is not a representative index of biomedical research; clinical and experimental preprints may instead appear on bioRxiv or medRxiv.
- **Primary sources:** arXiv abstract pages linked above (each entry links to its canonical abstract URL); versioned metadata and abstracts checked through the arXiv API. All ten entries are v1 new submissions in the 2026-11-24 announcement batch. No patient-specific advice or clinical recommendations are offered.
