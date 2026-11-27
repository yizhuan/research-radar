# Giant Watch Summary - Daily - 2026-11-27

## Headline

OpenAI's GPT-6.2 billing correction and GPT-5.6 retirement land together, forcing paid ChatGPT users to re-plan their usage budgets. The day's episode is metering and cost discipline: vendors are tightening how work is counted even as they ship cheaper, faster models.

## Top Developments

### 1. OpenAI admits GPT-6.2 billing mistake; paid users hit limits 40% faster (OpenAI)
OpenAI's head of Product & Platform, Thibault Sottiaux, said on November 26 that the company 'made a billing mistake at launch of GPT-6.2' that undercharged Astra and Sol usage for most users. With the fix live, OpenAI says users reach limits 40% faster on GPT-6.2 Astra and 25% faster on Sol; subscription prices are unchanged, no retroactive charges apply, and every paid subscriber on Go, Plus, Pro and Business receives one banked usage reset. A further change is planned for December, pooling ChatGPT and Codex into a single token-based allowance for Plus, Pro and Business.
Why it matters: A public admission that the meter behind a paid ChatGPT plan can be redefined after purchase, arriving nine days after the November 17 launch and drawing swift negative reaction from heavy users.
Refs: https://pricingrank.org/openai-gpt-6-2-billing-fix-limits-40-percent-faster-november-2026/

### 2. OpenAI sets December 23 shutdown for GPT-5.6 Sol and Terra (OpenAI)
OpenAI has fixed December 23 as the date GPT-5.6 Sol is retired from the ChatGPT tab and GPT-5.6 Sol and Terra are retired from Work and Codex, with the chat-optimized GPT-6.2 Sol taking over for Plus and Pro users. The report traces GPT-5.6 from limited preview on June 26 and general availability on July 9 to retirement in under six months, and cites cost of running multiple model generations plus the capability gap on image understanding, complex instruction following and BrowseComp as reasons for the fast migration. The article also notes that GPT-6.2's reception since launch has been poor.
Why it matters: A sub-six-month model lifespan that consolidates all paid users onto one base model ahead of planned agent features, and a rare public backlash over deprecation timing.
Refs: https://www.bitbase.com/zh-CN/news/gpt-6-2-openai-gpt-5-6

### 3. Google DeepMind releases Gemini 4 Neon with 1M context and $3/$15 pricing (Google)
Gemini 4 Neon (gemini-4-neon), announced November 18 and updated November 23, sits between Gemini 4 Hydrogen and Gemini 4 Carbon and targets high-frequency software engineering, analytical knowledge work, scientific reasoning and defensive security. It offers a unified 1M-token multimodal context, four thinking levels (low, medium, high default, xhigh), $3 per million input tokens ($0.15 cached) and $15 per million output tokens, and Google reports 32% lower cost per task than Carbon at default high thinking. DeepMind's evaluation table puts Neon first on the Artificial Analysis Coding Agent Index (58.6) and CursorBench 4.1 (65.4% versus 58.1% for Claude Opus 5.5), while Claude Opus 5.5 edges it on Terminal-Bench 4.1 (65.8% vs 65.2%) and FrontierCode 2.0 (47.3% vs 46.2%).
Why it matters: A mid-tier model pitched explicitly on cost per task, with published head-to-head comparisons against Claude Opus 5.5 and GPT-6.2 Sol that frame the competitive field as a price-performance contest.
Refs: https://www.toolai.io/info/google-deepmind-introduces-gemini-4-neon-with-1m-context-3-15-api-pricing-and-32-lower-task-cost, https://www.toolai.io/zh/info/google-deepmind-%e5%8f%91%e5%b8%83-gemini-4-neon-%e6%94%af%e6%8c%81%e7%99%be%e4%b8%87%e4%b8%8a%e4%b8%8b%e6%96%87%e4%b8%8e%e5%9b%9b%e6%a1%a3%e6%80%9d%e8%80%83%e5%bc%ba%e5%ba%a6-%e5%8d%95%e4%bb%bb%e5%8a%a1%e6%88%90%e6%9c%ac%e8%be%83-carbon-%e9%99%8d%e4%bd%8e-32

### 4. DeepMind gives AI agents partial control of compute for next Gemini experiments (Google)
On the company podcast, VP of Research Koray Kavukcuoglu said AI agents control part of the compute used to run experiments for the next Gemini model, while stressing the lab is far from full recursive self-improvement. He described a shift from separate teams for projects such as AlphaFold and nuclear fusion to a single general-purpose algorithm for science and products, said each Gemini generation is a hand-built one-off with parallel teams on successors, and said DeepMind does not reward agents' chain-of-thought during training so their intentions remain readable in natural language. He also argued no benchmark captures the core of intelligence and that AGI will arrive when everyday products earn enough trust for people to delegate decisions.
Why it matters: A concrete, if bounded, step toward AI-assisted research workflows, paired with an explicit safety rationale and a public rejection of benchmark-based AGI claims.
Refs: https://news.lavx.hu/article/google-deepmind-gives-ai-agents-partial-control-of-gemini-experiment-compute, https://cctest.ai/en/articles/deepmind-gives-ai-agents-a-role-in-gemini-experiments-but-self-improvement-is-still-distant, https://times.hntrends.net/story/50661218?view=reader#discussion

