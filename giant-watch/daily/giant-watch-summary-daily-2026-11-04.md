# Giant Watch Summary - Daily - 2026-11-04

## Headline

Revolut's self-hosting of Z.ai's GLM-5.3 for 2,000 engineers, cutting AI coding inference costs by about 90%, is the day's strongest concrete event. The episode's thesis is that open-weight economics and self-hosting are starting to displace frontier commercial APIs for high-volume coding work.

## Top Developments

### 1. Revolut self-hosts Z.ai's GLM-5.3, cutting AI coding inference costs about 90% (GLM)
Revolut moved its default coding workload for roughly 2,000 engineers to self-hosted open-weight GLM models from Z.ai (GLM-5.1, then GLM-5.3) on 56 NVIDIA B200 GPUs, reporting blended inference cost of about 30 cents per million tokens, roughly one-tenth of prior Anthropic and OpenAI spending. The company reported 70% better engineering lead times and 60% faster coding time, and said it still routes vision and other specialized work to Claude Code, Codex and Gemini.
Why it matters: A large fintech publicly quantifying a shift from frontier commercial APIs to self-hosted open weights is a concrete data point on cost-driven model substitution in production coding workloads.
Refs: https://techgig.com/news/ai/revolut-cuts-ai-coding-costs-by-90-per-cent-via-self-hosting-glm/135517042?utm_source=Mailer&utm_medium=ET_batch&utm_campaign=techgig_news_2026-11-04&dt=2026-11-04, https://news.lavx.hu/article/revolut-cuts-ai-coding-costs-90-by-self-hosting-chinese-model-glm

### 2. Huawei Cloud to retire openPangu-2.0 models from MaaS, pointing users to DeepSeek-V4.1-Flash and GLM-5.3 (GLM, DeepSeek)
Huawei Cloud will stop selling openPangu-2.0-Flash and openPangu-2.0-Pro on its MaaS platform on November 6 and take them offline November 30, recommending DeepSeek-V4.1-Flash-1017 and Zhipu's GLM-5.3 as replacements. The same bulletin schedules GLM-5.1 for retirement on November 16 with GLM-5.3 as successor, moves DeepSeek-V4-Flash users to V4.1-Flash, and retires Kimi-K2.6 on November 8.
Why it matters: A major Chinese cloud is steering hosted-model customers toward DeepSeek and GLM successors, showing rapid model turnover and consolidation of platform demand around a few open-weight families.
Refs: https://pandaily.com/huawei-cloud-maas-openpangu-2-0-flash-pro-offline-nov-30-deepseek-v4-1-flash-glm-5-3

### 3. DeepSeek engineer makes the open-source case for AGI at the Wuzhen summit (DeepSeek)
At the 2026 World Internet Conference Wuzhen summit, DeepSeek research engineer Gao Xi said the company chose open source to bring AGI sooner and framed DeepSeek's rival as time rather than other model companies. The report cited OpenRouter data that Chinese models' weekly token usage exceeded US models for 27 consecutive weeks, with DeepSeek ranked first among the top five models by weekly token volume.
Why it matters: A named DeepSeek engineer publicly articulating an open-source-first AGI strategy, backed by third-party token-usage rankings, is a concrete positioning statement from a leading Chinese lab.
Refs: http://big5.china.com.cn/gate/big5/news.china.com.cn/2026-11/04/content_118760744.shtml, https://www.kgi.com.hk/en/market-news-and-analysis/market-news/market-news-feed?id=6093149&iid=6c7889a28a4d4e238aae64f447146057&type=scnews

### 4. DeepSeek spotlights DSH 'creation mode' for natural-language plugin generation (DeepSeek)
DeepSeek published a video and prompts for DSH's creation mode, in which users describe an idea and an agent writes, packages and installs it as a DSH plugin; seven demos were released with bilingual prompts. Coverage notes the mode existed since August, that DeepSeek acknowledges it remains a developer preview with possible breaking changes, and that generated executable plugins raise permission and code-safety concerns.
Why it matters: DeepSeek is pushing plugin-level extensibility to users, a concrete step in its developer-ecosystem strategy, though the capability is still a preview with acknowledged security trade-offs.
Refs: https://news.pedaily.cn/202611/571302.shtml

