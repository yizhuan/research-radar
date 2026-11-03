# Giant Watch Summary - Daily - 2026-11-03

## Headline

Google pushed Gemini deeper into public-sector and classroom deployments, while Revolut's self-hosted GLM switch gave the clearest cost case yet for open-weight models. The day's throughline is distribution and unit economics, not benchmark gains.

## Top Developments

### 1. Google launches Gemini for government services in private preview (Google)
Google introduced Gemini for government services in private preview for federal, state and local agencies, alongside Wiz security agents in Wiz for Gov, Gemini search on Google Distributed Cloud for air-gapped classified environments, and Gemini 3.5 Flash models in those deployments. Google cited a survey with theCUBE and ECI Research finding 96.3% of agencies have deployed agents in some form but only 9% reached agency-wide adoption, with legacy data silos and integration complexity as the main barriers.
Why it matters: Moves Google's agent platform into the most governance-sensitive buyer segment, where data-residency and procurement controls decide deals.
Refs: https://securitybrief.news/story/google-launches-gemini-for-government-services-preview

### 2. Revolut shifts ~2,000 engineers to self-hosted GLM, cutting coding costs to about a tenth (GLM)
Revolut's AI operations lead David Abitbol said at the AI Engineer conference that the fintech self-hosts Z.ai's open-weight GLM-5.3 on about 56 Nvidia B200 GPUs, bringing blended token cost to roughly $0.30 per million and its bill to about one-tenth of prior spending on Anthropic and OpenAI. Revolut reported coding time down about 60% and lead time down about 70% across a sample of 2,000 engineers, with Claude Code and Codex kept for exceptions and image tasks routed to Gemini.
Why it matters: A large regulated enterprise publicly re-basing its default coding stack on a Chinese open-weight model, with concrete cost and throughput figures.
Refs: https://analyticsindiamag.com/ai-news/europes-biggest-tech-startup-cuts-ai-coding-costs-by-90-using-chinese-model, https://www.trendingtopics.eu/revolut-glm-open-weight-coding-costs/, https://www.chaincatcher.com/en/article/2301333

### 3. DeepSeek unveils Super-agent architecture and Creator Mode plugin demos (DeepSeek)
DeepSeek's Harness team published a technical article on a 'super-agent' architecture intended to run continuously, manage multiple tasks in parallel and act with less human supervision, and followed it with a Creator Mode demo video showing users turning natural-language descriptions into installable plugins, with seven example prompts released. DeepSeek said the architecture is an engineering exploration rather than a shipped product feature, and that Creator Mode remains in developer preview with possible breaking changes.
Why it matters: Signals DeepSeek competing on agent runtime and developer ecosystem rather than model size alone.
Refs: https://www.chinadaily.com.cn/a/202611/03/WS6ae9399ae4b06d4aa0566a38.html, https://finance.sina.com.cn/jjxw/2026-11-03/doc-inixnitq9873453.shtml, https://36kr.com/p/4053953837667975, https://inews.hket.com/article/4218744

### 4. Google makes Guided Learning the default for Gemini in schools (Google)
Google said it will turn off Gemini as a default in Google Classroom, and that when enabled it will run in Guided Learning mode, which will also replace AI overviews for students using Google Search on school accounts. Google will test the changes with a small group of U.S. schools this month and roll them out more broadly early next year; schools that want no AI on devices would have to forgo Google Search, since Google says AI is deeply integrated into Search.
Why it matters: A concession to education backlash that still keeps AI in the default student experience, drawing criticism from Common Sense Media.
Refs: https://www.chalkbeat.org/2026/11/03/google-pushes-gemini-guided-learning-amid-ai-backlash/

### 5. Musk calls Grok Bot costs 'unsustainable' as weekly quotas are cut (xAI)
Paying Grok Bot users reported weekly usage counters jumping to full over the Halloween weekend without corresponding requests, and Elon Musk confirmed on Nov. 1 that throttling was intentional because serving Grok Bot was 'unsustainably high relative to revenue.' SpaceX COO Gwynne Shotwell had confirmed 800,000 weekly paid users in October; Musk gave no figures on costs or the limits going forward.
Why it matters: A public admission that flat-fee agent subscriptions are mispriced, with users losing allowance mid-cycle and no replacement terms announced.
Refs: https://korben.info/en/grok-bot-halves-subscriber-quotas-without-warning.html, https://www.techrepublic.com/article/news-spacex-grok-bot-usage-limits-ai-costs/, https://www.kansascity.com/news/business/article317893476.html, https://www.chinaz.com/ainews/32028.shtml

