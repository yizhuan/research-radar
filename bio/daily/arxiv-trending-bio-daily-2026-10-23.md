# arXiv Biology and Biomedicine — Daily Report, 2026-10-23

## Headline

This prior announcement batch yielded 12 notable papers from an 18-paper candidate pool. The strongest pattern is computational design and evaluation of RNA/protein systems, alongside early translational methods in imaging and radiochemistry. The agenda is mRNA and RNA–protein design, privacy-aware single-cell synthesis, molecular modeling, and biomedical measurement. This is a relevance-ranked inference, not an official arXiv trending chart: arXiv has no official popularity ranking, and its biology/biomedicine corpus is incomplete—many clinical and experimental preprints appear on bioRxiv or medRxiv instead.

## Notable recent papers

### 1. [ProMORNA: An End-to-End Generative Framework for Full-Length mRNA Design](https://arxiv.org/abs/2605.01513)
- **Abstract:** ProMORNA generates full-length mRNA from a target protein sequence and reports improved in-silico stability/translation trade-offs plus higher reporter activity in three independent Fluc2P experiments.
- **Authors:** Zixi Shao, Tao Wang, Ye Shen, Tianyi Huang, Yibei Xiao
- **arXiv:** `2605.01513v2` (first submitted 2026-05-02 16:05:51 UTC; revised 2026-10-21 13:02:48 UTC; categories: `cs.LG` (primary), `cs.AI`, `q-bio.BM` (cross-lists))
- **Evidence for ranking:** A substantive v2 revision appeared in this batch; the authors report three independent in-vitro Fluc2P experiments and a Holm-adjusted 3.33× activity-AUC ratio for one candidate versus the conventional benchmark. Ranked for direct mRNA-design relevance and reported evidence, not measured popularity.
- **Claimed contribution:** The authors propose a zero-shot, end-to-end generator trained on more than six million protein–mRNA pairs, with supervised and multi-objective reinforcement-learning post-training.
- **Caveat:** Wet-lab testing covered seven selected candidates for one reporter protein. Candidate 2's 1.29× comparison with the reported best GEMORNA candidate did not remain significant after correction; reporter activity is not a direct measurement of mRNA stability or translation efficiency.
- **Announcement type:** revision, 2026-10-23 batch (v2; first submitted 2026-05-02)
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Quantitative methods

### 2. [RiboBridge: protein-conditioned de novo RNA binder structure design](https://arxiv.org/abs/2610.30668)
- **Abstract:** RiboBridge separates RNA-conformation generation from protein-relative assembly and predicts RNA–protein complex structures without a predefined binding site.
- **Authors:** Zhou Zhang, Hanqun Cao, Minghao Sun, Odin Zhang, Yang Zhang, Pheng Ann Heng, Wujun Li, Tianfan Fu
- **arXiv:** `2610.30668v1` (published 2026-10-22 03:32:07 UTC; categories: `cs.LG` (primary), `q-bio.BM` (cross-list))
- **Evidence for ranking:** Evaluated against existing methods on a temporally split, sequence-filtered and redundancy-controlled set of 124 protein–RNA complexes; authors report 20/124 targets reaching DockQ ≥ 0.23. Cross-listed in machine learning and biomolecules.
- **Claimed contribution:** The authors use a pretrained RNA structural latent space, predicted protein-surface interface hypotheses, and cross-frame interaction geometry to assemble candidate complexes.
- **Caveat:** The benchmark measures predicted structure recovery, not measured binding or biological activity; native interface information is used post hoc to select among already generated candidates, and the authors identify interface prioritization and sequence realization as unresolved.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** RNA & transcriptomics; Biochemistry & proteins; Quantitative methods

