# arXiv Biology & Biomedicine — Wednesday, 11 November 2026

## Headline

Nine notable papers from the latest available arXiv announcement batch (Wednesday, 11 November). The dominant pattern is computational molecular design increasingly paired with biochemical experiments, alongside computational advances in genomics, single-cell analysis, and imaging uncertainty. This report is a relevance-ranked selection, not a measured popularity chart: arXiv has no official trending chart, and its biomedical coverage is incomplete—much experimental and clinical preprint activity appears on bioRxiv and medRxiv.

The requested day is Thursday, 12 November; at the 01:17 UTC snapshot no Thursday batch was listed, so this report uses the prior Wednesday batch. The window is the 11 November announcement batch, not a filter on first-submission timestamps.

## Notable recent papers (ranked by demonstrated relevance)

### 1. [Emergent Biological Capabilities in a Foundation Model for Molecular Interactions](https://arxiv.org/abs/2611.14504)
- **Abstract:** Bonbon learns protein–ligand interaction representations and the authors report zero-shot molecular-function predictions plus prospective biochemical hit validation across nine targets.
- **Authors:** Adi Mashiach
- **arXiv:** `2611.14504v1` (published 2026-11-10 18:53:01 UTC; categories: `cs.LG` [primary], `q-bio.BM` [cross-list])
- **Evidence for ranking:** NeurIPS 2026 main-track oral status is independently listed by NeurIPS; the authors report a prospective assay panel spanning nine disease targets and seven protein families.
- **Claimed contribution:** The authors claim one frozen sequence-only model supports mechanism, binding-site, and bond-type predictions; their prospective assays yielded a 61.5% dose-response hit rate among the tested de novo compounds.
- **Caveat:** The paper says its interaction distinctions are still coarse and it does not recover explicit 3D coordinates. Biochemical target hits are not evidence of clinical safety or efficacy.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 2. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](https://arxiv.org/abs/2611.13348)
- **Abstract:** ProTEUS combines mutation-effect prediction with experimental feedback to guide protein engineering; the authors report two closed-loop enzyme campaigns producing variants with over tenfold wild-type activity.
- **Authors:** Yikun Zhang, Minghao Guo, Guangxue Xu, Peter Yichen Chen, Wojciech Matusik, Wengong Jin, Jingjing Chai, Kaiyi Jiang
- **arXiv:** `2611.13348v1` (published 2026-11-09 23:19:33 UTC; categories: `q-bio.BM` [primary], `cs.AI` [cross-list])
- **Evidence for ranking:** Listed in the 11 November biomolecules batch; the paper reports closed-loop wet-lab work on two enzymes, aldehyde dehydrogenase and levansucrase, in addition to mutation-prediction benchmarks.
- **Claimed contribution:** The authors connect sequence, evolutionary, and structural representations to mutation actions, and describe a physics-constrained structure predictor and feedback loop for steering protein evolution.
- **Caveat:** The reported engineering campaigns cover two enzyme targets and assay-specific activity outcomes; they do not establish broad transfer to other protein classes or organism-level effects.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 3. [Bridging Graph and Pairwise Learning for Gene Regulatory Network Inference from scRNA-seq Data](https://arxiv.org/abs/2611.13801)
- **Abstract:** scGPL combines whole-network topology with local transcription-factor/target-gene pair learning and reports improved benchmark performance across seven single-cell datasets.
- **Authors:** Hang Li, Jiaxin Qi, Yan Cui, Yuhua Zheng, Jianqiang Huang
- **arXiv:** `2611.13801v1` (published 2026-11-10 09:34:28 UTC; categories: `q-bio.GN` [primary], `cs.AI` [cross-list])
- **Evidence for ranking:** The arXiv record says accepted to Bioinformatics; the authors report seven benchmark datasets, a maximum 13.7% gain over their strongest baseline, and code plus versioned data releases.
- **Claimed contribution:** The method fuses global regulatory-graph features with dynamically sampled local subgraphs to address weaknesses of graph-only and pairwise-only inference.
- **Caveat:** These are computational network-inference benchmarks, not experimental confirmation of regulatory edges. The authors note dynamic subgraph sampling adds computational overhead.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** DNA & genomics; RNA & transcriptomics; Bioinformatics & sequence analysis

### 4. [ANTIOCH-VS: From Sequence to Hits with Modular, Open-Source Ensemble Virtual Screening](https://arxiv.org/abs/2611.14287)
- **Abstract:** ANTIOCH-VS builds receptor ensembles from sequence and ranks candidate ligands; on two retrospective target benchmarks, its top-20 lists were enriched for known binders.
- **Authors:** Hale S. Hasdemir, Venkata Sai Sreyas Adury, Pratyush Tiwary
- **arXiv:** `2611.14287v1` (published 2026-11-10 16:27:14 UTC; categories: `physics.chem-ph` [primary], `q-bio.BM` [cross-list])
- **Evidence for ranking:** The authors provide an open-source end-to-end workflow and report tests on JAK2 and ADRB2 DUD-E sets, with top-20 hit rates of 20% and 60% respectively (random selection about 1–2%).
- **Claimed contribution:** The pipeline combines conformational ensembles, docking, consensus ranking, and metadynamics triage to screen from a protein sequence without a ligand-bound crystal structure.
- **Caveat:** Both evaluations are retrospective computational benchmarks; enriched shortlists are not prospective biochemical hits or evidence of therapeutic efficacy.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 5. [Detection of local recombination and mutation hotspots in bacterial genomes using neural posterior estimation](https://arxiv.org/abs/2611.13763)
- **Abstract:** A simulation-trained neural posterior estimator models gene-level bacterial mutation and recombination rates and propagates uncertainty into hotspot detection.
- **Authors:** Haochu Liu, Richard G. Everitt, Xavier Didelot
- **arXiv:** `2611.13763v1` (published 2026-11-10 09:03:29 UTC; categories: `q-bio.GN` [primary])
- **Evidence for ranking:** The paper combines simulation recovery tests with applications to three bacterial datasets (Bacillus cereus, Staphylococcus aureus, and Escherichia coli) and provides a public Python implementation.
- **Claimed contribution:** The authors use neural posterior estimation conditioned on a fixed clonal genealogy, then a circular posterior-propagated detector to identify local rate hotspots.
- **Caveat:** The inference is conditional on the specified recombination model and genealogy; the data applications illustrate use but do not experimentally validate hotspot function or fitness effects.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

### 6. [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511)
- **Abstract:** Pyrite benchmarks protein–ligand pose ranking and compares expert chemists with language-model agents that reason over poses or discover features for a classical ranker.
- **Authors:** Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver
- **arXiv:** `2611.14511v1` (published 2026-11-10 18:56:32 UTC; categories: `cs.LG` [primary], `q-bio.QM` [cross-list])
- **Evidence for ranking:** The benchmark contains 1,500 pose pairs and is listed for the Agentic AI for Biological Discovery workshop at NeurIPS 2026; Semantic Scholar’s indexed record showed zero current citations and zero influential citations at this snapshot, so citations do not support a popularity claim.
- **Claimed contribution:** The authors report up to 67% accuracy for direct reasoning and 74% for LLM-guided feature construction, above the observed expert performance on this benchmark.
- **Caveat:** The reported accuracy is benchmark-specific and computational; it does not establish pose correctness or binding experimentally. The evaluation uses a held-out post-AF3 split after training on earlier benchmark data.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 7. [When Covariance Is Not Enough: Kernel-Based Regularization for Single-Cell Counterfactuals](https://arxiv.org/abs/2611.13748)
- **Abstract:** The authors add a nonlinear independence penalty to single-cell counterfactual models and report better recovery of known edits in simulations and improved expression-profile generation on one scRNA-seq dataset.
- **Authors:** Korbinian Traeuble, Edward de Brouwer, Archit Verma, Doron Haviv, Kipper Fletez-Brant
- **arXiv:** `2611.13748v1` (published 2026-11-10 08:49:33 UTC; categories: `cs.LG` [primary], `q-bio.GN` [cross-list])
- **Evidence for ranking:** The work pairs controlled simulations with a real single-cell RNA-seq application; the indexed Semantic Scholar record showed zero current citations and zero influential citations at the snapshot.
- **Claimed contribution:** The paper argues that linear cross-covariance penalties can miss nonlinear dependence and uses normalized HSIC to regularize the separation of known and unknown factors.
- **Caveat:** The real-data test is one dataset and the counterfactual profiles are model outputs, not observed responses to matched perturbation experiments.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 8. [Improved Myelin Water Fraction Estimation and Uncertainty Mapping in Multicomponent T2 Relaxometry via NNLS Bootstrap Aggregation](https://arxiv.org/abs/2611.14395)
- **Abstract:** NNLS-BB bootstraps repeated non-negative least-squares reconstructions to estimate myelin water fraction and signal-perturbation variability, improving simulation error and scan–rescan measures in small healthy cohorts.
- **Authors:** Erick J Canales-Rodríguez, Thomas Yu, Juan Manuel Górriz, Santiago Galdo-Álvarez, Tobias Kober, Tom Hilbert, Gian Franco Piredda, Miguel Ángel Rivas-Fernández
- **arXiv:** `2611.14395v1` (published 2026-11-10 17:43:51 UTC; categories: `physics.med-ph` [primary])
- **Evidence for ranking:** The study compares against four alternatives on 40,000 simulated voxels and assesses repeatability in two independent cohorts totaling 13 healthy participants.
- **Claimed contribution:** The authors report 36–41% lower mean absolute error than conventional NNLS in simulations and lower regional scan–rescan dispersion in both cohorts.
- **Caveat:** The in-vivo repeatability sample is small and limited to healthy participants; it does not establish performance in neurological disease or clinical diagnosis.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 9. [A first application of split conformal prediction for dose prediction in knowledge-based radiotherapy planning](https://arxiv.org/abs/2611.14438)
- **Abstract:** Split conformal prediction is used to form patient-level uncertainty intervals for deep-learning radiotherapy dose estimates, with empirical coverage assessed on head-and-neck cases.
- **Authors:** Raphaël Brodeur, Anne-Sophie Charest, Louis Archambault
- **arXiv:** `2611.14438v1` (published 2026-11-10 18:10:47 UTC; categories: `physics.med-ph` [primary])
- **Evidence for ranking:** The paper applies patient-level split conformal constructions to a deep ensemble and compares maximum, quantile, groupwise, and locally scaled intervals; the arXiv comment says it was submitted to Physics in Medicine & Biology.
- **Claimed contribution:** The authors report empirical coverage near nominal levels, with maximum aggregation more conservative and quantile aggregation producing narrower intervals.
- **Caveat:** The abstract does not state the cohort size, and empirical calibration in the reported head-and-neck setting is not external clinical validation; finite-sample guarantees depend on the conformal sampling assumptions.
- **Announcement type:** new submission, 2026-11-11 batch
- **Themes:** Medical physics & imaging; Quantitative methods

## Trending Research Themes

- **Protein design and ligand ranking are being tested across a prediction-to-assay spectrum.** ProTEUS and Bonbon report wet-lab activity experiments, whereas ANTIOCH-VS and Pyrite evaluate virtual screening or pose-ranking benchmarks. These are complementary tasks, not four independent validations of a single pipeline: only the first two include the reported biochemical follow-up, and none establishes clinical benefit.
- **Genomic and single-cell papers focus on recovering structure from sparse observations.** scGPL combines global and local regulatory-network information; the recombination-hotspot paper estimates gene-level rates with uncertainty; and the kernel counterfactual paper tests whether nonlinear dependence penalties improve cell-level intervention predictions. The evidence is primarily computational, with different forms of benchmark or dataset validation.
- **Imaging methods make uncertainty more explicit.** NNLS-BB estimates variability in myelin-water measurements, while the radiotherapy paper constructs patient-level dose intervals. Both move beyond point estimates, but cohort breadth and external calibration remain important boundaries.

## Open Problems and Research Directions

1. **Test protein predictions prospectively and independently.** ProTEUS reports closed-loop campaigns on two enzymes, while Bonbon’s nine-target panel remains biochemical target-level evidence. Follow-up could use blinded, preregistered panels across more protein families, matched baselines, independent assay labs, and reporting of inactive as well as active compounds; for pose ranking, Pyrite and ANTIOCH-VS could be evaluated against experimentally resolved poses and prospective binding assays.
2. **Ground genomic and single-cell predictions in perturbations.** scGPL’s regulatory edges and the kernel model’s counterfactual expression profiles are not direct observations of causal responses. A concrete next step is evaluation on held-out Perturb-seq or CRISPRi datasets, with perturbations and cell types excluded from training, plus calibration of edge- and cell-level uncertainty. The bacterial hotspot model could be tested against independent lineages and functional assays of genes near predicted hotspots.
3. **Measure imaging transfer outside the development setting.** NNLS-BB’s in-vivo repeatability cohorts contain 13 healthy participants, and the radiotherapy abstract does not report its case count. Replication across larger, diseased cohorts, scanners, institutions, and acquisition protocols could assess repeatability and interval coverage under distribution shift before any workflow claims.

## Takeaway

The clearest evidence-rich thread is protein modeling linked to experimental assays, while the genomics and single-cell papers mostly make computational predictions that still need perturbational checks. Imaging papers add uncertainty estimates, but their reported evaluation settings are not broad enough to imply clinical readiness. This is a snapshot of one arXiv batch, not a guide to the broader biomedical literature.

## Method and sources

- **Window:** daily announcement batch, 2026-11-11 through 2026-11-11; snapshot 2026-11-12 01:17 UTC. The 12 November listing had not appeared, so the latest available Wednesday batch was used. arXiv entry timestamps are preserved individually above and can precede the announcement date.
- **Candidate categories:** `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. The broad arXiv API query was: `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date descending; recent category listings were checked and cross-listed records were deduplicated by versionless arXiv ID. The `cs.BI` query returned no records.
- **Ranking:** no measured attention ranking was available for the batch, so entries are titled **Notable recent papers** and ordered by relevance plus checkable evidence (wet-lab versus computational evaluation, breadth of reported benchmarks, cross-listing, and stated acceptance status), not by inferred readership. Semantic Scholar metadata was checked where indexed; the two indexed records reported above had zero current citations and zero influential citations. These are current totals, not citation gains during this window.
- **Evidence boundary:** all nine arXiv abstract pages were verified; the first three papers were also read in PDF form through their methods/results/discussion or limitations. Author claims are identified as such. No paper is treated as clinical guidance or as a clinical trial.
- **Sources:** [arXiv q-bio.BM recent](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), [physics.med-ph](https://arxiv.org/list/physics.med-ph/recent); individual arXiv abstract pages are linked in each title. Corroboration: [NeurIPS oral listing for Bonbon](https://neurips.cc/virtual/2026/oral/149425), [Semantic Scholar record for Pyrite](https://www.semanticscholar.org/paper/e3b989ca327c85dd5745340e666fa353a7df1cdf), and [Semantic Scholar record for the kernel counterfactual paper](https://www.semanticscholar.org/paper/160b9958b1d5bd47d8b11ab8e055d8ae193a8191).
