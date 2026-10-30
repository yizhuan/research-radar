# Monthly arXiv Biology & Biomedicine — 2026-10-30

## Headline

Window: 1–30 October 2026 UTC; snapshot 2026-10-30T03:31:50Z. The latest candidate update present in arXiv’s API index was 29 October. Eleven notable papers are selected. The dominant pattern is computational modeling across transcriptomes, genomic data, RNA/protein structure and molecular dynamics, alongside a smaller set of papers with direct antibody or spatial-proteomics experiments. Agenda: antibody discovery, tumor spatial proteomics, then single-cell and molecular-modeling methods. arXiv has no official trending chart; this is a relevance-ranked snapshot of an incomplete biomedical corpus, not a measure of readership. Most clinical and experimental biology preprints appear outside arXiv, including bioRxiv and medRxiv.

## Top papers (ranked)

Because checkable attention evidence is sparse, this is a list of notable recent papers ranked by relevance to molecular biology/biomedicine and the evidence reported—not a measured popularity or readership ranking. New submissions and revisions are marked separately.

### 1. [Multimodal reasoning for broadly neutralizing antibody discovery from label-free human B cell repertoires across virus families](https://arxiv.org/abs/2610.03160)
- **Abstract:** The authors describe a closed-loop AI system for screening unsorted human B-cell repertoires and report antibody discovery assays plus protective activity for selected antibodies in a mouse influenza challenge.
- **Authors:** Hantao Lou, Jianqing Zheng, Can Yue, Meihan Zhang, Yuanchao Bao, Yu Chen, Mengting Huang, Yupeng Yang, Qianyu Pan, Nana Fu, Yansong Shi, Hongli Li, Yangyang Chai, Ruyi Chen, Wansheng Li, Zhu Liang, Rongmei Yao, Yuanhan Mo, Lei Wang, Chunmei Wang, Yun Quan, Qiong Zhang, Xiangxi Wang, Xuetao Cao
- **arXiv:** `2610.03160v1` (latest version published 2026-10-02T11:35:34Z; first submitted 2026-10-02; categories: `q-bio.QM`, `cs.AI`, `cs.CE`, `q-bio.CB`)
- **Evidence for ranking:** Direct immunology relevance, cross-listed in q-bio.CB and AI/computation, and the abstract reports cloning/neutralization assays plus an animal challenge; ranked for relevance and evidence type, not popularity.
- **Claimed contribution:** The authors claim ImmuneAgent combines repertoire, sequence, structure and experimental feedback to prioritize broadly neutralizing antibodies; among 110 cloned candidates, they report 60 neutralizing antibodies and 12 broadly neutralizing antibodies, with five tested antibodies protecting mice in a lethal influenza challenge.
- **Caveat:** This is preclinical evidence: 110 cloned candidates and five antibodies in the mouse challenge, not a human trial; the authors state the experiment was not powered to establish equivalence to the comparator.
- **Announcement type:** new submission, 2026-10-02
- **Themes:** Biochemistry & proteins, Biomedical & translational medicine, Omics & single-cell methods

