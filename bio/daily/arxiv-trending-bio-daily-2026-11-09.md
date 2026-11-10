# arXiv Trending Biology and Biomedicine — Daily — 2026-11-09

## Headline

Latest arXiv biology/biomedicine batch (Monday, 9 November 2026): 15 notable papers selected. This uses the prior announcement batch; the 10 November batch was not yet announced at snapshot time. The clearest cluster is computational protein and genome modeling alongside single-cell analysis; two papers also test AI-guided experimental workflows against biological recordings or organoid assays. Today’s agenda: protein ensembles and design, genome and transcriptome efficiency, evaluation integrity, and the boundary between model predictions and experiments. arXiv has no official trending chart; this is an inferred relevance ranking from one batch and reported evidence, not popularity. Its biomedical coverage is incomplete.

## Notable recent papers (ranked by relevance)

### 1. [BioMARS 2.0: a robotic biologist for formulating and adapting biological experiments](https://arxiv.org/abs/2611.12139)
- **Abstract:** A human-in-the-loop robotic system links literature-grounded protocol generation, phenotype-guided retinal-organoid culture optimization, and researcher-led testing of six nominated drug candidates.
- **Authors:** Yibo Qiu, Zan Huang, Yilin Qiao, Ziyang Ling, Yi Wang, Zhengyang Lu, Hangke Peng, Haoliang Ye, Ao Tian, Shu'ang Sun, Handi Liu, Yuqing Long, Mohan Yang, Kan Ding, Zhenzhen Zhou, Di Wu, Yu Xiong, Yaxuan Han, Jun'ao Song, Haoran Zhang, Ronald X Xu, Mingzhai Sun
- **arXiv:** `2611.12139v1` (published 2026-11-09 09:51:45 UTC; categories: `cs.RO`, `q-bio.QM`)
- **Evidence for ranking:** Authors report expert-reviewed protocol scoring across four model backends, three rounds of robotic retinal-organoid condition selection, and six candidates advanced to wet-lab screening; this is unusually direct experimental feedback in the selected batch.
- **Claimed contribution:** The authors say BioMARS connects experiment formulation, culture adaptation and intervention selection in one workflow; the evidence comprises separate protocol, organoid-culture and drug-screen studies in the preprint.
- **Caveat:** The organoid work is a specific culture-optimization demonstration, and candidate screening is preliminary ATP-based in-vitro evidence; it establishes neither general laboratory autonomy nor therapeutic efficacy.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** Molecular & cell biology, Quantitative methods

### 2. [Toward Controlling Biology with Language: Offline Learning of Prompt-Conditioned Interventions for Cells, Organoids, and Biobots](https://arxiv.org/abs/2610.02247)
- **Abstract:** The revised study reanalyzes 155 archived xenobot recordings and trains a prompt-to-intervention model to map natural-language requests to electrical-pulse durations for behaviors that the pulse can control.
- **Authors:** Nam H. Le, Douglas Blackiston, Michael Levin, Josh Bongard
- **arXiv:** `2610.02247v2` (published 2026-09-30 16:49:01 UTC; updated 2026-11-09 17:09:57 UTC; categories: `q-bio.QM`, `cs.AI`, `cs.CV`, `cs.NE`, `cs.RO`)
- **Evidence for ranking:** The v2 update reports a full reanalysis with two independent trackers, eight measured behaviors, 176 instructions, and tests on unseen instructions and bots; stopping within ten minutes rose from 0/22 at pulses ≤30 seconds to 17/19 above 220 seconds.
- **Claimed contribution:** The authors report that an archive can support a calibrated language interface for three dose-responsive behaviors, while the model declines to claim control over behaviors not associated with pulse duration.
- **Caveat:** There is no sham-control group, only pulse duration is varied, and the results are associations and predictions from archived xenobot recordings—not causal evidence in human cells or a general language-to-biology interface.
- **Announcement type:** revision, announcement batch 2026-11-09 (US Eastern)
- **Themes:** Molecular & cell biology, Quantitative methods

