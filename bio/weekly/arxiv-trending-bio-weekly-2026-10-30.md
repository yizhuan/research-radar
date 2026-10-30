# arXiv Trending Biology and Biomedicine — Weekly (2026-10-23 to 2026-10-30)

## Headline

This week’s 15 notable arXiv biology and biomedical papers cluster around model validation in molecular design and perturbation screens, with additional work on proteomics, synthetic genomes, and transcriptomics. For a spoken overview: start with the shared-clone and escaping-cell biases in CRISPR screens, then compare protein-design and molecular-dynamics methods, and close with omics resources and validation limits. The latest announcement batch visible in the traversed category listings was 28 October 2026. arXiv has no official trending chart, and this inferred, relevance-ranked selection comes from an incomplete biomedical preprint corpus that excludes most bioRxiv, medRxiv, and published medical research.

## Notable recent papers (ranked by demonstrated relevance)

Attention evidence is sparse: Semantic Scholar’s current citation totals are 1 for three selected papers and 0 for the other twelve; none has an influential citation in that index. These totals do not measure gains during this week. Accordingly, the ordering below prioritizes direct relevance and the scale or validation type of the reported work, not measured readership or popularity.

### 1. [Shared clones make random cell halves look reproducible in pooled screens](https://arxiv.org/abs/2610.32962v2)
- **Abstract:** The authors show that clones shared between random cell halves can inflate apparent reproducibility and model benchmarks in pooled single-cell perturbation screens.
- **Authors:** Xuanrui Huang
- **arXiv:** `2610.32962v2` (first submitted 2026-10-23T17:53:14Z; revised 2026-10-26; categories: `q-bio.QM`)
- **Evidence for ranking:** Direct relevance to single-cell CRISPR benchmarking; the revision adds four-donor analyses. Semantic Scholar currently lists 1 citation and 0 influential citations.
- **Claimed contribution:** The preprint compares random halves with independent transductions and clone-separated partitions across 16 screens. In a genome-scale primary T-cell screen, null perturbations agreed almost always across random halves but only about half the time across independent replicates; clone-separated splits largely removed the excess agreement.
- **Caveat:** The authors say the direct clone-strength relation was tested in only one clone-recording screen, and the 16 datasets differ in cell type, perturbation, and sequencing. The results concern benchmark reliability, not a reanalysis overturning the original biological findings.
- **Announcement type:** revision, 2026-10-26
- **Themes:** Omics & single-cell methods; Quantitative methods; Molecular & cell biology

