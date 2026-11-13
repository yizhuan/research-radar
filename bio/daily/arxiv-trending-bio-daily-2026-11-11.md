# arXiv Biology & Biomedicine — 11 November 2026 announcement batch

Seven notable recent papers from the latest available announcement batch (11 November 2026). The strongest cluster is computational protein design and molecular-interaction modeling, with some papers reporting wet-lab validation; the rest span gene-regulatory inference, sequence-based virtual screening, dose-aware molecule selection, bacterial genomics, and spatial expression prediction. Spoken agenda: what the protein models actually validated, where the genomics methods remain computational, and why generated or screened candidates still need independent experiments. arXiv has no official trending chart; this is an inferred, relevance-ranked selection using checkable evidence rather than a readership ranking, and arXiv is incomplete coverage of biomedical research.

Window: daily; announcement batch 11 November 2026 (the latest batch shown on arXiv recent listings at the snapshot). Window dates: 2026-11-11 to 2026-11-11. Snapshot: 2026-11-13 01:16 UTC. The current date has no newer batch visible, so this uses the prior announcement batch.

## Notable recent papers (ranked)

Attention/citation evidence is sparse for a batch this recent, so the ordering below emphasizes biological relevance and the reported validation setting. Venue acceptance and author-reported experiments are stated as signals, not as proof of correctness or popularity. Papers are new submissions, not revisions.