### 3. [OriDynamics: Towards a World Model for Biomolecular Dynamics](https://arxiv.org/abs/2611.11958)
- **Abstract:** OriDynamics generates all-atom ensembles for proteins and protein–ligand or protein–protein complexes, aiming to model alternative conformations and coordinated atomic fluctuations.
- **Authors:** Jiahao Yang, Dong Liu, Hongliang Li, Ji Chen, Yuehua Liu, Daoyun Ding, Duo An, Jun Li, Jiahua Rao, Ziqiao Zhang, Peicong Lin, Shuangjia Zheng
- **arXiv:** `2611.11958v1` (published 2026-11-09 06:20:58 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** The preprint reports comparisons on protein and complex benchmarks for conformational coverage, fluctuation fidelity and interaction geometry, plus application analyses of alternative states, partner effects and ligand dissociation.
- **Claimed contribution:** The authors propose latent ensemble decomposition with ensemble-level supervision of means, fluctuation amplitudes and coordinate covariance as a computational route to context-dependent biomolecular ensembles.
- **Caveat:** Evidence is computational benchmark and case-study performance; generated ensembles are not direct biochemical measurements, and the paper’s “world model” language is an aspiration rather than demonstrated experimental utility.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** Biochemistry & proteins

### 4. [scBIG++: Learning Across Genes and Cells to Predict Single-Cell Perturbation Responses](https://arxiv.org/abs/2611.11217)
- **Abstract:** scBIG++ predicts single-cell transcriptional perturbation responses over all retained measured protein-coding genes using expression-adaptive gene modules and population-conditioned generation.
- **Authors:** Jiafa Ruan, Zican Qiao, Zongxin Yang, Ruijie Quan, Yi Yang
- **arXiv:** `2611.11217v1` (published 2026-11-08 08:08:31 UTC; categories: `cs.LG`, `cs.AI`, `q-bio.GN`)
- **Evidence for ranking:** Authors evaluate six genetic and chemical settings spanning 6,539–19,451 genes, including unseen targets and combinations, cross-cell-line transfer and held-out compounds; they report gains over scBIG on all three Norman protocols.
- **Claimed contribution:** The preprint claims that cell-adaptive gene grouping and exchange of information across control cells improve full-gene perturbation prediction and reconstruction.
- **Caveat:** This is retrospective computational evaluation of existing perturbation data, not a validation that the generated profiles reproduce new biological responses; rare states and diverse contexts remain open.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** RNA & transcriptomics, Omics & single-cell methods, Bioinformatics & sequence analysis

### 5. [HyPLM Technical Report](https://arxiv.org/abs/2611.12000)
- **Abstract:** HyPLM-Flash is a 650-million-parameter protein language model and inference engine designed to reduce protein-sequence modeling cost while retaining benchmark performance.
- **Authors:** Haowei Lin, Cai Zhou, Xiangxin Zhou
- **arXiv:** `2611.12000v1` (published 2026-11-09 07:37:34 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** The technical report compares 28 public checkpoints on 32 tasks, reports ProteinGym zero-shot Spearman 0.409, long-range contact precision 0.650 at L/5, and about 130,000 residues per second on one NVIDIA H20 (1.9–2.7× its compared 600M-class encoders).
- **Claimed contribution:** The authors claim a favorable accuracy–compute trade-off against the evaluated public models; these are benchmark results reported in the technical report.
- **Caveat:** The evidence is benchmark-based and hardware-specific; contact and fitness scores do not establish experimental protein function, and independent reproduction is not reported here.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** Biochemistry & proteins, Bioinformatics & sequence analysis

### 6. [GeneZip: Region-Aware Compression for Long Context DNA Modeling](https://arxiv.org/abs/2602.17739)
- **Abstract:** GeneZip allocates a limited token budget adaptively across DNA regions, compressing redundant sequence more strongly while preserving predictive information in functionally dense regions.
- **Authors:** Jianan Zhao, Xixian Liu, Zhihao Zhan, Xinyu Yuan, Hongyu Guo, Jian Tang
- **arXiv:** `2602.17739v4` (published 2026-02-19 09:53:35 UTC; updated 2026-11-09 03:04:05 UTC; categories: `q-bio.GN`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The v4 record reports 137.6-fold compression with a 0.31 validation-perplexity increase versus uncompressed Mamba2-84M, best average rank among leakage-controlled compression models on four DNA-long-context tasks, and 36.1× throughput on 450-kb inputs.
- **Claimed contribution:** The authors say region-aware compression can lower long-context DNA modeling cost and report that repeat-aware allocation also transfers to a nine-species panel.
- **Caveat:** These are computational language-model benchmarks; region labels guide training, and no downstream experimental genomics outcome is demonstrated in the abstract.
- **Announcement type:** revision, announcement batch 2026-11-09 (US Eastern)
- **Themes:** DNA & genomics, Bioinformatics & sequence analysis

### 7. [AI-based characterization of lymphoid structures and the tumor microenvironment reveals lower mature tertiary lymphoid structures, lymph-node follicles, and plasma cells after neoadjuvant therapy in lung squamous cell carcinoma](https://arxiv.org/abs/2611.12855)
- **Abstract:** A computational histology analysis compares lymphoid structures and immune-cell distributions in neoadjuvant-treated versus therapy-naive lung squamous cell carcinoma and tests prognostic associations in a separate cohort.
- **Authors:** Arne Schmidt, Justin Nieder, Cornelius Boehm, Julika Ribbat-Idel, Marius Teodorescu, Marie-Lisa Eich, Simon Schallenberg, Gabriel Dernbach, Katja Lingelbach, Miriam Haegele, Timo Milbich, Adam Narai, Maria Stoelben, Hans Pinckaers, Lukas Ruff, Kai Standvoss, Christian Watermann, Christiane Kuempers, Sven Perner, Verena Sailer, Jasmin Tiebach, Torsten Goldmann, Sebastian Marwitz, Johannes Braegelmann, Frederick Klauschen, Marija Pezer, Rosemarie Krupar
- **arXiv:** `2611.12855v1` (published 2026-11-09 18:45:06 UTC; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** The authors report matched cohorts of 20 treated and 20 untreated patients, pathologist-annotated model validation, and an independent cohort of 458 (46 treated); stromal plasma-cell density and co-localization were associated with longer survival in that validation cohort.
- **Claimed contribution:** The preprint reports treatment-associated differences in mature lymphoid structures and a candidate prognostic immune-cell axis, not a treatment effect or validated clinical biomarker.
- **Caveat:** The cohort comparison is observational and small in the treated group; residual confounding and prospective external validation are needed before prognostic or clinical use can be inferred.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** Biomedical & translational medicine, Molecular & cell biology

### 8. [When gene summaries reveal the answers: Gene Ontology circularity in gene embedding benchmarks](https://arxiv.org/abs/2611.11118)
- **Abstract:** The study tests whether generated gene summaries expose Gene Ontology labels to text-embedding benchmarks, inflating apparent gene-function prediction performance.
- **Authors:** Jiawei Wu, Huishu Wang, Junlin Chen, Hongyi Wang
- **arXiv:** `2611.11118v1` (published 2026-11-08 04:05:52 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Generated summaries covered 6,172 of 19,256 human protein-coding genes; removing them lowered per-gene AUROC by 0.078 (95% bootstrap interval 0.072–0.084) for a linear probe among genes with 1–10 linked papers, with related effects in mouse and yeast.
- **Claimed contribution:** The authors argue that benchmark inputs can leak evaluation annotations through generated summaries and introduce GeneProv for matched-text and alternative-endpoint evaluation.
- **Caveat:** The authors state the historical GO scorer mishandled ties and original predictions are unavailable for rescoring, limiting how precisely the earlier benchmark results can be corrected.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** DNA & genomics, Bioinformatics & sequence analysis

### 9. [Co-folding model guided by structural proteomics](https://arxiv.org/abs/2605.26192)
- **Abstract:** AIMS-Fold guides a pretrained co-folding model using both attractive and repulsive structural-proteomics constraints to predict proximity-inducing drug complexes without retraining.
- **Authors:** Alon Shtrikman, Sagie Brodsky, Michal Ran Shchory, Nitzan Simchi, Yaron Ben Shoshan-Galeczki, Eran Seger, Kirill Pevzner
- **arXiv:** `2605.26192v2` (published 2026-05-25 14:54:08 UTC; updated 2026-11-09 09:37:15 UTC; categories: `cs.LG`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** The v2 report tests 28 PROTAC, glue and antibody complexes that Boltz-2 fails on; for 100 generated models across 20 seeds it reports 86% correct conformations with guidance versus 14% unguided.
- **Claimed contribution:** The authors report that using negative as well as positive structural-proteomics evidence can improve in-silico complex-geometry recovery.
- **Caveat:** The reported endpoint is structural-model recovery, not compound activity, degradation, binding or therapeutic efficacy; the evaluated complex set is limited.
- **Announcement type:** revision, announcement batch 2026-11-09 (US Eastern)
- **Themes:** Biochemistry & proteins, Biomedical & translational medicine

### 10. [Efficient and Accurate Zero Shot Generation of Symmetric Protein Complexes](https://arxiv.org/abs/2611.10424)
- **Abstract:** ZeUS uses symmetry-aware generation to convert existing equivariant backbones into efficient zero-shot generators of symmetric protein assemblies.
- **Authors:** Rory Gao, Yuanzhou Chen, Prajit Rajkumar, Wei Wang
- **arXiv:** `2611.10424v1` (published 2026-11-07 02:59:07 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** The preprint applies its method to FrameDiff, FoldFlow and RFdiffusion, reports minimal degradation in generation quality, and demonstrates computational generation of assemblies exceeding 10,000 residues; arXiv lists it as a NeurIPS 2026 conference paper.
- **Claimed contribution:** The authors use a quotient-space formulation and canonical-subunit inference to reduce memory and runtime with no retraining.
- **Caveat:** Evidence concerns generated structures and computational efficiency; the paper does not establish that the designed assemblies express, fold or assemble experimentally.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** Biochemistry & proteins

### 11. [KineCouple: Substrate-conditioned residual readout for enzyme kinetic prediction](https://arxiv.org/abs/2611.09377)
- **Abstract:** KineCouple uses substrate-conditioned attention over residue features to predict enzyme kcat and Km values from sequence and substrate representations.
- **Authors:** Chun Kang, Yunbo Zhang, Fanhu Zeng, Jian Liu, Siwei Deng, Lei Sha
- **arXiv:** `2611.09377v2` (published 2026-11-06 12:17:54 UTC; updated 2026-11-09 12:46:02 UTC; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** The v2 update reports pooled out-of-fold CataPro results with small improvements over reproduced CataPro: kcat RMSE 1.333→1.330 and PCC 0.492→0.496; Km RMSE 0.998→0.997 and PCC 0.633→0.634.
- **Claimed contribution:** The authors propose substrate-conditioned residue weighting as a modest improvement to computational enzyme-kinetics prediction.
- **Caveat:** The reported gains are small and benchmark-based; no new enzyme kinetics measurements or independent wet-lab validation are described in the abstract.
- **Announcement type:** revision, announcement batch 2026-11-09 (US Eastern)
- **Themes:** Biochemistry & proteins, Quantitative methods

### 12. [stMIND: Learning multiscale interaction dynamics from spatial-temporal transcriptomics](https://arxiv.org/abs/2611.12228)
- **Abstract:** stMIND infers local and long-range cell-interaction dynamics from spatial-temporal transcriptomic snapshots, jointly modeling molecular state, position and proliferation.
- **Authors:** Longquan Li, Lin Wan
- **arXiv:** `2611.12228v1` (published 2026-11-09 11:22:30 UTC; categories: `q-bio.QM`)
- **Evidence for ranking:** Authors report benchmark performance on axolotl and zebrafish datasets, ablation support for combining local and nonlocal operators, and an inferred axolotl telencephalon regenerative transition 10–15 days after injury.
- **Claimed contribution:** The authors interpret the model’s inferred drift components as scale-specific interactions and describe developmental and regenerative trajectories from snapshots.
- **Caveat:** Because sequencing samples different cells at each time point, inferred trajectories and interactions are model-based rather than direct tracking or causal perturbation evidence.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** RNA & transcriptomics, Omics & single-cell methods, Quantitative methods

### 13. [Rethinking One Gene, One Token: Transcriptome-Aware Tokenization for Single-Cell Foundation Models](https://arxiv.org/abs/2611.05410)
- **Abstract:** scTAT assigns variable token slots to recurring gene sets or individual genes on a per-cell basis, aiming to reduce compute without losing cell-type annotation quality.
- **Authors:** Jiaqi Xiong, Jiaying Li, Yu Zheng, Xiang Zhou, Ziteng Wang, Xinting Hu, Jiaxin Qi
- **arXiv:** `2611.05410v2` (published 2026-10-21 08:29:29 UTC; updated 2026-11-09 06:27:56 UTC; categories: `q-bio.GN`)
- **Evidence for ranking:** The v2 update reports matching a strong one-gene-per-token model in frozen-embedding cell-type annotation with half the token budget and nearly halving transformer matrix-multiplication cost.
- **Claimed contribution:** The authors argue that transcriptome-aware grouping can improve token efficiency while retaining gene-resolution reconstruction.
- **Caveat:** Reported benefits are benchmark and computational outcomes; robustness across tissues, protocols and downstream biological tasks needs independent assessment.
- **Announcement type:** revision, announcement batch 2026-11-09 (US Eastern)
- **Themes:** RNA & transcriptomics, Omics & single-cell methods

### 14. [Pruning DNA Sequence](https://arxiv.org/abs/2611.10386)
- **Abstract:** Sequence Pruning dynamically drops genomic sequences that become easy for a DNA language model to predict, reducing pretraining work without a separate scoring pass.
- **Authors:** Faias Satter, Shaker Islam, Aminul Islam
- **arXiv:** `2611.10386v1` (published 2026-11-07 01:42:12 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** The authors evaluate five pretraining settings across two corpora, three model families and two objectives, plus five genomic benchmarks; they report up to 96% less data processing and little loss at 4% of baseline GPU hours.
- **Claimed contribution:** The preprint claims dynamic sequence-level pruning can lower DNA-model training cost and sometimes improve downstream benchmark scores.
- **Caveat:** The efficiency/performance claims are tied to the evaluated training and genomic benchmarks; broad transfer to other genomes, objectives and experimental tasks remains untested.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** DNA & genomics, Bioinformatics & sequence analysis

### 15. [ProtLink: Sequence and Multispecies Graph Context for Protein Interaction Prediction](https://arxiv.org/abs/2611.11017)
- **Abstract:** ProtLink combines frozen protein-sequence embeddings with human and multispecies interaction-network context to predict protein–protein interactions.
- **Authors:** Xingyuan Zhang
- **arXiv:** `2611.11017v1` (published 2026-11-07 23:32:13 UTC; categories: `cs.LG`, `q-bio.MN`)
- **Evidence for ranking:** In controlled three-seed comparisons, the authors report AP 0.9701±0.0022 for a full multispecies graph model versus 0.9435±0.0094 for orthogroup-only; for held-out proteins, multispecies HGT reaches 0.8335±0.0094 versus 0.6482±0.0052 for a sequence-only pair model.
- **Claimed contribution:** The preprint reports that multispecies graph context can help PPI prediction, with benefits depending on message-passing depth and evaluation split.
- **Caveat:** Average precision depends on the negative-sampling protocol, and predicted held-out edges or proteins are not direct experimental interaction measurements.
- **Announcement type:** new submission, announcement batch 2026-11-09 (US Eastern)
- **Themes:** Biochemistry & proteins, Molecular & cell biology

## Trending Research Themes

The selected batch clusters around model-building and evaluation rather than a single new experimental theme. Protein structure and function methods recur in OriDynamics (conformational ensembles), HyPLM (sequence representations), ZeUS (symmetric assembly generation), AIMS-Fold (constraint-guided co-folding), KineCouple (enzyme kinetics) and ProtLink (interaction prediction). These are distinct computational tasks, not independent experimental confirmation.

A second strand targets the efficiency and fidelity of genome- and transcriptome-scale computation: GeneZip and Sequence Pruning reduce DNA-model sequence/training cost; scBIG++ predicts perturbation responses across measured genes; scTAT changes single-cell tokenization; and the Gene Ontology circularity paper shows how input provenance can inflate benchmark scores.

Two papers put more weight on biological feedback or measurements: BioMARS links a robotic organoid workflow to human-run screening, while the revised xenobot study audits archived pulse-response recordings. The lung-cancer histology analysis and stMIND add observational tissue and snapshot-derived spatial dynamics, respectively; neither alone establishes causal mechanisms or clinical utility.

## Open Problems and Research Directions

Biological validation for computational predictions. OriDynamics, HyPLM, ZeUS, AIMS-Fold, KineCouple and ProtLink report structural, sequence or interaction benchmarks. Follow-up work could test preregistered predictions with matched biochemical binding/kinetics assays, expression and assembly checks, and hard negative controls, using held-out targets not used in model development. This would separate improved benchmark fit from experimentally useful prediction.

Robustness across experimental contexts. BioMARS and the xenobot revision demonstrate feedback or reanalysis in particular settings; proposed follow-ups include multi-lab replication across cell types and batches. For pulse-to-behavior claims, add sham stimulation and vary control parameters independently. For scBIG++, scTAT and stMIND, test donors, tissues, rare states and perturbations outside training distributions, then compare predictions with new single-cell measurements.

Benchmark provenance and clinical translation. The Gene Ontology circularity study motivates matched-input, time-separated and non-GO endpoint evaluation for gene models. The lung-cancer paper’s candidate prognostic axis could be assessed in a prospectively specified, independent cohort with treatment and stage confounders addressed; the present observational associations do not establish a clinical biomarker.

## Takeaway

This batch is notable for computational tools that model protein structure, sequence and cell-state responses, with a smaller but important set of studies connecting algorithms to organoid or archived biological measurements. The strongest next evidence would be blinded, out-of-distribution replication and direct assays. The ordering is inferred by relevance and reported study design—not official arXiv popularity—and the corpus misses much biomedical preprint activity.

## Method and sources

Window: daily; announcement batch dated 2026-11-09 (US Eastern), released by the 2026-11-10 UTC snapshot. The batch covers first submissions from 2026-11-06 19:00:00 UTC through 2026-11-09 19:00:00 UTC; revisions are included when the latest version was updated in that period. Snapshot: 2026-11-10 17:14:51 UTC. This is the prior announcement batch; the 2026-11-10 batch was not yet announced by the snapshot.

Candidate discovery used the configured categories `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`, plus cross-listed records. The broad newest-first query returned 200 records back to 2026-10-27, beyond the selected batch; a separate last-updated scan returned 200 records back to 2026-10-31, beyond the update window. Cross-listed IDs were deduplicated. Fifteen papers were chosen from the relevant candidate pool; this is a selection, not an exhaustive daily feed. Every selected arXiv abstract page was checked; the first three entries were also read in PDF for study design, results and limitations.

Ranking is explicitly relevance-led because there is no dependable attention signal for this very recent batch. Signals are the reported evaluation design, biological fit, category breadth, and substantive update status where applicable. No download/view claims or period citation gains are inferred. Semantic Scholar citation momentum and independent discussion are not used as evidence here. All results and limitations are attributed to the preprints; computational predictions, in-vitro assays, observational cohorts and clinical evidence are distinguished.

Category query: `https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200`.

Sources: each linked arXiv abstract page is the primary source; PDF links are available from those records. arXiv listing/API metadata supplied version, author, date, category, comments and revision information. The ranking is not an official arXiv list and does not cover bioRxiv, medRxiv or the biomedical literature as a whole.
