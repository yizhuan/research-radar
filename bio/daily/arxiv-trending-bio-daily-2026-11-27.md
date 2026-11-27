# Biology & biomedicine on arXiv — 27 November 2026

The latest arXiv quantitative-biology listing is dated Thursday, 26 November (announced at 01:00 UTC on 27 November). Five notable papers span RNA design, spatial cell-state inference, DNA/protein binding, molecular-complex formation, and interpretable medical imaging. This is a relevance-ranked selection, not a measured “hottest” list: arXiv has no official trending chart, and its preprint listings are incomplete coverage of biomedical research. The signal file supplied for this run contains no candidate records or candidate scores.

## Notable recent papers

### 1. [KnitNet: Learning to Search at Inference Time for Exact RNA Inverse Design](https://arxiv.org/abs/2611.33812)
- **Abstract:** KnitNet uses verifier feedback to iteratively repair candidate RNA sequences; the authors report higher exact-fold solve rates on five secondary-structure benchmarks and improved 3D self-consistency in computational tests.
- **Authors:** Antonia Panescu, Xin Wang, Haoran Xu, Qingyu Chen, Carlos Oliver, Rex Ying
- **arXiv:** `2611.33812v1` (published 2026-11-25 05:42:56 UTC; categories: `q-bio.BM` (primary), `cs.AI`, `cs.LG`)
- **Evidence for ranking:** No candidate-level score or attention counts were present in the supplied signals file (pool size 0); ranked for direct RNA-design relevance, not popularity.
- **Claimed contribution:** The authors report an average 21-percentage-point increase in exact solves versus continued sampling with 70% less time-to-solve across five secondary-structure benchmarks; they also report 7.8% higher 3D structural self-consistency and 39.3% faster inference than per-target RL.
- **Caveat:** These are computational benchmark results; the abstract reports no biochemical folding or functional validation.
- **Announcement type:** New submission, listed in the 2026-11-26 announcement batch.
- **Themes:** RNA & transcriptomics; Bioinformatics & sequence analysis; Quantitative methods

### 2. [Resolving cell states in spatial transcriptomics with SCATTER](https://arxiv.org/abs/2611.34798)
- **Abstract:** SCATTER jointly estimates cell-type proportions and within-cell-type expression from spatial transcriptomic spots, using spatial context and single-cell reference profiles.
- **Authors:** Lei Huang, Yun Gong, Weiqiang Lin, Lindong Jiang, Hui Shen, Chaoyang Zhang, Hong-Wen Deng
- **arXiv:** `2611.34798v1` (published 2026-11-25 17:50:26 UTC; categories: `q-bio.QM` (primary))
- **Evidence for ranking:** No candidate-level score or attention counts were present in the supplied signals file (pool size 0); selected for direct relevance to spatial omics and for reported benchmark plus tissue-data analyses.
- **Claimed contribution:** The authors report higher measured-expression correlations than three comparators for 82.8–99.8% of evaluated gene–cell-type pairs across five pseudo-spot benchmarks, plus applications to breast cancer, multiple-sclerosis, and colorectal-cancer tissue datasets.
- **Caveat:** Much of the quantitative comparison uses pseudo-spots; the tissue applications are computational analyses and do not by themselves establish independent biological validation.
- **Announcement type:** New submission, listed in the 2026-11-26 announcement batch.
- **Themes:** Omics & single-cell methods; RNA & transcriptomics; Bioinformatics & sequence analysis