### 1. [Emergent Biological Capabilities in a Foundation Model for Molecular Interactions](https://arxiv.org/abs/2611.14504)
- **Abstract:** Bonbon learns protein–ligand interaction representations and reports zero-shot mechanism, binding-site, and bond-type predictions, alongside prospective compound testing.
- **Authors:** Adi Mashiach
- **arXiv:** `2611.14504v1` (published 2026-11-10 18:53:01 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Authors report prospective wet-lab testing across nine disease targets in seven protein families and a 61.5% dose-response hit rate; arXiv lists acceptance as a NeurIPS 2026 Main Track Oral. These are reported study results, not independent popularity measures.
- **Claimed contribution:** The author reports that one frozen representation supports several zero-shot interaction tasks and transfers to new compounds, with wet-lab hits across the stated target set (arXiv abstract and Discussion).
- **Caveat:** The paper says the capabilities are coarse-grained and do not cover residence time, dissociation kinetics, post-binding conformational change, or explicit 3D coordinate recovery. The model is not a toxicity or clinical-efficacy assessment.
- **Announcement type:** new submission, 11 November 2026 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Bioinformatics & sequence analysis

### 2. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](https://arxiv.org/abs/2611.13348)
- **Abstract:** ProTEUS combines sequence, evolutionary, structural, and assay information to choose protein mutations in closed-loop engineering campaigns.
- **Authors:** Yikun Zhang, Minghao Guo, Guangxue Xu, Peter Yichen Chen, Wojciech Matusik, Wengong Jin, Jingjing Chai, Kaiyi Jiang
- **arXiv:** `2611.13348v1` (published 2026-11-09 23:19:33 UTC; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** Authors report two multi-objective experimental campaigns on aldehyde dehydrogenase and levansucrase, yielding variants with over tenfold wild-type activity; the report describes zero-shot and fine-tuned mutation-prediction comparisons.
- **Claimed contribution:** The authors present a mutation-resolved model that uses experimental feedback to update its protein-activity predictions and guide subsequent choices (arXiv abstract).
- **Caveat:** Experimental demonstration is limited to two enzymes and campaign objectives. The paper discloses company-founder/employee relationships and related patent filings; independent replication across proteins and assay settings remains important.
- **Announcement type:** new submission, 11 November 2026 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 3. [Bridging Graph and Pairwise Learning for Gene Regulatory Network Inference from scRNA-seq Data](https://arxiv.org/abs/2611.13801)
- **Abstract:** scGPL combines global graph structure and local transcription-factor–target interactions to infer gene regulatory networks from single-cell RNA-seq.
- **Authors:** Hang Li, Jiaxin Qi, Yan Cui, Yuhua Zheng, Jianqiang Huang
- **arXiv:** `2611.13801v1` (published 2026-11-10 09:34:28 UTC; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Authors report results on seven benchmark datasets and up to a 13.7% improvement over their strongest baseline; arXiv lists acceptance to Bioinformatics.
- **Claimed contribution:** The authors say combining graph-level topology with dynamically sampled local subgraphs improves benchmark GRN inference over the compared methods (arXiv abstract).
- **Caveat:** These are benchmark evaluations of inferred networks, not direct experimental confirmation that predicted regulatory links operate in cells; performance depends on the datasets and reference labels used.
- **Announcement type:** new submission, 11 November 2026 batch
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Bioinformatics & sequence analysis

### 4. [ANTIOCH-VS: From Sequence to Hits with Modular, Open-Source Ensemble Virtual Screening](https://arxiv.org/abs/2611.14287)
- **Abstract:** ANTIOCH-VS assembles protein-ensemble generation, docking, consensus ranking, and physics-based triage into a sequence-to-shortlist virtual-screening workflow.
- **Authors:** Hale S. Hasdemir, Venkata Sai Sreyas Adury, Pratyush Tiwary
- **arXiv:** `2611.14287v1` (published 2026-11-10 16:27:14 UTC; categories: `physics.chem-ph`, `q-bio.BM`)
- **Evidence for ranking:** The paper reports retrospective DUD-E benchmark tests on JAK2 and ADRB2, with 4/20 and 12/20 top-shortlist hits respectively (20% and 60%), compared with an estimated random rate around 1–2%; code is linked from the abstract page.
- **Claimed contribution:** The authors propose an open-source, modular workflow that generates docking-ready conformational ensembles and ranked candidate lists from protein sequence without requiring a ligand-bound crystal structure (arXiv abstract and Results).
- **Caveat:** Validation is retrospective and limited to two targets and benchmark decoys; the authors note users still choose which structural features to monitor and the MSA-depth range. Shortlist enrichment is not experimental confirmation of binding or efficacy.
- **Announcement type:** new submission, 11 November 2026 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 5. [The Dose Makes the Poison: Exposure-Aware Evaluation of Generative Drug Design](https://arxiv.org/abs/2611.13398)
- **Abstract:** PBPK simulations re-rank PARP1-targeted generated molecules by dose-linked exposure and predicted safety, showing that static molecular-property filtering can miss exposure constraints.
- **Authors:** Maria Franz, N. Benjamin Erichson
- **arXiv:** `2611.13398v1` (published 2026-11-10 00:20:01 UTC; categories: `q-bio.QM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** The authors evaluate 60 shortlisted candidates from three generative pipelines: seven fail the modeled target-exposure requirement, 28% of those remaining show predicted dose-related safety risks, and 85% of candidates with achievable modeled dose are outperformed by molecules omitted in static selection. Accepted at the NeurIPS 2026 AI4DD workshop, according to arXiv.
- **Claimed contribution:** The authors argue that integrating modeled dose and exposure can change candidate prioritization relative to static predicted potency/toxicity criteria (arXiv abstract).
- **Caveat:** These are PBPK/model-based predictions for PARP1 candidate sets, not measured pharmacokinetics, toxicology, clinical outcomes, or validation of a drug candidate.
- **Announcement type:** new submission, 11 November 2026 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods; Biochemistry & proteins

### 6. [Detection of local recombination and mutation hotspots in bacterial genomes using neural posterior estimation](https://arxiv.org/abs/2611.13763)
- **Abstract:** A simulation-trained neural posterior estimator models gene-specific bacterial mutation and recombination rates and propagates uncertainty into hotspot detection.
- **Authors:** Haochu Liu, Richard G. Everitt, Xavier Didelot
- **arXiv:** `2611.13763v1` (published 2026-11-10 09:03:29 UTC; categories: `q-bio.GN`)
- **Evidence for ranking:** The authors test rate recovery on simulations and demonstrate the approach on three bacterial datasets—Bacillus cereus, Staphylococcus aureus, and Escherichia coli—and provide a Python implementation link on the abstract page.
- **Claimed contribution:** The method is designed to separate local mutation and recombination signals while carrying posterior uncertainty into hotspot probabilities (arXiv abstract).
- **Caveat:** The estimator is trained under a specified simulation model conditioned on a fixed clonal genealogy; the real-data applications demonstrate use, not independent experimental confirmation of the inferred hotspots.
- **Announcement type:** new submission, 11 November 2026 batch
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis; Quantitative methods

### 7. [Predicting Single-Cell Spatial Gene Expression from H&E using Pathology Foundation Models](https://arxiv.org/abs/2611.13649)
- **Abstract:** The authors adapt pathology foundation models to predict single-cell spatial expression from paired H&E images and Xenium 5K measurements.
- **Authors:** Ashley P. Tsang, Evan Liu, Conrad Foo, Bob Chen, Hassaan Maan, Donny Chan, Elisa Penna, Veronica Ibarra Lopez, Hector Corrada Bravo, Aicha BenTaieb, Lisa M. McGinnis, Runmin Wei, Kenneth T. Gao
- **arXiv:** `2611.13649v1` (published 2026-11-10 06:44:33 UTC; categories: `cs.CV`)
- **Evidence for ranking:** Authors report a 2.67× mean gene-wise Pearson-correlation increase over a zero-shot baseline, AUROC 0.800 for gene detection, and strongest correlation for spatially variable genes (r=0.643); arXiv lists the NeurIPS 2026 workshop on AI at Scale for Clinical Impact. Included under the scope exception for work unmistakably about molecular/biomedical research; it was not in the configured biology-category listings.
- **Claimed contribution:** The authors report that task-specific image-model adaptation can recover some spatial expression patterns from routine histology without requiring histology input at inference (arXiv abstract).
- **Caveat:** This is computational inference from paired image/transcriptomic data; the abstract does not establish generalization to independent cohorts, all genes, or clinical use, and reported performance varies by biological context.
- **Announcement type:** new submission, 11 November 2026 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Biomedical & translational medicine

## Trending Research Themes

- Protein models are increasingly presented as closed-loop or interaction-aware systems, but validation settings differ. Bonbon reports prospective dose-response testing across nine disease targets; ProTEUS reports two experimental protein-engineering campaigns; ANTIOCH-VS reports retrospective enrichment on two benchmark targets. The latter's shortlist enrichment should not be read as wet-lab evidence.
- Computational genomics and transcriptomics papers combine richer structure with explicit uncertainty or evaluation design. scGPL couples global and local representations for regulatory-network inference; the bacterial-hotspot method propagates posterior uncertainty under a simulation model; the H&E study maps image features to spatial expression. These are distinct prediction problems, not evidence of a single field-wide shift.
- Dose and exposure modeling makes candidate-selection assumptions more explicit. The PARP1 study shows how PBPK outputs can reorder computationally generated candidates, but does not report measured PK or clinical evidence.

## Open Problems and Research Directions

- **Independent protein-model validation:** Bonbon and ProTEUS report promising experiments, but broader tests could measure success across additional protein families, laboratories, assays, and prospective targets, with preregistered comparators and all attempted candidates reported. For ProTEUS, campaigns beyond the two tested enzymes would help assess transfer across objectives and epistasis regimes.
- **Move from screening benchmarks to measured activity:** ANTIOCH-VS's two-target DUD-E results motivate prospective synthesis and binding/functional assays for sequence-derived shortlists, with blinded comparisons to single-structure docking and predeclared hit definitions.
- **Stress-test inference against independent biological references:** scGPL could be tested against perturbation-derived regulatory links and held-out cell types or studies; the bacterial hotspot model could be assessed under alternative genealogies and simulation assumptions, with independent sequence collections and targeted validation where feasible.
- **Calibrate modeled exposure and morphology-based expression:** The dose-aware design study points to comparing PBPK predictions with measured exposure and safety assays for selected candidates. The H&E/Xenium result motivates independent-tissue validation, stratified by tissue, gene abundance, and spatial variability, before treating image-derived expression as a dependable surrogate.

## Takeaway

This batch is notable for protein-model papers that connect computation to some experimental testing, alongside several useful but still model- or benchmark-dependent genomics and drug-design methods. The evidence is heterogeneous: prospective wet-lab results, retrospective benchmark enrichment, and simulations are not interchangeable. Nothing here constitutes clinical evidence or patient-specific guidance.

## Method and sources

- **Window and snapshot:** Daily report for the latest arXiv announcement batch visible at the snapshot, 11 November 2026; window 2026-11-11 through 2026-11-11; snapshot 2026-11-13 01:16 UTC. The current date had no newer batch visible on the recent listings, so this uses a prior announcement batch.
- **Candidate scope and query:** Recent arXiv listings for `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph` were checked for the latest batch; retained abstracts were verified individually. The configured `cs.BI` recent-list URL returned “Invalid archive or category”; a cross-list is not required for the included q-bio/medical-physics candidates. The machine-readable corpus query is [the specified arXiv API query](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200); the daily candidate set here was taken from the recent category listings and verified abstract pages. The H&E paper is a deliberate scope exception because its primary contribution is spatial gene-expression prediction, though its arXiv category is `cs.CV` only.
- **Ranking:** No official arXiv trend or readership statistics exist. Attention evidence was too sparse for an attention ranking, so entries are labeled “Notable recent papers” and ordered by relevance and checkable research evidence: reported experimental validation, breadth of benchmark evaluation, and stated acceptance status when available. No citation gains, downloads, or views are asserted. Citation totals are not used as period gains.
- **Evidence boundary:** Author-reported claims are attributed to the preprints. Prospective wet-lab experiments, retrospective benchmark results, PBPK simulations, and computational predictions are kept distinct. arXiv is not a representative index of biomedical preprints; much clinical and experimental work appears on bioRxiv, medRxiv, journals, or elsewhere. This report is not a systematic review or clinical guidance.
- **arXiv recent listings:** [q-bio.BM](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), [physics.med-ph](https://arxiv.org/list/physics.med-ph/recent).
- **Paper sources:** Each linked arXiv abstract page is the source for its title, authors, version, categories, timestamp, abstract, and comments. The top three paper texts were checked beyond their abstracts where available. No Semantic Scholar citation totals or independent-attention claims are used.