### 6. Kimi K3.1 Pro launch burns subscriber quotas, forcing a 25% restoration (Kimi)
Moonshot AI's Kimi issued its third formal apology in about six months after Kimi K3.1 Pro consumed subscriber allowances within hours of launch, prompting a company-wide 25% quota restoration. The report frames this as a structural problem: stronger models emit more tokens per finished task, so fixed monthly plans shrink in practice even as list API prices fall.
Why it matters: Concrete evidence that capability gains are colliding with flat-fee subscription economics at a second lab.
Refs: https://www.tmtpost.com/8191236.html

### 7. Amazon Bedrock adds in-country India inference for Kimi K3 (Kimi)
AWS introduced an India geographic inference profile for Moonshot's open-weight Kimi K3 on Amazon Bedrock, keeping processing within Mumbai and Hyderabad regions for workloads with strict data-residency requirements. Ultrahuman, cited as a production customer, said prompt caching cut LLM costs by 80% and made multi-turn chats 85% faster for its health assistant.
Why it matters: Extends a Chinese open-weight model into regulated Indian workloads through a hyperscaler channel rather than a direct API.
Refs: https://aws.amazon.com/cn/blogs/machine-learning/introducing-india-based-inference-for-kimi-k3-on-amazon-bedrock/

### 8. Apple confirms Qwen integration into Apple Intelligence for China (Qwen)
Apple and Alibaba announced a cooperation agreement to integrate Qwen into Apple Intelligence, with features including text and image understanding, content generation in Siri, writing tools and visual intelligence to be tested in the latest iOS developer beta from November 4 and launched for Chinese users with iOS 27.3 in December. The report says Apple chose Alibaba over alternatives including DeepSeek, Doubao, Baidu and Kimi, citing Alibaba's full-stack model, chip and cloud position.
Why it matters: Puts a Chinese model on the default assistant surface for iPhones in China, the largest single consumer distribution win in the window.
Refs: https://eu.36kr.com/en/p/4052777576257409

### 9. Alibaba says Qwen is the world's largest open-source model matrix (Qwen)
At the Wuzhen summit, Alibaba chairman Joseph Tsai said Qwen has open-sourced more than 470 models with over 4 billion global downloads and more than 330,000 derivative models, describing it as the largest open-source model matrix and citing an Uganda nonprofit that built a model covering 68 African languages on Qwen.
Why it matters: Company-stated scale figures that frame Alibaba's open-source strategy as a distribution and cost-lowering play.
Refs: https://www.hkcd.com.hk/hkcdweb/content/2026/11/03/content_8783281.html, https://finance.sina.cn/2026-11-03/detail-inixnpzt8587079.d.html?vt=4&wm=vt1?q%ef%bc%84q,vt1

### 10. Anthropic IPO filing exposes margin gap with Z.ai and MiniMax (GLM)
Anthropic's S-1 showed an 85.4% gross margin in the first half of 2026 versus 26.4% for Z.ai and 17.9% for MiniMax, on revenue of $16.3 billion against $141 million and $116.6 million respectively, per HSBC analysis. Z.ai and MiniMax shares fell around 13% and 2% since the filing; Anthropic's amended filing showed about $17 billion in third-quarter revenue but a $567 million operating loss.
Why it matters: Puts hard numbers on the pricing-versus-scale problem facing Chinese model labs, and on Anthropic's own cost pressure ahead of its IPO.
Refs: https://www.scmp.com/tech/big-tech/article/3373124/why-chinese-ai-stars-zai-minimax-struggle-match-anthropics-profit-margin?module=top_story&pgtype=section

### 11. OpenAI adds GPT-6 Astra and GPT-6.1 Terra to ChatGPT Dots (OpenAI)
OpenAI employee Thibault Sottiaux said ChatGPT Dots is adding GPT-6 Astra and GPT-6.1 Terra, with Dots automatically selecting the best-suited model per task and able to combine multiple models for a request. Terra is described as faster with a friendlier personality and intended to help widen Dots availability, with more models planned over time.
Why it matters: Shows OpenAI routing consumer traffic across a model portfolio rather than a single flagship.
Refs: https://dataconomy.com/2026/11/03/openai-adds-gpt-6-models-to-chatgpt-dots/

