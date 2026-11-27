# Biology and biomedicine on arXiv — 27 November 2026

Ten notable recent papers from the 19–26 November announcement window, led by models for DNA–protein kinetics, cell perturbation, RNA design, and disease-associated red-cell adhesion. Spoken agenda: what these methods claim, what evidence supports them, and where validation remains open. This is an inferred, evidence-ranked selection: arXiv has no official trending chart, and its preprint corpus is incomplete for biomedicine; much experimental and clinical work appears on bioRxiv or medRxiv instead. Attention signals were sparse, so these are notable recent papers, not a measured popularity ranking.

## Top papers (ranked)

### 1. [Exclusion and internal structure in the association/dissociation kinetics of DNA-binding proteins in the fast diffusion limit](https://arxiv.org/abs/2611.33740)
- **Abstract:** A coarse-grained stochastic/mean-field model combines DNA-site exclusion and protein conformational switching, is fitted to previously measured RPA–ssDNA dynamics, and extends to multisegment binding and facilitated exchange.
- **Authors:** Xiangting Li, Tom Chou
- **arXiv:** `2611.33740v1` (published 2026-11-25T04:01:12Z; categories: `q-bio.BM`, `cond-mat.soft`, `cond-mat.stat-mech`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.75, entirely from three cross-lists (0.25 each); Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded. Daily editions featured it twice (26 and 27 Nov; best daily rank 1), a continuity signal only, not a weekly attention score.
- **Claimed contribution:** The authors report that their reduced Markov model captures stochastic coverage dynamics in tested fast-diffusion regimes and fits existing RPA binding data; the model also describes facilitated exchange in multisegment systems.
- **Caveat:** The central reduction assumes rapid positional equilibration; the RPA comparison refits prior experimental data rather than reporting a new biochemical experiment. The authors identify slower diffusion and active remodeling as open extensions.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** Biochemistry & proteins; DNA & genomics; Quantitative methods

### 2. [Receptor Abundance Alone Underpredicts Red Blood Cell Adhesion in Gaucher Disease](https://arxiv.org/abs/2611.27960)
- **Abstract:** A stochastic-bond red-cell model calibrated on control donors finds that the observed 1.3-fold Lu/BCAM increase does not explain the stronger adhesion reported for Gaucher-disease cells, pointing to receptor state as a possible additional factor.
- **Authors:** Zhaojie Chai, Pierre A. Buffet, Melanie Franco, George Em Karniadakis
- **arXiv:** `2611.27960v1` (published 2026-11-20T18:39:09Z; categories: `physics.bio-ph`, `cond-mat.soft`, `physics.med-ph`, `q-bio.CB`)
- **Evidence for ranking:** Signal score 0.75, entirely from three cross-lists; Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded. Daily editions featured it twice (22 and 23 Nov; best daily rank 1).
- **Claimed contribution:** Using published adhesion measurements and a model calibrated to control donors, the authors report a 1.6–1.7-fold gap between measured and predicted adhesion and propose binding-competent receptor state, not abundance alone, as a plausible explanation.
- **Caveat:** This is a model-based analysis of existing donor and assay data, not a prospective clinical study. The paper notes assumptions including short simulated flow exposure and uncertain cell contact density; its donor groups numbered 12–23 per group.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 3. [How Far Can Linear Go? BiPert, a Unified Framework for Single-Cell Perturbation Modelling](https://arxiv.org/abs/2611.31227)
- **Abstract:** BiPert uses a linear decomposition for forward prediction of perturbation responses and inverse identification of perturbed genes, with reported strengths on held-out cell lines and donors in published CRISPR-screen benchmarks.
- **Authors:** Abhishek Sharma, Aleksej Zelezniak
- **arXiv:** `2611.31227v1` (published 2026-11-23T18:58:32Z; categories: `cs.LG`, `q-bio.CB`, `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.75, entirely from three cross-lists; Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded.
- **Claimed contribution:** The authors report improved transfer on unseen cell lines over knowledge-free baselines and strong inverse identification on new contexts, with a few-shot variant using as few as ten measured perturbations.
- **Caveat:** Results are benchmark-based, not experimental validation of new gene mechanisms. On the full 34-view ExPert benchmark, ExPert slightly leads overall (top-10 recall 0.482 vs 0.449); BiPert's advantage concentrates in genuinely unseen lines or donors.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Bioinformatics & sequence analysis

### 4. [Motivo: A Motif-Based Algorithm-Architecture Co-Design for Fast and Energy-Efficient Graph-Based Genome Analysis](https://arxiv.org/abs/2611.29410)
- **Abstract:** Motivo uses recurring genome-graph motifs to reduce redundant sequence-to-graph mapping work, with CPU, GPU, and proposed ASIC implementations evaluated on short- and long-read mapping tasks.
- **Authors:** Eirini Maria Tzermpou, Konstantina Koliogeorgi, Konstantinos Kanellopoulos, Ataberk Olgun, Nisa Bostancı, Dimitrios Soudris, Nika Mansouri Ghiasi, Onur Mutlu
- **arXiv:** `2611.29410v1` (published 2026-11-22T11:25:32Z; categories: `cs.AR`, `cs.DC`, `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.75, entirely from three cross-lists; Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded.
- **Claimed contribution:** The authors report speed, energy, and throughput gains over named graph-mapping baselines while maintaining 96.8–99.7% mapping accuracy on two types of genome graphs.
- **Caveat:** This is an algorithm/architecture benchmark, not evidence of improved biological conclusions in downstream studies; the reported results are tied to tested graph types, reads, and comparators.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 5. [KnitNet: Learning to Search at Inference Time for Exact RNA Inverse Design](https://arxiv.org/abs/2611.33812)
- **Abstract:** KnitNet iteratively repairs candidate sequences using verifier feedback and an online surrogate; the authors report higher exact-match rates on five RNA secondary-structure benchmarks and improved 3D self-consistency.
- **Authors:** Antonia Panescu, Xin Wang, Haoran Xu, Qingyu Chen, Carlos Oliver, Rex Ying
- **arXiv:** `2611.33812v1` (published 2026-11-25T05:42:56Z; categories: `q-bio.BM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Signal score 0.50, entirely from two cross-lists; Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded. Daily editions featured it twice (26 and 27 Nov; best daily rank 1).
- **Claimed contribution:** Across five secondary-structure benchmarks, the authors report a 21-percentage-point average exact-solve gain over continued sampling with 70% less time-to-solve; they also report improved 3D structural self-consistency versus per-target reinforcement learning.
- **Caveat:** The exact-match results are computational benchmarks; the reported 3D metric is structural self-consistency, not experimental confirmation that designed RNA folds as intended in vitro or in cells.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Quantitative methods

### 6. [From the Deterministic Hook Effect to Stochastic Reliability in Ternary Complex Formation](https://arxiv.org/abs/2611.33753)
- **Abstract:** Deterministic and stochastic simulations of a minimal reversible binding network show that a favorable average hook-shaped dose response need not yield reliable ternary-complex formation in small volumes.
- **Authors:** Deepak K. Agrawal
- **arXiv:** `2611.33753v1` (published 2026-11-25T04:12:08Z; categories: `math.DS`, `q-bio.BM`, `q-bio.MN`)
- **Evidence for ranking:** Signal score 0.50, entirely from two cross-lists; Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded. Daily editions featured it twice (26 and 27 Nov; best daily rank 3).
- **Claimed contribution:** The author reports that volume, molecular copy-number thresholds, and complex formation/breakup rates change reliability even where deterministic dose-response favors assembly.
- **Caveat:** This is a minimal model with simulations, not an experimental test of a particular signaling pathway or therapeutic degrader.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 7. [Cell-Type-Specific Expression Is Hard to Predict from Bulk, but It Is Still Useful](https://arxiv.org/abs/2611.34166)
- **Abstract:** The authors derive linear-estimator learnability bounds for cell-type-specific expression and report that deconvolved features can retain prognostic information in a non-small-cell lung cancer survival analysis.
- **Authors:** Gadi Naveh, Amit Miller, Gal Keinan
- **arXiv:** `2611.34166v1` (published 2026-11-25T10:57:38Z; categories: `cs.LG`, `q-bio.QM`, `stat.ML`)
- **Evidence for ranking:** Signal score 0.50, entirely from two cross-lists; Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded. The daily rollup did not list it.
- **Claimed contribution:** For 106 biologically curated cell-type/gene pairs, the authors report that a sparse survival model using deconvolved features predicts overall survival about as well as a model on bulk genes while attributing signals to cell types.
- **Caveat:** The 106 targets were found post hoc to have higher learnability; the survival result is an analysis of an existing cohort, not prospective clinical validation or proof of causal cell-type mechanisms.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Biomedical & translational medicine

### 8. [Bayesian Learning of Spatially Heterogeneous Causal Structure in Spatial Transcriptomics](https://arxiv.org/abs/2611.33094)
- **Abstract:** SpaDAG estimates spatially varying causal DAGs on tissue triangulations, allowing edge direction to reverse across regions; the paper reports simulations and an application to a renal-cell-carcinoma/kidney section.
- **Authors:** Kyungwook Back, Junsouk Choi
- **arXiv:** `2611.33094v1` (published 2026-11-24T18:28:56Z; categories: `stat.ME`, `q-bio.GN`, `stat.AP`)
- **Evidence for ranking:** Signal score 0.50, entirely from two cross-lists; Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded. The daily rollup did not list it.
- **Claimed contribution:** The authors report improved recovery in simulations, including direction reversals, and identify tumor-region associations in one tissue section as hypotheses for region-specific gene coupling.
- **Caveat:** Spatial causal directions in the tumor example are inferred from one section and are not experimentally established mechanisms or validated therapeutic targets.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Bioinformatics & sequence analysis

### 9. [Stochastic Failure Dynamics in a Model Peptidoglycan Mesh under Hydrolysis and Mechanical Loading](https://arxiv.org/abs/2611.34610)
- **Abstract:** A stochastic-mechanical model of Gram-negative peptidoglycan under hydrolysis predicts weakest-link failure and localized rupture, with mechanical load accelerating collapse in simulations.
- **Authors:** Issan Patri, Garima Rani
- **arXiv:** `2611.34610v1` (published 2026-11-25T16:00:29Z; categories: `physics.bio-ph`, `math-ph`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.50, entirely from two cross-lists; Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded. The daily rollup did not list it.
- **Claimed contribution:** The authors derive limiting failure-time behavior and use stochastic simulations to show that hydrolysis can trigger localized wall collapse even when overall cross-linking remains high.
- **Caveat:** The work is a minimal mathematical model, not an experimental demonstration of bacterial lysis under an antibiotic; cellular growth and wall-repair processes are simplified or blocked.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 10. [Impact of Topology and Sequence Length on the Pressure-Dependent Collapsibility of Proteins](https://arxiv.org/abs/2611.30336)
- **Abstract:** A theoretical framework with pressure-dependent desolvation predicts that protein topology and sequence length shape pressure-induced collapse into compact, water-mediated conformations.
- **Authors:** Jiayi Wang, D. Thirumalai, Margaret S. Cheung, Andrei G. Gasic
- **arXiv:** `2611.30336v1` (published 2026-11-23T09:13:26Z; categories: `physics.bio-ph`, `cond-mat.soft`, `q-bio.BM`)
- **Evidence for ranking:** Signal score 0.50, entirely from two cross-lists; Semantic Scholar signals: 0 citations, 0 influential citations. No Hugging Face or Hacker News attention was recorded. The daily rollup did not list it.
- **Claimed contribution:** The authors report that increasing pressure destabilizes the fully folded native state while favoring some compact, water-mediated conformations, with effects depending on native topology.
- **Caveat:** These are theoretical predictions about collapsibility, distinct from demonstrated folding, function, or experimentally measured pressure response.
- **Announcement type:** new submission, 2026-11-27 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

## Trending Research Themes

- **Coarse-grained models of biomolecular interactions:** Li & Chou (DNA-binding proteins), Agrawal (ternary complexes), Patri & Rani (peptidoglycan mechanics), and Wang et al. (protein collapse) use mathematical or computational models to connect molecular-scale rules with aggregate behavior. The selected corpus supports methodological interest, not a field-wide change or shared experimental validation.
- **Prediction and inference across biological contexts:** BiPert, KnitNet, the cell-type-expression analysis, and SpaDAG apply learning or statistical inference to perturbation responses, RNA structure, bulk deconvolution, and spatial gene relationships. Most evidence is benchmark- or model-based; the spatial-tumor result is hypothesis-generating.
- **Infrastructure for genomics:** Motivo targets the computational bottleneck of graph-based read mapping. Its evidence is systems benchmarking rather than a biological discovery.

## Open Problems and Research Directions

- **Test model assumptions against direct measurements.** For Li & Chou, measure occupancy and exchange kinetics across controlled diffusion rates and protein conformational states, then test where fast-diffusion reductions fail. For the Gaucher-disease model, pair donor-level adhesion assays with cell-by-cell total and phosphorylated Lu/BCAM measurements and report contact-density uncertainty; the paper itself identifies receptor-state assays as a discriminating test.
- **Move RNA inverse design from in-silico metrics to experimental checks.** For KnitNet, synthesize designs selected across easy, out-of-distribution, and pseudoknotted targets, then compare predicted structures with an independent in-vitro structure assay. This would test whether exact verifier matches transfer to measured folding.
- **Stress-test generalization in independent biological contexts.** Evaluate BiPert and cell-type deconvolution on held-out donors, cell states, and datasets with harmonized perturbation or single-cell references; for SpaDAG, use multiple spatial sections and orthogonal perturbations to test whether inferred direction reversals replicate. These are proposed validation steps, not clinical recommendations.

## Takeaway

This week’s most defensible story is methodological: several new models address how molecular interactions and gene-expression patterns behave under context changes. The candidate scores mostly reflect cross-list breadth, not demonstrated audience attention; recurring daily coverage adds continuity but does not establish popularity. Treat computational predictions as hypotheses until independent experimental and external-cohort validation is reported.

## Method and sources

- **Window:** Weekly, 2026-11-19 19:00:00Z through 2026-11-26 19:00:00Z (inclusive of the stated submission/revision window); the announcement batch was 2026-11-27 01:00:00Z. Snapshot: 2026-11-27 08:09:05Z UTC. All ten selected records are v1 new submissions inside this window.
- **Candidate pool:** The supplied signals file listed 79 arXiv candidates across `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`; its source statuses for arXiv (79), Hugging Face (336), Hacker News (67), arXiv lookup (398), and Semantic Scholar (79) were all `ok`. No source was marked unavailable. Counts are collector totals, not counts of papers or users.
- **Ranking:** External attention was sparse among the selected biology-relevant papers: their Hugging Face upvotes, Hacker News points/comments, and Semantic Scholar citation/influential-citation values were zero or unrecorded; each score is exactly its cross-list component. Scores of 0.75 correspond to three cross-lists × 0.25; 0.50 to two × 0.25. These numbers are the supplied transparent candidate scores, not a measure of popularity. Scores determined the first tier; ties were resolved by direct biological relevance and then the supplied daily-rollup continuity. The only candidate with a larger non-cross-list score was 2611.33702 (score 8.111; 34 Semantic Scholar citations), a small-robot locomotion paper with only a peripheral q-bio.QM cross-list, so it was excluded from this biology/biomedicine selection. Zero attention does not imply lack of importance.
- **Continuity:** The supplied daily rollup covered daily editions dated 2026-11-21 through 2026-11-27. The selected papers already featured were 2611.33740 (2 appearances, 26–27 Nov, best rank 1), 2611.27960 (2, 22–23 Nov, best rank 1), 2611.33812 (2, 26–27 Nov, best rank 1), and 2611.33753 (2, 26–27 Nov, best rank 3). The other six selected papers were not listed in that rollup. Recurrence is reported as continuity evidence, not used as an independent attention measure.
- **Verification:** Each selected paper’s canonical arXiv abstract page was fetched and checked against ID and title; current version, authors, dates, categories, and abstracts were checked against one arXiv API response. The introduction/results/discussion or limitations were also read for the top three where HTML full text was available. Semantic Scholar values come from the supplied signal file; citation totals are current snapshot values, not gains during this week. No paper in this report is represented as clinical guidance or practice-changing evidence.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`.
- **Sources:** [Signals JSON](file:///home/yizhuan/.research/bio/weekly/arxiv-trending-bio-weekly-2026-11-26.signals.json); [daily rollup JSON](file:///home/yizhuan/.research/bio/weekly/arxiv-trending-bio-weekly-2026-11-27.rollup.json); arXiv abstract links are provided on each paper title. This report covers arXiv only, not bioRxiv, medRxiv, or the wider biomedical literature.
