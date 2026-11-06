# arXiv biology and biomedicine — week of 31 Oct–6 Nov 2026

Eight notable papers from the configured biology/biomedicine categories point to a busy week for DNA-design benchmarking, computational antibody/protein methods, and single-cell or cancer-genomics analyses. This is a relevance-ranked selection, not a reliable measure of “hotness”: arXiv has no official trending chart, and its preprint corpus incompletely covers biomedical research. I will cover benchmark evidence, model-generated biological hypotheses, and the main validation gaps. Snapshot: 2026-11-06 02:21 UTC.

## Notable recent papers (ranked)

### 1. [BEND 2.0: Benchmarking the Capabilities Needed to Design DNA](https://arxiv.org/abs/2611.03806)
- **Abstract:** BEND 2.0 evaluates whether genomic models can predict the effects of DNA edits and use those predictions to guide sequence design.
- **Authors:** Andreas Bjerregaard; Rachael DeVries; Dionysia Danai Brilli; Panagiotis Antoniadis; Yan Li; Anders Krogh; Wouter Boomsma; Ole Winther; Frederikke Isa Marin.
- **arXiv:** `2611.03806v1` (published 2026-11-02 19:00:07 UTC; categories: `q-bio.GN`, `cs.LG`, `q-bio.QM`).
- **Evidence for ranking:** Covered by two independent research-news roundups (Intelligence Synthesis and HST Genomics); authors link a public leaderboard and code. Semantic Scholar returned 0 citations and 0 influential citations at snapshot, so this is limited attention evidence, not demonstrated adoption.
- **Claimed contribution:** The authors test eight tasks across five experimental datasets. They report frozen-representation linear readouts can match or beat native model outputs, while average-effect prediction can conceal weaker context-specific and mutation-interaction performance.
- **Caveat:** This is a benchmark on existing datasets, not prospective wet-lab confirmation of designed sequences. The authors note substantial room to improve context-specific and multi-cell design.
- **Announcement type:** new submission, 2026-11-04 announcement batch.
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods.

### 2. [iGC: Antibody Optimization via Reinforcement Learning over a Learned Somatic Hypermutation Prior](https://arxiv.org/abs/2611.05270)
- **Abstract:** iGC combines a learned somatic-hypermutation prior with reinforcement learning to optimize antigen-specific antibody sequences while constraining mutation patterns.
- **Authors:** Thao Nguyen; Robert G. Alberstein; Ewa Nowara; Homa Mohammadi-Peyhani; Holly R. Steach; Sarah A. Robinson; Yuval Shechter; Donald W. Lee; Jason A. Vander Heiden; Franziska Seeger; Andrew Leaver-Fay; Richard Bonneau; Joshua Yao-Yu Lin.
- **arXiv:** `2611.05270v1` (published 2026-11-03 17:55:25 UTC; categories: `cs.LG`, `q-bio.BM`).
- **Evidence for ranking:** Discussed in the same two independent research-news roundups as BEND 2.0; Semantic Scholar returned 0 citations and 0 influential citations. The authors also report comparisons against mutation-prediction baselines.
- **Claimed contribution:** The authors report the mutation prior more than doubles the strongest baseline on mutation-site prediction, and that optimized sequences retain somatic-hypermutation-like sequence structure while balancing reward and diversity.
- **Caveat:** The paper reports computational evaluation on existing repertoire, animal, and deep-mutational-scanning datasets; it describes no new animal experiments or prospective wet-lab validation of generated antibodies. Binding optimization is therefore not evidence of therapeutic efficacy.
- **Announcement type:** new submission, 2026-11-04 announcement batch.
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods.

