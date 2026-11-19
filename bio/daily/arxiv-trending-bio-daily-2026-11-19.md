# arXiv Trending Biology & Biomedicine — Thursday, 19 November 2026

Latest batch announced Thursday, 19 November 2026; 8 notable papers from the 18 November submission date. The strongest patterns are cross-modal translation into scalable signals, predictive models of cellular dynamics, and better interpretation of molecular and imaging measurements. Agenda: examine what is genuinely measured versus predicted, then note where external validation is still needed. arXiv has no official trending chart; this is an inferred, relevance-ranked selection from incomplete biomedical coverage, not a readership or download ranking.

## Top papers (ranked)

### 1. [Cardiac MRI-informed electrocardiography enables biologically grounded cardiomyopathy detection](https://arxiv.org/abs/2611.23925)
- **Abstract:** MyoECG transfers cardiac MRI phenotype information into ECG representations; the authors report cardiomyopathy AUROCs of 0.800–0.974 across seven datasets and improved reader performance in a six-cardiologist study.
- **Authors:** Zhengyao Ding; Kewen Wang; Yujian Hu; Ziyu Li; Yiheng Mao; Yue Wang; Haitao Li; Dengnan Zhang; Xuanhong Liu; Yue Wang; Jing Wang; Yue Chen; Longbo Wang; Mengjia Chen; Chengchen Zhao; Xuesen Chu; Yubin Zhang; Mor Peleg; Judith Somekh; Mingxuan Yuan; Hui Yan; Yue Gu; Fan Yi; Zhilong Jia; Zhentao Tang; Xi Hu; Fei Wu; Hongkun Zhang; Ting Chen; Zhengxing Huang
- **arXiv:** `2611.23925v1` (published 2026-11-18T06:16:55Z; categories: cs.AI, q-bio.QM)
- **Evidence for ranking:** Ranked first for direct biomedical relevance and breadth of reported evaluation: 45,241 paired ECG–CMR examinations, over 1.8 million ECGs across seven datasets, and a six-cardiologist reader study; a third-party news summary also appeared. These are evidence-breadth signals, not measures of readership or independent validation.
- **Claimed contribution:** The authors claim CMR-guided training can transfer structural and functional information into ECG-only cardiomyopathy detection; in their retrospective reader study, assistance improved mean sensitivity and specificity.
- **Caveat:** Retrospective evidence; the paper reports limited positive predictive value in low-prevalence settings and calls for prospective evaluation of calibration, false-positive burden, clinical decisions, resource use, and outcomes. The authors do not position it as a standalone diagnostic test.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biomedical & translational medicine, Quantitative methods

### 2. [SCOPE: Single-Cell Omics Prediction from Histology via RNA-Protein Prior Enhancement](https://arxiv.org/abs/2611.24104)
- **Abstract:** SCOPE uses shared RNA–protein priors to predict single-cell molecular profiles from H&E images, reporting improvements over baselines across 16 organs and two external protein cohorts.
- **Authors:** Leyang Tao; Xuan Gong; Luyuan Xie; Arjun Beniwal; Yuqi Tan; Kun-Hsing Yu
- **arXiv:** `2611.24104v1` (published 2026-11-18T09:24:45Z; categories: cs.CV, q-bio.GN)
- **Evidence for ranking:** Ranked highly for direct omics relevance and evaluation breadth: 16-organ test data plus two external protein cohorts; cross-listed in cs.CV and q-bio.GN. The accessible Semantic Scholar record showed 0 citations at this snapshot, so no citation momentum is inferred.
- **Claimed contribution:** The authors claim that gene–protein correspondence and biomarker priors let a shared model transfer information across separately measured RNA and protein modalities, including to markers without direct H&E supervision.
- **Caveat:** These are image-based predictions, not direct molecular measurements. The authors note that RNA and protein assays came from separate sections rather than paired measurements on the same section; external protein validation involved two cohorts.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Omics & single-cell methods, Quantitative methods

