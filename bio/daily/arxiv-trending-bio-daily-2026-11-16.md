The latest available announcement batch is Monday, 16 November 2026: 11 notable papers (7 new submissions and 4 cross-listings). The strongest concentration is protein-function and molecular-structure evaluation, alongside transcriptomics prediction and biomedical imaging. Spoken agenda: begin with biochemical and structural tests, move through gene-response and molecular-mechanism models, and close with MRI and medical-physics validation. Snapshot: 2026-11-17T01:26:49Z; the 17 November batch was not yet announced, so this uses the prior batch. arXiv has no official trending chart; this is a relevance-ranked inference from incomplete biomedical coverage, not a readership ranking. Attention evidence is sparse, so these are “Notable recent papers,” not measured hottest or most-read papers.

## Top papers (ranked)

Notable recent papers, ranked by biological/biomedical relevance and the strength and type of evidence reported, because popularity signals are too sparse to support a trending ranking.

### 1. [Confident and Wrong: Structure Confidence Is a Poor Selection Filter for Protein Function](https://arxiv.org/abs/2611.17391)
- **Abstract:** The authors compare three lanmodulin design strategies and report that function-guided selection yielded substantially more terbium-binding variants than selection by structural-confidence scores.
- **Authors:** Eric LoPrete, Pavle Jeremić
- **arXiv:** `2611.17391v1` (published 2026-11-12T04:05:20Z; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** New q-bio.BM submission; 297 designs were screened against terbium and dysprosium using biochemical binding assays, the most direct functional experiment in this set.
- **Claimed contribution:** The authors report 83.3% terbium binding in the function-guided panel versus 16.7% in the structure-confidence-selected panel, arguing that measured-function supervision was a better selection signal for this design task (abstract and Results).
- **Caveat:** The comparison is bounded to lanmodulin rare-earth binding; the design panels also differed in generative method, so the result does not establish that structural confidence fails for other proteins or tasks.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [CARVE: A glycan-specific framework for assessing protein-glycan binding-pose quality](https://arxiv.org/abs/2611.18259)
- **Abstract:** CARVE combines glycan-aware geometry and contact measures to classify predicted protein–glycan poses, then benchmarks nine methods on experimentally determined complexes.
- **Authors:** Yifei Xiao, Huifeng Zhao, Silong Zhai, Zichang Jin, Tingjun Hou, Yu Kang
- **arXiv:** `2611.18259v1` (published 2026-11-13T14:55:34Z; categories: `q-bio.BM`)
- **Evidence for ranking:** New q-bio.BM submission; CARVE-Score reproduced quality classes on 25,068 poses (macro-F1 0.892), while CARVE-Bench covers 1,974 complexes and nine prediction methods.
- **Claimed contribution:** The authors report that HADDOCK3 reached the highest Acceptable-level success rate among top-25 predictions per target (47%); no tested method exceeded 20% for high-quality, structurally valid poses (abstract, Results, Conclusion).
- **Caveat:** This is a benchmark of predicted structures against existing complexes, not prospective experimental validation of new binding. The authors’ temporal split reduces possible training overlap but does not establish that every benchmark structure was unseen by every prediction method.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [Scan-specific k-space interpolation using deep Koopman autoencoders](https://arxiv.org/abs/2611.18301)
- **Abstract:** A scan-specific deep Koopman autoencoder reconstructs retrospectively undersampled brain MRI k-space data and is compared with GRAPPA and RAKI.
- **Authors:** Wassim Ben Salah, Jon Cleary, Sarah McElroy, Raphael Tomi-Tricot, Antoine Naegel, Sebastien Ourselin, Jonathan Shapey, Christos Bergeles, Radhouene Neji
- **arXiv:** `2611.18301v1` (published 2026-11-13T15:25:37Z; categories: `physics.med-ph`)
- **Evidence for ranking:** New primary submission in medical physics; tested on 281 retrospectively undersampled brain datasets and a 52-image reader-study subset, giving it the clearest image-quality evaluation in this batch.
- **Claimed contribution:** The authors report better reconstruction metrics than GRAPPA and RAKI and reader preference over RAKI, with improved ratings for sharpness, aliasing, and overall image quality (abstract and Results).
- **Caveat:** Evaluation used retrospective brain scans from one dataset; the authors call for tests on other anatomies, scanners, and coils. Reader preference is not evidence of improved clinical outcomes.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** Medical physics & imaging; Quantitative methods

### 4. [S1Pert: Scalable Target-Specific Gene Response Prediction with System-One Intelligence](https://arxiv.org/abs/2611.17705)
- **Abstract:** S1Pert combines uncertainty-aware response labels, reusable target and gene representations, and a hierarchical decoder to predict transcriptional responses to unseen genetic perturbations.
- **Authors:** Xiaoqi Sheng, Hou wang, Yan Liang, Yutong Li, Wenhao Du, Tinghe Zhang, Jiawen Liu, Hongmin Cai
- **arXiv:** `2611.17705v1` (published 2026-11-13T03:35:01Z; categories: `q-bio.GN`)
- **Evidence for ranking:** New genomics submission; the authors evaluate target-specific response discrimination across multiple cellular contexts and report improved performance over baselines.
- **Claimed contribution:** The authors present an inference-efficient framework intended to distinguish perturbation-specific responses rather than relying on historical gene-level response frequencies (abstract).
- **Caveat:** This is computational evaluation on existing perturbation data, not prospective CRISPR validation; response labels and performance remain dependent on the benchmark and cell context.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Bioinformatics & sequence analysis

### 5. [More Genes, Faster Inference: Efficient Large-Panel Spatial Transcriptomics Prediction from Histology](https://arxiv.org/abs/2611.17899)
- **Abstract:** GeneFlow combines tissue-image morphology and spatial gene interactions to predict large-panel spatial expression directly from histology.
- **Authors:** Songming Zhang, Yuxiao Luo, Shifu Luo, Siran Chen, Shuquan Su, Jinyan Li
- **arXiv:** `2611.17899v1` (published 2026-11-13T08:35:27Z; categories: `cs.CV`, `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Cross-listed into q-bio.QM; the authors report benchmark comparisons across multiple spatial-transcriptomics datasets, including up to 56.8% gains for 1,000-gene prediction.
- **Claimed contribution:** The authors describe a flow-matching model that predicts spatial gene-expression profiles from histology while reducing computational cost (abstract).
- **Caveat:** Expression is computationally inferred from images; benchmark performance does not establish that predicted profiles substitute for measured spatial transcriptomics or transfer to new tissue types and sites.
- **Announcement type:** cross-listing into q-bio.QM (original submission 2026-11-13), 2026-11-16 announcement batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Bioinformatics & sequence analysis

### 6. [Deciphering multiple binding modes in large protein complexes via Enhanced Sampling and beta-VAE: the CYFIP1-eIF4E case](https://arxiv.org/abs/2611.18236)
- **Abstract:** Enhanced molecular sampling and latent-space clustering are used to propose three binding modes for the flexible CYFIP1–eIF4E protein complex.
- **Authors:** Francesco Pignotti, Emanuele Telari, Edoardo Milanetti, Anna La Teana, Jesmina Rexha, Alice Romagnoli, Luca Maragliano, Giovanni Di Muccio
- **arXiv:** `2611.18236v1` (published 2026-11-13T14:31:47Z; categories: `q-bio.BM`, `q-bio.QM`)
- **Evidence for ranking:** New q-bio.BM submission, cross-listed in quantitative methods; the analysis uses ten enhanced-sampling replicas totaling 100 μs to identify recurring interface modes.
- **Claimed contribution:** The authors’ simulations suggest CYFIP1 samples the canonical dorsal site, a non-canonical lateral site, and a combined mode on eIF4E, including contacts outside the previously emphasized interface (abstract and Results).
- **Caveat:** The proposed interface modes are computational. The authors note that coarse-graining and elastic-network restraints limit side-chain detail and large-scale motion; experimental binding or mutagenesis tests remain necessary.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 7. [Exact stochastic theory of post-transcriptional gene autoregulation mediated by RNA-binding proteins](https://arxiv.org/abs/2611.18062)
- **Abstract:** An analytical stochastic model derives protein-number and burst-size distributions for RNA-binding-protein-mediated feedback and compares predicted noise and rhythm transmission with transcriptional feedback.
- **Authors:** Chen Jia
- **arXiv:** `2611.18062v1` (published 2026-11-13T11:45:58Z; categories: `q-bio.MN`, `cond-mat.stat-mech`, `physics.bio-ph`)
- **Evidence for ranking:** New q-bio.MN submission, cross-listed in biological physics and statistical mechanics; it gives an exact mathematical treatment of a molecular feedback mechanism.
- **Claimed contribution:** The author derives a steady-state distribution and a criterion for sub-Poissonian fluctuations, and predicts different noise-suppression advantages for positive versus negative feedback (abstract).
- **Caveat:** These are theoretical results from a reaction model, not newly measured molecular or cellular effects; the predicted regime differences need experimental testing.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Quantitative methods

### 8. [Certificate-Based Verification of Pulsed Field Ablation Models](https://arxiv.org/abs/2611.18148)
- **Abstract:** The paper proposes independent mathematical certificates that bound numerical error in pulsed-field-ablation simulations of electric fields and lesion maps.
- **Authors:** Konstantinos Dovelos
- **arXiv:** `2611.18148v1` (published 2026-11-13T13:22:35Z; categories: `cs.CE`, `math.NA`, `physics.med-ph`)
- **Evidence for ranking:** Cross-listed into medical physics; the authors compare certificate-based bounds with grid-convergence studies and report a checker running at roughly one-tenth of solve time.
- **Claimed contribution:** For a modeled focal electrode, the authors certify lesion-depth bounds of 3.50–3.75 mm at specified voltage and field thresholds across a stated conductivity-ratio range (abstract).
- **Caveat:** The certificates assess whether a specified mathematical model was solved within bounds; they do not validate the model’s tissue assumptions, lethal-field threshold, or predicted lesion against biological measurements.
- **Announcement type:** cross-listing into physics.med-ph (original submission 2026-11-13), 2026-11-16 announcement batch
- **Themes:** Medical physics & imaging; Quantitative methods

### 9. [A thorough review on Deep Learning approaches to 2D-to-3D Registration in Medical Imaging](https://arxiv.org/abs/2611.17468)
- **Abstract:** This review compares deep-learning approaches to 2D-to-3D registration across 41 studies, emphasizing pipeline design, metrics, and domain adaptation.
- **Authors:** Andrea Borghesi, Julia van Beurden, Maarten van Alphen, Michiel van den Brekel, Luc Karssemakers, Jan-Jakob Sonke, Baris Karakullukcu, Jonas Teuwen, George Yiasemis
- **arXiv:** `2611.17468v1` (published 2026-11-12T19:52:39Z; categories: `eess.IV`, `cs.CV`, `cs.LG`, `physics.med-ph`)
- **Evidence for ranking:** Cross-listed into medical physics; it synthesizes 41 studies and reports that 23 use direct regression and 18 iterative pipelines, with X-ray-to-CT work dominating the reviewed literature.
- **Claimed contribution:** The authors identify per-case uncertainty estimation and temporal/sequential modeling as under-addressed issues for clinical readiness (abstract).
- **Caveat:** This is a review of published methods, not a new comparative clinical study; conclusions depend on the coverage and evaluation choices of the included papers.
- **Announcement type:** cross-listing into physics.med-ph (original submission 2026-11-12), 2026-11-16 announcement batch
- **Themes:** Medical physics & imaging; Quantitative methods

### 10. [Domain-repetition patterns in protein domain trigrams are uniform across chromosomes and conserved among multicellular eukaryotes](https://arxiv.org/abs/2611.17580)
- **Abstract:** A reproducible analysis of Pfam domain triplets across 16 organisms reports broadly similar repetition-pattern proportions across chromosomes and multicellular eukaryotes.
- **Authors:** Yanying Wu
- **arXiv:** `2611.17580v1` (published 2026-11-12T23:02:11Z; categories: `q-bio.OT`)
- **Evidence for ranking:** New submission in quantitative biology; the analysis covers 199 chromosomes or other proteome components across 14 organisms and compares distinct domain triplets using gene-level permutations.
- **Claimed contribution:** The author reports conserved proportions of distinct three-domain patterns among multicellular eukaryotes, with chromosome-level exceptions including KRAB zinc-finger-rich regions (abstract).
- **Caveat:** This is a computational proteome-pattern analysis; the reported distributions do not establish functional consequences or causal evolutionary mechanisms.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 11. [Emergent intercellular contact-force networks shaped by deformability](https://arxiv.org/abs/2611.18414)
- **Abstract:** Cell-based simulations report that deformability and local geometry organize force networks in dense assemblies of active cells.
- **Authors:** Koshi Yoshida, Nen Saito, Shuji Ishihara, Kaoru Sugimura
- **arXiv:** `2611.18414v1` (published 2026-11-13T16:56:50Z; categories: `cond-mat.soft`, `q-bio.CB`)
- **Evidence for ranking:** Cross-listed in cell behavior; the authors compare deformable and non-deformable simulations and use persistent-homology analysis to characterize force-network structure.
- **Claimed contribution:** The authors report a bimodal contact-force distribution and a characteristic weak-tip/strong-side network motif in a modeled soft-liquid regime, dependent on cell deformability (abstract).
- **Caveat:** The findings are simulation-based and depend on the Fourier Contour Cell model and its assumptions about deformability and active motility; they are not direct observations of tissue forces.
- **Announcement type:** cross-listing into q-bio.CB (original submission 2026-11-13), 2026-11-16 announcement batch
- **Themes:** Molecular & cell biology; Quantitative methods

## Trending Research Themes

- **Protein function and molecular-structure evaluation:** “Confident and Wrong,” CARVE, and the CYFIP1–eIF4E study address different limits of computational structure-based reasoning. The evidence ranges from biochemical binding assays to retrospective structural benchmarks and molecular simulation; these are complementary but not equivalent validation.
- **Prediction of gene-expression outputs:** S1Pert predicts target-specific perturbation responses, while GeneFlow predicts spatial expression from histology. Both are computational approaches, but they address different inputs and targets and do not establish a field-wide shift.
- **Mechanistic models at different scales:** the RNA-binding-protein feedback theory and the intercellular force-network simulations study gene regulation and cell mechanics, respectively. Neither report supplies experimental validation in this announcement batch.
- **Biomedical imaging and model verification:** the MRI reconstruction study, the 2D-to-3D registration review, and the pulsed-field-ablation verification paper focus on image quality or numerical reliability. Their methods address distinct problems; none alone demonstrates improved patient outcomes.

## Open Problems and Research Directions

- **Test protein-design generalization:** “Confident and Wrong” is limited to lanmodulin and rare-earth binding, and design strategies differ beyond selection criteria. A blinded follow-up could compare function-trained, structure-confidence, and random selection across additional folds and ligands with matched budgets and prespecified assays.
- **Strengthen glycan-pose benchmarks:** CARVE-Bench’s temporal split reduces likely overlap but cannot prove every structure was unseen by each evaluated model. Future work could audit model training cutoffs and add prospective pose predictions followed by orthogonal structural or binding assays.
- **Validate transcriptomic predictions externally:** test S1Pert’s preregistered unseen-target predictions in replicated CRISPR screens across additional cell types; compare GeneFlow predictions with matched measured spatial-transcriptomics panels from independent tissues and sites.
- **Bridge molecular models to experiments:** evaluate the CYFIP1–eIF4E binding modes with targeted mutagenesis and binding measurements, and test the RNA-feedback model’s predicted protein-number distributions under controlled positive and negative feedback perturbations.
- **Separate numerical certainty from biological validity:** extend the MRI study to prospective, multi-site scans and additional anatomies; for ablation modeling, compare certified simulations with phantom or ex-vivo measurements while varying tissue properties and lesion-threshold assumptions.

## Takeaway

The clearest direct biological experiment is a lanmodulin design comparison in which measured-function guidance outperformed structural-confidence selection in that specific assay. CARVE offers a broad glycan-structure benchmark, while other papers contribute transcriptomic prediction, molecular simulation, RNA theory, and imaging or model-verification methods. This is a relevance-ranked snapshot of one arXiv batch, not a popularity chart, systematic review, or clinical evidence assessment.

## Method and sources

- **Window:** daily batch dated 2026-11-16; start and end date are both 2026-11-16. **UTC snapshot:** 2026-11-17T01:26:49Z. The 17 November announcement had not yet occurred; arXiv’s schedule indicated the next announcement as early as 2026-11-18T01:00Z, so the prior batch was used.
- **Scope categories:** `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`; `q-bio.OT` was additionally considered for the clearly protein-domain study. The configured `cs.BI` browse page was unavailable at snapshot, so primary-category-only `cs.BI` papers may be missing.
- **Candidate pool:** traversed the full [Quantitative Biology announcement page](https://arxiv.org/list/q-bio/new) (13 new submissions, 7 cross-listings, 22 replacements) and [Medical Physics announcement page](https://arxiv.org/list/physics.med-ph/new) (1 new submission, 4 cross-listings, 1 replacement) for the 16 November batch. Each retained paper’s individual arXiv abstract page was checked. The 11 selected entries comprise 7 new submissions and 4 cross-listings; no revision was selected.
- **Ranking:** arXiv has no official trend or readership ranking. Attention evidence and citation momentum were too sparse for a popularity ranking, so entries are ordered by relevance to biology/biomedicine and the specificity of reported assay, benchmark, or evaluation evidence. No downloads, views, or citation gains were inferred. The top three papers were read beyond their abstracts using available HTML/PDF full text; additional selected papers were checked against their abstracts.
- **Coverage caveat:** arXiv is not a representative biomedical index. Much experimental biology and clinical preprint research appears on bioRxiv or medRxiv. This report is not a systematic literature review, clinical guideline, or practice-changing evidence assessment.