### 2. [Agent-guided epitope excision enables economical de novo binder design](https://arxiv.org/abs/2610.33195v1)
- **Abstract:** The authors test whether cropping target proteins around a binder interface can reduce design compute while retaining interface geometry, then evaluate different levels of agent autonomy on FAP.
- **Authors:** Jun W. Kim, Artiom Myaskovsky, Oscar Donosa, Lawrence Chan, Jamie Rogers, Avinatan Hassidim, Yossi Matias, Annalisa Pawlosky
- **arXiv:** `2610.33195v1` (first submitted 2026-10-23T18:42:14Z; categories: `q-bio.BM`)
- **Evidence for ranking:** A 15-target, 3,666-design benchmark plus yeast-display validation; Semantic Scholar currently lists 0 citations and 0 influential citations. Google Research also posted an institutional technical account, not independent confirmation.
- **Claimed contribution:** The preprint reports a median interface RMSD of 0.37 Å for excised windows and up to about 88% lower GPU time in one FAP epitope. In a fixed-budget comparison, the human-in-the-loop arm raised the computational hit rate from 5.06% to 9.33%; yeast display detected nanomolar binders among designs from agent-driven arms.
- **Caveat:** Most claims are computational; yeast-display enrichment is not evidence of therapeutic efficacy or in-vivo performance. The paper also reports that omitting target MSAs can change apparent yield and that agent choices were tested on one main target campaign.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 3. [AI-guided deep visual proteomics reveals recurrence-associated morpho-molecular signatures within triple-negative breast cancers](https://arxiv.org/abs/2608.03145v3)
- **Abstract:** The authors use recurrence-risk maps from pathology images to guide spatial proteomic sampling and report tumor-region protein signatures associated with recurrence in triple-negative breast cancer.
- **Authors:** Yesung Cho, Ji Hwan Park, Chan Il Kim, Hyewon Kim, Honglan Li, Yumin Lee, Geongyu Lee, Sujeong Hong, Seong Min Park, Yoonyoung Lee, Hee Sool Rho, Sumin Lee, Amos Chungwon Lee, Changhwan Lee, Hwanyoung Shim, Hyunwook Kim, Hyeji Shin, Sanha Park, Jihoon Yu, Yoon Hee Shin, Sooheon Kim, Hyunjin Park, Seung Min Park, Sangwan Kim, Yujung Kim, Jinwon Jeong, Sung-Im Do, Eun-Young Kim, Dongmyung Shin, Ingu Do, Jongbae Park
- **arXiv:** `2608.03145v3` (first submitted 2026-08-04T05:19:35Z; revised 2026-10-27; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Human tumor material, mass-spectrometry profiling, and an expanded TNBC cohort; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** In 156 patients, the authors report high- and low-risk regions within tumors; they profiled 46 AI-selected regions from two recurrent cases, formed a 13-protein composite, and report improved out-of-bag discrimination when combined with an H&E-derived score (C-index 0.679 to 0.739; five-year AUC 0.675 to 0.770). A transcript score showed a similar trend in METABRIC.
- **Caveat:** Deep spatial profiling covered only 46 regions from two recurrent cases. The retrospective association and out-of-bag metrics do not establish prospective clinical utility; the expanded-cohort size is not stated in the abstract.
- **Announcement type:** revision, 2026-10-27
- **Themes:** Omics & single-cell methods; Biomedical & translational medicine; Molecular & cell biology

### 4. [A unified coarse-grained neural network potential for the dynamics of biomolecular complexes](https://arxiv.org/abs/2610.37606v1)
- **Abstract:** AMARO v2.0 is a heavy-atom coarse-grained neural potential for protein, ligand, and multi-component complex dynamics, assessed on complex retention and selected binding case studies.
- **Authors:** Antonio Mirarchi, Stephen E. Farr, Adrià Peréz, Gianni De Fabritiis
- **arXiv:** `2610.37606v1` (first submitted 2026-10-27T17:37:10Z; categories: `q-bio.BM`)
- **Evidence for ranking:** Evaluated across 262 complexes and 11 targets, with explicit comparison to all-atom mechanics in case studies; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** The preprint reports pose retention across most complexes and 3.3-fold more trajectories reaching the trypsin–benzamidine crystal pose than all-atom molecular mechanics at a fixed estimated GPU-time budget. It also reports recovery of a reference pose in TYK2.
- **Caveat:** These are simulation results, not experimental binding assays. The authors report more favorable-than-experimental free-energy estimates and limitations in SHP2 pose recovery, CDK8 site specificity, and HIF2A complex orientation.
- **Announcement type:** new submission, 2026-10-27
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [Accurate structural modelling of protein-glycan recognition with GlycoWeave](https://arxiv.org/abs/2610.37410v1)
- **Abstract:** GlycoWeave uses chemically constrained diffusion and multi-source training to predict protein–glycan complex structures.
- **Authors:** Huifeng Zhao, Jintu Zhang, Yifei Xiao, Youqiao Qian, Silong Zhai, Zichang Jin, Li Wang, Yuchao Wang, Hang Dong, Yifan Zhao, Zhenxing Wu, Hongyan Du, Yuansheng Huang, Bowei Zhao, Xiaorui Wang, Shukai Gu, Jike Wang, Zhongjun Li, Zhongtang Li, Tingjun Hou, Yu Kang
- **arXiv:** `2610.37410v1` (first submitted 2026-10-27T15:27:09Z; categories: `q-bio.BM`)
- **Evidence for ranking:** A 698-complex benchmark and explicit AlphaFold 3 comparison; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** The authors report a 71.9% Top-25 high-quality success rate versus 19.2% for AlphaFold 3, with a mean sampling time of 0.34 seconds per pose, while evaluating stereochemistry and interaction recovery.
- **Caveat:** The reported evidence is benchmark-based structural prediction, not prospective biochemical binding validation. The benchmark’s performance does not establish accuracy for all glycan classes or experimental settings.
- **Announcement type:** new submission, 2026-10-27
- **Themes:** Biochemistry & proteins; Quantitative methods

### 6. [HELICS: Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching](https://arxiv.org/abs/2610.36361v1)
- **Abstract:** HELICS generates conditional synthetic common-variant genomes from biobank-scale genotype data using chromosome compression and latent flow matching.
- **Authors:** Ahmad Abdel-Azim, Xihong Lin
- **arXiv:** `2610.36361v1` (first submitted 2026-10-26T22:25:36Z; categories: `q-bio.GN`, `cs.LG`)
- **Evidence for ranking:** Trained on more than 417,000 UK Biobank genomes and evaluated against external genotype data; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** The preprint reports stronger allele-frequency agreement and preservation of local and long-range SNP correlations than the compared haplotype-based simulators. Conditional generation follows ancestry and genetic-liability summaries; dosage shifts correlate with published association weights in perturbation analyses.
- **Caveat:** Fidelity and association-weight correlation do not establish privacy protection, especially against membership inference. The authors focus on common variants; rare variants and performance in underrepresented populations need separate evaluation.
- **Announcement type:** new submission, 2026-10-26
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 7. [Escaping cells dilute CRISPR screen responses unequally across cell types](https://arxiv.org/abs/2610.35508v1)
- **Abstract:** The authors estimate how cells with ineffective knockdown dilute pooled single-cell CRISPR responses and alter cross-cell-type comparisons and model benchmarks.
- **Authors:** Xuanrui Huang
- **arXiv:** `2610.35508v1` (first submitted 2026-10-26T14:33:48Z; categories: `q-bio.QM`)
- **Evidence for ranking:** The paper analyzes published screens across 13 cell types and tests a knockdown-escape estimator against simulated mixtures and independent replicate measurements; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** The preprint reports that escape fractions rise with gene essentiality in most examined cell types, reaching about half of measured cells for the most essential perturbations in human embryonic stem cells. The estimated fraction predicts dilution of response size and affects cell-type transfer coefficients and benchmark scores.
- **Caveat:** The estimator is based on target-transcript counts, not an independent protein-level knockdown measurement. Only seven cell types had enough cells for the core per-perturbation estimate, and screen timing and protocols vary.
- **Announcement type:** new submission, 2026-10-26
- **Themes:** Omics & single-cell methods; Molecular & cell biology; Quantitative methods

### 8. [MechGate: combining mechanism-derived measures of permeation and efflux to screen small molecule drugs targeting Escherichia coli](https://arxiv.org/abs/2610.33809v1)
- **Abstract:** MechGate reports separate mechanism-based measures for E. coli molecule permeation, efflux, and whole-cell activity rather than one composite score.
- **Authors:** Lang Qin, Jagath C Rajapakse
- **arXiv:** `2610.33809v1` (first submitted 2026-10-24T17:14:30Z; categories: `q-bio.BM`)
- **Evidence for ranking:** Includes an external set of marketed antibacterials and identifies source-library separability as a confound; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** The authors report precision of 0.789–0.873 for individual measures against baselines near 0.44, and 0.92 when combined according to the proposed mechanism. The tool returns five diagnostic measures without ranking molecules.
- **Caveat:** This is computational screening against curated endpoints, not a wet-lab antibiotic discovery or permeability experiment. The authors note that public source libraries can be separated by physicochemical features, which complicates validation.
- **Announcement type:** new submission, 2026-10-24
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Bioinformatics & sequence analysis

### 9. [Benchmarking miRNA Target Prediction Methods](https://arxiv.org/abs/2610.33960v1)
- **Abstract:** The authors benchmark seven miRNA–mRNA target tools against an evidence-graded reference built from curated interactions and paired expression data.
- **Authors:** Congliang Jin, Weibo Niu, Zhexing Wen, Zhaohui S Qin, Ximing Ran
- **arXiv:** `2610.33960v1` (first submitted 2026-10-25T00:23:22Z; categories: `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Compares seven methods across approximately 59.7 million candidate pairs and an iPSC cohort of 22q11.2 deletion syndrome and control lines; Semantic Scholar currently lists 0 citations and 0 influential citations. The arXiv comment reports acceptance for BIBM 2026.
- **Claimed contribution:** The preprint finds no tool is optimal across error control, power, and false-discovery proportion: TargetScan has the lowest FDP, while mirDIP is more sensitive but has the highest Type I error. The authors recommend selecting tools and cutoffs according to the application’s error trade-off.
- **Caveat:** Its evidence-graded reference is not a definitive ground truth, and expression-derived support does not prove direct molecular binding. The paired iPSC cohort is one biological context.
- **Announcement type:** new submission, 2026-10-25
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Quantitative methods

### 10. [Enhancing Clinical Classifier Robustness with Deep Representation Learning Based OOD Detection on DNA Methylation Data](https://arxiv.org/abs/2610.36344v1)
- **Abstract:** The authors evaluate out-of-distribution detection for methylation-array tumor classifiers using learned representations and spectral discrepancy.
- **Authors:** Md Zahangir Alom, Quynh T. Tran, Breuer Alexandar, Brent A. Orr
- **arXiv:** `2610.36344v1` (first submitted 2026-10-26T22:11:07Z; categories: `q-bio.GN`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Evaluated on public sarcoma and brain-tumor cohorts, holdouts, and an independent clinical dataset; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** The authors report that 1D-SSA was their strongest tested OOD method, with AUROC 0.975 in one sarcoma-in-distribution/brain-tumor-out setting and mean AUROC 0.976 on the independent clinical test set.
- **Caveat:** The abstract does not state the independent test-set sample size. This is retrospective model evaluation, not prospective evidence that OOD detection improves clinical decisions or patient outcomes.
- **Announcement type:** new submission, 2026-10-26
- **Themes:** Gene regulation & epigenetics; Bioinformatics & sequence analysis; Biomedical & translational medicine

### 11. [Probe Before You Edit: Probing-Guided Molecular Optimization for LLM Agents in Structure-Based Drug Design](https://arxiv.org/abs/2606.00555v3)
- **Abstract:** PROBE uses controlled ligand edits to estimate pocket-specific responses before guiding iterative molecular optimization by language-model agents.
- **Authors:** Zaifei Yang, Weiyu Chen, Yaqing Wang, James Kwok
- **arXiv:** `2606.00555v3` (first submitted 2026-05-30T06:06:51Z; revised 2026-10-23; categories: `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** A substantive revision within the window and evaluation on CrossDocked2020; Semantic Scholar currently lists 1 citation and 0 influential citations. The arXiv comment says accepted at NeurIPS 2026.
- **Claimed contribution:** The preprint proposes site maps and an edit-response manual to help an agent navigate affinity–druggability trade-offs, and reports state-of-the-art performance on its benchmark plus improved results on its diagnostic metrics.
- **Caveat:** Evidence is benchmark and computational optimization, not measured binding affinity, pharmacokinetics, safety, or efficacy. Results may depend on the benchmark’s docking and scoring assumptions.
- **Announcement type:** revision, 2026-10-23
- **Themes:** Biochemistry & proteins; Quantitative methods

### 12. [pyTransRate: reference-free quality assessment of de novo transcriptome assemblies with current aligners and quantifiers](https://arxiv.org/abs/2610.37031v2)
- **Abstract:** pyTransRate modernizes a reference-free transcriptome-assembly quality tool and compares its measurements with the original TransRate implementation.
- **Authors:** Matthew MacManes
- **arXiv:** `2610.37031v2` (first submitted 2026-10-27T11:08:52Z; revised 2026-10-28; categories: `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** The paper benchmarks 129 public assemblies in 5,031 paired comparisons; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** The author reports exact reproduction of sequence metrics and read counts, with strong rank agreement for assembly score (Spearman ρ=0.94) and good-mapping rate (ρ=0.98) against TransRate 1.0.3.
- **Caveat:** Read-based scores are not numerically interchangeable with the original, despite rank consistency. The study evaluates reimplementation agreement, not a biological gold standard for assembly completeness.
- **Announcement type:** revision, 2026-10-28
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Quantitative methods

### 13. [mdRNAcat: A Molecular Dynamics RNA Catalog of REST2 Conformational Ensembles](https://arxiv.org/abs/2610.35204v2)
- **Abstract:** mdRNAcat releases standardized force-labelled all-atom REST2 trajectories for 48 diverse RNA systems as a resource for data-driven RNA modelling.
- **Authors:** Anton E. Dorn, Emile de Bruyn, Fabrice von der Lehr, Philipp Knechtges, Stefan Kesselheim, Alexander Schug
- **arXiv:** `2610.35204v2` (first submitted 2026-10-26T10:56:24Z; revised 2026-10-27; categories: `q-bio.BM`, `cs.LG`, `physics.bio-ph`)
- **Evidence for ranking:** Cross-listed in biology, machine learning, and biophysics; offers 32-state simulations of 48 RNA systems; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** The authors provide coordinates, instantaneous and reference-Hamiltonian forces, structural annotations, and replica-exchange metadata, with 200–300 ns production per state, to support training and evaluating RNA models.
- **Caveat:** This is a simulation dataset; coverage and conformational populations depend on force-field and sampling choices and are not equivalent to experimentally measured ensembles. The 48 systems do not represent all RNA classes.
- **Announcement type:** revision, 2026-10-27
- **Themes:** RNA & transcriptomics; Biochemistry & proteins; Quantitative methods

### 14. [OmicsLM: A Multimodal Large Language Model for Multi-Sample Omics Reasoning](https://arxiv.org/abs/2605.06728v2)
- **Abstract:** OmicsLM combines continuous transcriptome embeddings with language prompts to support multi-sample omics reasoning and prediction tasks.
- **Authors:** Maciej Sypetkowski, Łukasz Smoliński, Remigiusz Kinas, Joanna Krawczyk, Bartłomiej Hofman, Aleksandra Możwiłło, Michał Pikusa, Tomasz Jetka, Rafał Powalski
- **arXiv:** `2605.06728v2` (first submitted 2026-05-07T11:27:11Z; revised 2026-10-25; categories: `q-bio.GN`, `cs.AI`, `q-bio.CB`)
- **Evidence for ranking:** The revision reports a publication-disjoint benchmark of 3,000 GEO-based questions and multiple held-out tasks; Semantic Scholar currently lists 1 citation and 0 influential citations.
- **Claimed contribution:** The authors report that a 9B model trained with continuous omics representations leads the compared systems on three of four held-out annotation tasks, six GEO-OmicsQA variants, and the average PerturbQA result.
- **Caveat:** These are model benchmark results, not experimental validation of inferred biology. The training corpus includes LLM-generated supervision, so evaluation leakage, task coverage, and answer grounding remain relevant checks.
- **Announcement type:** revision, 2026-10-25
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Bioinformatics & sequence analysis

### 15. [Label-free cell counting and viability prediction with brightfield imaging and deep learning](https://arxiv.org/abs/2610.10473v2)
- **Abstract:** ViabiLens predicts cell counts and live/dead status from brightfield images, including unstained samples, using models trained on stained-cell images.
- **Authors:** Amir Reza Vazifeh, Christian Zeigler, Sornanathan Meyyappan, Richard Jeske, Jason W. Fleischer
- **arXiv:** `2610.10473v2` (first submitted 2026-10-07T17:34:54Z; revised 2026-10-27; categories: `cs.CV`, `q-bio.CB`)
- **Evidence for ranking:** Reports comparison with fluorescence-based reference measurements over CHO-cell viability conditions; Semantic Scholar currently lists 0 citations and 0 influential citations.
- **Claimed contribution:** The authors report a mean absolute error of 2.33% for viability estimates on unstained CHO-cell samples and provide an interactive analysis tool.
- **Caveat:** Validation is specific to CHO cells and the reported imaging/reference setup. It does not establish performance across other cell types, instruments, or clinical specimens.
- **Announcement type:** revision, 2026-10-27
- **Themes:** Molecular & cell biology; Quantitative methods; Biomedical & translational medicine

## Trending Research Themes

- **Benchmark validity in perturbation biology:** Shared clones and escaping/ineffectively perturbed cells can distort reproducibility, transfer scores, or effect sizes (Huang, *Shared clones*; Huang, *Escaping cells*). Both argue for stronger separation between cell-level sampling precision and experimental reproducibility, but address distinct sources of distortion.
- **Structure-aware molecular design and simulation:** Target excision and PROBE aim to reduce or better allocate computational effort in binder/ligand design; GlycoWeave specializes in protein–glycan complexes; AMARO targets complex dynamics; MechGate decomposes small-molecule screening into entry, efflux, and activity. Their evidence ranges from computational benchmarks to selected yeast-display experiments—these are not interchangeable forms of validation.
- **Omics models and reusable resources:** HELICS, OmicsLM, pyTransRate, mdRNAcat, and the miRNA benchmark build or assess methods/data for genotype, transcriptome, RNA, or sequence analysis. Their shared practical question is how dataset construction and evaluation choices affect downstream biological interpretation.
- **Molecular evidence linked to biomedical samples:** The visual-proteomics study and methylation OOD paper connect computational tools to human tumor data; ViabiLens measures cultured cells. Each is an early-stage, study-specific evaluation rather than general clinical validation.

## Open Problems and Research Directions

- **Test model-driven structure/design prospectively.** Author-reported limits include AMARO’s over-favorable binding free energies and site-specific failures, and binder design’s dependence on target cropping and MSA choices. A useful follow-up would pre-register a blinded panel of targets and glycan classes, compare predicted poses with new structures or biochemical binding measurements, and report failure rates as well as successful cases. For binder workflows, replicate yeast-display findings across independent target campaigns before extending claims beyond design feasibility.
- **Separate perturbation response from selection and lineage effects.** The two CRISPR preprints point to clone sharing and ineffective knockdown as distinct confounders. Follow-up screens could combine independent transductions, clone barcodes, direct target-protein measurements, matched harvest times, and non-targeting controls; then test whether effect estimates and model rankings remain stable across donors and cell types. This is a synthesis proposal, not a clinical recommendation.
- **Stress-test synthetic and language-mediated omics.** HELICS reports common-variant fidelity but does not itself establish privacy protection; OmicsLM reports benchmark gains with some generated supervision. Follow-up evaluation could combine membership-inference and rare-variant tests, ancestry-stratified external biobanks, publication-disjoint benchmarks, and expert-curated or experimentally validated answer sets.
- **Connect RNA data resources to measured biology.** mdRNAcat’s force-labelled simulations could be compared with independent structural or biophysical ensemble measurements across RNA classes and sequence contexts. The goal would be to identify where simulation-derived training improves held-out conformational predictions, rather than treating increased dataset size as validation by itself.

## Takeaway

This week’s strongest pattern is methodological: several papers show that data generation and benchmark design can shape apparent biological performance as much as the model itself. The protein-design and omics tools report promising computational or study-specific results, but external replication and experiment remain the boundary between a useful method and a broader biological claim.

## Method and sources

- **Window:** 2026-10-23 00:00:00 UTC through snapshot time 2026-10-30 02:41:12 UTC; weekly means first submission or latest revision in that interval. The exact snapshot time is recorded here; arXiv’s latest announcement batch visible in the category listings was 2026-10-28.
- **Candidate scope:** `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. The arXiv API query was `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date and paginated. Update records were also collected with OAI-PMH sets `q-bio`, `cs`, and `physics` for 2026-10-23 through 2026-10-30, then filtered to the configured categories and checked against arXiv API timestamps. The filtered, API-checked pool contained 93 distinct papers eligible by first-submission or latest-update timestamp (59 first submissions and 42 updates, with 8 papers satisfying both). The selected 15 latest-version abstract pages were individually verified.
- **Ranking:** Semantic Scholar Graph API fields requested were title, authors, year, citationCount, influentialCitationCount, referenceCount, publicationTypes, fieldsOfStudy, and externalIds. At the snapshot, 3 of these papers had 1 current citation each and 12 had 0; all had 0 influential citations. The three nonzero current-total citation velocities were approximately 0.006–0.16 per day (total citations divided by age), not citation gains during the window. No numeric trend score was used. Because attention signals were sparse, this is a relevance-ranked “Notable recent papers” list, not a measured popularity chart.
- **Category listings:** [q-bio.BM](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), [cs archive (filtered for cs.BI)](https://arxiv.org/list/cs/recent), and [physics.med-ph](https://arxiv.org/list/physics.med-ph/recent). Candidate verification and final metadata use the linked arXiv abstract pages above.
- **Corroborating sources:** [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.32962?fields=title%2Cauthors%2Cyear%2CcitationCount%2CinfluentialCitationCount%2CreferenceCount%2CpublicationTypes%2CfieldsOfStudy%2CexternalIds); [Google Research’s institutional post on the binder-design workflow](https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/) (context from the same organization, not independent confirmation); [MechGate source](https://github.com/qinlang0008-blip/mechgate); [pyTransRate source](https://github.com/macmanes-lab/pytransrate); [mdRNAcat dataset page](https://huggingface.co/datasets/HelmholtzAI-FZJ/mdRNAcat).
- arXiv is not a representative biomedical index: most clinical and experimental biology preprints may instead appear on bioRxiv or medRxiv, and this report is not a systematic review or clinical evidence assessment.
