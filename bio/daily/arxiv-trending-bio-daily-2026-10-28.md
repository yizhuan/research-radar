# arXiv Biology & Biomedicine — Daily, 2026-10-28

## Headline
The Wednesday, 28 October 2026 announcement batch yielded 12 notable papers across biomolecules, genomics, quantitative biology, and medical physics. The strongest cluster is computational modeling tested against structural or cohort-scale data, with protein–glycan modeling, biomolecular dynamics, and synthetic genomics especially visible. Agenda: what each method contributes, what evidence the authors report, and where validation remains thin. arXiv has no official trending chart; this is an inferred relevance ranking, not a popularity ranking, and arXiv omits much biomedical work published on bioRxiv, medRxiv, and elsewhere. Attention evidence for this batch is sparse.

## Notable recent papers

### 1. [Accurate structural modelling of protein-glycan recognition with GlycoWeave](https://arxiv.org/abs/2610.37410)
- **Abstract:** GlycoWeave uses chemically constrained diffusion and multiscale molecular representations to predict protein-bound glycan conformations, reporting a 71.9% Top-25 high-quality success rate on 698 complexes versus 19.2% for AlphaFold 3.
- **Authors:** Huifeng Zhao, Jintu Zhang, Yifei Xiao, Youqiao Qian, Silong Zhai, Zichang Jin, Li Wang, Yuchao Wang, Hang Dong, Yifan Zhao, Zhenxing Wu, Hongyan Du, Yuansheng Huang, Bowei Zhao, Xiaorui Wang, Shukai Gu, Jike Wang, Zhongjun Li, Zhongtang Li, Tingjun Hou, Yu Kang
- **arXiv:** `2610.37410v1` (published 2026-10-27 15:27:09 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct biomolecular focus; the authors report a sizable benchmark and head-to-head AlphaFold 3 comparison. Semantic Scholar showed 0 citations and 0 influential citations at the snapshot; popularity is not established.
- **Claimed contribution:** The authors claim internal-coordinate diffusion preserves glycan connectivity and stereochemistry while combining atom- and monosaccharide-level context; the abstract reports 0.34 seconds per sampled pose.
- **Caveat:** This is structural-prediction benchmarking, not prospective binding or biochemical validation; the training signal also includes computationally refined structures.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [A unified coarse-grained neural network potential for the dynamics of biomolecular complexes](https://arxiv.org/abs/2610.37606)
- **Abstract:** AMARO v2.0 is a heavy-atom coarse-grained neural potential for proteins, drug-like molecules, and their complexes, evaluated across 262 complexes and selected binding case studies.
- **Authors:** Antonio Mirarchi, Stephen E. Farr, Adrià Peréz, Gianni De Fabritiis
- **arXiv:** `2610.37606v1` (published 2026-10-27 17:37:10 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Strong biomolecular relevance and reported coverage of 262 complexes across 11 targets, plus comparison with all-atom molecular mechanics in targeted cases. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors report charge-conditioned dynamics that distinguish trypsin–benzamidine protonation states and reach its crystal pose in 3.3 times as many trajectories as the tested all-atom baseline at fixed estimated GPU time.
- **Caveat:** The authors report binding-free-energy estimates more favorable than experimental references and unresolved pose-recovery or site-specificity issues for SHP2 and CDK8; this is simulation evidence, not experimental validation of drug performance.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [HELICS: Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching](https://arxiv.org/abs/2610.36361)
- **Abstract:** HELICS generates conditional synthetic common-variant genomes using latent flow matching trained on more than 417,000 UK Biobank genomes, with reported external allele-frequency and linkage-structure fidelity.
- **Authors:** Ahmad Abdel-Azim, Xihong Lin
- **arXiv:** `2610.36361v1` (published 2026-10-26 22:25:36 UTC; categories: `q-bio.GN`, `cs.LG`)
- **Evidence for ranking:** Direct genomic-method contribution, biobank-scale training, and an external-cohort evaluation; arXiv comments list NeurIPS 2026. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors claim phasing-free generation across more than 600,000 SNPs and show conditional dosage shifts correlated with published association weights.
- **Caveat:** The paper reports weaker fidelity for low-frequency variants and poorer alignment or polygenic-score recovery for underrepresented ancestry groups; the principal benchmark is restricted to common variants and European-ancestry evaluations.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 4. [Retrospective macromolecular pool fraction mapping from conventional clinical MRI: a physics-guided self-supervised deep learning framework](https://arxiv.org/abs/2610.37213)
- **Abstract:** A physics-guided model estimates macromolecular pool fraction from conventional brain MRI and is evaluated on a multisite, multivendor dataset of 7,705 sessions, including 1,237 test sessions.
- **Authors:** Jelmer van Lune, Miha Fuderer, Oscar van der Heide, Matteo Maspero, Martin B. Schilder, Jan Willem Dankbaar, Stefano Mandija, Alessandro Sbrizzi
- **arXiv:** `2610.37213v1` (published 2026-10-27 13:27:34 UTC; categories: `physics.med-ph`, `cs.CV`, `cs.LG`)
- **Evidence for ranking:** Broad retrospective dataset and explicit multisite/protocol consistency evaluation; relevant to quantitative imaging of demyelinating disease. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors report stable MPF estimates across vendor/protocol groups and lower MPF in lesions than normal-appearing white matter in 70 disease-labeled sessions.
- **Caveat:** It is a retrospective estimate without paired quantitative reference scans; the lesion association does not establish diagnostic performance or clinical utility.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 5. [pyTransRate: 1 reference-free quality assessment of de novo transcriptome assemblies with current aligners and quantifiers](https://arxiv.org/abs/2610.37031)
- **Abstract:** pyTransRate reimplements reference-free transcriptome-assembly quality scoring in Python and compares it with the prior TransRate release across 129 public assemblies.
- **Authors:** Matthew MacManes
- **arXiv:** `2610.37031v1` (published 2026-10-27 11:08:52 UTC; categories: `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Practical RNA-sequencing workflow relevance and 5,031 paired comparisons; the abstract reports strong rank correlations with the original software. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The author claims the updated Python implementation reproduces sequence metrics and read counts while supporting current aligners and compressed inputs.
- **Caveat:** It requires the reads used to build each assembly, and its read-based scores are explicitly not numerically interchangeable with the old release.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis

### 6. [Structure, Not Sequence: Tracking and Validating Folding Mechanisms in ESMFold's Trunk with Sparse Autoencoders](https://arxiv.org/abs/2610.36226)
- **Abstract:** Sparse autoencoders and attribution analyses are used to interpret ESMFold's internal folding computations and relate learned features to structural geometry and fold-quality predictions.
- **Authors:** Bohan Liu, Xiaohan Fan, Wenqian Ye, Aidong Zhang
- **arXiv:** `2610.36226v1` (published 2026-10-26 20:04:57 UTC; categories: `q-bio.QM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Direct protein-folding relevance and an explicit attempt to connect internal features to known biochemical structure; selected for relevance, not demonstrated attention. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors claim sparse dictionaries separate inherited sequence semantics from pairwise geometric computation and that feature activations forecast ESMFold's own fold quality.
- **Caveat:** Interpretability and biochemical alignment are computational analyses of one model; they do not independently establish that the inferred circuits are causally necessary or generalize to other folding systems.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 7. [Enhancing Clinical Classifier Robustness with Deep Representation Learning Based OOD Detection on DNA Methylation Data](https://arxiv.org/abs/2610.36344)
- **Abstract:** The authors test out-of-distribution detection for DNA-methylation tumor classifiers on public sarcoma and brain-tumor cohorts and an independent clinical dataset.
- **Authors:** Md Zahangir Alom, Quynh T. Tran, Breuer Alexandar, Brent A. Orr
- **arXiv:** `2610.36344v1` (published 2026-10-26 22:11:07 UTC; categories: `q-bio.GN`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Relevant genomic quality-control problem, multiple OOD methods, and an independent clinical test set are reported. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors report that 1D-SSA led their evaluated OOD methods, with mean AUROC 0.976 on the independent clinical test set.
- **Caveat:** The abstract does not specify that clinical set's size or composition, and the work evaluates classifier quality control rather than prospective diagnostic outcomes.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** DNA & genomics; Biomedical & translational medicine; Quantitative methods

### 8. [ACOR: incremental evidence accumulation towards real-time DNA storage reconstruction](https://arxiv.org/abs/2610.36500)
- **Abstract:** ACOR incrementally reconstructs DNA-storage sequences from streaming reads, with tests on simulated/public data and the authors' short-read wet-lab library.
- **Authors:** Linxuan Han, Huaming Wu, Shi Jia, Guanjin Qu
- **arXiv:** `2610.36500v1` (published 2026-10-27 01:58:03 UTC; categories: `cs.IR`, `q-bio.GN`)
- **Evidence for ranking:** Direct DNA-sequencing application and reported wet-lab-library evaluation covering more than ten million reads. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors claim second-scale reconstruction and parallel speedups from tens to over a thousand-fold over the tested serial configurations.
- **Caveat:** The evidence is about data-storage reconstruction on the tested libraries and baselines; it does not demonstrate an end-to-end production sequencing deployment.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** DNA & genomics; Quantitative methods

### 9. [HGPRGDel: GPR-Aware Learning and Ranking for Growth-Coupled Gene Deletion Design](https://arxiv.org/abs/2610.37478)
- **Abstract:** HGPRGDel learns gene-deletion priorities for microbial production and evaluates the resulting candidate strategies with constraint-based models across three metabolic reconstructions.
- **Authors:** Ziwei Yang, Takeyuki Tamura
- **arXiv:** `2610.37478v1` (published 2026-10-27 16:07:02 UTC; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** A direct metabolic-engineering application, three model backgrounds, and reported recovery of 90% of reference deletion genes while examining fewer genes. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors claim explicit gene–protein–reaction logic improves learned intervention ranking while retaining downstream mechanistic assessment.
- **Caveat:** These are computational reconstructions and reference-strategy recovery results, not experimentally measured strain yields or wet-lab confirmation.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Molecular & cell biology; Bioinformatics & sequence analysis; Quantitative methods

### 10. [OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents](https://arxiv.org/abs/2610.37081)
- **Abstract:** OpenGray benchmarks whether radiotherapy-planning agents recognize incompatible dose goals and feasible plans, using 30 patients plus logs from 39 stereotactic radiosurgery runs.
- **Authors:** Humza Nusrat, Kundan Thind
- **arXiv:** `2610.37081v1` (published 2026-10-27 11:42:47 UTC; categories: `cs.AI`, `physics.med-ph`)
- **Evidence for ranking:** A direct medical-physics application and an evaluation that reports decision errors hidden by aggregate accuracy. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors report that agents often failed to escalate contradictory plans despite high overall accuracy, motivating decision-centered benchmark criteria.
- **Caveat:** The task set is small and partly constructed; observed agent behavior does not establish safety or performance in prospective clinical workflow.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 11. [Image-Domain CT Metal Artifact Reduction Using an Endpoint-Conditioned Diffusion Bridge](https://arxiv.org/abs/2610.36319)
- **Abstract:** RDBM-MAR uses an endpoint-conditioned diffusion bridge to reduce metal artifacts in CT and is tested on 14,000 paired challenge slices and one qualitative clinical case.
- **Authors:** Hang Yu, Mojtaba Safari, Shansong Wang, Mingzhe Hu, Xiaofeng Yang
- **arXiv:** `2610.36319v1` (published 2026-10-26 21:45:56 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Medical-imaging method with a held-out test set and five named comparator methods; the authors report significant gains on three image metrics. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors report improved PSNR, SSIM, and MAE using 10 deterministic reverse steps, while another comparator had the best LPIPS.
- **Caveat:** The quantitative test is on challenge slices and the clinical evidence is one qualitative case; image metrics alone do not establish improved patient outcomes.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 12. [Optimization of 99mTc proton-induced production by means of cross-section measurements of technetium radioisotopes from molybdenum targets](https://arxiv.org/abs/2610.36949)
- **Abstract:** The authors measure proton-induced technetium production cross-sections on molybdenum targets and report production tests supporting a proposed medical-cyclotron route to 99mTc.
- **Authors:** Dellepiane Gaia, D'Uva Sofia, Eggimann Lars, Gottstein Alexander, Juillerat Samuel, Kasanda Eva, Mateu Isidre, Scampoli Paola, Kadenko Ihor, Braccini Saverio
- **arXiv:** `2610.36949v1` (published 2026-10-27 10:10:48 UTC; categories: `nucl-ex`, `physics.med-ph`)
- **Evidence for ranking:** Direct medical-isotope production relevance and measured reaction cross-sections followed by reported production tests. Semantic Scholar: 0 citations, 0 influential citations at snapshot.
- **Claimed contribution:** The authors identify approximately 16 MeV protons and a 0.5 mm enriched 100Mo target as suitable and calculate a yield near 1.7 GBq/μA for 10 hours of irradiation.
- **Caveat:** The reported yield is calculated from the measured parameters; this does not establish routine-scale supply, cost, or clinical deployment.
- **Announcement type:** new submission, 2026-10-28
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

## Trending Research Themes

Within this selected batch, two closely related papers push computational structure modeling toward richer chemistry: GlycoWeave addresses glycan flexibility and stereochemistry, while AMARO v2.0 models charged biomolecular complexes. This is a small batch-level cluster, not evidence of a field-wide shift. Genomic data methods form another strand: HELICS synthesizes cohort-scale genotypes, pyTransRate modernizes transcriptome assembly assessment, ESMFold analysis probes model representations, and ACOR handles DNA-sequencing reads for storage reconstruction. Medical applications focus on measurement and decision quality: the MPF and methylation papers assess retrospective or out-of-distribution signals, while OpenGray and CT-MAR test planning or image-restoration methods. HGPRGDel and the 99mTc study are distinct examples of computational metabolic design and experimental isotope production, respectively; they should not be conflated as a shared trend.

## Open Problems and Research Directions

Author-stated boundaries include AMARO's over-favorable free-energy estimates and remaining pose/site-specificity failures, and HELICS's weaker low-frequency-variant and underrepresented-ancestry performance. Across the selected papers, the next useful checks are concrete: test GlycoWeave on prospectively withheld glycan complexes and then compare predicted poses with structural or binding assays; calibrate AMARO free energies against a larger, independently measured affinity panel and probe off-site binding across targets; evaluate HELICS on external multi-ancestry cohorts, especially rare variants, and measure downstream association bias before using synthetic cohorts for inference. For the MPF method, a blinded multisite comparison against dedicated quantitative magnetization-transfer scans and pathology-linked outcomes would test the retrospective estimates more directly. For DNA-methylation OOD detection, report independent-cohort size, tumor-type composition, and prospective referral consequences. These are research proposals grounded in the reported limitations, not clinical recommendations.

## Takeaway
This batch is notable for methods that make molecular and clinical data more usable, but its strongest claims remain benchmark, retrospective, or computational results. Glycan modeling, coarse-grained complex dynamics, and synthetic-genome generation show substantial reported evaluation; none should be mistaken for validated clinical benefit. Because independent attention signals are absent or immature, the ordering reflects fit and reported evidence—not measured popularity.

## Method and sources
- **Window:** daily; announcement-batch coverage date 2026-10-28 to 2026-10-28. The latest arXiv batch was Wednesday, 28 October 2026; no prior-batch substitution was needed. Selected v1 submissions have arXiv UTC timestamps from 2026-10-26 through 2026-10-27.
- **Snapshot:** 2026-10-28 17:16:37 UTC.
- **Listings checked:** [q-bio.BM](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), and [physics.med-ph](https://arxiv.org/list/physics.med-ph/recent). arXiv rejected the configured `cs.BI` recent-list URL as an invalid category; the explicit API query below did include the requested term. The valid listings contained 18 entries, deduplicated to 16 unique IDs; one neuroscience-focused q-bio.CB entry was excluded from the narrower molecular/biomedical emphasis. Twelve of the remaining 15 candidates are listed here.
- **Candidate query:** [arXiv API query](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200). The 200 returned results extended back to 9 October, beyond this daily window; categories with cross-list duplicates were deduplicated by versionless arXiv ID.
- **Ranking:** arXiv has no official trend/readership ranking. Semantic Scholar Graph API snapshot fields were checked for title, authors, citations, influential citations, references, fields, and external IDs; all 12 selected papers had 0 citationCount and 0 influentialCitationCount. Targeted title searches found no independent technical discussion that established attention. Since attention evidence was sparse, this is a relevance-ranked “Notable recent papers” list, using biological/medical fit and the reported validation setting as tie-breakers; no numeric trend score is implied. The citation figures are current totals, not gains during this announcement window.
- **Sources:** Each entry links to its verified arXiv abstract page. Top three papers were also read from their PDFs for introduction, results, and conclusion/limitations. Semantic Scholar records for the selected set were retrieved on 2026-10-28. This is not systematic coverage of bioRxiv, medRxiv, clinical practice, or all biomedical research; no clinical recommendation is made.
