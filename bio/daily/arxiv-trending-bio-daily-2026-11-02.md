# arXiv Trending Biology and Biomedicine — Daily — 2026-11-02

## Headline

Daily biology and biomedicine batch announced Monday, 2 November 2026; 10 papers highlighted. The strongest pattern is computational biology for regulatory-sequence design, model interpretation, and biochemical dynamics, alongside experimentally grounded small-molecule design and biomedical imaging. Agenda: start with sequence and molecule design, move through gene-network methods, then clinical imaging and prediction. arXiv has no official trending chart; this is an inferred relevance ranking from an incomplete biomedical corpus, not a measure of readership or research validity.

## Notable recent papers

### 1. [D2ML: Models for Direct-to-Biology Small Molecule Screening](https://arxiv.org/abs/2610.41070)
- **Abstract:** Assay-aware machine-learning models combine crude and purified direct-to-biology screening data and are used to select compounds for synthesis and testing.
- **Authors:** AkshatKumar Nigam, Neri Amara, Hillary Dequina, Dyana Kenanova, Seth Malmersjo, Fiorella Ruggiu, Raymond V. Fucini, Jack Sadowsky, Stig K. Hansen, Imran S. Haque
- **arXiv:** `2610.41070v1` (published 2026-10-29 23:33:05 UTC; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** The paper reports a prospective test of 84 newly selected compounds, with synthesis and assay results; the most selective reported compound had a ROS1 IC50 of 14.7 nM and 233-fold selectivity over TRKB. The arXiv comment identifies a NeurIPS 2026 AI for Drug Discovery workshop.
- **Claimed contribution:** The authors say joint modelling of multiple direct-to-biology assay stages improves predictions and can guide a potency–selectivity trade-off in their ROS1/TRKB program.
- **Caveat:** The study is limited to one 2,4-disubstituted pyrimidine core and a kinase program; the authors note small purified evaluation sets and call for testing broader chemistries and targets.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine

### 2. [Locality-Controlled Out-of-Distribution Guidance for Robust Regulatory DNA Sequence Design](https://arxiv.org/abs/2610.41736)
- **Abstract:** LOCOGEN uses a learned motif mask to apply diffusion-model guidance to background positions while protecting regulatory DNA motifs, balancing predicted activity, novelty, and sequence plausibility.
- **Authors:** Dabin Jeong, Marwane Bourdim, Mo Lotfollahi
- **arXiv:** `2610.41736v1` (published 2026-10-30 13:44:07 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** The authors evaluate the design against property, novelty, and plausibility measures across HepG2, K562, and SK-N-SH cell-line datasets; the arXiv comment says accepted to NeurIPS 2026.
- **Claimed contribution:** The authors report that localizing out-of-distribution damping reaches a balance of the three computational objectives that their tested baselines did not achieve.
- **Caveat:** The paper tests one masked diffusion backbone and relies on computational oracles; the authors state that generated sequences still need experimental validation.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Bioinformatics & sequence analysis

### 3. [Co$^2$ODE: Conditionally Coarse-Grained Model Discovery for Rewiring in Biochemical Networks](https://arxiv.org/abs/2610.41634)
- **Abstract:** Co$^2$ODE combines context-specific selection of measured markers with a latent closure model to predict biochemical-network dynamics from single-cell phosphoproteomic data.
- **Authors:** Theodore de Pomereu, Fabian Fröhlich
- **arXiv:** `2610.41634v1` (published 2026-10-30 12:10:55 UTC; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** The reported evaluation spans 30 cancer-relevant overexpression conditions and compresses a 30-marker panel to a 10-dimensional state while matching a full-panel neural ODE's predictive accuracy.
- **Claimed contribution:** The authors propose conditional coarse-graining as a way to expose context-dependent marker selection while retaining predictive performance.
- **Caveat:** The authors' own analysis finds that the data do not identify the underlying network structure: alternative marker selections and prior scores can fit equally well, and interventions are needed to distinguish them.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Molecular & cell biology; Quantitative methods; Omics & single-cell methods

### 4. [Localizing predictive concepts encoded in neural representations via hierarchical testing](https://arxiv.org/abs/2610.41046)
- **Abstract:** CUTTIE hierarchically tests clusters of neural-network units to identify information-bearing groups and associate their representations with regulatory DNA motifs while controlling family-wise error.
- **Authors:** Viktoriia Huryn, Marco Simnacher, Jim Berend, Wojciech Samek, Christoph Lippert, Sonja Greven, Uwe Ohler
- **arXiv:** `2610.41046v1` (published 2026-10-29 22:34:52 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** The paper reports a controlled simulation and an application to a DNA-sequence model predicting cell-type-specific chromatin accessibility, where identified concepts map to known regulatory motifs.
- **Claimed contribution:** The authors present a top-down conditional-independence testing method intended to localize model concepts with population-level error control.
- **Caveat:** This is a model-interpretation method evaluated computationally; motif correspondence does not establish that the model's features are causal regulators.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Bioinformatics & sequence analysis

### 5. [Transmission and filtering of stochastic rhythms in bursty gene expression](https://arxiv.org/abs/2610.41109)
- **Abstract:** An analytical framework derives how degradation, transcriptional bursting, and variable upstream cycle timing shape the transmission of stochastic rhythms to gene expression.
- **Authors:** Chen Jia
- **arXiv:** `2610.41109v1` (published 2026-10-30 00:57:42 UTC; categories: `q-bio.MN`, `physics.bio-ph`)
- **Evidence for ranking:** The paper derives autocorrelation and power-spectrum relations and reports that its degradation threshold separates all 10 pulsing from non-pulsing p53 target proteins in previously published experiments.
- **Claimed contribution:** The author presents a quantitative theory for when upstream stochastic rhythms are retained or filtered by downstream gene-expression dynamics.
- **Caveat:** This is primarily theoretical work; the 10-protein comparison reuses prior experimental classifications rather than providing new experimental validation.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Molecular & cell biology; Quantitative methods; Gene regulation & epigenetics

### 6. [GraphTFactor: A graph-based approach for proteins transcription factor prediction](https://arxiv.org/abs/2610.40867)
- **Abstract:** GraphTFactor encodes protein sequences as graphs and classifies transcription factors, with the authors reporting benchmark performance and interpretable sequence-region signals.
- **Authors:** Domenico Amato, Salvatore Calderaro, Giosuè Lo Bosco, Riccardo Rizzo, Filippo Vella
- **arXiv:** `2610.40867v1` (published 2026-10-29 18:45:22 UTC; categories: `q-bio.QM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The paper reports benchmark comparisons and provides an open-source package and interactive prediction application.
- **Claimed contribution:** The authors say graph representations handle variable-length protein sequences without imposing a fixed sequence length and can support transcription-factor prediction.
- **Caveat:** The abstract does not give dataset sizes or independent experimental validation; benchmark gains do not establish that predicted proteins function as transcription factors in cells.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 7. [Quantitative Ultrasound Characterizes Perfusion Trajectories in Healthy and Inflamed Gingival Wound Healing](https://arxiv.org/abs/2610.41897)
- **Abstract:** A longitudinal ultrasound analysis estimates gingival perfusion after extraction and compares healing trajectories between visits classified as healthy or inflamed.
- **Authors:** Haowei Tai, Oscar Duran-Garnica, Karen Villarreal, Hsun-Liang Chan, Oliver D. Kripfgans
- **arXiv:** `2610.41897v1` (published 2026-10-30 15:35:27 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** The cohort included 51 patients imaged from two weeks to three months after extraction; automated segmentation had a reported mean Dice score of 0.98, and ultrasound perfusion estimates were compared with laser-speckle measurements.
- **Claimed contribution:** The authors report that velocity-weighted colour-pixel density tracked longitudinal perfusion changes and differed between healthy and inflamed recovery visits.
- **Caveat:** This is a small observational imaging cohort, not evidence that the measure improves treatment decisions or patient outcomes; the reported correlation with laser-speckle imaging was not statistically clear in inflamed visits.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 8. [A General-Purpose Adaptable Foundation Model for Total-Body PET Kinetic Modelling](https://arxiv.org/abs/2610.41093)
- **Abstract:** LoRACM adapts a pretrained consistency model with low-rank updates to infer posterior distributions for total-body PET kinetic models across tracer, protocol, and modelling settings.
- **Authors:** Yun Zhao, Qinlin Gu, Andrew J. Reader, Yanan Fan, Georgios I. Angelis, Katya Amadita, Kevin J. Chung, Xiaoyu Duan, Benjamin A. Spencer, Guobao Wang, Steven R. Meikle
- **arXiv:** `2610.41093v1` (published 2026-10-30 00:24:58 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** The authors test three adaptation scenarios using simulated and human data; each adaptation uses 50,000 simulated pairs, and human estimates are compared with non-negative least-squares fitting.
- **Claimed contribution:** The authors report that LoRA adaptation can transfer a pretrained model to new PET kinetic settings with less than three hours of training on one A100 GPU.
- **Caveat:** The abstract does not specify human cohort sizes; agreement with fitting baselines is not clinical validation or proof of improved patient care.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Medical physics & imaging; Quantitative methods; Biomedical & translational medicine

### 9. [Comparison of melanin subtypes using pump-probe microscopy](https://arxiv.org/abs/2610.40969)
- **Abstract:** Pump-probe microscopy and computational analyses characterize melanin photophysics across six lesion categories and test whether measured heterogeneity distinguishes tissue groups.
- **Authors:** Emma Bao, David Grass, Martin C. Fischer, Warren S. Warren
- **arXiv:** `2610.40969v1` (published 2026-10-29 20:57:44 UTC; categories: `physics.optics`, `physics.med-ph`)
- **Evidence for ranking:** The authors report measurements from 21 biological samples and 109 regions of interest, spanning cutaneous and non-cutaneous lesions plus a murine melanoma model.
- **Claimed contribution:** The paper reports that melanin heterogeneity differentiates cutaneous from non-cutaneous lesions in this dataset and that full transient-absorption curves classify most sampled subtypes above chance.
- **Caveat:** Heterogeneity was not correlated with malignancy in this dataset; this is an optical-characterization study, not a validated diagnostic test.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Medical physics & imaging; Molecular & cell biology; Biomedical & translational medicine

### 10. [Physiological Trajectories and Observation Patterns in ICU Mortality Prediction: Transportability Under Changing Measurement Conditions](https://arxiv.org/abs/2610.42126)
- **Abstract:** An ICU mortality-prediction study compares physiological trajectories with observation-frequency and timing features and tests performance under dataset transfer and changing measurement availability.
- **Authors:** Benjamin T. Pike
- **arXiv:** `2610.42126v1` (published 2026-10-30 17:56:10 UTC; categories: `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** The study trains on 7,762 MetaVision patients and evaluates on 21,682 MIMIC-IV and 43,878 eICU patients across 204 hospitals, with additional matched-observation sensitivity analyses.
- **Claimed contribution:** The author reports that physiological summaries transfer more consistently than observation-pattern features, whose benefit changes with measurement timing and availability.
- **Caveat:** These are retrospective dataset results for prediction, not prospective clinical-utility evidence; the observation-pattern increment did not clearly transfer from the source system.
- **Announcement type:** new submission, 2026-11-02 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

## Trending Research Themes

- **Sequence design and model interpretation:** LOCOGEN and CUTTIE both try to make genomic models more biologically legible: the former localizes sequence-generation pressure, while the latter tests which learned unit clusters carry motif-related information. Both remain computational studies; neither demonstrates that a designed or highlighted sequence changes biology in a new wet-lab experiment.
- **Learning biochemical and gene-expression dynamics:** Co$^2$ODE and the stochastic-rhythm paper formalize context-dependent signalling and noise transmission. Co$^2$ODE's authors emphasize that predictive fit alone does not identify the true network, while the rhythm paper checks its theoretical threshold against prior p53 classifications.
- **Assay- and imaging-aware biomedical modelling:** D2ML uses assay-stage structure to guide measured compound synthesis, whereas the ultrasound, PET, melanin, and ICU papers analyze human or tissue data through different imaging or prediction pipelines. Their evidence ranges from prospective compound assays to retrospective cohorts and computational comparisons; these are not equivalent validation types.

## Open Problems and Research Directions

- **LOCOGEN (author-stated):** test alternative diffusion backbones and perform wet-lab validation. A useful follow-up would synthesize generated sequences and measure expression in matched MPRA assays across the represented cell lines, while keeping the evaluation oracle independent of guidance.
- **Co$^2$ODE (author-stated):** the current measurements do not identify the rewired network. Targeted perturbations that break correlated marker relationships, followed by held-out prediction and independent pathway assays, could test whether the selected state markers are mechanistically informative.
- **D2ML (author-stated):** expand prospective evaluation beyond one chemical core and kinase program, with larger purified-compound sets across targets. This would show whether assay-aware transfer generalizes beyond the reported ROS1/TRKB setting.
- **Medical imaging studies (synthesis):** multi-site repeatability and independent cohorts would help establish how stable the ultrasound and melanin measurements are across scanners, operators, and patient populations. For PET, the roadmap paper identifies noisy simulation expectations, gradient/adjoint computation, and simulation-budget allocation as open algorithmic challenges.

## Takeaway

Today's clearest experimental signal is D2ML's model-guided synthesis and testing of new compounds. The sequence-design and network papers offer promising computational methods, but their biological interpretation still depends on stronger intervention or wet-lab tests. The biomedical imaging and ICU results are promising measurements or retrospective analyses, not practice-changing evidence.

## Method and sources

- **Window:** daily; latest arXiv announcement batch dated 2026-11-02. Date range: 2026-11-02 through 2026-11-02 (announcement-date window). Snapshot: 2026-11-02 17:13:25 UTC. The report uses today's batch, not a prior batch.
- **Candidate listings:** traversed the latest date heading on `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph`; `cs.BI` returned no current listing/API entries. There were 23 distinct identifiers across the available latest-date headings. Ten papers were selected for clear molecular, genomic, biochemical, or biomedical relevance; ecology-oriented and general-method entries were not used to pad the list. Selected abstract pages and metadata were checked individually.
- **Category query:** [arXiv API query](https://export.arxiv.org/api/query?search_query=cat%3Aq-bio.BM%20OR%20cat%3Aq-bio.GN%20OR%20cat%3Aq-bio.MN%20OR%20cat%3Aq-bio.SC%20OR%20cat%3Aq-bio.CB%20OR%20cat%3Aq-bio.TO%20OR%20cat%3Aq-bio.QM%20OR%20cat%3Acs.BI%20OR%20cat%3Aphysics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200), with category listings used to identify the actual announcement-date batch. The corpus is arXiv only; it is not a representative index of biomedical preprints, and does not cover bioRxiv, medRxiv, or the broader medical literature.
- **Ranking:** No citation-velocity or independent-attention signal was established for this just-announced batch. The list is therefore titled “Notable recent papers” and ordered by direct relevance plus checkable evidence reported in each paper, with recency only a tie-breaker. Conference/workshop comments are reported as status, not popularity. No downloads or readership claims are made.
- **Primary sources:** [q-bio recent listings](https://arxiv.org/list/q-bio/recent), [medical physics recent listings](https://arxiv.org/list/physics.med-ph/recent), and each linked arXiv abstract page above.
