# arXiv Biology & Biomedicine — Daily Batch, 2026-11-16

## Headline

The latest announcement batch is Monday, 16 November 2026. This relevance-ranked shortlist contains 7 papers; the dominant pattern is function-aware protein evaluation and molecular modeling, alongside gene-response prediction and one MRI reconstruction study. Spoken agenda: compare experimental protein design with glycan and antibody benchmarks, then cover CRISPR-response modeling, RNA feedback theory, flexible protein interfaces, and MRI. arXiv has no official trending chart, and this is an inferred ranking from a small, incomplete slice of biomedical research; clinical and experimental biology preprints often appear on bioRxiv or medRxiv instead. Targeted checks found little independent attention evidence, so these are “Notable recent papers,” not measured hottest or most-read papers.

## Top papers (ranked)

Notable recent papers, ranked by biological/biomedical relevance and strength of the reported evidence because popularity signals are sparse.

### 1. [Confident and Wrong: Structure Confidence Is a Poor Selection Filter for Protein Function](https://arxiv.org/abs/2611.17391)
- **Abstract:** The authors compare three lanmodulin design strategies and report that function-guided selection yielded substantially more terbium-binding variants than selection by structural-confidence scores.
- **Authors:** Eric LoPrete, Pavle Jeremić
- **arXiv:** `2611.17391v1` (published 2026-11-12T04:05:20Z; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** New q-bio.BM submission in this batch; the paper reports biochemical screening of 297 designs against terbium and dysprosium, making it the shortlist’s most direct functional assay. No independent attention signal surfaced in targeted searches.
- **Claimed contribution:** The authors report 83.3% terbium binding in the function-guided panel versus 16.7% in the structure-confidence-selected panel, and argue that measured-function supervision is a better selection signal in this design setting (arXiv abstract and Results).
- **Caveat:** The comparison is bounded to lanmodulin rare-earth binding and three design strategies; it does not establish that structural confidence is unhelpful for all proteins or design tasks.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [CARVE: A glycan-specific framework for assessing protein-glycan binding-pose quality](https://arxiv.org/abs/2611.18259)
- **Abstract:** CARVE combines glycan-aware geometry and contact measures to classify predicted protein–glycan poses, then benchmarks nine methods on experimentally determined complexes.
- **Authors:** Yifei Xiao, Huifeng Zhao, Silong Zhai, Zichang Jin, Tingjun Hou, Yu Kang
- **arXiv:** `2611.18259v1` (published 2026-11-13T14:55:34Z; categories: `q-bio.BM`)
- **Evidence for ranking:** New q-bio.BM submission; CARVE-Score reproduced quality classes on 25,068 poses (macro-F1 0.892), and CARVE-Bench covers 1,974 complexes and nine prediction methods. These are relevance and evaluation-depth signals, not readership measures.
- **Claimed contribution:** The authors report that HADDOCK3 had the highest acceptable-level success rate among the top 25 predictions per target (47%); no tested method exceeded 20% for high-quality, structurally valid poses (abstract and Conclusion).
- **Caveat:** This is a structural benchmark on existing complexes, not prospective experimental validation of new glycan binding. The authors used a temporal split to reduce training overlap, but note that it cannot ensure every prediction method had never seen every benchmark structure.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [Learning Task-Specific Antibody Representations via Function-Aware Masking](https://arxiv.org/abs/2609.00518)
- **Abstract:** The authors train antibody language models with function-aligned masking patterns and report improvements on the downstream tasks targeted by those patterns.
- **Authors:** Ayan Goel, Thomas A. Walton, Amirali Aghazadeh
- **arXiv:** `2609.00518v2` (first submitted 2026-09-01T00:37:56Z; latest revision 2026-11-13T18:26:45Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Listed as a replacement in today’s q-bio.BM batch; the arXiv comment reports acceptance to MLCB 2026 (Oral), a checkable venue signal rather than a readership claim.
- **Claimed contribution:** The authors report gains of up to 14% on structure-related tasks and 5.9-fold on CDR-related tasks, using specialist and hybrid masking strategies (abstract and Results).
- **Caveat:** Evaluations use a medium-sized, approximately 38M-parameter model and computational benchmarks; the authors identify label quality, model scale, and manually chosen hybrid mixtures as limitations. The study does not establish improved wet-lab binding success.
- **Announcement type:** revision, 2026-11-16 announcement batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 4. [S1Pert: Scalable Target-Specific Gene Response Prediction with System-One Intelligence](https://arxiv.org/abs/2611.17705)
- **Abstract:** S1Pert combines uncertainty-aware response labels, cached foundation-model representations, and a hierarchical decoder to predict gene-response direction for unseen genetic perturbations.
- **Authors:** Xiaoqi Sheng, Hou wang, Yan Liang, Yutong Li, Wenhao Du, Tinghe Zhang, Jiawen Liu, Hongmin Cai
- **arXiv:** `2611.17705v1` (published 2026-11-13T03:35:01Z; categories: `q-bio.GN`)
- **Evidence for ranking:** New genomics submission; evaluated with target-held-out splits in four cell-line datasets (HepG2, Jurkat, RPE1, K562), and the authors provide public code. No independent attention signal surfaced in targeted searches.
- **Claimed contribution:** The authors report Macro-F1 gains of 5.8–6.4 percentage points over the strongest baseline across the four evaluated datasets, with improved discrimination of target-specific response directions (abstract and Experiments).
- **Caveat:** This is retrospective computational evaluation on existing perturbation data, not prospective CRISPR validation. Its performance and response labels are benchmark- and cell-context-dependent; the authors call for extension to additional tissues and perturbation settings.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Bioinformatics & sequence analysis

### 5. [Scan-specific k-space interpolation using deep Koopman autoencoders](https://arxiv.org/abs/2611.18301)
- **Abstract:** A scan-specific deep Koopman autoencoder reconstructs retrospectively undersampled brain MRI k-space data and is compared with GRAPPA and RAKI.
- **Authors:** Wassim Ben Salah, Jon Cleary, Sarah McElroy, Raphael Tomi-Tricot, Antoine Naegel, Sebastien Ourselin, Jonathan Shapey, Christos Bergeles, Radhouene Neji
- **arXiv:** `2611.18301v1` (published 2026-11-13T15:25:37Z; categories: `physics.med-ph`)
- **Evidence for ranking:** New medical-physics submission; tested on 281 retrospectively undersampled brain MRI datasets and a 52-image reader study; the arXiv comment says it was submitted to Magnetic Resonance in Medicine. Semantic Scholar listed 0 citations at this snapshot.
- **Claimed contribution:** The authors report improved reconstruction metrics over GRAPPA and RAKI and reader preference over RAKI in 38 of 52 cases, with better ratings for sharpness, aliasing, and overall image quality (abstract and Results).
- **Caveat:** Data are retrospective brain scans from one dataset, not prospective patient scans or a multi-site evaluation. The paper itself calls for tests on other anatomies, scanners, and coils; reader-study preference is not clinical-outcome evidence.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** Medical physics & imaging; Quantitative methods

### 6. [Exact stochastic theory of post-transcriptional gene autoregulation mediated by RNA-binding proteins](https://arxiv.org/abs/2611.18062)
- **Abstract:** An analytical stochastic model derives protein-number and burst-size distributions for RNA-binding-protein-mediated feedback and compares its predicted noise and rhythm transmission with transcriptional feedback.
- **Authors:** Chen Jia
- **arXiv:** `2611.18062v1` (published 2026-11-13T11:45:58Z; categories: `q-bio.MN`, `cond-mat.stat-mech`, `physics.bio-ph`)
- **Evidence for ranking:** New q-bio.MN submission, cross-listed in biological physics and statistical mechanics; it provides an exact mathematical treatment of a molecular feedback mechanism. No independent attention signal surfaced in targeted searches.
- **Claimed contribution:** The author derives a steady-state distribution and sub-Poissonian criterion, and predicts that negative feedback favors post-transcriptional control for noise suppression and rhythm transmission, while positive feedback favors transcriptional control (abstract and Conclusion).
- **Caveat:** The results are theoretical predictions from a reaction model, not newly measured molecular or cellular effects; experimental tests are needed to assess the assumptions and predicted regime reversal.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Quantitative methods

### 7. [Deciphering multiple binding modes in large protein complexes via Enhanced Sampling and beta-VAE: the CYFIP1-eIF4E case](https://arxiv.org/abs/2611.18236)
- **Abstract:** Enhanced molecular sampling and latent-space clustering are used to propose three binding modes for the flexible CYFIP1–eIF4E protein complex.
- **Authors:** Francesco Pignotti, Emanuele Telari, Edoardo Milanetti, Anna La Teana, Jesmina Rexha, Alice Romagnoli, Luca Maragliano, Giovanni Di Muccio
- **arXiv:** `2611.18236v1` (published 2026-11-13T14:31:47Z; categories: `q-bio.BM`, `q-bio.QM`)
- **Evidence for ranking:** New q-bio.BM submission, cross-listed in quantitative methods; the reported analysis uses ten enhanced-sampling replicas totaling 100 μs and resolves recurring interface modes. This is a method/relevance signal, not evidence of popularity.
- **Claimed contribution:** The authors’ simulations suggest CYFIP1 samples the canonical dorsal site, a non-canonical lateral site, and a combined mode on eIF4E, including contacts outside the previously emphasized interface (abstract and Results).
- **Caveat:** The interface is computationally inferred. The authors note that coarse-graining and elastic-network restraints limit side-chain and large-scale motion, and that under-sampled modes may be missed; direct mutagenesis or binding experiments remain necessary.
- **Announcement type:** new submission, 2026-11-16 announcement batch
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

## Trending Research Themes

- **Function-aware protein and molecular-recognition evaluation:** “Confident and Wrong” tests whether structural confidence selects functional variants; CARVE proposes glycan-specific pose metrics; and “Learning Task-Specific Antibody Representations” aligns model pretraining with antibody tasks. Together they emphasize measuring or defining task-relevant function rather than relying on generic structural plausibility alone. The evidence types differ: lanmodulin has biochemical assays, CARVE is a retrospective structural benchmark, and antibody results are computational task evaluations.
- **Computational models of gene response and regulation:** S1Pert evaluates target-specific transcriptional-response prediction across four cell contexts, while Jia derives exact stochastic predictions for RNA-mediated feedback. Both address gene regulation, but one is a learned predictor and the other a mathematical model; neither by itself establishes prospective biological validation.

MRI reconstruction and CYFIP1–eIF4E interface sampling are notable individual contributions in this batch, not recurring corpus-level trends.

## Open Problems and Research Directions

- **Generalize function-guided protein selection:** “Confident and Wrong” is limited to one protein family and rare-earth binding. A blinded follow-up could compare function-trained selection, structure-confidence selection, and random selection across additional scaffolds, ligands, and assay conditions, using a prespecified synthesis and measurement budget.
- **Stress-test glycan pose benchmarks:** CARVE reduces, but cannot rule out, overlap with every model’s training data. Future evaluations could use structures released after model-training cutoffs and pair structural scores with prospective binding assays or orthogonal biochemical validation.
- **Validate computational predictions prospectively:** For S1Pert, test pre-registered unseen-target predictions in CRISPR screens across additional cell types and replicate populations. For the RNA-feedback theory, measure protein-number distributions and response to periodic input in controlled systems with positive and negative RNA-binding feedback; these are proposed tests, not reported results.
- **Establish MRI generalization:** The MRI study itself identifies anatomy, scanner, and coil coverage as open issues. A multi-site, multi-coil evaluation with prospectively acquired scans and reader assessment would test whether the reconstruction gains transfer beyond retrospective NYU fastMRI brain data.

## Takeaway

The strongest directly experimental signal in this batch is a lanmodulin design comparison showing that measured-function guidance outperformed structural-confidence selection in that specific assay. The other notable contributions are a sizable glycan-structure benchmark, an accepted antibody-representation revision, and computational work on gene regulation and MRI. The batch supports a relevance-ranked shortlist, not a claim about what arXiv readers are choosing or what is clinically validated.

## Method and sources

- **Window:** daily, 2026-11-16 through 2026-11-16; latest arXiv announcement batch dated 2026-11-16 (not a prior-day batch). **Snapshot:** 2026-11-16T17:14:46Z.
- **Candidate categories:** `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`; the broad arXiv API query is [here](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200). The `cs.BI` query returned no candidates for this batch.
- **Listing coverage:** official [Quantitative Biology new listings](https://arxiv.org/list/q-bio/new) showed 13 new submissions, 6 cross-lists, and 23 replacements for the batch; [Medical Physics new listings](https://arxiv.org/list/physics.med-ph/new) showed 1 new submission and 5 replacements. The configured q-bio subcategory listings were checked; only candidates with clear molecular, biomedical, or medical-physics relevance were retained. Seven selected entries include six new submissions and one revision.
- **Verification and ranking:** selected metadata and abstracts were checked against individual arXiv abstract pages, with the latest version used and original submission dates retained. The top three were read beyond their abstracts (introduction, results, and limitations/discussion) using available full text or PDF extraction. The selection is relevance-ranked because no reliable attention ranking was available; direct assay/benchmark strength, cross-listing, a stated MLCB oral acceptance, and the MRI reader study are checkable signals. Targeted searches found little independent technical discussion; no downloads or views were inferred, and citation totals are not treated as gains during the window.
- **Coverage caveat:** arXiv is not a representative index of biomedical research. This report excludes most work published only on bioRxiv or medRxiv and is not a systematic review or clinical evidence assessment.