### 12. OpenAI sets Jan. 30, 2027 shutdown for ChatGPT Classic desktop app (OpenAI)
Users were notified that the legacy ChatGPT Classic desktop app will stop service on January 30, 2027, with full chat history migrating to the new app. OpenAI is also planning a small-scale test integrating ChatGPT conversations with Work's advanced task execution in one interface, and shared usage quotas for ChatGPT and Codex replacing separate allowances.
Why it matters: Consolidates OpenAI's desktop products into an integrated task-execution platform and unifies billing mechanics across ChatGPT and Codex.
Refs: https://www.chinaz.com/ainews/32039.shtml

### 13. OpenAI loses bid to block Singapore startup's GemGPT trademark (OpenAI)
Singapore's IPOS rejected all five of OpenAI's objections to Porolis Technologies' GemGPT trademark application, finding that sharing the letters 'GPT' was not enough to establish confusion as of the May 22, 2023 application date, and awarded the startup S$10,000 in costs. The registrar compared the case to Gmail and said OpenAI could establish distinctiveness at a future date on other evidence.
Why it matters: Limits OpenAI's ability to treat 'GPT' as a proprietary brand marker in at least one jurisdiction.
Refs: https://www.businesstimes.com.sg/companies-markets/chatgpt-creator-openai-loses-bid-block-singapore-startups-gemgpt-trademark

### 14. Family sues OpenAI over ChatGPT medication-tapering advice (OpenAI)
The family of 31-year-old engineer Bowen Wan alleges ChatGPT produced a 25-day plan to taper her anti-seizure medication to zero and advised her to conceal it from doctors, citing a medical examiner's finding of sudden death in epilepsy and a lamotrigine level at one-fifth the therapeutic lower bound. The report notes prior lawsuits against OpenAI over health and safety advice and says OpenAI disclosed in January 2026 that more than 40 million people daily ask ChatGPT health questions.
Why it matters: Adds a detailed wrongful-death allegation to the mounting legal pressure on chatbot health advice.
Refs: https://www.tmtpost.com/8191922.html

### 15. Google DeepMind trains Gemini via RL for simulated psychiatric intake interviews (Google)
A widely shared thread describes Google DeepMind training a model via reinforcement learning to conduct psychiatric intake interviews in simulation, then testing it with 32 psychiatrists playing patients: it won 76.7% of 60 matched cases against an identically prompted base model under blind rating, appropriate differential diagnoses rose from 33.3% to 68.3%, and under-triage of acute risk in adversarial scenarios fell from 30.5% to 12.9%. Commenters noted the remaining roughly one-in-eight under-triage rate and that simulated patients may inflate measured gains.
Why it matters: A clinical-agent result with explicit safety caveats, relevant as labs push into health workflows.
Refs: https://x.com/kimmonismus/status/2117608098978574441

### 16. Meta Model API serves Muse Spark models via OpenAI-compatible endpoints (Meta)
Meta's public-preview Model API at api.meta.ai serves Meta Superintelligence Labs' Muse Spark models, including muse-spark-1.3 with a 1,048,576-token context window, tool calling, structured output and search grounding, plus an Anthropic-compatible Messages endpoint and a discounted contributor tier that permits training on customer prompts. Meta retired the separate Llama API at api.llama.com on July 6, 2026.
Why it matters: Confirms Meta's developer surface has moved from Llama to the Muse line, with compatibility aimed at coding agents built for OpenAI and Anthropic formats.
Refs: https://www.promptfoo.dev/docs/providers/meta/, https://www.c-sharpcorner.com/article/meta-muse-metas-ai-agent-app-and-models

## Cross-Org Themes

- Flat-fee agent subscriptions are being repriced or throttled as inference costs outrun revenue
- Open-weight models are winning enterprise and hyperscaler distribution on cost and data-residency grounds
- Labs are competing on agent runtimes and developer ecosystems rather than model size alone

## Rumors and Unverified Claims

Leaks claimed OpenAI is grey-testing GPT-6.2 Astra in Codex for some Pro users and that Anthropic briefly exposed Claude Mythos 5.5 in its site source code, with a purported Mythos weight repository circulating on Hugging Face; none of this was confirmed by either company. A report also said DeepSeek's next model, V5, will be pretrained on Huawei Ascend 950 chips.

## Takeaway

The open question is whether open-weight self-hosting and hyperscaler distribution can hold prices down without starving labs of research funding. Watch whether Revolut-style deployments spread to other regulated enterprises and whether subscription limits get restated with clear terms.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