### 3. [Exclusion and internal structure in the association/dissociation kinetics of DNA-binding proteins in the fast diffusion limit](https://arxiv.org/abs/2611.33740)
- **Abstract:** The paper develops a coarse-grained stochastic model for DNA-binding proteins that combines protein footprint exclusion, diffusion, and conformational switching, and fits it to previously measured RPA–ssDNA dynamics.
- **Authors:** Xiangting Li, Tom Chou
- **arXiv:** `2611.33740v1` (published 2026-11-25 04:01:12 UTC; categories: `q-bio.BM` (primary), `cond-mat.soft`, `cond-mat.stat-mech`, `q-bio.QM`)
- **Evidence for ranking:** No candidate-level score or attention counts were present in the supplied signals file (pool size 0); selected for molecular biophysics relevance and its explicit fit to experimental RPA data.
- **Claimed contribution:** The authors derive an effective Markov model and mean-field approximation, then use multisegment binding states to model facilitated exchange and the trade-off between affinity and remodeling.
- **Caveat:** This is a theoretical/coarse-grained model fitted to previously measured RPA dynamics, not a new binding experiment; broader applicability to other proteins remains to be tested.
- **Announcement type:** New submission, listed in the 2026-11-26 announcement batch.
- **Themes:** DNA & genomics; Biochemistry & proteins; Quantitative methods

### 4. [From the Deterministic Hook Effect to Stochastic Reliability in Ternary Complex Formation](https://arxiv.org/abs/2611.33753)
- **Abstract:** Deterministic equations and stochastic simulations show how mediator dose, compartment size, and copy-number thresholds can alter the reliability of ternary-complex formation in a minimal binding model.
- **Authors:** Deepak K. Agrawal
- **arXiv:** `2611.33753v1` (published 2026-11-25 04:12:08 UTC; categories: `math.DS` (primary), `q-bio.BM`, `q-bio.MN`)
- **Evidence for ranking:** No candidate-level score or attention counts were present in the supplied signals file (pool size 0); selected for direct relevance to molecular binding and targeted-degradation mechanisms.
- **Claimed contribution:** The author reports that small simulated volumes can fail to form sufficient complexes even where deterministic dose-response is favorable, and that volume, thresholds, completion rates, and breakup rates change the reliable dose range.
- **Caveat:** The findings come from minimal deterministic/stochastic models and a catalytic extension; no experimental system or clinical outcomes are reported in the abstract.
- **Announcement type:** New submission, cross-listed in the 2026-11-26 announcement batch.
- **Themes:** Biochemistry & proteins; Molecular & cell biology; Quantitative methods

### 5. [DDxBasis: Explaining Frozen Foundation Encoder-based Medical Classification by Exact Differential Diagnosis](https://arxiv.org/abs/2611.33358)
- **Abstract:** DDxBasis decomposes frozen-image-encoder classifications into diagnosis contrasts and case findings, with tests across five medical-image datasets.
- **Authors:** Luojie Huang, Gregory N. McKay, Nicholas J. Durr
- **arXiv:** `2611.33358v1` (published 2026-11-24 19:46:14 UTC; categories: `cs.CV` (primary), `q-bio.QM`)
- **Evidence for ranking:** No candidate-level score or attention counts were present in the supplied signals file (pool size 0); included as a biomedical methods paper cross-listed to quantitative biology, not as a popularity leader.
- **Claimed contribution:** The authors report exact concept-level decompositions of model decisions and performance competitive with published domain-specific methods across five datasets; they also report recovering label-free structure and exposing planted and real shortcuts.
- **Caveat:** These are retrospective model and dataset results, not evidence of clinical utility or prospective performance; dataset composition and external-site validation need scrutiny.
- **Announcement type:** New submission, cross-listed in the 2026-11-26 announcement batch (original v1 date: 2026-11-24).
- **Themes:** Biomedical & translational medicine; Bioinformatics & sequence analysis; Quantitative methods

## Trending Research Themes

- **Molecular design and interaction models:** KnitNet addresses computational RNA inverse design; Li and Chou model DNA–protein binding kinetics; Agrawal studies stochastic reliability in ternary-complex formation. Across this small selection, the common thread is algorithmic or mathematical treatment of molecular structure and interactions—not a field-wide shift or a shared experimental validation.
- **Cell-resolved spatial expression:** SCATTER targets the distinction between changing cell proportions and changing expression within a cell type. It is the sole selected spatial-omics paper, so it is a specific method signal rather than evidence of a broad trend.
- **More interpretable biomedical prediction:** DDxBasis structures image-classifier explanations as differential diagnoses. It is also a single-paper signal and remains a retrospective computational evaluation.