### 2. [AI-guided deep visual proteomics reveals recurrence-associated morpho-molecular signatures within triple-negative breast cancers](https://arxiv.org/abs/2608.03145)
- **Abstract:** The authors use recurrence-risk heatmaps to guide spatial proteomics in triple-negative breast cancer and report molecular differences between AI-defined high- and low-risk tumor regions.
- **Authors:** Yesung Cho, Ji Hwan Park, Chan Il Kim, Hyewon Kim, Honglan Li, Yumin Lee, Geongyu Lee, Sujeong Hong, Seong Min Park, Yoonyoung Lee, Hee Sool Rho, Sumin Lee, Amos Chungwon Lee, Changhwan Lee, Hwanyoung Shim, Hyunwook Kim, Hyeji Shin, Sanha Park, Jihoon Yu, Yoon Hee Shin, Sooheon Kim, Hyunjin Park, Seung Min Park, Sangwan Kim, Yujung Kim, Jinwon Jeong, Sung-Im Do, Eun-Young Kim, Dongmyung Shin, Ingu Do, Jongbae Park
- **arXiv:** `2608.03145v3` (latest version published 2026-10-27T06:22:13Z; first submitted 2026-08-04; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Substantive revisions v2 (23 Oct) and v3 (27 Oct) within the window, direct protein-level tissue measurements, and a larger patient-level evaluation; q-bio.QM cross-list.
- **Claimed contribution:** The authors report mass-spectrometry profiling of 46 AI-selected regions from two recurrent cases and derive a 13-protein composite; in an expanded TNBC cohort, combining it with the H&E score raises out-of-bag C-index from 0.679 to 0.739 and 5-year time-dependent AUC from 0.675 to 0.770.
- **Caveat:** The spatial discovery set comprised only two selected recurrence cases; the authors call the regional programs recurrence-associated rather than causal and note that independent TNBC cohorts with more recurrence events are needed.
- **Announcement type:** revision, 2026-10-27
- **Themes:** Biochemistry & proteins, Biomedical & translational medicine, Omics & single-cell methods

### 3. [Panoramic modelling of single-cell transcriptomes at scale with CellNet](https://arxiv.org/abs/2610.21943)
- **Abstract:** CellNet represents single-cell transcriptomes using DNA-derived gene identities and expression, with the authors reporting pretraining on 231 million profiles across 40 species and evaluations of cell-state and gene-expression prediction.
- **Authors:** Xiaoqing Lian, Pei Liu, Jiahui Tan, Luoda Tan, Chaoyi Li, Quan Zou, Chen Lin, Xiangxiang Zeng
- **arXiv:** `2610.21943v1` (latest version published 2026-10-15T14:17:14Z; first submitted 2026-10-15; categories: `q-bio.GN`)
- **Evidence for ranking:** Core q-bio.GN fit and unusually broad transcriptomic resource (231 million profiles, 40 species); selected for scope and evaluated breadth, not for measured readership.
- **Claimed contribution:** The authors claim the image-based model supports broader coding and non-coding RNA coverage; reported evaluations include rare-cell/state recognition, withheld-gene prediction, cross-species transfer and retrieval of known molecular modules.
- **Caveat:** The paper is computational; performance varies for sparsely detected non-coding RNAs, and its discussion says inferred gene associations need independent functional validation.
- **Announcement type:** new submission, 2026-10-15
- **Themes:** RNA & transcriptomics, Omics & single-cell methods, Bioinformatics & sequence analysis

### 4. [Cohort Effects, Not Treatment Response, Dominate Public Immunotherapy Cohorts: Evidence from Microbiome and Tumor Genomic Data](https://arxiv.org/abs/2610.33010)
- **Abstract:** The authors test pooled immunotherapy microbiome and tumor-genomic cohorts and report that cohort/site differences can exceed treatment-response signals in these public datasets.
- **Authors:** Amey Garg
- **arXiv:** `2610.33010v1` (latest version published 2026-10-08T01:32:17Z; first submitted 2026-10-08; categories: `q-bio.QM`, `q-bio.GN`, `stat.AP`)
- **Evidence for ranking:** Cross-listed in q-bio.GN and q-bio.QM; arXiv comment says an extended version was accepted to the IEEE BIBM 2026 Workshop Proceedings; code and a Zenodo record are linked.
- **Claimed contribution:** Across four public microbiome cohorts (39–283 patients), the authors report response effects at chance level while cohort effects remain; in three tumor-genomic cohorts (n=223), they report a small response signal beside a much larger cohort effect, and provide a chance-correction tool.
- **Caveat:** The negative microbiome result applies to the four analyzed cohorts and their response definitions; the authors note that other public cohorts were not analyzed, so it does not establish that microbiome-response associations are absent in general.
- **Announcement type:** new submission, 2026-10-08
- **Themes:** Biomedical & translational medicine, Omics & single-cell methods, Quantitative methods

### 5. [STRAND: Sequence-Conditioned Transport for Single-Cell Perturbations](https://arxiv.org/abs/2602.10156)
- **Abstract:** STRAND conditions single-cell perturbation-response predictions on the regulatory DNA sequence at the targeted locus, rather than representing an intervention only by a gene identifier.
- **Authors:** Boyang Fu, Sameer Gabbita, George Dasoulas, Xiang Lin, Shanghua Gao, Xiaorui Su, Soumya Ghosh, Marinka Zitnik
- **arXiv:** `2602.10156v2` (latest version published 2026-10-27T17:50:07Z; first submitted 2026-02-10; categories: `q-bio.GN`, `cs.LG`, `q-bio.CB`)
- **Evidence for ranking:** Substantive v2 revision on 27 Oct, relevant q-bio.GN/q-bio.CB cross-lists, NeurIPS 2026 journal reference, and four total Semantic Scholar citations at the snapshot (a current total, not monthly gains).
- **Claimed contribution:** On CRISPRi screens in K562, Jurkat and RPE1 cells, the authors report improved few-shot/unseen-gene benchmarks and held-out-cell-line transfer, with up to 33% improvement in perturbation discrimination and up to 0.12 gain in held-out-cell-line ΔPearson.
- **Caveat:** These are predictions evaluated against existing CRISPRi measurements; the work does not show that prospective STRAND-selected perturbations have been experimentally validated.
- **Announcement type:** revision, 2026-10-27
- **Themes:** Gene regulation & epigenetics, RNA & transcriptomics, Bioinformatics & sequence analysis

### 6. [A unified coarse-grained neural network potential for the dynamics of biomolecular complexes](https://arxiv.org/abs/2610.37606)
- **Abstract:** AMARO v2.0 is presented as a heavy-atom coarse-grained neural potential for protein, drug-like molecule and complex dynamics, with tests on 262 complexes across 11 targets.
- **Authors:** Antonio Mirarchi, Stephen E. Farr, Adrià Peréz, Gianni De Fabritiis
- **arXiv:** `2610.37606v1` (latest version published 2026-10-27T17:37:10Z; first submitted 2026-10-27; categories: `q-bio.BM`)
- **Evidence for ranking:** New q-bio.BM submission on 27 Oct; the paper directly addresses biomolecular-complex dynamics and benchmarks 262 complexes across 11 targets.
- **Claimed contribution:** The authors report ligand-pose retention and improved recovery of a trypsin–benzamidine crystal pose per estimated GPU-time versus atomistic molecular mechanics, plus case studies on TYK2, SHP2 and CDK8.
- **Caveat:** This is computational molecular simulation, not experimental binding evidence; the authors report overly favorable binding free energies and pose/site-specificity failures in some systems.
- **Announcement type:** new submission, 2026-10-27
- **Themes:** Biochemistry & proteins, Quantitative methods

### 7. [Reducing double-dipping in single-cell topic models with three-way count splitting](https://arxiv.org/abs/2610.24130)
- **Abstract:** The authors propose three-way count splitting for single-cell topic models to reduce false discoveries caused when a model uses the same counts later used for gene-topic inference.
- **Authors:** Zheng Qu
- **arXiv:** `2610.24130v1` (latest version published 2026-10-16T19:02:33Z; first submitted 2026-10-16; categories: `q-bio.GN`, `cs.LG`)
- **Evidence for ranking:** New q-bio.GN/cs.LG submission; the evaluated 104,400-cell cohort and null/permutation tests directly address a common inference failure in single-cell analysis; code and results are public.
- **Claimed contribution:** On a 104,400-cell lupus cohort with permuted null genes, the authors report that three-way splitting reduced nominal 5% null rejection to 7.7%, versus 36% for naive tests and 38% for the usual two-way split; they also report related results for LDVAE/scETM and a pre-specified COVID-19 cohort.
- **Caveat:** The paper is a statistical-method evaluation, not evidence that topic models improve clinical prediction; it explicitly does not claim better clustering, prediction or topic stability.
- **Announcement type:** new submission, 2026-10-16
- **Themes:** RNA & transcriptomics, Omics & single-cell methods, Quantitative methods

### 8. [RNAGenScape: Property-Guided, Optimized Generation of mRNA Sequences with Manifold Langevin Dynamics](https://arxiv.org/abs/2510.24736)
- **Abstract:** RNAGenScape constrains property-guided mRNA sequence generation to a learned data manifold; across three datasets, the authors report gains in oracle-predicted properties and viability proxies.
- **Authors:** Danqi Liao, Chen Liu, Xingzhi Sun, Dié Tang, Haochen Wang, Scott Youlten, Srikar Krishna Gopinath, Haejeong Lee, Ethan C. Strayer, Antonio J. Giraldez, Smita Krishnaswamy
- **arXiv:** `2510.24736v5` (latest version published 2026-10-19T04:16:21Z; first submitted 2025-10-14; categories: `q-bio.QM`, `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Substantive v4/v5 revisions on 10 and 19 Oct, q-bio.BM and cs.LG cross-lists, NeurIPS 2026 comment, and evaluation across three real-world mRNA datasets.
- **Claimed contribution:** The authors report up to 267% higher median oracle-predicted property gain and up to 31% higher success rate than compared generative methods while maintaining computational viability proxies.
- **Caveat:** The gains are based on computational oracles and proxies; the abstract does not report wet-lab translation, protein-expression or vaccine efficacy validation.
- **Announcement type:** revision, 2026-10-19
- **Themes:** RNA & transcriptomics, Bioinformatics & sequence analysis, Quantitative methods

### 9. [Leveraging secondary-structure information for accurate nucleic acid structure prediction with OFoldNA](https://arxiv.org/abs/2609.37414)
- **Abstract:** OFoldNA adds secondary-structure information to all-atom nucleic-acid folding and protein–nucleic-acid co-folding; the authors report benchmark improvements when secondary-structure information is available.
- **Authors:** Valhalla Team
- **arXiv:** `2609.37414v2` (latest version published 2026-10-08T07:49:40Z; first submitted 2026-09-29; categories: `q-bio.BM`)
- **Evidence for ranking:** A v2 revision on 8 Oct falls inside the window; directly relevant q-bio.BM paper focused on DNA/RNA structure and benchmarked on FoldBench/CHANRG.
- **Claimed contribution:** The authors report leading FoldBench results for nucleic-acid monomer and protein–nucleic-acid co-folding without external secondary structure, further gains with accurate or partial base-pairing inputs, and out-of-distribution RNA secondary-structure performance on CHANRG.
- **Caveat:** Reported outcomes are structure-prediction benchmarks; they do not establish experimental structures, binding, or function, and gains with supplied secondary structure depend on the quality of that input.
- **Announcement type:** revision, 2026-10-08
- **Themes:** Molecular & cell biology, RNA & transcriptomics, Quantitative methods

### 10. [HELICS: Biobank-scale Conditional Synthetic Genome Generation via Latent Flow Matching](https://arxiv.org/abs/2610.36361)
- **Abstract:** HELICS generates conditional synthetic genome-wide SNP profiles using latent flow matching, with training on more than 417,000 UK Biobank genomes and external genotype-fidelity evaluation.
- **Authors:** Ahmad Abdel-Azim, Xihong Lin
- **arXiv:** `2610.36361v1` (latest version published 2026-10-26T22:25:36Z; first submitted 2026-10-26; categories: `q-bio.GN`, `cs.LG`)
- **Evidence for ranking:** New q-bio.GN/cs.LG submission on 26 Oct; arXiv comment names NeurIPS 2026; reported training scale exceeds 417,000 genomes.
- **Claimed contribution:** The authors report better fidelity than compared haplotype-based simulators for common-variant data, including allele-frequency agreement and local/long-range SNP correlation preservation, and demonstrate conditioning on ancestry and genetic-liability summaries.
- **Caveat:** The reported fidelity is not proof of privacy protection, clinical validity or causal effects; training/evaluation are centered on UK Biobank and common variants, limiting straightforward generalization to other ancestries and rare variants.
- **Announcement type:** new submission, 2026-10-26
- **Themes:** DNA & genomics, Biomedical & translational medicine, Quantitative methods

### 11. [RiboBridge: protein-conditioned de novo RNA binder structure design](https://arxiv.org/abs/2610.30668)
- **Abstract:** RiboBridge separates RNA conformation generation from protein–RNA assembly and evaluates predicted binder structures on a temporally split benchmark of 124 protein–RNA complexes.
- **Authors:** Zhou Zhang, Hanqun Cao, Minghao Sun, Odin Zhang, Yang Zhang, Pheng Ann Heng, Wujun Li, Tianfan Fu
- **arXiv:** `2610.30668v1` (latest version published 2026-10-22T03:32:07Z; first submitted 2026-10-22; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** New q-bio.BM/cs.LG cross-listed submission on 22 Oct; evaluates 124 complexes with redundancy/temporal controls, making it directly relevant to molecular design methods.
- **Claimed contribution:** The authors report improved complex-structure recovery against compared methods using a structure-first pipeline that proposes protein-surface interfaces and bridges RNA/protein coordinate frames.
- **Caveat:** This is computational structure generation, not proof of RNA–protein binding or activity; the authors state that post-hoc native information selects among generated candidate pockets and that functional validation remains future work.
- **Announcement type:** new submission, 2026-10-22
- **Themes:** Biochemistry & proteins, RNA & transcriptomics, Bioinformatics & sequence analysis

## Trending Research Themes

• Multimodal and foundation-style modeling of molecular information: CellNet broadens single-cell RNA representation; STRAND conditions perturbation predictions on regulatory DNA; HELICS generates synthetic genotypes; RNAGenScape optimizes mRNA; OFoldNA and RiboBridge address nucleic-acid folding/design; AMARO models biomolecular complexes. These are diverse methods, not independent evidence of a single validated biological discovery.
• AI-guided experimental interrogation: ImmuneAgent reports cloned antibody assays and a mouse challenge, while the TNBC visual-proteomics study uses image-derived risk maps to select tissue regions for mass spectrometry. These are the clearest direct experimental components in this selected set, but neither is a human clinical validation.
• Evaluation and study-design safeguards: the cohort-effects paper quantifies site/cohort confounding in public immunotherapy omics; the three-way count-splitting paper tests false discoveries in single-cell topic models; STRAND and CellNet report held-out settings. Together these papers emphasize that cross-cohort calibration, leakage control and independent validation matter as much as headline benchmark scores.

## Open Problems and Research Directions

• Independent validation of designed biomolecules. RNAGenScape reports oracle-predicted mRNA property gains, RiboBridge reports structure recovery, OFoldNA reports structural benchmarks, and AMARO reports simulation outcomes. Follow-up could test blinded designs with cell-free translation/ expression assays, binding/activity assays, and prospective structure measurements; computational scores should be calibrated against these assays.
• Generalizability and privacy of synthetic or predicted omics. HELICS is trained on UK Biobank and reports genotype fidelity, while CellNet and STRAND evaluate cross-species or held-out-cell settings. Follow-up could use ancestry-balanced external biobanks, donor/site-held-out tests, rare-variant strata and explicit membership-inference/privacy audits before synthetic data are treated as safe to share.
• Replication of spatial and immune findings. The TNBC spatial discovery profiled 46 regions from two recurrent cases and calls the signals associative; ImmuneAgent reports 110 cloned candidates but only five antibodies tested in the mouse challenge, which was not powered for equivalence. Larger independent TNBC cohorts with prespecified recurrence horizons and prospectively blinded antibody selection/animal studies would test reproducibility; neither result is clinical efficacy evidence.
• Cohort harmonization in translational omics. The cohort-effects paper analyzed four microbiome cohorts and three tumor-genomic cohorts, leaving additional public cohorts untested. A follow-up could harmonize collection, sequencing and response definitions across the remaining datasets, then prospectively test whether chance-corrected response signals replicate within sites and across sites.

## Takeaway

October’s selected arXiv biology/biomedicine papers are method-heavy: generative and foundation models are being applied to genomes, RNA, proteins and spatial omics, while a few studies connect models to tissue or animal experiments. The strongest next test is external, prospectively designed validation. No entry here should be read as a clinical recommendation or practice-changing evidence.

## Method and sources

• Window: 2026-10-01 through 2026-10-30 UTC; snapshot: 2026-10-30T03:31:50Z. Monthly eligibility includes a new arXiv version first posted or last updated in this interval. Latest arXiv API-index update observed at snapshot: 2026-10-29.
• Candidate query: `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, paginated in descending `lastUpdatedDate` order until entries fell before 1 October. This yielded 480 distinct records with an in-window version update: 291 v1 submissions and 189 later-version records (including 155 papers first submitted before October). Cross-listed records were deduplicated by versionless arXiv ID. All selected abstract pages and current version histories were checked.
• Selection: 11 papers ranked by direct relevance to biochemistry, RNA/DNA/genomics or biomedical methods, then the reported evidence type and category breadth. Semantic Scholar returned a current total of 4 citations for STRAND; the remaining citation evidence was too sparse to support a popularity/velocity ranking. That count is not a gain during October. Independent attention was not inferred from novelty, authorship or title.
• Sources: arXiv API and each linked arXiv abstract/version history; selected full-text sections were read where extraction was practical (CellNet, ImmuneAgent and the TNBC spatial-proteomics paper). Other supporting records are linked inline (STRAND code, topic-model code/Zenodo, and the accepted-workshop/code record for the cohort-effects study). Semantic Scholar record: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2602.10156?fields=citationCount%2CinfluentialCitationCount.
• Coverage warning: arXiv is not representative of biomedical preprints or the clinical literature; bioRxiv and medRxiv are outside this corpus. Claims above are attributed to the preprints. Computational predictions, biochemical/cell/animal evidence and human-cohort associations are distinguished; no patient-specific advice is offered.
