# arXiv Trending Biology and Biomedicine — Weekly, 2026-11-20

## Headline

Biology and biomedicine | week 14–20 November 2026 UTC, latest included announcement batch 19 November | 10 notable papers. The dominant pattern is computational method-building paired with targeted validation: epithelial-barrier experiments, antibody campaigns, and fermentation models sit alongside spatial-omics tools. Agenda: distinguish measurements in cells and fermentation from benchmark-only predictions, then identify where external validation is still needed. arXiv has no official trending chart; this relevance-led ranking is inferred from incomplete signals and arXiv does not represent the full biomedical preprint or medical literature.

## Notable recent papers (ranked by demonstrated relevance)

### 1. [Reasoning in the loop: antibody lead optimization by probing mechanism and measurement](https://arxiv.org/abs/2611.19812)
- **Abstract:** Two antibody lead-optimization campaigns combine an AI agent, mechanistic interpretation of assay curves, designed mutation libraries, and follow-up measurements.
- **Authors:** Samuel Stanton, Aaron Solomon, Emily Delaney, Melanie Montgomery, Crystal Humphries, Timothy Acker, Ryan Henrici, Charbel Eid, Eddie Abrams, Peyton Greenside
- **arXiv:** `2611.19812v1` (published 2026-11-15T05:55:18Z; categories: `cs.LG`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** The authors report two scaffold-specific campaigns, seven rounds, roughly 1,010 variants, controlled comparisons, and assay changes tested against pre-registered predictions; the full paper includes raw-curve analysis.
- **Claimed contribution:** The authors report improved affinity, thermal stability, and aggregation metrics for both leads while maintaining or improving yield and purity; the VHH lead is reported at 1.15 nM KD versus 10.3 nM for its parent.
- **Caveat:** Only two campaigns on one company platform are reported. Lead measurements rest on one or two replicates, the scFv affinity assay approaches its resolution limit, and the paper discloses that Anthropic paid BigHat for the laboratory work. These are not clinical or safety outcomes.
- **Announcement type:** new submission, announcement batch 2026-11-17
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 2. [Rule-based curation and validation in batch fermentation of a genome-scale metabolic model of the mycoprotein fungus Fusarium venenatum A3/5](https://arxiv.org/abs/2611.21775)
- **Abstract:** A curated genome-scale metabolic model for Fusarium venenatum is tested against oxygen-enriched batch fermentation data on glucose and fructose.
- **Authors:** Jaewook Lee, Thomas Vinestock, Miao Guo
- **arXiv:** `2611.21775v1` (published 2026-11-16T19:05:11Z; categories: `q-bio.MN`)
- **Evidence for ranking:** Compared Draft and curated models across four fermentation batches: final-biomass discrepancy falls from 20% to 6%; an independent technical post also discussed the model’s energy-yield correction.
- **Claimed contribution:** The authors report that rule-based curation corrects ATP-yield errors; sequential sugar uptake plus a fitted lag time lowers time-course RMSE from 4.88 to 0.42 g/L.
- **Caveat:** Evidence is limited to oxygen-enriched batches on glucose/fructose at one total-sugar level; the lag time is fitted to those same time courses, and glucose cases still overpredict final biomass by 6–9%. The authors disclose Quorn funding for two authors.
- **Announcement type:** new submission, announcement batch 2026-11-18
- **Themes:** Molecular & cell biology; Quantitative methods; Bioinformatics & sequence analysis

### 3. [Structured AI ideation yields physical strategies for epithelial barrier repair](https://arxiv.org/abs/2611.22988)
- **Abstract:** Abelio structures AI research ideation and reports two independently tested physical interventions that restored barrier readouts in damaged Caco-2 monolayers.
- **Authors:** Geonho Nah, Johyun Park, Kyung-Ah Cho, Suyoung Hwang, Yoon Hee Lim, Eun-kyung Min, Seunghyun Moon, Donghyun Koh, Seungwon Kim, Jiho Park, Hojin Yoo, Myungsun Nam, Haneul Choi, Kyungsu Kim, In-Sun Hong, YunJae Jung, Minhyeong Lee
- **arXiv:** `2611.22988v1` (published 2026-11-17T16:05:22Z; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Its Ideation Core was compared with four frontier LLMs on 50 research objectives; the paper also reports two proposals archived before independent laboratory tests in damaged Caco-2 monolayers.
- **Claimed contribution:** The authors report that membrane-tethered PEG preserved barrier function and cholesterol-anchored complementary DNA enabled sequence-specific, reversible restoration in their cell model.
- **Caveat:** The biological validation is in damaged Caco-2 monolayers, not organoids, animals, or humans. Scientific-soundness benchmarking uses an LLM judge, and the intervention structures are proposed rather than directly observed.
- **Announcement type:** new submission, announcement batch 2026-11-18
- **Themes:** Molecular & cell biology; Biomedical & translational medicine; Quantitative methods

### 4. [Horizontal Flow Matching for Single-Cell Spatiotemporal Dynamics](https://arxiv.org/abs/2611.24764)
- **Abstract:** HORIZON uses horizontal flow matching to model cell abundance, gene expression, and tissue geometry while discounting shared rigid motion in spatial-transcriptomic time courses.
- **Authors:** Zihan Wang, Jianzhe Li, Zhenyi Zhang, Peijie Zhou
- **arXiv:** `2611.24764v1` (published 2026-11-18T17:16:53Z; categories: `cs.LG`, `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Evaluated on a simulated tissue and four spatial-transcriptomics time courses; the authors report improved reconstruction and interpolation of held-out developmental stages against existing trajectory methods.
- **Claimed contribution:** The method learns tissue dynamics up to shared translation and rotation, reducing coordinate-frame artifacts in inferred cell movement.
- **Caveat:** The reported evidence is computational evaluation on four datasets plus simulation; inferred trajectories and cell correspondences are not direct lineage-tracing observations or new biological experiments.
- **Announcement type:** new submission, announcement batch 2026-11-19
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Quantitative methods

### 5. [Biases and Limits of AlphaFold Predictions for Non-Globular Proteins](https://arxiv.org/abs/2611.24546)
- **Abstract:** The authors examine experimentally validated examples in which AlphaFold predictions for non-globular proteins diverge from biologically relevant structural states, emphasizing molecular context.
- **Authors:** Maria Cristina Aspromonte, Alexander M. Monzon, Miguel A. Andrade-Navarro, Oriol Bárcenas, Viktor Bartosik, Pau Bernadó, Juan Cortés, Zsuzsanna Dosztanyi, Gabor Erdos, Isabella C. Felli, Helena Gradišar, San Hadži, Tamás Hegedűs, Khalil Joron, Pavel Kaderavek, Eitan Lerner, Dirk Linke, Pablo Mier, Ana Pantelić, Roberta Pierattelli, Salvador Ventura, Marija Vidović, Metaxia Vlassi, Lukas Zidek, Silvio C. E. Tosatto
- **arXiv:** `2611.24546v1` (published 2026-11-18T14:51:02Z; categories: `q-bio.BM`)
- **Evidence for ranking:** Directly relevant protein-structure assessment grounded in experimentally validated cases; the paper appeared in the q-bio.BM corpus during the window.
- **Claimed contribution:** The authors argue that interpreting non-globular protein predictions requires accounting for molecular context and biological state rather than reading a predicted structure as a single definitive conformation.
- **Caveat:** The abstract describes case-based analysis but gives no sample count or population-wide error estimate, so it does not quantify AlphaFold accuracy for all non-globular proteins.
- **Announcement type:** new submission, announcement batch 2026-11-19
- **Themes:** Biochemistry & proteins; Quantitative methods

### 6. [STORM: A Lightweight Structure-Free Model for Binding Affinity Prediction](https://arxiv.org/abs/2611.23777)
- **Abstract:** STORM predicts small-molecule–protein binding affinity without requiring a complex structure, transferring information from related measured molecules.
- **Authors:** Ayush Pandit, Rohan V. Koodli, Wei Deng, Roxana Daneshjou, Ron O. Dror
- **arXiv:** `2611.23777v1` (published 2026-11-18T03:34:08Z; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** The authors compare against Boltz-2 on multiple evaluation datasets and report inference and training speed improvements exceeding five orders of magnitude.
- **Claimed contribution:** STORM ensembles lightweight models over diverse protein and molecule representations, with the authors reporting accuracy comparable to or better than Boltz-2 on their evaluated sets.
- **Caveat:** This is retrospective computational benchmarking; the abstract reports no prospective wet-lab confirmation, and performance depends on the availability and quality of historical affinity measurements.
- **Announcement type:** new submission, announcement batch 2026-11-19
- **Themes:** Biochemistry & proteins; Quantitative methods; Bioinformatics & sequence analysis

### 7. [OCCAM: Improved Single-Cell Representation Learning and Perturbation Effect Prediction](https://arxiv.org/abs/2611.21959)
- **Abstract:** OCCAM combines denoised cell representations with gene-interaction, text, and protein-sequence features to predict perturbation responses across cell contexts.
- **Authors:** Ihab Bendidi, Kian Kenyon-Dean, Alisandra K. Denton, Auguste Genovesio, Emmanuel Noutahi
- **arXiv:** `2611.21959v1` (published 2026-11-16T22:40:16Z; categories: `q-bio.QM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Compared with four retrained competitors and transfer baselines in cross-context few-shot settings, held-out cell lines/assays, and double perturbations.
- **Claimed contribution:** The authors report better capture of measured response patterns and stronger perturbation discrimination in the evaluated settings, including composition of single-gene responses for double perturbations.
- **Caveat:** Expression-level prediction remains challenging, and the results are computational evaluations on existing perturbation data rather than new perturbation experiments or universal evidence of generalization.
- **Announcement type:** new submission, announcement batch 2026-11-18
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Bioinformatics & sequence analysis

### 8. [Diversity Preservation Recovers Transcription Factor Motifs Across Challenging Confounder Landscapes](https://arxiv.org/abs/2611.21859)
- **Abstract:** A diversity-preserving MAP-Elites search improves transcription-factor motif recovery under confounding, tested on five liver ChIP-seq datasets.
- **Authors:** Alejandro Medina, Mary Lauren Benton
- **arXiv:** `2611.21859v1` (published 2026-11-16T20:23:15Z; categories: `cs.NE`, `q-bio.GN`)
- **Evidence for ranking:** Each archive ranks the target motif first in at least 13 of 30 seeds on all five datasets; comparisons use HOCOMOCO validation and MEME run on the same sequences.
- **Claimed contribution:** The authors report that preserving a diverse motif-search archive avoids collapse to one motif and improves recovery when motif width is constrained.
- **Caveat:** HNF4A and JUND remain difficult to distinguish from close relatives across the full width range; computational motif recovery does not itself establish new binding events.
- **Announcement type:** new submission, announcement batch 2026-11-18
- **Themes:** DNA & genomics; Gene regulation & epigenetics; Bioinformatics & sequence analysis

### 9. [A structure-based model of the bacterial chemosensory array reveals how the scaffolding protein CheW tunes sensory responses](https://arxiv.org/abs/2611.23921)
- **Abstract:** A cryo-EM-structure-based Ising model tests how the scaffold protein CheW changes cooperativity, sensitivity, and dynamics in bacterial chemosensory arrays.
- **Authors:** David Hathcock, Yingxin Zheng, Yuhai Tu
- **arXiv:** `2611.23921v1` (published 2026-11-18T06:11:15Z; categories: `physics.bio-ph`, `cond-mat.stat-mech`, `q-bio.MN`)
- **Evidence for ranking:** The model reproduces previously reported CheW-dependent response changes and generates specific, testable predictions about CheW placement and single-cell activity fluctuations.
- **Claimed contribution:** The authors propose that CheW abundance and spatial organization tune effective coupling between core signaling units and can shift fluctuations from relaxational toward oscillatory behavior.
- **Caveat:** The dynamical signatures, including oscillations near native CheW levels, are model predictions awaiting single-cell measurement; distinct coupling settings can yield similar static responses.
- **Announcement type:** new submission, announcement batch 2026-11-19
- **Themes:** Molecular & cell biology; Biochemistry & proteins; Quantitative methods

### 10. [multiCAsp: Spatially Informed Canonical Association Analysis of Multi-Omic Data](https://arxiv.org/abs/2611.20580)
- **Abstract:** multiCAsp integrates spatially resolved molecular modalities with graph-Laplacian latent factors to identify shared variation across tissue locations.
- **Authors:** Ziqi Mu, Qiuyi Wu, Zhicheng Ji, Pixu Shi
- **arXiv:** `2611.20580v1` (published 2026-11-16T06:04:03Z; categories: `stat.ME`, `q-bio.QM`)
- **Evidence for ranking:** Simulation comparisons are supplemented by applications to macaque-cortex metabolomic/proteomic data and human renal-carcinoma gene/protein data, including cross-animal transfer analysis.
- **Claimed contribution:** The authors report improved latent-factor recovery in simulations and spatially coherent factors in two real multi-omic applications, with protein-abundance prediction from metabolomic measurements in macaque cortex.
- **Caveat:** The real-data results are computational associations and predictions, not causal validation; generality beyond these applications and measured modalities remains to be established.
- **Announcement type:** new submission, announcement batch 2026-11-17
- **Themes:** Omics & single-cell methods; Quantitative methods; Molecular & cell biology

## Trending Research Themes

Experimental cell and protein work is represented by Abelio’s epithelial-barrier proposals and the antibody campaigns; the authors report tests in cell monolayers or antibody assays, not clinical studies. STORM is a computational affinity tool, while the AlphaFold case analysis asks how context affects structural interpretation and the CheW model uses a known complex structure to make dynamic predictions. These are distinct evidence levels, not one validated pipeline.

Spatial and perturbation inference recurs in HORIZON, OCCAM, and multiCAsp. Each reconstructs or predicts molecular/cellular state from measured datasets, but uses different targets—tissue motion, perturbation response, and cross-modal latent factors. Motif recovery adds a DNA-regulatory method evaluated against ChIP-seq and a motif database. Finally, the Fusarium model is a notable bridge from genome-scale computation to fermentation data; its fitted time-course component should not be mistaken for an out-of-sample prediction.

## Open Problems and Research Directions

For the two antibody leads, the authors themselves call for confirmation runs, larger replicate counts, and a more sensitive affinity platform for the scFv; independent replication should also test whether the revised assay metrics hold on additional antibody scaffolds. The fermentation model needs tests across more sugar mixtures, concentrations, and independent batches, separating fitted lag-time agreement from prediction on held-out fermentations.

For Abelio’s barrier interventions, replication in independent laboratories and more physiologically complex intestinal models could test whether effects persist beyond the reported Caco-2 setup. For STORM, prospective blinded screening followed by biochemical affinity assays would test transfer to new compounds and targets. For OCCAM, HORIZON, and multiCAsp, useful follow-ups include external cell/tissue cohorts, held-out subjects or sections, and calibration of uncertainty in inferred trajectories and factors. For CheW, single-cell time-series measurements across controlled CheW abundance and placement could test predicted oscillatory signatures. These are research proposals, not clinical recommendations.

## Takeaway

This week’s most persuasive biomedical work in the selected pool couples methods with concrete validation contexts: Caco-2 barrier assays, antibody measurements, and fermentation batches. Other entries improve computational inference on existing omics or affinity datasets. The evidence remains bounded to cell models, narrow fermentation settings, and retrospective benchmarks; it does not establish clinical utility.

## Method and sources

Window: 2026-11-14 through 2026-11-20 inclusive (UTC), covering papers first submitted or materially revised in the seven-calendar-day interval. Snapshot: 2026-11-20 02:27:54 UTC. The broad arXiv API query covered q-bio.BM, q-bio.GN, q-bio.MN, q-bio.SC, q-bio.CB, q-bio.TO, q-bio.QM, cs.BI, and physics.med-ph, with submittedDate or lastUpdatedDate inside the window. It returned 60 unique versionless records in one page (fewer than the 200-result page size); recent-list announcement dates were cross-checked in the configured q-bio category listings. All 10 selected abstract pages were checked directly. All selected entries are v1 new submissions; none is a revision.

Ranking: arXiv has no official trend/readership chart. Semantic Scholar Graph API returned zero current citations and zero influential citations for all 10 selected records at the snapshot. The list is therefore titled “Notable recent papers” and ranked by molecular/biomedical relevance and checkable validation design, with independent discussion as a secondary signal. Citation totals are snapshots, not gains during the week.

An important recency distinction: a candidate newly uploaded to arXiv this week but already published in a 2024 journal was not treated as a new research development. The arXiv corpus is not representative of biomedical research; much experimental and clinical preprint activity appears on bioRxiv or medRxiv, and this is not a systematic or clinical evidence review.

Category query:

```text
(cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph) AND ((submittedDate:[202611140000 TO 202611202359]) OR (lastUpdatedDate:[202611140000 TO 202611202359]))
```

Sources: [arXiv API](https://export.arxiv.org/api/query); the 10 linked arXiv abstract pages; [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/ARXIV:2611.21775?fields=title,authors,year,citationCount,influentialCitationCount,referenceCount,publicationTypes,fieldsOfStudy,externalIds); [independent discussion of the Fusarium model](https://x.com/kdpisda/status/2123259178986946936).
