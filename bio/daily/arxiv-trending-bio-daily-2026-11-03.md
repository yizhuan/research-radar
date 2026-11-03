# Notable recent papers: biology and biomedicine arXiv — 2026-11-03

The latest daily announcement batch contains 12 selected papers from 48 unique candidates across the configured, accessible biology/biomedicine listings. The strongest patterns are peptide/protein property prediction, cancer and variant genomics, and methods for single-cell or multimodal biological data. Spoken agenda: what the papers report, how strong their evidence is, and what remains untested. arXiv has no official trending chart; attention evidence for this just-announced batch is sparse, so this is an inferred relevance ranking rather than a popularity ranking. arXiv coverage is incomplete: much experimental and clinical preprint research appears on bioRxiv or medRxiv.

## Notable recent papers (ranked)

### 1. [PeptSol: A Translational Benchmark for Protected-Peptide Solubility in Drug Manufacturing](https://arxiv.org/abs/2611.00749)
- **Abstract:** PeptSol benchmarks prediction of protected-peptide solubility relevant to liquid-phase peptide synthesis, using 1,388 curated measurements and chemistry-aware train/test splits.
- **Authors:** Alexander Arjun Lobo, Marc Saouda, Urvi Awasthi, Leonid Zhukov
- **arXiv:** `2611.00749v1` (published 2026-10-31 08:56:07 UTC; categories: `cs.LG`, `physics.chem-ph`, `q-bio.BM`)
- **Evidence for ranking:** Direct peptide-manufacturing relevance; arXiv says accepted at the NeurIPS 2026 AI for Drug Discovery workshop; compares seven molecular encoders on a source-curated benchmark.
- **Claimed contribution:** The authors report a best macro-F1 of 0.843 for binary solubility in the historical subset, but no foundation model consistently beats a fingerprint-plus-descriptor baseline across tasks and splits.
- **Caveat:** The 1,388 records cover 84 parent sequences and 101 protected structures, with 92.5% from one historical programme. Retrospective solubility prediction does not establish coupling yield, recovery, or process performance.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [Evolutionary characterization of whole-genome doubling across human cancers](https://arxiv.org/abs/2611.01897)
- **Abstract:** The authors integrate genomic, evolutionary-timing, and multi-omic analyses to characterize whole-genome doubling across 41,332 tumours from 12 cancer types.
- **Authors:** Yangyang Zhang, Haiming Li, Xiaoyu Zhao, Zilong Wang, Yongqi Chen, Sumeng Yang, Shaocong Mo, Jinming Li, Xiaohua Wu, Xu Wang, Shuo Wang, Qinhao Guo
- **arXiv:** `2611.01897v1` (published 2026-11-01 13:39:58 UTC; categories: `q-bio.GN`, `q-bio.PE`)
- **Evidence for ranking:** Large multi-cancer genomic analysis with explicit timing and multi-omic evidence; directly in genomics and population/evolution categories.
- **Claimed contribution:** The authors report that driver mutations often precede WGD and that post-WGD chromosome-arm losses are less cancer-type-dependent; WGD-positive tumours also show reduced interferon and HLA-presentation programmes linked to epigenetic remodelling.
- **Caveat:** These are analyses of tumour datasets and associations, not intervention-based proof that WGD causes the reported immune changes or clinical outcomes.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Biomedical & translational medicine

### 3. [RangeFinder: Predicting Ligand Property Ranges from Protein Pockets](https://arxiv.org/abs/2611.03379)
- **Abstract:** RangeFinder predicts ranges for nine ligand physicochemical properties from protein-pocket structure, chemistry, and evolutionary context to help narrow molecular search.
- **Authors:** Alan Nadelsticher Ruvalcaba, Chris Alvin, Supratik Mukhopadhyay, Adam Bess
- **arXiv:** `2611.03379v1` (published 2026-11-02 16:21:09 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Direct protein–ligand relevance and q-bio.BM cross-list; arXiv says accepted at the NeurIPS 2026 AI for Drug Discovery workshop; BioLiP2 evaluation reports range-IoU 0.464 ± 0.002 and Reduction-Recall F-score 0.543 ± 0.011 against deployable baselines.
- **Claimed contribution:** The authors propose pocket-level property-range prediction as a complement to proposing or scoring individual ligands and report 12.2 ms inference per pocket.
- **Caveat:** Evaluation is limited to pockets with at least three known ligands; the authors note possible homology overlap across UniProt-based splits. Prospective ligand discovery or binding has not been demonstrated.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 4. [An auditable agentic pipeline for variant-to-gene prioritisation, validated against orthogonal functional evidence](https://arxiv.org/abs/2611.01461)
- **Abstract:** V2G records evidence retrieval and ranks candidate genes for GWAS loci; the authors test whether a language model's reranking gains actually depend on the retrieved evidence.
- **Authors:** Shakuntala Baichoo, Sohail (Neel) Sarkar, Bo Wang
- **arXiv:** `2611.01461v1` (published 2026-11-01 02:48:40 UTC; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Direct variant-to-gene genomics task; frozen benchmark and reproduction code are reported; the abstract quantifies results on held-out loci and explicitly tests evidence-row shuffling and known-gene recall.
- **Claimed contribution:** On 135 loci with successful retrieval, model reranking improves Precision@1 over the evidence ordering, but the authors find no detected difference from Open Targets L2G or training-membership baselines; their controls indicate the gain reflects recall of known genes more than use of the presented evidence.
- **Caveat:** The paper reports train/test overlap and retrieval-conditioned subsets; the results caution against treating an auditable evidence trail as proof that an agent reasoned from that evidence.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Biomedical & translational medicine

### 5. [Coupling cellular trajectories and RNA kinetics on continuous expression manifolds with ManifoldVelo](https://arxiv.org/abs/2611.03056)
- **Abstract:** ManifoldVelo jointly fits pseudotime, continuous spliced/unspliced RNA trajectories, and kinetic dynamics, with tests on simulated cyclic and branching processes and real single-cell datasets.
- **Authors:** Zhen Zhou, Jiachen Li, Yuan Liu, Xiaoyong Pan, Hong-Bin Shen
- **arXiv:** `2611.03056v1` (published 2026-11-02 12:49:50 UTC; categories: `q-bio.QM`)
- **Evidence for ranking:** Direct RNA/transcriptomics relevance; comparisons span cyclic and branching simulations plus real-data analyses; arXiv comment links code and numerical source tables.
- **Claimed contribution:** The authors report improved pseudotime and velocity comparisons on selected benchmarks and transfer of temporal and velocity predictions to new cells using spliced RNA with a fixed reference.
- **Caveat:** Inferred pseudotime and RNA velocity are computational estimates; agreement with marker or stage patterns is not direct time-resolved validation of every cell's trajectory.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 6. [Automatic Generation of Novel Highly-Functional Molecular Sequences](https://arxiv.org/abs/2611.03603)
- **Abstract:** The authors compare sequence-generation strategies on two complete fitness landscapes and report that a training-free information-theoretic method finds rare high-fitness sequences more effectively than the tested variational autoencoders.
- **Authors:** Vincent R. Ragusa, Chrisoph Adami
- **arXiv:** `2611.03603v1` (published 2026-11-02 18:41:20 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct biomolecular sequence-design fit; tests against two complete landscapes, including an experimentally assayed DHFR landscape; first-listed in the focused biomolecules category.
- **Claimed contribution:** The authors claim a faster, training-free information-theoretic search can outperform tested ML/AI generation methods at finding rare high-fitness sequences; antimicrobial peptide selectivity is discussed as an application, not demonstrated as a wet-lab result here.
- **Caveat:** The second landscape is digital life, and the paper does not report synthesis or antimicrobial/cytotoxicity assays of generated peptides.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Biochemistry & proteins; DNA & genomics; Quantitative methods

### 7. [The DynaCell Evaluation Suite for Dynamic 3D Virtual Staining of Live Cells](https://arxiv.org/abs/2611.02324)
- **Abstract:** DynaCell provides paired 3D live-cell imaging data, baseline virtual-staining models, and multi-level metrics to compare image fidelity, organelle segmentation, and cell-phenotype similarity over time.
- **Authors:** Alexandr A. Kalinin, Dihan Zheng, Taylla Milena Theodoro, Ivan Ivanov, Eduardo Hirata-Miyasaki, See-Chi Lee, Aofei Liu, Sricharan Reddy Varra, Talon Chandler, Soorya Pradeep, Chad Liu, Manuel D. Leonetti, Carolina Arias, Bo Huang, Shalin B. Mehta
- **arXiv:** `2611.02324v1` (published 2026-11-02 00:16:20 UTC; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Cross-listed in quantitative biology; arXiv says accepted to the NeurIPS 2026 Evaluations and Datasets Track; benchmark spans three cell types, two microscopes, four organelles, and three perturbation states, and releases data/code/checkpoints.
- **Claimed contribution:** The authors find regression baselines better localize organelles while a generative baseline better captures phenotype distributions, showing that one metric can hide different model strengths.
- **Caveat:** Benchmark results do not validate virtual staining as a replacement for fluorescence in biological experiments; temporal consistency and broader paired data remain important follow-up areas.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Molecular & cell biology; Biomedical & translational medicine; Quantitative methods

### 8. [HistoTx: Early fusion of H&E images and spatial transcriptomics at varying spatial transcriptomics resolution with self-supervised learning](https://arxiv.org/abs/2611.02681)
- **Abstract:** HistoTx fuses histology-image and spatial-transcriptomic tokens in a shared transformer and evaluates image-only and multimodal inference across gene-expression and pathology tasks.
- **Authors:** Alice Driessen, Emil Malmsten, Steffen Wolf, Bernd Illing, Isinsu Katircioglu, Adriano Martinelli, Rolf Stahel, Solange Peters, Enriqueta Felip, Sanjay Popat, Krisztian Homicsko, Raphael Gottardo, Marianna Rapsomaniki, Fei Tang
- **arXiv:** `2611.02681v1` (published 2026-11-02 07:36:09 UTC; categories: `cs.LG`, `cs.AI`, `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Cross-listed in genomics and quantitative biology; arXiv says presented at the ICML 2026 multimodal life-sciences workshop; evaluated on spatial-transcriptomics and pathology benchmarks.
- **Claimed contribution:** The authors report stronger gene-expression prediction than image-only baselines on several benchmarks and additional gains when transcript data are provided at inference.
- **Caveat:** The authors also report drops on some image-only cancer-subtype classification tasks; benchmark gains do not establish clinical utility or robust transfer to new institutions.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** DNA & genomics; RNA & transcriptomics; Omics & single-cell methods

### 9. [Can agents reliably design therapeutic antibodies?](https://arxiv.org/abs/2611.00558)
- **Abstract:** The authors evaluate agentic antibody design under instruction-following and black-box optimization settings, finding trade-offs among tool use, design history, exploration, and optimization.
- **Authors:** Asli Alpman, Nick Bhattacharya, Aaron Solomon, Hunter Elliott
- **arXiv:** `2611.00558v1` (published 2026-10-31 02:35:17 UTC; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** Direct antibody-design focus and q-bio.QM cross-list; tests ten expert-validated affinity-improvement tasks and compares its in-silico optimizer with Bayesian optimization.
- **Claimed contribution:** The authors report that tools improve instruction following and sequence exploration but reduce optimization performance, while design history improves optimization at the cost of exploration.
- **Caveat:** All reported optimization is in silico; the paper does not establish experimental binding affinity or therapeutic activity of newly designed antibodies.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 10. [Canonic hemoglobin-oxygen equilibrium: Reassessing the role of cooperativity](https://arxiv.org/abs/2611.00824)
- **Abstract:** The authors reformulate hemoglobin–oxygen equilibrium in a canonical model of the red-cell environment and predict lower cooperative interaction energies than grand-canonical treatments.
- **Authors:** A. E. Allahverdyan, S. G. Gevorkian, A. Harutyunyan, Y. Sh. Mamasakhlisov, V. Stepanyan
- **arXiv:** `2611.00824v1` (published 2026-10-31 11:09:28 UTC; categories: `physics.bio-ph`, `cond-mat.soft`, `cond-mat.stat-mech`, `q-bio.BM`)
- **Evidence for ranking:** Cross-listed in biomolecules and biological physics; arXiv lists a Journal of Chemical Physics reference and DOI; the paper directly revisits a classic biochemical binding model.
- **Claimed contribution:** The authors argue that a canonical red-cell model predicts smaller oxygen-binding fluctuations and that large cooperative energies can produce unstable oxygen release within that model.
- **Caveat:** This is a theoretical reformulation; the abstract does not report new red-cell experiments testing the predicted oxygen hopping or instability.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 11. [Attribution-based diagnostics for single-cell foundation models](https://arxiv.org/abs/2611.02335)
- **Abstract:** The authors use post-hoc attribution to inspect whether single-cell RNA foundation models rely on biologically meaningful features across cell annotation and perturbation-prediction tasks.
- **Authors:** Farnoush Rezaei Jafari, Tristan Lazard, Kenza Bouzid, Shruthi Bannur, Jeremiah Wander, Ashley Mae Conard, Stephanie Hyland, Lorin Crawford, Daniel Coelho de Castro
- **arXiv:** `2611.02335v1` (published 2026-11-02 00:32:31 UTC; categories: `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** Direct single-cell RNA focus and q-bio.QM cross-list; tests Cell2Sentence and scGPT annotation and scGPT+STATE perturbation prediction, including a synthetic regulatory-ground-truth setting.
- **Claimed contribution:** The authors report that attribution can expose feature use and model behavior missed by predictive metrics alone, while showing that interpretation depends on the chosen reference, baseline, and null model.
- **Caveat:** The perturbation analysis uses a controlled synthetic setting; attribution patterns are not themselves proof of causal gene regulation.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Bioinformatics & sequence analysis

### 12. [Findings-aware Language-Image Pretraining for CT Volume Interpretation](https://arxiv.org/abs/2611.02327)
- **Abstract:** FiLIP uses report-derived abnormal-finding phrases to supervise CT-volume representations and evaluates zero-shot finding classification and radiology report generation.
- **Authors:** Takuro Shimaya, Junya Inoh, Masahiro Saiko
- **arXiv:** `2611.02327v1` (published 2026-11-02 00:21:07 UTC; categories: `cs.CV`, `physics.med-ph`)
- **Evidence for ranking:** Direct medical-imaging focus; arXiv says accepted to WACV 2027; abstract reports in-domain and external-domain evaluations.
- **Claimed contribution:** The authors report improved multi-label zero-shot finding classification over weakly supervised approaches and utility after fine-tuning for report generation.
- **Caveat:** The abstract does not state cohort sizes or external-site details; classification and report-generation benchmark performance do not establish clinical benefit.
- **Announcement type:** new submission, 2026-11-03 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

## Trending Research Themes

- **Molecular developability and search:** PeptSol measures synthesis-relevant protected-peptide solubility, while RangeFinder predicts pocket-compatible ligand-property ranges. The molecular-sequence paper explores a different search problem on complete fitness landscapes. These are complementary computational directions, not evidence of a validated end-to-end discovery pipeline.
- **Genomic interpretation is being audited as well as automated:** The whole-genome-doubling analysis integrates large tumour datasets; V2G tests whether language-model reranking adds evidence-based value. Their evidence types differ—cohort-scale observational analysis versus a held-out computational benchmark—and should not be conflated.
- **Single-cell and multimodal evaluation:** ManifoldVelo models RNA dynamics; HistoTx fuses histology and spatial transcriptomics; DynaCell evaluates virtual stains; and the attribution paper probes model behavior. Across these papers, model utility depends on topology, input modalities, and task-specific metrics, rather than a single headline score.
- **Models versus biological validation:** Antibody design and sequence generation are computational; the hemoglobin paper is theoretical; none establishes new therapeutic function through experiments in this batch. The strongest direct empirical breadth comes from existing cohort and benchmark data, not prospective clinical evidence.

## Open Problems and Research Directions

- **Test whether predictions help peptide manufacturing:** PeptSol authors note that retrospective solubility does not directly measure synthesis yield, purification, or recovery. A prospective, blinded solvent-screen study across more scaffolds and independent programmes could compare model-guided and standard solvent selection on yield, purity, and recovery.
- **Separate model reasoning from known-gene recall:** V2G's controls suggest reranking gains may reflect known-gene recall rather than use of retrieved evidence. Evaluate on loci with independently generated functional assays and no training/reference overlap, with evidence ablation and provenance-preserving controls.
- **Validate molecular design outside retrospective or simulated settings:** RangeFinder, the sequence-generation comparison, and the antibody-agent study all stop short of prospective functional testing. Follow-up work could lock predictions before testing synthesized molecules, measure binding or activity and relevant off-target effects, and compare with matched baseline-selected designs.
- **Test inferred cell dynamics and virtual staining under distribution shift:** ManifoldVelo could be evaluated on independent, densely sampled perturbation time courses with held-out donors or plates. DynaCell's virtual stains could be tested on new microscopes and cell types with prespecified temporal, segmentation, and phenotype endpoints before use as a fluorescence substitute.

## Takeaway

This batch is notable for peptide and protein-design benchmarks, large-scale cancer genomics, and rigorous scrutiny of AI systems used for biological inference. Some papers have workshop or conference acceptance signals, but the batch is too new to support a measured popularity ranking. The key dividing line is validation: benchmark and cohort results can guide follow-up, but protein-design claims still need prospective experiments and clinical utility is not established here.

## Method and sources

- **Window:** daily, 2026-11-03 through 2026-11-03. Snapshot: 2026-11-03 17:10:39 UTC. The latest arXiv category listings showed the Tuesday 3 November announcement batch, so this report uses today's batch, not a prior batch.
- **Candidate pool:** traversed the recent listings for `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph`. The pages contained 49 category entries for the batch; after deduplicating the HistoTx cross-list, there were 48 unique candidates. `q-bio.CB` and `q-bio.TO` had no updates. The configured `cs.BI` listing returned an invalid-category response, so that category could not be independently checked. A broad API query was also paginated past the daily window. Twelve papers were selected for direct molecular, genomic, cellular, or biomedical relevance; the ecology-focused AI-FAIR entry was not included.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`.
- **Ranking:** “Notable recent papers” is used because arXiv has no official trending chart and meaningful citation momentum or independent attention evidence was not established for a just-announced batch. Ordering reflects direct relevance, specificity and breadth of reported evidence, cross-listing, and checkable acceptance or journal-reference metadata; no citation totals are treated as period gains.
- **Verification:** all 12 selected arXiv abstract pages and metadata were checked. The full HTML texts of PeptSol, RangeFinder, and ManifoldVelo were reviewed for methods, results, and limitations. Author claims are attributed, and computational prediction, mathematical modeling, cohort analyses, and experimental validation are distinguished.
- **Sources:** arXiv abstract pages are linked in every entry. Full text reviewed for ranks 1, 3, and 5: [PeptSol](https://arxiv.org/html/2611.00749v1), [RangeFinder](https://arxiv.org/html/2611.03379v1), [ManifoldVelo](https://arxiv.org/html/2611.03056v1). Recent-listing pages checked: [q-bio.BM](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), [medical physics](https://arxiv.org/list/physics.med-ph/recent).
