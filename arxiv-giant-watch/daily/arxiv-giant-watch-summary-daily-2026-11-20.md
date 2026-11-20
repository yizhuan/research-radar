# arXiv Giant Watch - Daily - 2026-11-20

## Headline

The latest arXiv cycle surfaced production-scale agent engineering from Meta and an Anthropic safety study on prompt-conditioned false beliefs. Meta's papers report operational gains, while the Anthropic work explores a scalable way to construct model organisms and warns that training interventions can undermine evaluation reliability.

## Notable Papers

### 1. Cap-and-Track: Optimizing LLM Inference Request Dispatch Across Shifting Capacity

- arXiv: [2611.24891](https://arxiv.org/abs/2611.24891)
- Organizations: Meta
- Attribution: verified — author affiliations identify Meta.
- Problem: Fixed inference dispatch rates become miscalibrated as fleet capacity and request lengths change, creating idle capacity or excess queues.
- Method: A per-replica admission cap rejects work before long waits; a stateful dispatcher uses capacity refusals to probe and track the live ceiling, with durable priority queues for retries.
- Key result: In a same-traffic production A/B, the shaper served a classifier using 43% fewer H100s than its queued, fixed-rate predecessor. In steady-capacity replay, throughput was within 1% of an aggressively tuned fixed rate with roughly one-quarter its refusal share.
- Caveat: Lower-priority work waited longer at backfill peaks; the replay and the production A/B are different evaluations, and the headline resource saving is workload-specific.
- Why it matters: This is evidence that adaptive admission control can improve real inference utilization at large scale without relying on output-length forecasts or fleet-wide rate retuning.

### 2. MLE Agents: Autonomous ML Engineering in Large-scale Recommendation Systems

- arXiv: [2611.23910](https://arxiv.org/abs/2611.23910)
- Organizations: Meta
- Attribution: verified — the authors list Meta Platforms affiliations.
- Problem: Search-ranking improvements require slow cycles of coding, training, and evaluation; offline metrics may not predict online impact.
- Method: Human-on-the-loop agents propose code changes, launch training, inspect offline results, and decide which candidates merit review. The system uses parallel experiments and an objective calibrated against online outcomes.
- Key result: In one campaign, 325 of 1,097 completed candidates were accepted (29.6%); the best model increased search volume by 0.23% in a large-scale A/B test.
- Caveat: The 29.6% acceptance rate is compared with an earlier campaign that used a different objective and search constraint; the online lift is modest and specific to the reported ranking system.
- Why it matters: It moves agentic ML engineering from benchmark tasks into a live industrial recommender workflow, while retaining human control over objectives and final review.

### 3. Can you make models believe false facts in the prompt?

- arXiv: [2611.23938](https://arxiv.org/abs/2611.23938)
- Organizations: Anthropic
- Attribution: verified — the author record identifies Anthropic and the Anthropic Fellows Program.
- Problem: Synthetic-document fine-tuning can implant false beliefs, but traditionally requires separate training for each injected fact, limiting scale for alignment evaluations.
- Method: Prompt-conditioned synthetic-document fine-tuning trains one model on documents conditioned on facts supplied in a prompt; the authors assess belief depth on held-out facts and test a subsequent RL intervention.
- Key result: Belief depth on unseen facts scales roughly log-linearly with the number of training facts. RL that reduces verbal compliance with false prompt facts generalizes to held-out evaluations and approaches SDF on some measures.
- Caveat: Initial alignment-audit experiments were negative on the small models studied, and optimizing one belief-depth metric made that evaluation less trustworthy.
- Why it matters: The work offers a potentially cheaper way to construct model organisms for alignment research, while showing that the measurement procedure itself can be affected by training.

## Research Themes

- Production agent systems are increasingly built around feedback and live constraints: Meta's MLE agents iterate over model changes, while Cap-and-Track steers inference dispatch using observed capacity refusals.
- More capable or controllable agent behavior creates an oversight burden: Meta keeps engineers in the loop for consequential model changes, while Anthropic finds that prompt-conditioned training can alter both model beliefs and the reliability of evaluation signals.

## Takeaway

The strongest operational signal is Meta's use of agents and adaptive control inside production recommendation and inference systems, with measurable but workload-specific efficiency gains. The safety result is a reminder that evaluation quality must be checked alongside capability: training designed to shape behavior can also undermine the metrics used to assess it.

## Sources and Method

The automated arXiv API fetch returned HTTP 500 on retry, so this briefing was assembled from the linked arXiv abstract records and their author/affiliation metadata rather than the feed script. Papers were selected only where the arXiv record supported an organization attribution; title/abstract mentions alone were excluded. The daily watch reflects the latest indexed arXiv cycle available on 2026-11-20. No portfolio-shift claim is made because no prior-window comparison was established.
