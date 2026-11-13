# arXiv Trending Biology and Biomedicine — Daily — 2026-11-12

## Headline

The latest available daily batch in the configured biology/biomedicine arXiv corpus is dated 2026-11-12: 8 eligible papers (7 new submissions and 1 revision). Protein-model reliability and mutation-effect prediction are the clearest shared thread, alongside low-field fMRI, red-cell mechanics, and decision-support methods. The agenda: examine how protein models are tested, then compare the translational claims with the evidence actually reported. arXiv has no official trending chart; this is an inferred relevance ranking, not a popularity measure, and arXiv omits much of biomedical preprint and clinical research. The batch is the latest available at the 2026-11-13 UTC snapshot.

## Notable recent papers (ranked by demonstrated relevance)

### 1. [MutAtlas: A PDB-Wide Energy-Guided Atlas of Protein Mutation Effects](https://arxiv.org/abs/2611.16361)
- **Abstract:** The authors combine structure-based energy estimates, protein-language-model scores, and inverse-folding scores into a PDB-scale mutation resource, then train a disagreement-aware preference model evaluated on ProteinGym.
- **Authors:** Ruihan Guo, Chaoran Cheng, Zhanghan Ni, Neil He, Bangji Yang, Ge Liu
- **arXiv:** `2611.16361v1` (published 2026-11-12T06:22:47Z; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Direct protein-variant relevance; arXiv notes acceptance at ICML 2026, corroborated by the [PMLR proceedings page](https://proceedings.mlr.press/v306/guo26c.html) and [ICML poster listing](https://icml.cc/virtual/2026/poster/63147). No popularity claim is inferred.
- **Claimed contribution:** The authors report 15.9 million residue positions across 86,479 chains and zero-shot evaluation on 201 ProteinGym datasets; their disagreement-aware model reaches macro Spearman 0.498, above the evaluated baselines. These are computational predictions and benchmark correlations, not new mutation assays.
- **Caveat:** Most augmentation signals are generated computationally (including FoldX); benchmark correlation does not establish experimental performance for a new protein or clinical variant.
- **Announcement type:** new submission, 2026-11-12
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 2. [Protein Language Models Fail To Capture Contact Predictions Under Invariant Relabeling](https://arxiv.org/abs/2611.16881)
- **Abstract:** The authors globally permute amino-acid labels without changing alignment statistics and report that contact maps from several protein language models change sharply, unlike the tested Potts and inverse-covariance methods.
- **Authors:** Paarth Batra, Aryan Keluskar
- **arXiv:** `2611.16881v1` (published 2026-11-12T14:45:07Z; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** Directly tests a key interpretation of protein-model outputs; arXiv records acceptance at the ICBINB workshop at NeurIPS 2026, also listed on the [NeurIPS workshop page](https://neurips.cc/virtual/2026/169424).
- **Claimed contribution:** Across ESM-2, MSA Transformer, and AMPLIFY, the authors report contact-map degradation after relabeling and argue that canonical amino-acid identities, not only coevolutionary statistics, influence these predictions. Their paper reports tests across nine proteins and three seeds for a central ESM-2 comparison.
- **Caveat:** The authors note a limited set of short proteins/families, readouts, and model families; relabeling invariance is necessary but not sufficient evidence of pure coevolutionary inference. This is a computational diagnostic, not a claim that contact predictions are unusable.
- **Announcement type:** new submission, 2026-11-12
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 3. [AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems](https://arxiv.org/abs/2611.17015)
- **Abstract:** This review proposes describing biological foundation-model reliability through five design elements—data, architecture, training, evaluation, and post-analysis—and links these boundaries to agentic workflows.
- **Authors:** Tian Cai, Andrew Kleist, Jaimin Patel, Duccio Malinverni, Alexander K. Taylor, Malvika Sharan, Renato Umeton, M. Madan Babu
- **arXiv:** `2611.17015v1` (published 2026-11-12T16:08:33Z; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** Broad fit to computational biology and model-evaluation practice; the arXiv comment says it is to be published in Annual Review of Biomedical Data Science.
- **Claimed contribution:** The authors offer a conceptual framework for stating where biological foundation models and agentic systems can be relied on, illustrated through literature on sequences, structures, single-cell, and other omics data.
- **Caveat:** This is a review/perspective rather than a prospective benchmark or new experimental study; the proposed framework still needs operational testing across real biological tasks.
- **Announcement type:** new submission, 2026-11-12
- **Themes:** Bioinformatics & sequence analysis; Omics & single-cell methods; Quantitative methods

### 4. [Using an energy pixels approach to estimate the size a 2nd Generation DEL must be to train a high-resolution binding model](https://arxiv.org/abs/2611.17121)
- **Abstract:** The paper models how a hit-centered second-generation DNA-encoded library (DEL) might need to sample chemical space to provide enough tight binders and local affinity variation for training a high-resolution binding model.
- **Authors:** Boris P. Belotserkovskii, R. Edward Watts
- **arXiv:** `2611.17121v1` (published 2026-11-12T17:13:57Z; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Clear molecular-discovery and biomolecule-modeling relevance; the available evidence is the new primary-category listing and paper abstract, with no independent attention signal used.
- **Claimed contribution:** The authors use an “energy pixels” abstraction and affinity spread from a naive library to estimate a required library complexity and a baseline expected yield for a randomly designed follow-up DEL.
- **Caveat:** The abstract describes an estimation framework, not a prospective library synthesis or experimental binding validation; predicted library requirements should be checked against measured compounds and affinities.
- **Announcement type:** new submission, 2026-11-12
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [Stretched bilayer-cytoskeleton links hold echinocytes in a model splenic slit](https://arxiv.org/abs/2611.16241)
- **Abstract:** In a two-component red-cell model, stage III echinocytes required much higher pressure drops than discocytes to pass a model splenic slit, with near-fully stretched bilayer–cytoskeleton links implicated in the hold.
- **Authors:** Zhaojie Chai, Jianlu Zheng, He Li, Ming Dao, George Em Karniadakis
- **arXiv:** `2611.16241v1` (published 2026-11-12T03:39:47Z; categories: `physics.bio-ph`, `cond-mat.soft`, `physics.flu-dyn`, `q-bio.CB`)
- **Evidence for ranking:** Strong direct cell-biophysics relevance and cross-listing in q-bio.CB; ranking rests on the paper’s reported mechanistic model results rather than readership evidence.
- **Claimed contribution:** The authors report model simulations in which stage III echinocytes were held at 37–50 times the pressure drop that passed a discocyte; lengthening the modeled links about twofold released held cells in most test runs.
- **Caveat:** The central evidence is computational and the model links do not break; this is not direct validation in perfused human spleens or evidence about transfusion outcomes.
- **Announcement type:** new submission, 2026-11-12
- **Themes:** Molecular & cell biology; Biomedical & translational medicine; Quantitative methods

### 6. [A risk-aware individualized blood pressure target to avoid hypotension in surgery](https://arxiv.org/abs/2611.16757)
- **Abstract:** The authors propose an online model to choose a MAP target and norepinephrine dose under a stated risk bound, then assess calibration retrospectively and in a virtual-patient cohort.
- **Authors:** Simon Buré, Jona Joachim, Florent Di Meglio
- **arXiv:** `2611.16757v1` (published 2026-11-12T13:06:52Z; categories: `q-bio.QM`, `math.OC`)
- **Evidence for ranking:** Direct biomedical decision-method relevance; the abstract reports a 4,096-virtual-patient evaluation and comparison with a fixed-target baseline. No independent attention signal was verified.
- **Claimed contribution:** At a nominal 5% risk threshold the method recommended a dose for 74% of virtual patients; 6.9% of those with recommendations had a MAP reading below 65 mmHg. The fixed 70-mmHg comparison reports 25% over the full virtual cohort.
- **Caveat:** This is retrospective/model-based evaluation, not a prospective clinical trial; the recommendation subset and full-cohort comparator are not identical populations. It is not evidence of clinical benefit or a treatment recommendation.
- **Announcement type:** new submission, 2026-11-12
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 7. [A Feasibility Study of Whole-Cerebrum Task-Based fMRI at 0.55 T: Motor and Visual Tasks Using Single-Shot EPI](https://arxiv.org/abs/2611.17211)
- **Abstract:** In six healthy participants, the authors report detectable task fMRI activations at 0.55 T and improved sensitivity with longer acquisitions, with a representative 3 T dataset as reference context.
- **Authors:** Parsa Razmara, Takfarinas Medani, Anand A. Joshi, Majid Abbasi Sisara, Ye Tian, Sophia X. Cui, Justin P. Haldar, Krishna S. Nayak, Richard M. Leahy
- **arXiv:** `2611.17211v1` (published 2026-11-12T18:09:22Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Direct medical-physics relevance; the primary abstract reports six participants and a within-session comparison of 5- versus 10-minute acquisitions.
- **Claimed contribution:** The authors report FWE-corrected task activations at 0.55 T and a 47% reduction in voxelwise dispersion after combining two runs; they conclude that longer low-field scans may offset some sensitivity loss in this setup.
- **Caveat:** Six healthy volunteers and a representative 3 T reference do not establish general clinical equivalence, diagnostic accuracy, or patient benefit.
- **Announcement type:** new submission, 2026-11-12
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 8. [Symmetry-Induced Conservation Laws, Three-Channel Attribution, and Solid-Phase Recycling in Prebiotic Enantiomeric Excess Amplification](https://arxiv.org/abs/2611.10725)
- **Abstract:** The authors formalize how phase removal, subpool fractionation, and chiral-excess changes contribute to enantiomeric excess, and re-analyze prebiotic chemistry benchmarks under explicit symmetry assumptions.
- **Authors:** Zeyu Jia, Anlin Gong, Bingmei Wu
- **arXiv:** `2611.10725v2` (first submitted 2026-11-07T13:38:03Z; revised 2026-11-12T03:06:16Z; categories: `q-bio.BM`)
- **Evidence for ranking:** A revision in the selected batch and direct biochemical/prebiotic-chemistry relevance; no independent attention signal was used to rank it.
- **Claimed contribution:** The authors state that their accounting framework distinguishes apparent enrichment caused by mass removal from net chiral-excess change, and report re-analysis of seven experimental systems plus model/data-set analyses. These are the authors’ theoretical and re-analysis claims.
- **Caveat:** The conclusions depend on the stated network and symmetry assumptions; the abstract reports re-analysis and modeling rather than new wet-lab validation. The version change is labeled as a revision, not a new paper.
- **Announcement type:** revision, 2026-11-12
- **Themes:** Prebiotic chemistry; Quantitative methods

## Trending Research Themes

Protein-model behavior and mutation-effect prediction form the most repeated thread in this batch. MutAtlas combines FoldX, protein-language-model, and inverse-folding signals while explicitly representing disagreement; the relabeling study tests whether protein-language-model contact maps rely on canonical residue labels; and the DEL paper estimates the data density needed to learn local binding-affinity differences. These papers concern distinct tasks and do not independently validate one another. The review by Cai et al. supplies a broader framework for describing model knowledge boundaries, but is a review rather than new benchmark evidence.

A second, smaller thread is how computational methods support biomedical decisions or interpretation. The fMRI paper reports feasibility measurements in six healthy volunteers, the blood-pressure paper evaluates a model on retrospective data and virtual patients, and the echinocyte paper uses a red-cell mechanics model. Their evidence types differ—human imaging observations, retrospective/in-silico decision modeling, and simulation—so they should not be combined into a single claim of clinical readiness.

## Open Problems and Research Directions

The authors’ evidence boundaries point to concrete follow-ups. For MutAtlas, test whether the modest ProteinGym ranking improvement transfers to prospective deep-mutational-scanning assays on proteins and sites held out by family, and report performance stratified by assay type. For the relabeling diagnostic, broaden the protein families, model families, and residue groupings, then compare public checkpoints with models retrained on consistently relabeled corpora; the paper itself notes its limited family/model scope and that invariance alone is not sufficient proof of coevolutionary inference. For DEL sizing, synthesize a small set of hit-centered libraries at multiple predicted complexities and compare observed tight-binder counts and affinity resolution with the predicted yield.

For low-field fMRI, a larger, prespecified cohort with matched 0.55 T and 3 T acquisition, repeat sessions, and task-specific sensitivity endpoints would test whether the reported scan-time trade-off generalizes. For blood-pressure control, evaluate prospectively with a matched comparator, report calibration across clinical subgroups, and measure clinician overrides and safety outcomes before considering workflow use. For the echinocyte mechanism, compare shape-sorted stored red cells in a slit-like microfluidic device and directly measure bilayer–cytoskeleton strain or detachment. These are research proposals based on the reported limitations, not clinical advice.

## Takeaway

This batch’s strongest shared signal is more careful characterization of protein-model inputs and disagreement, alongside a few distinct biomedical modeling and feasibility studies. The two venue-linked protein papers have checkable acceptance signals, but the available data do not support an arXiv-wide popularity ranking. Treat model outputs and feasibility claims as preprint evidence until the specific computational predictions and human-facing conclusions receive validation in the settings where they would be used.

## Method and sources

- **Window:** daily, latest available announcement batch dated 2026-11-12; eligible submissions/revisions dated 2026-11-12. The report uses the prior available batch relative to the 2026-11-13 snapshot. Snapshot: 2026-11-13T17:13:58Z.
- **Candidate query:** [arXiv API](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200) across `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. The retrieved 200-entry page reached 2026-10-29, beyond the selected batch; the eight retained records were deduplicated by versionless arXiv ID and checked against their arXiv abstract pages.
- **Ranking:** no official arXiv trend/readership statistics exist. Since direct attention evidence was sparse, entries are ranked by relevance to the requested biology/biomedicine scope and checkable publication/update signals, not by inferred reads or downloads. The ranking signals are stated per entry. Semantic Scholar returned current citation metadata only for the prebiotic revision (0 citations at snapshot); citation totals are not window gains. Selected-paper abstracts and top-paper full text were checked on arXiv; external corroboration includes the [PMLR/ICML MutAtlas listing](https://proceedings.mlr.press/v306/guo26c.html), the [ICML poster page](https://icml.cc/virtual/2026/poster/63147), and the [NeurIPS workshop listing](https://neurips.cc/virtual/2026/169424).
- **Coverage caveat:** arXiv is not representative of biomedical preprints; much clinical and experimental work appears on bioRxiv, medRxiv, or elsewhere. This is not a systematic review or clinical guidance. Claims are attributed to the preprints; no patient-specific advice is offered.
