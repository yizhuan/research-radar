# arXiv Biology & Biomedicine — Daily — 2026-10-26

## Headline

The latest available arXiv biology/biomedicine batch is Monday, 26 October 2026; this report covers six notable papers across single-cell screens, pediatric tumor splicing, neonatal EEG, protein design, cell imaging, and immune signaling. Today’s agenda: which results are based on experiments, which are computational, and what validation remains. This is the prior announcement batch for the current UTC date, Tuesday 27 October. arXiv has no official trending chart, and attention evidence is too sparse to claim a measured popularity ranking; this is an inferred relevance ranking from incomplete biomedical coverage. arXiv does not represent biomedical publishing as a whole, and this is not a systematic or clinical review.

## Notable recent papers (ranked)

### 1. [Shared clones make random cell halves look reproducible in pooled screens](https://arxiv.org/abs/2610.32962)
- **Abstract:** The paper shows how shared cell clones can make random halves of pooled single-cell perturbation screens appear reproducible, including for null perturbations.
- **Authors:** Xuanrui Huang
- **arXiv:** `2610.32962v1` (published 2026-10-23T17:53:14Z; categories: `q-bio.QM`)
- **Evidence for ranking:** Direct clone-aware tests and null controls across 16 screens, including a genome-scale primary CD4 T-cell screen; code and results are public. Semantic Scholar reported 0 citations at the snapshot.
- **Claimed contribution:** The author reports 96–99% positive agreement for null targets under random halves in the primary T-cell screen, versus roughly chance-level agreement across independent replicates; the excess did not disappear simply by measuring more cells.
- **Caveat:** Screen types and cell systems differ; many source datasets lack clone labels, and some size estimates rely on limited null controls. This cautions against overgeneralizing the reported effect size.
- **Announcement type:** new submission, 2026-10-26 announcement batch
- **Themes:** Omics & single-cell methods; Quantitative methods; Molecular & cell biology

### 2. [TAPESTRY: an interactive resource for exploring tumor-enriched splice junctions in pediatric brain tumors](https://arxiv.org/abs/2610.31816)
- **Abstract:** TAPESTRY is a searchable catalog of recurrent tumor-enriched splice junctions in pediatric brain tumors, paired with normal-brain references and annotations for prioritizing candidate targets.
- **Authors:** Patricia J. Sullivan, Ryan J. Corbett, Chao Di, Alex Sickler, Aylar Babaei, Meghali Goswami, Jo Lynne Rokita
- **arXiv:** `2610.31816v1` (published 2026-10-22T18:53:50Z; categories: `q-bio.GN`)
- **Evidence for ranking:** The resource catalogs 45,430 junctions across 19 histologies from 1,962 RNA-seq specimens, including 1,272 independent primary tumors; Semantic Scholar reported 0 citations at the snapshot.
- **Claimed contribution:** The authors provide an interactive database, downloadable tables, and a REST API for searching recurrent and oncofetal splice events alongside expression and protein-domain context.
- **Caveat:** Junction calls do not establish that a stable protein isoform or HLA-presented peptide is produced. The authors note small pediatric normal-reference cohorts and heuristic enrichment thresholds; experimental validation is needed.
- **Announcement type:** new submission, 2026-10-26 announcement batch
- **Themes:** RNA & transcriptomics; DNA & genomics; Biomedical & translational medicine