### 5. OpenAI says GPT-6 Astra designed a hardware device in under a week (OpenAI)
The Decoder reported that OpenAI's hardware team used GPT-6 Astra to design a device for talking to the Codex coding agent in under a week, covering enclosure, PCB layout and component selection, routing, firmware and UI, with a contract manufacturer producing a small batch. OpenAI said manufacturing tolerances caused most rework, and that an undisclosed newer internal model scored 0.875 on the BenchCAD 2.0 benchmark versus 0.594 for GPT-6 Astra at its highest reasoning setting.
Why it matters: A vendor-reported claim that a frontier model can carry a hardware design end-to-end is a notable capability marker, though the benchmark comparison rests on an undisclosed internal model.
Refs: https://fluxbbs.com/openai-gpt-6-astra-hardware-design-benchcad-20261104/

### 6. OpenAI consumer lead said ChatGPT search queries reached 20% of Google's (OpenAI, Google)
According to a Chinese tech report, OpenAI consumer product lead Adam Fry confirmed that search-type queries on ChatGPT have reached 20% of Google's search query volume. The same article cited Pew survey data that 42% of US adults have used AI to search for information and that 44% have used ChatGPT versus 24% for Gemini, and quoted Alphabet CEO Sundar Pichai arguing the competition is not zero-sum.
Why it matters: A named OpenAI executive putting a search-volume ratio against Google is a concrete competitive datapoint, though it is a single reported figure without independent verification in the supplied material.
Refs: https://www.chinaz.com/ainews/32060.shtml

### 7. Google launches Gemini for government services in private preview (Google)
Google launched Gemini for government services in private preview for federal, state and local agencies, alongside Wiz security agents in Wiz for Gov and expanded Gemini search tools for classified environments on Google Distributed Cloud, including Gemini 3.5 Flash and NVIDIA Blackwell B300 GPUs. Google cited a survey with theCUBE and ECI Research finding 96.3% of agencies have deployed agents in some form but only 9% reached agency-wide adoption, and named customers including America.gov, the Department of Energy's Genesis Mission and GenAI.mil.
Why it matters: A concrete public-sector product launch that also quantifies the gap between agent pilots and agency-wide deployment, in a market where cloud and AI vendors are competing hard.
Refs: https://securitybrief.news/story/google-launches-gemini-for-government-services-preview

### 8. Google DeepMind and Stanford paper finds simple shapes can steer VLM code choices (Google)
A Google DeepMind and Stanford paper tested 288 shapes in coding prompts across Claude Opus 4.7, Gemini 3.1 Pro and GPT-5.4, finding a red heart moved Claude Opus 4.7 and GPT-5.4 from 0% to 100% recursive solutions on a binary tree problem. When a shape steered Gemini 3.1 Pro, 71.5% of its reasoning traces called the image irrelevant, suggesting visual influence can occur without being reflected in stated reasoning.
Why it matters: Evidence that unrelated visual inputs can change model outputs while reasoning traces deny it is directly relevant to anyone deploying vision-capable agents.
Refs: https://www.bestblogs.dev/en/status/2117651708998484268?utm_source=rss&utm_medium=feed&utm_campaign=resources&entry=rss_article_item

### 9. Meta discloses MTIA chip roadmap targeting roughly one chip every six months (Meta)
Reuters-reported coverage says Meta disclosed a roadmap of four MTIA generations (300/400/450/500) over two years, covering workloads from ranking-recommendation training to generative-AI inference, with Meta claiming 4.5x cumulative HBM bandwidth and about 25x compute gains from 300 to 500. The report also says Meta renewed its custom-chip agreement with Broadcom through 2029 with an initial compute commitment above 1GW, and that MTIA 450 is planned for early-2027 mass production.
Why it matters: A concrete roadmap and supplier commitment signal that a hyperscaler is pursuing inference-cost reduction through custom silicon, a competitive pressure point for merchant GPU vendors.
Refs: https://www.renrendaima.com/article/34602.html

