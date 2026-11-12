# arXiv Biology & Biomedicine — Wednesday, 11 November 2026

## Headline

10 notable papers from the latest available arXiv announcement batch (Wednesday, 11 November). Protein interaction and engineering methods lead the set, alongside single-cell/genome inference and uncertainty-aware medical imaging. Spoken agenda: compare experimental results with computational predictions, then identify what still needs independent validation. arXiv has no official trending chart; this is an inferred relevance ranking from incomplete biomedical coverage, not a measured popularity list.

The current date is Thursday, 12 November 2026; no newer batch appeared in the checked listings, so this report uses the prior Wednesday batch. Window: 2026-11-11 through 2026-11-11 by announcement-batch date. Snapshot: 2026-11-12 17:17:10 UTC.

## Notable recent papers (ranked by relevance)

### 1. [Emergent Biological Capabilities in a Foundation Model for Molecular Interactions](https://arxiv.org/abs/2611.14504)
- **Abstract:** Bonbon is a protein–ligand sequence model whose authors report zero-shot interaction predictions and prospective dose-response hits across nine disease targets.
- **Authors:** Adi Mashiach
- **arXiv:** `2611.14504v1` (published 2026-11-10 18:53:01 UTC; categories: `cs.LG` [primary], `q-bio.BM` [cross-list])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; accepted NeurIPS 2026 Main Track oral (also listed in the conference program); its relevance signal is reported prospective wet-lab testing, not measured readership.
- **Claimed contribution:** Authors report zero-shot function, binding-site and covalent-engagement predictions from frozen representations, plus a 61.5% dose-response hit rate for de novo compounds across nine targets/seven protein families. The paper describes synthesized compounds and IC50 assays; these are preclinical biochemical results, not clinical evidence.
- **Caveat:** Authors say capabilities remain coarse and do not yield explicit 3D coordinates; kinetic properties are untested. The reported hit rate is not evidence of therapeutic benefit.
- **Announcement type:** new submission, 11 Nov 2026 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine

