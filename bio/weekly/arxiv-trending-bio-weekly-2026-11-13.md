# arXiv Biology and Biomedicine: Notable Recent Papers — Week of Nov 7–13, 2026

This week's scan covers 10 notable papers, led by protein-interaction models and experimental validation, with a second strand in single-cell genomics and benchmark quality. Spoken agenda: what new molecular models actually validate, and where biological evaluation can still mislead. arXiv has no official trending chart; this is an inferred relevance ranking from incomplete signals, and arXiv does not represent the broader biomedical preprint or clinical literature.

## Notable recent papers (ranked)

### 1. [Emergent Biological Capabilities in a Foundation Model for Molecular Interactions](https://arxiv.org/abs/2611.14504)
- **Abstract:** Bonbon learns protein–ligand interaction representations and reports zero-shot mechanism, binding-site, and bond-type predictions, followed by prospective compound testing.
- **Authors:** Adi Mashiach
- **arXiv:** `2611.14504v1` (published 2026-11-10T18:53:01Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** NeurIPS 2026 Main Track Oral acceptance; an independent Astrobiology write-up appeared Nov 12; also cross-listed in q-bio.BM. Semantic Scholar returned zero citations for this fresh record, so citation momentum is not a signal here.
- **Claimed contribution:** The authors report a 3.2-trillion-token paired-sequence model, scaling tests across 42M–1.6B parameters, and a prospective 61.5% dose-response hit rate across nine disease targets in seven protein families. The PDF also describes 1,176 PDB complexes, including 394 sequence-dissimilar held-out proteins, for binding-site analyses.
- **Caveat:** The authors say reported capabilities are coarse-grained and do not produce explicit 3D coordinates; the prospective hit rate is not clinical evidence, and model weights/data are not openly released.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine

### 2. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](https://arxiv.org/abs/2611.13348)
- **Abstract:** ProTEUS combines sequence, evolutionary, and structural representations with iterative experimental feedback to select higher-order protein variants.
- **Authors:** Yikun Zhang; Minghao Guo; Guangxue Xu; Peter Yichen Chen; Wojciech Matusik; Wengong Jin; Jingjing Chai; Kaiyi Jiang
- **arXiv:** `2611.13348v1` (published 2026-11-09T23:19:33Z; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** Cross-listed in q-bio.BM and cs.AI; the paper has a public project page and a Hugging Face Papers listing. Its strongest signal is direct wet-lab evaluation rather than citation counts or measured readership.
- **Claimed contribution:** The authors report two closed-loop enzyme campaigns: 90 levansucrase variants over three rounds yielded a 14.03× wild-type screening-activity variant; 150 aldehyde-dehydrogenase variants over five rounds yielded a 6.85× screening-activity variant (7.90× after catalytic-rate normalization). They also report improved mutation prediction and a structure predictor faster than AlphaFold 3.
- **Caveat:** Experimental evidence is limited to two enzyme targets and modest campaign sizes; activity gains do not establish transfer to other proteins or applications. The 14.03× and 6.85× figures are screening activity, not clinical or industrial outcomes.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine

### 3. [Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511)
- **Abstract:** Pyrite tests whether LLM agents can rank difficult protein–ligand poses more accurately than expert chemists using structured geometry and interaction features.
- **Authors:** Megha Srivastava; Michael H. Lim; Allison M. Keys; Pranav Murugan; Nate Gruver
- **arXiv:** `2611.14511v1` (published 2026-11-10T18:56:32Z; categories: `cs.LG`, `q-bio.QM`)
- **Evidence for ranking:** A NeurIPS 2026 biological-discovery workshop submission with public code and dataset; independent coverage appeared at Bioscience.com.pk. The benchmark's 1,500 pose pairs and expert comparison make this a substantial, checkable evaluation.
- **Claimed contribution:** The authors report up to 67% accuracy for direct LLM ranking and 74% for LLM-guided feature construction plus logistic regression, on a 1,500-pair benchmark spanning 285 structures and 1,799 poses. Chemist annotators performed near chance on the difficult comparisons.
- **Caveat:** Poses originate from the authors' proprietary co-folding/sampling system; model-agent performance is computational pose ranking, not evidence that a drug binds or works in a patient. The paper notes a remaining accuracy gap and possible pre-/post-AF3 distribution shift.
- **Announcement type:** new submission, 2026-11-11 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 4. [scBIG++: Learning Across Genes and Cells to Predict Single-Cell Perturbation Responses](https://arxiv.org/abs/2611.11217)
- **Abstract:** scBIG++ predicts heterogeneous single-cell responses across all retained protein-coding genes rather than restricting inference to highly variable genes.
- **Authors:** Jiafa Ruan; Zican Qiao; Zongxin Yang; Ruijie Quan; Yi Yang
- **arXiv:** `2611.11217v1` (published 2026-11-08T08:08:31Z; categories: `cs.LG`, `cs.AI`, `q-bio.GN`)
- **Evidence for ranking:** Three-category cross-listing includes genomics and AI; the paper evaluates six genetic and chemical settings, reports cross-cell-line transfer and unseen-target tests, and links an implementation.
- **Claimed contribution:** The authors introduce expression-adaptive gene modules and population-conditioned generation to reconstruct perturbation responses over 6,539–19,451 genes, reporting competitive recovery under unseen targets/combinations and held-out compounds.
- **Caveat:** Results are benchmark-based predictions from existing single-cell perturbation data; they do not establish that predicted responses occur in newly performed experiments or in human patients.
- **Announcement type:** new submission, 2026-11-10 announcement batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Bioinformatics & sequence analysis

### 5. [When gene summaries reveal the answers: Gene Ontology circularity in gene embedding benchmarks](https://arxiv.org/abs/2611.11118)
- **Abstract:** This study measures how generated gene summaries can expose Gene Ontology labels to text-embedding benchmarks and proposes provenance-aware comparisons.
- **Authors:** Jiawei Wu; Huishu Wang; Junlin Chen; Hongyi Wang
- **arXiv:** `2611.11118v1` (published 2026-11-08T04:05:52Z; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Cross-listed in genomics; includes a released GeneProv benchmark and leaderboard, with a substantial provenance audit across 19,256 human protein-coding genes and comparisons in mouse and yeast.
- **Claimed contribution:** The authors found Alliance-generated summaries for 6,172 human genes (32.1%). Removing them reduced reported per-gene AUROC by 0.078 for a linear probe among genes with 1–10 linked publications; the effect also appeared with other encoders and text sources.
- **Caveat:** The authors flag a historical GO scorer that mishandled ties, and original predictions were unavailable for rescoring; the reported effect size is therefore provisional. Shared curation sources also complicate interpreting a benchmark as pure leakage.
- **Announcement type:** new submission, 2026-11-10 announcement batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 6. [Pruning DNA Sequence](https://arxiv.org/abs/2611.10386)
- **Abstract:** Sequence Pruning dynamically removes genomic sequences that become easy to predict during DNA-language-model pretraining.
- **Authors:** Faias Satter; Shaker Islam; Aminul Islam
- **arXiv:** `2611.10386v1` (published 2026-11-07T01:42:12Z; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Cross-listed in genomics; compared across five pretraining settings, two corpora, three model families, and five genomic benchmarks, with open code.
- **Claimed contribution:** The authors report up to 96% less data processing while largely retaining downstream performance; at the most aggressive setting, training used 4% of baseline GPU hours with little performance loss. At moderate savings, some results improved by up to 1.2 MCC points.
- **Caveat:** These are benchmark- and corpus-specific computational results. The paper does not show that the same savings preserve performance for every genome, task, or pretraining distribution.
- **Announcement type:** new submission, 2026-11-10 announcement batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

### 7. [OriDynamics: Towards a World Model for Biomolecular Dynamics](https://arxiv.org/abs/2611.11958)
- **Abstract:** OriDynamics generates all-atom conformational ensembles for proteins and complexes while modeling coordinated fluctuations between interacting partners.
- **Authors:** Jiahao Yang; Dong Liu; Hongliang Li; Ji Chen; Yuehua Liu; Daoyun Ding; Duo An; Jun Li; Jiahua Rao; Ziqiao Zhang; Peicong Lin; Shuangjia Zheng
- **arXiv:** `2611.11958v1` (published 2026-11-09T06:20:58Z; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct biomolecular focus and comparisons across protein monomer and complex benchmarks; the authors report a zero Semantic Scholar citation count at this early snapshot, so no citation momentum is claimed.
- **Claimed contribution:** The authors combine latent-space conformational exploration with local all-atom sampling and ensemble-level supervision of mean positions, fluctuation amplitudes, and coordinate covariance; benchmark results claim better conformational coverage, fluctuation fidelity, and interaction geometry than selected baselines.
- **Caveat:** Evidence is computational benchmark and application analysis, not a demonstration that generated ensembles reproduce experimentally measured dynamics across diverse systems.
- **Announcement type:** new submission, 2026-11-10 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 8. [The DynaCell Evaluation Suite for Dynamic 3D Virtual Staining of Live Cells](https://arxiv.org/abs/2611.02324)
- **Abstract:** DynaCell evaluates virtual fluorescence staining on 3D live-cell time series using pixel, organelle-segmentation, and single-cell-phenotype measures.
- **Authors:** Alexandr A. Kalinin; Dihan Zheng; Taylla Milena Theodoro; Ivan Ivanov; Eduardo Hirata-Miyasaki; See-Chi Lee; Aofei Liu; Sricharan Reddy Varra; Talon Chandler; Soorya Pradeep; Chad Liu; Manuel D. Leonetti; Carolina Arias; Bo Huang; Shalin B. Mehta
- **arXiv:** `2611.02324v2` (latest version posted 2026-11-07T06:45:00Z; first submitted 2026-11-02T00:16:20Z; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** A substantive revision in the requested week; the arXiv comment says accepted to NeurIPS 2026's Evaluations and Datasets track. The suite spans three cell types, two microscopes, four organelles, and three perturbation states, and its resources are public.
- **Claimed contribution:** The authors find regression baselines better for localizing target organelles, while a generative baseline better captures phenotype distributions across cells, exposing trade-offs obscured by single-metric evaluation.
- **Caveat:** This is an evaluation suite, not evidence that virtual staining is interchangeable with fluorescence for every cell type, microscope, or downstream biological conclusion.
- **Announcement type:** revision, 2026-11-07 version update
- **Themes:** Molecular & cell biology; Quantitative methods

### 9. [KineCouple: Substrate-conditioned residual readout for enzyme kinetic prediction](https://arxiv.org/abs/2611.09377)
- **Abstract:** KineCouple uses substrate-conditioned attention over protein residues to predict enzyme kcat and Km from sequence and substrate representations.
- **Authors:** Chun Kang; Yunbo Zhang; Fanhu Zeng; Jian Liu; Siwei Deng; Lei Sha
- **arXiv:** `2611.09377v2` (latest version posted 2026-11-09T12:46:02Z; first submitted 2026-11-06T12:17:54Z; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** A version update within the week and cross-listing in quantitative biology; the abstract reports pooled out-of-fold comparisons on CataPro rather than an isolated favorable split.
- **Claimed contribution:** The authors report small gains over a reproduced CataPro baseline: kcat RMSE 1.333 to 1.330 and PCC 0.492 to 0.496; Km RMSE 0.998 to 0.997 and PCC 0.633 to 0.634.
- **Caveat:** Improvements are numerically modest and computational; kinetic predictions complement, but do not replace, experimental enzyme characterization. No independent biochemical validation is reported in the abstract.
- **Announcement type:** revision, 2026-11-09 version update
- **Themes:** Biochemistry & proteins; Quantitative methods

### 10. [PathwayDesigner: an interactive SBML/KEGG/Reactome/Escher compatible editor for biochemical network diagrams](https://arxiv.org/abs/2611.14930)
- **Abstract:** PathwayDesigner is an open-source editor for biochemical network diagrams that supports several pathway formats and computes stoichiometric network summaries.
- **Authors:** Herbert M. Sauro
- **arXiv:** `2611.14930v1` (published 2026-11-11T02:34:06Z; categories: `q-bio.MN`)
- **Evidence for ranking:** Single-category q-bio.MN submission with unusually concrete interoperability tests: the authors report round-tripping 1,062 BioModels models and 1,823 SBML Test Suite cases, plus diagram exchanges with COPASI and SBMLNetwork.
- **Claimed contribution:** The author presents a cross-platform Rust/WebAssembly editor that imports/exports SBML and related maps, preserves model components, annotates species and reactions, and visualizes stoichiometry, conservation laws, and flux null spaces.
- **Caveat:** Passing file round-trip and interoperability tests is software validation, not evidence that downstream pathway models or biological interpretations are correct.
- **Announcement type:** new submission, 2026-11-11 arXiv submission date
- **Themes:** Biochemistry & proteins; Quantitative methods

## Trending Research Themes

Protein modeling spans multiple levels rather than a single benchmark: Bonbon predicts interaction properties from paired sequences, ProTEUS uses experimental feedback to navigate mutation combinations, Pyrite studies pose ranking, OriDynamics models conformational ensembles, and KineCouple estimates enzyme kinetics. Only Bonbon and ProTEUS report prospective wet-lab campaigns; the other results are computational. Across these papers, the practical question is how to connect learned scores to measurable binding, activity, or dynamics without treating prediction as validation.

A second cluster concerns genomic and single-cell model evaluation. scBIG++ targets full-gene perturbation response prediction; Pruning DNA Sequence reduces sequence-model training load; and the Gene Ontology circularity study shows how input provenance can inflate an apparent benchmark. DynaCell adds a multidimensional evaluation suite for dynamic virtual staining. Together, these works emphasize coverage, data provenance, and task-matched metrics—not a field-wide shift established by this small arXiv sample.

Benchmark and interoperability design also recur: Pyrite releases a difficult pose-pair dataset, GeneProv records text provenance, DynaCell separates pixel, segmentation, and phenotype performance, and PathwayDesigner tests standards-compatible model exchange. Their contributions are evaluation infrastructure; they should not be confused with biological discoveries or independent replication.

## Open Problems and Research Directions

Author-stated limits are explicit in Bonbon (coarse predictions, no 3D coordinates, untested kinetic properties), Pyrite (remaining accuracy gap and possible distribution shift), and GeneProv (a historical scorer error prevents rescoring the original predictions). A useful follow-up would prospectively test Bonbon and ProTEUS predictions in blinded, preregistered assays across additional protein families, include inactive and selectivity controls, and report denominators and uncertainty. For Pyrite, evaluate poses from independent generators and targets, with temporal and scaffold-held-out splits and crystal-structure adjudication; for GeneProv, rerun all probes with a corrected scorer and timestamped input/label provenance.

For scBIG++ and DNA Sequence Pruning, the abstracts report multi-setting computational evaluations but leave external reproducibility across labs, organisms, and perturbation collections open. Replication on held-out public datasets, with fixed compute budgets and cell-line-aware splits, would clarify transfer and the accuracy–cost trade-off. OriDynamics needs broader comparison against experimental ensemble measurements, while KineCouple's small CataPro gains merit external kinetic datasets and prospective assay checks. DynaCell could test whether its metric trade-offs predict downstream tracking or phenotype conclusions in independent microscopes and laboratories. These are synthesis proposals, not claims of clinical readiness or novelty.

## Takeaway

The clearest signal this week is not a verified popularity surge but a cluster of protein-modeling work that ranges from sequence-only interaction predictions to closed-loop enzyme evolution. Alongside it, several papers make evaluation itself the contribution. The strongest translational evidence remains early wet-lab validation in a small number of targets; most other results are benchmark-based, and none should be read as clinical evidence.

## Method and sources

Window: 2026-11-07 through 2026-11-13 inclusive (seven UTC calendar dates). Snapshot: 2026-11-13T02:20:50Z. The category pool used one arXiv API query over `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`, sorted by submitted date, with 200 results fetched; the page extended back to Oct 29, beyond the selected window. Cross-listed records were deduplicated by versionless arXiv ID. Of 65 unique records submitted or revised in the window, 58 were new submissions and 7 were updates. Each selected abstract page was checked; PDFs for the three leading papers were read for methods/results and limitations.

arXiv has no official trending ranking or readership statistics. Attention signals were sparse and citation totals too immature to establish citation velocity, so this is titled “Notable recent papers” and ordered by biology relevance, checkable external discussion or acceptance where available, cross-list breadth, and the strength/type of reported validation—not claimed popularity. Current citation totals, where available, were not treated as period gains. Most clinical and experimental preprints appear outside arXiv, especially on bioRxiv and medRxiv; this is neither a comprehensive biomedical survey nor clinical guidance.

Category query: `https://export.arxiv.org/api/query?search_query=cat:q-bio.BM%20OR%20cat:q-bio.GN%20OR%20cat:q-bio.MN%20OR%20cat:q-bio.SC%20OR%20cat:q-bio.CB%20OR%20cat:q-bio.TO%20OR%20cat:q-bio.QM%20OR%20cat:cs.BI%20OR%20cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200`

Primary papers: [Bonbon](https://arxiv.org/abs/2611.14504) · [ProTEUS](https://arxiv.org/abs/2611.13348) · [Pyrite](https://arxiv.org/abs/2611.14511) · [scBIG++](https://arxiv.org/abs/2611.11217) · [GeneProv](https://arxiv.org/abs/2611.11118) · [DNA Sequence Pruning](https://arxiv.org/abs/2611.10386) · [OriDynamics](https://arxiv.org/abs/2611.11958) · [DynaCell](https://arxiv.org/abs/2611.02324) · [KineCouple](https://arxiv.org/abs/2611.09377) · [PathwayDesigner](https://arxiv.org/abs/2611.14930).

Corroborating discussion and project records: [NeurIPS Oral — Bonbon](https://neurips.cc/virtual/2026/oral/149425); [Astrobiology coverage — Bonbon](https://astrobiology.com/2026/11/12/emergent-biological-capabilities-in-a-foundation-model-for-molecular-interactions/); [ProTEUS project page](https://yikunpku.github.io/ProTEUS/); [Hugging Face Papers — ProTEUS](https://huggingface.co/papers/2611.13348); [Bioscience.com.pk coverage — Pyrite](https://www.bioscience.com.pk/en/subject/biology/pyrite-building-and-benchmarking-protein-ligand-pose-ranking-agents); [DynaCell project](https://biohub.github.io/dynacell/); [GeneProv benchmark](https://hwang595.github.io/gene-embedding-exposure/); [PathwayDesigner source](https://github.com/sys-bio/PathwayDesigner-rs).
