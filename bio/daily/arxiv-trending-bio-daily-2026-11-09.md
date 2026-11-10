# Notable biology and biomedical papers — arXiv batch of 9 November 2026

Daily snapshot: 2026-11-10 01:25:17 UTC. The latest available announcement batch is Monday, 9 November (today's Tuesday batch had not appeared at snapshot time). Thirteen papers are relevance-ranked below. The recurring agenda is computational biology with stronger data/validation settings, alongside translational imaging methods. arXiv has no official trending chart; this is an inferred relevance-and-evidence ranking, not a popularity ranking. Biomedical coverage on arXiv is incomplete: much clinical and experimental biology preprinting appears on bioRxiv or medRxiv.

No checkable popularity signal was strong enough to call these the “hottest” papers, so this report is titled Notable recent papers. Some entries were cross-listed into a relevant arXiv category in the 9 November batch; their original submission timestamps are shown separately. No revisions are included.

## Notable recent papers (relevance-ranked)

### 1. [Synchronized Optimal Transport Reconstructs Coupled Transcriptomic and Chromatin Dynamics](https://arxiv.org/abs/2611.08853)
- **Abstract:** COATI models RNA and ATAC developmental trajectories in separate spaces and is evaluated on synthetic data and four developmental datasets, including held-out-stage reconstruction.
- **Authors:** Jingfeng Wang; Yanxiang Zhao; Qing Nie; Zixuan Cang
- **arXiv:** `2611.08853v1` (published 2026-11-06T01:19:41Z; categories: `q-bio.GN`, `math.OC`)
- **Evidence for ranking:** Close fit to the requested RNA/genomics focus; the authors report four developmental datasets, held-out-stage tests, and agreement of inferred lineage responses with independent CRISPR perturbation and epigenetic results.
- **Claimed contribution:** The authors say synchronized unbalanced optimal transport improves held-out population reconstruction and preserves chromatin heterogeneity and developmental lineage relationships.
- **Caveat:** Trajectories are inferred from destructive snapshots, not tracked individual cells; results depend on a pretrained RNA-to-ATAC map and do not establish true lineage paths.
- **Announcement type:** New submission; announcement-batch date 2026-11-09.
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Omics & single-cell methods

### 2. [Health-System-Wide Mapping of Demographic Information in Routine Clinical Histopathology](https://arxiv.org/abs/2611.09851)
- **Abstract:** An analysis of 1.3 million H&E slides from 257,322 patients across 25 organs found that models could recover sex, age group, and self-reported race from histology, with performance varying by organ and label.
- **Authors:** Shengjia Chen; Ruchika Verma; Kevin Clare; Paula Restrepo; Jannes Jegminat; Eugenia Alleva; Kuan-lin Huang; Aryeh Stock; Brandon Veremis; Thomas Fuchs; Gabriele Campanella
- **arXiv:** `2611.09851v1` (published 2026-11-06T18:34:51Z; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Direct biomedical relevance and unusually broad cohort scale: 1.3 million slides, 257,322 patients, 25 organs, and 69 organ-demographic combinations in the authors' analysis.
- **Claimed contribution:** The authors provide a systematic map of demographic-associated information in routine histopathology and identify possible implications for shortcut learning; explanations for the signals remain hypotheses.
- **Caveat:** Predictability does not identify its biological or social source. This is a retrospective single-health-system analysis; diagnosis grouping is not external replication or causal evidence.
- **Announcement type:** New submission, cross-listed into q-bio.QM; announcement-batch date 2026-11-09.
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 3. [Personalized health coaching via coachable health age and counterfactual wearable trajectories](https://arxiv.org/abs/2611.08568)
- **Abstract:** The authors combine a wearable-derived health-age metric with a model trained on over 2.2 million person-weeks to forecast responses to lifestyle changes and generate counterfactual coaching plans, evaluated across three cohorts and by expert reviewers.
- **Authors:** Simon A. Lee; Zeinab Esmaeilpour; Menglian Zhou; Marius Guerard; Sohrab Sidhu; Alexandru Solot; Hamid Palangi; Pramod Rudrapatna; Ming-Zher Poh; Max A. Xu; Daniel McDuff; Dimitrios Antos; Yuzhe Yang; Jeffrey N. Chiang; Anthony Z. Faranesh; Lindsey Sunden; Mark Malhotra; Shwetak Patel; A. Ali Heydari; Ahmed A. Metwally
- **arXiv:** `2611.08568v1` (published 2026-11-05T17:52:57Z; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** The paper reports cohorts of 2,780, 22,748, and 1,464 participants, SensorWM pretraining on about 100,000 people, and blinded coach/clinician review of generated plans.
- **Claimed contribution:** The authors report improved prognostic discrimination over age, sex, and BMI, multi-week response forecasts, and higher expert preference for counterfactual-grounded plans.
- **Caveat:** Forecast accuracy and expert review do not show that plans change behavior or health outcomes; the abstract reports no prospective intervention.
- **Announcement type:** New submission; announcement-batch date 2026-11-09.
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 4. [Navigating Selection Bias in Genome-wide Association Studies (GWAS)](https://arxiv.org/abs/2611.09429)
- **Abstract:** This methods review organizes ten ways to diagnose or correct GWAS selection bias by available data and selection mechanism, with R implementations for nine methods and simulated examples.
- **Authors:** Ciarrah-Jane S Barry; Tahereh Gholipourshahraki; Zoltán Kutalik; Bjarni J Vilhjálmsson; Esben Agerbo
- **arXiv:** `2611.09429v1` (published 2026-11-06T13:00:13Z; categories: `stat.ME`, `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Broad relevance to human genetics and biobank inference; the authors compare ten methods, state assumptions and data needs, and provide code plus worked simulations.
- **Claimed contribution:** The review offers a decision framework for participation, case-control, index-event, sex-differential, and survival-related selection bias.
- **Caveat:** This is a methods synthesis, not new population-scale validation; every correction remains conditional on its assumptions and required data.
- **Announcement type:** New submission, cross-listed into q-bio.GN/QM; announcement-batch date 2026-11-09.
- **Themes:** DNA & genomics; Quantitative methods

### 5. [Dual-energy cardiac DSA imaging using a dual-layer flat-panel detector: in vivo validation study](https://arxiv.org/abs/2611.08820)
- **Abstract:** A dual-energy material-decomposition method using a dual-layer detector is evaluated with simulations and preliminary in-vivo swine cardiac angiography; the authors report improved vessel contrast and reduced scatter effects.
- **Authors:** Yuhang Tan; Jiongtao Zhu; Xin Zhang; Haodi Wu; Xiao Xuan; Mang Feng; Mingzhi Cui; Hairong Zheng; Dong Liang; Yongshuai Ge
- **arXiv:** `2611.08820v1` (published 2026-11-06T00:22:13Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Direct imaging validation: Monte Carlo simulations and in-vivo swine experiments on a clinical DSA system; the authors report over 80% lower scatter impact in simulation.
- **Claimed contribution:** The authors propose temporally subtracted low/high-energy projections with penalized-likelihood decomposition to improve cardiac vessel visualization without requiring precise scatter correction.
- **Caveat:** Preliminary animal validation is not human clinical evidence; broader motion and multi-material performance remain to be tested.
- **Announcement type:** New submission; announcement-batch date 2026-11-09.
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 6. [KineCouple: Substrate-conditioned residual readout for enzyme kinetic prediction](https://arxiv.org/abs/2611.09377)
- **Abstract:** KineCouple uses substrate-conditioned cross-attention over residue features to predict enzyme kcat and Km, reporting small pooled out-of-fold improvements over reproduced CataPro results.
- **Authors:** Chun Kang; Yunbo Zhang; Fanhu Zeng; Jian Liu; Siwei Deng; Lei Sha
- **arXiv:** `2611.09377v1` (published 2026-11-06T12:17:54Z; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Direct enzyme-kinetics relevance and a benchmark comparison; reported kcat RMSE/PCC move from 1.333/0.492 to 1.330/0.496, and Km from 0.998/0.633 to 0.997/0.634.
- **Claimed contribution:** The authors condition residue-level aggregation on substrate features while keeping ProtT5 and MolT5 encoders frozen.
- **Caveat:** Metric gains are small; repeated-run variability and matched controls are needed, and attention weights do not establish physical catalytic contacts.
- **Announcement type:** New submission, cross-listed into q-bio.QM; announcement-batch date 2026-11-09.
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis; Quantitative methods

### 7. [Smart Spectral Doppler Ultrasound Imaging using Motion Tracking based on Wide-beam transmission and Neural Networks: Preliminary Results](https://arxiv.org/abs/2611.09002)
- **Abstract:** A single-transmit wide-beam Doppler method tracks vessel motion and updates the sample volume; simulations and in-vivo carotid-artery and hepatic-vein demonstrations report improved spectral signal-to-noise under tissue motion.
- **Authors:** Jihye Baek; Allison Lee; Jinbum Kang; Yangmo Yoo
- **arXiv:** `2611.09002v1` (published 2026-11-06T05:18:42Z; categories: `physics.med-ph`)
- **Evidence for ranking:** The authors report Field II simulations plus in-vivo demonstrations in two vessels, with spectral-SNR gains of 9.3 dB and 4.5 dB respectively.
- **Claimed contribution:** Wide-beam transmission aims to preserve pulse-repetition frequency while a lightweight tracker follows motion and repositions the Doppler sample volume.
- **Caveat:** In-vivo evidence is limited to two demonstrations; performance across patients, pathologies, and routine clinical workflows is not established.
- **Announcement type:** New submission; announcement-batch date 2026-11-09.
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 8. [SmartBloch-Agent: An Agentic Framework for Automated MRI Sequence Design and Optimization](https://arxiv.org/abs/2611.09413)
- **Abstract:** SmartBloch-Agent uses an AI agent and an in-house Bloch simulator to turn natural-language imaging objectives into MRI sequence designs, simulations, reconstructions, and optimization feedback.
- **Authors:** Jiakai Yang; Haoye Zheng; Yixiao Yue; Qinqin Yang; Zhong Chen; Shuhui Cai; Congbo Cai
- **arXiv:** `2611.09413v1` (published 2026-11-06T12:44:55Z; categories: `physics.med-ph`, `cs.AI`, `eess.IV`)
- **Evidence for ranking:** Cross-listed across medical physics, AI, and imaging; the authors report automated experiments across varied objectives and improved parameter-estimation and quantitative-reconstruction metrics.
- **Claimed contribution:** The framework links sequence construction, physical simulation, parameter search, reconstruction, and evaluation into an agent-driven research loop.
- **Caveat:** Reported evidence is computational; scanner deployment and independent validation on acquired patient data are not established.
- **Announcement type:** New submission; announcement-batch date 2026-11-09.
- **Themes:** Medical physics & imaging; Quantitative methods

### 9. [Pangenome Peeling: Decomposing Weighted Adjacencies into Path-Forest Genomes](https://arxiv.org/abs/2611.09533)
- **Abstract:** The authors define an inverse pangenome problem that reconstructs constituent linear genomes from weighted adjacency graphs and compare two algorithms on simulated data.
- **Authors:** Alitzel López Sánchez; Jiazhen Leng; Natasha Ivanova; Lingling Jin; David Sankoff
- **arXiv:** `2611.09533v1` (published 2026-11-06T14:45:32Z; categories: `cs.DM`, `q-bio.GN`)
- **Evidence for ranking:** Direct genomics application, a formal problem definition and lower-bound result, and a simulation comparison using genome similarity and matching criteria.
- **Claimed contribution:** The maximum-spanning-tree path decomposition reportedly recovers simulated constituent genomes more faithfully than sequential edge addition as genome size grows.
- **Caveat:** Evaluation is simulation-based; performance on real, noisy pangenome graphs and ancestral genomes remains unshown.
- **Announcement type:** New submission, cross-listed into q-bio.GN; announcement-batch date 2026-11-09.
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

### 10. [Protein B-factor modeling with local magnitude](https://arxiv.org/abs/2611.08832)
- **Abstract:** A local geometric descriptor for protein structures modestly improves B-factor prediction across protein benchmarks while reducing feature-extraction cost for large structures.
- **Authors:** Wanying Bi; Jian Liu; Hongsong Feng
- **arXiv:** `2611.08832v1` (published 2026-11-06T00:39:33Z; categories: `q-bio.BM`)
- **Evidence for ranking:** The authors use 364 proteins in fitting analyses and 345 in blind prediction across three validation protocols; local-feature gains are consistent but small.
- **Claimed contribution:** Nearest-neighbor local magnitude features preserve residue-level structural information and have lower asymptotic factorization cost than global magnitude for large structures.
- **Caveat:** Predictive gains are modest and experiments use a single-seed configuration; faster extraction is not universal for small proteins.
- **Announcement type:** New submission; announcement-batch date 2026-11-09.
- **Themes:** Biochemistry & proteins; Quantitative methods

### 11. [Hybrid Quantum-Classical Annealing for Protein Side-Chain Optimization: A Feasibility Study](https://arxiv.org/abs/2611.08696)
- **Abstract:** A hybrid annealer is compared with Gurobi on 40 side-chain optimization instances derived from 20 experimentally determined protein structures; the authors report competitive or lower-energy solutions on larger instances.
- **Authors:** Valeria B. C. Visani; Simone Reale; Alfonso Gautieri; Elisabetta Di Nitto
- **arXiv:** `2611.08696v1` (published 2026-11-05T20:52:29Z; categories: `cs.ET`, `q-bio.BM`, `quant-ph`)
- **Evidence for ranking:** A direct protein-design optimization task, 40 instances from 20 structures, and comparisons with a commercial solver at multiple runtime budgets.
- **Claimed contribution:** The authors argue that side-chain optimization is a suitable binary-quadratic problem for testing hybrid annealing and report reaching certified optima when available.
- **Caveat:** This is a feasibility study, not experimental protein-design validation; comparisons with heuristics tailored to side-chain optimization are still needed.
- **Announcement type:** New submission, cross-listed into q-bio.BM; announcement-batch date 2026-11-09.
- **Themes:** Biochemistry & proteins; Quantitative methods

### 12. [Medical Radioisotopes: Clinical Demand, Production Physics, and Untapped Pathways](https://arxiv.org/abs/2611.08727)
- **Abstract:** This review maps more than 40 medical radioisotopes across established, underused, and emerging groups, connecting clinical applications with production routes and radiochemical constraints.
- **Authors:** Jarrett Moon; Claire Huchthausen; Jose R Alonso; Shadi A Esfahani; Faraz Farhadi; David McClain; Hamid Sabet; Pedram Heidari; Janet M Conrad; Daniel Winklehner
- **arXiv:** `2611.08727v1` (published 2026-11-05T21:20:35Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Broad cross-disciplinary coverage of clinical demand and production constraints across 40+ isotopes; included for direct medical-physics relevance, not popularity.
- **Claimed contribution:** The authors identify production-side bottlenecks and underused isotopes that could merit further assessment for clinical access.
- **Caveat:** This is a review, not a trial or new evidence that expanding production changes patient outcomes.
- **Announcement type:** New submission; announcement-batch date 2026-11-09.
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

### 13. [Medical Radioisotopes: Supply-chain Resilience, Distributed Production, and Access](https://arxiv.org/abs/2611.08734)
- **Abstract:** A review pairs literature analysis with expert interviews to assess isotope supply disruptions and argues for regional accelerator centers alongside centralized reactor production.
- **Authors:** David McClain; Daniel Winklehner; Faraz Farhadi; Jose R Alonso; Shadi A Esfahani; Claire Huchthausen; Jarrett Moon; Hamid Sabet; Pedram Heidari; Janet M Conrad
- **arXiv:** `2611.08734v1` (published 2026-11-05T21:33:33Z; categories: `physics.med-ph`)
- **Evidence for ranking:** Direct relevance to access and resilience of nuclear-medicine isotopes; the authors combine 2025–2026 supply-chain cases with expert interviews.
- **Claimed contribution:** The authors argue that regional accelerator production could complement aging centralized reactors and reduce single-point and cross-border vulnerabilities.
- **Caveat:** The proposal is a literature- and interview-based analysis; the effects of regional centers on access and patient outcomes are not evaluated.
- **Announcement type:** New submission; announcement-batch date 2026-11-09.
- **Themes:** Biomedical & translational medicine; Medical physics & imaging

## Trending Research Themes

- **Multimodal and population-level inference:** COATI couples RNA and chromatin trajectories; the histopathology study maps demographic-associated signals across organs; the GWAS review organizes corrections for biased genetic samples. These papers ask different questions and do not by themselves establish a field-wide shift.
- **Computational protein biology:** KineCouple predicts enzyme kinetics, local magnitude models protein B-factors, and hybrid annealing tests side-chain optimization. Each is a computational result, with distinct benchmark limits; none demonstrates experimental protein engineering outcomes.
- **Translation through imaging and infrastructure:** DSA and Doppler report animal/in-vivo imaging demonstrations, SmartBloch-Agent is simulation-based, and the two radioisotope reviews analyze production and supply. Their evidence ranges from technical experiments to synthesis and expert interviews, not clinical effectiveness.
- **Predictive health models remain pre-intervention:** The wearable coaching paper reports cohort prediction and expert review of plans, not observed behavior change or health benefit.

## Open Problems and Research Directions

- **Establish where histology signals come from:** The pathology authors treat tissue and context explanations as hypotheses. Multi-health-system replication with site/acquisition controls, blinded pathology review, and subgroup calibration could separate tissue-associated information from case mix and technical artifacts.
- **Test inferred developmental paths directly:** COATI reports agreement with perturbation and epigenetic data, but cannot track the same cells through destructive sampling. Independent lineage-tracing or perturbation datasets, denser stages, and sensitivity to the pretrained RNA-to-ATAC map would sharpen the evidence.
- **Measure robustness of small model gains:** For KineCouple and local-magnitude prediction, repeated seeds, paired out-of-fold errors, and matched-compute baselines would clarify stability. Pangenome peeling needs tests on noisy real graphs and known-truth simulated ancestries.
- **Expand imaging validation:** The cardiac DSA and Doppler studies could be tested across broader motion regimes and acquisition settings, with failure cases reported; animal feasibility should remain distinct from human performance.
- **Evaluate translation prospectively:** Wearable coaching requires prospective studies measuring adherence and health outcomes; SmartBloch requires real-scanner evaluation. For isotope production proposals, scenario analyses and real-world access measures would test whether distributed capacity addresses documented shortages.

## Takeaway

The most evidence-rich papers in this snapshot combine computational methods with broad cohorts, multiple developmental datasets, or explicit animal/in-vivo imaging tests. Others are reviews or simulations. The ranking is relevance-led because the batch is too new for robust attention evidence; none of these preprints alone supports a change in clinical practice.

## Method and sources

- **Window:** Daily, 2026-11-09 to 2026-11-09. Latest available announcement batch: Monday 2026-11-09; no Tuesday batch had appeared at the 2026-11-10T01:25:17Z snapshot. This is not a prior-batch substitution.
- **Snapshot:** 2026-11-10T01:25:17Z.
- **Candidate discovery:** The arXiv q-bio combined recent listing showed 20 entries for 9 November; the physics.med-ph listing showed five new submissions. Cross-listed records were deduplicated by versionless arXiv ID. Thirteen relevant papers are selected. The standalone cs.BI listing could not be independently confirmed, so papers found only there may be missing; this should not be read as an exhaustive survey of the configured corpus.
- **Configured category query:** `https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200`
- **Ranking:** arXiv publishes no trend/readership statistics. With attention evidence sparse for this new batch, papers are ordered by fit to biochemistry, DNA/RNA, genomics, and medicine; breadth and type of author-reported evidence; and cross-list breadth where applicable. Recency is only a tie-breaker. No views, downloads, citation gains, or popularity claims are used.
- **Primary sources:** [q-bio recent listing](https://arxiv.org/list/q-bio/recent), [physics.med-ph new submissions](https://arxiv.org/list/physics.med-ph/new), and the linked arXiv abstract pages for all selected papers. Full-text checks for the top three: [2611.08853 PDF](https://arxiv.org/pdf/2611.08853), [2611.09851 PDF](https://arxiv.org/pdf/2611.09851), and [2611.08568 PDF](https://arxiv.org/pdf/2611.08568).
