# arXiv Biology & Biomedicine — Daily batch, 23 October 2026

Ten notable papers from the Friday, 23 October announcement batch. The strongest cluster is RNA design—from full-length mRNA generation to protein-binding RNA structures—alongside single-cell privacy methods and mechanistic models of DNA/protein and amyloid systems. Today's agenda: what is newly testable in RNA design, where computational results stop short of biological validation, and which biomedical methods have early experimental support. This is a relevance-ranked selection, not a measured popularity chart: arXiv has no official trending chart, independent attention evidence is sparse for a fresh batch, and arXiv's biomedical coverage is incomplete relative to bioRxiv, medRxiv, and the wider medical literature.

## Top papers (ranked)

### 1. [ProMORNA: An End-to-End Generative Framework for Full-Length mRNA Design](https://arxiv.org/abs/2605.01513)
- **Abstract:** ProMORNA uses a protein-conditioned encoder–decoder and multi-objective post-training to generate full-length mRNAs, reporting improved in-silico scores and higher Fluc2P reporter activity for selected candidates in three independent in-vitro experiments.
- **Authors:** Zixi Shao; Tao Wang; Ye Shen; Tianyi Huang; Yibei Xiao
- **arXiv:** `2605.01513v2` (published 2026-10-21T13:02:48Z; first submitted 2026-05-02; categories: `cs.LG`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** Substantive v2 revision in this announcement batch; q-bio.BM cross-list; the revision reports three independent Fluc2P experiments. These are relevance and study-design signals, not popularity measures.
- **Claimed contribution:** The authors report that Candidate 2's 12–72 h reporter-activity AUC was 3.33× the conventional benchmark (Holm-adjusted P=0.01285); its estimated 1.29× advantage over the selected GEMORNA candidate did not remain significant after correction.
- **Caveat:** The experimental evidence is an in-vitro Fluc2P reporter screen, not evidence of therapeutic efficacy or generalization across payloads or in vivo settings; the GEMORNA comparison is explicitly exploratory after multiple-comparison correction.
- **Announcement type:** revision (v2; originally submitted 2 May 2026), announcement batch 23 October 2026.
- **Themes:** RNA & transcriptomics; Biomedical & translational medicine; Bioinformatics & sequence analysis

### 2. [RiboBridge: protein-conditioned de novo RNA binder structure design](https://arxiv.org/abs/2610.30668)
- **Abstract:** RiboBridge separates canonical RNA conformation generation from protein-relative assembly, using predicted interfaces and cross-frame interaction geometry to generate candidate protein–RNA structures without a specified binding site.
- **Authors:** Zhou Zhang; Hanqun Cao; Minghao Sun; Odin Zhang; Yang Zhang; Pheng Ann Heng; Wujun Li; Tianfan Fu
- **arXiv:** `2610.30668v1` (published 2026-10-22T03:32:07Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Direct q-bio.BM relevance and a temporally split, sequence-filtered, redundancy-controlled benchmark of 124 protein–RNA complexes; the paper includes component ablations and stage-wise diagnostics.
- **Claimed contribution:** On that benchmark, authors report the best fNAT and DockQ and lowest interface/ligand RMSDs among compared methods under post-hoc interface-correspondence evaluation.
- **Caveat:** Native interface information is used after generation to select the corresponding predicted-pocket candidate; the results are structural predictions, not demonstrations of binding, activity, safety, or therapeutic effect. The authors identify interface prioritization and sequence realization as limitations.
- **Announcement type:** new submission, announcement batch 23 October 2026.
- **Themes:** RNA & transcriptomics; Biochemistry & proteins; Bioinformatics & sequence analysis

### 3. [Benchmarking Recent Single-Cell Synthetic Data Generation Methods on the OneK1K Dataset](https://arxiv.org/abs/2610.31454)
- **Abstract:** The authors compare scGFT, scLDM, and Cell2Sentence on synthetic single-cell RNA-seq utility and membership-inference privacy, finding that how non-highly-variable genes are reconstructed strongly affects leakage.
- **Authors:** Buse Giledereli; Basar Temiz; Amirreza Sattarzadeh Khanehbargh
- **arXiv:** `2610.31454v1` (published 2026-10-22T15:49:27Z; categories: `q-bio.GN`)
- **Evidence for ranking:** Primary genomics category; donor-split OneK1K evaluation (633,711 training cells from 490 donors and 634,022 test cells from 491 donors); compares fidelity, downstream biological preservation, and membership inference rather than marginal similarity alone.
- **Claimed contribution:** The authors report that copying non-HVG values can yield severe membership leakage, while Poisson reconstruction lowers risk; scGFT/scLDM preserve more biological structure than an independent Poisson baseline in tested configurations.
- **Caveat:** Compute limits restricted generative modeling mainly to highly variable genes, and the benchmark is one dataset/split; privacy results do not establish protection against all attacks or populations.
- **Announcement type:** new submission, announcement batch 23 October 2026.
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Biomedical & translational medicine

### 4. [Supercoiling Drives DNA-Protein Co-Condensation](https://arxiv.org/abs/2610.30588)
- **Abstract:** A coupled DNA-elasticity/protein-field model predicts that supercoiling and protein wetting reinforce one another, helping DNA cross a kinetic barrier into a protein-rich condensed state.
- **Authors:** Sihan Liu; Hongbo Zhao; Andrej Košmrlj
- **arXiv:** `2610.30588v1` (published 2026-10-22T01:42:38Z; categories: `physics.bio-ph`, `cond-mat.soft`, `q-bio.BM`)
- **Evidence for ranking:** Cross-listed in biophysics, soft matter, and biomolecules; simulations and a reduced analytical model examine a defined supercoiling/protein-concentration phase space, including biologically relevant supercoiling ranges.
- **Claimed contribution:** The authors' model shows protein wetting can promote twist-to-writhe conversion and capillary collapse, while sufficient supercoiling lowers the modeled nucleation barrier.
- **Caveat:** This is theory and simulation, not a direct cellular or biochemical demonstration; it assumes an idealized closed DNA loop and simplified DNA–protein/solvent interactions.
- **Announcement type:** new submission, announcement batch 23 October 2026.
- **Themes:** DNA & genomics; Biochemistry & proteins; Molecular & cell biology

### 5. [Escaping the Phylogenetic Trap: Persistent Homology Enables Cross-Species Ion Channel Classification via Multimodal Graph Neural Networks](https://arxiv.org/abs/2610.30394)
- **Abstract:** A multimodal sequence-and-structure classifier uses persistent-homology features to improve venom-compound ion-channel target classification when evaluation holds out entire taxa.
- **Authors:** Arezoo Bybordi; Favour Achimba; Mariam Gelashvili; Jessy Ramirez; Weigang Qiu; Mandë Holford; Anita Raja
- **arXiv:** `2610.30394v1` (published 2026-10-21T19:59:07Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** q-bio.BM cross-list and a leave-one-taxon-out benchmark of 1,373 ColabFold-predicted venom compounds across five taxa; the paper quantifies how random splits overstate performance.
- **Claimed contribution:** The authors report 63.4% accuracy for the persistent-homology model under taxonomic shift, more than eight percentage points above the next-best tested method; sequence-only performance fell to about 30% in that setting.
- **Caveat:** Structural inputs are predicted rather than experimentally resolved, and classification scores do not establish toxin binding or functional effects in assays.
- **Announcement type:** new submission, announcement batch 23 October 2026.
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 6. [Shorter but not more catalytic: an active-site-resolved model of how tau reshapes amyloid-β secondary nucleation](https://arxiv.org/abs/2610.30531)
- **Abstract:** An active-site-resolved kinetic model examines when tau cross-seeding changes amyloid-β42 fibril populations and secondary nucleation, concluding that shorter fibrils alone need not be more catalytic.
- **Authors:** Andrey V. Kuznetsov
- **arXiv:** `2610.30531v1` (published 2026-10-21T23:33:32Z; categories: `q-bio.SC`)
- **Evidence for ranking:** Direct subcellular/molecular scope; model explores 800 Latin-hypercube parameter samples and fibril lengths from 0.3 to 30 μm.
- **Claimed contribution:** The author reports that fibril shortening increases catalytic potential only if each new fibril adds enough active sites; monomer clearance versus elongation controls the modeled direction of secondary-nucleation change.
- **Caveat:** These are model-dependent mechanistic predictions, not new measurements of tau/amyloid aggregation or patient outcomes.
- **Announcement type:** new submission, announcement batch 23 October 2026.
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 7. [Behavioral Mapping of Hierarchical Dynamical Models Accelerates Bayesian Parameter Inference](https://arxiv.org/abs/2610.30683)
- **Abstract:** The method uses posterior information from a simpler model to screen parameter proposals for a more detailed model, and is tested on gene-expression models fitted to cell-free data.
- **Authors:** Jingsong Bai; Ayush Pandey
- **arXiv:** `2610.30683v1` (published 2026-10-22T03:53:06Z; categories: `stat.ME`, `eess.SY`, `q-bio.QM`)
- **Evidence for ranking:** q-bio.QM cross-list; applied to a hierarchy of gene-expression models and reports measured inference-time changes rather than only a proposed algorithm.
- **Claimed contribution:** Authors report 8.02% and 15.21% MCMC speedups for phenomenological and mechanistic models, respectively, after setup costs.
- **Caveat:** Evidence is limited to one gene-expression model hierarchy and cell-free experimental data; the reported gains are modest and may not transfer to other models.
- **Announcement type:** new submission, announcement batch 23 October 2026.
- **Themes:** Quantitative methods; Molecular & cell biology; Bioinformatics & sequence analysis

### 8. [Direct Production of Ultra-High Radioisotopic Pure ⁶⁴Cu from Natural Zinc Metal via D-D Fusion Narrowband Fast Neutron Source Irradiation](https://arxiv.org/abs/2610.31340)
- **Abstract:** The authors irradiate natural zinc with a D-D fusion neutron source and report no-carrier-added ⁶⁴Cu with high measured radioisotopic purity, a possible route to lower-cost radiopharmaceutical isotope production.
- **Authors:** Jeremy M. C. Brown; Mantas Grigalavicius; Tibor Gilinger; Adam Kovacs; Parvin Varmazyar; Hsin-Hui Huang; Saulius Juodkazis; Mikas Vengris; Darius Gailevicius; Karoly Osvay
- **arXiv:** `2610.31340v1` (published 2026-10-22T14:24:29Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Direct medical-physics/radiopharmaceutical application with a physical irradiation and 72-hour gamma-spectroscopy measurement; the paper reports threshold-corrected purity values.
- **Claimed contribution:** Authors report 99.62% minimum and 99.97% detection-threshold-corrected ⁶⁴Cu radioisotopic purity after a one-hour irradiation of natural zinc.
- **Caveat:** The abstract describes a single irradiation protocol, not demonstrated production scale, cost in routine manufacture, clinical availability, or patient benefit.
- **Announcement type:** new submission, announcement batch 23 October 2026.
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 9. [AI Enhanced Cerenkov Luminescence Microscopy](https://arxiv.org/abs/2610.31240)
- **Abstract:** A Monte-Carlo-guided CARE network restores simulated Cerenkov microscopy images and is then applied to images from 27 ¹⁸F-FDG-treated U87 tumor spheroids.
- **Authors:** Stefano Pizzardi; Lisa Alborghetti; Caterina Lomazzi; Antonello Enrico Spinelli
- **arXiv:** `2610.31240v1` (published 2026-10-22T13:23:12Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Medical-imaging application; training set comprises 15,360 simulated image pairs from 80 spheroid geometries, followed by an application to experimental images from 27 spheroids.
- **Claimed contribution:** On synthetic validation data, authors report mean-squared error 0.0051 versus 0.0492 for Noise2Void, and report improved contrast/localization metrics on the experimental spheroid images.
- **Caveat:** The quantitative ground truth is simulated; the experimental application is a small U87 spheroid set, not validation in patients or a clinical imaging workflow.
- **Announcement type:** new submission, announcement batch 23 October 2026.
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 10. [Geometry-Dependent Properties of Physically Crosslinked PPy-PVA Hydrogels Enable Tunable Iontophoretic Drug Delivery](https://arxiv.org/abs/2610.31567)
- **Abstract:** Five polypyrrole–polyvinyl-alcohol hydrogel geometries carrying bovine serum albumin were compared for iontophoretic transport using finite-element modeling and Franz diffusion cells with artificial membranes.
- **Authors:** Heather Jin Hee Kim; Mohsen Alishahi; Kyuin Park; Mikaila K. Roncevich; Larissa M. Shepherd; Cara M. Nunez
- **arXiv:** `2610.31567v1` (published 2026-10-22T17:10:35Z; categories: `cs.RO`, `physics.med-ph`; DOI: [10.1109/TBME.2026.3744496](https://doi.org/10.1109/TBME.2026.3744496))
- **Evidence for ranking:** Direct drug-delivery application; compares five fabricated geometries using measured microstructure and membrane-transport assays, with finite-element field analysis.
- **Claimed contribution:** Authors report geometry-dependent transport and mean iontophoretic permeability of (3.80 ± 1.93) × 10⁻⁵ in the artificial-membrane assay.
- **Caveat:** The cargo is BSA and transport was measured using artificial membranes, not intact human skin or a clinical drug-delivery study.
- **Announcement type:** new submission, announcement batch 23 October 2026.
- **Themes:** Biomedical & translational medicine; Quantitative methods

## Trending Research Themes

- **Protein-conditioned RNA design is splitting into distinct problems.** ProMORNA targets full-length mRNA sequence design and reports reporter activity, while RiboBridge targets protein–RNA structural assembly. The former has limited in-vitro functional evidence; the latter remains a structure-prediction result. Neither alone establishes a general design solution.
- **Evaluation design matters as much as model architecture.** The OneK1K benchmark shows privacy can be compromised by non-HVG handling; the ion-channel paper shows random splits can hide taxonomic generalization failures. Both argue for explicit adversarial or out-of-distribution evaluation, but on different tasks and datasets.
- **Mechanistic biomolecular models are probing hidden state variables.** The DNA paper models topology and wetting together; the tau paper tracks active catalytic sites rather than fibril mass alone. Both are model-based explanations, not new experimental confirmation.
- **Biomedical translation is represented by several separate proof-of-concept methods, not one unified shift.** The batch includes isotope production (⁶⁴Cu), image restoration (Cerenkov microscopy), and membrane-based delivery (PPy-PVA hydrogels), each with different validation levels and none establishing clinical efficacy.

## Open Problems and Research Directions

- **Test RNA designs beyond computational or reporter proxies.** For RiboBridge, synthesize prioritized candidates and measure binding affinity, specificity, and functional activity across multiple protein targets; for ProMORNA, repeat reporter and protein-output assays on payloads beyond Fluc2P and assess stability/translation under relevant cellular conditions. These follow-ups address the papers' stated boundary between predicted structure or reporter activity and functional, generalizable designs.
- **Stress-test privacy on independent donors and attacks.** Repeat the OneK1K-style evaluation on external cohorts, hold out cell types and donors, and compare membership inference plus reconstruction attacks while retaining full-transcriptome utility. This would test whether the observed non-HVG privacy effect generalizes.
- **Experimentally vary DNA topology and protein affinity.** Reconstituted systems could independently vary supercoiling density, protein concentration, and DNA–protein interaction strength, then quantify condensation kinetics and hysteresis. This directly tests the model's predicted cooperative pathway against its simplified physical assumptions.
- **Strengthen translational validation.** For Cerenkov restoration, compare against independent spatial ground truth across diverse spheroid geometries and tracer conditions; for the hydrogel study, test intact skin or a validated skin model with multiple cargos. For ⁶⁴Cu, replicate production across runs and quantify yield, impurity profiles, and scale-up behavior before making manufacturing claims.

## Takeaway

The clearest fresh-batch signal is topical rather than statistical: two complementary RNA-design papers, a substantial single-cell privacy benchmark, and molecular models that expose assumptions worth testing. ProMORNA adds early in-vitro reporter evidence, but none of these papers warrants a claim of clinical efficacy; the biomedical engineering papers remain preclinical or assay-level.

## Method and sources

- **Window:** daily, latest available announcement batch dated Friday 23 October 2026. Underlying first-submission or revision timestamps among selected records span 21–22 October 2026; ProMORNA is a v2 revision (first submitted 2 May). Snapshot: 2026-10-23 16:16:31 UTC. The latest batch visible on the arXiv recent listings at the snapshot was dated Friday 23 October 2026.
- **Candidate query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date descending. The broad API response was traversed until results extended beyond this daily batch; recent-list pages were checked for q-bio.BM, GN, MN, SC, CB, TO, QM, and physics.med-ph. The `cs.BI` recent-list endpoint was unavailable during this run, although it was included in the broad API query; category-level completeness is therefore not guaranteed.
- **Ranking:** No arXiv popularity chart exists, and no defensible independent attention or citation-velocity signal was established for this very recent batch. The list is consequently titled **Notable recent papers** and ranked by direct biology/biomedicine relevance, category fit, and checkable study or validation design—not by claimed readership. The 10 entries were selected from the latest batch after topical screening and deduplication by versionless arXiv ID. Citation totals, downloads, and views are not claimed.
- **Evidence boundary:** Abstracts were checked on the linked arXiv pages. The full HTML text was also reviewed for ProMORNA, RiboBridge, and the OneK1K benchmark; summaries distinguish author-reported in-silico, in-vitro, and imaging evidence. arXiv is not a representative biomedical index; clinical papers here are not practice-changing evidence, and this report is not medical advice.
- **Category listings:** [q-bio.BM](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), [physics.med-ph](https://arxiv.org/list/physics.med-ph/recent). Each paper entry links to its verified abstract page; version and category metadata were checked against the arXiv API.