### 3. [PeptSol: A Translational Benchmark for Protected-Peptide Solubility in Drug Manufacturing](https://arxiv.org/abs/2611.00749)
- **Abstract:** PeptSol provides a chemistry-aware benchmark for predicting solubility of protected peptide intermediates used in liquid-phase peptide synthesis.
- **Authors:** Alexander Arjun Lobo; Marc Saouda; Urvi Awasthi; Leonid Zhukov.
- **arXiv:** `2611.00749v2` (first submitted 2026-10-31 08:56:07 UTC; latest revision 2026-11-04 21:12:17 UTC; categories: `cs.LG`, `physics.chem-ph`, `q-bio.BM`).
- **Evidence for ranking:** The arXiv comment reports acceptance at the AI for Drug Discovery workshop, NeurIPS 2026; it also drew external research-summary coverage. Semantic Scholar returned 0 citations and 0 influential citations. Version 2 is a substantive update in this window.
- **Claimed contribution:** The authors curate 1,388 measurements, but these cover 84 parent sequences and 101 protected structures. Across seven frozen encoders, the best reported macro-F1 is 0.843 for binary solubility and 0.614 for the harder three-class task in the stated historical-subset split.
- **Caveat:** 92.5% of measurements come from one historical programme. The authors report no consistent foundation-model advantage over explicit chemical fingerprints and descriptors; external chemistry and synthesis programmes are needed to test transfer.
- **Announcement type:** revision (`v2`), 2026-11-05 batch (updated 2026-11-04 UTC).
- **Themes:** Biochemistry & proteins; Quantitative methods; Biomedical & translational medicine.

### 4. [Evolutionary characterization of whole-genome doubling across human cancers](https://arxiv.org/abs/2611.01897)
- **Abstract:** The authors examine genomic and multi-omic patterns associated with whole-genome doubling across 41,332 tumours from 12 cancer types.
- **Authors:** Yangyang Zhang; Haiming Li; Xiaoyu Zhao; Zilong Wang; Yongqi Chen; Sumeng Yang; Shaocong Mo; Jinming Li; Xiaohua Wu; Xu Wang; Shuo Wang; Qinhao Guo.
- **arXiv:** `2611.01897v1` (published 2026-11-01 13:39:58 UTC; categories: `q-bio.GN`, `q-bio.PE`).
- **Evidence for ranking:** Cross-listed in genomics and populations/evolution and surfaced in an independent genomics-paper index; Semantic Scholar returned 0 citations and 0 influential citations. Ranking reflects strong scope fit and dataset scale, not a measured attention lead.
- **Claimed contribution:** The authors report that driver mutations and homologous-recombination-deficiency mutagenesis generally precede doubling when both occur, and that post-doubling chromosome-arm losses vary less by cancer type. They also report reduced interferon-response and HLA-presentation programmes associated with epigenetic remodelling.
- **Caveat:** These are retrospective tumour-genomics associations, not causal tests of immune suppression or treatment response. Functional follow-up is needed before interpreting the proposed mechanisms.
- **Announcement type:** new submission, 2026-11-03 announcement batch.
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Biomedical & translational medicine.

### 5. [An auditable agentic pipeline for variant-to-gene prioritisation, validated against orthogonal functional evidence](https://arxiv.org/abs/2611.01461)
- **Abstract:** V2G records evidence retrieval and ranks candidate genes at GWAS loci; the authors test whether language-model reranking adds information beyond candidate ordering and prior knowledge.
- **Authors:** Shakuntala Baichoo; Sohail (Neel) Sarkar; Bo Wang.
- **arXiv:** `2611.01461v1` (published 2026-11-01 02:48:40 UTC; categories: `q-bio.GN`, `cs.AI`).
- **Evidence for ranking:** Covered in an independent genomics-paper index alongside the WGD study; Semantic Scholar returned 0 citations and 0 influential citations. Its explicit ablations make the evidence boundary unusually checkable.
- **Claimed contribution:** On 135 eligible held-out loci, the authors report Precision@1 of 0.793 versus 0.711 for the evidence ordering, but no detected difference from Open Targets L2G or training-membership baselines. Their ablations suggest the apparent gain largely reflects recall of known genes and anchoring to candidate order.
- **Caveat:** The authors report train/test overlap and note that the split does not fully separate associations. Performance on a constrained benchmark is not proof that retrieved molecular evidence caused better gene prioritisation.
- **Announcement type:** new submission, 2026-11-03 announcement batch.
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods.

