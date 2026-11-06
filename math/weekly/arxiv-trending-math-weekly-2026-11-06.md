# Mathematics arXiv weekly report — 31 Oct–6 Nov 2026

Mathematics (math), through the Thu, 5 Nov 2026 announcement batch: 12 notable recent papers. The clearest pattern is author-reported conjecture resolutions and sharp boundary results, spanning group theory, algebraic combinatorics, operator theory, and geometric analysis. Spoken agenda: counterexamples and formal proofs first, then sharp estimates and geometric constructions. This is an inferred notable-paper ranking, not an official arXiv trending chart; citation evidence is too sparse to measure popularity reliably.

## Top papers (ranked)

### 1. [Kaplansky's conjectures fail for torsion-free hyperbolic groups in positive characteristic](https://arxiv.org/abs/2611.04599)
- **Abstract:** The authors construct, for every prime characteristic, a finitely presented torsion-free word-hyperbolic group whose group algebra has a one-sided inverse, yielding counterexamples to all four Kaplansky conjectures in positive characteristic.
- **Authors:** Nidhal Mghirbi, Seth Douglas
- **arXiv:** `2611.04599v1` (published 2026-11-03T09:53:55Z; categories: `math.GR`, `math.RA`)
- **Evidence for ranking:** A concrete counterexample to four longstanding group-ring conjectures, across group theory and ring theory; the arXiv comment links a Lean 4 formalization of the main theorem, and the authors' public project contains the formalization.
- **Claimed result:** The authors prove that for every prime p there is such a group G and a,b in F_p[G] with ab=1 but ba≠1; they derive failure of direct finiteness, the idempotent, zero-divisor, and unit conjectures over every field of characteristic p.
- **Assumptions and setting:** The counterexamples are torsion-free word-hyperbolic groups with finite two-dimensional classifying spaces; the construction is characteristic-dependent.
- **Caveat:** The result is for positive characteristic. The authors state that direct finiteness and the idempotent conjecture hold in characteristic zero for torsion-free hyperbolic groups, while the unit and zero-divisor cases remain open; their construction also rules out one proposed route to characteristic-zero cancellation.
- **Announcement type:** new submission, Wed, 4 Nov 2026 announcement batch
- **Themes:** Algebra & number theory; Geometry & topology

### 2. [A proof of the sharpness conjectures for all saturated fusion systems](https://arxiv.org/abs/2611.02043)
- **Abstract:** For every saturated fusion system over a finite p-group, the authors prove vanishing of positive-degree higher limits for the contravariant part of every Mackey functor over the p-local integers, implying sharp subgroup and normaliser decompositions.
- **Authors:** Baoyu Zhang, Shengmin Zhang
- **arXiv:** `2611.02043v1` (published 2026-11-01T16:42:53Z; categories: `math.GR`, `math.AT`, `math.CT`, `math.RT`)
- **Evidence for ranking:** Resolves named sharpness conjectures and an open question, with relevance across four mathematical categories. The arXiv comment reports unconditional Lean and Rocq formalizations.
- **Claimed result:** The authors prove that the positive-degree higher limits vanish for every Mackey functor over Z_(p), establishing sharpness of the subgroup and normaliser decompositions for every p-local finite group.
- **Assumptions and setting:** The category is a saturated fusion system over a finite p-group; coefficients are Mackey functors over the localization Z_(p), and the higher limits are taken over the centric orbit category.
- **Caveat:** This is a theorem about the stated centric-orbit-category higher limits and coefficient systems; it is not a classification of finite groups. The formalizations are reported by the authors and were not independently audited for this report.
- **Announcement type:** new submission, Tue, 3 Nov 2026 announcement batch
- **Themes:** Algebra & number theory; Geometry & topology

### 3. [Multivariate diagonal harmonics: character polynomials and proofs of two conjectures of Bergeron](https://arxiv.org/abs/2611.00629)
- **Abstract:** The paper proves Bergeron's Hook-Components and Coefficient-Length conjectures for diagonal harmonics and derives character and dimension formulas, stability thresholds, and related results for several algebraic models.
- **Authors:** Eren Ercan
- **arXiv:** `2611.00629v1` (published 2026-10-31T04:54:46Z; categories: `math.CO`)
- **Evidence for ranking:** Two named conjectures are proved, alongside answers to character and dimension questions and explicit sharp stability ranges.
- **Claimed result:** The author proves the hook-component and coefficient-length identities for the Vandermonde polarization module and full diagonal harmonics, and gives character/dimension polynomials in the stated degree range.
- **Assumptions and setting:** The principal character-polynomial result assumes degree D≥3 and n≥max(D,2D−6); other theorems in the paper have their own specified ranges. The Schur presentations and resolutions are over characteristic-zero augmented commutative algebras.
- **Caveat:** The abstract reports the fully graded sign component of the t=0, (1,2)-superspace Theta conjecture, not the full Theta conjecture in all components or parameters.
- **Announcement type:** new submission, Tue, 3 Nov 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Algebra & number theory

