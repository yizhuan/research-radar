# Biology & biomedicine — 22 November 2026 announcement: 8 notable recent papers

This batch is strongest in computational biomolecular structure and dynamics, alongside spatial gene-expression reconstruction and biomedical measurement methods. Agenda: compare the protein-modeling approaches, then review genomics, imaging, and translational assays. arXiv has no official trending chart; this is an inferred, relevance-ranked selection from an incomplete biomedical preprint corpus. The collected attention signals found no independent-attention hits (0 of 16 candidates), so these are notable recent papers, not a measured popularity ranking.

## Top papers (ranked)

### 1. [BioEmu2: Scalable Emulation of Biomolecular Dynamics](https://arxiv.org/abs/2611.27924)
- **Abstract:** BioEmu2 is a generative model for atom-resolved biomolecular structures that aims to unify structure prediction, equilibrium sampling, and time propagation across protein, nucleic-acid, ligand, and ion-containing systems.
- **Authors:** Michael Gastegger; Adam E. Foster; José Jiménez-Luna; Tim Hempel; Sarah Lewis; Yu Xie; Lixin Sun; Iryna Zaporozhets; J. Thorben Frank; Yaoyi Chen; Michael Plainer; Ludwig Winkler; Pedro B. P. S. Reis; Sven H. Giese; Roberto Sordillo; Victor García Satorras; Eray Inanc; Kacper Kapuśniak; Soojung Yang; Rishwanth Raghu; Rachel Kim; Gabriel Dernbach; Deniz Gunceler; Hannes Schulz; Bonnie Kruft; Marwin Segler; Christopher M. Bishop; Cecilia Clementi; Ryota Tomioka; Frank Noé
- **arXiv:** `2611.27924v1` (published 2026-11-20 17:58:47 UTC; categories: `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** Signal score 0.25, entirely one cross-list (`q-bio.BM`); no HF or HN attention signal. The candidate's recorded Semantic Scholar counts were 0 citations and 0 influential citations. Selected for direct biomolecular relevance, not measured popularity.
- **Claimed contribution:** The authors report competitive structure-prediction benchmarks, equilibrium samples with 0.7–1.2 kcal/mol free-energy errors against MD references, and time-propagation tests across 78 systems; the full text notes that some trajectories relax too quickly.
- **Caveat:** This is computational comparison to structures and MD, not experimental validation. The authors explicitly say slow binding, dissociation, folding, and unfolding kinetics are not established as quantitatively accurate in this release.
- **Announcement type:** new submission, 2026-11-22 batch
- **Themes:** Biochemistry & proteins; DNA & genomics; Quantitative methods

### 2. [Structural Agreement Indicates Prediction Accuracy For Protein-Ligand Co-Folding](https://arxiv.org/abs/2611.27058)
- **Abstract:** Across seven protein–ligand co-folding models, the authors evaluate ensemble structural agreement as a signal for whether predicted ligand poses are correct, and propose the CORE Score.
- **Authors:** J. Henry Broster; Bojana Popovic; Diana Kondinskaia; Charlotte M. Deane; Fergus Imrie
- **arXiv:** `2611.27058v1` (published 2026-11-20 03:27:19 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Signal score 0.25, from one cross-list (`q-bio.BM`); no HF/HN attention or candidate-level S2 citation record. Ranked for direct protein–ligand relevance.
- **Claimed contribution:** In the Runs N’ Poses benchmark of 2,600 protein–ligand systems, the authors report mean ROC AUCs of 0.866 (top-1 success) and 0.838 (oracle success) for CORE, compared with 0.757 and 0.759 for ipTM.
- **Caveat:** These are retrospective structural benchmark results, not prospective validation. The authors evaluate pose correctness, not whether a compound binds or has an effect.
- **Announcement type:** new submission, 2026-11-22 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 3. [Hierarchical Hybrid-Coordinate Flow Matching for Accurate and Physically Plausible Apo-to-Holo Protein Generation](https://arxiv.org/abs/2611.27162)
- **Abstract:** CrypticFlow combines Cartesian anchor generation with recursive internal-coordinate decoding to predict holo-like conformations from apo protein structures while controlling local geometry.
- **Authors:** Minjong Kim; Jaemin Sim; Dongwoo Kim; Myunghyun Jang; Eun-Sol Kim; Juyong Lee
- **arXiv:** `2611.27162v1` (published 2026-11-20 05:47:46 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Signal score 0.25, from one cross-list (`q-bio.BM`); no HF/HN attention signal. Selected for a concrete structural-biology method and quantitative held-out evaluation.
- **Claimed contribution:** On a fixed 150-pair D3PM split and five training runs, the authors report improved local geometry (99.58% adjacent-distance fidelity) and mean direct RMSD of 2.766 Å; their external CryptoBench evaluation reports modest improvement over the unchanged apo input.
- **Caveat:** The paper states that the accuracy lead does not hold against all capacity-matched baselines. The predictor is effectively deterministic, ligand-free, and does not represent alternative holo states.
- **Announcement type:** new submission, 2026-11-22 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 4. [GaLF-ST: Gaussian Latent Fields for Spatial Transcriptomics Reconstruction](https://arxiv.org/abs/2611.27143)
- **Abstract:** GaLF-ST jointly learns Gaussian spatial fields, latent vectors, and a decoder to reconstruct multigene expression from sparse spatial-transcriptomics observations.
- **Authors:** Baichuan Yang; Yifan Luo; Yong Liu; Bing Su
- **arXiv:** `2611.27143v1` (published 2026-11-20 05:23:08 UTC; categories: `cs.LG`, `q-bio.GN`)
- **Evidence for ranking:** Signal score 0.25, from one cross-list (`q-bio.GN`); no HF/HN attention signal. Relevance is direct to genomics and spatial transcriptomics.
- **Claimed contribution:** The authors compare against four methods on seven dataset groups and three held-out fractions, reporting leading overall reconstruction performance and reduced runtime and GPU memory use.
- **Caveat:** Evidence is benchmark-based expression reconstruction; the abstract does not establish transfer to prospective tissues or experimental confirmation of inferred expression patterns. The authors say code and appendix are planned for a later version.
- **Announcement type:** new submission, 2026-11-22 batch
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 5. [Receptor Abundance Alone Underpredicts Red Blood Cell Adhesion in Gaucher Disease](https://arxiv.org/abs/2611.27960)
- **Abstract:** A stochastic bond model and reported adhesion measurements suggest that red-cell adhesion in Gaucher disease is not explained by total Lu/BCAM receptor abundance alone, and may depend more on receptor activation state.
- **Authors:** Zhaojie Chai; Pierre A. Buffet; Melanie Franco; George Em Karniadakis
- **arXiv:** `2611.27960v1` (published 2026-11-20 18:39:09 UTC; categories: `physics.bio-ph`, `cond-mat.soft`, `physics.med-ph`, `q-bio.CB`)
- **Evidence for ranking:** Signal score 0.75, entirely three cross-lists; no independent HF/HN attention signal. It has the broadest cross-listing among the selected candidates; cross-listing is a relevance/breadth signal, not readership.
- **Claimed contribution:** The authors report that observed adhesion exceeds the model prediction based on a 1.3-fold receptor increase, and that matching it requires more binding-competent receptors; their sickle-cell analysis also models the reported hydroxyurea-associated change.
- **Caveat:** This is a model-and-assay study, not evidence of clinical outcomes or treatment benefit. The abstract gives no cohort size, and the inferred receptor activation mechanism needs direct validation.
- **Announcement type:** new submission, 2026-11-22 batch
- **Themes:** Molecular & cell biology; Biomedical & translational medicine; Quantitative methods

### 6. [Beyond Final Answers: Interpretable Tumor Immune Microenvironment Reasoning from H&E and mIF](https://arxiv.org/abs/2611.26794)
- **Abstract:** HERMES uses paired H&E and multiplex-immunofluorescence images with process-level supervision to generate auditable tumor-immune-microenvironment readouts.
- **Authors:** Yixuan Duan; Kexin Geng; Hanwen Xu; Wei Qiu
- **arXiv:** `2611.26794v1` (published 2026-11-19 20:36:13 UTC; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.25, from one cross-list; the pre-collected S2 record has 0 citations and 0 influential citations, and no HF/HN attention signal. Selected for direct biomedical measurement relevance.
- **Claimed contribution:** Across four colorectal-cancer field-level tasks, the authors report 84.5% average accuracy for HERMES (4B), versus 74.7% for the strongest of twelve compared models; they also report results on a CODEX cohort and head-and-neck cancer.
- **Caveat:** This is model evaluation, not clinical validation or evidence that the outputs improve care. The abstract does not provide cohort sizes or prospective evaluation details.
- **Announcement type:** new submission, 2026-11-22 batch
- **Themes:** Biomedical & translational medicine; Omics & single-cell methods; Quantitative methods

### 7. [One-Step Self-Assembling Lipopolymer Coatings Enable Direct Longitudinal Biosensing in Native Biological Matrices](https://arxiv.org/abs/2611.27422)
- **Abstract:** The authors describe a self-assembling antifouling coating for label-free digital biosensing in undiluted biological matrices, including time-resolved extracellular-vesicle measurements from lung-cancer cell models.
- **Authors:** Pascal Rüedi; Sarina Seiter; Stephan Handschin; Chiara Lombardo; Jaime Ortega Arroyo; Romain Quidant
- **arXiv:** `2611.27422v1` (published 2026-11-20 10:24:01 UTC; categories: `q-bio.QM`, `cond-mat.mtrl-sci`, `physics.chem-ph`)
- **Evidence for ranking:** Signal score 0.50, from two cross-lists; no HF/HN attention signal. Included for the direct biomolecular assay application.
- **Claimed contribution:** Integrated optofluidic measurements reportedly quantify tetraspanin-positive extracellular-vesicle secretion from 2D and 3D lung-cancer cell models using 50 μL in 10 minutes without isolation or purification.
- **Caveat:** Demonstrations use cell models and assay matrices, not patient cohorts or clinical diagnostic endpoints; broader performance across biological samples remains to be established.
- **Announcement type:** new submission, 2026-11-22 batch
- **Themes:** Biomedical & translational medicine; Molecular & cell biology; Quantitative methods

### 8. [MambaSplit: Severity-Robust and Inference-Efficient Semantic Unmixing of Fluorescence Microscopy Image Data](https://arxiv.org/abs/2611.26703)
- **Abstract:** MambaSplit uses a state-space image encoder and convolutional decoder to separate overlapping fluorescence structures across varied mixing ratios.
- **Authors:** Aman Kukde; Ruggiero Santeramo; Federico Carrara; Ashesh Ashesh; Igor Zubarev; Florian Jug
- **arXiv:** `2611.26703v1` (published 2026-11-19 19:02:02 UTC; categories: `eess.IV`, `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.50, from two cross-lists; the pre-collected S2 record has 0 citations and 0 influential citations, and no HF/HN attention signal. Selected for its microscopy-method relevance.
- **Claimed contribution:** Across five datasets and nine mixing ratios, the authors report the best RI-PSNR in 11 of 15 dataset-severity combinations and 5.9× faster inference than their strongest baseline.
- **Caveat:** Results are image-unmixing benchmark metrics, including computationally summed images; they do not by themselves establish improved biological interpretation or downstream experimental outcomes.
- **Announcement type:** new submission, 2026-11-22 batch
- **Themes:** Molecular & cell biology; Quantitative methods

## Trending Research Themes

- **Atomistic protein modeling is moving from single structures toward ensembles and reliability estimates.** BioEmu2 targets equilibrium and time evolution as well as structures; CORE tests whether agreement among generated protein–ligand poses can flag likely errors; CrypticFlow emphasizes local physical geometry in apo-to-holo predictions. These are complementary computational approaches, not independent experimental confirmation.
- **Spatial and microscopy methods increasingly treat reconstruction as a quantitative inference problem.** GaLF-ST reconstructs spatial gene expression; MambaSplit separates overlapping fluorescence signals; HERMES uses paired pathology modalities with cell-level process checks. Their evidence is benchmark or cohort evaluation, not clinical deployment.
- **Biological measurement platforms target richer, more dynamic readouts.** The lipopolymer biosensor reports time-resolved extracellular-vesicle sensing, while the Gaucher-disease study links receptor state, adhesion modeling, and measurements. Both remain bounded by their assay/model settings.

## Open Problems and Research Directions

- **Test predicted biomolecular dynamics against direct experimental kinetics.** BioEmu2's authors state that slow transition rates are not quantitatively established. Follow-up work could compare blinded predictions with time-resolved structural or biochemical measurements for systems with known binding, dissociation, or conformational rates.
- **Stress-test structure reliability beyond retrospective benchmarks.** CORE and CrypticFlow use benchmarked structural outcomes, and CrypticFlow reports capacity-matching and diversity limits. Prospective, held-out target sets—with ligand-conditioned multi-state outputs and consistent evaluation of geometry, pose accuracy, and uncertainty—would clarify generalization.
- **Measure transfer and calibration in biological samples.** GaLF-ST, HERMES, MambaSplit, and the biosensor report computational or model-based evaluations. External tissue cohorts, independently prepared microscopy mixtures, and blinded serum/sample panels compared with orthogonal reference assays would test whether benchmark gains hold under realistic variation.
- **Validate the receptor-state explanation independently.** The Gaucher-disease paper's model suggests activation state matters beyond receptor abundance. Direct measurements of phosphorylated/binding-competent Lu/BCAM alongside adhesion across a clearly characterized donor cohort could test that mechanism; this is a research proposal, not a clinical recommendation.

## Takeaway

This is a relevance-ranked snapshot, not a reliable popularity leaderboard: the signal collector found no independent attention among the 16 papers in the batch. The most concentrated scientific thread is computational protein modeling, with separate work on spatial transcriptomics and measurement-focused biomedical methods. The reported results are promising benchmarks and assays, but independent experimental and prospective validation remains the limiting evidence.

## Method and sources

- **Window:** daily batch for 2026-11-22; the most recent batch available on 2026-11-23, announced at 2026-11-23 01:00 UTC. It covers submissions from **2026-11-19 19:00 UTC through 2026-11-20 19:00 UTC**. Snapshot: **2026-11-23 17:08 UTC**.
- **Scope/query:** `q-bio.BM OR q-bio.GN OR q-bio.MN OR q-bio.SC OR q-bio.CB OR q-bio.TO OR q-bio.QM OR cs.BI OR physics.med-ph`, restricted to `submittedDate:[202611191900 TO 202611201900]`. The arXiv API returned 16 candidates for this window; this fully traversed result was checked against the supplied signal pool. Eight are selected here for direct relevance; ecological/population and less directly molecular candidates were not allowed to displace the biology/biomedicine focus.
- **Ranking:** the supplied deterministic signals file is primary. It reports `with_attention: 0` across 16 candidates; HF and HN sources were marked available, but no independent paper-attention signal was recorded for the selected entries. Scores shown above are the collector's weighted scores (0.25 per cross-list where no other component was present), not popularity measures. Relevant cross-list counts are given per paper. Where present in the file, Semantic Scholar citation and influential-citation totals were 0; these are not period gains. A fresh Graph API check returned HTTP 429 for the selected IDs, so no new citation totals are claimed. Ranking therefore falls back to demonstrated scope relevance. Zero attention is not evidence of unimportance.
- **Source availability:** the signal file marked arXiv, Hugging Face, Hacker News, arXiv lookup, and Semantic Scholar collection `ok`; arXiv returned 16 entries, HF 102 source items, HN 29, and S2 11. The later direct S2 corroboration request was rate-limited (HTTP 429). No source errors were reported by the pre-collected signals.
- **Primary verification:** every selected abstract page and metadata were checked at its canonical arXiv URL. The three leading papers were also read in HTML full text, including results/discussion or limitations.
- **Coverage caveat:** arXiv is not a representative biomedical index; this does not cover bioRxiv, medRxiv, or biomedical literature as a whole. These preprints are not clinical guidance.
- **Signal file:** `/home/yizhuan/.research/bio/daily/arxiv-trending-bio-daily-2026-11-22.signals.json`
- **ArXiv listing query:** `https://export.arxiv.org/api/query?search_query=%28%28cat%3Aq-bio.BM%20OR%20cat%3Aq-bio.GN%20OR%20cat%3Aq-bio.MN%20OR%20cat%3Aq-bio.SC%20OR%20cat%3Aq-bio.CB%20OR%20cat%3Aq-bio.TO%20OR%20cat%3Aq-bio.QM%20OR%20cat%3Acs.BI%20OR%20cat%3Aphysics.med-ph%29%20AND%20submittedDate%3A%5B202611191900%20TO%20202611201900%5D%29`
