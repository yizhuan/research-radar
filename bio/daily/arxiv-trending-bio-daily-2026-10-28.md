# arXiv Biology and Biomedicine — Daily — 28 October 2026 batch

## Headline

Thirteen notable biology and biomedical papers from arXiv’s latest available announcement batch, Wednesday 28 October 2026. The strongest shared pattern is computational methods paired with explicit benchmarks: molecular-complex modeling, RNA simulation resources, synthetic genomes, transcriptomics, and medical-imaging/decision support. The agenda is to compare what these methods actually tested and where their evidence stops. This is a relevance-ranked selection, not a measured popularity chart: arXiv has no official trending ranking, and its biomedical preprint coverage is incomplete, particularly for experimental and clinical work.

## Notable recent papers (ranked by relevance)

### 1. [A unified coarse-grained neural network potential for the dynamics of biomolecular complexes](https://arxiv.org/abs/2610.37606)
- **Abstract:** AMARO v2.0 uses a heavy-atom coarse-grained neural potential to model protein, drug-like molecule, and complex dynamics with solvent treated implicitly.
- **Authors:** Antonio Mirarchi, Stephen E. Farr, Adrià Peréz, Gianni De Fabritiis
- **arXiv:** `2610.37606v1` (published 2026-10-27 17:37:10 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** A recent independent arXiv News explainer discussed the paper; the authors report tests across 262 complexes and 11 targets, plus targeted binding simulations. Ranking is relevance-based, not readership-based.
- **Claimed contribution:** The authors report a shared heavy-atom representation for proteins and drug-like molecules, with 3.3-fold more trajectories reaching the trypsin–benzamidine crystal pose than all-atom mechanics at a matched estimated GPU-time budget. The Results and Conclusion support this method claim; it is computational validation, not experimental confirmation of binding behavior.
- **Caveat:** Binding free-energy estimates were more favorable than experimental references; the authors also report quaternary reorientation in one HIF2A complex and pose/site-specificity failures in SHP2 and CDK8. Evidence is simulation-based.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [Accurate structural modelling of protein-glycan recognition with GlycoWeave](https://arxiv.org/abs/2610.37410)
- **Abstract:** GlycoWeave is a glycan-specific diffusion framework that samples protein–glycan structures while enforcing chemical constraints and combining atom- and monosaccharide-level representations.
- **Authors:** Huifeng Zhao, Jintu Zhang, Yifei Xiao, Youqiao Qian, Silong Zhai, Zichang Jin, Li Wang, Yuchao Wang, Hang Dong, Yifan Zhao, Zhenxing Wu, Hongyan Du, Yuansheng Huang, Bowei Zhao, Xiaorui Wang, Shukai Gu, Jike Wang, Zhongjun Li, Zhongtang Li, Tingjun Hou, Yu Kang
- **arXiv:** `2610.37410v1` (published 2026-10-27 15:27:09 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** The authors report a 698-complex benchmark and comparison with AlphaFold 3; the subject is directly in biomolecular modeling. Benchmark size is evidence of evaluation scope, not popularity.
- **Claimed contribution:** The abstract reports a 71.9% Top-25 high-quality success rate versus 19.2% for AlphaFold 3, with 0.34 seconds per sampled pose, and says the method preserves glycan structural validity and linkage-specific preferences. These are benchmark/modeling results, not wet-lab validation.
- **Caveat:** Results depend on benchmark construction and scoring; the abstract does not establish prospective performance on newly solved complexes or experimental binding outcomes. The arXiv HTML conversion was unavailable, so this summary is bounded to the verified abstract.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 3. [mdRNAcat: A Molecular Dynamics RNA Catalog of REST2 Conformational Ensembles](https://arxiv.org/abs/2610.35204)
- **Abstract:** mdRNAcat is a curated dataset of all-atom replica-exchange simulations for 48 diverse RNA systems, with coordinates, forces, structural annotations, and exchange metadata.
- **Authors:** Anton E. Dorn, Emile de Bruyn, Fabrice von der Lehr, Philipp Knechtges, Stefan Kesselheim, Alexander Schug
- **arXiv:** `2610.35204v2` (published 2026-10-26 10:56:24 UTC; revised 2026-10-27 10:19:38 UTC; categories: `q-bio.BM`, `cs.LG`, `physics.bio-ph`)
- **Evidence for ranking:** Substantive v2 replacement in the batch; cross-listed in biomolecules, machine learning, and biological physics. The authors cover 48 systems, 32 REST2 states per system, and 200–300 ns production per state.
- **Claimed contribution:** The paper presents a standardized HDF5 resource with atomic coordinates and forces at reference and replica-exchange states for training and evaluating data-driven RNA models.
- **Caveat:** These are simulated ensembles, not experimentally observed native ensembles; elevated-temperature states require careful interpretation. The dataset is large (about 699 GB per the paper’s listing), which may constrain reuse.
- **Announcement type:** revision, 2026-10-28 batch
- **Themes:** RNA & transcriptomics; Biochemistry & proteins; Quantitative methods

### 4. [HELICS: Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching](https://arxiv.org/abs/2610.36361)
- **Abstract:** HELICS learns to generate conditional genome-wide common-variant genotype data from unphased biobank data using compressed chromosome representations and latent flow matching.
- **Authors:** Ahmad Abdel-Azim, Xihong Lin
- **arXiv:** `2610.36361v1` (published 2026-10-26 22:25:36 UTC; categories: `q-bio.GN`, `cs.LG`)
- **Evidence for ranking:** Cross-listed in genomics and machine learning; the arXiv listing notes NeurIPS 2026. Authors report training on more than 417,000 UK Biobank genomes and external fidelity evaluation.
- **Claimed contribution:** Authors report high allele-frequency agreement in external evaluation (R² = 0.992), improved preservation of SNP correlations versus tested simulators, and conditional generation based on ancestry and genetic-liability summaries. This is synthetic-data modeling, not disease-risk prediction in patients.
- **Caveat:** The data focus on common variants and UK Biobank training; synthetic fidelity does not itself establish privacy protection, portability across populations, or clinical utility. The perturbation analysis is not causal evidence about disease.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 5. [Structure, Not Sequence: Tracking and Validating Folding Mechanisms in ESMFold's Trunk with Sparse Autoencoders](https://arxiv.org/abs/2610.36226)
- **Abstract:** Sparse autoencoders and attribution are used to interpret how ESMFold’s internal representations contribute to protein-structure prediction.
- **Authors:** Bohan Liu, Xiaohan Fan, Wenqian Ye, Aidong Zhang
- **arXiv:** `2610.36226v1` (published 2026-10-26 20:04:57 UTC; categories: `q-bio.QM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Three-category cross-listing and a direct protein-folding interpretation question; the authors trace learned features across model blocks to model outputs and compare interpretations with known biochemistry.
- **Claimed contribution:** The abstract reports that single representations carry inherited sequence semantics while pair representations compute pairwise geometry; concept activations also forecast the model’s own fold quality.
- **Caveat:** These are interpretations of a model’s internal computation, not experimental evidence of biological mechanisms. The quality prediction is about the model’s own output and should not be mistaken for independent structural validation.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 6. [pyTransRate: 1 reference-free quality assessment of de novo transcriptome assemblies with current aligners and quantifiers](https://arxiv.org/abs/2610.37031)
- **Abstract:** pyTransRate reimplements reference-free transcriptome-assembly quality scoring in Python using current alignment and quantification tools.
- **Authors:** Matthew MacManes
- **arXiv:** `2610.37031v1` (published 2026-10-27 11:08:52 UTC; categories: `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Cross-listed in genomics and quantitative methods; the authors compare 129 public assemblies and report 5,031 paired metric comparisons against the original software.
- **Claimed contribution:** The authors report exact reproduction of sequence metrics and read counts, with Spearman correlations of 0.94 for assembly score and 0.98 for good-mapping rate. They also provide compressed-input support and a Python implementation.
- **Caveat:** The authors explicitly say read-based scores are not numerically interchangeable with the original implementation; an assembly-quality score is not a guarantee of biological completeness or correctness.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis

### 7. [HGPRGDel: GPR-Aware Learning and Ranking for Growth-Coupled Gene Deletion Design](https://arxiv.org/abs/2610.37478)
- **Abstract:** HGPRGDel ranks candidate microbial gene deletions for growth-coupled production while explicitly representing gene–protein–reaction logic.
- **Authors:** Ziwei Yang, Takeyuki Tamura
- **arXiv:** `2610.37478v1` (published 2026-10-27 16:07:02 UTC; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** The authors evaluate three metabolic models (e_coli_core, iMM904, iML1515) and report comparison with baseline learning configurations and deletion-ranking methods.
- **Claimed contribution:** The paper reports the highest macro-F1 and AUC among tested learning configurations; rankings recovered an average 90% of reference deletion genes while examining fewer candidates. This is computational prioritization followed by constraint-based assessment.
- **Caveat:** Results use computationally curated/reference strategies; the abstract reports no engineered-strain experiments or metabolite-production measurements. Performance in silico does not show that a ranked intervention increases yield in a laboratory strain.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** Molecular & cell biology; Quantitative methods

### 8. [Enhancing Clinical Classifier Robustness with Deep Representation Learning Based OOD Detection on DNA Methylation Data](https://arxiv.org/abs/2610.36344)
- **Abstract:** The authors test out-of-distribution detection for methylation-array tumor classifiers using learned representations and several distance-based methods.
- **Authors:** Md Zahangir Alom, Quynh T. Tran, Breuer Alexandar, Brent A. Orr
- **arXiv:** `2610.36344v1` (published 2026-10-26 22:11:07 UTC; categories: `q-bio.GN`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Three-category cross-listing and evaluation across public sarcoma and brain-tumor cohorts plus an independent clinical test set. Authors report AUROC and operating-point metrics for both in-/out-of-distribution directions.
- **Claimed contribution:** Authors report that 1D subspace analysis performed best among five approaches; independent-test mean AUROC was 0.976, with TNR@95TPR of 0.935. This is classifier-quality-control evaluation, not prospective clinical deployment.
- **Caveat:** The abstract does not give the independent test-set size or establish performance across laboratories, platforms, or tumor types beyond those studied. Out-of-distribution flagging does not itself validate a tumor diagnosis.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** DNA & genomics; Biomedical & translational medicine; Quantitative methods

### 9. [ACOR: incremental evidence accumulation towards real-time DNA storage reconstruction](https://arxiv.org/abs/2610.36500)
- **Abstract:** ACOR incrementally reconstructs DNA-storage sequences from streaming read evidence using a persistent k-mer ledger and length-constrained decoding.
- **Authors:** Linxuan Han, Huaming Wu, Shi Jia, Guanjin Qu
- **arXiv:** `2610.36500v1` (published 2026-10-27 01:58:03 UTC; categories: `cs.IR`, `q-bio.GN`)
- **Evidence for ranking:** Cross-listed in information retrieval and genomics; tests cover real and simulated datasets, including the authors’ short-read NGS library with more than ten million reads.
- **Claimed contribution:** The authors report near-complete recovery with second-scale reconstruction on their wet-lab library and large speedups over tested serial baselines under parallel execution. This is computational pipeline evaluation using sequencing data.
- **Caveat:** “Near-complete” is not numerically specified in the abstract, and reported speedups depend on baseline configurations and hardware. The study concerns DNA as an information-storage medium, not genomic interpretation.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 10. [Retrospective macromolecular pool fraction mapping from conventional clinical MRI: a physics-guided self-supervised deep learning framework](https://arxiv.org/abs/2610.37213)
- **Abstract:** A physics-guided self-supervised model estimates macromolecular pool fraction maps from conventional brain MRI without paired quantitative reference scans.
- **Authors:** Jelmer van Lune, Miha Fuderer, Oscar van der Heide, Matteo Maspero, Martin B. Schilder, Jan Willem Dankbaar, Stefano Mandija, Alessandro Sbrizzi
- **arXiv:** `2610.37213v1` (published 2026-10-27 13:27:34 UTC; categories: `physics.med-ph`, `cs.CV`, `cs.LG`)
- **Evidence for ranking:** Cross-listed in medical physics, computer vision and machine learning. The authors report a multisite, multivendor, multiprotocol dataset of 7,705 MRI sessions, including 1,237 test sessions and 70 sessions with demyelinating-disease labels.
- **Claimed contribution:** Authors report stable MPF estimates across protocol groups and lower MPF in segmented lesions than normal-appearing white matter in the labeled subset. They also report cross-protocol consistency in two scans from one healthy volunteer.
- **Caveat:** The disease-labeled analysis is small and observational, and the single-volunteer protocol comparison does not establish broad prospective reproducibility or diagnostic utility. No patient outcome or treatment benefit was tested.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 11. [OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents](https://arxiv.org/abs/2610.37081)
- **Abstract:** OpenGray evaluates whether automated radiotherapy-planning systems make correct submit-or-escalate decisions on feasible and contradictory planning tasks.
- **Authors:** Humza Nusrat, Kundan Thind
- **arXiv:** `2610.37081v1` (published 2026-10-27 11:42:47 UTC; categories: `cs.AI`, `physics.med-ph`)
- **Evidence for ranking:** Cross-listed in AI and medical physics; benchmark covers 30 patients and the authors also examined logs from 39 stereotactic radiosurgery runs. Semantic Scholar listed zero citations at this snapshot, a current total and not a period trend.
- **Claimed contribution:** The authors report that high aggregate decision accuracy concealed weak escalation on deliberately contradictory dose goals; some systems escalated only 25–50% of overlap contradictions. They argue decision correctness should be measured alongside dose quality.
- **Caveat:** This is a benchmark of planning agents, not a clinical trial or evidence that an agent can safely plan or approve radiotherapy. The task set and evaluated systems are limited.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 12. [Optimization of 99mTc proton-induced production by means of cross-section measurements of technetium radioisotopes from molybdenum targets](https://arxiv.org/abs/2610.36949)
- **Abstract:** The authors measure proton-induced technetium-isotope production cross-sections from molybdenum targets to optimize a medical-cyclotron route to 99mTc.
- **Authors:** Dellepiane Gaia, D'Uva Sofia, Eggimann Lars, Gottstein Alexander, Juillerat Samuel, Kasanda Eva, Mateu Isidre, Scampoli Paola, Kadenko Ihor, Braccini Saverio
- **arXiv:** `2610.36949v1` (published 2026-10-27 10:10:48 UTC; categories: `nucl-ex`, `physics.med-ph`)
- **Evidence for ranking:** Cross-listed in nuclear experiment and medical physics; measured cross-sections and production tests directly support a biomedical isotope-production question.
- **Claimed contribution:** Authors report suitable conditions near 16 MeV with a 0.5 mm enriched 100Mo target; for a 10-hour irradiation they calculate about 1.7 GBq/μA and report production tests demonstrating feasibility within stated radionuclidic-purity limits.
- **Caveat:** The activity is a calculated yield based on measurements and production tests, not evidence of routine commercial-scale supply or clinical outcomes.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 13. [Image-Domain CT Metal Artifact Reduction Using an Endpoint-Conditioned Diffusion Bridge](https://arxiv.org/abs/2610.36319)
- **Abstract:** RDBM-MAR uses an endpoint-conditioned diffusion bridge to reduce metal artifacts in CT images, initialized from the artifact-corrupted scan.
- **Authors:** Hang Yu, Mojtaba Safari, Shansong Wang, Mingzhe Hu, Xiaofeng Yang
- **arXiv:** `2610.36319v1` (published 2026-10-26 21:45:56 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Medical-physics batch paper with a held-out comparison on 1,322 CT slices from a 14,000-slice paired dataset and five named comparator methods.
- **Claimed contribution:** Authors report best PSNR, SSIM, and MAE among tested methods using 10 reverse steps; one clinical case was assessed qualitatively. This supports image-restoration performance on the stated benchmark.
- **Caveat:** The clinical case is qualitative and singular; benchmark image metrics do not establish diagnostic accuracy, robustness across scanners, or improved patient outcomes.
- **Announcement type:** new submission, 2026-10-28 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

## Trending Research Themes

The selected papers cluster around computational validation rather than new clinical evidence. Protein modeling is represented by AMARO v2.0 and GlycoWeave: one targets dynamics across diverse complexes, while the other focuses on glycan-aware pose modeling. mdRNAcat adds a large simulated RNA resource, and ESMFold interpretability examines learned structure representations; neither is experimental validation of biological mechanism. Genomic data methods include HELICS synthetic common-variant cohorts, methylation OOD detection, ACOR DNA-storage reconstruction, and pyTransRate transcriptome-assembly scoring. In medical physics, van Lune et al. test MRI-derived biomarker mapping, OpenGray audits radiotherapy-agent decisions, the 99mTc paper reports production measurements, and Yu et al. evaluate CT restoration. These are distinct directions and evidence types, not independent confirmation of one field-wide shift.

## Open Problems and Research Directions

For AMARO v2.0 and GlycoWeave, test on independently curated complexes and report blinded structural or biochemical validation alongside simulation and pose metrics; current papers identify energy, pose, or benchmark-generalization limits. For mdRNAcat and ESMFold interpretability, compare learned ensembles or concepts against experimental structural restraints and independent model checkpoints. For HELICS, assess membership-inference and attribute leakage separately from fidelity, then test underrepresented ancestry groups and rare variants in independent biobanks. For pyTransRate, compare assembly rankings with orthogonal long-read and reference-based truth sets because scores are not numerically interchangeable with legacy outputs.

For methylation OOD detection, publish cohort sizes and evaluate across independent laboratories, platforms, and tumor taxonomies with prespecified thresholds. For MRI MPF mapping, use larger external cohorts with paired quantitative-reference scans and longitudinal outcomes. For OpenGray and CT artifact reduction, expand to multi-institutional tasks and scanner/protocol shifts, measuring expert decisions rather than image metrics alone. For 99mTc production, replicate yield and purity across target batches and operating conditions before inferring scalable supply. For HGPRGDel, test ranked deletion strategies in engineered strains and measure growth and metabolite output. These are proposed follow-ups, not claims of clinical readiness.

## Takeaway

The 28 October batch offers technically substantial methods across proteins, RNA, genomes, transcriptomes, and imaging. Its clearest signal is better tooling and evaluation design; evidence ranges from simulations and retrospective data to production experiments, but clinical utility is not established by these reports. This is a relevance-ranked snapshot of arXiv, not a popularity chart, systematic biomedical survey, or clinical guidance.

## Method and sources

- **Window:** daily announcement batch dated 2026-10-28 only; date range 2026-10-28 through 2026-10-28. Snapshot: 2026-10-30 01:15:40 UTC. The current-day listings showed no later announcement batch, so this uses the prior available batch.
- **Candidate scope/query:** `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`; cross-lists deduplicated by arXiv ID. The broad API query was sorted by submitted date; official recent listings for quantitative biology and medical physics were checked against individual arXiv abstract pages. The `/list/cs.BI` route is not a valid archive page, so that category was covered through the query and relevant genomics cross-lists. Neural/population work without a clear molecular or biomedical connection was excluded.
- **Ranking:** attention evidence for this very recent batch was sparse, so entries are labeled “Notable recent papers” and ranked by biological/biomedical relevance, cross-list breadth, and reported validation setting—not readership. One independently surfaced arXiv News explainer discussed AMARO v2.0. Semantic Scholar showed zero citations for OpenGray at snapshot; that current total is not a period gain. No downloads or views were inferred.
- **Coverage:** arXiv is not a representative biomedical index; many experimental and clinical preprints are on bioRxiv or medRxiv. This is not a systematic review. Computational predictions, retrospective cohorts, and experimental production measurements are distinguished.
- **Sources:** [arXiv quantitative biology recent listings](https://arxiv.org/list/q-bio/recent); [arXiv medical physics recent listings](https://arxiv.org/list/physics.med-ph/recent); the thirteen linked arXiv abstract pages above. Corroborating discussion: [arXiv News explainer for AMARO v2.0](https://arxivnews.org/en/articles/4763ba88-de7e-4cce-b143-5f006e776e36). Citation metadata: [Semantic Scholar record for OpenGray](https://api.semanticscholar.org/graph/v1/paper/arXiv:2610.37081?fields=title,citationCount,influentialCitationCount,referenceCount).