### 3. [STORM: A Lightweight Structure-Free Model for Binding Affinity Prediction](https://arxiv.org/abs/2611.23777)
- **Abstract:** STORM predicts protein–small-molecule binding affinity by transferring information from experimentally measured reference molecules, without requiring protein–ligand structures.
- **Authors:** Ayush Pandit; Rohan V. Koodli; Wei Deng; Roxana Daneshjou; Ron O. Dror
- **arXiv:** `2611.23777v1` (published 2026-11-18T03:34:08Z; categories: q-bio.QM, cs.LG)
- **Evidence for ranking:** Ranked for biochemical relevance and its reported multi-dataset comparisons with Boltz-2; cross-listed in q-bio.QM and cs.LG. One early Biology+AI social-media post discussed the paper, which is a weak attention signal rather than independent validation.
- **Claimed contribution:** The authors report comparable or better affinity-prediction accuracy than Boltz-2 on their evaluation datasets and over five orders of magnitude faster inference and training in their comparisons.
- **Caveat:** The model does not use structural or biophysical signals and depends on historical affinity data and reference-molecule similarity. Dataset split design and performance on genuinely novel targets or scaffolds matter; the preprint does not establish experimental or drug-discovery utility.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biochemistry & proteins, Bioinformatics & sequence analysis

### 4. [MitoWorld: A Stochastic World Model of the Single-Cell Cycle under Genetic Perturbation](https://arxiv.org/abs/2611.23953)
- **Abstract:** MitoWorld models individual cell-image trajectories and division timing after genetic perturbation; on 325 held-out MitoCheck tracks across 17 knockdowns and a control, it reports improved video metrics and calibrated prediction intervals.
- **Authors:** Ting Long; Xiaojing Sun; Cheng Han; Zhicheng Ji; Yingnian Wu; Jiebo Luo; Heng Fan; Dongfang Liu
- **arXiv:** `2611.23953v1` (published 2026-11-18T06:42:32Z; categories: cs.CV, q-bio.QM)
- **Evidence for ranking:** Ranked for cell-biology relevance and a checkable held-out benchmark (325 tracks; 17 knockdowns plus control); cross-listed in cs.CV and q-bio.QM. The accessible Semantic Scholar record showed 0 citations at this snapshot, so citation momentum is not used.
- **Claimed contribution:** The authors claim a stochastic generative model can jointly forecast cell appearance and division hazard, with lower FID and JEDi scores than their strongest baselines on the held-out tracks.
- **Caveat:** Evaluation is computational and confined to the MitoCheck dataset; generated trajectories and hazard estimates are not direct evidence that predicted perturbation effects will generalize to new cell types or experimental settings.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Molecular & cell biology, Quantitative methods

### 5. [Horizontal Flow Matching for Single-Cell Spatiotemporal Dynamics](https://arxiv.org/abs/2611.24764)
- **Abstract:** HORIZON learns spatial transcriptomic tissue dynamics while factoring out shared rotation and translation; the authors report improved reconstruction and held-out-stage interpolation on four spatial transcriptomics time courses.
- **Authors:** Zihan Wang; Jianzhe Li; Zhenyi Zhang; Peijie Zhou
- **arXiv:** `2611.24764v1` (published 2026-11-18T17:16:53Z; categories: cs.LG, cs.AI, q-bio.QM)
- **Evidence for ranking:** Ranked for a concrete spatial-transcriptomics method and evaluation across four time courses, plus a simulated test of coordinate-frame perturbations; cross-listed in cs.LG, cs.AI, and q-bio.QM.
- **Claimed contribution:** The authors claim horizontal flow matching removes rigid-frame motion from inferred tissue dynamics and enables continuous tissue generation from an initial snapshot.
- **Caveat:** Results are computational comparisons on four time courses plus simulated alignment tests. Reconstructed dynamics are not direct cell tracking or causal evidence, and broader datasets and experimental settings are needed to assess transfer.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** RNA & transcriptomics, Omics & single-cell methods, Quantitative methods

