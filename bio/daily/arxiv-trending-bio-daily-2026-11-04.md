# arXiv Biology & Biomedicine — latest announcement batch, 2026-11-04

## Headline
The latest available batch contains 8 biology and biomedical papers, led by computational cell-perturbation prediction, protein-backbone modeling, and experimental proton-range imaging. The agenda is to compare what is being modeled or measured, what evidence the authors actually report, and where validation remains thin. arXiv has no official trending chart: attention signals were sparse, so this is a relevance-ranked selection of notable recent papers, not a measured popularity ranking. arXiv also covers only a fraction of biomedical preprints; this is not a survey of bioRxiv, medRxiv, or the biomedical literature.

## Notable recent papers (ranked by relevance)

### 1. [CellCanon: An Agentic Cellular World Model for Prediction, Explanation, and Observation-Driven Updating](https://arxiv.org/abs/2611.05890)
- **Abstract:** CellCanon combines single-cell expression prediction, source-grounded explanations, and observation-driven updating; on 339 held-out SciPlex3 drug–cell conditions across three cell lines, the authors report improved differential-expression metrics over their best baselines.
- **Authors:** Zhaokang Liang, Shuyang Zhuang, Xiaoran Jiao, Hao Chen
- **arXiv:** `2611.05890v1` (published 2026-11-04T03:29:21Z; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** Direct single-cell perturbation relevance; the abstract reports 339 held-out conditions in three cell lines and benchmark comparisons. No independent attention or citation signal was corroborated at the snapshot, so rank reflects relevance, not popularity.
- **Claimed contribution:** The authors report DE AUPRC and Macro-F1 gains of 63.3% and 17.3% over the best baseline, respectively, plus updating from simulated feedback using measurements withheld from the same dataset.
- **Caveat:** Evaluation is on SciPlex3 and simulated measurement feedback, not prospective experiments or an external perturbation cohort; benchmark gains do not establish biological or clinical validity.
- **Announcement type:** new submission, 2026-11-04
- **Themes:** Omics & single-cell methods; Quantitative methods

### 2. [Discrete Backbone Elasticity and Curvature-Dependent Torsion Statistics in Proteins](https://arxiv.org/abs/2611.06363)
- **Abstract:** The paper derives a local elastic statistical model linking neighboring protein-backbone bends to torsion distributions and tests it against protein structures and molecular-dynamics trajectories.
- **Authors:** Yiquan Wang, Mingyu Bian, Jiayuan Ma
- **arXiv:** `2611.06363v1` (published 2026-11-04T11:25:47Z; categories: `q-bio.BM`, `cond-mat.soft`, `math-ph`, `physics.bio-ph`, `physics.chem-ph`)
- **Evidence for ranking:** Strong direct protein-biophysics fit and explicit held-out evaluation: model fitting on 194 ATLAS chains, testing on 1,744 sequence-nonredundant proteins, and transfer checks on 72 peptide/miniprotein trajectories. No independent attention or citation signal was corroborated at the snapshot.
- **Claimed contribution:** The authors report that the six-parameter baseline lowers negative log-density loss from 1.490 to 1.160 nats and improves torsion-sign and helix-fraction errors; a two-state extension further lowers test loss to 0.790 nats.
- **Caveat:** Results are statistical predictions against structural and simulation references, not experimental validation of folding or conformational kinetics. The discussion notes force-field and starting-state dependence and remaining errors associated with atomic context.
- **Announcement type:** new submission, 2026-11-04
- **Themes:** Biochemistry & proteins; Quantitative methods

### 3. [Experimental Assessment of Prompt Gamma Time Imaging in Complex Anatomy](https://arxiv.org/abs/2611.06683)
- **Abstract:** Prompt-Gamma Time Imaging jointly reconstructs proton velocity and gamma-emission profiles from multi-detector time-of-flight data, tested experimentally in an anthropomorphic head phantom.
- **Authors:** Pavel Kavrigin, Alicia Garnier, Adélie André, Chaima Abid, Yannick Boursier, Mathieu Dupont, Giuseppe Fanciulli, Laurent Gallin Martel, Marie-Laure Gallin Martel, Christophe Hoarau, Christian Morel, Jean-François Muraz, Maxime Pinson, Dimitrios Psarras, Nicola Toschi, Daniel Maneval, Sara Marcatili
- **arXiv:** `2611.06683v1` (published 2026-11-04T15:52:06Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Experimental proton-therapy imaging method with eight detector modules; the authors tested 100 MeV protons in two anatomical phantom configurations and report an approximately 1 mm range difference in the example. No independent attention or citation signal was corroborated at the snapshot.
- **Claimed contribution:** The authors report recovering material sequence and proton range from the phantom measurements, extending prompt-gamma timing beyond indirect range verification.
- **Caveat:** This is a phantom demonstration in two configurations, not patient testing. The paper notes limited sensitivity for materials with similar densities and material misclassification in some bins.
- **Announcement type:** new submission, 2026-11-04
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 4. [Modeling Gene Expression Noise: From Transcriptional Dynamics to Cell Growth and Division](https://arxiv.org/abs/2611.06537)
- **Abstract:** This review synthesizes stochastic gene-expression models that account for cell growth, DNA replication, cell-cycle variation, and division, including how these processes affect single-cell measurements and parameter inference.
- **Authors:** Augustinas Sukys, Lucy Ham, Kaan Öcal, James Holehouse, Ramon Grima
- **arXiv:** `2611.06537v1` (published 2026-11-04T14:07:17Z; categories: `q-bio.MN`)
- **Evidence for ranking:** Direct relevance to transcriptional dynamics and single-cell measurement; the review covers modeling assumptions, inference strategies, and explicit open questions. No independent attention or citation signal was corroborated at the snapshot.
- **Claimed contribution:** The authors argue that static-cell telegraph/bursty models can misattribute noise when growth and division matter, and outline cell-cycle-resolved measurements and models needed for better inference.
- **Caveat:** This is a review, not a new experimental dataset or systematic evidence appraisal; its conclusions depend on the underlying studies and their measurement designs.
- **Announcement type:** new submission, 2026-11-04
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Quantitative methods

### 5. [System-Theoretic Analysis of Extended Cellular Potts Models for Tumor Invasion](https://arxiv.org/abs/2611.06690)
- **Abstract:** The authors formulate an extended Cellular Potts model coupling interacting tumor cells to extracellular-matrix degradation and derive convergence and invasion-time results.
- **Authors:** Andrea Tramaloni, Simone Baroncini, Sofia Avnet, Nicola Baldini, Giuseppe Notarstefano
- **arXiv:** `2611.06690v1` (published 2026-11-04T15:55:57Z; categories: `eess.SY`, `q-bio.CB`)
- **Evidence for ranking:** Direct tumor-invasion and cell-microenvironment relevance; the paper supplies a formal stochastic/dynamical analysis and numerical simulation checks. No independent attention or citation signal was corroborated at the snapshot.
- **Claimed contribution:** The authors derive asymptotic ECM behavior, transition-probability bounds, convergence results, and closed-form invasion-time probabilities in one-dimensional settings.
- **Caveat:** Evidence is mathematical analysis and simulation of a model, not validation against tumor experiments or patient data; the closed-form invasion results are restricted to one dimension.
- **Announcement type:** new submission, 2026-11-04
- **Themes:** Molecular & cell biology; Biomedical & translational medicine; Quantitative methods

### 6. [Ventilation Perfusion Functional Difference Images in Lung SPECT: a linear and symmetrical scale as an alternative to the Ventilation Perfusion Ratio](https://arxiv.org/abs/2611.06390)
- **Abstract:** The paper evaluates a bounded, symmetric ventilation–perfusion difference scale as an alternative to ratio images for displaying mismatches in lung SPECT.
- **Authors:** Robin de Nijs, Ronan M. G. Berg, Sofie Lindskov Hansen, Jann Mortensen
- **arXiv:** `2611.06390v1` (published 2026-11-04T11:55:50Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Direct clinical-imaging relevance; the abstract reports investigation in ten patients and includes an existing journal reference (Physica Medica 119, 2024, DOI: 10.1016/j.ejmp.2024.103306). The arXiv record is a new submission, but the work is not newly published research.
- **Claimed contribution:** The authors propose that a relative VQ-difference scale is symmetric and bounded from −1 to +1, and report deriving image thresholds from their patient examples.
- **Caveat:** The cohort is ten patients and results are shown for three; diagnostic benefit is proposed rather than established by an external or outcome-based validation study.
- **Announcement type:** new submission, 2026-11-04
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 7. [Can a self-sustaining chemical network emerge due to just a few catalysts?](https://arxiv.org/abs/2611.06033)
- **Abstract:** A stochastic mathematical model examines when heterogeneous catalytic activity and reaction compatibility permit reflexively autocatalytic, food-generated chemical networks to form.
- **Authors:** Jinsu Kim, Ercan Sönmez
- **arXiv:** `2611.06033v1` (published 2026-11-04T06:38:47Z; categories: `q-bio.MN`, `math.PR`)
- **Evidence for ranking:** Direct relevance to catalytic networks and chemical origins-of-life theory; the paper derives formation/nonformation criteria and identifies a heavy-tailed-weight phase transition. No independent attention or citation signal was corroborated at the snapshot.
- **Claimed contribution:** The authors show mathematically that reaction-dependent catalysis can alter classical RAF phase-transition criteria and that heavy-tailed catalytic weights may permit RAF formation even as catalytic intensity tends to zero.
- **Caveat:** This is a theoretical random-network result; it does not demonstrate that such a network forms in a laboratory or occurs in a prebiotic environment.
- **Announcement type:** new submission, 2026-11-04
- **Themes:** Molecular & cell biology; Quantitative methods; Chemical reaction networks

### 8. [Estimation of Very High Energy Electron (VHEE) beam parameters using an in-air screen](https://arxiv.org/abs/2611.05973)
- **Abstract:** The authors develop a scattering-corrected method for estimating very-high-energy electron beam parameters from quadrupole scans and in-air screen measurements, motivated by radiotherapy.
- **Authors:** Joel Valerian, Paul Giansiracusa, Vincent Lu, Paarangat Pushkarna, Roger Rassool, Suzie Lyn Sheehy, Yaw-Ren Eugene Tan, Matteo Volpi
- **arXiv:** `2611.05973v1` (published 2026-11-04T05:07:26Z; categories: `physics.med-ph`, `physics.acc-ph`)
- **Evidence for ranking:** Direct radiotherapy-beam modeling relevance with both Monte Carlo validation and measurements at the PEER end station; the abstract reports parameter errors and experimental emittance ranges. No independent attention or citation signal was corroborated at the snapshot.
- **Claimed contribution:** The authors report a multiple-scattering correction that recovers simulated beam parameters and yields experimental estimates within expected ranges after fitting correction factors.
- **Caveat:** The study concerns accelerator beam characterization, not patient treatment or clinical outcomes; the authors call for more work to improve consistency and reliability of experimental estimates.
- **Announcement type:** new submission, 2026-11-04
- **Themes:** Medical physics & imaging; Biomedical & translational medicine; Quantitative methods

## Trending Research Themes

- Computational representations of biological state: CellCanon combines learned expression-response prediction with evidence-linked explanations and simulated updates; the protein-backbone paper derives a compact local statistical potential. These are distinct computational approaches, not independent biological validations.
- Linking molecular measurements to cell history: the gene-expression review emphasizes how replication, cell-cycle phase, growth, and division complicate inference from static single-cell snapshots. CellCanon addresses perturbation responses in held-out conditions, but on a different task and dataset.
- Modeling tumor and reaction-system dynamics: the Cellular Potts analysis and the RAF network paper both formalize emergence or progression in mathematical models. Neither reports direct experimental confirmation.
- Imaging and therapy instrumentation: PGTI demonstrates multi-detector phantom measurements; the VQ-difference paper studies SPECT presentation in a small patient cohort; the VHEE paper concerns beam-parameter estimation. These are related by medical-physics application, not by a shared validation level.

## Open Problems and Research Directions

- CellCanon: test prospective drug–cell conditions and independent perturbation-screen datasets, with preregistered splits across compounds, cell types, and assays; compare predicted expression changes with newly measured responses rather than simulated reveal schedules alone.
- Protein-backbone model: evaluate fixed parameters on independent experimental conformational ensembles, and test whether adding sequence, neighboring-chain, or atomic-context information addresses the residual torsion errors and force-field sensitivity reported by the authors.
- PGTI and VQ-difference imaging: assess repeatability across more heterogeneous phantoms and detector geometries, then validate locked reconstruction/threshold settings in larger external cohorts; distinguish technical reconstruction accuracy from diagnostic or treatment benefit.
- Cell-cycle noise models: collect matched cell-age/size, nascent and mature RNA, and protein measurements in lineage-resolved experiments, which the review identifies as important for separating biological mechanisms from measurement noise.

## Takeaway
This batch mixes computational models, a review, a phantom imaging experiment, and small-cohort imaging work. The most concrete signals are benchmarked single-cell prediction, quantitative protein-model evaluation, and a multi-detector phantom demonstration; none should be mistaken for a clinical validation or evidence of field-wide popularity. The ranking is by relevance because independent attention evidence is sparse.

## Method and sources

- Window: daily, 2026-11-04 through 2026-11-04 UTC. The current UTC date was 2026-11-05; the latest available arXiv announcement batch in the category query was 2026-11-04, so this report uses the prior batch.
- Snapshot: 2026-11-05 17:11:39 UTC.
- Candidate query: `https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200`. The query returned 200 recent records, including all 8 entries with a 2026-11-04 first-submission date; each retained abstract page was checked.
- Ranking: no arXiv popularity statistic exists. Recent-entry citation and independent-attention evidence was not sufficient to support a popularity ranking, so papers are ordered by direct biology/biomedicine relevance and reported evidence. No downloads or view counts are claimed.
- Claims, categories, dates, versions, authors, abstracts, and journal metadata were checked against the linked arXiv abstract pages. The VQ-difference record reports DOI `10.1016/j.ejmp.2024.103306`. Search links: [CellCanon](https://arxiv.org/abs/2611.05890), [protein-backbone model](https://arxiv.org/abs/2611.06363), [PGTI](https://arxiv.org/abs/2611.06683), [gene-expression review](https://arxiv.org/abs/2611.06537), [tumor-invasion model](https://arxiv.org/abs/2611.06690), [VQ-difference SPECT](https://arxiv.org/abs/2611.06390), [RAF network model](https://arxiv.org/abs/2611.06033), [VHEE beam model](https://arxiv.org/abs/2611.05973).
- This is a point-in-time selection from specified arXiv categories, not systematic coverage of biomedical research; many clinical and experimental preprints appear elsewhere, including bioRxiv and medRxiv.
