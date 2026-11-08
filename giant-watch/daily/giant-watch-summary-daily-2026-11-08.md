# Giant Watch Summary - Daily - 2026-11-08

## Headline

OpenAI closed the first $11B tranche of a round at a $1.25T valuation, while Google's Gemini Omni 1.2 Flash took the top spot on both Arena video leaderboards. The day's episode is capital and product cadence running in parallel, with Chinese open-weight vendors winning share on price rather than revenue.

## Top Developments

### 1. OpenAI closes first $11B tranche at $1.25T valuation (OpenAI)
OpenAI completed the first tranche of a new funding round, raising about $11 billion at a $1.25 trillion valuation, with the remainder expected in coming weeks and the total potentially reaching $20 billion. CFO Sarah Friar said continued data-center investment is needed to meet customer demand and hinted at further fundraising.
Why it matters: The largest single capital event in the window, and the clearest signal that frontier-lab spending plans remain tied to data-center buildout rather than near-term profitability.
Refs: https://ai.synthepulse.app/daily/2026-11-06, https://www.dolc.de/thread-2450010-1-1.html

### 2. Google DeepMind releases Gemini Omni 1.2 Flash video model (Google)
Google DeepMind released Gemini Omni 1.2 Flash, a video generation model that ranks first on both Arena's text-to-video and image-to-video leaderboards. It extends clip length from 10 to 15 seconds with 3-15 second options, adds multi-turn conversational editing, and is 30% cheaper than its predecessor at $1.05 for a 15-second 720p video, available via the Gemini API, Google Cloud and Google AI Studio. A separate Chinese-language roundup put 720p generation cost at $0.07 per second.
Why it matters: A concrete frontier release with leaderboard placement and a price cut, putting pressure on rival video models on both quality and cost.
Refs: https://ai.synthepulse.app/daily/2026-11-06, https://www.dolc.de/thread-2450010-1-1.html

### 3. Meta upgrades Muse and Meta AI models, opens Active Memory and Active Focus to all users (Meta)
Meta upgraded the models behind its Muse agent and Meta AI apps, making Active Memory and Active Focus available to all users. The specialized models are claimed to be 2.4x less likely to forget critical information and 67% better at self-correcting and completing everyday tasks, alongside a 9% rise in Meta's Personal Superintelligence Index and a 14% rise in Active Memory Eval. A separate account said the new models are trained using the frontier Muse Wonder model and report 90% correct use of key context versus 76% for the prior model.
Why it matters: Meta is pushing frontier-derived behavior to a free consumer tier, a distribution play that differs from per-seat enterprise pricing at OpenAI and Anthropic.
Refs: https://ai.synthepulse.app/daily/2026-11-06, https://juejin.cn/post/7705330413947273231

### 4. Musk says Grok Bot token-efficiency fixes underway after usage complaints (xAI)
Elon Musk posted on Nov. 8 that "Grok Bot fixes for improved token efficiency and smarter behavior are underway," after a subscriber said his $200 plan lasted 14 hours of moderate use this week versus seven days the prior week. Musk gave no timeline and did not say whether weekly limits or tier prices would change. On Nov. 1 he had said Grok Bot serving costs were "unsustainably high relative to revenue." xAI lists tiers at $30 Premium, $100 Super (3.5x usage) and $200 Ultra (12x usage) per month.
Why it matters: The first public admission-and-response cycle on agent inference economics at a major lab, and a test case for how subscription quotas get redesigned as agent usage scales.
Refs: https://www.aichatdaily.com/ai-news/musk-says-grok-bot-token-efficiency-fixes-underway-after, https://teslanorth.com/2026/11/08/grok-bot-usage-limits-musk/, https://finance.biggo.com/news/e0e37da1-df2a-4131-b52c-6644b41c44ff

### 5. Revolut moves ~2,000 engineers from Claude Code and Codex to self-hosted GLM 5.3 (GLM, Anthropic, OpenAI)
Revolut shifted roughly 2,000 engineers from Anthropic's Claude Code and OpenAI's Codex to a self-hosted deployment of Z.ai's open-weight GLM 5.3, cutting AI-assisted coding costs by about 90% to roughly $0.30 per million tokens. The deployment runs on 56 Nvidia B200 GPUs on US infrastructure. David Abitbol, who leads AI operations at Revolut, said out-of-box latency of about 14 seconds was tuned down to 1.6 seconds, with coding time down about 60% and lead time down about 70%. GLM handles text coding only; image work routes to Google's Gemini, and Claude Code and Codex remain available as fallbacks.
Why it matters: The most concrete enterprise proof point in the window that self-hosted open-weight models can displace per-seat frontier subscriptions at scale, with named infrastructure and cost figures.
Refs: https://opentools.ai/news/revolut-drops-claude-for-chinese-glm-model-cuts-coding-costs-90-percent

### 6. Menlo Ventures: Chinese models take 89% of enterprise open-source AI spend (Kimi, DeepSeek, GLM, Meta, Anthropic, OpenAI)
Menlo Ventures' "2026 Corporate AI Status" report, released Nov. 4, found Chinese models accounted for 89% of corporate spending on open-source AI models: Moonshot AI's Kimi at 61%, DeepSeek at 15%, Z.ai's GLM at 11%, and Meta's Llama at 7%. In paid enterprise AI, Anthropic held 55% and OpenAI 31%, together 86%. Token volume for open-source models rose 22.5x in a year while their share of total corporate AI spending fell from 6% to 4%; EpochAI estimated combined revenue of six major Chinese AI firms at $11 billion, against an Anthropic annualized revenue estimate of $65 billion.
Why it matters: Quantifies the split between open-weight adoption and monetization, and frames the strategic risk that Chinese labs win usage without recovering development costs.
Refs: https://chosun-chosun-prod.cdn.arcpublishing.com/english/industry-en/2026/11/09/VU5YD3CLFBANBAQRGV42XOOLBI/, https://locdd.com/t/topic/107721