### 3. [Benchmarking Recent Single-Cell Synthetic Data Generation Methods on the OneK1K Dataset](https://arxiv.org/abs/2610.31454)
- **Abstract:** The authors compare scGFT, scLDM and Cell2Sentence for single-cell RNA-seq fidelity, biological-structure preservation and membership-inference risk on donor-split OneK1K data.
- **Authors:** Buse Giledereli, Başar Temiz, Amirreza Sattarzadeh Khanehbargh
- **arXiv:** `2610.31454v1` (published 2026-10-22 15:49:27 UTC; categories: `q-bio.GN` (primary))
- **Evidence for ranking:** Uses OneK1K (about 1.2 million PBMCs from 982 donors) and three evaluation axes; the authors report direct copying of non-highly-variable-gene values creates membership leakage, while Poisson reconstruction reduces it. Presented at the CAMDA 2026 ELSA Health Privacy Challenge.
- **Claimed contribution:** The benchmark shows that post-processing and non-HVG handling materially change the privacy–utility balance; scGFT and scLDM retain more biological structure than an independent-Poisson baseline in reported tests.
- **Caveat:** Generative modeling was restricted to highly variable genes and evaluated on one dataset; privacy and biological-fidelity metrics can disagree, and the authors warn that metric choice and gene filtering affect conclusions.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Biomedical & translational medicine

