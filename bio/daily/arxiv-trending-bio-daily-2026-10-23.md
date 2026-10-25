# arXiv Biology and Biomedicine — Daily Report, 2026-10-23

## Headline

The latest relevant announcement batch is Friday 23 October 2026: 18 unique candidates were found across the configured biology/biomedicine listings, and 15 are included here. RNA/protein design and sequence/structure evaluation recur alongside molecular-model studies and translational imaging or radiochemistry methods. The agenda is to distinguish computational predictions from biochemical, tissue, phantom and small-cohort evidence. arXiv has no official trending chart; this relevance-ranked selection is inferred from one announcement batch and incomplete arXiv biomedical coverage, not a popularity measure. Many experimental and clinical preprints appear on bioRxiv or medRxiv instead.

## Notable recent papers (relevance-ranked)

### 1. [RiboBridge: protein-conditioned de novo RNA binder structure design](https://arxiv.org/abs/2610.30668)
- **Abstract:** RiboBridge generates candidate RNA conformations and assembles protein–RNA complexes through predicted cross-frame interaction geometry, without assuming a binding site.
- **Authors:** Zhou Zhang, Hanqun Cao, Minghao Sun, Odin Zhang, Yang Zhang, Pheng Ann Heng, Wujun Li, Tianfan Fu
- **arXiv:** `2610.30668v1` (published 2026-10-22T03:32:07Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** The authors compare methods on 124 temporally split, sequence-filtered protein–RNA complexes; RiboBridge reports the best complex-recovery metrics and DockQ ≥0.23 for 20/124 targets (16.13%). It is cross-listed in machine learning and biomolecules.
- **Claimed contribution:** The authors propose a structure-first pipeline that predicts interface hypotheses, generates RNA in a pretrained structural latent space, and uses predicted interaction constraints to place it relative to the protein.
- **Caveat:** This is computational structure recovery, not experimental binding or activity validation. Native interface information is used after generation for candidate correspondence; the authors identify interface prioritization and sequence realization as remaining challenges.
- **Announcement type:** new submission (also cross-listed in q-bio.BM), announcement batch 2026-10-23
- **Themes:** Biochemistry & proteins; RNA & transcriptomics

### 2. [ProMORNA: An End-to-End Generative Framework for Full-Length mRNA Design](https://arxiv.org/abs/2605.01513)
- **Abstract:** ProMORNA generates full-length mRNA from a target protein sequence and reports improved predicted stability/translation trade-offs plus higher reporter activity in three independent Fluc2P experiments.
- **Authors:** Zixi Shao, Tao Wang, Ye Shen, Tianyi Huang, Yibei Xiao
- **arXiv:** `2605.01513v2` (published 2026-05-02T16:05:51Z; revised 2026-10-21T13:02:48Z; categories: `cs.LG`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** The v2 revision appeared in this announcement batch. The authors tested seven selected candidates in three independent in-vitro Fluc2P experiments; Candidate 2 had 3.33× the 12–72-hour reporter-activity AUC of the conventional benchmark (Holm-adjusted P=0.01285).
- **Claimed contribution:** The authors introduce a BART-style, end-to-end mRNA generator pretrained on over six million natural protein–mRNA pairs and post-trained with supervised learning and multi-objective reinforcement learning.
- **Caveat:** Prospective testing covered seven selected candidates for one reporter protein. The reported 1.29× advantage over the best GEMORNA candidate is exploratory; reporter activity does not directly measure mRNA stability or translation efficiency.
- **Announcement type:** revision (v2; first submitted 2026-05-02), announcement batch 2026-10-23
- **Themes:** RNA & transcriptomics; Biomedical & translational medicine

### 3. [Benchmarking Recent Single-Cell Synthetic Data Generation Methods on the OneK1K Dataset](https://arxiv.org/abs/2610.31454)
- **Abstract:** The authors compare scGFT, scLDM and Cell2Sentence for single-cell RNA-seq fidelity, biological-structure preservation and membership-inference risk on donor-split OneK1K data.
- **Authors:** Buse Giledereli, Basar Temiz, Amirreza Sattarzadeh Khanehbargh
- **arXiv:** `2610.31454v1` (published 2026-10-22T15:49:27Z; categories: `q-bio.GN`)
- **Evidence for ranking:** The study uses 633,711 training cells from 490 donors and 634,022 test cells from 491 donors, and the arXiv record notes its presentation at the CAMDA 2026 ELSA Health Privacy Challenge. The authors show that copying non-HVG expression can leak membership while Poisson reconstruction reduces that risk.
- **Claimed contribution:** The authors benchmark three synthetic single-cell generators across statistical fidelity, downstream biological structure and membership-inference vulnerability, highlighting how non-HVG processing changes the privacy–utility balance.
- **Caveat:** Generative modeling focused on highly variable genes and one donor-linked dataset. Different fidelity and privacy metrics disagree, and the authors note that filtering and metric assumptions affect interpretation.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Biomedical & translational medicine

### 4. [Supercoiling Drives DNA-Protein Co-Condensation](https://arxiv.org/abs/2610.30588)
- **Abstract:** A coupled DNA-elasticity and protein-concentration model predicts that supercoiling can promote protein wetting and DNA–protein co-condensation by lowering a nucleation barrier.
- **Authors:** Sihan Liu, Hongbo Zhao, Andrej Košmrlj
- **arXiv:** `2610.30588v1` (published 2026-10-22T01:42:38Z; categories: `physics.bio-ph`, `cond-mat.soft`, `q-bio.BM`)
- **Evidence for ranking:** Cross-listed in biological physics, soft matter and biomolecules; the paper combines simulations and a reduced theoretical energy landscape to analyze supercoiling-dependent condensation kinetics.
- **Claimed contribution:** The authors propose a cooperative mechanism in which protein wetting promotes twist-to-writhe conversion and writhed DNA in turn facilitates capillary collapse.
- **Caveat:** The findings are model-based and do not experimentally establish this pathway in cells or its quantitative importance in vivo.
- **Announcement type:** new submission (also cross-listed in q-bio.BM), announcement batch 2026-10-23
- **Themes:** DNA & genomics; Molecular & cell biology

### 5. [Shorter but not more catalytic: an active-site-resolved model of how tau reshapes amyloid-$\beta$ secondary nucleation](https://arxiv.org/abs/2610.30531)
- **Abstract:** A coupled tau–amyloid-β model tracks fibril mass, number and active secondary-nucleation sites to test when shorter fibrils change catalytic activity.
- **Authors:** Andrey V. Kuznetsov
- **arXiv:** `2610.30531v1` (published 2026-10-21T23:33:32Z; categories: `q-bio.SC`)
- **Evidence for ranking:** The model explores 800 Latin-hypercube samples and mean fibril lengths from 0.3 to 30 μm; it predicts that fibril shortening alone need not increase catalytic activity.
- **Claimed contribution:** The author identifies active-site density and exposure, together with the balance between monomer clearance and elongation, as key controls on modeled secondary nucleation.
- **Caveat:** This is a mechanistic model, not a new biochemical measurement. Its predictions need comparison with matched-mass fibril assays and direct measurements of active-site accessibility.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Biochemistry & proteins; Molecular & cell biology

### 6. [Escaping the Phylogenetic Trap: Persistent Homology Enables Cross-Species Ion Channel Classification via Multimodal Graph Neural Networks](https://arxiv.org/abs/2610.30394)
- **Abstract:** A multimodal graph model combines protein sequence and structural features to classify venom ion-channel targets under leave-one-taxon-out evaluation.
- **Authors:** Arezoo Bybordi, Favour Achimba, Mariam Gelashvili, Jessy Ramirez, Weigang Qiu, Mandë Holford, Anita Raja
- **arXiv:** `2610.30394v1` (published 2026-10-21T19:59:07Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** The reported benchmark spans 1,373 ColabFold-predicted venom compounds across five taxa; PH-GNN reaches 63.4% in taxon-held-out evaluation versus 54–55% for the next geometric priors. It is cross-listed in machine learning and biomolecules.
- **Claimed contribution:** The authors argue that persistent-homology structural features improve generalization under phylogenetic distribution shift compared with the tested alternatives.
- **Caveat:** This is computational classification over predicted structures, not experimental toxin–channel binding or functional validation; results are specific to the benchmark and split.
- **Announcement type:** new submission (also cross-listed in q-bio.BM), announcement batch 2026-10-23
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 7. [QProtFuse: Query-Guided Layer Fusion for Retrieval-Augmented Protein Function Prediction](https://arxiv.org/abs/2610.30180)
- **Abstract:** QProtFuse uses a query-conditioned fusion of protein-language-model layers to improve retrieval of proteins and annotations for function-description systems.
- **Authors:** Mianzhi Pan, Peishuo Liu, Yawen Ouyang, Botian Wang, Yiming Rong, Hao Zhou, Jianbing Zhang
- **arXiv:** `2610.30180v1` (published 2026-10-19T14:47:25Z; categories: `cs.IR`, `q-bio.QM`)
- **Evidence for ranking:** The arXiv recent listing adds this cs.IR paper to q-bio.QM in the 23 October batch; the authors report 16.4% annotation Recall@1 with reranking on Prot-Inst-OOD.
- **Claimed contribution:** The authors jointly learn protein and annotation retrieval using query-guided multi-layer features and intra-/cross-modal contrastive objectives.
- **Caveat:** Evidence is computational and benchmark-specific. LLM-as-a-judge scores for generated descriptions are not experimental evidence that predicted functions are correct.
- **Announcement type:** new cross-list into q-bio.QM (paper v1 first submitted 2026-10-19), announcement batch 2026-10-23
- **Themes:** Bioinformatics & sequence analysis; Biochemistry & proteins

### 8. [Global Convergence of Detailed Balanced Mass Action Systems](https://arxiv.org/abs/2610.30808)
- **Abstract:** The authors give a Lean 4-formalized proof that positive trajectories in finite detailed-balanced mass-action systems converge to a unique positive equilibrium in each positive compatibility class.
- **Authors:** Haoran Lv, Chengjin Ni, Manqin Wang, Shenli He
- **arXiv:** `2610.30808v1` (published 2026-10-22T06:33:06Z; categories: `cs.LO`, `math.DS`, `q-bio.MN`)
- **Evidence for ranking:** Cross-listed in logic, dynamical systems and molecular networks; the authors report a machine-checked Lean 4 proof and provide a public formalization.
- **Claimed contribution:** The paper supplies a proof of boundedness, persistence, equilibrium uniqueness and global convergence for the stated detailed-balanced reaction-network class.
- **Caveat:** The theorem is limited to finite deterministic detailed-balanced systems with positive rate constants; it is not evidence about stochastic, noisy, non-detailed-balanced or experimentally measured networks.
- **Announcement type:** new submission (also cross-listed in q-bio.MN), announcement batch 2026-10-23
- **Themes:** Molecular & cell biology; Quantitative methods

### 9. [Geometry-Dependent Properties of Physically Crosslinked PPy-PVA Hydrogels Enable Tunable Iontophoretic Drug Delivery](https://arxiv.org/abs/2610.31567)
- **Abstract:** Five BSA-loaded PPy-PVA hydrogel geometries are compared for iontophoretic transport using Franz diffusion cells with artificial membranes.
- **Authors:** Heather Jin Hee Kim, Mohsen Alishahi, Kyuin Park, Mikaila K. Roncevich, Larissa M. Shepherd, Cara M. Nunez
- **arXiv:** `2610.31567v1` (published 2026-10-22T17:10:35Z; categories: `cs.RO`, `physics.med-ph`)
- **Evidence for ranking:** The authors fabricated five geometries and report different transport profiles; the arXiv record includes DOI 10.1109/TBME.2026.3744496.
- **Claimed contribution:** The authors propose geometry as a way to tune hydrogel microstructure, local electric fields and transdermal transport without individually changing current density.
- **Caveat:** The payload was bovine serum albumin and testing used artificial membranes; this does not establish therapeutic delivery through intact skin or in-vivo efficacy.
- **Announcement type:** new submission (cross-listed in physics.med-ph), announcement batch 2026-10-23
- **Themes:** Biomedical & translational medicine; Molecular & cell biology

### 10. [Direct Production of Ultra-High Radioisotopic Pure $^{64}$Cu from Natural Zinc Metal via D-D Fusion Narrowband Fast Neutron Source Irradiation](https://arxiv.org/abs/2610.31340)
- **Abstract:** The authors report producing carrier-free copper-64 from natural zinc using a D–D fusion neutron source and assessing the irradiated sample by time-resolved gamma spectroscopy.
- **Authors:** Jeremy M. C. Brown, Mantas Grigalavicius, Tibor Gilinger, Adam Kovacs, Parvin Varmazyar, Hsin-Hui Huang, Saulius Juodkazis, Mikas Vengris, Darius Gailevicius, Karoly Osvay
- **arXiv:** `2610.31340v1` (published 2026-10-22T14:24:29Z; categories: `physics.med-ph`)
- **Evidence for ranking:** The reported experiment used one hour of irradiation and 72 hours of spectroscopy; the authors report 99.62% radioisotopic purity, or 99.97% after minimum-detection-activity correction.
- **Claimed contribution:** The authors present a potential alternative 64Cu production route intended to reduce reliance on enriched nickel targets.
- **Caveat:** This is a production experiment, not a radiopharmaceutical formulation, animal study or clinical evaluation; reproducibility, scale-up and application-specific suitability are not established here.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 11. [AI Enhanced Cerenkov Luminescence Microscopy](https://arxiv.org/abs/2610.31240)
- **Abstract:** A Monte-Carlo-guided CARE network restores simulated Cerenkov microscopy images and is applied to images from 27 radiotracer-exposed U87 tumor spheroids.
- **Authors:** Stefano Pizzardi, Lisa Alborghetti, Caterina Lomazzi, Antonello Enrico Spinelli
- **arXiv:** `2610.31240v1` (published 2026-10-22T13:23:12Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Training used 15,360 simulated image pairs from 80 spheroid geometries; synthetic-validation MSE was 0.0051 versus 0.0492 for Noise2Void, followed by application to 27 experimental spheroids.
- **Claimed contribution:** The authors propose physics-guided image restoration to reduce noise and positron-induced blur in 3D Cerenkov luminescence microscopy.
- **Caveat:** Quantitative ground-truth comparison is on simulations; spheroid results are image-quality comparisons, not independent ground-truth recovery or in-vivo/clinical validation.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 12. [Advancing oxygen-enhanced MRI acquisition and modelling through dynamic $\Delta R_{1}$ and $\Delta R_2^*$ sensing](https://arxiv.org/abs/2610.30793)
- **Abstract:** SR-Fat DESPOT combines fat–water-separated MRI acquisition with dynamic relaxation-rate modeling and is tested in a numerical phantom and small in-vivo studies.
- **Authors:** Jorge Campos Pazmiño, Amiel Beausoleil-Morrison, Nathalie Panov, Véronique Fortier, Ives R. Levesque
- **arXiv:** `2610.30793v1` (published 2026-10-22T06:16:41Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Evaluation includes a numerical phantom, one-participant test–retest experiment and a six-participant pilot during 100% oxygen breathing; the authors report significant spleen and kidney changes.
- **Claimed contribution:** The authors propose a lower-acquisition approach to quantify fat- and water-specific baseline and gas-challenge-related relaxation changes.
- **Caveat:** In-vivo evidence is a six-person pilot plus one repeatability participant; diagnostic performance, generalizability and clinical utility are not established.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 13. [LieGROG: A Lie algebra approach for calibrating GRAPPA operators](https://arxiv.org/abs/2610.30927)
- **Abstract:** LieGROG estimates non-Cartesian GRAPPA-operator generators through a joint Lie-algebra fit and evaluates MRI reconstruction against classical GROG and NUFFT/Toeplitz methods.
- **Authors:** Tobias Wech
- **arXiv:** `2610.30927v1` (published 2026-10-22T08:45:35Z; categories: `physics.med-ph`)
- **Evidence for ranking:** The authors report close reconstruction agreement, 6–189× faster runtimes and 20–45% lower peak VRAM in 3D experiments; the arXiv comment says it was submitted to Magnetic Resonance in Medicine.
- **Claimed contribution:** The method aims to make GROG calibration more robust across non-Cartesian trajectories while reducing reconstruction cost.
- **Caveat:** Evidence is from simulations and MRI reconstruction comparisons, not diagnostic accuracy or improved patient outcomes; the journal submission is not an acceptance claim.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Medical physics & imaging; Quantitative methods

### 14. [Unified Projection-Domain Material Decomposition for Energy-Integrating and Photon-Counting CT](https://arxiv.org/abs/2610.30440)
- **Abstract:** A nested-optimization method performs spectral CT material decomposition with two or more measurements without reducing data to two effective energies.
- **Authors:** Dale Black, Surya Naidu, Hamidreza Khodajou-Chokami, Sabee Molloi
- **arXiv:** `2610.30440v1` (published 2026-10-21T20:49:51Z; categories: `eess.IV`, `physics.med-ph`)
- **Evidence for ranking:** The authors evaluate three scanner configurations; report noiseless iodine error below 3×10⁻⁶ g/cm², noise near the Cramér–Rao bound, agreement with physical-scan/vendor images and 0.34–0.67 seconds per million rays on an A100 GPU.
- **Claimed contribution:** The method uses all spectral measurements in a Poisson-likelihood-based decomposition and is designed to work across energy-integrating and photon-counting acquisition.
- **Caveat:** Validation is primarily simulation and phantom/reference-image comparison; no patient-level diagnostic or clinical outcome study is reported.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Medical physics & imaging; Quantitative methods

### 15. [Comparing local and global optimization reveals untapped hybrid potentials for machine learning-based inverse planning](https://arxiv.org/abs/2610.30424)
- **Abstract:** The authors compare global mixed-integer and local differentiable optimization for machine-learning-based radiotherapy inverse planning, including hybrid strategies.
- **Authors:** Tim Ortkamp, Florian Leininger, Zhongxing Liao, Niklas Wahl, Ali Ajdari
- **arXiv:** `2610.30424v1` (published 2026-10-21T20:33:02Z; categories: `physics.med-ph`)
- **Evidence for ranking:** The comparison uses eight head-and-neck photon cases and seven lung proton cases; the authors report broadly similar dose distributions and an 80% reduction in binary decision variables for one hybrid decision-tree-based plan.
- **Claimed contribution:** The authors identify warm starts, stronger constraints and pruning as ways to combine global guarantees with local-optimization speed.
- **Caveat:** The evaluation is limited to 15 treatment plans and predicted normal-tissue complication probabilities; it does not show prospective clinical benefit or improved patient outcomes.
- **Announcement type:** new submission, announcement batch 2026-10-23
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

## Trending Research Themes

This batch clusters around four topics, not evidence of field-wide shifts. RNA design and sequence-to-function methods appear in RiboBridge and ProMORNA; they address different tasks, and only ProMORNA reports in-vitro reporter experiments. Evaluation robustness recurs in the OneK1K privacy benchmark, cross-species ion-channel classification and QProtFuse protein-function retrieval, each with different data and metrics. Molecular organization and aggregation are addressed by the supercoiling–condensation model, the tau/amyloid model and a formal result for detailed-balanced reaction networks; these are model/theory claims rather than new biological discoveries. Finally, Cerenkov microscopy, oxygen-enhanced MRI, LieGROG, spectral CT, inverse planning, hydrogel delivery and 64Cu production form a medical-physics and translational-method cluster, with evidence ranging from simulations and artificial membranes to spheroids and a six-person pilot.

## Open Problems and Research Directions

The authors of RiboBridge identify interface-hypothesis prioritization and sequence realization as bottlenecks; a useful follow-up is prospective, blinded synthesis and binding/function assays across protein families, with no native-interface selection at evaluation time. The OneK1K benchmark is restricted to highly variable genes and one donor-linked cohort; repeat privacy attacks and biological-utility metrics on independent tissues, platforms and donor cohorts, including full-gene outputs, would test whether its trade-offs generalize. ProMORNA's authors note that validation covers seven candidates and one reporter protein; follow-up could test longer transcripts and diverse targets while measuring reporter expression, mRNA stability and translation separately against independent baselines. For the supercoiling and tau/amyloid models, matched-condition biochemical experiments could vary DNA linking number/protein concentration or quantify fibril active sites at matched mass and length. Imaging and delivery methods would benefit from held-out physical phantoms, independent spheroid models, broader membrane/payload testing and larger repeatability cohorts; none of these proposals is clinical advice or a claim of demonstrated feasibility.

## Takeaway

This batch is notable for computational RNA/protein design and carefully scoped biomedical measurement methods, not for a measured popularity surge. ProMORNA offers the clearest in-vitro bridge, while RiboBridge, privacy-aware single-cell synthesis and protein-function models remain benchmark evidence. The medical-physics papers span simulations, artificial-membrane assays, spheroids and a very small MRI pilot; none establishes clinical benefit. Read the evidence level, not the title, as the guide to what is ready for follow-up.

## Method and sources

- **Window:** daily, 2026-10-23 through 2026-10-23. Snapshot: 2026-10-25T17:20:57Z. The current day was Sunday with no newer relevant batch; this uses the prior Friday 23 October announcement batch.
- **Candidate pool:** 18 unique arXiv IDs were deduplicated across the configured recent listings. The `q-bio.CB` and `q-bio.TO` pages had no entries in the 23 October batch; the configured `cs.BI` code yielded no identifiable batch entry. Fifteen papers are shown, selected for the most direct molecular or biomedical relevance; three adjacent cross-listed items were not included. The 15 selected abstract pages and metadata were checked, and the top three were read beyond their abstracts using the arXiv full-text PDFs.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date; cross-listed papers were deduplicated by versionless arXiv ID. Daily announcement dates come from arXiv recent category listings; the arXiv `published` timestamp is reported separately. One cross-list event (QProtFuse) is labeled as such, and the ProMORNA v2 update is labeled as a revision.
- **Ranking:** no verified citation-velocity or independent attention signal supported a popularity ordering for this just-announced batch. Papers are ranked by direct fit to molecular biology/biomedicine and specificity of reported evaluation; publication status, revision timing and cross-list breadth are supplementary signals. Citation totals, downloads and views are not claimed.
- **Primary sources:** [q-bio.BM recent](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN recent](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN recent](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC recent](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB recent](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO recent](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM recent](https://arxiv.org/list/q-bio.QM/recent), [physics.med-ph recent](https://arxiv.org/list/physics.med-ph/recent); each selected paper’s linked arXiv abstract. Full-text reads: [RiboBridge](https://arxiv.org/pdf/2610.30668v1), [ProMORNA v2](https://arxiv.org/pdf/2605.01513v2), [OneK1K benchmark](https://arxiv.org/pdf/2610.31454v1). The CAMDA benchmark context is at [ELSA Health Privacy Challenge](https://benchmarks.elsa-ai.eu/?ch=4&com=track2).
