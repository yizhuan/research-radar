# arXiv Biology & Biomedicine — Daily Brief (27 October 2026)

Today's 27 October arXiv announcement batch yields seven notable biology/biomedicine papers in this focused selection. The strongest concentration is in computational molecular methods—protein binder design, CRISPR-screen interpretation, miRNA benchmarking, and RNA simulation data—with one externally validated medical-imaging model and one theory paper. This is a relevance-ranked selection, not a measured popularity chart: arXiv has no official trending chart, citation/attention evidence is sparse, and its biomedical coverage is incomplete relative to bioRxiv, medRxiv, and the broader medical literature. Spoken agenda: what is experimentally checked, what remains computational, and where validation is still needed.

## Notable recent papers

Ranked by demonstrated relevance to molecular biology and biomedicine, then by the kind and breadth of reported evidence—not by presumed readership. All seven are v1 submissions listed in the 27 October batch; original submission timestamps are preserved below.

### 1. [Agent-guided epitope excision enables economical de novo binder design](https://arxiv.org/abs/2610.33195)
- **Abstract:** The authors crop protein targets to local binding-site windows and combine this with an agent-guided design loop, reporting faster structure-design computation and yeast-display-enriched binders, including four tested clones with nanomolar apparent affinity.
- **Authors:** Jun W. Kim, Artiom Myaskovsky, Oscar Donosa, Lawrence Chan, Jamie Rogers, Avinatan Hassidim, Yossi Matias, Annalisa Pawlosky
- **arXiv:** `2610.33195v1` (published 2026-10-23 18:42:14 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Direct protein-design relevance; 15-target/3,666-design benchmark and wet-lab yeast-display follow-up on FAP. Semantic Scholar snapshot: 0 citations and 0 influential citations, so no citation-momentum claim.
- **Claimed contribution:** The preprint reports a median interface Cα RMSD of 0.37 Å for cropped versus full targets and about 88% lower RFdiffusion/AlphaFold3 GPU time for one FAP epitope. At a fixed budget, the human-in-the-loop arm's computational hit rate was 9.33% versus 5.06% for the PI-alone arm; yeast display recovered enriched designs, and four representative clones showed apparent K_D values of 3.0–9.1 nM.
- **Caveat:** Wet-lab evidence is yeast display, not in-vivo efficacy or therapeutic validation. The autonomy comparison used one large target (FAP), one backbone class, and one LLM controller; the authors identify soluble-binder characterization, FAP specificity, and inhibition assays as future work.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 2. [Escaping cells dilute CRISPR screen responses unequally across cell types](https://arxiv.org/abs/2610.35508)
- **Abstract:** Reanalysis of published single-cell CRISPR screens estimates the fraction of measured cells that escaped effective knockdown and argues that this cell-type-dependent fraction can dilute perturbation responses and distort cross-cell comparisons and benchmarks.
- **Authors:** Xuanrui Huang
- **arXiv:** `2610.35508v1` (published 2026-10-26 14:33:48 UTC; categories: `q-bio.QM`)
- **Evidence for ranking:** A methodological result spanning published screens in 13 cell types/states, with per-perturbation estimates possible in seven datasets and checks against simulated mixtures and independent-replicate dilution. Semantic Scholar snapshot: 0 citations and 0 influential citations.
- **Claimed contribution:** The author defines an escape fraction estimated from each cell's target-gene counts. In the reported analyses, it rose with gene essentiality and reached roughly one half in human embryonic stem cells for some essential perturbations; the estimated fraction tracked response dilution and affected a simple cross-cell transfer model and benchmark scoring.
- **Caveat:** This is a reanalysis, not a new controlled CRISPR experiment. The inferred escape fraction is validated against simulations and measured dilution, not an independent per-cell protein-level measurement; datasets differ by study and protocol, and the paper notes limits to generalization beyond the cultured perturbation screens examined.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Molecular & cell biology; Omics & single-cell methods; Quantitative methods

### 3. [Benchmarking miRNA Target Prediction Methods](https://arxiv.org/abs/2610.33960)
- **Abstract:** Seven miRNA–mRNA prediction tools are compared over about 59.7 million candidate pairs using an evidence-graded reference combining two validated-interaction databases with paired RNA-seq evidence from an iPSC cohort.
- **Authors:** Congliang Jin, Weibo Niu, Zhexing Wen, Zhaohui S Qin, Ximing Ran
- **arXiv:** `2610.33960v1` (published 2026-10-25 00:23:22 UTC; categories: `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Cross-listed in genomics and quantitative biology; accepted for presentation at IEEE BIBM 2026 per the arXiv comment. The comparison covers seven tools and 59,734,204 candidate pairs. Semantic Scholar snapshot: 0 citations and 0 influential citations.
- **Claimed contribution:** The authors report that TargetScan and miRDB maintained Type I error below 0.05 across their settings but had limited power; mirDIP had the highest power but more false positives. No tool led on every metric, so they recommend selecting tools and cutoffs according to the intended sensitivity/specificity trade-off.
- **Caveat:** The expression component comes from one iPSC cohort—five 22q11.2 deletion syndrome donor lines and five controls—and the reference combines incomplete databases with expression-derived evidence rather than a gold-standard assay for all pairs. Transfer to other tissues or disease contexts remains untested.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Quantitative methods

### 4. [mdRNAcat: A Molecular Dynamics RNA Catalog of REST2 Conformational Ensembles](https://arxiv.org/abs/2610.35204)
- **Abstract:** The paper releases a curated all-atom molecular-dynamics dataset for 48 RNA systems, with coordinates, forces, structural annotations, and replica-exchange metadata intended for training and evaluating data-driven RNA models.
- **Authors:** Anton E. Dorn, Emile de Bruyn, Fabrice von der Lehr, Philipp Knechtges, Stefan Kesselheim, Alexander Schug
- **arXiv:** `2610.35204v1` (published 2026-10-26 10:56:24 UTC; categories: `q-bio.BM`, `cs.LG`, `physics.bio-ph`)
- **Evidence for ranking:** Cross-listed across biomolecules, machine learning, and biological physics; dataset scale and downloadable HDF5-format trajectories make this a reusable molecular-method resource. Semantic Scholar snapshot: 0 citations and 0 influential citations.
- **Claimed contribution:** The authors report REST2 simulations with 32 Hamiltonian states and 200–300 ns production per state, plus force labels evaluated at the sampled and unscaled reference Hamiltonians. They characterize sampling, exchange, base pairing, and sugar-pucker distributions.
- **Caveat:** These are simulation ensembles, not experimental observations of RNA conformational populations. Coverage is 48 selected systems, and force-field/sampling choices bound what downstream models can learn; experimental cross-validation is needed before treating the ensembles as a complete physical reference.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** RNA & transcriptomics; Biochemistry & proteins; Bioinformatics & sequence analysis

### 5. [MechGate: combining mechanism-derived measures of permeation and efflux to screen small molecule drugs targeting Escherichia coli](https://arxiv.org/abs/2610.33809)
- **Abstract:** MechGate combines separate computational measures of porin and membrane permeation, efflux, and antibacterial activity to diagnose which modeled barrier may impede candidate small molecules against E. coli.
- **Authors:** Lang Qin, Jagath C Rajapakse
- **arXiv:** `2610.33809v1` (published 2026-10-24 17:14:30 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Mechanism-focused antibiotic screening with an external set of marketed antibacterials; the authors report precision of 0.789–0.873 for component measures and 0.92 for their combined rule, versus baselines near 0.44. Semantic Scholar snapshot: 0 citations and 0 influential citations.
- **Claimed contribution:** The preprint presents five readouts from SMILES input and argues that separate measures make predicted failures more interpretable than a single aggregate score.
- **Caveat:** This is computational screening, not an antibacterial efficacy experiment. The authors report that public source libraries are separable by physicochemical properties and therefore construct comparisons within each library; external validation on experimentally measured, prospectively selected compounds is still needed.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Quantitative methods

### 6. [Regional prediction of hematoma expansion from non-contrast computed tomography in spontaneous intracerebral hemorrhage patients](https://arxiv.org/abs/2610.34645)
- **Abstract:** A regional transport-based morphometry model is derived on one intracerebral-hemorrhage cohort and tested on a separate archive to predict hematoma expansion from admission CT scans.
- **Authors:** Natasha Ironside, Hongyu Kan, Kristofor Pas, Mohammad Shifat-E-Rabbi, Benjamin Newman, Shinjini Kundu, Kareem El Naamani, Tanvir Rizvi, Andrea Becerril-Gaitan, Harrison Snyder, Aarathi Manchikalapudi, Sarah Ratcliffe, Stacie L. Demel, Carl D. Langefeld, Daniel Woo, Stephan Mayer, E. Sander Connolly, Gustavo Rohde, for the ERICH Investigators, the VISTA-ICH collaboration
- **arXiv:** `2610.34645v1` (published 2026-10-26 00:11:24 UTC; categories: `cs.CV`, `q-bio.TO`)
- **Evidence for ranking:** Direct biomedical imaging question and an explicit derivation/validation split: 574 ERICH patients and 196 VISTA-ICH patients. The combined regional model's reported validation AUROC was 0.787. No Semantic Scholar Graph match was returned at snapshot time.
- **Claimed contribution:** The authors report that regional transport-based features captured size, heterogeneity, eccentricity, and peripheral density patterns, and outperformed the comparator methods they evaluated in the validation dataset.
- **Caveat:** This is retrospective model validation, not evidence of improved clinical decisions or patient outcomes. The abstract calls the evidence preliminary; independent prospective validation, calibration, and assessment across acquisition sites would be needed before clinical-use claims.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 7. [Tau creates spatially moving hotspots of amyloid-β secondary nucleation: a reaction-diffusion model](https://arxiv.org/abs/2610.33981)
- **Abstract:** A reaction-diffusion model predicts that tau-driven amyloid-β nucleation can create a moving spatial maximum in secondary-nucleation activity as fibril growth depletes free monomer near the source.
- **Authors:** Andrey V. Kuznetsov
- **arXiv:** `2610.33981v1` (published 2026-10-25 01:39:16 UTC; categories: `q-bio.SC`)
- **Evidence for ranking:** A molecular mechanism question in subcellular-processes research, with explicit transport/turnover parameters and testable spatial predictions. No Semantic Scholar Graph match was returned at snapshot time; the ranking here reflects topic relevance, not measured attention.
- **Claimed contribution:** The author derives a condition for an interior nucleation-rate maximum and uses simulations to show a possible separation between tau burden, fibril-mass growth, and instantaneous amyloid-β secondary-nucleation activity.
- **Caveat:** This is a theoretical model, not an experiment or clinical finding. The predicted spatial pattern depends on assumptions about oligomer transport, exchange, and site density; it should be treated as a hypothesis for spatially resolved biochemical testing.
- **Announcement type:** new submission, 27 October 2026 batch
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

## Trending Research Themes

Within this seven-paper selection, three recurring threads stand out; they are themes in this small corpus, not proof of a field-wide shift.

- **Benchmark reliability and measurement bias:** The CRISPR-screen paper identifies guide-escape and depletion as sources of attenuated perturbation effects; the miRNA benchmark makes tool rankings depend on evidence thresholds and a cohort-derived reference; MechGate reports source-library separability that can confound apparent performance. Together they emphasize checking what labels and benchmark splits actually measure.
- **Scaling computational biology without mistaking speed for validation:** The binder-design paper reduces compute cost and adds yeast-display experiments, while mdRNAcat contributes reusable RNA simulation data. Both make computational workflows more scalable, but the evidence boundary differs: one has limited experimental binder readouts; the other is a simulation resource.
- **A range of translational evidence levels:** The hematoma model includes a retrospective external cohort; the binder study includes yeast-display enrichment and a small clone-binding assay; MechGate and the tau study remain computational. These are distinct forms of evidence and should not be pooled as equivalent demonstrations of clinical or biological efficacy.

## Open Problems and Research Directions

The papers support several concrete follow-ups. The binder-design authors identify soluble-expression binding characterization, FAP-domain specificity, and catalytic inhibition as next steps; expanding the comparison to more target classes and scaffold families would test whether the compute and agent-autonomy results generalize. For CRISPR screens, an intervention that prevents depletion of successfully perturbed cells, paired with direct per-cell protein/knockdown measurements and matched harvest times, could distinguish true cell-type response differences from survivor and guide-escape effects. The miRNA benchmark would benefit from independent, tissue-diverse cohorts and held-out biochemical interaction assays, while preserving strict separation between tool-development data and evaluation labels. For MechGate, prospective testing on compounds chosen before assay results—with permeability, efflux, and growth measurements separated—could reveal whether the mechanism-level scores transfer beyond the reported libraries. mdRNAcat could be compared against orthogonal experimental ensemble measurements across its RNA targets. The hematoma model needs prospective, multi-site validation with calibration and decision-impact analyses. Finally, spatially resolved experiments that vary tau and amyloid-β gradients could test whether the modeled nucleation maximum moves independently of local tau or fibril mass. These are research proposals grounded in the reported limitations, not clinical recommendations.

## Takeaway

The most evidence-rich work today pairs computational efficiency or large-scale analysis with a defined validation boundary: the binder study has early in-vitro follow-up, the CRISPR and miRNA papers expose benchmark assumptions, and the imaging model has a separate retrospective cohort. The RNA dataset and tau model are useful resources or hypotheses, not experimental confirmation. No paper can be called popular from the available attention signals.

## Method and sources

- **Window:** daily; announcement batch 27 October 2026. Start/end dates for the batch: 2026-10-27 to 2026-10-27. Snapshot: 2026-10-27 17:22 UTC. The current day's category listing contains a batch, so this is not a prior-batch substitute. The selected v1 records' first-submission timestamps range from 2026-10-23 to 2026-10-26 UTC; those timestamps are kept distinct from the batch date.
- **Candidate scope:** official recent listings for `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, and `physics.med-ph`; cross-listed duplicates were deduplicated by versionless arXiv ID. A date-bounded API query for `cs.BI` returned no records in this date window. Selected abstract pages were verified against arXiv; the top three papers were also read beyond the abstracts (introduction, results, discussion/limitations) from their PDFs.
- **Category query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, submitted-date descending. Daily batch membership was checked against category listings; selection was filtered for biology/biomedicine relevance.
- **Ranking:** arXiv publishes no official trending or readership ranking. Semantic Scholar Graph was queried for `arXiv:<id>` using citation and influential-citation totals: the five matched selected records each returned 0 citations and 0 influential citations; two had no Graph match. These are current totals, not gains during the reporting window. No reliable independent attention signal was strong enough to support a popularity ranking, so entries are ordered by demonstrated biological/medical relevance and evidence type. A conference-acceptance comment is noted only where arXiv reports it.
- **Coverage caveat:** arXiv is not representative of biomedical preprints; many clinical and experimental biology papers instead appear on bioRxiv or medRxiv. This report is not a systematic review or clinical evidence assessment.
- **Primary sources:** [q-bio.BM recent](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN recent](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN recent](https://arxiv.org/list/q-bio.MN/recent), [q-bio.SC recent](https://arxiv.org/list/q-bio.SC/recent), [q-bio.CB recent](https://arxiv.org/list/q-bio.CB/recent), [q-bio.TO recent](https://arxiv.org/list/q-bio.TO/recent), [q-bio.QM recent](https://arxiv.org/list/q-bio.QM/recent), [physics.med-ph recent](https://arxiv.org/list/physics.med-ph/recent), and each linked arXiv abstract page above. Corroboration: Semantic Scholar Graph API (`ARXIV:<id>`; current citation totals) and arXiv comments for the BIBM acceptance statements.