### 4. [Escaping the Phylogenetic Trap: Persistent Homology Enables Cross-Species Ion Channel Classification via Multimodal Graph Neural Networks](https://arxiv.org/abs/2610.30394)
- **Abstract:** A multimodal graph model uses persistent-homology features to classify venom ion-channel targets under leave-one-taxon-out evaluation.
- **Authors:** Arezoo Bybordi, Favour Achimba, Mariam Gelashvili, Jessy Ramirez, Weigang Qiu, Mandë Holford, Anita Raja
- **arXiv:** `2610.30394v1` (published 2026-10-21 19:59:07 UTC; categories: `cs.LG` (primary), `q-bio.BM` (cross-list))
- **Evidence for ranking:** The reported benchmark includes 1,373 ColabFold-predicted venom compounds across five taxa. Under taxon-held-out testing, PH-GNN reaches 63.4%, versus 54–55% for the next geometric priors; random splits give higher and less discriminating scores.
- **Claimed contribution:** The authors argue that topology-aware structural features help mitigate taxonomic leakage in cross-species ion-channel classification.
- **Caveat:** This is computational classification over predicted structures, not experimental toxin–channel binding or functional validation; performance is specific to the reported benchmark and split.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 5. [Behavioral Mapping of Hierarchical Dynamical Models Accelerates Bayesian Parameter Inference](https://arxiv.org/abs/2610.30683)
- **Abstract:** A behavioral-compatibility filter uses a simpler model's posterior to reduce costly Bayesian inference for a more detailed model, demonstrated on cell-free gene-expression models.
- **Authors:** Jingsong Bai, Ayush Pandey
- **arXiv:** `2610.30683v1` (published 2026-10-22 03:53:06 UTC; categories: `stat.ME` (primary), `eess.SY`, `q-bio.QM` (cross-lists))
- **Evidence for ranking:** The authors report MCMC speedups of 8.02% for a phenomenological and 15.21% for a mechanistic gene-expression model after setup; the paper is cross-listed in quantitative biology, statistics and systems/control.
- **Claimed contribution:** The method learns a Gaussian-process level set of detailed-model parameters behaviorally supported by a reduced-model posterior, then filters proposals while retaining parameters that fit within a stated tolerance.
- **Caveat:** Evidence is from a hierarchy of cell-free gene-expression models; transfer to other model families or experimental regimes is not established, and the speedup follows initial setup costs.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** Quantitative methods; Molecular & cell biology

### 6. [Supercoiling Drives DNA-Protein Co-Condensation](https://arxiv.org/abs/2610.30588)
- **Abstract:** A coupled DNA-elasticity/protein-field model predicts that DNA supercoiling can facilitate protein wetting and co-condensation.
- **Authors:** Sihan Liu, Hongbo Zhao, Andrej Košmrlj
- **arXiv:** `2610.30588v1` (published 2026-10-22 01:42:38 UTC; categories: `physics.bio-ph` (primary), `cond-mat.soft`, `q-bio.BM` (cross-lists))
- **Evidence for ranking:** Cross-listed across biological physics, soft matter and biomolecules; the paper reports a mechanistic model linking twist-to-writhe conversion, protein wetting and droplet formation, with supercoiling-dependent nucleation behavior.
- **Claimed contribution:** The authors propose DNA topology as a control parameter for biomolecular co-condensation and genome organization.
- **Caveat:** The result is model-based; it does not demonstrate the proposed pathway in cells or establish its quantitative importance in vivo.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** DNA & genomics; Molecular & cell biology; Quantitative methods

### 7. [Direct Production of Ultra-High Radioisotopic Pure ⁶⁴Cu from Natural Zinc Metal via D-D Fusion Narrowband Fast Neutron Source Irradiation](https://arxiv.org/abs/2610.31340)
- **Abstract:** The authors report producing ⁶⁴Cu from natural zinc using a D-D fusion neutron source and measuring the irradiated sample by time-resolved gamma spectroscopy.
- **Authors:** Jeremy M. C. Brown, Mantas Grigalavicius, Tibor Gilinger, Adam Kovacs, Parvin Varmazyar, Hsin-Hui Huang, Saulius Juodkazis, Mikas Vengris, Darius Gailevicius, Karoly Osvay
- **arXiv:** `2610.31340v1` (published 2026-10-22 14:24:29 UTC; categories: `physics.med-ph` (primary))
- **Evidence for ranking:** Reports a one-hour irradiation of high-purity natural zinc and 72-hour spectroscopy; authors give radioisotopic purity estimates of 99.62% and 99.97% after minimum-detection-activity correction.
- **Claimed contribution:** The authors present a potential alternative production route for copper-64, motivated by the cost of enriched nickel targets.
- **Caveat:** This is a production experiment, not a radiopharmaceutical formulation, animal study or clinical evaluation; reproducibility, scale-up and suitability for particular applications remain unestablished here.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 8. [AI Enhanced Cerenkov Luminescence Microscopy](https://arxiv.org/abs/2610.31240)
- **Abstract:** A Monte-Carlo-guided CARE network restores simulated Cerenkov microscopy images and is applied to images from 27 radiotracer-exposed U87 tumor spheroids.
- **Authors:** Stefano Pizzardi, Lisa Alborghetti, Caterina Lomazzi, Antonello Enrico Spinelli
- **arXiv:** `2610.31240v1` (published 2026-10-22 13:23:12 UTC; categories: `physics.med-ph` (primary))
- **Evidence for ranking:** Trained on 15,360 simulated image pairs from 80 spheroid geometries; synthetic validation MSE is reported as 0.0051 versus 0.0492 for Noise2Void, followed by application to experimental images from 27 U87 spheroids.
- **Claimed contribution:** The authors propose physics-guided image restoration to mitigate noise and positron-induced blur in 3D Cerenkov luminescence microscopy.
- **Caveat:** The quantitative ground-truth comparison is on simulations; experimental spheroid results are image-quality comparisons, not independent ground-truth recovery or in-vivo/clinical validation.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 9. [Advancing oxygen-enhanced MRI acquisition and modelling through dynamic ΔR₁ and ΔR₂* sensing](https://arxiv.org/abs/2610.30793)
- **Abstract:** SR-Fat DESPOT combines fat–water-separated MRI acquisition with dynamic relaxation-rate modeling and is tested in a numerical phantom and small in-vivo studies.
- **Authors:** Jorge Campos Pazmiño, Amiel Beausoleil-Morrison, Nathalie Panov, Véronique Fortier, Ives R. Levesque
- **arXiv:** `2610.30793v1` (published 2026-10-22 06:16:41 UTC; categories: `physics.med-ph` (primary))
- **Evidence for ranking:** The authors report phantom nMedAE below 3% at SNR >30, one-participant test–retest work and a six-participant pilot under 100% oxygen, with statistically significant relaxation changes in spleen and kidneys.
- **Claimed contribution:** The proposed method aims to quantify fat- and water-specific baseline and gas-challenge-induced relaxation changes with fewer acquisitions.
- **Caveat:** The in-vivo evidence is a six-person pilot plus a single-participant repeatability test; it does not establish diagnostic performance, generalizability or clinical utility.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 10. [Geometry-Dependent Properties of Physically Crosslinked PPy-PVA Hydrogels Enable Tunable Iontophoretic Drug Delivery](https://arxiv.org/abs/2610.31567)
- **Abstract:** Five BSA-loaded PPy-PVA hydrogel geometries are compared for iontophoretic transport using Franz diffusion cells with artificial membranes.
- **Authors:** Heather Jin Hee Kim, Mohsen Alishahi, Kyuin Park, Mikaila K. Roncevich, Larissa M. Shepherd, Cara M. Nunez
- **arXiv:** `2610.31567v1` (published 2026-10-22 17:10:35 UTC; categories: `cs.RO` (primary), `physics.med-ph` (cross-list))
- **Evidence for ranking:** Abstract reports five fabricated geometries, a permeability estimate of (3.80 ± 1.93) × 10⁻⁵, and a DOI registered to an IEEE Transactions on Biomedical Engineering article (10.1109/TBME.2026.3744496; Crossref record).
- **Claimed contribution:** The authors argue geometry can tune hydrogel microstructure, local fields and transport without changing current density for each design.
- **Caveat:** The reported payload is BSA and transport testing used artificial membranes; this does not establish delivery of a therapeutic through intact skin or in-vivo efficacy.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** Biomedical & translational medicine; Molecular & cell biology; Quantitative methods

### 11. [Shorter but not more catalytic: an active-site-resolved model of how tau reshapes amyloid-β secondary nucleation](https://arxiv.org/abs/2610.30531)
- **Abstract:** A coupled tau–amyloid-β model tracks fibril mass, number and active secondary-nucleation sites to test when shorter fibrils change catalytic activity.
- **Authors:** Andrey V. Kuznetsov
- **arXiv:** `2610.30531v1` (published 2026-10-21 23:33:32 UTC; categories: `q-bio.SC` (primary))
- **Evidence for ranking:** The model explores 800 Latin-hypercube samples and mean fibril lengths from 0.3 to 30 μm; it predicts fibril shortening alone does not necessarily increase catalytic activity.
- **Claimed contribution:** The author identifies active-site density, exposure and monomer clearance/elongation balance as conditions governing the modeled secondary-nucleation response.
- **Caveat:** This is a mechanistic model, not a new biochemical measurement; predictions need comparison with matched-mass fibril assays and measured active-site accessibility.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Biomedical & translational medicine

### 12. [Global Convergence of Detailed Balanced Mass Action Systems](https://arxiv.org/abs/2610.30808)
- **Abstract:** The authors give a Lean 4-formalized proof that positive trajectories in finite detailed-balanced mass-action systems converge to a unique positive equilibrium in each positive compatibility class.
- **Authors:** Haoran Lv, Chengjin Ni, Manqin Wang, Shenli He
- **arXiv:** `2610.30808v1` (published 2026-10-22 06:33:06 UTC; categories: `cs.LO` (primary), `math.DS`, `q-bio.MN` (cross-lists))
- **Evidence for ranking:** Cross-listed in logic, dynamical systems and molecular networks; authors report a complete formalization checked by the Lean kernel and provide a public Lean development.
- **Claimed contribution:** The paper supplies a self-contained proof of uniqueness and global convergence for the stated class of detailed-balanced reaction networks.
- **Caveat:** The theorem is limited to finite, detailed-balanced deterministic systems with positive rate constants; it is not evidence about stochastic, noisy, non-detailed-balanced or experimentally measured networks.
- **Announcement type:** new submission, 2026-10-23 batch
- **Themes:** Quantitative methods; Molecular & cell biology

## Trending Research Themes

- **Protein/RNA design and sequence-to-function modeling:** ProMORNA, RiboBridge and the ion-channel classifier (Bybordi et al.) use generative or structure-aware learning around biological sequences and structures. The tasks differ—mRNA design, complex-structure prediction and cross-taxon classification—so this is a cluster of computational methods, not evidence that one approach has become dominant.
- **Mechanistic models spanning molecular organization and kinetics:** Supercoiling–co-condensation, tau/amyloid secondary nucleation and detailed-balanced mass-action convergence each formalize molecular behavior with models or proofs. ProMORNA is the clearest experimental bridge in this set; the other molecular conclusions are model- or theorem-scoped.
- **Biomedical methods paired with physical or experimental data:** The copper-64 production study, Cerenkov microscopy, oxygen-enhanced MRI and hydrogel transport connect methods to measurements, but at different stages—from a materials assay or spheroid experiment to a small human pilot. None establishes clinical benefit.
- **Privacy-aware synthetic omics:** The OneK1K paper is the batch's single direct contribution here, rather than a repeated signal; it makes non-HVG handling and donor-level privacy part of the benchmark rather than treating expression similarity alone as success.

## Open Problems and Research Directions

- **mRNA and RNA-binder validation:** ProMORNA's authors call for broader targets, longer transcripts and independent validation; RiboBridge identifies interface prioritization and sequence realization as bottlenecks. Follow-up work could test blinded, prospectively selected sequences across multiple proteins and RNA lengths, measure expression/stability separately, and compare predicted binding with biochemical binding and functional assays.
- **Privacy and biological utility beyond one dataset:** The OneK1K benchmark is restricted to highly variable genes and one donor-linked cohort. Replication on an independent donor cohort, sequencing platform and tissue, with full-transcriptome generation and donor-level attack evaluations, would test whether the reported privacy–utility trade-offs persist.
- **From physical models to biological evidence:** Supercoiling and tau/amyloid predictions suggest matched-condition experiments—vary DNA linking number and protein concentration, or quantify fibril active sites at matched mass and length—to discriminate their proposed mechanisms. These are proposals, not results reported in the papers.
- **Translational measurement boundaries:** The ⁶⁴Cu route needs repeatability and scale-up characterization; Cerenkov restoration needs held-out physical phantoms and independent spheroid models with reference measurements; the oxygen-MRI pilot needs larger, independent cohorts and repeatability analysis. Hydrogel transport would require testing beyond BSA and artificial membranes before claims about intact-skin delivery.

## Takeaway

This batch is strongest in computational molecular design and evaluation, with a smaller set of measurement-oriented biomedical studies. ProMORNA is the clearest experimental bridge, but remains a single-reporter study; RiboBridge and the protein-structure methods are promising benchmark results, not confirmed molecular function. The imaging and delivery work is similarly early-stage. These are notable research directions from one arXiv batch, not evidence of clinical readiness or field-wide popularity.

## Method and sources

- **Window:** daily, 2026-10-23 through 2026-10-23. The current date (2026-10-24) had no newer batch at snapshot; this report therefore uses the prior Friday announcement batch, 23 October 2026.
- **Snapshot:** 2026-10-24 16:16:28 UTC.
- **Candidate corpus:** latest-day arXiv listings for `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`, cross-checked against the arXiv API query `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date. No `cs.BI` records appeared in this batch. Category listings yielded 18 unique candidates; all 18 arXiv abstract pages were checked. Papers were deduplicated by versionless arXiv ID and use latest announced-version metadata while retaining first-submission dates.
- **Selection and ranking:** Attention/citation signals were too sparse for this just-announced batch to support a defensible popularity ranking. These 12 are labeled notable, ranked by direct fit to molecular biology/biomedicine and the specificity of reported evaluation; computational, simulated, biochemical and in-vivo evidence are kept distinct. No citation velocity or downloads/views are claimed. A revision is identified explicitly.
- **Primary sources:** category listing pages [q-bio.BM](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), and [physics.med-ph](https://arxiv.org/list/physics.med-ph/recent); each paper's linked abstract page; full HTML for the top three ([ProMORNA v2](https://arxiv.org/html/2605.01513v2), [RiboBridge](https://arxiv.org/html/2610.30668v1), [OneK1K benchmark](https://arxiv.org/html/2610.31454v1)). The broad arXiv API query is recorded above. The hydrogel DOI was cross-checked against [Crossref](https://api.crossref.org/works/10.1109/TBME.2026.3744496).