### 7. Vals tests put DeepSeek V4.1 Flash close to OpenAI's gated Daybreak on cyber tasks (DeepSeek, OpenAI, Kimi, GLM, Meta, xAI)
Vals AI's CyberOffense leaderboard, updated Oct. 23 and reported by WIRED on Nov. 6 and The Decoder on Nov. 7, had agents attempt multi-step intrusions on mock corporate networks. OpenAI's GPT-6 Sol Daybreak, available only to trusted partners, completed about 81% of tasks versus about 73% for open-weight DeepSeek V4.1 Flash; DeepSeek was slightly ahead on the Nova range (16.3/21 vs 15.7/21) and behind on Lighthouse (21/31 vs 27/31). Token costs were $17-$46 for GPT-6-Sol against $2-$3 for DeepSeek per WIRED, and about $22 versus under $3 per the Vals page. Meta Wonder scored 7/21 on Nova but 28/31 on Lighthouse; GLM 5.3 Flash scored lowest on both; no model finished the final Lighthouse objectives.
Why it matters: The strongest evidence yet that downloadable weights are closing on gated frontier cyber capability at a fraction of the cost, which undercuts limited-release programs as a safety buffer.
Refs: https://debugged-pro.com/blog/open-weight-ai-vals-deepseek-hacking-agency-guide-india-usa, https://www.threads.com/@whaleagent/post/DfevfYaEwD9/media

### 8. China Mobile Cloud and Zhipu sign cooperation agreement; GLM models to join MaaS platform (GLM)
On Nov. 6, China Mobile Cloud and Beijing Zhipu Huazhang Technology signed a cooperation agreement covering token technology innovation, model services, product development and industry solutions. The two will work on domestic computing-power adaptation and model optimization, jointly establish a Token Development Center, and integrate Zhipu's GLM series into China Mobile's MaaS platform. They will also co-build AI Coding products and target finance and government with combined computing-power, model and application offerings.
Why it matters: A state-carrier distribution channel for GLM, extending the model family from developer APIs into regulated industry verticals.
Refs: https://stock.10jqka.com.cn/20261108/c681582072.shtml, https://www.kucoin.com/news/flash/china-mobile-cloud-and-zhipu-sign-cooperation-agreement-for-domestic-computing-power-and-ai-services?lang=en_US&

### 9. Leaked Moonshot notes outline Kimi K3 Flash, K3.5 and K4 roadmap (Kimi, DeepSeek)
A post citing leaked notes from a Moonshot investor call and Chinese tech reports described a lineup: Kimi K3 Flash before the end of 2026 to replace Kimi K2.8 and compete with DeepSeek V4.1 Flash; Kimi K3.5 around Q1 2027 at near 3 trillion parameters trained on 10 trillion post-training tokens, aimed at self-distillation and compression to cut thinking-token costs; and Kimi K4 in Q2 or Q3 2027 at 5.4 trillion parameters across H100, H200 and B200 clusters, roughly double K3.1 Pro, possibly with GPU rentals in Europe.
Why it matters: The only signal in the window on Moonshot's forward plan, and it points at inference-cost compression rather than raw scale as the near-term lever.
Refs: https://x.com/bebuu_ai/status/2119319459206934677

### 10. xAI enables invisible statistical watermarking by default on seven Grok API text models (xAI)
According to xAI developer documentation and developer media reports dated Nov. 7, xAI turned on invisible statistical watermarking by default for seven Grok API text models (grok-4.7, 4.6, 4.5, 4.3 and three grok-4.20 variants), covering plain text, structured output and tool-call parameters, with no code changes required. Each response indicates watermarking via an x-watermark response header. xAI's documentation cites compliance with the EU AI Act, whose Article 50(2) machine-readable marking deadline for systems already on market is Dec. 2, putting xAI about three weeks ahead.
Why it matters: Reported as the first time a major frontier vendor has made machine-readable content marking a default rather than an option, setting a de facto baseline for peers ahead of the EU deadline.
Refs: https://www.renrendaima.com/article/36221.html

## Cross-Org Themes

- Inference cost and quota economics are now the binding constraint on agent products, visible in xAI's Grok Bot fixes, Revolut's GLM migration and Meta's free-tier model strategy.
- Open-weight Chinese models are winning usage share and enterprise displacement while capturing little revenue, per Menlo Ventures and the Revolut case.

## Rumors and Unverified Claims

Leaked Moonshot investor-call notes describe Kimi K3 Flash before end-2026, Kimi K3.5 around Q1 2027 at near 3 trillion parameters trained on 10 trillion post-training tokens, and Kimi K4 in Q2-Q3 2027 at 5.4 trillion parameters with possible European GPU rentals; Moonshot has not confirmed any of this. Separately, xAI's default-on Grok API watermarking and its EU AI Act rationale rest on developer documentation and secondary developer-media reports rather than a primary xAI announcement in the supplied material, and the same source concedes the watermark may slightly affect token selection while also claiming no quality or speed impact, which has not been independently evaluated.

## Takeaway

The next evidence to watch is whether OpenAI closes the remainder of its round and at what final size, and whether other frontier vendors match xAI's default watermarking before the Dec. 2 EU deadline. For the open-weight story, the test is whether cheap self-hosted deployments translate into durable revenue for the labs that publish the weights.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