### 4. [A general framework for universal bounds on the analytic functional calculus](https://arxiv.org/abs/2611.01503)
- **Abstract:** The authors give a flexible Hilbert-space method for dimension-independent bounds on matrix-valued analytic functional calculus and apply it to spectral sets, sectors, and analytic Jordan domains.
- **Authors:** Mihai Putinar, Georgios Tsikalas
- **arXiv:** `2611.01503v1` (published 2026-11-01T03:36:51Z; categories: `math.FA`, `math.CA`, `math.CV`, `math.OA`, `math.SP`)
- **Evidence for ranking:** Five math categories, a reusable framework, and explicit sharp or improved bounds including a sharp right-angle sector result.
- **Claimed result:** The authors establish complete functional-calculus bounds under accretivity and multiplier hypotheses, including improved sector bounds and bounds on regular real-analytic Jordan domains; the right-angle sector case is claimed optimal.
- **Assumptions and setting:** The bound depends on an auxiliary holomorphic-function Hilbert space meeting the stated accretivity and multiplier conditions. Applications assume spectral-set disks, numerical range in a sector, or a regular real-analytic boundary with a lower bound on its double-layer potential.
- **Caveat:** These are conditional bounds for specified operator/domain classes, not a universal bound for arbitrary operators and arbitrary spectral sets.
- **Announcement type:** new submission, Tue, 3 Nov 2026 announcement batch
- **Themes:** Analysis & PDE

### 5. [Transfer of similarity to Hilbert space contractions through inner functions: a proof of Douglas's conjecture](https://arxiv.org/abs/2611.01703)
- **Abstract:** For a bounded Hilbert-space operator, the author proves that similarity to a contraction is preserved and reflected by applying a nonconstant inner function when the operator's spectrum avoids the function's reflected singularities.
- **Authors:** Catalin Badea
- **arXiv:** `2611.01703v1` (published 2026-11-01T08:44:04Z; categories: `math.FA`, `math.CV`, `math.OA`)
- **Evidence for ranking:** A named conjecture is settled, with extensions to infinite Blaschke products, commuting tuples, and weighted resolvents across three math categories.
- **Claimed result:** The author proves Douglas's conjecture for finite or infinite Blaschke products under spectral separation, and extends the equivalence to inner functions whose reflected singularity set avoids the spectrum.
- **Assumptions and setting:** A is a bounded operator on a Hilbert space; the central hypothesis is that its spectrum misses the closure of the poles of the Blaschke product. The broader inner-function version excludes the reflected singularity set.
- **Caveat:** The spectral-separation condition is essential to the stated theorem; the paper gives examples showing that several proposed weaker substitutes do not suffice, even for Ritt operators.
- **Announcement type:** new submission, Tue, 3 Nov 2026 announcement batch
- **Themes:** Analysis & PDE

### 6. [The covering radius of the first-order Reed-Muller code in nine variables is 242](https://arxiv.org/abs/2611.00890)
- **Abstract:** The author proves that the binary first-order Reed-Muller code RM(1,9) has covering radius 242, equivalently that the maximum nonlinearity of a Boolean function of nine variables is 242.
- **Authors:** Yi Li
- **arXiv:** `2611.00890v1` (published 2026-10-31T12:48:41Z; categories: `math.NT`, `cs.IT`, `math.CO`)
- **Evidence for ranking:** An exact parameter is determined across coding theory and combinatorics, using a rigidity theorem and finite spectral/computational exclusions.
- **Claimed result:** The author proves the exact covering radius by ruling out nonlinearities 243 and 244, together with the known construction attaining 242.
- **Assumptions and setting:** The result concerns the binary first-order Reed-Muller code in nine variables; the proof uses exact Walsh identities, classification of alternating trilinear forms, and exhaustive finite enumerations.
- **Caveat:** This is a specific code-parameter result, and the exclusion step depends on finite exact computations whose completeness is part of the proof burden; it does not establish covering radii in general dimensions.
- **Announcement type:** new submission, Tue, 3 Nov 2026 announcement batch
- **Themes:** Combinatorics & discrete mathematics; Numerical analysis & computation

