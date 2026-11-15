# Notable recent biology and biomedical papers — Friday, 13 November 2026 arXiv batch

Thirteen papers are selected from the latest biology/biomedicine announcement batch. The clearest recurring pattern is computational methods being tested against molecular or assay data, with important gaps between in-silico performance and experimental or clinical validation. Spoken agenda: resistance enzymes, siRNA potency and perturbation response; protein mutation and conjugate design; sequencing adjudication; then biomedical modeling and imaging. arXiv has no official trending chart; this relevance-ranked list is inferred from incomplete arXiv coverage and is not a measured popularity ranking.

Semantic Scholar returned zero citations and zero influential citations for all 13 papers at the snapshot, so citation momentum does not support a popularity ranking. The entries below are therefore “Notable recent papers,” ranked by direct relevance and checkable research evidence, not by readership, downloads, or author reputation. Acceptance and journal comments are reported as publication-status signals only.

## Notable recent papers

### 1. [Deep learning-guided discovery reveals the diversity and mutational potential of environmental beta-lactamases](https://arxiv.org/abs/2611.14568)
- **Abstract:** The authors combine protein-language-model representations and ensemble learning to identify environmental beta-lactamase candidates, then report resistance assays for two divergent enzymes and mutation effects.
- **Authors:** Liangjun Ge, Qiandi Gao, Haiming Xu, Zhiwei Qin, Heqian Zhang
- **arXiv:** `2611.14568v1` (published 2026-11-09 14:29:14 UTC; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Direct antimicrobial-resistance and protein-function relevance; the authors report expression and antibiotic testing, including MIC measurements, rather than sequence prediction alone. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report identifying more than 46,000 putative environmental beta-lactamases and finding that two divergent class-C candidates expressed in *E. coli* confer resistance to multiple beta-lactams; predicted substitutions altered resistance profiles.
- **Caveat:** The full paper states that experimental characterization covered only two class-C candidates and resistance was assessed primarily by MIC. It does not establish environmental prevalence, transmission, or human risk.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; DNA & genomics; Bioinformatics & sequence analysis

### 2. [Silscore: modelling siRNA potency with positional thermodynamics and data-selected nucleotide-identity terms](https://arxiv.org/abs/2611.15812)
- **Abstract:** Silscore is a compact guide-sequence-only model combining overall and position-specific duplex thermodynamics with sparse nucleotide-identity terms to estimate siRNA potency.
- **Authors:** Giuseppe Sacco, Isabella Baldini, Riccardo Paone, Mattia Capulli, Guido Sanguinetti, Giovanni Bussi
- **arXiv:** `2611.15812v1` (published 2026-11-11 18:28:24 UTC; categories: `q-bio.BM`, `physics.bio-ph`, `q-bio.QM`)
- **Evidence for ranking:** Direct RNA silencing-design question; tested on the Huesken split, Mixset, Katoh–Suzuki, and an unseen-target transfer setting. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report that the 26-parameter model has the highest observed Pearson correlation in three transfer evaluations; on Katoh–Suzuki, the data support an advantage over each applicable comparator. The paper also reports that some other comparisons are inconclusive.
- **Caveat:** These are retrospective dataset evaluations, not prospective silencing experiments. The guide-only model omits target-site accessibility and transcript context by design.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** RNA & transcriptomics; Biochemistry & proteins; Quantitative methods

### 3. [Predicting transcriptional interactions with GrnPFN](https://arxiv.org/abs/2611.14559)
- **Abstract:** GrnPFN uses simulated gene-regulatory-network screens for pretraining, then predicts non-additive transcriptional responses to combined perturbations from single-perturbation profiles and limited measured combinations.
- **Authors:** Haihui Zhang
- **arXiv:** `2611.14559v1` (published 2026-11-05 00:32:22 UTC; categories: `q-bio.MN`)
- **Evidence for ranking:** Direct gene-regulation and single-cell perturbation focus; the paper evaluates CRISPR activation, RNA knockdown, and drug combinations and includes an additional CRISPRi–drug screen. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The author reports better prediction than tested gradient-boosting and kernel-ridge baselines when combination measurements are absent or limited, with the relative advantage diminishing as screen-specific combinations accumulate.
- **Caveat:** The full paper notes that several later partitions reused cells, perturbation-pair folds overlap in members or compounds, and an additional drug–gene evaluation involved one drug in one cell line. Predicted transcriptional non-additivity does not itself establish a molecular mechanism or synergy in other phenotypes.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Omics & single-cell methods

### 4. [MutAtlas: A PDB-Wide Energy-Guided Atlas of Protein Mutation Effects](https://arxiv.org/abs/2611.16361)
- **Abstract:** MutAtlas assembles mutation signals from physics-based, protein-language, and inverse-folding models across experimentally resolved structures, then proposes disagreement-aware distillation for zero-shot mutation-effect prediction.
- **Authors:** Ruihan Guo, Chaoran Cheng, Zhanghan Ni, Neil He, Bangji Yang, Ge Liu
- **arXiv:** `2611.16361v1` (published 2026-11-12 06:22:47 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Direct protein mutation interpretation and engineering relevance; cross-listed in genomics; the arXiv comment says accepted at ICML 2026. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report that their method, trained without experimental mutation labels, had the best overall performance among evaluated zero-shot baselines and naive fusion strategies on ProteinGym; the full-text table reports 0.498 overall macro-averaged Spearman correlation.
- **Caveat:** This is a computational benchmark result using model-generated training signals, not experimental or clinical validation. Generalization across proteins, assays, and engineering decisions remains to be tested.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 5. [CupOFMoCA: Coupled Objective-Guided Discrete Flows for Molecular Conjugate Assembly](https://arxiv.org/abs/2611.16099)
- **Abstract:** CupOFMoCA generates PROTACs and peptide–drug conjugates while enforcing cross-component chemical constraints during generation rather than filtering invalid assemblies afterward.
- **Authors:** Ruoxi Rosie Zhang, Ziang Li, Jiatao Gu, Pranam Chatterjee
- **arXiv:** `2611.16099v1` (published 2026-11-11 23:18:03 UTC; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** Direct molecular-conjugate design application; arXiv comment identifies publication at NeurIPS 2026. The abstract reports evaluations across three peptide–drug-conjugate and three PROTAC systems. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report improved valid-conjugate yield over matched post-hoc filtering for peptide–drug conjugates and the highest assembly validity on two of three PROTAC systems; they also report post-hoc scoring and molecular-dynamics analyses.
- **Caveat:** Evidence is computational generation, predicted scoring, and simulation; the paper does not establish experimentally measured degradation, binding, or therapeutic efficacy for generated molecules.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 6. [AVA: Agentic Variant Adjudication for Automated, Auditable Read-Level Review in Cancer Diagnostic Sequencing](https://arxiv.org/abs/2611.14560)
- **Abstract:** AVA uses auditable agent workflows to inspect read-level sequencing evidence for borderline low-variant-allele-frequency calls, evaluated on a DNA-sequencing benchmark and patient RNA-seq data.
- **Authors:** Caleb Chin, Sidharth Gupta, Arun K Anguraj Vadivel, Robert Siddaway, Siddharth Arya, Arianna He, Peter Zhukovsky, Cynthia Hawkins
- **arXiv:** `2611.14560v1` (published 2026-11-05 06:41:32 UTC; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Direct cancer-sequencing workflow relevance; the abstract names the SEQC2 DNA-seq benchmark and patient RNA-seq data, and the arXiv comment reports acceptance to the ML4H 2026 Findings Track. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report that tested closed- and open-weight agents outperformed the best VAF/depth thresholds on a subsample of borderline variants, returning auditable reasoning traces.
- **Caveat:** Benchmark results do not establish performance in routine prospective laboratories, diagnostic error reduction, turnaround-time improvement, or patient benefit.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** DNA & genomics; Biomedical & translational medicine; Bioinformatics & sequence analysis

### 7. [Protein Language Models Fail To Capture Contact Predictions Under Invariant Relabeling](https://arxiv.org/abs/2611.16881)
- **Abstract:** An amino-acid alphabet permutation that preserves alignment statistics disrupts contact predictions from tested protein language models, unlike the classical Potts and inverse-covariance estimators.
- **Authors:** Paarth Batra, Aryan Keluskar
- **arXiv:** `2611.16881v1` (published 2026-11-12 14:45:07 UTC; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** Direct protein-model interpretability result; tests ESM-2, MSA Transformer, and AMPLIFY across multiple scales; the arXiv comment reports acceptance to the ICBINB failure-modes workshop at NeurIPS 2026. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** Across nine proteins, the authors report that global residue relabeling sharply reduces model contact-map overlap while Potts predictions remain invariant, which they interpret as evidence of “alphabet anchoring.”
- **Caveat:** The full paper limits the evaluation to a relatively small set of short, mostly single-domain proteins and three model families. The authors state that invariance is necessary but not sufficient evidence for pure coevolutionary inference; retrained or fine-tuned models were not tested.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 8. [Using an energy pixels approach to estimate the size a 2nd Generation DEL must be to train a high-resolution binding model](https://arxiv.org/abs/2611.17121)
- **Abstract:** The authors model target–ligand binding as sums of interaction “pixels” and use affinity distributions from a naive DNA-encoded library to estimate the complexity and expected yield of a focused follow-up library.
- **Authors:** Boris P. Belotserkovskii, R. Edward Watts
- **arXiv:** `2611.17121v1` (published 2026-11-12 17:13:57 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Direct biomolecular binding and medicinal-chemistry data-design relevance; cross-listed in biomolecules. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors say the model translates a desired number of tight binders into an estimated library size and supplies a random-design baseline against which machine-learning or active-learning designs could be assessed.
- **Caveat:** This is a model-based sizing method inferred from existing affinity distributions; no prospective synthesis-and-selection test of the predicted second-generation library is reported.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 9. [AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems](https://arxiv.org/abs/2611.17015)
- **Abstract:** This review frames a biological model’s “knowledge boundary” around data, architecture, training, evaluation, and post-analysis, to make reliability limits explicit for researchers and tool-using agents.
- **Authors:** Tian Cai, Andrew Kleist, Jaimin Patel, Duccio Malinverni, Alexander K. Taylor, Malvika Sharan, Renato Umeton, M. Madan Babu
- **arXiv:** `2611.17015v1` (published 2026-11-12 16:08:33 UTC; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** Broad biological foundation-model scope; the arXiv comment says it is to be published in Annual Review of Biomedical Data Science. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors synthesize evidence about where biological foundation models succeed or fail and propose standardized descriptions of the conditions under which their outputs are reliable.
- **Caveat:** This is a review and framework proposal, not a new comparative benchmark or prospective demonstration that the framework improves biological decisions.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Omics & single-cell methods

### 10. [Stage-Resolved EBV-Induced B-Cell Programs Across CNS Selection and Multiple Sclerosis Compartments](https://arxiv.org/abs/2611.14524)
- **Abstract:** A cross-dataset reanalysis reports compartment- and stage-dependent EBV-associated B-cell transcriptional programs, rather than a stable signature shared across blood, cerebrospinal fluid, and brain.
- **Authors:** Hasan Jamil, Alexander Gow
- **arXiv:** `2611.14524v1` (published 2026-09-23 23:28:52 UTC; categories: `q-bio.GN`, `cs.DB`, `cs.IR`)
- **Evidence for ranking:** The paper appeared in the 13 November q-bio.GN recent-list batch as a category listing; its arXiv record retains the earlier first-submission date shown above. The abstract reports human and humanized-mouse data with anatomical, sequencing-depth, and other controls. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report that a frozen EBV-associated B-cell factor did not predict MS activity (AUC 0.487; p=0.489), and that early and late EBV-associated transcriptional programs showed opposing directions across compartments.
- **Caveat:** This is retrospective reanalysis with small samples for key contrasts, including nine evaluable human CSF participants and five EBV-exposed mice. The authors state that no external program met their prespecified prospective criterion; the results do not establish causation or a validated biomarker.
- **Announcement type:** new q-bio.GN category listing, 2026-11-13 batch (original arXiv submission 2026-09-23)
- **Themes:** RNA & transcriptomics; Molecular & cell biology; Biomedical & translational medicine

### 11. [Stretched bilayer-cytoskeleton links hold echinocytes in a model splenic slit](https://arxiv.org/abs/2611.16241)
- **Abstract:** In a two-component red-cell model, stage III echinocytes required 37–50 times the pressure drop that passed an equal-area, equal-volume discocyte through a model splenic slit; stretched bilayer–cytoskeleton links were implicated in retention.
- **Authors:** Zhaojie Chai, Jianlu Zheng, He Li, Ming Dao, George Em Karniadakis
- **arXiv:** `2611.16241v1` (published 2026-11-12 03:39:47 UTC; categories: `physics.bio-ph`, `cond-mat.soft`, `physics.flu-dyn`, `q-bio.CB`)
- **Evidence for ranking:** Direct cell-mechanics and splenic-clearance question; cross-listed in cell biology and supported by a detailed mechanical study. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors' model suggests spicule shape together with membrane loss can hinder passage through a splenic slit; lengthening the modeled links by about twofold released a held cell.
- **Caveat:** Central passage and link-stretch results are from simulated cells in a model slit, not a direct test of clearance in human spleens or transfusion outcomes.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Molecular & cell biology; Biomedical & translational medicine; Quantitative methods

### 12. [A risk-aware individualized blood pressure target to avoid hypotension in surgery](https://arxiv.org/abs/2611.16757)
- **Abstract:** The authors propose an online method for choosing an individualized blood-pressure target and norepinephrine dose from a short MAP/dose record, using a reduced PK/PD model and uncertainty propagation to limit predicted hypotension risk.
- **Authors:** Simon Buré, Jona Joachim, Florent Di Meglio
- **arXiv:** `2611.16757v1` (published 2026-11-12 13:06:52 UTC; categories: `q-bio.QM`, `math.OC`)
- **Evidence for ranking:** Direct perioperative biomedical decision-modeling question; the abstract reports retrospective-record calibration and a cohort of 4,096 virtual patients. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** In the virtual cohort, the method recommended a dose for 74% at a nominal 5% risk; 6.9% of patients receiving recommendations had a MAP reading below 65 mmHg, compared with 25% under a fixed 70 mmHg target applied to the full virtual cohort.
- **Caveat:** The comparison is not a prospective clinical trial: recommendations were assessed retrospectively under doses actually administered and in virtual patients. It does not establish clinical benefit or safety.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 13. [A Feasibility Study of Whole-Cerebrum Task-Based fMRI at 0.55 T: Motor and Visual Tasks Using Single-Shot EPI](https://arxiv.org/abs/2611.17211)
- **Abstract:** In six healthy participants, the authors detected motor- and visual-task activation at 0.55 T and report that concatenating two five-minute runs increased activation statistics and reduced voxelwise background dispersion.
- **Authors:** Parsa Razmara, Takfarinas Medani, Anand A. Joshi, Majid Abbasi Sisara, Ye Tian, Sophia X. Cui, Justin P. Haldar, Krishna S. Nayak, Richard M. Leahy
- **arXiv:** `2611.17211v1` (published 2026-11-12 18:09:22 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Direct medical-physics imaging feasibility question with a stated healthy-participant sample and task comparison. Semantic Scholar snapshot: 0 citations, 0 influential citations.
- **Claimed contribution:** The authors report that whole-cerebrum task fMRI was feasible with single-shot EPI at 0.55 T; a representative 3 T dataset is used for reference, and the abstract reports that longer low-field acquisition could approach 3 T statistical significance over the compared durations.
- **Caveat:** Only six healthy participants were studied; the 3 T reference is not described as a matched-cohort comparison, and this does not establish clinical diagnostic performance.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

## Trending Research Themes

- **Modeling molecular function needs context-specific validation.** The beta-lactamase study includes limited expression/MIC testing; Silscore evaluates retrospective potency datasets; GrnPFN predicts non-additive transcription; MutAtlas and the invariant-relabeling study test protein-model signals; and CupOFMoCA and the DEL paper assess generated or planned binding designs computationally. Their targets and evidence types differ, so the set supports an evaluation theme, not a single validated AI capability.
- **RNA and perturbation models emphasize transfer.** Silscore tests potency transfer across datasets/targets, while GrnPFN evaluates combination-response predictions across perturbation screens. Both remain bounded by the particular data splits, target contexts, and readouts used.
- **Translation claims remain bounded by study design.** AVA is evaluated on sequencing datasets; the EBV report is a reanalysis with small human and mouse contrasts; and the red-cell, perioperative, and low-field fMRI papers each have different model, cohort, or feasibility limits. These papers do not collectively establish clinical benefit or a field-wide clinical shift.

## Open Problems and Research Directions

These follow-ups are grounded in the limitations reported by the selected authors and are research proposals, not clinical advice.

- **Expand enzyme-function validation.** The beta-lactamase authors identify two class-C candidates as experimentally characterized and call for broader functional testing. A next study could sample divergent candidates from all Ambler classes, pair MICs with direct hydrolysis, expression, and stability assays, then test predicted substitutions across sequence backgrounds and controlled antibiotic exposures.
- **Freeze and prospectively test transfer models.** For Silscore, preregister a guide-only prediction set across targets and laboratories, then compare with models incorporating target accessibility and transcript context. For GrnPFN, prospectively measure unseen perturbation pairs in independent cell lines and screens, separating cells used for inputs from those used for evaluation and checking whether predicted transcriptional non-additivity corresponds to other phenotypes.
- **Compare model-derived protein signals with new experiments.** Test MutAtlas predictions on proteins and assays outside ProteinGym using focused deep-mutational scanning; stratify calibration and ranking by cross-model disagreement. For CupOFMoCA and the DEL sizing method, synthesize selected generated or focused-library compounds and measure binding, assembly validity, and functional effects against predefined baselines.
- **Validate diagnostic and clinical models prospectively.** AVA needs blinded multi-laboratory assessment with adjudicated variants and prespecified false-positive/false-negative and turnaround measures. The perioperative blood-pressure method needs prospective evaluation with predefined clinician override and safety endpoints. The 0.55 T fMRI result needs a larger same-subject 0.55/3 T study with repeat scans and patient cohorts before clinical-performance claims.
- **Test EBV compartment hypotheses longitudinally.** The EBV reanalysis itself calls for virologic, clonotypic, antigen-specific, epigenetic, and longitudinal evidence. A follow-up could measure paired blood/CSF samples over time with prespecified external validation, rather than inferring ancestry from transcriptional resemblance alone.

## Takeaway

This batch is most notable for methods that expose the limits of model transfer or reveal how much validation is still needed. A few papers report experimental or patient-derived data, but the strongest claims remain bounded by small experimental panels, retrospective datasets, or computational evaluation. The ranking reflects relevance, not measured arXiv popularity, and arXiv alone is incomplete biomedical coverage.

## Method and sources

- **Window:** daily; latest announcement batch Friday 2026-11-13. The current date, Sunday 2026-11-15, has no newer batch in the checked listings, so this report uses the prior Friday batch. Announcement date range: 2026-11-13 through 2026-11-13. The underlying new-submission timestamps for most selected papers span 2026-11-05 through 2026-11-12; the EBV paper is explicitly identified as a new q-bio.GN category listing although its arXiv record retains its earlier 2026-09-23 first-submission date.
- **Snapshot:** 2026-11-15 01:23:26 UTC.
- **Candidate pool:** Checked recent listings for `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph`; the broad arXiv API query also included `cs.BI`. The Friday batch had 30 category appearances (29 unique IDs after cross-list deduplication) in the checked listings; 13 papers were selected for direct biological/biomedical relevance. The API pool was paginated through 400 results, reaching first-submission dates older than the daily batch. The EBV category listing was verified directly because its stored first-submission timestamp predates this batch.
- **Ranking:** arXiv has no official trend or readership ranking. Semantic Scholar Graph API was queried by arXiv ID for citation count, influential-citation count, reference count, publication type, fields of study, and external IDs. All 13 showed 0 citations and 0 influential citations at the snapshot, so citation velocity did not provide a defensible popularity order. Entries are ranked by relevance to the requested molecular/biomedical scope and checkable reported evidence; publication-status comments and category breadth are disclosed, not treated as readership measures. No independent technical discussion was located for these candidates.
- **Reading and evidence:** All selected abstracts were checked against arXiv records. The introductions, results, and limitations/discussion of the first three papers were also read from their PDFs. Claims are attributed to the authors; predictions, assays, retrospective reanalyses, and human clinical evidence are distinguished.
- **Coverage:** This is an arXiv-only point-in-time sample. Much experimental and clinical biology appears on bioRxiv or medRxiv; those repositories and the broader medical literature are not covered. This is not a systematic review or clinical guidance.
- **Sources:** [arXiv q-bio.BM recent listings](https://arxiv.org/list/q-bio.BM/recent); [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent); [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent); [q-bio.CB](https://arxiv.org/list/q-bio.CB/recent); [q-bio.TO](https://arxiv.org/list/q-bio.TO/recent); [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent); [medical physics](https://arxiv.org/list/physics.med-ph/recent); [arXiv API category query](https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200) (paginated); [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch). Individual arXiv abstract links appear in each title.
