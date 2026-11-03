# arXiv Biology and Biomedicine — Daily — 2026-11-02

## Headline

Latest available biology/biomedicine announcement batch: Monday, 2 November 2026. Seven papers are highlighted, led by assay-aware small-molecule design and computational methods for regulatory DNA and biochemical networks; a smaller set reports new assay or human-imaging data. Agenda: begin with experimental molecule design, move through DNA and network modelling, then close with imaging, PET, and DNA-assay methods. Snapshot: 2026-11-03 01:18:57 UTC; the current day has no batch yet, so this uses the prior announcement batch. arXiv has no official trending chart, and this is an inferred relevance ranking from incomplete biomedical coverage—not a popularity measure or evidence of validity.

## Notable recent papers

### 1. [D2ML: Models for Direct-to-Biology Small Molecule Screening](https://arxiv.org/abs/2610.41070)
- **Abstract:** Assay-aware models combine crude and purified direct-to-biology screening data, and a prospective campaign used model-selected compounds to extend the measured ROS1 potency/selectivity frontier.
- **Authors:** AkshatKumar Nigam, Neri Amara, Hillary Dequina, Dyana Kenanova, Seth Malmersjo, Fiorella Ruggiu, Raymond V. Fucini, Jack Sadowsky, Stig K. Hansen, Imran S. Haque
- **arXiv:** `2610.41070v1` (published 2026-10-29 23:33:05 UTC; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** The authors report synthesis and testing of 84 prospectively selected compounds; the strongest reported compound had ROS1 IC50 14.7 nM and 233-fold selectivity over TRKB. The arXiv comment lists the NeurIPS 2026 AI for Drug Discovery workshop.
- **Claimed contribution:** The authors say tailoring model objectives to each assay stage and sharing information across stages improves prediction from heterogeneous screening data and supports multi-objective compound selection.
- **Caveat:** The study uses one pyrimidine core and a kinase discovery program; the authors note the purified evaluation sets are small and call for broader chemistries and targets. These are compound-assay results, not clinical evidence.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine

### 2. [Locality-Controlled Out-of-Distribution Guidance for Robust Regulatory DNA Sequence Design](https://arxiv.org/abs/2610.41736)
- **Abstract:** LocoGen guides a frozen DNA diffusion model by protecting inferred motif positions and applying out-of-distribution damping to background sequence, seeking a balance of predicted activity, novelty, and plausibility.
- **Authors:** Dabin Jeong, Marwane Bourdim, Mo Lotfollahi
- **arXiv:** `2610.41736v1` (published 2026-10-30 13:44:07 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Accepted to NeurIPS 2026 per the arXiv comment; evaluated against held-out prediction oracles using a benchmark of about 700,000 enhancer sequences from HepG2, K562, and SK-N-SH cells, generating 640 sequences per method.
- **Claimed contribution:** The authors report that localized guidance reaches a property–novelty–plausibility region that tested baselines miss, under their computational evaluation protocol.
- **Caveat:** This is computational generation and re-scoring, not a wet-lab test of the generated sequences. The authors tested one masked-diffusion backbone and explicitly call for experimental validation and comparisons with other backbones.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Bioinformatics & sequence analysis

### 3. [Co$^2$ODE: Conditionally Coarse-Grained Model Discovery for Rewiring in Biochemical Networks](https://arxiv.org/abs/2610.41634)
- **Abstract:** Co$^2$ODE learns context-specific marker selection and a latent closure term to model signalling dynamics from single-cell phosphoproteomic measurements.
- **Authors:** Theodore de Pomereu, Fabian Fröhlich
- **arXiv:** `2610.41634v1` (published 2026-10-30 12:10:55 UTC; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** The study uses a published mass-cytometry dataset across 30 single-gene overexpression contexts, reducing a 30-marker panel to a 10-dimensional state with predictive accuracy comparable to a full-panel neural ODE.
- **Claimed contribution:** The authors present conditional coarse-graining as a way to expose context-dependent marker selection while preserving prediction of a signalling readout.
- **Caveat:** Predictive fit does not identify the underlying network: the paper reports that prior scores can shift the inferred structure without materially changing fit, and its own limitations note that recovered couplings are not reproducible across seeds. The study is not a causal demonstration of network rewiring.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Molecular & cell biology; Quantitative methods; Omics & single-cell methods

### 4. [Quantitative Ultrasound Characterizes Perfusion Trajectories in Healthy and Inflamed Gingival Wound Healing](https://arxiv.org/abs/2610.41897)
- **Abstract:** A longitudinal ultrasound analysis estimates gingival perfusion after extraction and compares healing trajectories at visits classified as healthy or inflamed.
- **Authors:** Haowei Tai, Oscar Duran-Garnica, Karen Villarreal, Hsun-Liang Chan, Oliver D. Kripfgans
- **arXiv:** `2610.41897v1` (published 2026-10-30 15:35:27 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** The cohort comprised 51 patients followed from two weeks to three months after extraction; ultrasound-derived perfusion was compared with laser-speckle imaging, and automated region segmentation had a reported mean Dice score of 0.98.
- **Claimed contribution:** The authors report that velocity-weighted color-pixel density tracked perfusion changes and was higher at recovery visits classified as inflamed than at healthy visits.
- **Caveat:** This is a small observational imaging cohort, not evidence of improved treatment decisions or patient outcomes. The reported laser-speckle correlation was not statistically clear in the inflamed visits.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 5. [A General-Purpose Adaptable Foundation Model for Total-Body PET Kinetic Modelling](https://arxiv.org/abs/2610.41093)
- **Abstract:** LoRACM adapts a pretrained consistency model with low-rank updates to estimate posterior distributions for total-body PET kinetic models across tracer, protocol, and modelling settings.
- **Authors:** Yun Zhao, Qinlin Gu, Andrew J. Reader, Yanan Fan, Georgios I. Angelis, Katya Amadita, Kevin J. Chung, Xiaoyu Duan, Benjamin A. Spencer, Guobao Wang, Steven R. Meikle
- **arXiv:** `2610.41093v1` (published 2026-10-30 00:24:58 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** The authors report three adaptation settings on simulated and human data, each trained with 50,000 simulated pairs; human estimates were compared with non-negative least-squares fitting.
- **Claimed contribution:** The authors report adaptation in under three hours on one A100 GPU, simulation agreement with MCMC reference posteriors, and human-data estimates comparable to fitting baselines.
- **Caveat:** The abstract does not state the human cohort sizes, and agreement with a fitting baseline is not clinical validation or proof of improved patient care. The paper is submitted to a journal, not reported as accepted.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Medical physics & imaging; Quantitative methods; Biomedical & translational medicine

### 6. [PCR-ALERA: A PCR-ELISA analogue but antibody-free DNA detection system](https://arxiv.org/abs/2610.40262)
- **Abstract:** PCR-ALERA couples PCR-amplified DNA to an activator peptide that reactivates papain, producing a fluorescent readout without antibody handling.
- **Authors:** Miles Bonenberger, Roland Krämer
- **arXiv:** `2610.40262v1` (published 2026-10-29 15:25:37 UTC; categories: `q-bio.QM`)
- **Evidence for ranking:** The paper describes a biochemical assay workflow and reports an overall run time of about four hours including PCR, directly relevant to DNA detection and assay design.
- **Claimed contribution:** The authors propose an antibody-free microplate alternative to PCR-ELISA based on modified-nucleotide incorporation, click-linked peptide activation, and a fluorogenic papain substrate.
- **Caveat:** The abstract does not report limits of detection, specificity, sensitivity, or head-to-head performance, so comparative analytical performance and clinical utility remain unestablished.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** DNA & genomics; Molecular & cell biology; Biomedical & translational medicine

### 7. [Transmission and filtering of stochastic rhythms in bursty gene expression](https://arxiv.org/abs/2610.41109)
- **Abstract:** An analytical framework derives how degradation, transcriptional bursting, and upstream timing variability affect the transmission of stochastic regulatory rhythms to gene expression.
- **Authors:** Chen Jia
- **arXiv:** `2610.41109v1` (published 2026-10-30 00:57:42 UTC; categories: `q-bio.MN`, `physics.bio-ph`)
- **Evidence for ranking:** The paper derives autocorrelation and power-spectrum transmission relations and reports that its predicted degradation threshold separates all ten pulsing and non-pulsing p53 target proteins classified in earlier experiments.
- **Claimed contribution:** The author proposes an analytical theory for conditions under which downstream genes preserve or filter stochastic rhythmic signals.
- **Caveat:** This is mainly theoretical; the ten-protein comparison uses previously published experimental classifications and does not supply new experimental validation.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Gene regulation & epigenetics; Molecular & cell biology; Quantitative methods

## Trending Research Themes

- **Design methods paired with biological measurements:** D2ML combines assay-specific prediction with prospective compound synthesis and testing. By contrast, LocoGen's DNA designs are assessed with computational oracles; the paper itself identifies wet-lab validation as a next step. These are related model-guided design efforts, but their validation levels differ.
- **Learning biochemical dynamics without overclaiming mechanism:** Co$^2$ODE and the stochastic-rhythm analysis formalize signalling and gene-expression dynamics. Co$^2$ODE exposes a specific identifiability problem in its phosphoproteomic data, while the rhythm theory checks a derived threshold against prior p53 classifications.
- **Quantitative biomedical measurement and assay translation:** The gingival-ultrasound and PET papers report human-data evaluations; PCR-ALERA describes a biochemical assay concept. The evidence ranges from an observational cohort to fitting-baseline comparisons and an assay workflow, not clinical-effectiveness studies.

## Open Problems and Research Directions

- **LocoGen (author-stated):** Evaluate alternative generative backbones and test generated sequences experimentally. A concrete follow-up would synthesize a prespecified set of candidates and measure expression in matched MPRA assays across the represented cell lines, retaining an independent evaluation oracle.
- **Co$^2$ODE (author-stated):** The current data do not identify the underlying network structure. Targeted perturbations that break correlations among candidate markers, followed by held-out prediction and independent pathway assays, could test whether selected markers are mechanistically informative.
- **D2ML (author-stated):** Repeat prospective selection across additional chemical scaffolds and targets with larger purified-compound sets to test how far the ROS1/TRKB result generalizes.
- **Ultrasound and PET (synthesis):** Independent cohorts and multi-site/scanner repeatability studies would clarify robustness; for PET, report human cohort sizes and prespecify comparisons against reference methods before assessing any clinical use.
- **PCR-ALERA (synthesis):** Measure analytical sensitivity, specificity, detection limits, reproducibility, and matrix interference against established PCR readouts before considering deployment beyond proof of concept.

## Takeaway

The strongest experimental result in this batch is D2ML's prospective compound synthesis and assay, but it remains a single-program preprint result. LocoGen and Co$^2$ODE offer useful computational approaches while highlighting the need for wet-lab and intervention-based validation. The imaging, PET, and PCR papers report measurement or method development—not evidence of clinical benefit.

## Method and sources

- **Window:** daily, covering the 2026-11-02 announcement batch only (2026-11-02 through 2026-11-02). Snapshot time: 2026-11-03 01:18:57 UTC. The Tuesday 2026-11-03 batch was not available at snapshot time, so this uses the prior announcement batch.
- **Candidate listings:** checked the latest-date entries in `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph`, then deduplicated by arXiv identifier and verified the selected abstract pages. The configured `cs.BI` listing returned “Invalid archive or category,” so that category could not be checked separately. The arXiv pool is not comprehensive.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`; recent category listings were used to identify the actual announcement batch.
- **Ranking:** This is titled “Notable recent papers” because no checkable citation-velocity or independent-attention signal was established for the batch. The order reflects direct relevance to molecular biology/biomedicine and the type and strength of author-reported evidence; conference/workshop comments are status information, not popularity metrics. Citation totals are not interpreted as gains during this window.
- **Primary sources:** [q-bio recent listings](https://arxiv.org/list/q-bio/recent), [medical physics recent listings](https://arxiv.org/list/physics.med-ph/recent), and the linked arXiv abstract pages. The report covers arXiv only—not bioRxiv, medRxiv, or biomedical research as a whole.
