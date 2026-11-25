# arXiv Biology and Biomedicine — 2026-11-25 announcement batch

Nine notable recent papers in the 2026-11-25 arXiv biology/biomedicine announcement batch span multimodal cancer pathology, protein-generation benchmarks, multi-omics prediction, and quantitative biomedical models. With no collected HF/HN attention and Semantic Scholar unavailable, the list is ranked by demonstrated fit to biology and biomedicine—not measured popularity. The agenda: tissue proteomics and reproducibility; protein structure/generation; and validation limits in computational and translational studies. arXiv has no official trending chart, and its biomedical coverage is incomplete; this is an inferred relevance ranking from a limited arXiv corpus, not a popularity chart or a comprehensive biomedical survey. Many clinical and experimental preprints appear on bioRxiv or medRxiv.

## Top papers (ranked)

### 1. [A multimodal foundation model for tissue proteomics and morphology in cancer](https://arxiv.org/abs/2611.31451)
- **Abstract:** VirTues-M2 jointly models H&E histology and spatial proteomics and reports cross-task evaluations plus survival-signature stratification in a 1,053-patient treatment-naive NSCLC cohort and an independent validation cohort.
- **Authors:** Benedikt von Querfurth; Lukas Klein; Cédric Vincent-Cuaz; Eeshaan Jain; Yexiang Cheng; Johann Wenckstern; Phil F. Cheng; Petros Liakopoulos; Olivier Michielin; Martina Haberecker; Andreas Wicki; Pascal Frossard; Charlotte Bunne
- **arXiv:** `2611.31451v1` (published 2026-11-23 19:25:07 UTC; categories: `q-bio.QM`, `cs.CV`)
- **Evidence for ranking:** Signal score 0.25, entirely one cross-list (0.25); no candidate HF upvotes or HN points/comments were recorded. Ranked first for direct fit to cancer tissue proteomics and multimodal biomedical research, not for measured popularity.
- **Claimed contribution:** The authors present a marker-aware multimodal tissue foundation model that supports H&E-only, proteomics-only, and joint inference; in the preprint, multimodal signatures stratified survival in the discovery data and transferred to an external cohort.
- **Caveat:** The authors say the independent survival validation cohort was small (39 patients) and call for larger external and prospective multi-site validation; the reported survival associations are not clinical-utility evidence.
- **Announcement type:** new submission, 2026-11-25 batch
- **Themes:** Biomedical & translational medicine; Omics & single-cell methods; Molecular & cell biology

### 2. [Tempering and few-shot calibration of pathology foundation models improve digital biomarker reproducibility across slide scanners](https://arxiv.org/abs/2611.31536)
- **Abstract:** The authors fine-tune a pathology foundation model to reduce scanner-dependent shifts across HPV, colorectal MSI, prostate grading, and breast-expression signatures, reporting lower prediction discrepancies and improved cross-scanner agreement.
- **Authors:** Frank T Wen; Kyler Rosen; Siddhi Ramesh; Michael Koo; Sara Kochanny; Sasha Jain-Liu; Emma Dyer; Alexander T Pearson; James M Dolezal
- **arXiv:** `2611.31536v1` (published 2026-11-23 20:44:41 UTC; categories: `q-bio.QM`, `cs.AI`, `cs.CV`)
- **Evidence for ranking:** Signal score 0.50, entirely two cross-lists (0.50); no candidate HF upvotes or HN points/comments were recorded. Ranked highly for direct biomedical pathology relevance and reproducibility focus, not for measured popularity.
- **Claimed contribution:** The preprint reports that tempering H-optimus-0 features reduced cross-scanner variation across four retrospective pathology applications, including prostate grade agreement rising from 42.5% to 92.7%.
- **Caveat:** All evaluations were retrospective; the study tempers one foundation model and the authors note uncertainty on scanners outside those represented in training, so prospective multi-site generalization remains unestablished.
- **Announcement type:** new submission, 2026-11-25 batch
- **Themes:** Biomedical & translational medicine; Medical physics & imaging; Quantitative methods