### 2. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](https://arxiv.org/abs/2611.13348)
- **Abstract:** ProTEUS combines sequence, evolutionary and structural signals with experimental feedback to select protein mutations, reporting two enzyme-engineering campaigns with variants above tenfold wild-type activity.
- **Authors:** Yikun Zhang, Minghao Guo, Guangxue Xu, Peter Yichen Chen, Wojciech Matusik, Wengong Jin, Jingjing Chai, Kaiyi Jiang
- **arXiv:** `2611.13348v1` (published 2026-11-09 23:19:33 UTC; categories: `q-bio.BM` [primary], `cs.AI` [cross-list])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; appears in the 11 Nov q-bio.BM announcement listing as a new cross-list; authors report closed-loop experimental campaigns on two enzymes.
- **Claimed contribution:** Authors present mutation-focused modeling plus a physics-constrained structure predictor and experimental feedback; they report >10-fold activity variants in aldehyde dehydrogenase and levansucrase campaigns.
- **Caveat:** Evidence is limited to two enzyme targets/campaigns and does not establish transfer to other proteins or therapeutic outcomes. The paper discloses cofounder/employment relationships with Foundry Biosciences and related patent filings. Its v1 was first submitted 9 Nov; 11 Nov is the q-bio.BM listing date, not a new version.
- **Announcement type:** new cross-list into q-bio.BM, 11 Nov 2026 batch (original v1 submission: 9 Nov)
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [Bridging Graph and Pairwise Learning for Gene Regulatory Network Inference from scRNA-seq Data](https://arxiv.org/abs/2611.13801)
- **Abstract:** scGPL combines whole-network topology with local transcription-factor/target-pair learning to infer gene regulatory networks from single-cell expression data.
- **Authors:** Hang Li, Jiaxin Qi, Yan Cui, Yuhua Zheng, Jianqiang Huang
- **arXiv:** `2611.13801v1` (published 2026-11-10 09:34:28 UTC; categories: `q-bio.GN` [primary], `cs.AI` [cross-list])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; accepted to Bioinformatics; reports results across seven benchmark datasets and provides code/data archives.
- **Claimed contribution:** Authors report up to 13.7% improvement over the strongest baseline by combining global graph features and sampled local subgraphs.
- **Caveat:** Benchmark performance is computational evidence; inferred TF–target links still need perturbation or other experimental validation. The authors identify unseen genes and transfer to distinct biological systems as open challenges.
- **Announcement type:** new submission, 11 Nov 2026 batch
- **Themes:** DNA & genomics; RNA & transcriptomics; Bioinformatics & sequence analysis

### 4. [Improved Myelin Water Fraction Estimation and Uncertainty Mapping in Multicomponent T2 Relaxometry via NNLS Bootstrap Aggregation](https://arxiv.org/abs/2611.14395)
- **Abstract:** NNLS-BB uses residual resampling and repeated non-negative least-squares reconstruction to estimate myelin-water fraction and map sensitivity to noise.
- **Authors:** Erick J Canales-Rodríguez, Thomas Yu, Juan Manuel Górriz, Santiago Galdo-Álvarez, Tobias Kober, Tom Hilbert, Gian Franco Piredda, Miguel Ángel Rivas-Fernández
- **arXiv:** `2611.14395v1` (published 2026-11-10 17:43:51 UTC; categories: `physics.med-ph` [primary])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; evaluation includes 40,000 simulated voxels and scan–rescan measurements in two independent cohorts totaling 13 healthy participants.
- **Claimed contribution:** Authors report 36–41% lower mean absolute error than conventional NNLS in simulations and favorable regional repeatability in both cohorts, with bootstrap variability maps.
- **Caveat:** The in-vivo sample is small and consists of healthy participants; this does not establish clinical utility in neurological disease or across scanners.
- **Announcement type:** new submission, 11 Nov 2026 batch
- **Themes:** Medical physics & imaging; Quantitative methods

### 5. [Detection of local recombination and mutation hotspots in bacterial genomes using neural posterior estimation](https://arxiv.org/abs/2611.13763)
- **Abstract:** A simulation-trained neural posterior method estimates gene-specific bacterial mutation/recombination rates and propagates uncertainty into hotspot detection.
- **Authors:** Haochu Liu, Richard G. Everitt, Xavier Didelot
- **arXiv:** `2611.13763v1` (published 2026-11-10 09:03:29 UTC; categories: `q-bio.GN` [primary])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; authors report recovery tests on simulated data and applications to three bacterial datasets (*Bacillus cereus*, *Staphylococcus aureus*, *Escherichia coli*); implementation is public.
- **Claimed contribution:** Authors propose neural posterior estimation conditioned on a fixed clonal genealogy and a posterior-propagating local hotspot detector.
- **Caveat:** Inference depends on the specified recombination model and simulated training conditions; real-data applications demonstrate use, not independent experimental confirmation of detected hotspots.
- **Announcement type:** new submission, 11 Nov 2026 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 6. [The Dose Makes the Poison: Exposure-Aware Evaluation of Generative Drug Design](https://arxiv.org/abs/2611.13398)
- **Abstract:** PBPK simulations re-rank PARP1-targeted generated molecules after considering whether predicted target exposure and dose-related safety remain plausible.
- **Authors:** Maria Franz, N. Benjamin Erichson
- **arXiv:** `2611.13398v1` (published 2026-11-10 00:20:01 UTC; categories: `q-bio.QM` [primary], `cs.AI`, `cs.LG` [cross-lists])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; accepted to the NeurIPS 2026 AI4DD workshop; quantitative analysis of 60 shortlisted molecules across three generative pipelines.
- **Claimed contribution:** Authors' PBPK simulations predict insufficient exposure for seven of 60 molecules and dose-related safety risks for 28% of the remainder; 85% of candidates with an achievable dose are outperformed by molecules missed by static selection.
- **Caveat:** These are model-based predictions for PARP1 candidates, not experimental pharmacokinetics, toxicology, or evidence of clinical safety or efficacy.
- **Announcement type:** new submission, 11 Nov 2026 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 7. [ANTIOCH-VS: From Sequence to Hits with Modular, Open-Source Ensemble Virtual Screening](https://arxiv.org/abs/2611.14287)
- **Abstract:** ANTIOCH-VS builds receptor ensembles from sequence and screens ligand libraries, reporting enriched top-20 lists for JAK2 and ADRB2 benchmark sets.
- **Authors:** Hale S. Hasdemir, Venkata Sai Sreyas Adury, Pratyush Tiwary
- **arXiv:** `2611.14287v1` (published 2026-11-10 16:27:14 UTC; categories: `physics.chem-ph` [primary], `q-bio.BM` [cross-list])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; open-source code and two-target DUD-E benchmark; authors report 20% and 60% hit rates in top-20 shortlists versus roughly 1–2% random.
- **Claimed contribution:** Authors combine predicted conformational ensembles, docking, consensus ranking and metadynamics in a modular sequence-to-shortlist workflow.
- **Caveat:** The reported tests are retrospective benchmark enrichment on two targets, not prospective binding assays or evidence that predicted hits work experimentally.
- **Announcement type:** new submission, 11 Nov 2026 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 8. [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511)
- **Abstract:** Pyrite benchmarks protein–ligand pose comparisons and tests language-model agents that reason over poses or generate features for a learned ranker.
- **Authors:** Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver
- **arXiv:** `2611.14511v1` (published 2026-11-10 18:56:32 UTC; categories: `cs.LG` [primary], `q-bio.QM` [cross-list])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; 1,500 pose pairs and a NeurIPS 2026 Agentic AI for Biological Discovery workshop submission; the best reported agent reaches 74% accuracy.
- **Claimed contribution:** Authors report that LLM-guided feature discovery outperforms direct text reasoning and exceeds near-chance expert performance on their benchmark.
- **Caveat:** Accuracy is benchmark-specific; it does not show that agent-selected poses improve prospective experiments or drug discovery outcomes.
- **Announcement type:** new submission, 11 Nov 2026 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 9. [When Covariance Is Not Enough: Kernel-Based Regularization for Single-Cell Counterfactuals](https://arxiv.org/abs/2611.13748)
- **Abstract:** A nonlinear kernel-independence penalty improves counterfactual single-cell expression profiles when known and unknown factors interact nonlinearly.
- **Authors:** Korbinian Traeuble, Edward de Brouwer, Archit Verma, Doron Haviv, Kipper Fletez-Brant
- **arXiv:** `2611.13748v1` (published 2026-11-10 08:49:33 UTC; categories: `cs.LG` [primary], `q-bio.GN` [cross-list])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; evaluates controlled simulations with known edits and applies the method to a single-cell RNA-seq dataset.
- **Claimed contribution:** Authors report that normalized HSIC regularization recovers true intervention effects in simulations and improves counterfactual profiles in the applied dataset.
- **Caveat:** The real-data demonstration is computational and does not establish counterfactual predictions against measured perturbations.
- **Announcement type:** new submission, 11 Nov 2026 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 10. [A first application of split conformal prediction for dose prediction in knowledge-based radiotherapy planning](https://arxiv.org/abs/2611.14438)
- **Abstract:** Patient-level split-conformal intervals quantify uncertainty in deep-learning dose predictions for head-and-neck radiotherapy planning.
- **Authors:** Raphaël Brodeur, Anne-Sophie Charest, Louis Archambault
- **arXiv:** `2611.14438v1` (published 2026-11-10 18:10:47 UTC; categories: `physics.med-ph` [primary])
- **Evidence for ranking:** Semantic Scholar snapshot: 0 citations, 0 influential citations; submitted to *Physics in Medicine & Biology*; evaluates empirical coverage and interval width on head-and-neck cases.
- **Claimed contribution:** Authors formulate maximum- and quantile-aggregation guarantees for future-patient voxel coverage and report empirical coverage consistent with nominal levels.
- **Caveat:** This is a model-evaluation study, not a prospective clinical workflow or proof that intervals improve treatment decisions; the abstract does not state the cohort size.
- **Announcement type:** new submission, 11 Nov 2026 batch
- **Themes:** Medical physics & imaging; Quantitative methods

## Trending Research Themes

- Protein interaction and engineering methods span different evidence levels: Bonbon reports prospective biochemical assays and ProTEUS two closed-loop enzyme campaigns, while ANTIOCH-VS and Pyrite remain computational benchmark studies. These are related tasks, not independent validation of one another.
- Genomic and single-cell inference methods are emphasizing uncertainty or nonlinear structure: the bacterial hotspot model propagates posterior uncertainty, scGPL joins global and local regulatory-network features, and the counterfactual model tests nonlinear disentanglement. Their claims are computational and await broader experimental checks.
- Measurement reliability is a visible biomedical-methods theme in this small batch: NNLS-BB estimates MRI-derived myelin-water fraction variability, while the radiotherapy paper uses conformal intervals for predicted dose. Neither establishes clinical impact.
- Drug-design prioritization is evaluated beyond static scores in the PARP1 PBPK study, which shows how exposure assumptions can change a shortlist; its conclusions remain simulation-based.

## Open Problems and Research Directions

- **Independent protein validation:** Bonbon and ProTEUS report wet-lab results, but with different tasks and limited target sets. Replicate findings with blinded assays, prespecified comparators, more protein families and independent laboratories; report inactive compounds as well as hits.
- **From inferred networks to causal regulation:** scGPL and the kernel-counterfactual study need evaluation against held-out perturbation experiments, unseen genes and new systems. A follow-up could pre-register targets and compare predictions with CRISPRi or drug-perturbation single-cell profiles.
- **Imaging generalization:** NNLS-BB's in-vivo cohorts total 13 healthy participants, and the radiotherapy abstract does not state its case count. Test repeatability, calibration and interval width across larger external cohorts, disease groups, scanners and protocols before evaluating prospective workflow effects.
- **Bridge virtual screening/PBPK predictions to assays:** prospectively synthesize a blinded set from ANTIOCH-VS and compare PBPK-adjusted versus statically ranked compounds; measure biochemical binding, exposure and toxicity rather than assuming simulation predictions transfer.

## Takeaway

This batch is notable for protein-focused modeling and methods that quantify uncertainty or improve biological inference. Evidence ranges from prospective biochemical experiments to retrospective benchmarks and simulations; none of these reports establishes clinical benefit. Citation and independent-attention signals are too sparse to support a popularity ranking, so the ordering reflects biological relevance and reported validation strength.

## Method and sources

- **Window:** daily; latest available announcement batch dated 11 Nov 2026. No newer batch appeared in the checked listings on 12 Nov. Window start/end: 2026-11-11 through 2026-11-11 (announcement-batch dates). Snapshot: 2026-11-12 17:17:10 UTC.
- **Scope:** configured categories `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`; relevant cross-lists were included. Recent-list pages were checked for all categories; arXiv rejected `cs.BI` as an invalid listing page and the API returned no `cs.BI` records in the queried pool, so no papers were added from it.
- **arXiv API query:** [explicit category query, newest submissions](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200). The first 200 results extended back to 28 Oct, beyond the selected batch; category listings were also checked to catch cross-list additions. Cross-listed papers were deduplicated by versionless arXiv ID.
- **Verification:** every selected paper was checked on its arXiv abstract page. The top three were additionally read in PDF, including introduction, results and discussion/limitations. Semantic Scholar Graph API was queried for the requested bibliographic and citation fields; all ten selected records showed 0 citations and 0 influential citations at retrieval. Citation totals are current snapshots, not gains during this window.
- **Ranking:** arXiv has no official trend metric. Citation momentum and independent discussion were insufficient to establish attention. An independent search confirmed Bonbon's NeurIPS oral program listing; the rest are ranked as notable recent papers by biological relevance and reported validation, with cross-list breadth and venue status as supporting context—not readership.
- **Coverage caveat:** this is a point-in-time arXiv sample, not a representative survey of biomedical research. Clinical and experimental biology preprints often appear on bioRxiv or medRxiv; those repositories and the broader medical literature are outside this report.
- **Sources:** [arXiv q-bio.BM recent](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), [physics.med-ph](https://arxiv.org/list/physics.med-ph/recent); individual arXiv abstract pages are linked in each title. Corroboration: [NeurIPS 2026 oral listing for Bonbon](https://neurips.cc/virtual/2026/oral/149425), [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch).