### 7. [A height transportation approach to the quantitative Prékopa--Leindler inequality](https://arxiv.org/abs/2611.03295)
- **Abstract:** The authors provide a height-transport proof of sharp stability for Prékopa--Leindler and derive optimal-exponent stability consequences for log-Sobolev and Talagrand inequalities.
- **Authors:** João Miguel Machado, João P. G. Ramos
- **arXiv:** `2611.03295v1` (published 2026-11-02T15:32:14Z; categories: `math.FA`, `math.AP`, `math.PR`)
- **Evidence for ranking:** Cross-listed in analysis, PDE, and probability; it supplies a simpler proof of sharp stability and a sharp dependence on τ in a log-concave-input case.
- **Claimed result:** The authors prove sharp stability for Prékopa--Leindler with improved dependence on τ=min(λ,1−λ) when one input is log-concave, and obtain optimal-exponent stability results for the Bakry--Émery log-Sobolev and Talagrand inequalities.
- **Assumptions and setting:** The sharp τ-dependence application assumes one input is logarithmically concave; the paper's stability distances and inequality hypotheses are those of the cited Prékopa--Leindler, log-Sobolev, and Talagrand settings.
- **Caveat:** The authors show that the L1 distance in these stability results cannot generally be replaced by an Lp distance for p>1; stronger metric conclusions therefore need additional hypotheses.
- **Announcement type:** new submission, Tue, 3 Nov 2026 announcement batch
- **Themes:** Analysis & PDE; Probability & statistics

### 8. [Pseudo-Einstein Structures on Links of Isolated Singularities](https://arxiv.org/abs/2611.04851)
- **Abstract:** The authors construct links violating a pseudo-Einstein existence conjecture and characterize the condition for links of isolated log-canonical singularities in complex dimension at least three.
- **Authors:** Yoshinori Gongyo, Kengo Hirachi, Shuya Matsumoto, Yuya Takeuchi
- **arXiv:** `2611.04851v1` (published 2026-11-03T13:15:23Z; categories: `math.DG`, `math.AG`, `math.CV`)
- **Evidence for ranking:** A concrete counterexample and a positive characterization bridge CR geometry, algebraic geometry, and complex analysis.
- **Claimed result:** The authors construct counterexamples to Jack Lee's conjecture on links of isolated singularities in every odd dimension at least three; for isolated log-canonical singularities of complex dimension at least three, they prove equivalence among the real Chern-class condition, Q-Cartierness, log-canonicity, and existence of a pseudo-Einstein structure.
- **Assumptions and setting:** The setting is compact strictly pseudoconvex CR manifolds arising as links of isolated algebraic singularities, with the characterization restricted to log-canonical singularities of complex dimension at least three.
- **Caveat:** The arXiv abstract says the initial proof versions used AI assistance and were subsequently revised and verified by the authors; this report has not independently checked the proofs.
- **Announcement type:** new submission, Wed, 4 Nov 2026 announcement batch
- **Themes:** Geometry & topology; Analysis & PDE

### 9. [Branched Covers and Fiberwise Degeneration along Weak Kähler Geodesics](https://arxiv.org/abs/2611.07451)
- **Abstract:** The authors construct weak Kähler geodesics with prescribed fiberwise degeneracy, disproving a uniform nondegeneracy expectation for Monge--Ampère approximations and producing higher-dimensional rank-drop examples.
- **Authors:** Wenjiong Guo, Zekun Sheng
- **arXiv:** `2611.07451v1` (published 2026-11-05T04:53:47Z; categories: `math.DG`)
- **Evidence for ranking:** The authors tie an explicit branched-cover construction to a named AIMPL open problem, independently confirmed by the problem listing; the contribution is an explicit construction in Kähler geometry.
- **Claimed result:** The authors answer AIMPL Problem 2.5 in the negative, realizing fiber zeros of order 2m−2 on compact connected Riemann surfaces and rank drops along smooth hypersurfaces in higher-dimensional product examples.
- **Assumptions and setting:** The construction starts on the projective line with smooth endpoint potentials, extends to compact connected Riemann surfaces with prescribed Kähler form, and uses branched covers and products for the stated examples.
- **Caveat:** These are constructed examples and do not classify degeneracy for arbitrary weak geodesics or endpoint data.
- **Announcement type:** new submission; its batch was not yet present in the latest posted listing at the 2026-11-06T02:26:01Z snapshot
- **Themes:** Geometry & topology; Analysis & PDE