### 6. [Predicting protein structures at any folding stage from sequence](https://arxiv.org/abs/2611.04287)
- **Abstract:** FoldScape generates protein conformational ensembles conditioned on folding progress, rather than predicting only a native-state structure.
- **Authors:** Lisheng Zhang; Qingsong Li; Zinan Xie; Yanting Yang; Qikui Yang; Peng Lu; Zhican Fu; Wentao Cui; Runtong Hou; Zhengwei Xie.
- **arXiv:** `2611.04287v2` (first submitted 2026-11-03 04:15:20 UTC; latest revision 2026-11-04 03:46:56 UTC; categories: `q-bio.BM`, `cs.AI`).
- **Evidence for ranking:** Independently indexed or summarized by Emergent Mind, Fugu-MT, and Papers.cool; Semantic Scholar returned 0 citations and 0 influential citations. Version 2 falls within the window.
- **Claimed contribution:** The authors train on about one million conformations from 10,000 sequences and report broader ensemble coverage than seed-varied AlphaFold 3 samples across three structural measures, while maintaining reconstruction accuracy over evaluated folding stages.
- **Caveat:** Broad coverage against generated AlphaFold ensembles is not validation against experimentally measured folding kinetics or equilibrium ensembles. The work combines simulated folding and mechanical-unfolding trajectories; authors say code and benchmark data are to be released on publication.
- **Announcement type:** revision (`v2`), 2026-11-04 batch (updated 2026-11-04 UTC).
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods.

### 7. [CellCanon: An Agentic Cellular World Model for Prediction, Explanation, and Observation-Driven Updating](https://arxiv.org/abs/2611.05890)
- **Abstract:** CellCanon combines single-cell expression prediction, evidence-grounded explanations, and updating from newly supplied observations.
- **Authors:** Zhaokang Liang; Shuyang Zhuang; Xiaoran Jiao; Hao Chen.
- **arXiv:** `2611.05890v1` (published 2026-11-04 03:29:21 UTC; categories: `q-bio.QM`, `cs.AI`).
- **Evidence for ranking:** Received an external research-summary feature; Semantic Scholar did not return a record in the batch lookup, so no citation signal is available. It is directly relevant to emerging single-cell response-modelling methods.
- **Claimed contribution:** On 339 held-out SciPlex3 conditions across three cell lines, the authors report improvements in differential-expression AUPRC and Macro-F1 over the best baseline, plus an observation-update simulation that does not change model weights.
- **Caveat:** These are held-out benchmark and simulated-feedback results, not prospective experimental confirmation of predicted drug responses. A small set of cell lines and benchmark conditions does not establish transfer to other systems.
- **Announcement type:** new submission, 2026-11-05 announcement batch.
- **Themes:** Omics & single-cell methods; Molecular & cell biology; Bioinformatics & sequence analysis.

### 8. [Coupling cellular trajectories and RNA kinetics on continuous expression manifolds with ManifoldVelo](https://arxiv.org/abs/2611.03056)
- **Abstract:** ManifoldVelo jointly estimates cell pseudotime and RNA-velocity dynamics using topology-conditioned continuous expression trajectories.
- **Authors:** Zhen Zhou; Jiachen Li; Yuan Liu; Xiaoyong Pan; Hong-Bin Shen.
- **arXiv:** `2611.03056v1` (published 2026-11-02 12:49:50 UTC; categories: `q-bio.QM`).
- **Evidence for ranking:** The authors provide numerical source tables and code; Semantic Scholar returned 0 citations and 0 influential citations. No independent technical discussion was located in the sampled search, so this ranks on direct RNA/single-cell relevance rather than demonstrated attention.
- **Claimed contribution:** The authors report improved pseudotime recovery in cyclic and branching simulations and directional agreement in velocity estimates, with real-data analyses consistent with differentiation stages and plate-held-out phase prediction.
- **Caveat:** RNA velocity and pseudotime are model-derived from transcriptomic snapshots, not direct observation of each cell's lineage. Real-data consistency is not independent lineage-tracing validation.
- **Announcement type:** new submission, 2026-11-03 announcement batch.
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods.

## Trending Research Themes

The selected papers suggest three recurring method clusters, not a field-wide shift. First, sequence models are being tested as design tools rather than only predictors: BEND 2.0 measures DNA-edit and design capabilities, while iGC applies constrained optimization to antibody sequences. Second, molecular modelling is moving toward operational constraints: PeptSol focuses on protected-intermediate solubility in peptide manufacturing, and FoldScape targets ensembles across folding stages. Both remain benchmark/model claims with meaningful validation gaps. Third, single-cell methods connect observations to dynamics and perturbation response: ManifoldVelo estimates RNA kinetics along inferred trajectories, while CellCanon predicts and updates responses across conditions. WGD and V2G add complementary genome-interpretation work, but neither should be conflated with experimentally established causal mechanisms.

