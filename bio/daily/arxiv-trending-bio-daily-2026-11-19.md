## Headline

Biology and biomedicine, arXiv batch 2026-11-19: nine notable papers selected from the supplied 12-candidate signal pool. The clearest pattern is computational methods applied to molecular, structural, genomic, and biomedical data; the strongest detected attention signal is one current citation for an MR elastography paper. Spoken agenda: compare this single citation and the cross-list-only scores with the papers' actual evidence, then distinguish computational benchmarks from experimental and clinical validation. arXiv has no official trending chart, so this is an inferred, evidence-ranked selection from incomplete biomedical coverage—not a measured popularity list. This report follows the supplied 19 November signal window; a later 20 November batch exists, but no matching attention-signal file was supplied here.

Window: 2026-11-18 19:00 UTC–2026-11-19 19:00 UTC. Announcement batch: 2026-11-19 (announced 2026-11-20 01:00 UTC). Snapshot: 2026-11-22 17:10:05 UTC. This uses a prior batch; the current calendar day has no batch represented in the supplied signals.

## Notable recent papers (ranked; attention evidence sparse)

### 1. [Physics-Informed Deep Learning for Shear Wave Speed Estimation in MR Elastography](https://arxiv.org/abs/2611.26111)
- **Abstract:** An end-to-end model combines undersampled MRI reconstruction with MRE wave inversion to estimate tissue shear-wave-speed maps from measured k-space data.
- **Authors:** Stefan Martin, Jakob Schattenfroh, Patrick Schuenke, Felix Frederik Zimmermann, Ingolf Sack, Christoph Kolbitsch, Andreas Kofler
- **arXiv:** `2611.26111v1` (published 2026-11-19T13:39:46Z; categories: `eess.IV`, `cs.LG`, `physics.med-ph`)
- **Evidence for ranking:** Collector score 1.886, the only positive citation-derived score in the supplied pool: Semantic Scholar reports 1 current citation (0 influential) and the candidate has 2 cross-lists; score components are 1.386 from citations and 0.500 from cross-lists. Hugging Face and Hacker News collection succeeded, but no matched engagement is recorded. The citation is not a gain measured during this window.
- **Claimed contribution:** The authors report 30% lower NRMSE than total-variation minimization and SWS estimation at up to 19-fold acceleration. The arXiv record identifies an accepted/published IEEE Transactions on Biomedical Engineering version (DOI: 10.1109/TBME.2026.3666306).
- **Caveat:** The study uses retrospectively undersampled brain data and an in-vivo healthy-volunteer application; the authors state that systematic validation in a larger patient population remains necessary. It does not establish clinical benefit.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 2. [Dynamical Variational Theory of Stochastic Reaction Networks](https://arxiv.org/abs/2611.25491)
- **Abstract:** A field-theoretic variational approximation estimates means, correlations, responses, and steady states for stochastic reaction networks, including low-copy-number regimes.
- **Authors:** Moshir Harsh, Peter Sollich
- **arXiv:** `2611.25491v1` (published 2026-11-19T04:26:42Z; categories: `cond-mat.stat-mech`, `q-bio.MN`, `q-bio.PE`)
- **Evidence for ranking:** Collector score 0.500, entirely from 2 cross-lists; Semantic Scholar reports 0 citations and 0 influential citations. No matched Hugging Face or Hacker News engagement is recorded. Relevance is direct: the paper benchmarks gene-regulation and enzyme-kinetics models.
- **Claimed contribution:** The authors report numerical benchmarks on gene regulation, enzyme kinetics, and infection dynamics, where their generalized self-consistent bubble resummation captures time-dependent behavior and fluctuations missed by selected approximations.
- **Caveat:** This is a theoretical and numerical method, not a wet-lab study. The authors assume well-mixed systems; their more advanced approximation focuses on networks with at most binary reactions, and they identify computational simplification and spatially resolved dynamics as further work.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Molecular & cell biology; Quantitative methods

### 3. [Ab-initio cryo-EM reconstruction from moments of denoised images](https://arxiv.org/abs/2611.25525)
- **Abstract:** A method-of-moments procedure estimates an initial 3D cryo-EM model from the first three moments of denoised particle images without explicit particle-orientation estimation.
- **Authors:** Yunpeng Shi, Amit Singer, Yuguan Wang, Andy Zhang
- **arXiv:** `2611.25525v1` (published 2026-11-19T05:26:45Z; categories: `q-bio.QM`)
- **Evidence for ranking:** Collector score 0.000; no citations, cross-lists, or matched Hugging Face/Hacker News engagement are recorded. Zero means no attention signal was detected, not that the work is unimportant. The relevance signal is direct structural-biology application on experimental datasets.
- **Claimed contribution:** The authors report that moment-based initial models can seed high-resolution refinement on experimental cryo-EM datasets without assuming uniform particle orientations.
- **Caveat:** The authors say denoising biases the moments and loses fine detail; they show failure on a low-molecular-weight example and identify improved denoising or direct moment estimation as needed. This is a reconstruction-method result, not a new biological structure discovery.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biochemistry & proteins; Quantitative methods

### 4. [An Explainable and Scalable Hierarchical Tensor Framework for Integrating Multi-Omics and Digital Pathomics](https://arxiv.org/abs/2611.25584)
- **Abstract:** HIT-Fuse integrates six molecular and pathology modalities across four TCGA cancer cohorts, including a procedure to reconstruct missing latent modalities.
- **Authors:** Ahmad Hussein, Ali Anaissi, Mukesh Prasad, Ali Braytee
- **arXiv:** `2611.25584v1` (published 2026-11-19T06:27:17Z; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Collector score 0.250, from 1 cross-list; Semantic Scholar reports 0 citations and 0 influential citations. No matched Hugging Face or Hacker News engagement is recorded. Relevance: the study combines copy-number, methylation, RNA, microRNA, protein, and pathology data.
- **Claimed contribution:** Across glioma, lung, breast, and kidney TCGA cohorts, the authors report survival-stratified subgroups, biological checks against DepMap/miRTarBase/RPPA resources, and a cohort-specific 56.4% relative weighted-F1 increase for glioma in a cohort-expansion experiment.
- **Caveat:** The evaluation is retrospective and TCGA-based; reconstructed modalities and database annotations do not establish prospective prognostic value, causal biology, or external clinical performance. The reported gain is cohort-specific.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** DNA & genomics; RNA & transcriptomics; Omics & single-cell methods

### 5. [ShEPhERD-score: Fast, adaptable three-dimensional alignment of molecular features](https://arxiv.org/abs/2611.25076)
- **Abstract:** ShEPhERD-score unifies differentiable 3D molecular similarity scoring and alignment, with CPU/GPU kernels for virtual screening and pairwise workflows.
- **Authors:** Nate Somers, Kento A. Abeywardane, Connor W. Coley, Masha Elkin
- **arXiv:** `2611.25076v1` (published 2026-11-18T19:17:58Z; categories: `q-bio.BM`)
- **Evidence for ranking:** Collector score 0.000; no citations, cross-lists, or matched Hugging Face/Hacker News engagement are recorded. Zero is no detected attention, not evidence of low importance. Relevance: a direct 3D molecular-design method.
- **Claimed contribution:** In the DUDE-Z virtual-screening benchmark, the authors report comparable-or-better results than matched open-source tools in 8 of 9 comparisons and throughput up to 1.03 million alignments per second on one NVIDIA L40S GPU.
- **Caveat:** This is computational screening evidence, not experimental binding or therapeutic evidence. The most effective scoring mode varied by protein target, so the authors note that target-specific calibration may be useful.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biochemistry & proteins; Quantitative methods

### 6. [From Sequence Uncertainty to Phenotype Hypotheses: Uncertainty-Conditioned Inference over Biomedical Knowledge Graphs](https://arxiv.org/abs/2611.25422)
- **Abstract:** An uncertainty-conditioned path-energy method maps genomic-model evidence into graph-supported distributions over gene–disease–phenotype hypotheses without patient-level phenotype supervision.
- **Authors:** Huixin Zhan, Jason H. Moore
- **arXiv:** `2611.25422v1` (published 2026-11-19T03:02:19Z; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Collector score 0.250, from 1 cross-list; Semantic Scholar reports 0 citations and 0 influential citations. No matched Hugging Face or Hacker News engagement is recorded. The authors evaluate on AlzKB and Hetionet.
- **Claimed contribution:** The authors report that phenotype-entropy tracks upstream uncertainty on both graphs and that recall@10 exceeded a DistMult baseline on 24 of 30 gene-holdout masks.
- **Caveat:** This is computational hypothesis generation, not patient diagnosis or validated phenotype prediction. The authors note that the gene-holdout advantage is mainly attributable to three genes with many variants and is not established for all genes.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

### 7. [When Foundation Models Disagree: Representational Heterogeneity for Calibrated Uncertainty in Whole-Slide Image Classification](https://arxiv.org/abs/2611.26159)
- **Abstract:** CALIFUSE uses disagreement among pathology foundation-model representations and chunk-level evidence consistency to estimate confidence in whole-slide classifications.
- **Authors:** Yekai Shen, Yuqian Wang, Zishun Liao, Rongsheng Wang, Wenting Chen, S. Kevin Zhou, Qingsong Yao
- **arXiv:** `2611.26159v1` (published 2026-11-19T14:15:07Z; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Collector score 0.250, from 1 cross-list; Semantic Scholar reports 0 citations and 0 influential citations. No matched Hugging Face or Hacker News engagement is recorded. The abstract reports seven WSI classification tasks; the arXiv comment says the paper was accepted by IEEE BIBM 2026.
- **Claimed contribution:** The authors report improved calibration, misclassification detection, and selective prediction over the strongest single-encoder baseline and naive ensemble averaging, with competitive balanced accuracy.
- **Caveat:** These are task-benchmark results; the abstract gives no cohort sizes and does not establish external-institution performance or clinical workflow value.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biomedical & translational medicine; Bioinformatics & sequence analysis

### 8. [Colloquium: Isotopes for medicine and fundamental physics](https://arxiv.org/abs/2611.25145)
- **Abstract:** A review surveys isotope enrichment and detection technologies and discusses possible medical uses, including radioisotopes for cancer therapy and stable isotopes as metabolic tracers.
- **Authors:** V. J. Ajith, Mark G. Raizen
- **arXiv:** `2611.25145v1` (published 2026-11-18T20:24:17Z; categories: `physics.app-ph`, `physics.atom-ph`, `physics.hist-ph`, `physics.med-ph`, `quant-ph`)
- **Evidence for ranking:** Collector score 1.000, entirely from 4 cross-lists; Semantic Scholar reports 0 citations and 0 influential citations. No matched Hugging Face or Hacker News engagement is recorded. Cross-list breadth is not itself a popularity measure.
- **Claimed contribution:** The authors review isotope-separation and detection methods, then outline anticipated medical and fundamental-physics applications.
- **Caveat:** This is a review and outlook, not an experimental or clinical validation of the proposed detection or treatment applications.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 9. [GraphEP: A Calibrated Data System and Benchmark for Learning Cardiac Electrophysiology](https://arxiv.org/abs/2611.26551)
- **Abstract:** GraphEP packages graph-native cardiac electrophysiology simulations and benchmarks neural models for predicting transmembrane-potential trajectories.
- **Authors:** Matteo Baldan, Chiara D'Ercoli, James Rowbottom, Pietro Liò, Stefania Fresca
- **arXiv:** `2611.26551v1` (published 2026-11-19T18:23:10Z; categories: `q-bio.TO`)
- **Evidence for ranking:** Collector score 0.000; no citations, cross-lists, or matched Hugging Face/Hacker News engagement are recorded. Zero means no attention signal was detected, not that the work is unimportant. The abstract describes 732 simulations across 20 anatomies.
- **Claimed contribution:** The authors report that physiology-informed models provide the strongest inductive bias in their simulation benchmark, with HGT-Lag and GAP2ODE leading on complementary prediction metrics.
- **Caveat:** These are simulated trajectories rather than experimentally measured or clinical cardiac data; generalization to real-world recordings remains to be established.
- **Announcement type:** new submission, 2026-11-19
- **Themes:** Molecular & cell biology; Quantitative methods

## Trending Research Themes

- **Computational representations for molecular and structural problems:** ShEPhERD-score addresses 3D molecular similarity, while the cryo-EM paper uses denoised image moments to initialize 3D reconstruction. Both target computational bottlenecks, but neither demonstrates a new biological mechanism or therapeutic effect.
- **Uncertainty and integration across heterogeneous biomedical data:** HIT-Fuse combines multi-omics with pathology, the phenotype-graph paper carries sequence-model uncertainty into graph hypotheses, and CALIFUSE estimates uncertainty from pathology-model disagreement. These distinct benchmark studies do not independently validate one another.
- **Dynamics from biochemical networks to cardiac simulation:** The reaction-network paper models low-copy-number biochemical dynamics; GraphEP benchmarks simulation-derived cardiac trajectories. The first is numerical theory, the second a simulated-data resource—neither is a direct wet-lab validation.

## Open Problems and Research Directions

- **Test methods against independent measurements:** Evaluate MRE reconstruction prospectively across sites and patient populations; compare the reaction-network predictions with low-copy-number biochemical time series; and test GraphEP against independent experimental electrophysiology recordings and held-out anatomies.
- **Stress-test molecular reconstruction and screening:** For cryo-EM, compare improved denoising and direct moment estimation across particle sizes and acquisition conditions, especially the small-particle cases where the authors report failure. For ShEPhERD-score, use target- and scaffold-held-out evaluation followed by prospective biochemical assays.
- **Establish external validity for multimodal inference:** Replicate HIT-Fuse and CALIFUSE on independent institutions with pre-specified missing-modality patterns and calibration checks. For phenotype hypotheses, use blinded patient-level phenotype evaluation and gene hold-outs that test whether performance extends beyond the few genes driving the reported gains.

## Takeaway

The supplied batch spans practical computational tools and models for molecular screening, biochemical dynamics, cryo-EM, multi-omics, and biomedical inference. Detected attention is limited: only the MRE candidate has a non-zero citation count, and that is a current total, not a within-window increase. Stronger evidence is needed before treating the computational gains as general biological or clinical performance.

## Method and sources

- **Window and snapshot:** Daily interval 2026-11-18T19:00:00Z–2026-11-19T19:00:00Z; announcement batch date 2026-11-19, announced 2026-11-20T01:00:00Z. Snapshot 2026-11-22T17:10:05Z. The supplied signal file was generated 2026-11-22T17:09:37Z. This report covers that requested window; a later 2026-11-20 batch is present in the local archive, so the 19 November batch is not the newest batch as of this snapshot.
- **Candidate pool and sources:** Started from `/home/yizhuan/.research/bio/daily/arxiv-trending-bio-daily-2026-11-19.signals.json`, which contains 12 candidates and the configured categories `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. The file reports `status: ok` for arXiv (12), Hugging Face (141), Hacker News (42), arXiv lookup (182), and Semantic Scholar (12); no source was reported unavailable. All nine selected candidates were checked against their arXiv abstract pages.
- **Ranking:** Collector scores and component values are reported per paper. The only citation component is one current Semantic Scholar citation for the MRE paper; no citation gain during the window is inferred. Other positive scores here come from cross-list breadth, not external engagement. Because attention evidence is sparse, the list is labeled “Notable recent papers” and prioritizes direct relevance and reported evidence; zero scores mean no matched attention was found, not low importance. Semantic Scholar totals are current totals. No independent discussion signal was found in the collected evidence.
- **Reading and evidence boundary:** For the top three, introduction, results, and discussion/limitations were checked in the arXiv source text; the remaining selected records were verified on their arXiv abstract pages. Claims are attributed to the authors. In-silico, simulation, retrospective, experimental, and clinical evidence are kept distinct. This is not clinical advice.
- **Coverage:** arXiv is not a representative index of biomedical preprints. This report does not cover bioRxiv, medRxiv, or the biomedical literature as a whole and is not a systematic review or clinical guideline.
- **Sources:** [Configured arXiv category query](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200); [q-bio recent listings](https://arxiv.org/list/q-bio/recent); [selected paper records: 2611.26111](https://arxiv.org/abs/2611.26111), [2611.25491](https://arxiv.org/abs/2611.25491), [2611.25525](https://arxiv.org/abs/2611.25525), [2611.25584](https://arxiv.org/abs/2611.25584), [2611.25076](https://arxiv.org/abs/2611.25076), [2611.25422](https://arxiv.org/abs/2611.25422), [2611.26159](https://arxiv.org/abs/2611.26159), [2611.25145](https://arxiv.org/abs/2611.25145), and [2611.26551](https://arxiv.org/abs/2611.26551). Attention evidence and source availability come from the cited signal file.