### 10. Meta Muse agent app and open-weight models detailed (Meta)
A report describes Meta's Muse personal AI agent app, launched in the US on September 8, 2026, which can browse, fill forms, send email and book travel, running on a dedicated cloud VM per user, with free and $20/$100 monthly tiers. The Muse model family includes Muse Spark, Muse Image, Muse Glimmer (a 30B Apache 2.0 open-weight model) and Muse Spark Open (816B total, 42B active parameters under a custom license), with Meta AI now powered by Muse Spark rather than Llama.
Why it matters: Concrete detail on Meta's post-Llama model branding and its split between open-weight and custom-licensed releases, relevant to developers choosing deployable models.
Refs: https://www.gatewebsite.com/zh/news/detail/meta-muse-adds-ai-agent-app-and-open-weight-models-25391466

### 11. Qwen3.8 lineup detailed: Apache 2.0 27B weights, custom-licensed MoE, regional expansion (Qwen)
A roundup states Alibaba's Qwen3.8 family includes a 27B dense model released in August under Apache 2.0 with a 262,000-token native context, a larger open-weight MoE flagship (Qwen3.8-2.4T-A95B) under a custom Qwen3.8-Max License, and hosted Max and Flash variants with 1M-token native context. It reports QwenCloud expanded Flash to Virginia on October 3 and Frankfurt and Hong Kong on October 26, with OpenAI- and Anthropic-compatible API formats, and lists third-party pricing of $2.00/$6.00 per million tokens for Max and $0.50/$3.00 for the 27B.
Why it matters: The licensing split between permissive and custom terms, plus regional hosting expansion, is practically relevant to teams choosing deployable models, though pricing figures are third-party.
Refs: https://www.gatenode.irish/zh/news/detail/qwen38-offers-apache-20-27b-weights-and-1m-token-hosted-models-25389440

### 12. Musk says Grok Bot serving costs are unsustainable relative to revenue (xAI)
A commentary piece reports that on November 1 Musk responded to a user about Grok Bot quota consumption by saying the cost of serving Grok Bot is unsustainable relative to revenue and that unlimited use is not possible at present. The article describes Grok Bot as built by the Cursor team after its acquisition into SpaceXAI, and frames Musk's AI strategy across infrastructure, models and agent applications.
Why it matters: A direct statement from xAI's owner about unit economics of an agent product is a concrete signal on the cost side of consumer agent deployment.
Refs: https://www.bitbase.com/zh-HK/news/336159

## Cross-Org Themes

- Inference cost economics are driving concrete deployment choices, from Revolut's self-hosted GLM to Meta's inference-first MTIA roadmap and Musk's comments on Grok Bot serving costs.
- Open-weight and permissively licensed models are being positioned as production substitutes, seen in Revolut's GLM deployment, Huawei Cloud's DeepSeek and GLM recommendations, and Qwen's Apache 2.0 27B release.

## Rumors and Unverified Claims

A Chinese report says OpenAI pushed GPT-6 globally to ChatGPT users, replacing GPT-5.6 Sol and Luna, with a new intelligent UI and 44% shorter web-search waits; this appears only in a related-links blurb and was not selected as an event. The same source mentions an OpenAI plan to merge ChatGPT and Codex usage quotas starting in December. A Simon Willison post says Kimi K3.1 Pro landed on the Kimi API with a promise that full model weights would be released by November 4, 2026. A commentary piece says SpaceX acquired Cursor for over $60 billion in stock and that Anthropic is preparing an IPO. A roundup mentions an unconfirmed report that Qwen3.8-Max's Artificial Analysis score rose from 40 to 45.

## Takeaway

The evidence to watch is whether self-hosting and open-weight substitution show up in disclosed production numbers beyond a single customer, and whether cloud platforms' model-retirement schedules accelerate that shift. Independent verification of vendor-reported capability and cost claims, rather than launch announcements, will be the better signal.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
