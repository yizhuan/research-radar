# Biology and Biomedicine on arXiv — Weekly Report (22 November 2026)

## Headline

**Nine notable papers; the clearest cluster is AI-assisted molecular modelling alongside early experimental and translational methods.** This report moves from protein modelling and antibody optimization to antiviral experiments, then to tissue imaging and computational cell biology. The requested calendar window is 15–22 November 2026, but the supplied latest available arXiv signal batch covers 12 November 19:00–19 November 19:00 UTC (announced 20 November 01:00 UTC; batch date 19 November). The nine selected records are first submissions dated 15–19 November; the 20–22 November portion is not represented in that source. arXiv has no official trending chart: this is an inferred ranking from incomplete attention signals and incomplete biomedical coverage, since many clinical and experimental preprints appear on bioRxiv or medRxiv instead.

## Notable recent papers (ranked; attention evidence is sparse)

The first five are ordered by the supplied collector score; the remaining four share a cross-list-only score and are ordered by demonstrated relevance. Scores are signals, not judgments of scientific quality. A zero or low score is not evidence that a paper is unimportant.

### 1. [Calpha: Toward Native Biomolecular Intelligence in a General-Purpose Language Model](https://arxiv.org/abs/2611.20986)
- **Abstract:** Calpha connects an LLM to a pretrained protein-structure head and reports single-chain folding results on FoldBench-334, CASP16 domains, and a CAMEO-style set.
- **Authors:** Yong Liu, Zhanpeng Shi, Peicong Lin, Zhenyi Zhong, Yizhou Dang, Wendi Wu, Haoling Li, Shuangjia Zheng
- **arXiv:** `2611.20986v1` (published 2026-11-16 12:17:37 UTC; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** Supplied score 9.963 (components: HF upvotes 8.124 from 14 upvotes/3 comments; 23 GitHub stars contribute 1.589; one cross-list contributes 0.25); Semantic Scholar snapshot: 0 citations. HF Papers listing: https://huggingface.co/papers/2611.20986.
- **Claimed contribution:** The authors report mean TM-scores of 0.808 on FoldBench-334, 0.635 on CASP16 domains, and 0.900 on a CAMEO-style PDB set. This is a computational structure-prediction result, not experimental validation of predicted structures.
- **Caveat:** This report covers the single-chain folding stage, not the broader future ambition of folding complexes. The paper notes that baseline systems differ in trainable weights, training duration, and crop length; it also reports lower accuracy on a 350-item MMLU-Pro subset after protein training.
- **Announcement type:** new submission, included in the 19 November 2026 weekly announcement window
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 2. [Discovery of new antiviral agents through artificial intelligence: in vitro and in vivo results](https://arxiv.org/abs/2611.22230)
- **Abstract:** A reinforcement-learning molecule-design workflow generated neuraminidase inhibitors, with two selected compounds reported active in enzyme, cell, and mouse experiments against influenza A and B.
- **Authors:** Roza Izmailyan, Mher Matevosyan, Hamlet Khachatryan, Anastasiya Shavina, Smbat Gevorgyan, Artur Ghazaryan, Irina Tirosyan, Yeva Gabrielyan, Marusya Ayvazyan, Boris Martirosyan, Vardan Harutyunyan, Hovakim Zakaryan
- **arXiv:** `2611.22230v1` (published 2026-11-17 05:22:24 UTC; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** Supplied score 6.688 (Semantic Scholar citations component 6.438; one cross-list 0.25); signal snapshot records 24 citations and 0 influential citations. These are citation totals, not gains during this week. The arXiv record says the accepted article was published in *Antiviral Research* 222 (2024), DOI: https://doi.org/10.1016/j.antiviral.2024.105818, so the citation total is not evidence of new attention to a 2026 study.
- **Claimed contribution:** The authors selected nine compounds for in-vitro testing and report that DS-22-inf-009 and DS-22-inf-021 inhibit influenza A/B neuraminidases, including H275Y strains, with cell-assay EC50 values of 0.29–2.31 μM; mouse experiments are also reported.
- **Caveat:** These are preclinical results, not human efficacy or safety evidence. The abstract does not give mouse group sizes; the arXiv upload is a 2026 posting of an already published 2024 paper.
- **Announcement type:** new submission, included in the 19 November 2026 weekly announcement window
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine

### 3. [Multimodal assessment of the skin biomechanical properties during wound healing and hyaluronic acid response](https://arxiv.org/abs/2611.20949)
- **Abstract:** In 12 rats followed over three weeks, the study compares an impact-based skin-mechanics method with two commercial devices during wound healing and after hyaluronic-acid injection.
- **Authors:** Arthur Bouffandeau, David Poisbleau, Mohand Ou Idir Ouidja, Patrick Karasinski, Dulce Papy, Charles-Henri Flouzat-Lachaniette, Romain Bosc, Barbara Hersant, Jean-Paul Meningaud, Guillaume Haiat
- **arXiv:** `2611.20949v1` (published 2026-11-16 11:59:32 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Supplied score 2.197, entirely from the Semantic Scholar citation component; snapshot records 2 citations and 0 influential citations. The direct Semantic Scholar Graph API check also returned 2 citations and 0 influential citations.
- **Claimed contribution:** The authors report that IBAM indicators vary with wound-healing time and after hyaluronic-acid injection, with changes broadly consistent with tissue stiffening during healing and reduced stiffness after injection.
- **Caveat:** This is a small animal study (12 rats), not clinical validation. The authors themselves call for further animal models or clinical studies.
- **Announcement type:** new submission, included in the 19 November 2026 weekly announcement window
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 4. [Physics-Informed Deep Learning for Shear Wave Speed Estimation in MR Elastography](https://arxiv.org/abs/2611.26111)
- **Abstract:** An end-to-end, physics-informed reconstruction and inversion pipeline estimates shear-wave speed from undersampled brain MR-elastography data.
- **Authors:** Stefan Martin, Jakob Schattenfroh, Patrick Schuenke, Felix Frederik Zimmermann, Ingolf Sack, Christoph Kolbitsch, Andreas Kofler
- **arXiv:** `2611.26111v1` (published 2026-11-19 13:39:46 UTC; categories: `eess.IV`, `cs.LG`, `physics.med-ph`)
- **Evidence for ranking:** Supplied score 1.886 (citation component 1.386; two cross-lists contribute 0.5); snapshot records 1 Semantic Scholar citation and 0 influential citations. The direct Graph API check matched those totals. The arXiv comment identifies an accepted journal version, DOI: https://doi.org/10.1109/TBME.2026.3666306.
- **Claimed contribution:** The authors report 30% lower NRMSE than total-variation minimization and SWS estimation at acceleration factors up to 19, with an additional in-vivo demonstration.
- **Caveat:** The main evaluation is retrospective and focused on brain MRE; the abstract does not report cohort size. The result is a reconstruction-method evaluation, not evidence of improved patient outcomes.
- **Announcement type:** new submission, included in the 19 November 2026 weekly announcement window
- **Themes:** Medical physics & imaging; Quantitative methods

### 5. [Using an instrumented hammer to predict the lateral hinge fracture in high tibial osteotomy: A cadaveric study](https://arxiv.org/abs/2611.20961)
- **Abstract:** An instrumented hammer and impact-signal algorithm are tested for identifying bone transitions and fracture during high-tibial osteotomy on cadaveric specimens.
- **Authors:** Claire Bastard, Manon Bas-Dit Nugues, Giuseppe Rosi, Charles-Henri Flouzat-Lachaniette, Arnaud Dubory, Guillaume Haiat
- **arXiv:** `2611.20961v1` (published 2026-11-16 12:06:29 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Supplied score 1.386, entirely from the Semantic Scholar citation component; snapshot records 1 citation and 0 influential citations.
- **Claimed contribution:** The authors report that the algorithm identified the surgeon's transition point within two impacts in 71% of medial and 81% of lateral cases, using 17 lower-limb specimens from nine human anatomical donors.
- **Caveat:** Cadaveric proof of concept only; it does not establish performance or safety in live surgery.
- **Announcement type:** new submission, included in the 19 November 2026 weekly announcement window
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 6. [Reasoning in the loop: antibody lead optimization by probing mechanism and measurement](https://arxiv.org/abs/2611.19812)
- **Abstract:** Two antibody-engineering campaigns combine model proposals, controlled variant libraries, assay review, and human/AI reasoning to identify and correct misleading thermal-stability metrics.
- **Authors:** Samuel Stanton, Aaron Solomon, Emily Delaney, Melanie Montgomery, Crystal Humphries, Timothy Acker, Ryan Henrici, Charbel Eid, Eddie Abrams, Peyton Greenside
- **arXiv:** `2611.19812v1` (published 2026-11-15 05:55:18 UTC; categories: `cs.LG`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** Supplied score 0.5, from two cross-lists only; snapshot records 0 Semantic Scholar citations. No matched HF or Hacker News attention was recorded for this candidate.
- **Claimed contribution:** Across seven rounds and about 1,010 design variants for an anti-albumin nanobody and an anti-mesothelin scFv, the authors report that scaffold-specific assay interpretation and protocol changes led to improved affinity, thermal stability, and aggregation while maintaining or improving yield and purity.
- **Caveat:** Two target/scaffold campaigns on one platform do not establish generality to other antibodies or assays; the abstract reports lead-property measurements, not clinical evidence.
- **Announcement type:** new submission, included in the 19 November 2026 weekly announcement window
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine

### 7. [A structure-based model of the bacterial chemosensory array reveals how the scaffolding protein CheW tunes sensory responses](https://arxiv.org/abs/2611.23921)
- **Abstract:** A structure-based Ising model explores how CheW placement and abundance alter cooperative signaling and predicted fluctuations in bacterial chemosensory arrays.
- **Authors:** David Hathcock, Yingxin Zheng, Yuhai Tu
- **arXiv:** `2611.23921v1` (published 2026-11-18 06:11:15 UTC; categories: `physics.bio-ph`, `cond-mat.stat-mech`, `q-bio.MN`)
- **Evidence for ranking:** Supplied score 0.5, from two cross-lists only; snapshot records 0 Semantic Scholar citations. No matched HF or Hacker News attention was recorded for this candidate.
- **Claimed contribution:** The authors say the lattice model reproduces previously reported CheW-dependent cooperativity and sensitivity changes, and predicts a shift from relaxational to oscillatory dynamics that could be tested with single-cell measurements.
- **Caveat:** The oscillatory behavior is a model prediction; it is not presented as a new experimental observation in this paper.
- **Announcement type:** new submission, included in the 19 November 2026 weekly announcement window
- **Themes:** Molecular & cell biology; Biochemistry & proteins

### 8. [OCCAM: Improved Single-Cell Representation Learning and Perturbation Effect Prediction](https://arxiv.org/abs/2611.21959)
- **Abstract:** OCCAM combines denoised cell representations with gene, text, and protein-sequence features to predict perturbation responses across cell contexts.
- **Authors:** Ihab Bendidi, Kian Kenyon-Dean, Alisandra K. Denton, Auguste Genovesio, Emmanuel Noutahi
- **arXiv:** `2611.21959v1` (published 2026-11-16 22:40:16 UTC; categories: `q-bio.QM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Supplied score 0.5, from two cross-lists only; snapshot records 0 Semantic Scholar citations. No matched HF or Hacker News attention was recorded for this candidate.
- **Claimed contribution:** The authors report improved cross-context few-shot perturbation-response matching against four retrained competitors and transfer baselines, while noting that accurate expression-level prediction remains difficult.
- **Caveat:** Evidence is computational benchmarking across assays and held-out cell lines; the abstract does not establish experimental validation of predicted perturbation effects.
- **Announcement type:** new submission, included in the 19 November 2026 weekly announcement window
- **Themes:** Omics & single-cell methods; Bioinformatics & sequence analysis

### 9. [Beyond AUC: Do Mammography Risk Models Predict When Cancer Occurs?](https://arxiv.org/abs/2611.20274)
- **Abstract:** A reanalysis argues that common discrimination metrics can miss whether mammography risk models correctly order cancer cases by time to diagnosis, and proposes a two-stage alternative.
- **Authors:** Svetlana Krasnova, Andrey Krylov, Dmitry Sorokin
- **arXiv:** `2611.20274v1` (published 2026-11-15 22:08:11 UTC; categories: `q-bio.QM`, `cs.CV`, `eess.IV`)
- **Evidence for ranking:** Supplied score 0.5, from two cross-lists only; snapshot records 0 Semantic Scholar citations. No matched HF or Hacker News attention was recorded for this candidate.
- **Claimed contribution:** On the CSAW-CC cohort with a five-year horizon, the authors report that two models' time-ordering c_time scores (0.51 and 0.55) were not significantly above chance, while a proposed two-stage model reached 0.58 with similar C-index to LMV-Net.
- **Caveat:** This is a retrospective reanalysis on one cohort; it does not demonstrate prospective clinical utility or establish performance in other screening populations.
- **Announcement type:** new submission, included in the 19 November 2026 weekly announcement window
- **Themes:** Biomedical & translational medicine; Quantitative methods

## Trending Research Themes

- **Protein models meet biological features and measurement quality.** Calpha explores an LLM-to-structure-head route, while the antibody campaigns show that assay definitions and raw measurement interpretation can constrain model-led optimization as much as the model itself. These are complementary computational and experimental reports, not independent replications.
- **Biomedical methods are being tested against concrete physical or biological endpoints.** The skin study compares three mechanical measurement approaches; the MR-elastography paper couples reconstruction to inversion; the osteotomy study uses impact signals to detect transitions and fracture. Their evidence remains animal, retrospective imaging, or cadaveric rather than clinical-outcome validation.
- **Context and evaluation design matter.** OCCAM tests perturbation prediction across cell contexts; the CheW paper identifies dynamic behaviors for future single-cell experiments; the mammography paper shows that ranking discrimination alone may not measure timing accuracy. The corpus supports a methods-oriented observation, not a field-wide shift.

## Open Problems and Research Directions

- **Separate model improvements from evaluation and training choices.** For Calpha, report matched compute/training and crop settings, stronger leakage-aware structural benchmarks, and experimentally resolved structures for prospective test proteins. For the antibody campaigns, repeat the assay-proxy calibration on additional scaffolds and independently validate the chosen thermal metrics.
- **Test transfer beyond the current experimental settings.** The antiviral candidates warrant independent replication across strains and laboratories, with complete dose, toxicity, and animal-group reporting before any human study is considered. The skin and osteotomy methods need larger, preregistered validation studies; for the hammer, the next relevant test is prospective intraoperative measurement against a prespecified fracture endpoint, not extrapolation from cadavers.
- **Validate inferred dynamics and risk estimates in external data.** For OCCAM, evaluate predicted perturbations in new cell lines with matched experimental follow-up; for CheW, test the predicted oscillatory dynamics using single-cell time-series measurements. For mammography timing, predefine the timing metric and assess calibration and discrimination in an independent longitudinal cohort.

## Takeaway

The strongest observed attention in this supplied batch went to a protein-folding/LLM integration paper and an already-published antiviral study. The remaining selected work is notable for specific experimental settings and careful evaluation questions, but sparse attention signals should not be mistaken for either low importance or strong validation. No patient-specific advice or practice-changing claims follow from this corpus.

## Method and sources

- **Requested window:** 2026-11-15 through 2026-11-22 inclusive (the last seven calendar dates at the snapshot). **UTC snapshot:** 2026-11-22 02:15:00 UTC.
- **Source-window caveat:** The supplied signal file was generated 2026-11-22 02:15 UTC but its arXiv announcement window is 2026-11-12 19:00 through 2026-11-19 19:00 UTC, announced 2026-11-20 01:00 UTC (announcement date 2026-11-19). It contains 86 arXiv candidates and does not include 20–22 November submissions. We filtered the candidate set to the requested dates where possible; the report therefore reflects available coverage only through 19 November, not a complete rolling seven-day corpus.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`; cross-listed papers were retained when clearly biomedical or molecular. All nine selected records were checked against their arXiv abstract pages linked above, including title, authors, version/date, abstract, and categories.
- **Ranking:** Started from `/home/yizhuan/.research/bio/weekly/arxiv-trending-bio-weekly-2026-11-19.signals.json`, as requested. Its candidate-level score uses weights: HF upvotes 3.0, Hacker News points 1.5, Hacker News comments 1.0, Semantic Scholar citations 2.0, influential citations 1.0, code stars 0.5, and cross-lists 0.25. The first five papers are ordered by the supplied composite score; the four papers tied at 0.5 on cross-list breadth are ordered by biological/biomedical relevance. Citation counts are totals, not period gains. No matched HF/HN activity was recorded for the latter four; a zero score or missing match is not evidence of unimportance.
- **Source availability:** The collected snapshot reports `ok` for arXiv (86), Hugging Face (278 records), Hacker News (91), arXiv lookup (364), and Semantic Scholar (86). A separate live Semantic Scholar Graph API check was rate-limited (HTTP 429) for most selected records; it succeeded for the skin and MRE papers only. The displayed ranking values use the supplied snapshot, not an inferred absence of attention. PDF text extraction was unavailable in this environment, so precise summaries rely on verified abstracts and metadata; the top-three full-text limitation check could not be completed.
- **Primary sources:** The linked arXiv abstract pages for each paper. Corroborating sources: HF Papers entry for Calpha (linked in its entry), journal DOI for the 2024 antiviral article and accepted MRE article (linked in entries), and the supplied signal JSON for attention and citation counts. arXiv is not a representative index of biomedical preprints; this report does not cover bioRxiv, medRxiv, or the biomedical literature as a whole.
