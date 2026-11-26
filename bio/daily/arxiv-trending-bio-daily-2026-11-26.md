# arXiv Biology & Biomedicine — 26 November 2026 announcement batch

## Headline

The 26 November batch contains 14 notable papers across molecular biophysics, RNA design, computational biology, and medical imaging. The strongest recurring thread is computational modeling that makes hidden constraints explicit—from molecular binding and RNA fold-back to cell-state deconvolution and lesion-preserving reconstruction. This is a relevance-ranked notable-paper selection, not a measured popularity chart: arXiv has no official trending chart, and its biomedical coverage is incomplete relative to bioRxiv, medRxiv, and the broader literature.

## Notable recent papers (ranked)

### 1. [Exclusion and internal structure in the association/dissociation kinetics of DNA-binding proteins in the fast diffusion limit](https://arxiv.org/abs/2611.33740)
- **Abstract:** The authors derive a reduced stochastic and mean-field model for fast-diffusing, multi-state proteins binding DNA with steric exclusion, and fit it to previously measured RPA–ssDNA dynamics.
- **Authors:** Xiangting Li, Tom Chou
- **arXiv:** `2611.33740v1` (published 2026-11-25 04:01:12 UTC; categories: `q-bio.BM`, `cond-mat.soft`, `cond-mat.stat-mech`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.75; 3 cross-lists (including q-bio.BM and q-bio.QM). No external attention component was recorded for this candidate.
- **Claimed contribution:** The authors report that a coarse-grained continuous-time Markov model and its mean-field limit capture footprint size and conformational switching, reproduce prior RPA binding dynamics, and represent facilitated exchange in multisegment binding.
- **Caveat:** This is a theoretical model checked against simulations and previously measured RPA data, not a new biochemical experiment; the fast-diffusion assumptions and broader applicability require system-specific validation.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Biochemistry & proteins; DNA & genomics; Quantitative methods

### 2. [KnitNet: Learning to Search at Inference Time for Exact RNA Inverse Design](https://arxiv.org/abs/2611.33812)
- **Abstract:** KnitNet uses folding-verifier feedback and coordinated sequence edits to search for RNA sequences whose predicted folds exactly match target structures.
- **Authors:** Antonia Panescu, Xin Wang, Haoran Xu, Qingyu Chen, Carlos Oliver, Rex Ying
- **arXiv:** `2611.33812v1` (published 2026-11-25 05:42:56 UTC; categories: `q-bio.BM`, `cs.AI`, `cs.LG`)
- **Evidence for ranking:** Signal score 0.50; 2 cross-lists. No external attention component was recorded for this candidate.
- **Claimed contribution:** Across five secondary-structure benchmarks, the authors report a 21-percentage-point average gain in exact solve rate over continued sampling with 70% less time-to-solve; they also report computational results on pseudoknots and 3D fold-back self-consistency.
- **Caveat:** Exactness is defined by computational folding verifiers; the paper does not establish that designed sequences adopt the target structures or functions in laboratory assays.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Quantitative methods

### 3. [From the Deterministic Hook Effect to Stochastic Reliability in Ternary Complex Formation](https://arxiv.org/abs/2611.33753)
- **Abstract:** Deterministic equations and exact stochastic simulations show how mediator dose, reaction volume, and copy-number thresholds can make ternary-complex formation unreliable despite a favorable mean response.
- **Authors:** Deepak K. Agrawal
- **arXiv:** `2611.33753v1` (published 2026-11-25 04:12:08 UTC; categories: `math.DS`, `q-bio.BM`, `q-bio.MN`)
- **Evidence for ranking:** Signal score 0.50; 2 cross-lists, including q-bio.BM and q-bio.MN. No external attention component was recorded.
- **Claimed contribution:** In a minimal reversible binding network, the author reports that stochastic reliability windows depend on compartment volume and threshold, and that faster ternary completion or slower breakup can improve modeled reliability.
- **Caveat:** The author explicitly frames the network as a deliberately minimal model, not a prediction for a particular drug, assay, or intracellular pathway; no experimental measurements are reported.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 4. [MolGPAO: Molecular Generative Pre-trained Autoregressive Octree with Speculative Decoding and Sub-Millisecond Seam Healing for 3D Molecules](https://arxiv.org/abs/2611.33985)
- **Abstract:** MolGPAO proposes an autoregressive 3D molecular-generation model with octree decoding and geometric refinement, evaluated on drug-like molecule and quantum-chemistry benchmarks.
- **Authors:** Shangqian Chen, Guojiang Zhao, Zheng Cheng, Jiankun Wang, Hongshuai Wang, Zhifeng Gao
- **arXiv:** `2611.33985v1` (published 2026-11-25 08:41:30 UTC; categories: `cs.LG`, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** Signal score 0.50; 2 cross-lists, including q-bio.BM. The score reflects cross-listing only for this candidate.
- **Claimed contribution:** The authors report improved generated-molecule validity and computational efficiency on GEOM-Drugs and QM9, plus DFT-based comparisons on OE62; reported figures are benchmark results, not drug efficacy.
- **Caveat:** Evidence is computational and benchmark-specific; generated structures and property estimates do not demonstrate synthesis, biological activity, safety, or therapeutic value.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 5. [Escape Time with Quenched Extrinsic Fluctuations in Positive Feedback Systems](https://arxiv.org/abs/2611.33341)
- **Abstract:** A theoretical framework combines intrinsic biochemical noise with slowly varying cell-to-cell parameter heterogeneity to estimate switching-time statistics in two bistable gene-regulation motifs.
- **Authors:** Manuel Eduardo Hernandez-Garcia, Natalia Lopez-Paleta, Jorge Velazquez-Castro
- **arXiv:** `2611.33341v1` (published 2026-11-24 19:25:49 UTC; categories: `q-bio.MN`)
- **Evidence for ranking:** Signal score 0.00; no external attention or cross-list component was recorded. Zero is not evidence of low scientific importance.
- **Claimed contribution:** For positive autoregulation and a genetic toggle switch, the authors report that extrinsic parameter variability can substantially alter mean escape times and increase their dispersion across modeled cells.
- **Caveat:** The results are theoretical and depend on the selected motifs and parameter distributions; they are not observations of a biological cell population.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Gene regulation & epigenetics; Molecular & cell biology; Quantitative methods

### 6. [Cell-Type-Specific Expression Is Hard to Predict from Bulk, but It Is Still Useful](https://arxiv.org/abs/2611.34166)
- **Abstract:** The authors derive accuracy limits for cell-type deconvolution and test whether cell-type-specific expression features from bulk RNA data retain prognostic value in non-small-cell lung cancer.
- **Authors:** Gadi Naveh, Amit Miller, Gal Keinan
- **arXiv:** `2611.34166v1` (published 2026-11-25 10:57:38 UTC; categories: `cs.LG`, `q-bio.QM`, `stat.ML`)
- **Evidence for ranking:** Signal score 0.50; 2 cross-lists. The arXiv record states acceptance at the NeurIPS 2026 Workshop on AI for Drug Discovery (AI4DD); this is publication-status context, not an attention measure.
- **Claimed contribution:** The authors derive closed-form R² bounds and assess 106 curated cell-type/gene pairs; in an NSCLC overall-survival analysis, a sparse model using deconvolved features performs comparably to one using bulk genes while attributing signals to cell types.
- **Caveat:** The survival result is a modeling analysis, not prospective clinical validation; selected targets were found post hoc to have higher learnability scores.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Biomedical & translational medicine

### 7. [Wasserstein-Fisher-Rao Reconstruction of Discrete space Population Dynamics](https://arxiv.org/abs/2611.33923)
- **Abstract:** The paper extends dynamic Wasserstein–Fisher–Rao transport to discrete states and uses it to reconstruct coarse-grained cell-state dynamics from sparse snapshots.
- **Authors:** Junda Ying, Xinyu Wang, Peijie Zhou, Lei Zhang
- **arXiv:** `2611.33923v1` (published 2026-11-25 07:43:34 UTC; categories: `math.OC`, `q-bio.PE`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.50; 2 cross-lists, including q-bio.PE and q-bio.QM. No external attention component was recorded.
- **Claimed contribution:** The authors derive a closed-form discrete-space solution and propose unbalanced discrete flow matching for larger or more general settings; numerical experiments and real-data applications are reported as plausibility checks.
- **Caveat:** Reconstructed trajectories are inferred from sparse observations under modeling assumptions; biological plausibility is not direct evidence that the inferred path is uniquely correct.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Omics & single-cell methods; Quantitative methods; Molecular & cell biology

### 8. [Using waveform types, discrete Sobolev distances, and trend compatibility to cluster short time series of clinical data](https://arxiv.org/abs/2611.33623)
- **Abstract:** A trend-aware clustering method identifies response patterns in short oral-glucose-tolerance-test curves, applied to 1,283 five-point tests.
- **Authors:** Robyn J. N. Kettlitz, Daniel Cisternas, Alvaro Olivera-Nappa, David Medina-Ortiz, Seba Contreras
- **arXiv:** `2611.33623v1` (published 2026-11-25 01:54:23 UTC; categories: `q-bio.QM`, `physics.data-an`, `stat.ME`)
- **Evidence for ranking:** Signal score 0.50; 2 cross-lists. No external attention component was recorded.
- **Claimed contribution:** The authors report seven glycemia and eight insulinemia response types from 1,283 five-point OGTT records; resampling and comparisons with six classical clustering methods are described.
- **Caveat:** This is an analysis of cohort-level curve patterns, not an individual diagnostic method; the reported clusters do not establish clinical utility or causal physiology.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 9. [Do Not Let the Prior Heal the Anomaly: Selective Anchoring for Detection from Incomplete Measurements](https://arxiv.org/abs/2611.33331)
- **Abstract:** Selective anchoring constrains generative image reconstruction to preserve reliably measured components, with reported lesion-preservation and detection results across sparse-view CT, accelerated MRI, and photoacoustic tomography.
- **Authors:** Nicolas Tricard, Stefan Brandstätter, Jason Chen, Zituo Chen, Linzheng Wang, Georg Langs, Sili Deng
- **arXiv:** `2611.33331v1` (published 2026-11-24 19:19:21 UTC; categories: `cs.CV`, `cs.LG`, `physics.med-ph`)
- **Evidence for ranking:** Signal score 0.50; 2 cross-lists, including physics.med-ph. No external attention component was recorded.
- **Claimed contribution:** For accelerated-MRI tumor detection, the authors report that deterministic anchoring raises mean AUROC across eight samplers from 78.4% to 84.6%; on other inverse-imaging tasks they report lesion-contrast and uncertainty improvements.
- **Caveat:** These are study-specific reconstruction and detection experiments, not evidence of clinical effectiveness; performance depends on the acquisition, reference, and evaluation setup.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

### 10. [Did the Model Forecast It, or Already Know It? Evaluating Large Language Models for Novel Drug-Target Prioritisation with a Temporal Knowledge-Graph Oracle](https://arxiv.org/abs/2611.34247)
- **Abstract:** A temporal knowledge-graph evaluation tests whether six open language models forecast target–disease pairs entering first clinical trials rather than exploit information recorded after the decision date.
- **Authors:** Pui Chung Siu, Yuan Liang, Claudia Cabrera, Mani Mudaliar, Arkaitz Zubiaga
- **arXiv:** `2611.34247v1` (published 2026-11-25 12:10:57 UTC; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.25; 1 cross-list. The record notes acceptance at a NeurIPS 2026 AI4DD workshop; this is not an attention measure.
- **Claimed contribution:** Across six open LLMs and dated yearly graphs, the authors find that unassisted models rank roughly like trial-history baselines, while newer graph retrieval often leaks the answer through post-decision evidence.
- **Caveat:** The result concerns a specific historical target-prioritization benchmark and does not demonstrate prospective drug discovery or clinical success.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Biomedical & translational medicine; Bioinformatics & sequence analysis; Quantitative methods

### 11. [DosePET: An Open-Source Dataset with 2100 Radiation Dose Maps for PET/CT](https://arxiv.org/abs/2611.34008)
- **Abstract:** DosePET provides 2,100 patient-specific PET/CT absorbed-dose maps generated by Monte Carlo simulation, drawing from examinations at five institutions and seven scanner models.
- **Authors:** Eleftherios Tzanis, Antonios Tzortzakakis, Michail E. Klontzas
- **arXiv:** `2611.34008v1` (published 2026-11-25 08:55:37 UTC; categories: `physics.med-ph`, `cs.AI`)
- **Evidence for ranking:** Signal score 0.25; 1 cross-list. No external attention component was recorded.
- **Claimed contribution:** The authors describe an open dataset with dose maps, 117 organ/tissue masks per study, regional dosimetry reports, and tools for download and conversion.
- **Caveat:** The dose maps are simulation-generated from public PET/CT inputs; their availability does not itself establish dosimetry accuracy or clinical benefit.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 12. [Monte Carlo-based secondary dose check platform for the world's first ultra-compact upright proton therapy system](https://arxiv.org/abs/2611.33924)
- **Abstract:** A TOPAS Monte Carlo model is compared with a treatment-planning system for 15 water-phantom and 25 clinical plans on an upright proton therapy platform.
- **Authors:** Toghrul Alakbarzade, Emir Musa Olgun, Yuan James Rao, Billy W. Loo Jr, Adam Johansson, Yong Yang, Murat Surucu, Mehmet Burcin Unlu, Serdar Charyyev
- **arXiv:** `2611.33924v1` (published 2026-11-25 07:44:38 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Signal score 0.00; no external attention or cross-list component was recorded. Zero is not evidence of low scientific importance.
- **Claimed contribution:** The authors report agreement with measurements and TPS plans, with all 40 recalculated plans passing the study's point-dose and 3%/2 mm gamma criteria.
- **Caveat:** This is a platform-specific secondary-dose comparison; the reported retrospective plan checks do not establish effects on patient outcomes.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 13. [Milk-removal feedback shapes lactation sustainability and daily output in a model of human lactation](https://arxiv.org/abs/2611.33997)
- **Abstract:** A minimal dynamical model compares how milk-removal amount or duration could feed back on production and daily output under alternative removal schedules.
- **Authors:** Angelika Manhart, Tobias Müller
- **arXiv:** `2611.33997v1` (published 2026-11-25 08:47:46 UTC; categories: `q-bio.QM`, `math.DS`)
- **Evidence for ranking:** Signal score 0.25; 1 cross-list. No external attention component was recorded.
- **Claimed contribution:** The authors' model predicts that amount-dependent feedback can produce a critical waiting interval or bistability, and that maximizing removal per session need not maximize daily output.
- **Caveat:** This is a mathematical model proposed as a basis for testing against longitudinal data, not an empirical study or individualized feeding guidance.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Molecular & cell biology; Quantitative methods

### 14. [DDxBasis: Explaining Frozen Foundation Encoder-based Medical Classification by Exact Differential Diagnosis](https://arxiv.org/abs/2611.33358)
- **Abstract:** DDxBasis builds concept-based, differential-diagnosis-style explanations for frozen-encoder medical image classifiers and is evaluated on five medical datasets.
- **Authors:** Luojie Huang, Gregory N. McKay, Nicholas J. Durr
- **arXiv:** `2611.33358v1` (published 2026-11-24 19:46:14 UTC; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.25; 1 cross-list. No external attention component was recorded.
- **Claimed contribution:** The authors report accuracy competitive with domain-specific results across five datasets and exact decomposition of model decisions into concept evidence; they also report cell-lineage, dermatology-annotation, and shortcut analyses.
- **Caveat:** These are retrospective dataset evaluations of classifier explanations, not evidence that the outputs are safe or effective for clinical diagnosis.
- **Announcement type:** new submission, 2026-11-26 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

## Trending Research Themes

- **Molecular constraints made explicit:** Li and Chou model DNA-protein occupancy, footprint switching, and facilitated exchange; Agrawal asks how stochastic copy numbers alter ternary-complex reliability; Hernandez-Garcia et al. model cell-to-cell heterogeneity in gene-network switching. These are theoretical or computational mechanisms, not new experimental discoveries.
- **Learning from structured biological feedback:** KnitNet uses fold errors to refine RNA sequences; Naveh et al. quantify which cell-type-specific expression signals can be recovered from bulk RNA; Ying et al. reconstruct discrete cell-state dynamics from sparse snapshots. Across them, the recurring methodological move is to expose what the data or verifier can and cannot identify.
- **Medical reconstruction and evaluation discipline:** Tricard et al. constrain generative imaging to avoid erasing measured anomalies; DosePET releases simulation-derived dose maps; Alakbarzade et al. compare an independent dose calculation with a treatment-planning system. Kettlitz et al. and Huang et al. add, respectively, cohort-level clinical-curve clustering and image-classifier explanation. These distinct studies support interest in trustworthy evaluation and reusable data, but do not amount to clinical validation.

## Open Problems and Research Directions

The follow-up directions below are synthesis proposals grounded in the selected papers, not claims that the authors proposed or validated these next steps.

- **Validate molecular models against new measurements:** Li and Chou fit earlier RPA–ssDNA data, while Agrawal's minimal binding network is theoretical. A useful next step would be prospective biochemical measurements across protein footprints, concentrations, and compartment volumes, testing whether their predicted exchange or reliability regimes hold outside the fitted or idealized settings.
- **Separate predicted structure from biological function:** KnitNet's exact matches use computational folding verifiers. Follow-up work could synthesize a preregistered subset of designed sequences, measure structure with an orthogonal assay, and test the intended function against matched controls, especially for pseudoknotted targets.
- **Test generalization without information leakage:** Naveh et al. study a curated set of 106 cell-type/gene pairs, while Siu et al. show how post-decision graph edges can leak target-trial outcomes. Independent cohorts and strictly time-stamped, externally held-out data would clarify which deconvolved signals and target rankings generalize prospectively.
- **Move imaging and dose methods beyond internal comparisons:** Tricard et al.'s lesion-preservation results, DosePET's simulated maps, and Alakbarzade et al.'s platform-specific dose checks motivate external scanner/site validation and blinded evaluation against independent measurements or clinical reference data; the relevant endpoints and safety thresholds would need to be prespecified by domain experts.

## Takeaway

Today's eligible batch ranges from DNA-binding kinetics and RNA inverse design to clinical imaging and dose calculation. Its standout contribution is not a single biological finding but a set of methods that make constraints, uncertainty, or leakage visible. The signal file recorded cross-listing but no external-attention signal for any candidate; treat this as a relevance-ranked snapshot, not a popularity verdict.

## Method and sources

- **Window:** daily announcement batch for 2026-11-26; submitted/updated between 2026-11-24 19:00:00 UTC and 2026-11-25 19:00:00 UTC. The batch was announced 2026-11-26 01:00:00 UTC, so this uses today's batch, not a prior one. Snapshot time: 2026-11-26 03:09:31 UTC.
- **Candidate pool:** pre-collected signal file `/home/yizhuan/.research/bio/daily/arxiv-trending-bio-daily-2026-11-26.signals.json` (15 candidates; arXiv, Hugging Face, and Hacker News collectors reported OK). The pool is capped and not exhaustive. `with_attention` was 0. The selected records' scores were based only on cross-list counts (0–3); HF upvotes, HN points/comments, citations, and code stars were not recorded as positive candidate components. A zero score means no external attention was found in the collected signals, not that a paper is unimportant. Semantic Scholar was unavailable (HTTP 429), so no citation evidence is used.
- **Ranking:** because independent attention evidence was absent, the section is titled “Notable recent papers” and ordered by fit to molecular biology, RNA/genomics, and biomedicine, with cross-list counts and signal scores disclosed per paper; it is not a popularity ranking. The robot-locomotion record was excluded as not sufficiently biomedical for this focused selection. All 14 selected records were checked against their arXiv abstract pages; the first three full-text HTML versions were also read.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`.
- **Primary sources:** arXiv abstract pages linked in each title; those pages supply authors, v1 dates, category metadata, abstracts, and comments. Signal counts and scores are from the dated signal file above. This is arXiv-only and does not represent bioRxiv, medRxiv, or the full biomedical literature.