## Open Problems and Research Directions

- **RNA design to experimental function (KnitNet):** Test designed sequences with orthogonal structure assays and functional readouts, including sequences outside the five reported benchmark families; compare compute-matched search and generator baselines.
- **Spatial expression validation (SCATTER):** Evaluate on independent, multi-platform tissues with cell-type-specific measurements not used to construct pseudo-spots, and report calibration and failure modes under reference-cell mismatch.
- **Binding-model generalization (Li & Chou; Agrawal):** Measure conformational switching and complex-formation reliability across protein footprints, concentrations, and reaction volumes; compare observed distributions with the models’ predictions rather than only mean dose-response curves.
- **Explanations under clinical shift (DDxBasis):** Use external-site and prospective image cohorts with blinded expert assessment, and test whether the proposed contrasts remain faithful when acquisition protocols and disease prevalence change. This is a research direction, not clinical advice.

## Takeaway

The selected batch is strongest in computational and mathematical methods for RNA design, molecular binding, and cell-resolved expression, with one interpretable medical-imaging method. The supplied attention collector did not return paper-level candidates, and several listed papers’ submission timestamps predate its stated window; these results should be read as relevance-ranked notable papers, not measured arXiv trends.

## Method and sources

- **Window:** Daily. The supplied signal manifest specifies 2026-11-25 19:00:00–2026-11-26 19:00:00 UTC, with its arXiv announcement at 2026-11-27 01:00:00 UTC. Snapshot: 2026-11-27 03:09:40 UTC. The official Quantitative Biology page says “new listings for Thursday, 26 November 2026” and shows 14 new submissions, 11 cross-submissions, and 20 replacements (45 entries total).
- **Window/listing discrepancy:** The signal manifest reports `arxiv.status=ok, count=0` and `pool_size=0`, while the official category listing contains 45 entries. The five selected arXiv records show v1 dates from 2026-11-24 to 2026-11-25, before the manifest’s 2026-11-25 19:00 UTC start. To honor “today’s” latest batch, selection was made from the official 26 November listing and the discrepancy is disclosed; the collector’s date window could not be independently reconciled with that listing.
- **Configured categories:** `q-bio.BM`, `q-bio.GN`, `q-bio.MN`, `q-bio.SC`, `q-bio.CB`, `q-bio.TO`, `q-bio.QM`, `cs.BI`, `physics.med-ph`.
- **Attention evidence:** Supplied signal file `/home/yizhuan/.research/bio/daily/arxiv-trending-bio-daily-2026-11-27.signals.json`: arXiv 0 candidates; candidate pool 0; `with_attention=0`; Hugging Face status OK (124 records), Hacker News OK (16), arXiv lookup OK (139), Semantic Scholar OK (0). These are source-level counts, not per-paper scores. No candidate-level HF, HN, Semantic Scholar, or other attention values were available for these papers. Signal weights were HF upvotes 3.0, HN points 1.5, HN comments 1.0, citations 2.0, influential citations 1.0, code stars 0.5, and cross-listings 0.25; no numeric ranking score was applied because the candidate array was empty. A missing score is not evidence of unimportance.
- **Ranking:** Relevance-ranked notable papers rather than inferred popularity: direct fit to molecular/biomedical scope first, then the specificity of the abstract’s reported method and evidence. Recency was not used to imply attention.
- **Primary sources:** [Quantitative Biology announcement listing](https://arxiv.org/list/q-bio/new); verified arXiv abstract pages: [2611.33812](https://arxiv.org/abs/2611.33812), [2611.34798](https://arxiv.org/abs/2611.34798), [2611.33740](https://arxiv.org/abs/2611.33740), [2611.33753](https://arxiv.org/abs/2611.33753), [2611.33358](https://arxiv.org/abs/2611.33358). Claims are attributed to the preprint abstracts; computational predictions, modeling, and retrospective dataset results are not presented as clinical or experimental validation.
