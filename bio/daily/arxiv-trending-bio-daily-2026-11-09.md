# arXiv Biology & Biomedicine — notable papers in the 9 November 2026 batch

Daily batch: Monday, 9 November 2026. Eleven papers are selected from 16 deduplicated entries across the configured same-day category listings. The batch's strongest recurring pattern is computational biology that combines large or multimodal datasets with prediction or reconstruction; today's agenda is pathology-wide demographic signal, coupled RNA/chromatin trajectories, and safeguards for genetic association analysis. arXiv has no official trending chart, so this is an inferred relevance-and-evidence ranking, not a popularity ranking; arXiv also covers only part of biomedical preprinting, with much clinical and experimental work appearing on bioRxiv or medRxiv.

## Top papers (ranked)

### 1. [Health-System-Wide Mapping of Demographic Information in Routine Clinical Histopathology](https://arxiv.org/abs/2611.09851)
- **Abstract:** An analysis of 1.3 million H&E slides from 257,322 patients across 25 organs found that models could recover sex, age group, and self-reported race from histology, with performance varying by organ and demographic label.
- **Authors:** Shengjia Chen; Ruchika Verma; Kevin Clare; Paula Restrepo; Jannes Jegminat; Eugenia Alleva; Kuan-lin Huang; Aryeh Stock; Brandon Veremis; Thomas Fuchs; Gabriele Campanella
- **arXiv:** `2611.09851v1` (published 2026-11-06 18:34:51 UTC; categories: `cs.CV`, `q-bio.QM`)
- **Evidence for ranking:** Highest direct biomedical relevance and cohort scale in this batch; 1.3 million slides, 257,322 patients, 25 organs, and 69 organ-demographic combinations are reported by the authors.
- **Claimed contribution:** The authors provide a systematic map of demographic-associated information in routine histopathology and identify possible implications for shortcut learning; their proposed tissue/context explanations remain hypotheses.
- **Caveat:** Predictability does not identify its biological or social source. This is a retrospective single-health-system analysis, and diagnosis-based grouping does not substitute for external replication or causal interpretation.
- **Announcement type:** New submission, announcement batch 2026-11-09.
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 2. [Synchronized Optimal Transport Reconstructs Coupled Transcriptomic and Chromatin Dynamics](https://arxiv.org/abs/2611.08853)
- **Abstract:** COATI jointly models time-varying RNA and ATAC trajectories in separate state spaces and is evaluated on synthetic data and four developmental datasets, including held-out-stage reconstruction and lineage analyses.
- **Authors:** Jingfeng Wang; Yanxiang Zhao; Qing Nie; Zixuan Cang
- **arXiv:** `2611.08853v1` (published 2026-11-06 01:19:41 UTC; categories: `q-bio.GN`, `math.OC`)
- **Evidence for ranking:** Strong fit to RNA/genomics focus; authors report four developmental datasets, held-out-stage tests, and agreement of inferred lineage responses with independent CRISPR perturbation and epigenetic results.
- **Claimed contribution:** The authors say synchronized unbalanced optimal transport improves held-out population reconstruction and preserves chromatin heterogeneity and developmental lineage relationships.
- **Caveat:** Trajectories are inferred from destructive snapshots, not tracked individual cells; results depend on a pretrained RNA-to-ATAC map, and agreement with held-out distributions alone cannot establish the true lineage path.
- **Announcement type:** New submission, announcement batch 2026-11-09.
- **Themes:** RNA & transcriptomics; Gene regulation & epigenetics; Omics & single-cell methods

### 3. [Navigating Selection Bias in Genome-wide Association Studies (GWAS)](https://arxiv.org/abs/2611.09429)
- **Abstract:** This methods review organizes ten ways to diagnose or correct GWAS selection bias by data availability and selection mechanism, with R implementations for nine methods and simulated examples.
- **Authors:** Ciarrah-Jane S Barry; Tahereh Gholipourshahraki; Zoltán Kutalik; Bjarni J Vilhjálmsson; Esben Agerbo
- **arXiv:** `2611.09429v1` (published 2026-11-06 13:00:13 UTC; categories: `stat.ME`, `q-bio.GN`, `q-bio.QM`)
- **Evidence for ranking:** Broad relevance to biobank and genetic inference; the authors compare ten methods, state their assumptions and data needs, and provide code plus worked simulated examples.
- **Claimed contribution:** The review offers a decision framework for diagnosing or correcting participation, case-control, index-event, sex-differential, and survival-related selection bias.
- **Caveat:** It is a methods synthesis, not a new population-scale validation of the methods; each correction remains conditional on its assumptions and required data.
- **Announcement type:** New submission, cross-listed to genomics/quantitative-biology listings, announcement batch 2026-11-09.
- **Themes:** DNA & genomics; Quantitative methods

### 4. [Dual-energy cardiac DSA imaging using a dual-layer flat-panel detector: in vivo validation study](https://arxiv.org/abs/2611.08820)
- **Abstract:** A dual-energy material-decomposition method using a dual-layer detector is evaluated with simulations and preliminary in-vivo swine cardiac angiography, with the authors reporting improved vessel contrast and reduced scatter effects.
- **Authors:** Yuhang Tan; Jiongtao Zhu; Xin Zhang; Haodi Wu; Xiao Xuan; Mang Feng; Mingzhi Cui; Hairong Zheng; Dong Liang; Yongshuai Ge
- **arXiv:** `2611.08820v1` (published 2026-11-06 00:22:13 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** Direct medical-imaging validation: Monte Carlo simulations and in-vivo swine experiments on a clinical DSA system; the authors report over 80% lower scatter impact in simulation.
- **Claimed contribution:** The authors propose temporally subtracted low/high-energy projections with penalized-likelihood decomposition to improve iodine-specific cardiac vessel imaging without explicit scatter correction.
- **Caveat:** Preliminary animal validation is not human clinical evidence; residual scatter may remain under larger motion, and the current method decomposes soft tissue and iodine rather than multiple materials.
- **Announcement type:** New submission, announcement batch 2026-11-09.
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 5. [Personalized health coaching via coachable health age and counterfactual wearable trajectories](https://arxiv.org/abs/2611.08568)
- **Abstract:** The authors combine a wearable-derived health-age metric with a model trained on over 2.2 million person-weeks to forecast responses to lifestyle changes and generate counterfactual coaching plans, evaluated across three cohorts and by expert reviewers.
- **Authors:** Simon A. Lee; Zeinab Esmaeilpour; Menglian Zhou; Marius Guerard; Sohrab Sidhu; Alexandru Solot; Hamid Palangi; Pramod Rudrapatna; Ming-Zher Poh; Max A. Xu; Daniel McDuff; Dimitrios Antos; Yuzhe Yang; Jeffrey N. Chiang; Anthony Z. Faranesh; Lindsey Sunden; Mark Malhotra; Shwetak Patel; A. Ali Heydari; Ahmed A. Metwally
- **arXiv:** `2611.08568v1` (published 2026-11-05 17:52:57 UTC; categories: `q-bio.QM`, `cs.LG`)
- **Evidence for ranking:** The paper reports three cohorts (N=2,780; 22,748; and 1,464), a SensorWM model pretrained on roughly 100,000 participants, and blinded coach/clinician review of generated plans.
- **Claimed contribution:** The authors report improved prognostic discrimination over age, sex, and BMI, multi-week response forecasts, and greater expert preference for counterfactual-grounded plans.
- **Caveat:** Forecast accuracy and expert review do not show that the plans change behavior or health outcomes; a prospective intervention study is not reported in the abstract.
- **Announcement type:** New submission, announcement batch 2026-11-09.
- **Themes:** Biomedical & translational medicine; Quantitative methods

### 6. [Smart Spectral Doppler Ultrasound Imaging using Motion Tracking based on Wide-beam transmission and Neural Networks: Preliminary Results](https://arxiv.org/abs/2611.09002)
- **Abstract:** The proposed single-transmit wide-beam Doppler method tracks vessel motion and updates the sample volume; simulations and in-vivo carotid-artery and hepatic-vein demonstrations report improved spectral signal-to-noise under tissue motion.
- **Authors:** Jihye Baek; Allison Lee; Jinbum Kang; Yangmo Yoo
- **arXiv:** `2611.09002v1` (published 2026-11-06 05:18:42 UTC; categories: `physics.med-ph`)
- **Evidence for ranking:** The authors report Field II simulations plus in-vivo demonstrations in two vessels, with 9.3 dB and 4.5 dB spectral-SNR gains respectively.
- **Claimed contribution:** Wide-beam transmission is intended to preserve pulse-repetition frequency while a lightweight tracker follows motion and repositions the Doppler sample volume.
- **Caveat:** The in-vivo evidence is limited to two demonstrations; performance across patients, pathologies, and routine clinical workflows is not established.
- **Announcement type:** New submission, announcement batch 2026-11-09.
- **Themes:** Medical physics & imaging; Biomedical & translational medicine

### 7. [SmartBloch-Agent: An Agentic Framework for Automated MRI Sequence Design and Optimization](https://arxiv.org/abs/2611.09413)
- **Abstract:** SmartBloch-Agent uses an AI agent and an in-house Bloch simulator to turn natural-language imaging objectives into MRI sequence designs, simulations, reconstructions, and optimization feedback.
- **Authors:** Jiakai Yang; Haoye Zheng; Yixiao Yue; Qinqin Yang; Zhong Chen; Shuhui Cai; Congbo Cai
- **arXiv:** `2611.09413v1` (published 2026-11-06 12:44:55 UTC; categories: `physics.med-ph`, `cs.AI`, `eess.IV`)
- **Evidence for ranking:** Cross-listed across medical physics, AI, and imaging; the authors report automated experiments across varied objectives and improved parameter-estimation and quantitative-reconstruction metrics.
- **Claimed contribution:** The framework links sequence construction, physical simulation, parameter search, reconstruction, and evaluation into an agent-driven research loop.
- **Caveat:** Reported evidence is computational; scanner deployment and independent validation on acquired patient data are not established.
- **Announcement type:** New submission, announcement batch 2026-11-09.
- **Themes:** Medical physics & imaging; Quantitative methods

### 8. [KineCouple: Substrate-conditioned residual readout for enzyme kinetic prediction](https://arxiv.org/abs/2611.09377)
- **Abstract:** KineCouple uses substrate-conditioned cross-attention over residue features to predict enzyme kcat and Km, reporting small pooled out-of-fold improvements over reproduced CataPro results.
- **Authors:** Chun Kang; Yunbo Zhang; Fanhu Zeng; Jian Liu; Siwei Deng; Lei Sha
- **arXiv:** `2611.09377v1` (published 2026-11-06 12:17:54 UTC; categories: `cs.AI`, `q-bio.QM`)
- **Evidence for ranking:** Direct enzyme-kinetics relevance and a benchmark comparison; the abstract reports RMSE/Pearson improvements on both kcat and Km tasks.
- **Claimed contribution:** The authors condition residue-level aggregation on substrate features while keeping the ProtT5 and MolT5 encoders frozen.
- **Caveat:** Reported metric gains are very small; repeated-run variability and matched controls are needed, and attention weights do not establish physical catalytic contacts.
- **Announcement type:** New submission, cross-listed to quantitative biology, announcement batch 2026-11-09.
- **Themes:** Biochemistry & proteins; Bioinformatics & sequence analysis

### 9. [Pangenome Peeling: Decomposing Weighted Adjacencies into Path-Forest Genomes](https://arxiv.org/abs/2611.09533)
- **Abstract:** The authors define an inverse pangenome problem that reconstructs constituent linear genomes from weighted adjacency graphs and compare two algorithms on simulated data.
- **Authors:** Alitzel López Sánchez; Jiazhen Leng; Natasha Ivanova; Lingling Jin; David Sankoff
- **arXiv:** `2611.09533v1` (published 2026-11-06 14:45:32 UTC; categories: `cs.DM`, `q-bio.GN`)
- **Evidence for ranking:** Direct genomics application, with a formal problem definition, lower-bound result, and simulation comparison using genome similarity and matching criteria.
- **Claimed contribution:** The maximum-spanning-tree path decomposition reportedly recovers simulated constituent genomes more faithfully than sequential edge addition as genome size grows.
- **Caveat:** Evaluation is simulation-based; performance on real, noisy pangenome graphs and ancestral genomes remains unshown.
- **Announcement type:** New submission, cross-listed to genomics, announcement batch 2026-11-09.
- **Themes:** DNA & genomics; Bioinformatics & sequence analysis

### 10. [Protein B-factor modeling with local magnitude](https://arxiv.org/abs/2611.08832)
- **Abstract:** A local geometric descriptor for protein structures modestly improves B-factor prediction across protein benchmarks while reducing feature-extraction cost for large structures.
- **Authors:** Wanying Bi; Jian Liu; Hongsong Feng
- **arXiv:** `2611.08832v1` (published 2026-11-06 00:39:33 UTC; categories: `q-bio.BM`)
- **Evidence for ranking:** Protein-focused method with 364 proteins in fitting analyses and 345 in blind prediction across three validation protocols; the reported local-feature gains are consistent but small.
- **Claimed contribution:** The authors introduce nearest-neighbor local magnitude features and report lower asymptotic factorization cost than global magnitude for large structures.
- **Caveat:** Predictive gains are modest and experiments use a single-seed configuration; faster extraction is not universal for small proteins.
- **Announcement type:** New submission, announcement batch 2026-11-09.
- **Themes:** Biochemistry & proteins; Quantitative methods

### 11. [Hybrid Quantum-Classical Annealing for Protein Side-Chain Optimization: A Feasibility Study](https://arxiv.org/abs/2611.08696)
- **Abstract:** A hybrid annealer is compared with Gurobi on 40 side-chain optimization instances derived from 20 experimentally determined protein structures, with the authors reporting competitive or lower-energy solutions on larger instances.
- **Authors:** Valeria B. C. Visani; Simone Reale; Alfonso Gautieri; Elisabetta Di Nitto
- **arXiv:** `2611.08696v1` (published 2026-11-05 20:52:29 UTC; categories: `cs.ET`, `q-bio.BM`, `quant-ph`)
- **Evidence for ranking:** Direct computational protein-design task, 40 instances from 20 structures, and comparisons with a commercial solver at multiple runtime budgets.
- **Claimed contribution:** The authors argue that side-chain optimization is a suitable binary-quadratic problem for testing hybrid annealing and report that it reaches certified optima when available.
- **Caveat:** This is a feasibility study, not experimental protein-design validation; the authors call for comparisons with heuristics tailored to side-chain optimization.
- **Announcement type:** New submission, cross-listed to biomolecules, announcement batch 2026-11-09.
- **Themes:** Biochemistry & proteins; Quantitative methods

## Trending Research Themes

- **Cross-modal molecular and genome inference:** COATI links RNA and ATAC dynamics in separate spaces, while the GWAS review emphasizes how sample-selection mechanisms can distort downstream genetic inference. Pangenome Peeling takes a complementary algorithmic route, attempting to recover genomes from aggregated adjacency information. These are three different contributions, not evidence of a single field-wide shift.
- **Biomedical images as high-dimensional measurements:** The histopathology study maps demographic signal across a large clinical slide collection. In medical physics, the cardiac DSA and Doppler papers report in-vivo imaging demonstrations, whereas SmartBloch-Agent remains a simulation-driven sequence-design workflow. The evidence types are not interchangeable.
- **Protein methods remain prediction/optimization work:** KineCouple predicts kinetics, local magnitude predicts B-factors, and hybrid annealing tests side-chain optimization. All are computational evaluations; none establishes an experimental protein-design or biochemical intervention outcome.
- **Wearable-data models and prospective translation:** Coachable Health Age and SensorWM combine retrospective cohorts with counterfactual plan generation and expert review. Their reported prediction and review results do not establish real-world health benefit.

## Open Problems and Research Directions

- **Explain demographic signals in pathology:** The histopathology authors leave tissue and contextual sources as hypotheses. Follow-up work could test these candidates with pre-registered, multi-health-system cohorts, explicit acquisition/site controls, and pathology review blinded to demographic labels; report subgroup calibration and error as well as AUROC.
- **Validate inferred RNA–chromatin paths:** COATI reports agreement with perturbation and epigenetic evidence, but inferred trajectories remain distinct from direct lineage tracking. Useful next tests include denser time points, independent lineage-tracing or perturbation datasets, and sensitivity analyses for the pretrained RNA-to-ATAC map and stage spacing.
- **Separate method gains from training and benchmark effects:** For KineCouple and local-magnitude prediction, repeated seeds, paired out-of-fold errors, and matched-compute baselines would quantify stability. For pangenome peeling, noisy real graphs and known-truth simulated ancestries would test whether the reconstruction transfers beyond its current simulations.
- **Move imaging and coaching claims toward external validation:** The cardiac DSA and Doppler studies could be extended to larger, varied animal/human acquisition settings and motion regimes, while reporting failure cases. Wearable coaching needs prospective testing of adherence and outcomes; prediction and blinded plan preference alone are insufficient.

## Takeaway

Today's strongest papers pair computational methods with unusually broad datasets or explicit validation: pathology-scale cohort mapping, coupled developmental multi-omics, and imaging feasibility tests. The evidence ranges from retrospective cohorts and simulations to animal imaging; none of these preprints alone supports a change in clinical practice. Treat the ordering as a relevance-led snapshot, not a measured popularity chart.

## Method and sources

- **Window:** Daily; announcement batch 2026-11-09 (Monday). Calendar window and announcement date: 2026-11-09 to 2026-11-09. This is the latest announced batch at the snapshot, not a prior-batch substitute.
- **Snapshot:** 2026-11-09 17:14:33 UTC.
- **Candidate categories:** `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, and `physics.med-ph`. Daily category listings were checked and cross-listed IDs deduplicated; 11 papers were selected from 16 distinct same-day category entries for relevance to biochemistry, DNA/RNA, genomics, molecular medicine, and direct biomedical methods.
- **Machine-readable query:** `https://export.arxiv.org/api/query?search_query=cat:q-bio.BM+OR+cat:q-bio.GN+OR+cat:q-bio.MN+OR+cat:q-bio.SC+OR+cat:q-bio.CB+OR+cat:q-bio.TO+OR+cat:q-bio.QM+OR+cat:cs.BI+OR+cat:physics.med-ph&sortBy=submittedDate&sortOrder=descending&start=0&max_results=200`
- **Ranking:** No official arXiv trend/readership measure was available. Items are ordered by relevance to the requested subfields, breadth and type of author-reported evidence, and cross-list breadth where applicable; recency was only a tie-breaker. Searches did not provide an independent technical-attention signal for this just-announced cohort. No download/view counts or citation gains are claimed.
- **Primary sources:** The arXiv abstract pages linked above; category announcements at [q-bio](https://arxiv.org/list/q-bio/recent), [q-bio.BM](https://arxiv.org/list/q-bio.BM/recent), [q-bio.GN](https://arxiv.org/list/q-bio.GN/recent), [q-bio.MN](https://arxiv.org/list/q-bio.MN/recent), [q-bio.QM](https://arxiv.org/list/q-bio.QM/recent), and [physics.med-ph](https://arxiv.org/list/physics.med-ph/recent). Full-text checks for the top three: [2611.09851 PDF](https://arxiv.org/pdf/2611.09851), [2611.08853 PDF](https://arxiv.org/pdf/2611.08853), and [2611.09429 PDF](https://arxiv.org/pdf/2611.09429).