### 10. [Cells, cacti, and the asymptotic algebra](https://arxiv.org/abs/2611.07439)
- **Abstract:** The authors realize a cactus-group action on the asymptotic algebra of a Hecke algebra, proving a conjecture of Rouquier and White under Lusztig's conjectures P1--P15.
- **Authors:** F. Dos Santos, J. Parkinson
- **arXiv:** `2611.07439v1` (published 2026-11-05T04:38:37Z; categories: `math.RT`)
- **Evidence for ranking:** Resolves a named conjecture in representation theory, with an explicit conditional extension to unequal parameters.
- **Claimed result:** The authors prove that the Losev--Bonnafé cactus-group action on a Coxeter group is realized on the Hecke algebra's asymptotic algebra, conditional on P1--P15 in the unequal-parameter setting.
- **Assumptions and setting:** The result concerns Coxeter groups and Hecke algebras; Lusztig's P1--P15 are assumed for general parameters and are known in the equal-parameter case.
- **Caveat:** The unequal-parameter theorem is conditional; the stated assumptions are known in the equal-parameter case but not asserted here for all unequal parameters.
- **Announcement type:** new submission; its batch was not yet present in the latest posted listing at the 2026-11-06T02:26:01Z snapshot
- **Themes:** Algebra & number theory

### 11. [Holomorphic sectional curvature and the Calabi operator on Kähler C-spaces](https://arxiv.org/abs/2611.07402)
- **Abstract:** The authors establish curvature and spectral bounds for homogeneous Kähler metrics on generalized flag manifolds, prove conjectures of Ni and Zheng, and give nonhomogeneous examples with related spectral properties.
- **Authors:** Xiaolong Li, Peter Petersen
- **arXiv:** `2611.07402v1` (published 2026-11-05T03:54:55Z; categories: `math.DG`)
- **Evidence for ranking:** Includes a sharp spectral bound and explicit counterexamples to a homogeneity characterization, linking Kähler curvature and operator spectrum.
- **Claimed result:** The authors prove positivity of holomorphic sectional curvature for every homogeneous Kähler metric on a generalized flag manifold, bound the Calabi operator spectrum for the normalized homogeneous Kähler--Einstein metric, prove conjectures of Ni and Zheng, and construct nonhomogeneous Kähler--Einstein examples.
- **Assumptions and setting:** The spectral interval and sharp upper bound are for the standard homogeneous Kähler--Einstein metric on generalized flag manifolds with Einstein constant 2; the nonhomogeneous examples are in dimensions 4, 5, and 13.
- **Caveat:** The sharp spectral theorem is tied to the stated homogeneous setting; the examples show the spectral conditions do not characterize homogeneity.
- **Announcement type:** new submission; its batch was not yet present in the latest posted listing at the 2026-11-06T02:26:01Z snapshot
- **Themes:** Geometry & topology; Analysis & PDE

### 12. [Higher Noncommutative Motives and Higher K-theory](https://arxiv.org/abs/2611.07262)
- **Abstract:** The author constructs higher additive motives for stable (∞,n)-categories, with universal properties and higher K-theory as their iterated Hom objects.
- **Authors:** Hisato Matsukawa
- **arXiv:** `2611.07262v1` (published 2026-11-05T00:30:16Z; categories: `math.KT`, `math.AT`, `math.CT`)
- **Evidence for ranking:** A broad categorical construction cross-listed in K-theory, algebraic topology, and category theory, with two constructions and explicit recovery of classical and secondary theories.
- **Claimed result:** The author defines higher additive noncommutative motives for stable (∞,n)-categories, proves a universal property, gives presheaf-localization and weighted Waldhausen S-construction models, and identifies their Hom objects with iterated K-theoretic information.
- **Assumptions and setting:** The construction is for stable (∞,n)-categories with the paper's notion of exact sequences; the results extend additive and secondary theories rather than claiming a classification of all noncommutative invariants.
- **Caveat:** The abstract describes a framework and its universal property; it does not by itself establish computational consequences for particular categories beyond the stated recoveries.
- **Announcement type:** new submission; its batch was not yet present in the latest posted listing at the 2026-11-06T02:26:01Z snapshot
- **Themes:** Algebra & number theory; Geometry & topology

## Trending Research Themes

