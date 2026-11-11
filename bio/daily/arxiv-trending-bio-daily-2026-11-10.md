# arXiv Trending Biology and Biomedicine — Daily — 2026-11-10

## Headline

Daily bio/biomed report for the latest announcement batch labeled Tuesday, 10 November 2026. Seven papers are selected from 40 distinct papers across the accessible configured category listings (41 category appearances before deduplication). The dominant pattern is computational biology: protein-structure and molecular-dynamics models alongside transcriptomic prediction and evaluation. The spoken agenda is a quick tour from molecular ensembles and protein design to spatial expression, perturbation modeling, and benchmark reliability. arXiv has no official trending chart; attention evidence is sparse, so this is an inferred ranking by relevance and reported evaluation—not a popularity ranking—and arXiv's biomedical coverage is incomplete.

The snapshot was taken on 11 November 2026 at 01:17 UTC. It uses the prior announcement batch labeled 10 November; no batch labeled 11 November was available at snapshot time.

## Notable recent papers (ranked by relevance, not popularity)

### 1. [OriDynamics: Towards a World Model for Biomolecular Dynamics](https://arxiv.org/abs/2611.11958)
- **Abstract:** OriDynamics generates all-atom conformational ensembles for proteins and protein/ligand complexes, aiming to model both broad state diversity and coordinated atomic fluctuations.
- **Authors:** Jiahao Yang, Dong Liu, Hongliang Li, Ji Chen, Yuehua Liu, Daoyun Ding, Duo An, Jun Li, Jiahua Rao, Ziqiao Zhang, Peicong Lin, Shuangjia Zheng
- **arXiv:** `2611.11958v1` (published 2026-11-09 06:20:58 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct biomolecules-category fit; the authors report comparisons across four ensemble benchmark settings. Semantic Scholar recorded 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report improved conformational coverage, fluctuation fidelity, and interaction geometry versus leading baselines, with computational examples of alternative states and partner-dependent ensembles.
- **Caveat:** The evidence is structural benchmark and in-silico application work; the preprint does not establish biochemical function or experimentally measured binding/dissociation.
- **Announcement type:** new submission, 10 November 2026 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [Efficient and Accurate Zero Shot Generation of Symmetric Protein Complexes](https://arxiv.org/abs/2611.10424)
- **Abstract:** ZeUS adapts pretrained SE(3)-equivariant backbone generators to create symmetric protein assemblies without retraining, by generating a canonical subunit and using symmetry-aware computation.
- **Authors:** Rory Gao, Yuanzhou Chen, Prajit Rajkumar, Wei Wang
- **arXiv:** `2611.10424v1` (published 2026-11-07 02:59:07 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct biomolecules-category fit; arXiv notes publication at NeurIPS 2026, and the paper compares three backbone models across symmetry settings. Semantic Scholar recorded 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report comparable designability/diversity to full-complex inference with predicted O(k) memory and runtime savings, and generation of very large symmetric backbones.
- **Caveat:** The authors state that biological validity at the largest scales remains untested: these are backbone-only structures, and designability is intractable for the largest examples.
- **Announcement type:** new submission, 10 November 2026 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [stMIND: Learning multiscale interaction dynamics from spatial-temporal transcriptomics](https://arxiv.org/abs/2611.12228)
- **Abstract:** stMIND infers continuous gene-expression, spatial, and proliferation dynamics from unmatched spatial-transcriptomics snapshots by modeling cell-intrinsic, local, and nonlocal influences.
- **Authors:** Longquan Li, Lin Wan
- **arXiv:** `2611.12228v1` (published 2026-11-09 11:22:30 UTC; categories: `q-bio.QM`)
- **Evidence for ranking:** Direct quantitative-biology listing; evaluated on axolotl regeneration and zebrafish development against four baselines, with five random seeds reported. Semantic Scholar recorded 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report stronger short-horizon expression prediction and spatial coherence on those datasets, and infer a 10–15-day post-injury transition in axolotl telencephalon.
- **Caveat:** Dynamics and interaction operators are inferred from destructive, unmatched snapshots rather than tracked cells; at long horizons the paper reports that a non-spatial baseline has lower expression error.
- **Announcement type:** new submission, 10 November 2026 batch
- **Themes:** RNA & transcriptomics; Molecular & cell biology; Quantitative methods

### 4. [HyPLM Technical Report](https://arxiv.org/abs/2611.12000)
- **Abstract:** HyPLM-Flash is a 650-million-parameter protein language model and inference engine that the authors present as a compute-efficient alternative for protein representation tasks.
- **Authors:** Haowei Lin, Cai Zhou, Xiangxin Zhou
- **arXiv:** `2611.12000v1` (published 2026-11-09 07:37:34 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Cross-listed in machine learning and biomolecules; the technical report compares 28 public checkpoints across 32 tasks. Semantic Scholar recorded 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report training on 726 billion tokens, throughput around 130,000 residues/s on one NVIDIA H20 GPU, and competitive results across the stated benchmark suite.
- **Caveat:** These are author-reported computational benchmarks; throughput is hardware- and implementation-dependent, and benchmark performance is not experimental validation of protein function.
- **Announcement type:** new submission, 10 November 2026 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 5. [scBIG++: Learning Across Genes and Cells to Predict Single-Cell Perturbation Responses](https://arxiv.org/abs/2611.11217)
- **Abstract:** scBIG++ predicts full-gene single-cell expression responses to genetic or chemical perturbations while modeling heterogeneity across cells and shared gene modules.
- **Authors:** Jiafa Ruan, Zican Qiao, Zongxin Yang, Ruijie Quan, Yi Yang
- **arXiv:** `2611.11217v1` (published 2026-11-08 08:08:31 UTC; categories: `cs.LG`, `cs.AI`, `q-bio.GN`)
- **Evidence for ranking:** Cross-listed in genomics, machine learning, and AI; the authors evaluate six perturbation settings, including unseen targets/combinations and transfer settings. Semantic Scholar recorded 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report competitive recovery of perturbation effects and reconstruction across all assayed protein-coding genes retained after preprocessing.
- **Caveat:** The contribution is prediction on benchmark data; it does not show that predicted gene-expression changes reproduce in new wet-lab perturbation experiments.
- **Announcement type:** new submission, 10 November 2026 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Bioinformatics & sequence analysis

### 6. [KineCouple: Substrate-conditioned residual readout for enzyme kinetic prediction](https://arxiv.org/abs/2611.09377)
- **Abstract:** KineCouple uses substrate-conditioned attention over protein residues to predict enzyme kcat and Km values from sequence and substrate representations.
- **Authors:** Chun Kang, Yunbo Zhang, Fanhu Zeng, Jian Liu, Siwei Deng, Lei Sha
- **arXiv:** `2611.09377v2` (first submitted 2026-11-06 12:17:54 UTC; revised 2026-11-09 12:46:02 UTC; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Cross-listed in AI and quantitative biology; v2 is the substantive update in the selected batch, evaluated on pooled out-of-fold CataPro predictions. Semantic Scholar recorded 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report small improvements over reproduced CataPro results for both kcat and Km prediction.
- **Caveat:** Reported gains are marginal (for example, kcat RMSE 1.333 to 1.330 and Km RMSE 0.998 to 0.997); these are prediction metrics, not biochemical assay results.
- **Announcement type:** revision (v2), 10 November 2026 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 7. [When gene summaries reveal the answers: Gene Ontology circularity in gene embedding benchmarks](https://arxiv.org/abs/2611.11118)
- **Abstract:** The paper tests whether gene-description text already contains Gene Ontology labels used to evaluate gene embeddings, and proposes a benchmark for comparing models with matched input text.
- **Authors:** Jiawei Wu, Huishu Wang, Junlin Chen, Hongyi Wang
- **arXiv:** `2611.11118v1` (published 2026-11-08 04:05:52 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Cross-listed in machine learning and genomics; the authors analyze 19,256 human protein-coding genes and report parallel checks in mouse and yeast. Semantic Scholar recorded 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** They report that removing generated GO-derived summaries reduces function-prediction AUROC in several settings and introduce GeneProv to evaluate text/label provenance and non-GO endpoints.
- **Caveat:** The paper says its historical GO scorer mishandled ties and the original predictions were unavailable for rescoring, limiting exact reproduction of some estimates.
- **Announcement type:** new submission, 10 November 2026 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

## Trending Research Themes

- Protein modeling is moving beyond a single predicted structure toward ensembles and scalable assembly generation: OriDynamics models conformational variability, ZeUS reduces the cost of symmetric backbone generation, and HyPLM-Flash targets efficient learned protein representations. These are computational results; they do not by themselves establish molecular function or experimental designability.
- Transcriptome methods are modeling more than cell labels: stMIND reconstructs spatial-temporal expression dynamics from tissue snapshots, while scBIG++ predicts heterogeneous perturbation responses across genes and cells. Their evidence is benchmark-based and should be separated from direct causal or wet-lab validation.
- Evaluation quality is an explicit concern across biological AI: KineCouple reports small gains on enzyme-kinetics benchmarks, while GeneProv highlights possible input/label overlap in gene-function evaluation. Together they support careful external testing, not a claim that one benchmark issue generalizes to every biological model.

## Open Problems and Research Directions

- **Validate generated molecular states experimentally.** OriDynamics evaluates ensemble statistics computationally; ZeUS notes that the largest backbone-only structures cannot yet be assessed for designability. Follow-up work could test representative predicted conformational populations and interfaces with independent structural or biochemical measurements, and assess whether large assemblies fold and assemble as designed. This is a proposed validation path, not evidence that the current systems are ready for use.
- **Test inferred tissue dynamics against independent time-resolved evidence.** stMIND infers trajectories from unmatched snapshots and reports weaker long-horizon expression errors than a non-spatial baseline in some comparisons. A useful next analysis would hold out later stages and compare predicted spatial neighborhoods with lineage tracking or independently collected spatial-transcriptomic samples; perturbing predicted local versus nonlocal influences could test whether the learned operators are causal.
- **Strengthen perturbation and enzyme-prediction benchmarks.** For scBIG++, evaluate predictions on independent cell lines, donors, and genuinely held-out intervention combinations, ideally with new measured profiles. For KineCouple, test whether its small CataPro gains persist on external enzyme–substrate pairs and whether uncertainty identifies cases where assays are most informative.
- **Make gene-embedding evaluations provenance-aware.** GeneProv's reported GO circularity and scoring caveat motivate matched-text splits, independent annotation sources, and non-GO functional outcomes, with the benchmark scorer and original predictions preserved for reproducibility.

## Takeaway

The batch is strongest in computational protein modeling and transcriptomic inference, with useful attention to benchmark reliability. The central uncertainty is not whether these models can produce compelling predictions, but how well those predictions survive independent experimental, temporal, and out-of-distribution checks. The list is a relevance-ranked snapshot, not evidence that these are the most-read papers.

## Method and sources

- **Window:** daily announcement batch labeled 2026-11-10; exact batch-date range 2026-11-10 through 2026-11-10. Snapshot: 2026-11-11 01:17 UTC; the latest batch is therefore the prior batch relative to the UTC calendar date. The arXiv API feed reported `updated=2026-11-11T01:17:55Z`.
- **Candidate query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date descending. The first 200 API results extended back beyond the selected batch; recent category listings were checked for the configured q-bio and medical-physics categories. Those listings showed 41 category entries, deduplicated to 40 arXiv IDs. The `cs.BI` term was included in the API query; no `cs.BI` entries appeared in the recent API sample, and its current recent-listing page was not available.
- **Selection and ranking:** seven papers selected for direct molecular, genomic, or biomedical relevance and the scope of reported evaluation. arXiv has no official popularity chart. Semantic Scholar Graph API records were requested by arXiv ID with `title, authors, year, citationCount, influentialCitationCount, referenceCount, publicationTypes, fieldsOfStudy, externalIds`; at the snapshot each selected paper had 0 citations and 0 influential citations. Targeted web searches did not surface independently verifiable technical discussion for the selected papers. Counts are current totals, not citation gains during this batch. Ranking therefore prioritizes relevance and evidence reported by the authors, not measured attention.
- **Verification:** each selected arXiv abstract page was checked for authors, version, submission/revision history, categories, and abstract. The introduction/results/discussion or limitations were also checked in the PDFs for the top three: [OriDynamics](https://arxiv.org/pdf/2611.11958v1), [ZeUS](https://arxiv.org/pdf/2611.10424v1), and [stMIND](https://arxiv.org/pdf/2611.12228v1). Claims above are attributed to the preprints; computational prediction is not described as experimental or clinical validation.
- **Sources:** [q-bio.BM recent](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN recent](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN recent](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC recent](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB recent](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO recent](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM recent](https://arxiv.org/list/q-bio.QM/recent), [medical physics recent](https://arxiv.org/list/physics.med-ph/recent), and Semantic Scholar Graph API (`https://api.semanticscholar.org/graph/v1/paper/batch`).