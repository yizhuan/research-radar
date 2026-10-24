# arXiv Biology and Biomedicine — Daily Report, 2026-10-23

## Headline

This daily snapshot covers the Friday 23 October 2026 announcement batch: 15 notable papers selected from 18 deduplicated candidates across the configured biology/biomedicine categories. The main patterns are computational RNA/protein design and prediction alongside medical-imaging and radiotherapy-planning methods. ArXiv has no official trending chart; citations and independent attention were too sparse to establish popularity, so this is an inferred relevance ranking, and arXiv omits much clinical and experimental biology published on bioRxiv, medRxiv and elsewhere. Snapshot: 2026-10-24 00:20 UTC.

## Notable recent papers

### 1. [RiboBridge: protein-conditioned de novo RNA binder structure design](https://arxiv.org/abs/2610.30668)
- **Abstract:** How can a protein-binding RNA structure be generated without specifying its binding site or relative pose?
- **Authors:** Zhou Zhang, Hanqun Cao, Minghao Sun, Odin Zhang, Yang Zhang, Pheng Ann Heng, Wujun Li, Tianfan Fu
- **arXiv:** `2610.30668v1` (published 2026-10-22T03:32:07Z; categories: `cs.LG, q-bio.BM`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations at snapshot; cross-listed from cs.LG into q-bio.BM, directly linking structure generation to molecular biology.
- **Claimed contribution:** The authors introduce a structure-first pipeline that proposes protein interfaces, generates RNA conformations in a pretrained RNA latent space, predicts cross-frame interaction constraints, and places the RNA as a rigid body. On a temporally split, sequence-filtered benchmark of 124 complexes, they report the best fNAT and DockQ and lowest interface/ligand RMSDs among compared methods; native interface correspondence is used only post hoc.
- **Caveat:** Structural-computational evidence, not experimental binding or function. The authors identify interface-hypothesis ranking and sequence realization as unresolved.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Biochemistry & proteins; RNA & transcriptomics; Bioinformatics & sequence analysis

### 2. [Benchmarking Recent Single-Cell Synthetic Data Generation Methods on the OneK1K Dataset](https://arxiv.org/abs/2610.31454)
- **Abstract:** Which single-cell RNA-seq synthesis choices preserve biological structure while limiting donor-membership leakage?
- **Authors:** Buse Giledereli, Basar Temiz, Amirreza Sattarzadeh Khanehbargh
- **arXiv:** `2610.31454v1` (published 2026-10-22T15:49:27Z; categories: `q-bio.GN`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; q-bio.GN paper whose arXiv comment notes presentation at the CAMDA 2026 ELSA Health Privacy Challenge.
- **Claimed contribution:** The authors compare scGFT, scLDM and Cell2Sentence on donor-split OneK1K data across fidelity, biological preservation and membership-inference risk. They report severe leakage when non-HVG values are copied, lower leakage with Poisson reconstruction, and near-random membership-inference profiles for tuned scGFT/scLDM configurations.
- **Caveat:** Generative modeling focuses on highly variable genes and reconstructs non-HVGs, reflecting stated time/computational limits. One dataset and empirical membership inference do not establish formal differential privacy or generalization.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Omics & single-cell methods; Bioinformatics & sequence analysis; Biomedical & translational medicine

### 3. [Supercoiling Drives DNA-Protein Co-Condensation](https://arxiv.org/abs/2610.30588)
- **Abstract:** How does DNA torsional stress alter protein-mediated condensation and genome compaction?
- **Authors:** Sihan Liu, Hongbo Zhao, Andrej Košmrlj
- **arXiv:** `2610.30588v1` (published 2026-10-22T01:42:38Z; categories: `physics.bio-ph, cond-mat.soft, q-bio.BM`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; cross-listed in q-bio.BM, physics.bio-ph and cond-mat.soft.
- **Claimed contribution:** Using a coupled DNA-elasticity/protein-concentration model and simulations, the authors propose that protein wetting promotes twist-to-writhe conversion, lowering the barrier to DNA–protein co-condensation under sufficient supercoiling.
- **Caveat:** The mechanism is theoretical/model-based, not an experimental demonstration in cells. Predictions depend on model parameters and require validation across relevant proteins and chromatin contexts.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** DNA & genomics; Molecular & cell biology; Quantitative methods

### 4. [Shorter but not more catalytic: an active-site-resolved model of how tau reshapes amyloid-$β$ secondary nucleation](https://arxiv.org/abs/2610.30531)
- **Abstract:** Does tau-induced shortening of amyloid-β fibrils necessarily increase secondary-nucleation activity?
- **Authors:** Andrey V. Kuznetsov
- **arXiv:** `2610.30531v1` (published 2026-10-21T23:33:32Z; categories: `q-bio.SC`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; q-bio.SC primary category and a focused molecular mechanism with parameter-sweep evidence.
- **Claimed contribution:** The author extends a tau–amyloid-β kinetic model to track fibril number, mass and exposed catalytic sites. Simulations suggest shortening alone has little effect at matched mass; site density/exposure and the balance between elongation-driven monomer consumption and clearance control the response. Analysis includes 800 Latin-hypercube samples and modeled fibril lengths of 0.3–30 μm.
- **Caveat:** A mechanistic model, not direct measurement of fibril catalytic sites or patient biology; conclusions depend on assumptions about active-site creation, exposure and monomer clearance.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 5. [Escaping the Phylogenetic Trap: Persistent Homology Enables Cross-Species Ion Channel Classification via Multimodal Graph Neural Networks](https://arxiv.org/abs/2610.30394)
- **Abstract:** Can structural representations improve venom-peptide ion-channel classification when entire taxa are held out?
- **Authors:** Arezoo Bybordi, Favour Achimba, Mariam Gelashvili, Jessy Ramirez, Weigang Qiu, Mandë Holford, Anita Raja
- **arXiv:** `2610.30394v1` (published 2026-10-21T19:59:07Z; categories: `cs.LG, q-bio.BM`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; cross-listed from cs.LG to q-bio.BM, with a taxon-held-out validation design.
- **Claimed contribution:** The authors combine ESM-2 sequence embeddings with structure-aware graph networks and compare five structural priors on 1,373 ColabFold-predicted venom compounds from five taxa. In leave-one-taxon-out evaluation, persistent homology reaches 63.4% mean accuracy, versus about 54–55% for other geometric priors and about 30% for a sequence-only baseline; ordinary random splits mask the gap.
- **Caveat:** Computational evidence based on predicted structures and five taxa; no experimental binding/activity validation. The authors flag multi-label channel promiscuity and richer structural/dynamic modeling as future work.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 6. [ProMORNA: An End-to-End Generative Framework for Full-Length mRNA Design](https://arxiv.org/abs/2605.01513)
- **Abstract:** Can a generative model design full-length mRNA candidates balancing predicted stability and translation?
- **Authors:** Zixi Shao, Tao Wang, Ye Shen, Tianyi Huang, Yibei Xiao
- **arXiv:** `2605.01513v2` (published 2026-05-02T16:05:51Z; updated 2026-10-21T13:02:48Z; categories: `cs.LG, cs.AI, q-bio.BM`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; substantive v2 update in the current batch, cross-listed across cs.LG, cs.AI and q-bio.BM, with three in-vitro assays.
- **Claimed contribution:** The v2 paper describes a BART-style model pretrained on over six million protein–mRNA pairs, then supervised fine-tuning and multi-objective reinforcement learning. The authors report in-silico Pareto-frontier gains and three independent in-vitro Fluc2P experiments: Candidate 2 had 3.33× the conventional benchmark’s 12–72 h reporter-activity AUC (Holm-adjusted P=0.01285); its estimated 1.29× advantage over the reported best GEMORNA candidate remained exploratory.
- **Caveat:** Reporter activity is not therapeutic efficacy, in-vivo performance or clinical evidence. The GEMORNA comparison is explicitly exploratory; this is a v2 revision of a May submission, not a new paper.
- **Announcement type:** revision, 2026-10-23
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Quantitative methods

### 7. [QProtFuse: Query-Guided Layer Fusion for Retrieval-Augmented Protein Function Prediction](https://arxiv.org/abs/2610.30180)
- **Abstract:** Can protein-language-model features from multiple layers improve query-conditioned retrieval for protein-function descriptions?
- **Authors:** Mianzhi Pan, Peishuo Liu, Yawen Ouyang, Botian Wang, Yiming Rong, Hao Zhou, Jianbing Zhang
- **arXiv:** `2610.30180v1` (published 2026-10-19T14:47:25Z; categories: `cs.IR, q-bio.QM`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; newly surfaced in q-bio.QM from cs.IR and directly concerns protein-function retrieval.
- **Claimed contribution:** The authors propose query-guided fusion of protein-language-model layers with joint protein/annotation retrieval objectives. On Prot-Inst-OOD they report 16.4% Recall@1 with annotation reranking and improved LLM-as-judge scores for generated descriptions.
- **Caveat:** Retrieval and LLM-judge results are benchmark-specific and do not experimentally validate function. First submitted 2026-10-19; it appears as a q-bio.QM cross-list on 2026-10-23, not a new submission or versioned revision.
- **Announcement type:** new q-bio.QM cross-list (original v1: 2026-10-19), 2026-10-23
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 8. [Global Convergence of Detailed Balanced Mass Action Systems](https://arxiv.org/abs/2610.30808)
- **Abstract:** Under what assumptions do positive trajectories in detailed-balanced mass-action systems converge to equilibrium?
- **Authors:** Haoran Lv, Chengjin Ni, Manqin Wang, Shenli He
- **arXiv:** `2610.30808v1` (published 2026-10-22T06:33:06Z; categories: `cs.LO, math.DS, q-bio.MN`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; cross-listed in q-bio.MN, math.DS and cs.LO, with a Lean 4 formalization noted in the arXiv comment.
- **Claimed contribution:** The authors prove a unique positive equilibrium in each positive stoichiometric compatibility class and convergence of every positive trajectory, alongside a Lean 4 formalization using a persistence/barrier argument, the Horn–Jackson dissipation identity and bounded-speed descent.
- **Caveat:** A mathematical theorem under finite detailed-balanced mass-action assumptions, not empirical evidence for a particular biochemical network; application depends on those assumptions holding.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Molecular & cell biology; Quantitative methods

### 9. [Direct Production of Ultra-High Radioisotopic Pure $^{64}$Cu from Natural Zinc Metal via D-D Fusion Narrowband Fast Neutron Source Irradiation](https://arxiv.org/abs/2610.31340)
- **Abstract:** Can copper-64 be produced from natural zinc using a controlled D-D fusion neutron source?
- **Authors:** Jeremy M. C. Brown, Mantas Grigalavicius, Tibor Gilinger, Adam Kovacs, Parvin Varmazyar, Hsin-Hui Huang, Saulius Juodkazis, Mikas Vengris, Darius Gailevicius, Karoly Osvay
- **arXiv:** `2610.31340v1` (published 2026-10-22T14:24:29Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; physics.med-ph paper with a direct radiopharmaceutical-production question and reported irradiation/spectroscopy.
- **Claimed contribution:** The authors irradiated high-purity natural zinc for one hour and used gamma spectroscopy over 72 hours. They report no other copper radioisotope detected and threshold-corrected copper-64 purity estimates of 99.62% and 99.97% under two reporting thresholds.
- **Caveat:** The abstract does not establish production yield, reproducible scale-up, full radiopharmaceutical manufacture or realized cost reduction; cost savings are prospective, not clinical outcomes.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 10. [AI Enhanced Cerenkov Luminescence Microscopy](https://arxiv.org/abs/2610.31240)
- **Abstract:** Can physics-based simulated training pairs restore spatial detail in Cerenkov luminescence microscopy of tumor spheroids?
- **Authors:** Stefano Pizzardi, Lisa Alborghetti, Caterina Lomazzi, Antonello Enrico Spinelli
- **arXiv:** `2610.31240v1` (published 2026-10-22T13:23:12Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; direct imaging paper with simulation benchmarking and a 27-spheroid image application.
- **Claimed contribution:** The authors train CARE on 15,360 Monte-Carlo-generated image pairs from 80 simulated spheroid geometries. They report lower synthetic-validation MSE than Noise2Void (0.0051 vs 0.0492) and apply the model to experimental images from 27 U87 spheroids, reporting more localized signal and higher local contrast/SNR.
- **Caveat:** Quantitative ground truth is simulated; 27 spheroids are an experimental image set, not in-vivo or patient validation. Results depend on simulator fidelity.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 11. [Geometry-Dependent Properties of Physically Crosslinked PPy-PVA Hydrogels Enable Tunable Iontophoretic Drug Delivery](https://arxiv.org/abs/2610.31567)
- **Abstract:** Can hydrogel geometry tune iontophoretic transport independently of changing current density?
- **Authors:** Heather Jin Hee Kim, Mohsen Alishahi, Kyuin Park, Mikaila K. Roncevich, Larissa M. Shepherd, Cara M. Nunez
- **arXiv:** `2610.31567v1` (published 2026-10-22T17:10:35Z; categories: `cs.RO, physics.med-ph`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; physics.med-ph paper with a DOI and geometry-controlled in-vitro membrane experiments.
- **Claimed contribution:** The authors compare five PPy-PVA hydrogel geometries containing bovine serum albumin, characterize microstructure/electric fields, and measure transport in Franz cells with artificial membranes. They report geometry-dependent release/permeability and greater permeability under iontophoresis than passive diffusion.
- **Caveat:** Experiments use artificial membranes and a model protein, not living skin, animals or people; the DOI is a publication identifier, not evidence of clinical effectiveness.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Biomedical & translational medicine; Molecular & cell biology

### 12. [Advancing oxygen-enhanced MRI acquisition and modelling through dynamic $ΔR_{1}$ and $ΔR_2^*$ sensing](https://arxiv.org/abs/2610.30793)
- **Abstract:** Can a reduced-acquisition fat/water MRI method quantify relaxation changes during an oxygen challenge?
- **Authors:** Jorge Campos Pazmiño, Amiel Beausoleil-Morrison, Nathalie Panov, Véronique Fortier, Ives R. Levesque
- **arXiv:** `2610.30793v1` (published 2026-10-22T06:16:41Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; physics.med-ph paper with phantom and explicitly sized in-vivo pilot evaluations.
- **Claimed contribution:** The authors introduce SR-Fat DESPOT, optimize sequence settings by Cramér–Rao analysis, and report phantom accuracy plus in-vivo measurements under 100% oxygen in one test–retest participant and a six-participant pilot. Spleen and kidney changes were statistically significant in that pilot.
- **Caveat:** The in-vivo sample is small and evaluates a gas-challenge measurement method, not a validated diagnostic or clinical outcome; larger independent cohorts are needed.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 13. [Comparing local and global optimization reveals untapped hybrid potentials for machine learning-based inverse planning](https://arxiv.org/abs/2610.30424)
- **Abstract:** How do global and local optimization approaches compare when embedding complication-risk models into radiotherapy planning?
- **Authors:** Tim Ortkamp, Florian Leininger, Zhongxing Liao, Niklas Wahl, Ali Ajdari
- **arXiv:** `2610.30424v1` (published 2026-10-21T20:33:02Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; physics.med-ph comparison with 15 defined planning cases and a hybrid-optimization result.
- **Claimed contribution:** The authors compare OptiCL and pyanno4rt across eight head-and-neck photon cases and seven lung proton cases, report broadly similar dose plans with different runtimes, and test hybrid strategies; one decision-tree-based hybrid reduces binary variables by 80% without reported plan-quality loss.
- **Caveat:** A planning comparison on 15 cases with predicted NTCP, not prospective evidence of toxicity reduction or improved patient outcomes.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 14. [LieGROG: A Lie algebra approach for calibrating GRAPPA operators](https://arxiv.org/abs/2610.30927)
- **Abstract:** Can Lie-algebra calibration improve GRAPPA-operator gridding for non-Cartesian MRI?
- **Authors:** Tobias Wech
- **arXiv:** `2610.30927v1` (published 2026-10-22T08:45:35Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; physics.med-ph method with scan comparisons and measured runtime/memory results.
- **Claimed contribution:** The author estimates a joint generator for GRAPPA operators and compares LieGROG with classical calibration and NUFFT/Toeplitz references across simulations and 2D/3D MR scans. The abstract reports reduced noise amplification, similar reconstructions, 6–189× faster runtimes and 20–45% lower peak VRAM in 3D experiments.
- **Caveat:** This is reconstruction/compute benchmarking, not diagnostic accuracy or patient-outcome evidence. The arXiv comment says the work was submitted to Magnetic Resonance in Medicine, not accepted.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Medical physics & imaging; Quantitative methods

### 15. [Unified Projection-Domain Material Decomposition for Energy-Integrating and Photon-Counting CT](https://arxiv.org/abs/2610.30440)
- **Abstract:** Can one projection-domain decomposition method use multiple spectral measurements across different CT acquisition systems?
- **Authors:** Dale Black, Surya Naidu, Hamidreza Khodajou-Chokami, Sabee Molloi
- **arXiv:** `2610.30440v1` (published 2026-10-21T20:49:51Z; categories: `eess.IV, physics.med-ph`)
- **Evidence for ranking:** Semantic Scholar Graph: 0 citations and 0 influential citations; cross-listed in eess.IV and physics.med-ph, with tests spanning three named CT systems.
- **Claimed contribution:** The authors formulate nested optimization for two-material decomposition from at least two spectral measurements and test energy-integrating and photon-counting CT. They report noiseless line-integral errors below 3×10⁻⁶ g/cm² and noise within 3% of the Cramér–Rao bound; four rather than two photon-counting measurements reduce iodine CRLB by 19%.
- **Caveat:** Evidence is mainly simulation and comparison with vendor reconstructions, not improved diagnosis or patient outcomes; performance depends on tested scanner models and basis assumptions.
- **Announcement type:** new submission, 2026-10-23
- **Themes:** Medical physics & imaging; Quantitative methods

## Trending Research Themes

**Molecular modeling and sequence-to-function tools.** RiboBridge, Escaping the Phylogenetic Trap, QProtFuse and the v2 ProMORNA report computational approaches spanning protein–RNA structure generation, cross-taxon peptide classification, protein-function retrieval and mRNA design. Evidence ranges from structural benchmarks to in-vitro reporter assays; these are not interchangeable levels of validation.

**Molecular mechanisms and formal models.** Supercoiling Drives DNA-Protein Co-Condensation and the tau/amyloid-β model use theoretical or simulation-based accounts of condensation and nucleation; Global Convergence of Detailed Balanced Mass Action Systems contributes a formal theorem rather than an experimental pathway study. This is modeling activity in the selected batch, not evidence of a field-wide shift.

**Medical imaging and treatment-planning methods.** AI Enhanced Cerenkov Luminescence Microscopy, the oxygen-enhanced MRI study, LieGROG, CT material decomposition and inverse planning address reconstruction, acquisition or optimization. Their evidence is simulation/phantom, small in-vitro/in-vivo pilot data or planning cases—not clinical benefit.

**Single-cell privacy is a focused result, not a recurring theme in this small batch.** The OneK1K benchmark shows why privacy auditing must include non-HVG handling as well as fidelity (2610.31454).

## Open Problems and Research Directions

**Model-to-experiment validation.** RiboBridge reports complex-structure recovery on 124 benchmarks but not direct binding assays. Follow-up could synthesize a blinded subset of candidates, quantify affinity and specificity, and test whether predicted interface ranking tracks activity; this addresses the authors’ stated interface-ranking and sequence-realizability limits.

**Generalizable privacy evaluation.** The OneK1K study centers on one donor-split dataset and membership-inference metrics. A useful follow-up is a held-out-cohort comparison across tissues and platforms, with explicit privacy guarantees and attacks after the complete preprocessing/post-processing pipeline; distinguish formal guarantees from empirical attack resistance.

**Test molecular-model predictions.** The supercoiling and tau/amyloid papers make testable predictions about condensation barriers and active-site density. Experiments could vary DNA linking density and protein concentration while measuring droplet nucleation, then compare fibrils at matched mass with direct site-counting and secondary-nucleation assays. These are informed synthesis proposals, not established mechanisms.

**Validate imaging and delivery beyond proxies.** Cerenkov restoration should be tested on independent acquisition settings and reference structures; the oxygen-MRI pilot needs larger test–retest cohorts; hydrogel transport needs biological-barrier validation. CT decomposition and radiotherapy-planning methods need external-case or phantom-to-clinic validation before claims about patient outcomes.

## Takeaway

This batch is notable for its mix of molecular-modeling papers and practical medical-physics methods, not measurable popularity: Semantic Scholar reported zero citations and zero influential citations for every selected paper at the snapshot. Evidence is mixed—mostly in-silico benchmarks, with a few in-vitro or small pilot experiments—and none alone establishes clinical effectiveness.

## Method and sources

**Window:** daily; announcement batch 2026-10-23; date range 2026-10-23 through 2026-10-23; snapshot 2026-10-24T00:20:05Z. At the UTC snapshot on Saturday 24 October, no 24 October announcement batch was available, so this daily report uses the prior Friday 23 October batch.
**Candidate scope/query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`. Category recent listings were checked for the batch; a broad arXiv API query returned 200 records and extended back to 2026-10-05, beyond the selected daily window. Cross-listed records were deduplicated by versionless arXiv ID, and all 15 retained abstract pages were verified. Eighteen distinct records appeared in the traversed listings; three peripheral items (a general AI protocol, drought-stress detection without a clear molecular/medical question, and generic dynamical inference) were excluded for scope.
**Ranking:** arXiv publishes no official trend or readership ranking. Semantic Scholar Graph reported 0 citations and 0 influential citations for all 15 selected papers at this snapshot; citation totals are not period gains. Searches did not establish enough current independent technical discussion to rank by attention. The list is therefore titled “Notable recent papers” and ordered by direct molecular/biomedical relevance and reported evidence, using recency only as a tie-breaker. One entry is a substantive v2 revision; QProtFuse is marked as a q-bio.QM cross-list rather than a new submission. No downloads or views are inferred.
**Coverage caveat:** arXiv is not a representative biomedical index; many experimental and clinical preprints appear on bioRxiv or medRxiv, and this report is not a survey of those repositories or the medical literature.
**Sources:** [arXiv q-bio recent listings](https://arxiv.org/list/q-bio/recent), [cs.BI API query](https://export.arxiv.org/api/query?search_query=cat%3Acs.BI&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200), [physics.med-ph recent listing](https://arxiv.org/list/physics.med-ph/recent), [arXiv API](https://export.arxiv.org/api/query), [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2610.30668?fields=title,citationCount,influentialCitationCount,referenceCount,publicationTypes,fieldsOfStudy,externalIds). Individual arXiv abstract links appear with each paper.