- **Conjecture resolution and explicit counterexamples:** Zhang and Zhang settle sharpness questions for saturated fusion systems; Mghirbi and Douglas give characteristic-specific counterexamples for group-ring conjectures; Ercan proves two diagonal-harmonics conjectures; and Dos Santos and Parkinson resolve a cactus-group conjecture subject to stated hypotheses. These are separate results, not evidence of a shared proof technique.
- **Operator theory and functional calculus:** Putinar and Tsikalas develop dimension-independent analytic-calculus bounds, while Badea settles Douglas's similarity conjecture through inner functions. Both concern operator-theoretic structure, but the arguments and hypotheses differ.
- **Geometry, curvature, and degeneration:** Guo and Sheng construct controlled weak-geodesic degenerations; Gongyo et al. study pseudo-Einstein structures on singularity links; Li and Petersen analyze curvature and the Calabi operator on Kähler flag manifolds. This is a set of distinct geometric signals, not a field-wide shift.
- **Sharp quantitative and exact results:** Li determines one Reed--Muller covering radius exactly, and Machado and Ramos obtain sharp stability dependence for Prékopa--Leindler in a log-concave-input setting. Their methods are unrelated; the common feature is an explicit sharp endpoint.
- **Higher categorical invariants:** Matsukawa's higher motives connect stable (∞,n)-categories to higher K-theory, while the fusion-system and Hecke-algebra papers also use categorical structures in different settings. The week's sample suggests active categorical work, not a single shared technique.

## Open Problems and Research Directions

- **Author-stated open cases — Mghirbi and Douglas, [2611.04599](https://arxiv.org/abs/2611.04599):** their paper states that the unit and zero-divisor conjectures remain open for torsion-free hyperbolic groups in characteristic zero, while direct finiteness and idempotent statements are known there. A follow-up direction is to test constructions not subject to the paper's characteristic-zero obstruction on vertex-type cancellations.
- **Conditional hypothesis — Dos Santos and Parkinson, [2611.07439](https://arxiv.org/abs/2611.07439):** the unequal-parameter result assumes Lusztig's P1--P15. Establishing the relevant cases, or weakening the required hypotheses, would test how far the cactus action theorem extends beyond equal parameters.
- **Scope left open — Ercan, [2611.00629](https://arxiv.org/abs/2611.00629):** the paper proves one fully graded sign component of the t=0, (1,2)-superspace Theta conjecture. Extending the transfer to other components or parameter regimes is a concrete next test, not a claim that those cases are tractable.
- **Geometric generalization — Guo and Sheng, [2611.07451](https://arxiv.org/abs/2611.07451):** the construction realizes specific zero orders and product rank drops. One can ask which degeneracy loci and orders are possible for broader endpoint data and on general compact Kähler manifolds.
- **Metric limitation — Machado and Ramos, [2611.03295](https://arxiv.org/abs/2611.03295):** the authors show that the L1 distance cannot generally be upgraded to Lp for p>1. A follow-up is to identify additional structural assumptions on the inputs that permit stronger-distance stability, or to delineate sharp subclasses where such improvement is impossible.
- **Singularity scope — Gongyo et al., [2611.04851](https://arxiv.org/abs/2611.04851):** their characterization is for links of log-canonical singularities in complex dimension at least three, alongside counterexamples on links more broadly. Extending the criterion to other singularity classes or to general strictly pseudoconvex CR manifolds would test the boundary of the result.

## Takeaway

This week's notable set contains several concrete conjecture answers, formalized or exact-computation-backed claims, and sharp geometric or analytic bounds. These remain preprint claims, and the characteristic-specific group-ring counterexamples and conditional unequal-parameter theorem merit specialist scrutiny.

## Method and sources

- **Window:** inclusive calendar dates 2026-10-31 through 2026-11-06, with the snapshot cutoff at 2026-11-06T02:26:01Z. The latest posted arXiv mathematics announcement batch visible at that time was Thu, 5 Nov 2026. The four papers dated 5 Nov UTC below were available on their abstract pages but had not yet appeared in that posted listing.
- **Coverage:** arXiv Mathematics archive and its `math.*` subject classes, retaining adjacent-category papers when cross-listed in math. A machine-readable query over the submitted-date and last-updated-date window returned 1,694 records in one page; 34 were revisions, and none of the selected papers was a revision. Ranking used explicit theorem/construction claims, cross-listing, formal or computational artifacts, and available expert/problem-list corroboration, with recency only a tie-breaker.
- **Attention evidence:** Semantic Scholar was checked for eight selected papers; each had 0 current citations at the snapshot (not zero gains during this week). Citation records for the four newest selections were unavailable. No reliable age-normalized citation momentum or independent seminar-discussion signal was available, so the ordering is labeled notable rather than a popularity ranking.
- **Reading:** every selected arXiv abstract page was checked. The introductions and main-result statements were also inspected for the first three papers; proofs were not independently verified. The Kähler-geodesic open problem was checked against the AIMPL problem listing.
- **Sources:** [arXiv Mathematics recent listing](https://arxiv.org/list/math/recent), [arXiv API](https://export.arxiv.org/api/query), individual abstract pages linked above, [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1), and [AIMPL Problem 2.5](http://aimpl.org/nonlinpdegeom/2/).
