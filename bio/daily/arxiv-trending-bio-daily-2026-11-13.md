# arXiv Trending Biology and Biomedicine — Friday, 13 November 2026

## Headline

Daily arXiv biology/biomedicine report for the Friday 13 November announcement batch: 11 papers selected. The strongest recurring pattern is computational biology models being tested against molecular, sequencing, or cell-level evidence, while direct experimental and clinical validation remains uneven. Today’s agenda: environmental resistance enzymes, RNA silencing and perturbation prediction, protein-variant models, diagnostic sequencing, and one low-field MRI feasibility study. This is the most recent batch because Saturday, 14 November has no newer announcement batch. arXiv has no official trending chart; this is an inferred relevance ranking over an incomplete arXiv-only slice of biomedical research, not a readership or download ranking.

## Notable recent papers (ranked by relevance)

### 1. [Deep learning-guided discovery reveals the diversity and mutational potential of environmental beta-lactamases](https://arxiv.org/abs/2611.14568)
- **Abstract:** The authors combine protein-language-model representations and ensemble learning to identify over 46,000 putative environmental beta-lactamases, then report resistance assays for divergent candidates and mutation effects.
- **Authors:** Liangjun Ge, Qiandi Gao, Haiming Xu, Zhiwei Qin, Heqian Zhang
- **arXiv:** `2611.14568v1` (published 2026-11-09 14:29:14 UTC; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** Direct antimicrobial-resistance relevance; the authors report expression/antibiotic testing, including MIC-based validation, rather than sequence prediction alone. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors claim a PLM/ensemble workflow expands the candidate reservoir and identifies mutation-associated resistance changes; their abstract reports divergent candidates conferring resistance when expressed in E. coli.
- **Caveat:** The full text says experimental characterization covered only two class-C candidates, with resistance assessed mainly by MIC; this does not establish environmental prevalence, transmission, or human risk.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; DNA & genomics; Bioinformatics & sequence analysis

### 2. [Silscore: modelling siRNA potency with positional thermodynamics and data-selected nucleotide-identity terms](https://arxiv.org/abs/2611.15812)
- **Abstract:** Silscore is a compact guide-sequence-only model combining global and positional duplex thermodynamics with sparse nucleotide-identity terms, evaluated on held-out and external siRNA potency datasets.
- **Authors:** Giuseppe Sacco, Isabella Baldini, Riccardo Paone, Mattia Capulli, Guido Sanguinetti, Giovanni Bussi
- **arXiv:** `2611.15812v1` (published 2026-11-11 18:28:24 UTC; categories: `q-bio.BM`, `physics.bio-ph`, `q-bio.QM`)
- **Evidence for ranking:** Strong fit to RNA design; the paper reports evaluations on the Huesken split plus Mixset and Katoh–Suzuki external datasets and an unseen-target transfer test. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report the highest observed Pearson correlation among evaluated comparators in three transfer evaluations, with a 26-parameter interpretable model.
- **Caveat:** This is retrospective dataset validation, not a prospective silencing experiment; a guide-only model omits target-site accessibility and transcript context by design.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** RNA & transcriptomics; Biochemistry & proteins; Quantitative methods

### 3. [Predicting transcriptional interactions with GrnPFN](https://arxiv.org/abs/2611.14559)
- **Abstract:** GrnPFN uses a prior-data-fitted network trained on simulated gene-regulatory screens to predict non-additive transcriptional responses from single-perturbation profiles, with measured combinations added in context without retraining.
- **Authors:** Haihui Zhang
- **arXiv:** `2611.14559v1` (published 2026-11-05 00:32:22 UTC; categories: `q-bio.MN`)
- **Evidence for ranking:** Direct relevance to gene regulation and single-cell perturbation studies; evaluated across CRISPR activation, RNA knockdown and drug-combination screens, with an additional CRISPRi–drug screen. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The author reports better prediction than specified gradient-boosting and kernel-ridge baselines under low-measurement settings, including transfer to an additional perturbation screen.
- **Caveat:** The paper notes that several pair folds overlap in perturbation members or compounds, some partitions reuse cells, and the additional drug–gene test covers one drug in one cell line; broader independent prospective tests are needed.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Omics & single-cell methods

### 4. [MutAtlas: A PDB-Wide Energy-Guided Atlas of Protein Mutation Effects](https://arxiv.org/abs/2611.16361)
- **Abstract:** MutAtlas assembles computational mutation preferences across experimentally resolved PDB structures and distills physics-based, protein-language-model, and inverse-folding signals while representing their disagreement.
- **Authors:** Ruihan Guo, Chaoran Cheng, Zhanghan Ni, Neil He, Bangji Yang, Ge Liu
- **arXiv:** `2611.16361v1` (published 2026-11-12 06:22:47 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** The arXiv comment says accepted at ICML 2026; the authors report a ProteinGym zero-shot benchmark and release a dataset/evaluation pipeline. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors claim that learning relative mutation preferences while modeling disagreement improves overall performance over the tested zero-shot baselines and naive multi-source fusion methods.
- **Caveat:** The method is trained without experimental mutation labels and is assessed on benchmark data; model-derived mutation preferences are not biochemical measurements or clinical variant interpretations.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 5. [CupOFMoCA: Coupled Objective-Guided Discrete Flows for Molecular Conjugate Assembly](https://arxiv.org/abs/2611.16099)
- **Abstract:** CupOFMoCA generates molecular conjugates while applying cross-component chemical constraints during generation, with computational evaluations across peptide-drug conjugate and PROTAC systems.
- **Authors:** Ruoxi Rosie Zhang, Ziang Li, Jiatao Gu, Pranam Chatterjee
- **arXiv:** `2611.16099v1` (published 2026-11-11 23:18:03 UTC; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** The arXiv comment identifies publication in NeurIPS 2026; the abstract reports tests on three PDC systems and three PROTAC systems, including post-hoc scoring and molecular-dynamics checks. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report improved chemically valid assembly yield versus tested post-hoc filtering and higher assembly validity on two of three PROTAC systems.
- **Caveat:** The evidence is computational generation, predicted binding/degradation scoring, and simulation; the generated molecules were not shown in the abstract to have experimentally measured degradation or therapeutic efficacy.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 6. [AVA: Agentic Variant Adjudication for Automated, Auditable Read-Level Review in Cancer Diagnostic Sequencing](https://arxiv.org/abs/2611.14560)
- **Abstract:** AVA uses auditable agent workflows to review read-level evidence for borderline low-variant-allele-frequency calls, and is evaluated on a DNA-sequencing benchmark and patient RNA-seq data.
- **Authors:** Caleb Chin, Sidharth Gupta, Arun K Anguraj Vadivel, Robert Siddaway, Siddharth Arya, Arianna He, Peter Zhukovsky, Cynthia Hawkins
- **arXiv:** `2611.14560v1` (published 2026-11-05 06:41:32 UTC; categories: `q-bio.GN`, `cs.AI`)
- **Evidence for ranking:** The arXiv comment says accepted to the ML4H 2026 Findings Track; the abstract names the SEQC2 DNA-seq benchmark and patient RNA-seq data. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report that several closed- and open-weight agents outperform the best tested VAF/depth thresholds on a subsample of borderline variants and produce reasoning traces for review.
- **Caveat:** Benchmark performance is not prospective clinical validation; the abstract does not establish impacts on diagnostic errors, turnaround time, or patient outcomes in routine laboratories.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** DNA & genomics; Biomedical & translational medicine; Bioinformatics & sequence analysis

### 7. [Stage-Resolved EBV-Induced B-Cell Programs Across CNS Selection and Multiple Sclerosis Compartments](https://arxiv.org/abs/2611.14524)
- **Abstract:** A cross-dataset reanalysis finds stage- and compartment-dependent EBV-associated B-cell transcriptional programs rather than a stable signature shared across blood, cerebrospinal fluid, and brain.
- **Authors:** Hasan Jamil, Alexander Gow
- **arXiv:** `2611.14524v1` (published 2026-09-23 23:28:52 UTC; categories: `q-bio.GN`, `cs.DB`, `cs.IR`)
- **Evidence for ranking:** The paper combines human and humanized-mouse datasets with multiple control analyses; the abstract reports nine evaluable human CSF participants and five EBV-exposed mice for key contrasts. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report that an early EBV-associated expression program was depleted in CSF while later latency-associated programs increased, with the directions persisting after shared genes were removed.
- **Caveat:** The study is a retrospective reanalysis with small evaluable samples for key contrasts; the factor did not predict MS activity (AUC 0.487), and the results do not establish causation or a validated biomarker.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** RNA & transcriptomics; Molecular & cell biology; Biomedical & translational medicine

### 8. [Protein Language Models Fail To Capture Contact Predictions Under Invariant Relabeling](https://arxiv.org/abs/2611.16881)
- **Abstract:** The authors test whether protein language models preserve contact predictions after a global amino-acid relabeling that leaves alignment-level statistics unchanged, reporting marked degradation across models and scales.
- **Authors:** Paarth Batra, Aryan Keluskar
- **arXiv:** `2611.16881v1` (published 2026-11-12 14:45:07 UTC; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** Accepted to the ICBINB failure-modes workshop at NeurIPS 2026 per the arXiv comment; tests cover ESM-2, MSA Transformer, and AMPLIFY from 8M to 3B parameters. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors claim the perturbation exposes reliance on canonical residue identities (“alphabet anchoring”) rather than only invariant coevolutionary statistics.
- **Caveat:** This is a computational invariance stress test; it demonstrates sensitivity of model outputs to token relabeling, not a direct experimental failure of protein structure prediction in biological settings.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 9. [Using an energy pixels approach to estimate the size a 2nd Generation DEL must be to train a high-resolution binding model](https://arxiv.org/abs/2611.17121)
- **Abstract:** An energy-pixels model estimates how large a focused second-generation DNA-encoded library may need to be to sample local chemical neighborhoods and provide enough tight binders for affinity-model training.
- **Authors:** Boris P. Belotserkovskii, R. Edward Watts
- **arXiv:** `2611.17121v1` (published 2026-11-12 17:13:57 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** It directly addresses data design for protein-binding models and appears in both machine-learning and biomolecular categories; its abstract gives an explicit route to compare active-learning yield with a random-library baseline. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors claim their estimates translate the number of tight binders needed by a model into a library-size requirement without structural information or a control library as large as the experiment.
- **Caveat:** The approach rests on an additive “pixel” model and affinity distributions from a naive library; predicted library requirements and yields need experimental validation.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 10. [AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems](https://arxiv.org/abs/2611.17015)
- **Abstract:** This review proposes a framework for describing where biological foundation models and agentic workflows are reliable, organized around data, architecture, training, evaluation, and post-analysis.
- **Authors:** Tian Cai, Andrew Kleist, Jaimin Patel, Duccio Malinverni, Alexander K. Taylor, Malvika Sharan, Renato Umeton, M. Madan Babu
- **arXiv:** `2611.17015v1` (published 2026-11-12 16:08:33 UTC; categories: `q-bio.BM`, `cs.AI`)
- **Evidence for ranking:** The arXiv comment says it is to be published in Annual Review of Biomedical Data Science; its subject is broad evaluation reliability across sequence, protein, and single-cell models. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors propose standardized descriptions of model limits so researchers and model-using agents can state the conditions under which outputs may be trusted.
- **Caveat:** This is a review and framework proposal, not a new controlled comparison or a validated operational standard.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Bioinformatics & sequence analysis; Biochemistry & proteins; Quantitative methods

### 11. [A Feasibility Study of Whole-Cerebrum Task-Based fMRI at 0.55 T: Motor and Visual Tasks Using Single-Shot EPI](https://arxiv.org/abs/2611.17211)
- **Abstract:** A six-participant feasibility study reports detectable motor and visual task fMRI at 0.55 T and improved signal statistics when two five-minute runs are combined.
- **Authors:** Parsa Razmara, Takfarinas Medani, Anand A. Joshi, Majid Abbasi Sisara, Ye Tian, Sophia X. Cui, Justin P. Haldar, Krishna S. Nayak, Richard M. Leahy
- **arXiv:** `2611.17211v1` (published 2026-11-12 18:09:22 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** This is the latest medical-physics batch’s directly biomedical imaging feasibility paper; the abstract reports six healthy participants, both tasks, and a comparison to a representative 3 T dataset. Semantic Scholar listed 0 citations and 0 influential citations at the snapshot.
- **Claimed contribution:** The authors report task activations at 0.55 T and suggest longer acquisition can compensate for lower intrinsic BOLD sensitivity in their tested setting.
- **Caveat:** The sample is small and healthy; the 3 T reference is described as representative rather than a matched cohort. The result does not establish clinical utility or broad reproducibility.
- **Announcement type:** new submission, 2026-11-13 batch
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

## Trending Research Themes

- **Prediction under biological constraints:** GrnPFN, MutAtlas, CupOFMoCA, the environmental beta-lactamase study, the protein-language-model relabeling test, and the DEL energy-pixels paper all use computational models, but they test different outputs: perturbation responses, mutation preferences, valid molecular assemblies, enzyme function, contact maps, and library-size estimates. These are related uses of modeling, not independent evidence for one general “AI biology” capability.
- **RNA and gene-regulation decisions:** Silscore predicts siRNA potency from guide features, while GrnPFN predicts non-additive expression responses to combined genetic or chemical perturbations. Both use retrospective data; their distinct targets should not be conflated with measured therapeutic efficacy.
- **Molecular evidence and translation boundaries:** The beta-lactamase work includes limited E. coli resistance assays; AVA evaluates sequencing adjudication benchmarks; and the EBV paper reanalyzes human and mouse datasets. Their evidence types differ, and none by itself establishes clinical benefit or a practice-changing biomarker.
- **Medical imaging:** The 0.55 T fMRI paper is a single small feasibility study. It is notable within this batch, but does not support a field-wide shift in low-field imaging.

## Open Problems and Research Directions

These directions follow from limitations reported in the selected papers and are proposals, not established priorities or clinical advice.

- **Broaden experimental enzyme validation:** The beta-lactamase paper’s full text identifies only two class-C candidates as experimentally characterized. A next step is a blinded panel spanning all Ambler classes and habitats, with expression/stability controls, MIC and direct hydrolysis assays, followed by competition or evolution experiments to test whether predicted resistance shifts persist under defined antibiotic exposures.
- **Test transfer models prospectively:** Silscore and GrnPFN report retrospective transfer across external datasets or screens. A prospective design could freeze each model before testing, hold out targets, cell lines, perturbation pairs, and laboratories, and report calibration alongside correlation/error. For Silscore, include target accessibility and chemistry-informed controls; for GrnPFN, measure new combinations in independent screens rather than relying only on overlapping perturbation members.
- **Separate computational mutation scores from function:** MutAtlas should be compared with new deep-mutational-scanning experiments across structurally diverse proteins, including proteins and assay types absent from its development benchmark. This would test whether disagreement-aware distillation improves experimentally measured function rather than only benchmark ranking.
- **Establish diagnostic workflow performance:** AVA could be evaluated in a blinded multi-laboratory study with prespecified borderline-variant sets, expert adjudication, false-positive/false-negative rates, auditability, and turnaround time. That would address deployment questions not answered by benchmark comparisons alone.
- **Increase independent imaging validation:** The 0.55 T fMRI result calls for a larger, diverse, same-subject 0.55 T/3 T comparison with prespecified tasks and test–retest analysis. The current six-person feasibility study cannot establish performance across patient groups or clinical indications.

## Takeaway

This batch is strongest in computational methods for molecular and perturbation biology, with several papers making their evidence boundary visible. The clearest experimental result is limited enzyme testing; the RNA, protein-variant, diagnostic, and conjugate-design claims remain dataset- or model-based. Treat the ranking as a relevance-led reading list, not a popularity chart or a clinical evidence assessment.

## Method and sources

- **Window:** daily; announcement-batch date 2026-11-13 only. The report uses the prior batch because 2026-11-14 is Saturday and no newer batch was listed. Exact date range: 2026-11-13 through 2026-11-13. Snapshot: 2026-11-14 17:13:01 UTC.
- **Candidate scope:** arXiv categories `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. The candidate listings checked were the 13 November quantitative-biology new/cross-list page and medical-physics recent page; 11 papers are selected from the in-scope batch after relevance screening. Neuroscience and population-only items were excluded.
- **Ranking:** There is no official arXiv trend ranking. Semantic Scholar Graph API citation and influential-citation totals were 0 for all 11 selected records at the snapshot. Attention evidence was insufficient to call these “trending”; entries are ranked by demonstrated relevance and reported evidence. Conference/journal comments and cross-list breadth are disclosed where present, and recency is not treated as popularity. Citation totals are point-in-time totals, not gains during the day.
- **Metadata and reading:** Candidate metadata and abstracts were checked against arXiv abstract pages and the arXiv API. The first three papers were also read in HTML full text for introduction, results, and limitations/discussion. Author-reported evidence is attributed; computational predictions, assays, retrospective reanalyses, and clinical evidence are kept distinct.
- **Coverage caveat:** This covers the configured arXiv categories only. arXiv is not a representative biomedical index; much experimental and clinical preprint activity appears on bioRxiv or medRxiv, and the report does not cover those repositories or the broader medical literature.
- **Sources:** [arXiv quantitative biology new listings](https://arxiv.org/list/q-bio/new); [arXiv medical physics recent listings](https://arxiv.org/list/physics.med-ph/recent); [arXiv API category query](https://export.arxiv.org/api/query?search_query=cat%3Aq-bio.BM+OR+cat%3Aq-bio.GN+OR+cat%3Aq-bio.MN+OR+cat%3Aq-bio.SC+OR+cat%3Aq-bio.CB+OR+cat%3Aq-bio.TO+OR+cat%3Aq-bio.QM+OR+cat%3Acs.BI+OR+cat%3Aphysics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200); [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/batch).
