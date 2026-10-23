# Biology and Biomedicine on arXiv — weekly snapshot, 17–23 October 2026

11 notable recent papers selected from 99 deduplicated records matching the configured categories and date window (60 new submissions, 39 revisions). The recurring threads are experimental feedback in AI-assisted molecular design, computational modeling of molecular recognition, and robustness/privacy in transcriptomics. This is an evidence-weighted editorial shortlist, not a measured popularity chart: arXiv has no official trending ranking, citation/attention evidence is sparse for papers posted this recently, and arXiv omits much of biomedical preprint activity, especially bioRxiv and medRxiv. The ranking below therefore emphasizes research relevance and checkable study evidence rather than readership.

## Top papers (ranked)

### 1. [Aptamers as a sandbox for lab-in-the-loop agentic molecular discovery](https://arxiv.org/abs/2610.24806)
- **Abstract:** The authors report three design–test–improve rounds of AI-guided ssDNA aptamer screening against α-thrombin and myoglobin, with bead-corrected hit rates changing across rounds and orthogonal titrations on eight thrombin candidates.
- **Authors:** Zachary Cutts, John Coller, Rachel Chen, Hua Tang, Mathias Bellaiche, Ryder Easterlin, Dina Zverinski, Petar Sirkovic, Avinatan Hassidim, Yossi Matias, Pooja Rao, Annalisa Pawlosky
- **arXiv:** `2610.24806v1` (published 2026-10-17T18:21:50Z; categories: `q-bio.BM` primary, `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Direct wet-lab evidence across ~4,400 sequenced constructs and three rounds; eight-clone titration check (reported Pearson r=0.90); the work was also highlighted on Google Research's publication page and blog (author-affiliated attention, not independent validation).
- **Claimed contribution:** The authors say iterative assay feedback let their agent pipelines diagnose cross-reactivity and raise reported on-target hit rates by the third round; titrations for selected thrombin binders gave apparent K_D estimates of 24.6–133 nM.
- **Caveat:** Assays cover two protein targets and bead-based binding, not in-vivo function or clinical performance. The authors note they did not run matched-budget no-feedback or non-agent control arms, so the specific value of agentic reasoning is not isolated.
- **Announcement type:** new submission, 2026-10-17
- **Themes:** Biochemistry & proteins; DNA & genomics; Quantitative methods

### 2. [ProMORNA: An End-to-End Generative Framework for Full-Length mRNA Design](https://arxiv.org/abs/2605.01513)
- **Abstract:** The revised paper presents a BART-style full-length mRNA generator trained on over six million protein–mRNA pairs and reports improved predicted design trade-offs plus a small in-vitro Fluc2P reporter screen.
- **Authors:** Zixi Shao, Tao Wang, Ye Shen, Tianyi Huang, Yibei Xiao
- **arXiv:** `2605.01513v2` (first published 2026-05-02T16:05:51Z; revised 2026-10-21T13:02:48Z; categories: `cs.LG` primary, `cs.AI`, `q-bio.BM`)
- **Evidence for ranking:** Substantive v2 revision during this window adds in-vitro validation; three independent reporter experiments and an explicitly described comparator; cross-listed in computational learning and biomolecular categories.
- **Claimed contribution:** The authors report that Candidate 2's 12–72 h reporter-activity AUC was 3.33× the conventional benchmark (Holm-adjusted P=0.01285); its estimated 1.29× advantage over the reported GEMORNA candidate remains exploratory after multiplicity correction.
- **Caveat:** The prospective validation selected seven candidates for one reporter protein; reporter activity is not a direct measurement of mRNA stability or translation, and no animal or human evidence is reported. The authors call for broader, independent validation.
- **Announcement type:** revision, 2026-10-21
- **Themes:** RNA & transcriptomics; Biochemistry & proteins; Quantitative methods

### 3. [RiboBridge: protein-conditioned de novo RNA binder structure design](https://arxiv.org/abs/2610.30668)
- **Abstract:** RiboBridge separates RNA conformer generation from protein-relative placement and, in a benchmark of 124 protein–RNA complexes, reports better complex-recovery metrics than the compared methods under post-hoc interface correspondence.
- **Authors:** Zhou Zhang, Hanqun Cao, Minghao Sun, Odin Zhang, Yang Zhang, Pheng Ann Heng, Wujun Li, Tianfan Fu
- **arXiv:** `2610.30668v1` (published 2026-10-22T03:32:07Z; categories: `cs.LG` primary, `q-bio.BM`)
- **Evidence for ranking:** A temporally split, sequence-filtered and redundancy-controlled 124-complex benchmark, component ablations, and an external computational-biology paper listing; these are technical/relevance signals, not readership counts.
- **Claimed contribution:** The authors report the best fNAT and DockQ and lowest interface/ligand RMSDs among compared methods; 20/124 targets reached DockQ ≥0.23.
- **Caveat:** Native interface information is used after generation to match a generated pocket candidate for evaluation. This is computational structure recovery, not evidence of binding affinity, function, or therapeutic potential; the paper itself calls for larger functional validation.
- **Announcement type:** new submission, 2026-10-22
- **Themes:** Biochemistry & proteins; RNA & transcriptomics; Bioinformatics & sequence analysis

### 4. [Accurate quantification of protein concentrations and state populations by 2D 1H-N Q-BEST NMR](https://arxiv.org/abs/2610.26017)
- **Abstract:** The authors introduce a three-spectrum 2D Q-BEST NMR protocol for estimating protein concentration and relative conformational-state populations, validated on ubiquitin and applied to heterogeneous protein samples.
- **Authors:** Yacine Ouali, Beate Bersch, Bernhard Brutscher
- **arXiv:** `2610.26017v1` (published 2026-10-19T08:40:00Z; categories: `q-bio.BM` primary)
- **Evidence for ranking:** The arXiv record cites a 2026 Journal of Biomolecular NMR publication; the abstract reports a model-protein validation and applications to multiple samples.
- **Claimed contribution:** The authors report approximately 15–20% precision at individual ubiquitin cross-peaks, with improved precision possible by averaging resolved resonances.
- **Caveat:** Validation is centered on ubiquitin and NMR-visible species; that precision should not be generalized to every protein, spectrum, or state population without further testing.
- **Announcement type:** new submission, 2026-10-19
- **Themes:** Biochemistry & proteins; Quantitative methods

### 5. [EMBER: Predicting TCR–pMHC Binding Without a Docked Complex](https://arxiv.org/abs/2610.27334)
- **Abstract:** EMBER predicts T-cell receptor–peptide–MHC binding from independently folded receptor and pMHC residue graphs, avoiding a predicted docked complex, and reports gains over six retrained baselines in epitope-disjoint tests.
- **Authors:** Lin Ha, Chen Zhou, Haozheng Luo, Han Liu, Xiaoyu Zhang, Yan Chen
- **arXiv:** `2610.27334v1` (published 2026-10-19T21:55:45Z; categories: `q-bio.QM` primary, `cs.LG`)
- **Evidence for ranking:** Epitope-disjoint evaluation, six retrained baselines, and four folding tools; the authors report gains across AUROC, AUPRC, MCC, and ranking stability.
- **Claimed contribution:** The authors attribute the gains to representation comparison without a shared coordinate frame, which prevents placement error from a predicted complex from entering the predictor.
- **Caveat:** This is benchmarked computational prediction, not a prospective binding assay or evidence of clinical utility; performance depends on the test distribution and label quality.
- **Announcement type:** new submission, 2026-10-19
- **Themes:** Biomedical & translational medicine; Bioinformatics & sequence analysis; Quantitative methods

### 6. [Benchmarking Recent Single-Cell Synthetic Data Generation Methods on the OneK1K Dataset](https://arxiv.org/abs/2610.31454)
- **Abstract:** On a donor-split OneK1K single-cell RNA-seq dataset, the authors compare three synthetic-data methods for biological fidelity and membership-inference risk, finding that non-highly-variable-gene reconstruction strongly affects privacy leakage.
- **Authors:** Buse Giledereli, Basar Temiz, Amirreza Sattarzadeh Khanehbargh
- **arXiv:** `2610.31454v1` (published 2026-10-22T15:49:27Z; categories: `q-bio.GN` primary)
- **Evidence for ranking:** The abstract reports evaluation across statistical fidelity, downstream biological preservation, and membership-inference vulnerability; the arXiv comment says it was presented at the CAMDA 2026 ELSA Health Privacy Challenge.
- **Claimed contribution:** The authors report that copying non-HVG values causes substantial leakage, while Poisson-based reconstruction reduces membership-inference risk; scGFT and scLDM retain more biological structure than an independent Poisson baseline in their tested setup.
- **Caveat:** Findings are specific to the OneK1K donor split and evaluated attacks/configurations; synthetic data should not be assumed private or biologically representative in other cohorts.
- **Announcement type:** new submission, 2026-10-22
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Quantitative methods

### 7. [An autoencoder outperforms two transformers on prediction of gene expression from chromatin accessibility](https://arxiv.org/abs/2610.28853)
- **Abstract:** A harmonized benchmark of 126,604 paired single-nucleus profiles from 19 human studies finds a dual-variational-autoencoder pipeline ahead of the tested transformer pipelines on per-gene and within-cell expression-prediction correlations.
- **Authors:** Jesse G. Meyer
- **arXiv:** `2610.28853v1` (published 2026-10-20T19:27:47Z; categories: `q-bio.GN` primary)
- **Evidence for ranking:** 70 trained runs, ten 5×2 cross-validation folds, 19 studies, paired comparisons, and an audited code/results release are reported in the abstract.
- **Claimed contribution:** The author reports that scButterfly-B beat all tested transformer pipelines in 60 paired fold comparisons and trained 3.8× faster.
- **Caveat:** Correlations were low for two withheld cell types; results depend on pipeline-specific preprocessing and target choices, and prediction from accessibility does not establish causal regulation.
- **Announcement type:** new submission, 2026-10-20
- **Themes:** DNA & genomics; RNA & transcriptomics; Bioinformatics & sequence analysis

### 8. [Spatially Informed and Direction Sensitive Representation Learning for Spatial Transcriptomics](https://arxiv.org/abs/2610.28579)
- **Abstract:** Tessera combines spatially informed gene selection with direction-sensitive, translation-invariant local cell context and reports improved representation quality across held-out tissues and technologies.
- **Authors:** Azim Dehghani Amirabad, Ali Khodabandeh Yalabadi, Artem Moskalev, Yun-Ching Chen, Mehdi Pirooznia, Scott Oloff, Rui Liao
- **arXiv:** `2610.28579v1` (published 2026-10-20T17:32:57Z; categories: `q-bio.QM` primary, `cs.AI`)
- **Evidence for ranking:** Cross-listed in quantitative biology and AI; the arXiv comment reports acceptance at the NeurIPS 2026 Workshop on AI for Drug Discovery; the abstract claims held-out tissue/technology tests.
- **Claimed contribution:** The authors say preserving relative direction between cells, rather than using distance alone or absolute coordinates, improves representation and zero-shot transfer to contexts up to 16× larger than training contexts.
- **Caveat:** This is representation-learning evaluation; the abstract does not establish improved biological discovery or downstream clinical outcomes, and does not provide cohort sizes or detailed effect estimates.
- **Announcement type:** new submission, 2026-10-20
- **Themes:** RNA & transcriptomics; Omics & single-cell methods; Quantitative methods

### 9. [Evaluating Conformal Reliability of Pathway-Level Transcriptomic Signatures Under Cross-Cohort Shift in Sepsis Mortality Prediction](https://arxiv.org/abs/2607.17405)
- **Abstract:** Across four public blood-transcriptome cohorts (936 patients, 248 mortality events), the revised study compares gene-, pathway-, and hybrid-level models under leave-one-cohort-out sepsis mortality prediction.
- **Authors:** Pratyush Kumar Shukla, Manveer Singh Tib, Siddhant Garg
- **arXiv:** `2607.17405v2` (first published 2026-07-19T20:39:30Z; revised 2026-10-18T19:20:09Z; categories: `q-bio.GN` primary)
- **Evidence for ranking:** Substantive v2 revision during the window; four-cohort external validation with 936 patients and 248 events; the arXiv comment reports acceptance at the IEEE BIBM 2026 Trustworthy AI for Biomedical Discovery workshop.
- **Claimed contribution:** The authors report that pathway-level representations gave more reliable uncertainty behavior and more stable signatures under cohort shift, while gene-level and hybrid representations generally discriminated best.
- **Caveat:** This is retrospective model evaluation, not prospective clinical validation or evidence that the model improves patient outcomes; results depend on harmonization and the selected cohorts.
- **Announcement type:** revision, 2026-10-18
- **Themes:** RNA & transcriptomics; Biomedical & translational medicine; Quantitative methods

### 10. [Reading Between the Reads: A Decade On, Revisiting Sequencing Protocol Annotation in the Sequence Read Archive](https://arxiv.org/abs/2610.27331)
- **Abstract:** Reapplying historical keyword rules to a September 2026 SRA metadata snapshot, the author finds protocol-field sparsity across 41,593,302 experiments and checks 150 sampled classifications against source XML.
- **Authors:** Jamie J. Alnasir
- **arXiv:** `2610.27331v1` (published 2026-10-19T21:49:36Z; categories: `q-bio.GN` primary, `q-bio.QM`)
- **Evidence for ranking:** Large-scale audit of 41.6 million records, a historical comparison, and a 150-record source-XML check; the paper addresses a foundational data-quality issue for genomics reuse.
- **Claimed contribution:** The author reports that the protocol field is NULL for 67.65% of experiments and that searching an additional description field raises three-step keyword detection from 1.42% to 2.88%.
- **Caveat:** Keyword detection is not the same as adequate protocol documentation; differences in library strategies and evolving terminology complicate the decade comparison.
- **Announcement type:** new submission, 2026-10-19
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

### 11. [Supercoiling Drives DNA-Protein Co-Condensation](https://arxiv.org/abs/2610.30588)
- **Abstract:** A coupled DNA-elasticity/protein-concentration model predicts that supercoiling can promote protein wetting, twist-to-writhe conversion, and DNA–protein co-condensation.
- **Authors:** Sihan Liu, Hongbo Zhao, Andrej Košmrlj
- **arXiv:** `2610.30588v1` (published 2026-10-22T01:42:38Z; categories: `physics.bio-ph` primary, `cond-mat.soft`, `q-bio.BM`)
- **Evidence for ranking:** Cross-listed in biophysics, soft matter, and biomolecules; the paper connects DNA topology with biomolecular condensation using a coupled mechanical model.
- **Claimed contribution:** The authors report that sufficiently strong supercoiling removes a nucleation barrier in their model, whereas the unsupercoiled system remains trapped in extended metastable states.
- **Caveat:** This is a theoretical/modeling result, not experimental confirmation that supercoiling drives co-condensation in cells.
- **Announcement type:** new submission, 2026-10-22
- **Themes:** DNA & genomics; Biochemistry & proteins; Quantitative methods

## Trending Research Themes

- **Experimental feedback in AI-assisted molecular design:** The aptamer study and the revised ProMORNA paper both connect generative or agentic design to lab assays. The aptamer work includes multi-round binding selection; ProMORNA reports a reporter assay. They are distinct assays and do not establish that one design loop generalizes to other targets or therapeutic settings.
- **Computational prediction of molecular recognition:** RiboBridge models protein–RNA complex geometry, while EMBER predicts TCR–pMHC binding from separately folded partners. Both rely on benchmark evaluation; neither provides prospective functional validation in the reported work.
- **Robustness, transfer, and privacy in transcriptomic data:** The OneK1K synthetic-data comparison evaluates membership-inference risk; the chromatin-accessibility benchmark exposes weak performance on held-out cell types; Tessera studies transfer across tissues/technologies; and the sepsis revision tests cohort shift. These are complementary, not independent replications of one method.
- **Measurement and data infrastructure:** Q-BEST NMR addresses quantitative protein-state measurement, while the SRA audit examines whether sequencing metadata support reliable reuse. The DNA co-condensation paper adds a molecular-mechanics hypothesis, but it is currently model-based.

## Open Problems and Research Directions

- **Separate agent effects from feedback effects:** The aptamer authors explicitly call for matched-budget no-feedback and non-reasoning control arms. A follow-up could compare agentic, non-agentic, and fixed-rule proposal strategies across multiple targets with blinded assays and the same synthesis/screening budget.
- **Test mRNA designs beyond one reporter:** ProMORNA's authors identify seven tested Pareto-selected candidates and a single reporter protein as a limitation. Independent replication with longer transcripts, multiple protein targets, and direct measurements of stability and translation would test generalizability; the reported reporter AUC alone does not establish therapeutic performance.
- **Move predicted interfaces toward functional evidence:** RiboBridge's authors identify interface prioritization and sequence realization as unresolved. Useful next steps include blind prospective target selection without post-hoc native-interface matching, RNA synthesis, affinity assays, and sequence/function tests.
- **Stress-test transfer and privacy claims:** The selected transcriptomic papers point to distinct evaluation gaps: independent donor-level privacy tests for synthetic data, additional held-out cell types for expression prediction, and external hospital cohorts for sepsis models. These would assess robustness beyond the current datasets, not establish clinical readiness.
- **Improve protocol metadata quality:** The SRA audit shows that keyword presence does not guarantee adequate documentation. A follow-up could compare structured protocol fields with source records and expert judgments across library strategies, then evaluate whether standardized fields improve reproducibility of downstream analyses.

## Takeaway

The strongest experimental signal this week is closed-loop aptamer design, while ProMORNA's new revision adds a limited reporter assay to a computational mRNA-design pipeline. Several other papers test prediction and transferability more carefully, but remain computational or retrospective. Treat the ranking as an evidence-led reading list, not a measure of popularity or clinical readiness.

## Method and sources

- **Window:** 2026-10-17 through 2026-10-23 inclusive (UTC calendar dates); snapshot taken 2026-10-23T15:09:07Z. This is a weekly window, not a single announcement batch.
- **Candidate query:** `cat:q-bio.BM OR cat:q-bio.GN OR cat:q-bio.MN OR cat:q-bio.SC OR cat:q-bio.CB OR cat:q-bio.TO OR cat:q-bio.QM OR cat:cs.BI OR cat:physics.med-ph`; recent results were checked using arXiv API sorting by submission and last-update dates, deduplicated by versionless ID. A paper qualified if first submitted or revised in the window. 99 records matched (60 new submissions, 39 revisions); 11 were selected after relevance screening, and their arXiv abstract pages were verified.
- **Ranking:** No official arXiv trending metric exists. Because the papers are very recent and citation/independent-attention signals are sparse, the order prioritizes checkable experimental or benchmark evidence, category relevance, substantive revision, and publication/workshop status; it does not claim measured popularity. Citation totals, where they may later exist, should not be read as gains during this window.
- **Coverage:** This is a selected arXiv corpus, not a systematic review. Biomedical work on bioRxiv, medRxiv, and elsewhere is not included; none of the computational or retrospective studies above should be read as practice-changing clinical evidence.
- **Sources:** Each linked arXiv abstract page is the primary metadata and abstract source. Additional context: [Google Research publication page](https://research.google/pubs/aptamers-as-a-sandbox-for-lab-in-the-loop-agentic-molecular-discovery/), [Google Research blog](https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/), and [contemporaneous AI paper listing for RiboBridge](https://ai-papers.fareesh.com/). The Google pages are author-affiliated; external listings are not readership statistics.
