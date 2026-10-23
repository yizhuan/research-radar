# Notable recent biology and biomedical papers on arXiv — 2026-10-22

## Headline

The latest available announcement batch is 2026-10-22: 5 papers selected from 10 relevant-category submissions in the batch. The dominant pattern is computational molecular design and validation, alongside early-stage imaging and radiopharmaceutical methods. Today's agenda: RNA–protein binder structure design, privacy-preserving single-cell data, DNA supercoiling and condensation, and two translational imaging/radiochemistry studies. arXiv has no official trending chart; this is a relevance-ranked, inferred selection, not a popularity ranking, and arXiv's biomedical coverage is incomplete relative to bioRxiv, medRxiv, and the wider literature.

The current calendar date is 2026-10-23. As of the 2026-10-23 14:29:08 UTC snapshot, no 2026-10-23 announcement batch was available, so this daily report uses the prior 2026-10-22 batch. Window: 2026-10-22 through 2026-10-22 UTC.

## Notable recent papers (ranked by relevance, not measured popularity)

### 1. [RiboBridge: protein-conditioned de novo RNA binder structure design](https://arxiv.org/abs/2610.30668)
- **Abstract:** RiboBridge separates RNA conformation generation from protein–RNA assembly and evaluates predicted complex structures on a temporally split, filtered benchmark of 124 protein–RNA complexes.
- **Authors:** Zhou Zhang, Hanqun Cao, Minghao Sun, Odin Zhang, Yang Zhang, Pheng Ann Heng, Wujun Li, Tianfan Fu
- **arXiv:** `2610.30668v1` (published 2026-10-22 03:32:07 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Strong match to the molecular/RNA focus and cross-listed in computational biology; the authors report a controlled 124-complex benchmark and component ablations. This is relevance evidence, not an attention or citation signal.
- **Claimed contribution:** The authors report improved structural recovery versus compared methods, including best fNAT and DockQ and lowest interface/ligand RMSDs on their benchmark; native information is used only after generation to select among predicted-pocket candidates.
- **Caveat:** This is computational structural prediction, not evidence that designed RNAs bind or function experimentally. The authors identify interface-hypothesis prioritization and sequence realization as unresolved, and call for functional validation.
- **Announcement type:** new submission, 2026-10-22
- **Themes:** Biochemistry & proteins; RNA & transcriptomics; Bioinformatics & sequence analysis

### 2. [Benchmarking Recent Single-Cell Synthetic Data Generation Methods on the OneK1K Dataset](https://arxiv.org/abs/2610.31454)
- **Abstract:** The paper compares scGFT, scLDM, and Cell2Sentence on donor-split OneK1K single-cell RNA-seq data (633,711 training cells from 490 donors; 634,022 test cells from 491 donors) across fidelity, biological preservation, and membership-inference risk.
- **Authors:** Buse Giledereli, Başar Temiz, Amirreza Sattarzadeh Khanehbargh
- **arXiv:** `2610.31454v1` (published 2026-10-22 15:49:27 UTC; categories: `q-bio.GN`)
- **Evidence for ranking:** Direct genomics and single-cell relevance; the authors compare three generators on one named donor-split dataset and evaluate privacy as well as biological utility. The arXiv comment says it was presented at the CAMDA 2026 ELSA Health Privacy Challenge.
- **Claimed contribution:** The authors report that copying non-highly-variable-gene expression can expose donor membership, while Poisson-based reconstruction reduces that risk; scGFT and scLDM preserve more biological structure than an independent Poisson baseline in their tests.
- **Caveat:** Modeling is restricted to highly variable genes with reconstructed background expression; the authors note dataset sparsity, metric sensitivity, and the need to assess both HVG-focused and full-gene behavior. Results on this dataset do not establish privacy for other cohorts or releases.
- **Announcement type:** new submission, 2026-10-22
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Biomedical & translational medicine

### 3. [Supercoiling Drives DNA-Protein Co-Condensation](https://arxiv.org/abs/2610.30588)
- **Abstract:** Coupled DNA-elasticity and protein-concentration modeling suggests that supercoiling can promote DNA–protein co-condensation by coupling protein wetting to DNA twist-to-writhe conversion.
- **Authors:** Sihan Liu, Hongbo Zhao, Andrej Košmrlj
- **arXiv:** `2610.30588v1` (published 2026-10-22 01:42:38 UTC; categories: `physics.bio-ph`, `cond-mat.soft`, `q-bio.BM`)
- **Evidence for ranking:** Cross-listed in biomolecular research and directly addresses genome organization; the paper combines theoretical analysis with simulations and relates modeled energy scales to prior single-molecule measurements.
- **Claimed contribution:** The authors' model predicts that supercoiling can lower a nucleation barrier and enable co-condensation that otherwise remains kinetically trapped, proposing DNA topology as a control parameter.
- **Caveat:** This is a theoretical/computational mechanism, not a new cellular or biochemical demonstration. The authors discuss consistency with prior experiments, but the proposed causal pathway needs targeted experimental testing.
- **Announcement type:** new submission, 2026-10-22
- **Themes:** DNA & genomics; Molecular & cell biology; Biochemistry & proteins

### 4. [AI Enhanced Cerenkov Luminescence Microscopy](https://arxiv.org/abs/2610.31240)
- **Abstract:** A Monte Carlo-guided image-restoration model trained on simulated tumor-spheroid images is evaluated on experimental Cerenkov luminescence microscopy images from 27 U87 spheroids.
- **Authors:** Stefano Pizzardi, Lisa Alborghetti, Caterina Lomazzi, Antonello Enrico Spinelli
- **arXiv:** `2610.31240v1` (published 2026-10-22 13:23:12 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Direct biomedical imaging application with both a stated simulation set (15,360 paired images from 80 simulated spheroid geometries) and experimental-image application (27 spheroids), rather than simulation-only evaluation.
- **Claimed contribution:** The authors report lower reconstruction error for CARE than Noise2Void on synthetic validation data and improved localization, contrast, and signal-to-noise measures when applying CARE to the experimental images.
- **Caveat:** The paired ground truth is simulated; improvement in image metrics on 27 spheroids does not establish diagnostic accuracy, clinical utility, or performance across scanners, tracers, and tumor models.
- **Announcement type:** new submission, 2026-10-22
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 5. [Direct Production of Ultra-High Radioisotopic Pure $^{64}$Cu from Natural Zinc Metal via D-D Fusion Narrowband Fast Neutron Source Irradiation](https://arxiv.org/abs/2610.31340)
- **Abstract:** The authors irradiate natural zinc with a deuterium–deuterium fusion neutron source and use time-resolved gamma spectroscopy to assess the resulting copper radioisotopes.
- **Authors:** Jeremy M. C. Brown, Mantas Grigalavicius, Tibor Gilinger, Adam Kovacs, Parvin Varmazyar, Hsin-Hui Huang, Saulius Juodkazis, Mikas Vengris, Darius Gailevicius, Karoly Osvay
- **arXiv:** `2610.31340v1` (published 2026-10-22 14:24:29 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Biomedical radiopharmaceutical production relevance and a direct irradiation/spectroscopy experiment; the abstract specifies a one-hour irradiation and 72-hour measurement period.
- **Claimed contribution:** The authors report no-carrier-added $^{64}$Cu from natural zinc, with $^{64}$Cu the only copper radioisotope detected in the sample and a threshold-corrected radioisotopic-purity estimate of 99.97%.
- **Caveat:** This is a production-method demonstration, not a radiopharmaceutical efficacy or patient study. Reproducibility, radiochemical labeling, batch yield, and downstream biological performance are not established by the abstract's reported experiment.
- **Announcement type:** new submission, 2026-10-22
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

## Trending Research Themes

- **Structure-first molecular design and its validation boundary:** RiboBridge decomposes protein-conditioned RNA binder structure generation into separate stages. Its benchmarked structural recovery is a computational result; functional binding remains to be tested.
- **Synthetic single-cell data must balance utility with privacy:** The OneK1K study shows that preprocessing choices for non-HVG genes can change membership leakage and that conclusions depend on which fidelity metrics are used.
- **Genome organization through physical mechanisms:** The supercoiling paper models how DNA topology could alter co-condensation barriers. This is a theoretical proposal that complements, but does not replace, experimental evidence.
- **Translational imaging and isotope-production methods:** The Cerenkov paper combines simulated training data with a small experimental spheroid set; the $^{64}$Cu paper measures isotope production. Neither establishes clinical benefit.

## Open Problems and Research Directions

- **From predicted RNA structures to binders (RiboBridge):** The authors explicitly identify interface-hypothesis selection and sequence realization as limitations. A useful next step is blinded biochemical binding assays for generated sequences, with negative controls and structure-prediction confidence stratification, followed by testing whether predicted pose quality tracks measured binding.
- **Privacy beyond a single synthetic-data benchmark (OneK1K):** The authors call for robust, interpretable evaluation across metrics and fuller gene coverage. Follow-up analyses could repeat membership-inference tests across donor-held-out cohorts, report per-donor leakage distributions, and compare HVG-only reconstruction with full-transcriptome synthesis under matched utility constraints.
- **Test the supercoiling mechanism (DNA–protein co-condensation):** The model predicts supercoiling-dependent changes in nucleation and hysteresis. In-vitro experiments that vary supercoiling while holding protein concentration and DNA length fixed could measure condensation thresholds and reversibility; cellular tests would be needed before extending the result to genome organization in vivo.
- **Generalization and reproducibility (Cerenkov microscopy; $^{64}$Cu production):** Evaluate restoration against independent experimental image sets spanning spheroid geometries and acquisition conditions. For isotope production, repeat irradiation across batches and quantify yield and radiochemical as well as radionuclidic quality before drawing conclusions about radiopharmaceutical manufacturing applications.

## Takeaway

The batch's most directly biology-focused work is computational RNA design, synthetic single-cell data, and a physical model of DNA condensation. Two further papers report useful early-stage imaging and radiochemistry results, but remain far from clinical validation. With no defensible attention signal for such a fresh batch, these are notable recent papers rather than measured arXiv trends.

## Method and sources

- **Window:** 2026-10-22 to 2026-10-22 UTC; daily report uses the prior batch dated 2026-10-22 because no 2026-10-23 batch was available at the 2026-10-23 14:29:08 UTC snapshot.
- **Candidate query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date descending. The first 200 results extended back to 2026-10-05 and contained 10 entries dated 2026-10-22 before any 2026-10-21 entry; candidates were checked against their arXiv abstract pages. Five were selected for direct molecular, genomics, or biomedical relevance.
- **Ranking:** Relevance and evidence type only; there is no official arXiv trending chart. Citation totals and citation velocity are not shown because reliable citation evidence was not available for a defensible ranking of this newly announced batch. No download or view statistics are inferred.
- **Coverage:** arXiv is not a comprehensive biomedical index; many clinical and experimental preprints appear on bioRxiv or medRxiv. This report is not a clinical evidence review.
- **Abstract pages:** [RiboBridge](https://arxiv.org/abs/2610.30668), [OneK1K synthetic-data benchmark](https://arxiv.org/abs/2610.31454), [DNA–protein co-condensation](https://arxiv.org/abs/2610.30588), [Cerenkov microscopy](https://arxiv.org/abs/2610.31240), [$^{64}$Cu production](https://arxiv.org/abs/2610.31340).
- **Full text checked for the top three:** [RiboBridge HTML](https://arxiv.org/html/2610.30668v1), [OneK1K HTML](https://arxiv.org/html/2610.31454v1), [DNA–protein co-condensation HTML](https://arxiv.org/html/2610.30588v1).