### 6. [Unmyelinated axons alter the biological interpretation of MRI biomarkers of demyelination](https://arxiv.org/abs/2611.24487)
- **Abstract:** A mouse-model study combining diffusion and relaxation MRI with electron microscopy finds that unmyelinated axons materially affect white-matter MRI metrics commonly interpreted as measures of myelinated fibers.
- **Authors:** Ali Abdollahzadeh; Ricardo Coronado-Leija; Elizabeth Chasen; Sungheon G. Kim; Dmitry S. Novikov; Els Fieremans
- **arXiv:** `2611.24487v1` (published 2026-11-18T14:20:34Z; categories: physics.med-ph)
- **Evidence for ranking:** Ranked for direct biomedical and measurement relevance, with MRI measurements checked against electron microscopy in a cuprizone mouse model of demyelination and recovery; the abstract reports a g-ratio bias of up to 8% when within-voxel heterogeneity is ignored.
- **Claimed contribution:** The authors claim axonal-water-fraction estimates at short diffusion times reflect total intra-axonal space, and that g-ratio estimates align with EM only when myelinated and unmyelinated axons are both included.
- **Caveat:** The evidence is from a mouse model and does not establish performance or interpretation in human patients. MRI-derived measures and automated EM segmentation remain dependent on acquisition and analysis assumptions.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Medical physics & imaging, Biomedical & translational medicine

### 7. [A structure-based model of the bacterial chemosensory array reveals how the scaffolding protein CheW tunes sensory responses](https://arxiv.org/abs/2611.23921)
- **Abstract:** A structure-based Ising model of the bacterial chemosensory array reproduces previously reported CheW-dependent response changes and predicts how CheW abundance and placement shape signaling dynamics.
- **Authors:** David Hathcock; Yingxin Zheng; Yuhai Tu
- **arXiv:** `2611.23921v1` (published 2026-11-18T06:11:15Z; categories: physics.bio-ph, cond-mat.stat-mech, q-bio.MN)
- **Evidence for ranking:** Ranked for molecular-mechanistic relevance and cross-list breadth (physics.bio-ph, cond-mat.stat-mech, q-bio.MN); the model reproduces response patterns reported in prior experiments and generates specific, testable single-cell dynamics predictions.
- **Claimed contribution:** The authors attribute sharper signaling responses to CheW-mediated effective coupling between core units and predict a transition from relaxational to oscillatory fluctuations as CheW abundance changes.
- **Caveat:** This is a model, not a new experimental demonstration. CheW states and couplings are indirectly constrained, and the predicted oscillations and assembly effects require direct tests such as single-cell FRET across CheW levels.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biochemistry & proteins, Molecular & cell biology

### 8. [Benchmarking Traditional and Learning-Based Reference-Free Compressors for Long-Read Sequencing Data](https://arxiv.org/abs/2611.23794)
- **Abstract:** LRCBench compares reference-free long-read sequencing compressors across 35 methods and 16 real-world Oxford Nanopore and PacBio datasets, assessing compression, speed, memory, and robustness.
- **Authors:** Huidong Ma; Hui Sun; Xinyan Shi; Cheng Zhong; Xiaoguang Liu; Gang Wang
- **arXiv:** `2611.23794v1` (published 2026-11-18T04:00:08Z; categories: cs.IT, q-bio.GN)
- **Evidence for ranking:** Ranked for genomic-method relevance and the breadth of its benchmark (35 compressors; 16 datasets from two sequencing platforms); cross-listed in cs.IT and q-bio.GN.
- **Claimed contribution:** The authors report that CoLoRd gave the best overall compression ratios in their tests, while other tools traded off speed, memory use, and robustness.
- **Caveat:** Learning-based compressors were evaluated on only six MinION datasets because of computational cost; results depend on the sampled technologies, data, and benchmark settings and are not a biological finding.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** DNA & genomics, Bioinformatics & sequence analysis