### 5. US chip rule and anti-distillation push GLM-5.5 and Kimi K4 into 2027 (GLM, Kimi)
A US Commerce Department rule effective November 19 imposes licensing on covered computing arrangements at data centres outside the US above roughly the equivalent of 750 Nvidia H100 chips, with 90 days for existing operators to obtain licences. People familiar with the matter told Reuters on November 26 that Z.AI missed its target of releasing GLM-5.5, a roughly 3-trillion-parameter model, this month, with the launch possibly slipping to Q1 2027 or later, partly due to more effective anti-distillation safeguards; Z.AI released GLM-5.4 on Monday, built on a 750-billion-parameter base. Moonshot AI, which rents overseas compute, internally expects its six-month release cadence to stretch to a year or more and Kimi K4 to slip to around mid-2027; it has stepped up European capacity rentals, plans to approach Chinese chipmakers, and has begun distilling from Google and Meta models as OpenAI and Anthropic data became harder to obtain. The Information reported Moonshot scrapped a $150 million deal for Nvidia Blackwell access via an Indonesian data centre.
Why it matters: The clearest evidence yet that export controls and anti-distillation defences are translating into schedule slippage for China's next flagship models, with both labs declining to comment.
Refs: https://pivotnews.ai/five/chinese-labs-z-ai-and-moonshot-face-model-delays-from-us, https://www.radardigital.ai/en/articles/us-restrictions-delay-ai-models-china/, https://paktechstan.com/article/us-chip-curbs-are-stalling-china-s-next-ai-models-z-ai-s-glm-5-5-and-moonshot-s-kimi-k4-slip-into-2027, https://technews.tw/2026/11/27/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development/, https://www.gatewebsite.com/zh-tw/news/detail/moonshot-ai-model-updates-delayed-by-us-chip-curbs-and-anti-distillation-25893642, https://ai-trends.today/moonshot-ai-begins-distilling-from-google-and-meta-models-amid-delays-unite-ai/

### 6. DeepSeek app adds per-conversation cost display after usage caps (DeepSeek)
DeepSeek's Android app version 2.10.0 adds a button letting users see the specific charge corresponding to each conversation's quota consumption, using the same billing model as the official API documentation, which reports read as groundwork for a paid app tier. Earlier this month DeepSeek capped single inputs at roughly 40,000 characters and stopped supporting long conversations inactive for more than seven days, with users seeing 'server busy, usage limit reached' and 'insufficient compute' messages. China Galaxy Securities attributed the limits to the industry-wide tension between compute supply, service cost and commercial return, noting that agent workloads accumulate context and raise inference costs; the article also cites DeepSeek's October 20 open-sourcing of the DeepInfer inference framework, which supports Nvidia GPUs and Huawei Ascend NPUs.
Why it matters: A visible step from free consumer access toward metered billing at a lab known for open models, framed by analysts as a structural cost problem rather than a one-off.
Refs: https://api3.cls.cn/share/article/2546211?os=ios&sv=812&app=, https://www.eet-china.com/mp/a542341.html, https://finance.eastmoney.com/a/202611273941540191.html

### 7. Thomson Reuters builds Thomson 1.1 on Z.ai's GLM and Google's Gemma (GLM, Google)
Business Insider reported on November 26 that Thomson Reuters plans to launch its next in-house model, Thomson 1.1, later this year, built separately on Z.ai's GLM and Google's Gemma, after Thomson 1.0 was built on Alibaba's Qwen in August. CTO Joel Hron said GLM suits AI agents because of strong computer-operation capabilities and Gemma's strengths are small size and efficiency; the company will keep using OpenAI and Anthropic models for higher-difficulty work and use in-house models for mid-level tasks such as tax advisory. Thomson Reuters has spent about $40 million on in-house model development, with in-house models under 5% of total AI token usage, and plans to integrate validated use cases into products from 2027. The report also notes a Hirundo analysis finding bias in an existing Thomson model and the company's claim of further mitigation in the next generation.
Why it matters: A named enterprise buyer publicly splitting workloads across US and Chinese open models on cost and IP-control grounds, giving GLM a concrete commercial reference even as its next flagship slips.
Refs: https://www.digitaltoday.co.kr/en/view/131577/thomson-reuters-chooses-us-and-china-ai-tech-amid-race-for-ai-dominance

### 8. Grok Bot product lead recounts one-month build and manual onboarding of hundreds of users (xAI)
In a podcast interview with Lenny Rachitsky, Roman Ugarte — a former Cursor employee who worked on incubating Grok Bot and leads its product — described a small team building an internal prototype in about a month, then going from internal beta to public release in roughly three weeks. He said the team manually onboarded two to three hundred people over about two weeks, deliberately cut experimental features before launch, and chose to hide tool calls and chain-of-thought behind a Slack-like activity indicator, while surfacing task lists and priorities. He described users promoting one bot to a 'chief of staff' role that dispatches work to others, and said the product gives each bot its own cloud computer to handle tasks lacking APIs or MCP support.
Why it matters: A detailed account of how a major lab's personal-agent product was scoped and shipped, including the deliberate decision to hide agent internals from users — a design stance that contrasts with transparency-first approaches.
Refs: https://www.woshipm.com/ai/6501123.html

## Cross-Org Themes

- Metering and cost-per-task economics are being redefined at both consumer subscription and API pricing layers
- Compute access and inference cost are shaping release schedules and product decisions across US and Chinese labs

## Rumors and Unverified Claims

A Chinese-language report says OpenAI's announcement teased 'more to look forward to' before year-end, leaving open whether another launch is planned; no specifics were given. Separately, an article states that Moonshot began distilling from Google and Meta models and that Z.AI's GLM-5.5 delay is partly due to anti-distillation safeguards, both attributed to unnamed people familiar with the matter; neither company responded to requests for comment.

## Takeaway

Watch whether OpenAI's December pooled ChatGPT-and-Codex allowance compounds the billing correction's effect on heavy users, and whether Z.AI and Moonshot confirm or revise their 2027 timelines as European and domestic compute options are tested.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