## Open Problems and Research Directions

Author-stated boundaries include BEND 2.0's weaker performance on context-specific and multi-cell design; PeptSol's concentration of measurements in one historical programme; and V2G's incomplete association-level separation in train/test evaluation. The following are synthesis proposals, not claims of novelty or clinical utility:

- For BEND 2.0 and iGC, test model-selected DNA edits and antibody variants prospectively with blinded, matched wet-lab assays, including cell-context changes and negative controls; compare against simple sequence/chemistry baselines.
- For PeptSol, add measurements from independent synthesis programmes, protected scaffolds, and solvent families, then evaluate with scaffold- and programme-held-out splits.
- For V2G, rerun comparisons with association- and locus-family-separated splits, freeze candidate retrieval before reranking, and test whether evidence perturbations predictably alter gene choices.
- For FoldScape, compare predicted ensemble distributions against experimental time-resolved or single-molecule folding data, rather than only generated-ensemble coverage; clarify when simulated pathway samples approximate physical populations.
- For CellCanon and ManifoldVelo, validate on independent perturbation and lineage-tracing datasets, reporting calibration and failure cases across cell types, donors, and trajectory topologies.
- For WGD, use longitudinal or perturbation-controlled models to test whether the reported post-doubling immune-expression associations are causal and reproducible across tumour contexts.

## Takeaway

The strongest defensible thread is evaluation: several papers benchmark what biological models can predict, design, or explain, while their own results expose limits in transfer, context sensitivity, causal interpretation, or experimental confirmation. The week contains relevant computational proposals, not evidence that any method is clinically ready. Citation counts were absent or zero for this very recent set, so the ordering is a qualified relevance ranking rather than a readership chart.

## Method and sources

- **Window:** weekly, 2026-10-31 through 2026-11-06 inclusive; snapshot 2026-11-06 02:21:25 UTC. The final calendar day is partial at snapshot time.
- **Candidate query:** arXiv API search across `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`, constrained to `lastUpdatedDate:[202610310000 TO 202611062359]`. The broad query returned 71 unique records in one page (fewer than the 200-result page limit); cross-listed records were deduplicated by versionless ID. Recent category listings were checked for announcement dates, and each selected abstract page was verified.
- **Selection and ranking:** eight papers ranked by relevance to molecular biology/genomics/biomedicine, then checkable signals such as independent research-summary coverage, an arXiv workshop-acceptance comment, cross-listing, and a substantive revision. This is not a quantitative trend score. Semantic Scholar Graph API returned zero citations and zero influential citations for indexed selected papers; CellCanon was not returned. No citation velocity could be meaningfully inferred, and citation totals are not period gains.
- **Coverage limits:** arXiv has no official trending or readership chart. This corpus omits much experimental and clinical biology published on bioRxiv, medRxiv, or elsewhere; it is not representative of biomedical research. All biomedical claims above are attributed to the preprints and are not clinical recommendations.
- **Sources:** [arXiv API query](https://export.arxiv.org/api/query?search_query=%28cat%3Aq-bio.BM%20OR%20cat%3Aq-bio.GN%20OR%20cat%3Aq-bio.MN%20OR%20cat%3Aq-bio.SC%20OR%20cat%3Aq-bio.CB%20OR%20cat%3Aq-bio.TO%20OR%20cat%3Aq-bio.QM%20OR%20cat%3Acs.BI%20OR%20cat%3Aphysics.med-ph%29%20AND%20lastUpdatedDate%3A%5B202610310000%20TO%20202611062359%5D&sortBy=lastUpdatedDate&sortOrder=descending&start=0&max_results=200); selected [arXiv abstract pages](https://arxiv.org/abs/2611.03806), [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch); [Intelligence Synthesis research roundup](https://pharma.intelligence-synthesis.com/en/ai-science/); [HST Genomics roundup](https://hstgenomics.com/news_cn.html); [PeerRevenue genomics index](https://peerrevenue.com/papers/q-bio.GN); [Emergent Mind](https://www.emergentmind.com/papers/2611.04287), [Fugu-MT](https://fugumt.com/fugumt/paper_check/2611.04287v2), [Papers.cool](https://papers.cool/arxiv/2611.04287); [CellCanon summary](https://pulseaugur.com/cluster/342037-cellcanon-agentic-world-model-advances-biological-discovery).