### 3. [U-NeXt: General-purpose event detection for neonatal EEG](https://arxiv.org/abs/2610.32811)
- **Abstract:** U-NeXt uses semantic segmentation for neonatal EEG event detection, applying a shared architecture to seizures, low-voltage intervals, and artifacts.
- **Authors:** Robert Hogan, Sean R. Mathieson, Aurel Luca, Soraia Ventura, Sean Griffin, Geraldine B. Boylan, John M. O'Toole
- **arXiv:** `2610.32811v1` (published 2026-10-23T15:47:15Z; categories: `cs.LG`, `eess.SP`, `physics.med-ph`)
- **Evidence for ranking:** The paper reports over 11,000 hours and 82,000 annotated events in development data, plus two independent held-out seizure datasets totaling 130 neonates; this is a substantive external-validation signal, not evidence of popularity.
- **Claimed contribution:** The authors report U-NeXt+ Matthews correlation coefficients of 0.862 and 0.891 on the Helsinki and Cork held-out datasets, respectively, and higher sensitivity for short events than the compared task-specific baseline.
- **Caveat:** Evaluation is retrospective and only seizure detection receives held-out testing; no prospective clinical impact is shown. The authors disclose affiliations with CergenX, a neonatal neuromonitoring company.
- **Announcement type:** new submission (cross-listed), 2026-10-26 announcement batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 4. [Computational De Novo Design of Miniprotein Candidate Neutralizers Targeting the IL-23 Cytokine Subunit p19](https://arxiv.org/abs/2610.32779)
- **Abstract:** The authors computationally design short protein candidates intended to occupy the IL-23 p19 receptor-binding surface and compare interface-aware design pipelines.
- **Authors:** Raghav Paladugu, Fardina Fathmiul Alam
- **arXiv:** `2610.32779v1` (published 2026-10-23T15:26:49Z; categories: `q-bio.BM`)
- **Evidence for ranking:** The paper contrasts 972 conventional designs with 50 interface-optimized designs and reports five leads; its arXiv comment says accepted as a short paper at IEEE BIBM 2026. Semantic Scholar reported 0 citations at the snapshot.
- **Claimed contribution:** Under the authors’ computational scoring, none of the 972 conventional designs met their reliable-interface threshold, while 42 of 50 BindCraft designs exceeded the paper’s ipSAE 0.60 cutoff.
- **Caveat:** The candidates have not been experimentally expressed or tested for binding or neutralization. Predictions use a partly modeled structure, and the score bands are not calibrated specifically for de novo binders.
- **Announcement type:** new submission, 2026-10-26 announcement batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 5. [Video-rate quantitative phase and polarimetric imaging (QP2I) for label-free imaging of contracting muscle cells](https://arxiv.org/abs/2610.32756)
- **Abstract:** QP2I combines single-shot quantitative phase and polarization measurements on a standard DIC microscope to image structural and anisotropic changes in contracting muscle cells.
- **Authors:** Lucas Kreiss Roohian, Nachiket Pathak, David Ripp, Mitchell Harling, Nils Kronenberg, Marcel Schubert, Malte C. Gather
- **arXiv:** `2610.32756v1` (published 2026-10-23T15:00:24Z; categories: `physics.optics`, `q-bio.QM`)
- **Evidence for ranking:** The authors report validation on simulations, static reference targets, fixed muscle tissue, and living dynamically moving cells; one independent science-news item also covered the method (see sources).
- **Claimed contribution:** The authors report video-rate label-free phase and retardance readouts, including sarcomere length and retardance changes during cardiomyocyte contraction.
- **Caveat:** This is an imaging-method validation, not diagnostic or clinical evidence. The abstract does not specify cohort-scale replication or establish performance across instruments and laboratories.
- **Announcement type:** new submission (cross-listed), 2026-10-26 announcement batch
- **Themes:** Medical physics & imaging; Molecular & cell biology; Quantitative methods

### 6. [Kinetic Proofreading Activation Times Beyond the Weibull Limit](https://arxiv.org/abs/2610.31788)
- **Abstract:** The authors derive a first-passage description of T-cell receptor activation that retains ligand dissociation and identifies when the Weibull approximation breaks down.
- **Authors:** Thomas Mourier, Cameron Hopkinson, Kenny Wong
- **arXiv:** `2610.31788v1` (published 2026-10-22T18:29:29Z; categories: `q-bio.QM`)
- **Evidence for ranking:** The work combines an exact continuous-time Markov-chain result with stochastic simulations; its approximation matches exact medians within 2% in 19 of 25 tested parameter sets.
- **Claimed contribution:** The authors give a dimensionless diagnostic for the Weibull regime and a closed-form alternative that accounts for dissociation and repeated binding attempts.
- **Caveat:** Evidence is mathematical and simulation-based; the tested parameter grid does not establish quantitative accuracy in living immune systems.
- **Announcement type:** new submission, 2026-10-26 announcement batch
- **Themes:** Molecular & cell biology; Quantitative methods

## Trending Research Themes

This small, mixed batch does not support a field-wide shift or a single dominant molecular topic. The closest recurring thread is that validation design determines what a result can establish: the pooled-screen analysis tests whether cell halves are independent, U-NeXt tests on held-out cohorts, and TAPESTRY makes normal-reference coverage visible. These are different domains, not a unified trend.

Two papers also quantify biological dynamics at distinct scales: QP2I measures live cardiomyocyte structure and retardance over time, while the kinetic-proofreading paper models receptor activation timing. The IL-23 binder paper is a computational design study; it is a standalone signal in this batch, not evidence of a wider move toward experimentally validated de novo binders.

## Open Problems and Research Directions

- For pooled single-cell screens, repeat key comparisons across more cell types using separate transductions, explicit null controls, and clone barcodes; test how well the estimated clone effect transfers between screens. This follows the paper’s stated limitations about unlabeled clones and heterogeneous source datasets.
- For TAPESTRY candidates, add broader developmental and pediatric normal references, then test prioritized junctions at transcript, protein, and immunopeptidome levels. The catalog alone cannot establish target protein production or peptide presentation.
- For the IL-23 candidates, the authors identify recombinant expression, direct affinity measurement, receptor-competition or STAT3 assays, and assembly-level compatibility checks as next steps. These would distinguish predicted interfaces from functional neutralization.
- For U-NeXt and QP2I, independent multi-site evaluation with pre-specified comparator pipelines would test robustness beyond the reported cohorts and instruments; prospective utility would require separate study.
- For kinetic proofreading, compare the predicted dissociation-dependent timing regimes with measurements across ligands of known off-rates. This is a proposed mechanistic test, not a result of the current paper.

## Takeaway

The batch’s strongest cross-paper lesson is methodological: biological conclusions depend on valid experimental units, appropriate reference data, and independent validation. U-NeXt reports external retrospective testing, TAPESTRY offers a sizeable splice-junction resource, and the IL-23 and kinetic-proofreading papers remain computational/theoretical. None should be read as clinical guidance or as establishing efficacy in patients.

## Method and sources

- **Window:** daily; latest available announcement batch dated 2026-10-26 (Monday). The current UTC date is 2026-10-27, so this uses the prior announcement batch. The batch date range is 2026-10-26 through 2026-10-26; selected new submissions were first posted on 2026-10-22 through 2026-10-23 UTC. Snapshot: 2026-10-27T01:19:39Z.
- **Candidate collection:** traversed new-submission, cross-list, and replacement listings for `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph`; cross-listed duplicates were deduplicated by versionless arXiv ID. The `cs.BI` listing route returned an invalid-archive response, so the explicit API query was also used: `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`. Its first 200 results extended well beyond the selected announcement window. All six selected papers’ arXiv abstract pages were checked. PDF text for the three highest-ranked entries was reviewed for introduction, results, and limitations.
- **Ranking:** arXiv has no official trend chart. Semantic Scholar Graph API returned 0 citations for `2610.32962`, `2610.31816`, and `2610.32779` at the snapshot; citation evidence is sparse, and totals are not period gains. No claim of readership or downloads is made. The list is therefore titled “Notable recent papers” and ordered by direct relevance, reported validation breadth, and useful methods/resources, with acceptance or independent coverage noted only where available.
- **Coverage caveat:** arXiv is not a representative biomedical index; many experimental and clinical preprints appear on bioRxiv or medRxiv. Purely clinical papers are not practice-changing evidence.
- **Sources:** [q-bio.BM listings](https://arxiv.org/list/q-bio.BM/new), [q-bio.GN listings](https://arxiv.org/list/q-bio.GN/new), [q-bio.QM listings](https://arxiv.org/list/q-bio.QM/new), [medical physics listings](https://arxiv.org/list/physics.med-ph/new), [arXiv API](https://export.arxiv.org/api/query), [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper), and the [QP2I independent coverage](https://science-feed.com/scientists-capture-live-muscle-cell-contractions-without-using-chemical-labels/). Each paper’s canonical arXiv abstract and PDF are linked in the entry.
