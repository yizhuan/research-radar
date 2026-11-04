# Notable recent papers: biology and biomedicine arXiv — 2026-11-03

The latest visible daily batch is Tuesday, 3 November 2026: 13 selected papers, with protein/peptide design, single-cell RNA inference, and evidence-aware evaluation among the strongest threads. Spoken agenda: what these methods claim, what data support them, and what still needs biological or external validation. arXiv has no official trending chart; this is an inferred, relevance-ranked selection from an incomplete biomedical corpus, not a popularity ranking. Much experimental and clinical preprint research appears on bioRxiv or medRxiv instead.

## Notable recent papers (ranked by relevance)

### 1. [RangeFinder: Predicting Ligand Property Ranges from Protein Pockets](https://arxiv.org/abs/2611.03379)
- **Abstract:** RangeFinder uses an SE(3)-equivariant model to predict ranges for nine ligand properties from protein-pocket structure, chemistry, and evolutionary context, aiming to narrow molecular search.
- **Authors:** Alan Nadelsticher Ruvalcaba, Chris Alvin, Supratik Mukhopadhyay, Adam Bess
- **arXiv:** `2611.03379v1` (published 2026-11-02 16:21:09 UTC; categories: `cs.LG` (primary), `q-bio.BM`)
- **Evidence for ranking:** Direct protein–ligand relevance, q-bio.BM cross-list, and an arXiv comment recording acceptance at the NeurIPS 2026 AI for Drug Discovery workshop; BioLiP2 evaluation reports range-IoU 0.464 ± 0.002 and Reduction-Recall F-score 0.543 ± 0.011.
- **Claimed contribution:** The authors propose pocket-level property-range prediction as a complement to generating or scoring individual ligands and report 12.2 ms inference per pocket.
- **Caveat:** Evaluation is limited to pockets with at least three known ligands; the authors note possible homology overlap across UniProt-based splits. Prospective ligand discovery or binding has not been demonstrated.
- **Announcement type:** new submission, cross-listed into q-bio.BM in the 2026-11-03 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [PeptSol: A Translational Benchmark for Protected-Peptide Solubility in Drug Manufacturing](https://arxiv.org/abs/2611.00749)
- **Abstract:** PeptSol benchmarks prediction of protected-peptide solubility relevant to liquid-phase peptide synthesis, using 1,388 curated measurements and chemistry-aware splits.
- **Authors:** Alexander Arjun Lobo, Marc Saouda, Urvi Awasthi, Leonid Zhukov
- **arXiv:** `2611.00749v1` (published 2026-10-31 08:56:07 UTC; categories: `cs.LG` (primary), `physics.chem-ph`, `q-bio.BM`)
- **Evidence for ranking:** Direct peptide-manufacturing relevance; an arXiv comment records acceptance at the NeurIPS 2026 AI for Drug Discovery workshop; compares seven molecular encoders on a source-curated benchmark.
- **Claimed contribution:** The authors report best macro-F1 of 0.843 for binary solubility in the historical subset, but no foundation model consistently beats a fingerprint-plus-descriptor baseline across tasks and splits.
- **Caveat:** The measurements cover 84 parent sequences and 101 protected structures, with 92.5% from one historical programme. Retrospective solubility prediction does not establish synthesis yield, recovery, or process performance.
- **Announcement type:** new submission, cross-listed into q-bio.BM in the 2026-11-03 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [Automatic Generation of Novel Highly-Functional Molecular Sequences](https://arxiv.org/abs/2611.03603)
- **Abstract:** On two complete fitness landscapes, the authors compare a position-probability “biased typewriter” generator with a variational autoencoder and report that the better search method depends on landscape and training-set size.
- **Authors:** Vincent R. Ragusa, Chrisoph Adami
- **arXiv:** `2611.03603v1` (published 2026-11-02 18:41:20 UTC; categories: `q-bio.BM` (primary))
- **Evidence for ranking:** Direct biomolecular sequence-design fit and first-listed in the focused biomolecules category; the abstract reports evaluation on two complete landscapes.
- **Claimed contribution:** The authors propose training-free sequence search and report a sample-size- and landscape-dependent comparison: the biased typewriter is more efficient on DHFR and low-data settings, while the autoencoder can do better on Avida at larger sample sizes, with signs of overfitting.
- **Caveat:** The comparison is computational on existing DHFR and Avida landscapes; the paper does not report synthesis or antimicrobial and cytotoxicity assays of generated peptides. Selective antibacterial peptides are a proposed application, not a demonstrated result.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Biochemistry & proteins; DNA & genomics; Quantitative methods

### 4. [Can agents reliably design therapeutic antibodies?](https://arxiv.org/abs/2611.00558)
- **Abstract:** The authors evaluate agentic antibody design under instruction-following and black-box optimization settings, finding trade-offs among tool use, design history, exploration, and optimization.
- **Authors:** Asli Alpman, Nick Bhattacharya, Aaron Solomon, Hunter Elliott
- **arXiv:** `2611.00558v1` (published 2026-10-31 02:35:17 UTC; categories: `q-bio.QM` (primary), `cs.LG`)
- **Evidence for ranking:** Direct antibody-design focus and q-bio.QM placement; tests ten expert-validated affinity-improvement tasks and compares an in-silico optimizer with Bayesian optimization.
- **Claimed contribution:** The authors report that tools improve instruction following and sequence exploration but reduce optimization performance, while design history improves optimization at the expense of exploration.
- **Caveat:** Reported optimization is in silico; the paper does not establish experimental binding affinity or therapeutic activity of newly designed antibodies.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 5. [Coupling cellular trajectories and RNA kinetics on continuous expression manifolds with ManifoldVelo](https://arxiv.org/abs/2611.03056)
- **Abstract:** ManifoldVelo jointly fits pseudotime, continuous spliced/unspliced RNA trajectories, and kinetic dynamics, with tests on simulated cyclic and branching processes and real single-cell datasets.
- **Authors:** Zhen Zhou, Jiachen Li, Yuan Liu, Xiaoyong Pan, Hong-Bin Shen
- **arXiv:** `2611.03056v1` (published 2026-11-02 12:49:50 UTC; categories: `q-bio.QM` (primary))
- **Evidence for ranking:** Direct RNA/transcriptomics relevance; comparisons span cyclic and branching simulations plus real-data analyses; the arXiv comment links code and numerical source tables.
- **Claimed contribution:** The authors report improved pseudotime and velocity comparisons on selected benchmarks and transfer of predictions to new cells using spliced RNA with a fixed reference.
- **Caveat:** Pseudotime and RNA velocity are computational estimates; agreement with marker or stage patterns is not direct time-resolved validation of every inferred trajectory.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 6. [An auditable agentic pipeline for variant-to-gene prioritisation, validated against orthogonal functional evidence](https://arxiv.org/abs/2611.01461)
- **Abstract:** V2G records evidence retrieval and ranks candidate genes for GWAS loci; the authors test whether language-model reranking gains depend on the retrieved evidence.
- **Authors:** Shakuntala Baichoo, Sohail (Neel) Sarkar, Bo Wang
- **arXiv:** `2611.01461v1` (published 2026-11-01 02:48:40 UTC; categories: `q-bio.GN` (primary), `cs.AI`)
- **Evidence for ranking:** Direct variant-to-gene genomics task; the abstract quantifies held-out results and tests evidence-row shuffling and known-gene recall.
- **Claimed contribution:** On 135 loci with successful retrieval, reranking improves Precision@1 over the evidence ordering, but the authors find no detected difference from Open Targets L2G or training-membership baselines; controls suggest the gain reflects recall of known genes more than use of presented evidence.
- **Caveat:** The paper reports train/test overlap and retrieval-conditioned subsets; an auditable evidence trail is not proof that an agent reasoned from that evidence.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Biomedical & translational medicine

### 7. [HistoTx: Early fusion of H&E images and spatial transcriptomics at varying spatial transcriptomics resolution with self-supervised learning](https://arxiv.org/abs/2611.02681)
- **Abstract:** HistoTx fuses histology-image and spatial-transcriptomic tokens in a shared transformer and evaluates image-only and multimodal inference across gene-expression and pathology tasks.
- **Authors:** Alice Driessen, Emil Malmsten, Steffen Wolf, Bernd Illing, Isinsu Katircioglu, Adriano Martinelli, Rolf Stahel, Solange Peters, Enriqueta Felip, Sanjay Popat, Krisztian Homicsko, Raphael Gottardo, Marianna Rapsomaniki, Fei Tang
- **arXiv:** `2611.02681v1` (published 2026-11-02 07:36:09 UTC; categories: `cs.LG` (primary), `cs.AI`, `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Cross-listed in genomics and quantitative biology; an arXiv comment records presentation at the ICML 2026 multimodal life-sciences workshop; evaluated on spatial-transcriptomics and pathology benchmarks.
- **Claimed contribution:** The authors report stronger gene-expression prediction than image-only baselines on several benchmarks and further gains when transcript data are provided at inference.
- **Caveat:** The full text notes that increased HEST image exposure during continued pretraining may partly explain gains; a task-specific supervised baseline outperforms HistoTx on one BEAT prediction task. Benchmark results do not establish clinical utility or transfer to new institutions.
- **Announcement type:** new submission, cross-listed into q-bio.GN and q-bio.QM in the 2026-11-03 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Molecular & cell biology

### 8. [Cell lines that share a well are not independent observations in the Tahoe-100M drug screen](https://arxiv.org/abs/2611.01604)
- **Abstract:** The authors test whether pooled cell lines in the same well share expression effects that invalidate treating each line as an independent observation in drug-screen evaluation.
- **Authors:** Xuanrui Huang
- **arXiv:** `2611.01604v1` (published 2026-11-01 05:42:09 UTC; categories: `q-bio.QM` (primary))
- **Evidence for ranking:** Directly relevant to drug-screen experimental design; reports analyses of 13 plates, replicate wells, and well-by-well repeated plates, with code and results linked in the arXiv comment.
- **Claimed contribution:** The authors report that within-well dependence can inflate predictive scores and significance tests, and argue that the well should be treated as the experimental unit.
- **Caveat:** Findings concern the Tahoe-100M pooled-screen setting; extension to other pooled assays and independent datasets needs checking.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 9. [The DynaCell Evaluation Suite for Dynamic 3D Virtual Staining of Live Cells](https://arxiv.org/abs/2611.02324)
- **Abstract:** DynaCell provides paired 3D live-cell imaging data, baseline virtual-staining models, and multi-level metrics for image fidelity, organelle segmentation, and cell-phenotype similarity over time.
- **Authors:** Alexandr A. Kalinin, Dihan Zheng, Taylla Milena Theodoro, Ivan Ivanov, Eduardo Hirata-Miyasaki, See-Chi Lee, Aofei Liu, Sricharan Reddy Varra, Talon Chandler, Soorya Pradeep, Chad Liu, Manuel D. Leonetti, Carolina Arias, Bo Huang, Shalin B. Mehta
- **arXiv:** `2611.02324v1` (published 2026-11-02 00:16:20 UTC; categories: `cs.CV` (primary), `q-bio.QM`)
- **Evidence for ranking:** Cross-listed in quantitative biology; an arXiv comment records acceptance to the NeurIPS 2026 Evaluations and Datasets Track; the benchmark spans three cell types, two microscopes, four organelles, and three perturbation states.
- **Claimed contribution:** The authors find regression baselines better localize organelles while a generative baseline better captures phenotype distributions, showing that one metric can hide different model strengths.
- **Caveat:** Benchmark results do not validate virtual staining as a replacement for fluorescence in biological experiments; the tested cell types and imaging settings are limited.
- **Announcement type:** new submission, cross-listed into q-bio.QM in the 2026-11-03 batch
- **Themes:** Molecular & cell biology; Quantitative methods

### 10. [Attribution-based diagnostics for single-cell foundation models](https://arxiv.org/abs/2611.02335)
- **Abstract:** The authors use post-hoc attribution to inspect whether single-cell RNA foundation models rely on biologically meaningful features across cell-annotation and perturbation-prediction tasks.
- **Authors:** Farnoush Rezaei Jafari, Tristan Lazard, Kenza Bouzid, Shruthi Bannur, Jeremiah Wander, Ashley Mae Conard, Stephanie Hyland, Lorin Crawford, Daniel Coelho de Castro
- **arXiv:** `2611.02335v1` (published 2026-11-02 00:32:31 UTC; categories: `cs.LG` (primary), `q-bio.QM`)
- **Evidence for ranking:** Direct single-cell RNA focus and q-bio.QM cross-list; tests Cell2Sentence and scGPT annotation and scGPT+STATE perturbation prediction, including a synthetic regulatory-ground-truth setting.
- **Claimed contribution:** The authors report that attribution can expose feature use and model behavior missed by predictive metrics alone, while showing that interpretation depends on the selected reference, baseline, and null model.
- **Caveat:** The perturbation analysis uses a controlled synthetic setting; attribution patterns are not themselves proof of causal gene regulation.
- **Announcement type:** new submission, cross-listed into q-bio.QM in the 2026-11-03 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Bioinformatics & sequence analysis

### 11. [In-depth data movement characterization of DNA read mapping algorithms](https://arxiv.org/abs/2611.03400)
- **Abstract:** The authors profile read-mapping implementations across sequencing technologies to identify memory bottlenecks and opportunities for hardware optimization.
- **Authors:** Berkan Şahin, Ecem İlgün, Klea Zambaku, Can Alkan
- **arXiv:** `2611.03400v1` (published 2026-11-02 16:31:32 UTC; categories: `cs.AR` (primary), `q-bio.GN`)
- **Evidence for ranking:** Cross-listed in genomics; compares named short-read, long-read, and whole-genome alignment tools using VTune and a data-movement simulator.
- **Claimed contribution:** The authors report Minimap2 fastest for long-read scenarios but weaker on whole-genome alignment due to multithreading, and identify memory-bound tools whose cache use could be improved.
- **Caveat:** Results depend on the selected workloads, tools, and hardware; simulated processing-in-memory gains are not a deployment demonstration.
- **Announcement type:** new submission, cross-listed into q-bio.GN in the 2026-11-03 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 12. [Findings-aware Language-Image Pretraining for CT Volume Interpretation](https://arxiv.org/abs/2611.02327)
- **Abstract:** FiLIP uses report-derived abnormal-finding phrases to supervise CT-volume representations and evaluates zero-shot finding classification and radiology-report generation.
- **Authors:** Takuro Shimaya, Junya Inoh, Masahiro Saiko
- **arXiv:** `2611.02327v1` (published 2026-11-02 00:21:07 UTC; categories: `cs.CV` (primary), `physics.med-ph`)
- **Evidence for ranking:** Direct medical-imaging focus; an arXiv comment records acceptance to WACV 2027; the abstract reports in-domain and external-domain evaluations.
- **Claimed contribution:** The authors report improved multi-label zero-shot finding classification over weakly supervised approaches and utility after fine-tuning for report generation.
- **Caveat:** The abstract does not state cohort sizes or external-site details; classification and report-generation benchmarks do not establish clinical benefit.
- **Announcement type:** new submission, cross-listed into physics.med-ph in the 2026-11-03 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 13. [A Scientific Claim Stability Framework for Evaluating MRI Morphometry Pipelines](https://arxiv.org/abs/2611.02413)
- **Abstract:** Scientific Claim Stability converts MRI morphometry tables into auditable claims and tests whether those claims persist across datasets, cohorts, pipelines, atlases, and covariate choices.
- **Authors:** Duy-Cat Can, Dang-Duat Tran, Anh-Khang Nguyen, Quoc-Bao Tran, Trung-Hieu Do, Van-Tu Nguyen, Duy-Thanh Vu, Oliver Y. Chén, Hoang-Quynh Le
- **arXiv:** `2611.02413v1` (published 2026-11-02 02:35:45 UTC; categories: `cs.LG` (primary), `q-bio.QM`, `stat.ME`)
- **Evidence for ranking:** Cross-listed in quantitative biology; an arXiv comment records acceptance at NeurIPS 2026 (Evaluations and Datasets Track); evaluates 10,370 MRI scans from three datasets and five cohorts.
- **Claimed contribution:** The authors report 2,783 claim cards and 89 claim-family comparisons, finding that evidence concordance and anatomical-support overlap can diverge across FreeSurfer and FastSurfer analyses.
- **Caveat:** Pipeline disagreement is an audit of evidential stability, not proof that one pipeline is clinically correct or that the findings predict patient outcomes.
- **Announcement type:** new submission, cross-listed into q-bio.QM in the 2026-11-03 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

## Trending Research Themes

- **Molecular search and developability:** RangeFinder predicts pocket-compatible property ranges; PeptSol benchmarks protected-peptide solubility; the sequence-generation paper compares landscape search; and the antibody-agent paper studies in-silico optimization. These are complementary computational approaches, not a validated end-to-end drug-discovery pipeline.
- **Single-cell and multimodal inference:** ManifoldVelo couples RNA kinetics to cell trajectories, HistoTx combines histology with spatial transcriptomics, DynaCell evaluates dynamic virtual staining, and the attribution paper probes how single-cell foundation models make predictions. Their different tasks and datasets make their metrics non-interchangeable.
- **Evaluation and evidence quality:** V2G tests whether reranking uses retrieved evidence; the Tahoe-100M paper challenges the experimental unit in pooled screens; and Scientific Claim Stability asks whether MRI conclusions persist across analysis choices. All emphasize that benchmark accuracy alone can conceal fragile evidence.
- **Genomic and biomedical computation:** DNA mapper profiling identifies hardware bottlenecks, while FiLIP evaluates report-guided CT representation learning. Both are computational evaluations, not evidence of improved patient outcomes.

## Open Problems and Research Directions

- **Prospective molecular validation:** RangeFinder, PeptSol, sequence generation, and antibody design all leave a gap between prediction and practical function. A blinded follow-up could freeze model predictions, synthesize or select matched candidates, measure binding/activity or peptide solubility and process recovery, and compare against baseline-selected molecules. For PeptSol, independent programmes and broader protected scaffolds would address the source concentration noted by the authors.
- **Separate evidence use from memorized association:** V2G's controls suggest that reranking gains may reflect known-gene recall rather than the retrieved evidence. Test on loci with independently generated functional assays and minimal reference overlap, with evidence ablation and provenance-preserving controls.
- **Validate inferred cell dynamics and multimodal transfer:** ManifoldVelo could be tested on independent, densely sampled perturbation time courses with held-out donors or plates. HistoTx needs external-institution and assay/platform evaluation, while DynaCell's virtual stains should be tested on new cell types and microscopes with prespecified temporal and phenotype endpoints before use as a fluorescence substitute.
- **Check generality of evaluation warnings:** Replicate the Tahoe-100M well-level dependence analysis in independent pooled screens, and compare MRI claim stability across additional acquisition protocols and prespecified covariate sets. These studies would establish how broadly the reported evaluation risks apply.

## Takeaway

This batch is most notable for molecular-design benchmarks, RNA and spatial-omics methods, and work that audits how biomedical AI evidence is generated. Workshop or conference acceptance and broad benchmark coverage are checkable signals of relevance, not popularity or biological validity. Prospective experiments, independent datasets, and external validation remain the key gaps; no clinical recommendation follows from these preprints.

## Method and sources

- **Window:** daily batch dated 2026-11-03 (announcement date, UTC); range 2026-11-03 through 2026-11-03. Snapshot: 2026-11-04 01:17:47 UTC. The latest visible arXiv batch is the prior announcement batch for Tuesday, 3 November; the 4 November batch was not yet listed at snapshot time.
- **Candidate pool:** traversed the daily listings for `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph`: 74 category entries and 71 unique arXiv IDs after deduplicating cross-lists. The configured `cs.BI` API query returned no records, and its category listing page did not resolve. Replacements and cross-listings were checked; 13 papers were selected for relevance to molecular biology, genomics, cell methods, or biomedical research.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`.
- **Ranking:** arXiv has no official trending chart. Because no robust attention or citation-momentum signal was established for this newly announced batch, the report is titled “Notable recent papers” and ordered by direct relevance and specificity of reported evidence, with cross-listing and checkable workshop/conference metadata as secondary signals. Citation totals are not treated as gains during the batch.
- **Verification:** all 13 selected abstract pages and arXiv metadata were checked. Full HTML texts for RangeFinder, PeptSol, Automatic Generation of Novel Highly-Functional Molecular Sequences, ManifoldVelo, and HistoTx were reviewed for methods, results, and limitations. Claims are attributed; computational prediction, simulation, mathematical inference, cohort analysis, and experimental validation are distinguished.
- **Sources:** arXiv abstract pages are linked in each entry. Full text reviewed for [RangeFinder](https://arxiv.org/html/2611.03379v1), [PeptSol](https://arxiv.org/html/2611.00749v1), [Automatic Generation of Novel Highly-Functional Molecular Sequences](https://arxiv.org/html/2611.03603v1), [ManifoldVelo](https://arxiv.org/html/2611.03056v1), and [HistoTx](https://arxiv.org/html/2611.02681v1). Daily listing pages: [q-bio.BM](https://arxiv.org/list/q-bio.BM/new), [q-bio.GN](https://arxiv.org/list/q-bio.GN/new), [q-bio.MN](https://arxiv.org/list/q-bio.MN/new), [q-bio.SC](https://arxiv.org/list/q-bio.SC/new), [q-bio.CB](https://arxiv.org/list/q-bio.CB/new), [q-bio.TO](https://arxiv.org/list/q-bio.TO/new), [q-bio.QM](https://arxiv.org/list/q-bio.QM/new), [physics.med-ph](https://arxiv.org/list/physics.med-ph/new). The explicit configured-category query was `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`.