### 3. [Benchmarking Protein Structure Tokenizers as Generation Targets for Language Models](https://arxiv.org/abs/2611.32168)
- **Abstract:** In a controlled benchmark, the authors swap eight protein-structure tokenizers in the same 9B language model across four compute budgets and three held-out sets, finding substantial differences in generated-structure quality.
- **Authors:** Yong Liu; Zhanpeng Shi; Peicong Lin; Zhenyi Zhong; Yizhou Dang; Wendi Wu; Haoling Li; Jiayu Gu; Duo An; Shuangjia Zheng
- **arXiv:** `2611.32168v1` (published 2026-11-24 08:19:49 UTC; categories: `q-bio.QM`, `cs.AI`)
- **Evidence for ranking:** Signal score 0.25, entirely one cross-list (0.25); no candidate HF upvotes or HN points/comments were recorded. Ranked for direct protein-structure and generation-method relevance, not for measured popularity.
- **Claimed contribution:** The preprint introduces “writability” as a generation-oriented criterion and reports that local structure preservation in token spaces best tracks the observed differences; the authors explicitly describe this as a supported correlate, not established causality.
- **Caveat:** This is a computational benchmark under one base model, training recipe, and greedy decoding regime; it does not test generated proteins experimentally, and the authors caution against generalizing beyond that configuration.
- **Announcement type:** new submission, 2026-11-25 batch
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 4. [Cancer multi-omics joint dimension reduction leads to reliable and interpretable survival predictions](https://arxiv.org/abs/2611.32382)
- **Abstract:** The authors benchmark 12 joint-dimension-reduction methods on 18 TCGA cancer datasets for survival prediction, reporting that performance varies substantially by cancer and that some methods improve on models using clinical data alone.
- **Authors:** Vincent Le Goff; Vincent Guillemot; Cathy Philippe; Wiam Ahdidou; Gwendoline Mendes; Jean-François Deleuze; Edith Le Floch; Arnaud Gloaguen
- **arXiv:** `2611.32382v1` (published 2026-11-24 10:48:03 UTC; categories: `q-bio.GN`)
- **Evidence for ranking:** Signal score 0.00 and zero cross-lists; the collector found no external attention signal for this candidate. Zero is not evidence of low importance. Ranked for direct genomics, multi-omics, and cancer-prognosis relevance.
- **Claimed contribution:** The preprint identifies JIVE and RGCCA among the stronger approaches and reports bootstrap analyses of prognostic-marker reliability, with a low-grade-glioma interpretation.
- **Caveat:** The reported results are retrospective TCGA analyses with marked between-cancer variability; predictive performance and marker stability do not establish prospective clinical utility or treatment benefit.
- **Announcement type:** new submission, 2026-11-25 batch
- **Themes:** Omics & single-cell methods; Biomedical & translational medicine; Quantitative methods

### 5. [Beyond Hard Tokens: Predictive Memory for Multimodal Protein Generation](https://arxiv.org/abs/2611.32347)
- **Abstract:** Predictive Memory carries soft sequence and structure-token predictions between decoding steps; the authors report improved unconditional co-generation success for DPLM-2, DPLM-2.1, and ESM3 in computational evaluations.
- **Authors:** Xiaoliang Shi; Zichen Wang; Zhijian Wei; Zhanpeng Shi; Zhenghong Zhou; Yunpeng Wang; Shuangjia Zheng
- **arXiv:** `2611.32347v1` (published 2026-11-24 10:25:16 UTC; categories: `cs.LG`, `q-bio.BM`)
- **Evidence for ranking:** Signal score 0.25, entirely one cross-list (0.25); no candidate HF upvotes or HN points/comments were recorded. Ranked for direct multimodal protein-generation relevance, not for measured popularity.
- **Claimed contribution:** The preprint proposes a training-free self-conditioning recurrence and reports gains of 3.6, 17.7, and 48.7 percentage points on the three evaluated models, with improved quality-diversity trade-offs and less repetitive collapse.
- **Caveat:** The evidence is model-generation benchmarking, not biochemical or cellular validation of generated proteins; the reported gains vary substantially across the tested models.
- **Announcement type:** new submission, 2026-11-25 batch
- **Themes:** Biochemistry & proteins; Quantitative methods

### 6. [A Description-Derived Drug-Drug Interaction Benchmark Reveals Split-Dependent Molecular Representation Rankings](https://arxiv.org/abs/2611.32371)
- **Abstract:** The authors derive six drug-interaction labels from DrugBank descriptions and benchmark molecular representations under four train-test split regimes, finding that fingerprints lead on random splits while graph representations lead on drug- and scaffold-holdout splits.
- **Authors:** Manel Gil-Sorribes; Isaac Filella-Merce; Alexis Molina
- **arXiv:** `2611.32371v1` (published 2026-11-24 10:40:38 UTC; categories: `q-bio.BM`, `cs.LG`)
- **Evidence for ranking:** Signal score 0.25, entirely one cross-list (0.25); no candidate HF upvotes or HN points/comments were recorded. The arXiv comment reports two workshop acceptances, which is publication-status metadata rather than an attention metric. Ranked for molecular and biomedical-method relevance.
- **Claimed contribution:** The preprint provides a description-derived DDI benchmark and shows that representation rankings depend on chemical novelty in the test split; its arXiv comment reports acceptance at two NeurIPS 2026 workshops.
- **Caveat:** Targets are categories derived from curated text, not measured patient outcomes or prospective interaction events; benchmark performance is not clinical validation.
- **Announcement type:** new submission, 2026-11-25 batch
- **Themes:** Biochemistry & proteins; Biomedical & translational medicine; Bioinformatics & sequence analysis

### 7. [Synchronized Memory-Dependent Intracellular Oscillations for a Cell-Bulk ODE-PDE Model in $\mathbb{R}^3$](https://arxiv.org/abs/2611.32077)
- **Abstract:** A cell-bulk ODE-PDE model is reduced to a memory-kernel system for intracellular dynamics; numerical analysis of Sel’kov kinetics predicts weak, slow synchronization among separated cells in three dimensions.
- **Authors:** Merlin Pelz; Michael J. Ward
- **arXiv:** `2611.32077v1` (published 2026-11-24 07:00:43 UTC; categories: `math.AP`, `nlin.AO`, `q-bio.CB`)
- **Evidence for ranking:** Signal score 0.50, entirely two cross-lists (0.50); no candidate HF upvotes or HN points/comments were recorded. Ranked for a clear intracellular molecular-dynamics application, not for measured popularity.
- **Claimed contribution:** The authors derive an asymptotic-numerical method and matrix perturbation analysis, then compare predicted stability thresholds with their time-marching numerical scheme.
- **Caveat:** The demonstrated system uses conceptual Sel’kov kinetics and mathematical/numerical validation, not measurements in biological cells; conclusions depend on the model assumptions and asymptotic regime.
- **Announcement type:** new submission, 2026-11-25 batch
- **Themes:** Molecular & cell biology; Quantitative methods

### 8. [Uncertainty Quantification and Global Sensitivity Analysis of Patient-Specific Coronary Hemodynamics Under Unsteady Flow Conditions](https://arxiv.org/abs/2611.31594)
- **Abstract:** A polynomial-chaos uncertainty framework propagates uncertain flow waveforms and physiological inputs through coronary hemodynamics simulations for three patient-specific models, reporting greater relative uncertainty in multidirectional wall-shear metrics.
- **Authors:** Muhammad Usman; Nafis M. Arefin; Akil Narayan; Lucas H. Timmins
- **arXiv:** `2611.31594v1` (published 2026-11-23 21:40:33 UTC; categories: `physics.flu-dyn`, `math.NA`, `physics.med-ph`)
- **Evidence for ranking:** Signal score 0.50, entirely two cross-lists (0.50); no candidate HF upvotes or HN points/comments were recorded. Ranked for direct cardiovascular biomedical modeling relevance, not for measured popularity.
- **Claimed contribution:** The preprint combines finite-element simulations, polynomial-chaos emulators, and global sensitivity analysis; velocity waveform uncertainty dominated variability in oscillatory shear and cross-flow indices in the three modeled cases.
- **Caveat:** This is a computational study of three patient-specific models, not a clinical outcomes or prospective validation study; its conclusions depend on parameter distributions and model assumptions.
- **Announcement type:** new submission, 2026-11-25 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods; Medical physics & imaging

### 9. [Longitudinal Characterization of Personalized Hydration Dynamics Using a Facial-Video Digital Hydration Biomarker](https://arxiv.org/abs/2611.32326)
- **Abstract:** In a small longitudinal study, five adults completed scheduled water/electrolyte observations and a separate electrolyte challenge; facial-video hydration scores changed after drinking and varied markedly between people.
- **Authors:** Janindu Athukorala; D. M. J. Prathapa; Thanveer Ahamed; Yudara Kularathne
- **arXiv:** `2611.32326v1` (published 2026-11-24 10:16:50 UTC; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Signal score 0.25, entirely one cross-list (0.25); no candidate HF upvotes or HN points/comments were recorded. Ranked last for weaker fit to the molecular-biology emphasis and exploratory five-person evidence, not as a claim of low importance.
- **Claimed contribution:** The authors report exploratory within-person trajectories and argue that the observed variation warrants studying personal calibration in larger controlled hydration studies.
- **Caveat:** Only five adults were studied; the water/electrolyte day order was fixed and the authors call for larger controlled studies. This exploratory digital biomarker is not established as a clinical hydration measure.
- **Announcement type:** new submission, 2026-11-25 batch
- **Themes:** Biomedical & translational medicine; Quantitative methods; Medical physics & imaging

## Trending Research Themes

1. **Multimodal tissue pathology and reproducibility.** VirTues-M2 (2611.31451) joins morphology and spatial proteomics for prediction, segmentation, and biomarker work; the scanner-tempering study (2611.31536) targets reproducibility across image-acquisition devices. These are two different contributions, not independent replications of one another.

2. **Protein generation is being evaluated at the representation and decoding levels.** The tokenizer benchmark (2611.32168) isolates tokenizer choice in a fixed language-model setup, while PredMem (2611.32347) changes inference-time self-conditioning in existing multimodal generators. Both report computational generation results; neither demonstrates experimental protein function.

3. **Evaluation design and uncertainty shape biomedical prediction claims.** The DDI benchmark (2611.32371) shows representation rankings changing with chemical holdout; multi-omics survival benchmarking (2611.32382) reports cancer-specific variability; and coronary simulations (2611.31594) quantify uncertainty in predicted flow-derived indices. These papers share an emphasis on split, model, and input uncertainty—not evidence of a field-wide shift.

## Open Problems and Research Directions

**Author-stated limits:** VirTues-M2 calls for larger independent cohorts and prospective multi-site assessment; the tempering study is retrospective and tests one encoder, with transfer to unrepresented scanners uncertain. The protein-tokenizer benchmark is limited to one base-model/training configuration and greedy decoding, while the intracellular-oscillation study validates a mathematical model numerically rather than in cells. The hydration paper itself calls for larger controlled studies.

**Follow-up synthesis:** (1) Evaluate VirTues-M2 and tempering prospectively across institutions, scanner manufacturers, and patient groups, with prespecified calibration and threshold metrics; for survival signatures, use substantially larger external cohorts. (2) Repeat protein-tokenizer and PredMem comparisons across model sizes, training recipes, and decoding strategies, then test selected generated sequences in biochemical folding/stability or activity assays. (3) For DDI and multi-omics models, use external temporal or institutional holdouts and report label provenance, calibration, and subgroup performance; for coronary models, compare propagated uncertainty against independent physiological measurements across more patients. (4) Test predicted cell synchronization in a controlled multicellular system while varying cell spacing and kinetic parameters. These are proposed validation steps, not claims of clinical readiness or novelty.

## Takeaway

The clearest biomedical signals in this batch are methodological: combining tissue morphology with molecular measurements and making model outputs more reproducible, while protein-generation work probes how representations affect computational results. The candidate pool contained no detected HF/HN attention and citation retrieval failed, so this is a relevance-ranked snapshot—not a popularity ranking. None of the preprints alone establishes clinical benefit.

## Method and sources

**Window:** daily; latest announcement batch, 2026-11-25. The announced batch covers submissions from 2026-11-23 19:00 UTC through 2026-11-24 19:00 UTC and was announced at 2026-11-25 01:00 UTC; no prior-batch substitution was needed. Snapshot: 2026-11-25 03:09:01 UTC (signal file generated_at). All nine papers are v1 new submissions.

**Candidate query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`, sorted by submitted date. The arXiv API returned 200 newest entries; all nine in the selected window were identified before the returned results crossed the window boundary. Each selected candidate was checked against its versioned arXiv abstract page and API metadata. The supplied signal pool is `/home/yizhuan/.research/bio/daily/arxiv-trending-bio-daily-2026-11-25.signals.json` (arXiv source status ok, 9 candidates).

**Ranking:** the collector recorded zero candidates with external HF/HN attention (`with_attention: 0`). For individual candidates, the listed score is entirely the cross-list component: 0.50 for two cross-lists, 0.25 for one, and 0.00 for none. Hugging Face and Hacker News collection succeeded, but no candidate-specific upvotes, points, or comments entered these scores. Semantic Scholar retrieval was unavailable (HTTP 429), so citation and influential-citation evidence could not be assessed. Zero means no collected signal, not low importance. Because measured attention was absent, entries are ordered by direct biological/biomedical relevance and evidence specificity; scores are disclosed but not treated as popularity or validity measures.

**Primary sources:** arXiv abstract pages: [2611.31451](https://arxiv.org/abs/2611.31451), [2611.31536](https://arxiv.org/abs/2611.31536), [2611.32168](https://arxiv.org/abs/2611.32168), [2611.32382](https://arxiv.org/abs/2611.32382), [2611.32347](https://arxiv.org/abs/2611.32347), [2611.32371](https://arxiv.org/abs/2611.32371), [2611.32077](https://arxiv.org/abs/2611.32077), [2611.31594](https://arxiv.org/abs/2611.31594), [2611.32326](https://arxiv.org/abs/2611.32326). The top three papers were also read in PDF through their introduction, results, and limitations/discussion sections where available. No bioRxiv, medRxiv, clinical guideline, or patient-specific evidence is represented.