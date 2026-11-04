# arXiv Biology & Biomedicine — Daily, 2026-11-04

Latest announcement batch: Wednesday, 4 November 2026. Six notable papers, led by prospective protein-binder design, DNA-design benchmarking, and protein conformational modeling. Spoken agenda: what biological sequence and structure models can do, what has been tested experimentally, and where the evidence remains bounded. arXiv has no official trending chart; this is a relevance-ranked snapshot, not a popularity ranking, and arXiv omits much of the biomedical preprint literature.

## Notable recent papers

### 1. [ProteoCraft: Protein Design as Proposal-Verification Search](https://arxiv.org/abs/2611.03963)
- **Abstract:** Introduces a tree-search framework for de novo binder design and reports computational comparisons across 14 design settings plus prospective binding assays for PD-L1 miniproteins and IFNAR2 VHHs.
- **Authors:** Fang Wu; Hongbin Lin; Bingchen Duan; Yuchen Wang; Li Erran Li; Yanjie Huang; Mingxuan Cao; Yijun Ma; Yunxiang Mo; Yanchao Li; Kuan Pang; Juangui Xu; Hanqun Cao; Dongwei Jiang; Xinyue Xu; Xiangru Tang; Zehong Wang; Jian Ma; Kejun Ying; Guanlue Li; Mingran Cao; Fanjin Wang; Tianfan Fu; Shuangjia Zheng; Yao Shu; Jure Leskovec; Yejin Choi
- **arXiv:** `2611.03963v1` (published 2026-11-02 21:03:10 UTC; categories: `cs.CE`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** Strong biomolecular fit and three-category cross-listing; compares 14 design settings; the authors report prospective synthesis and binding measurements, including 29 binding hits among 35 PD-L1 miniprotein candidates.
- **Claimed contribution:** The authors propose using diffusion-model structural gradients to guide search while independent structure-model inference verifies candidates; they report an 82.9% PD-L1 miniprotein binding hit rate, a best measured KD of 0.879 nM, and binding for designed IFNAR2 VHH.
- **Caveat:** The experimental validation is limited to the tested targets and designs; the authors say specificity, biological activity, and generalization to additional targets require further characterization. Binding alone does not establish therapeutic efficacy.
- **Announcement type:** new submission, 2026-11-04 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 2. [BEND 2.0: Benchmarking the Capabilities Needed to Design DNA](https://arxiv.org/abs/2611.03806)
- **Abstract:** Introduces an eight-task benchmark across five experimental datasets to test genomic models' DNA mutation-effect prediction and sequence-design capabilities.
- **Authors:** Andreas Bjerregaard; Rachael DeVries; Dionysia Danai Brilli; Panagiotis Antoniadis; Yan Li; Anders Krogh; Wouter Boomsma; Ole Winther; Frederikke Isa Marin
- **arXiv:** `2611.03806v1` (published 2026-11-02 19:00:07 UTC; categories: `q-bio.GN`, `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** Broad fit to DNA/genomics; cross-listed in genomics and quantitative biology; eight tasks/five experimental datasets; public code and benchmark leaderboard are linked in the arXiv comment.
- **Claimed contribution:** The authors report that fitted linear readouts can match or exceed native model outputs and transfer across some genes and assays, while context-specific effects and mutation interactions remain difficult.
- **Caveat:** This is a retrospective benchmark on existing experimental datasets, not prospective validation of newly designed DNA; the authors caution that results may not generalize uniformly across populations or biological settings.
- **Announcement type:** new submission, 2026-11-04 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 3. [Ablating Design Choices for Protein Ensemble Generators Across Structural Regimes](https://arxiv.org/abs/2611.05055)
- **Abstract:** Ablates design choices in a protein conformational-ensemble generator and compares generated ensembles with experimental SAXS and NMR chemical-shift data across ordered, disordered, multi-domain, and transitional proteins.
- **Authors:** Eoin Quinn; Oliver Bent
- **arXiv:** `2611.05055v1` (published 2026-11-03 15:20:50 UTC; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** Direct biomolecular relevance; cross-listed with machine learning; experimental SAXS and NMR observables provide an explicit comparison beyond simulated benchmarks.
- **Claimed contribution:** The authors find training-source choices matter more than several tested architectural choices; fragment-assembled disorder ensembles improve chemical-shift agreement, while mixing sources moderates the SAXS trade-off.
- **Caveat:** Authors note approximate training sources, unquantified back-mapping error, limited observables, and small non-ordered SAXS groups (34–42 proteins per cell, three seeds per variant); compactness agreement is not proof of fold correctness.
- **Announcement type:** new submission, 2026-11-04 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 4. [Predicting protein structures at any folding stage from sequence](https://arxiv.org/abs/2611.04287)
- **Abstract:** Presents FoldScape, a sequence-conditioned model that generates coarse-grained protein conformational ensembles at a specified folding fraction, covering stages from collapsed coil toward near-native globules.
- **Authors:** Lisheng Zhang; Qingsong Li; Zinan Xie; Yanting Yang; Qikui Yang; Peng Lu; Zhican Fu; Wentao Cui; Runtong Hou; Zhengwei Xie
- **arXiv:** `2611.04287v1` (published 2026-11-03 04:15:20 UTC; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** Cross-listed in biomolecules and AI; evaluates 20 human proteins of 36–857 residues and compares folding-coordinate coverage with seed-varied AlphaFold 3 ensembles.
- **Claimed contribution:** The authors report about an order-of-magnitude greater folding-coordinate coverage than the tested AlphaFold 3 ensembles at matched sample size, while AlphaFold 3 better anchors the immediate native vicinity.
- **Caveat:** The reported ensembles are coarse-grained Cα models trained on simulated folding/unfolding trajectories; the abstract does not establish experimental accuracy for intermediate conformations, and the authors describe the methods as complementary.
- **Announcement type:** new submission, 2026-11-04 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [iGC: Antibody Optimization via Reinforcement Learning over a Learned Somatic Hypermutation Prior](https://arxiv.org/abs/2611.05270)
- **Abstract:** Presents a two-stage reinforcement-learning framework that learns a somatic-hypermutation prior from B-cell lineage data and uses it to guide antigen-specific antibody sequence optimization.
- **Authors:** Thao Nguyen; Robert G. Alberstein; Ewa Nowara; Homa MohammadiPeyhani; Holly R. Steach; Sarah A. Robinson; Yuval Shechter; Donald W. Lee; Jason A. Vander Heiden; Franziska Seeger; Andrew Leaver-Fay; Richard Bonneau; Joshua Yao-Yu Lin
- **arXiv:** `2611.05270v1` (published 2026-11-03 17:55:25 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Strong biomolecular fit and cross-listing with machine learning; evaluates mutation-site prediction, somatic-hypermutation consistency, affinity-reward optimization, and candidate diversity.
- **Claimed contribution:** The authors report that their learned prior more than doubles the strongest baseline on mutation-site prediction and that RL optimization retains sequence-structure signals while balancing predicted reward and diversity.
- **Caveat:** The evaluation relies on deep-mutational-scanning-derived rewards rather than direct binding measurements of newly generated candidates, so experimental affinity improvement is not established.
- **Announcement type:** new submission, 2026-11-04 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 6. [Empirical Bayes Flow Matching for Continuous Cryo-EM Heterogeneity](https://arxiv.org/abs/2611.05202)
- **Abstract:** Proposes an empirical-Bayes flow-matching method to infer continuous distributions of protein conformations from indirect observations, including simulated cryo-EM projections.
- **Authors:** Daniel Aibinder; Azmi Haider; Dan Rosenbaum
- **arXiv:** `2611.05202v1` (published 2026-11-03 16:51:30 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Cross-listed in biomolecules and machine learning; arXiv comment reports acceptance at NeurIPS 2026; tests include controlled inverse problems and simulated cryo-EM with known poses.
- **Claimed contribution:** The authors report recovering continuous protein-conformation distributions directly in atomic-coordinate space without pretraining on clean structures.
- **Caveat:** The cryo-EM demonstration uses simulated data and known poses; performance on real particle stacks, where poses and experimental effects are uncertain, remains to be established.
- **Announcement type:** new submission, 2026-11-04 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

## Trending Research Themes

- **Protein design pipelines combine broad computational search with targeted experimental checks.** ProteoCraft is the clearest example in this batch: its structural-search strategy is evaluated in many design settings and then tested prospectively for binding on PD-L1 and IFNAR2. iGC shares the antibody-optimization goal but reports computational reward and sequence-plausibility evidence, not binding assays.
- **Protein models are expanding from a single native structure toward ensembles.** The protein-ensemble ablation study compares conformational samples with SAXS and NMR observables; FoldScape generates folding-stage ensembles; Empirical Bayes Flow Matching targets continuous heterogeneity from cryo-EM observations. Their evidence is not interchangeable: FoldScape is coarse-grained, and EB-FM's cryo-EM demonstration is simulated.
- **Genomic foundation models are being evaluated for intervention selection, not only prediction.** BEND 2.0 tests whether models can guide DNA-edit choices across eight tasks and five experimental datasets. It reports useful signals but also gaps in context-specific and interaction prediction; these results do not amount to prospective validation of designed edits.

## Open Problems and Research Directions

These are follow-up directions suggested by the papers, not clinical recommendations or claims of novelty.

- **Binder specificity and breadth:** For ProteoCraft, measure off-target binding, functional activity, and repeatability across independent target families, beyond the reported PD-L1 and IFNAR2 designs. For iGC, synthesize blinded top-ranked candidates and controls, then compare measured binding with its DMS-derived reward and diversity estimates.
- **Prospective DNA design:** For BEND 2.0, test model-selected edits in held-out genes and cell contexts, including paired single and combined mutations, to measure whether context-specific effects and interactions transfer to new experiments.
- **Structure-sensitive ensemble validation:** For the protein-ensemble ablation study, add orthogonal observables and partially ordered proteins, quantify coarse-grain-to-atom back-mapping uncertainty, and increase replicate counts where SAXS comparisons were unresolved. For FoldScape, compare intermediate-state ensembles with independent experimental measurements rather than only other model-generated ensembles.
- **Real cryo-EM robustness:** For Empirical Bayes Flow Matching, evaluate on real particle stacks with unknown poses and compare recovered heterogeneity against established reconstruction workflows and available orthogonal structural evidence.

## Takeaway

This batch combines computational protein and DNA design with increasingly explicit modeling of conformational ensembles. ProteoCraft stands out for prospective binder assays, while several other contributions remain supported mainly by retrospective benchmarks or simulations. Read the performance claims within those evidence boundaries; none alone establishes clinical benefit.

## Method and sources

- **Window:** daily; announcement batch 2026-11-04 (Wednesday). The current arXiv recent listings show a 4 Nov batch, so this is not a prior-batch fallback. Snapshot: 2026-11-04 17:11 UTC. Candidate eligibility is based on submissions/updates appearing in this announcement batch; the six selected records were first-submitted on 2–3 Nov and are all v1.
- **Candidate query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.TO OR cat:q-bio.CB OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date. Recent category listings and the broad arXiv API query were checked; records were deduplicated by versionless arXiv ID and verified against their arXiv abstract pages.
- **Ranking:** arXiv provides no official popularity ranking. Citation momentum and independent attention were not sufficient to support a defensible popularity ordering for this very recent batch, so these are ranked by demonstrated relevance and the scope/type of reported evaluation. Cross-list breadth, availability of checkable benchmark or experimental evidence, and accepted-status comments were used as supporting signals; the order is not a claim about readership.
- **Coverage:** arXiv is not a representative index of biomedical research. Many experimental and clinical preprints appear on bioRxiv or medRxiv; this report does not cover them, and it is not a systematic review or clinical guidance.
- **Sources:** [arXiv q-bio recent listings](https://arxiv.org/list/q-bio/recent); [arXiv Medical Physics recent listings](https://arxiv.org/list/physics.med-ph/recent); [arXiv Computer Science recent listings](https://arxiv.org/list/cs/recent). Paper metadata and abstracts: [2611.03963](https://arxiv.org/abs/2611.03963), [2611.03806](https://arxiv.org/abs/2611.03806), [2611.05055](https://arxiv.org/abs/2611.05055), [2611.04287](https://arxiv.org/abs/2611.04287), [2611.05270](https://arxiv.org/abs/2611.05270), [2611.05202](https://arxiv.org/abs/2611.05202). For the top three, full HTML texts were checked for reported evidence and limitations.