## Trending Research Themes

- **Cross-modal transfer for broader reach:** MyoECG transfers CMR supervision to ECG-only inference, while SCOPE predicts RNA/protein profiles from H&E. Both target information-rich assays that are costly or sparsely available; neither result means the inferred signal replaces the original measurement.
- **Models that recover biological dynamics:** HORIZON and MitoWorld infer spatial or single-cell trajectories from transcriptomic and time-lapse data, while the CheW paper uses a structure-based model to predict collective signaling dynamics. These are distinct settings; the CheW dynamic signatures remain predictions.
- **Measurement and data infrastructure:** the MRI/EM study revisits what white-matter indices represent, and LRCBench compares practical long-read compression choices. These are distinct methods papers, not evidence of a field-wide shift from one day of submissions.

## Open Problems and Research Directions

- **Clinical transport and calibration (MyoECG):** authors report low positive predictive value in low-prevalence cohorts and retrospective validation. A prospective, multi-site study should pre-specify thresholds and assess calibration, false-positive burden, downstream imaging use, and patient outcomes across broader disease spectra and ancestries.
- **Direct molecular ground truth (SCOPE):** test RNA and protein predictions against matched assays from the same tissue sections, especially for markers unseen during training and across additional organs and laboratories; prediction correlation alone does not establish assay equivalence.
- **Novel-target binding affinity (STORM):** evaluate with target- and scaffold-held-out splits and prospective biochemical affinity measurements, separating gains from reference-molecule similarity from gains on genuinely new chemistry.
- **Mechanistic and translational validation (CheW; MRI/EM; HORIZON):** measure predicted CheW-dependent activity fluctuations by single-cell FRET across CheW expression levels, test whether MRI–axon interpretation transfers beyond the cuprizone mouse model, and evaluate HORIZON on additional spatial-transcriptomics time courses with independently measured cell-state transitions.

## Takeaway

This batch is notable for methods that bridge modalities and sharpen interpretation, not for an established popularity surge. The strongest evidence ranges from multi-dataset retrospective evaluation to mouse-model measurements and computational benchmarks; prospective clinical or experimental confirmation remains uneven and is not implied by the preprints.

## Method and sources

- **Window:** latest arXiv announcement batch dated 2026-11-19; candidate submission/revision dates 2026-11-18 through 2026-11-18 UTC. Snapshot: 2026-11-19 17:16:06 UTC; no later batch for that calendar day was available at the snapshot.
- **Candidate query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date descending; candidates deduplicated by versionless arXiv ID and checked against abstract records. The first 200 results reached back to 2026-11-04 and contained 16 eligible 2026-11-18 submissions/updates; 8 met the relevance and evidence bar for this concise report.
- **Ranking:** because papers were less than a day into the announcement cycle and attention/citation signals were sparse, this is titled “notable recent papers,” not a measured trend chart. Ordering emphasizes direct biology/biomedicine relevance and checkable reported validation breadth. Citation counts were not treated as period gains; the accessible Semantic Scholar records for SCOPE and MitoWorld each showed 0 citations at this snapshot. A third-party mention is noted only where found and is not treated as validation.
- **Coverage caveat:** arXiv is not a representative biomedical index; this does not cover bioRxiv, medRxiv, or the medical literature as a whole. The list is not a systematic review or clinical guidance.
- **Sources:** [arXiv recent q-bio listings](https://arxiv.org/list/q-bio/recent); [arXiv API](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200); each paper’s abstract page is linked above. Third-party context: [MyoECG news summary](https://www.aifyd.com/news/cardiac-mri-informed-electrocardiography-enables-biologically-grounded-cardiomyopathy-detection) and [STORM discussion](https://x.com/BiologyAIDaily/status/2123391317346598942).
