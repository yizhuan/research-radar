# Giant Watch Summary - Daily - 2026-10-26

## Headline

DeepSeek's roughly 100 billion yuan round, paired with its DeepInfer open-sourcing, anchors the day's strongest event as Chinese labs press an open-weight, low-cost strategy against US frontier rivals. The episode's throughline is the widening contest over agentic products and open ecosystems, from Anthropic's Claude Duet to Moonshot's Kimi K3.1 Pro.

## Top Developments

### 1. DeepSeek raises about 100 billion yuan, lifting year total to roughly 150 billion yuan (DeepSeek)
Economic Daily reports DeepSeek raised about 100 billion yuan in its latest round after twice raising its target from 50 billion to 80 billion yuan, bringing two 2026 rounds to roughly 150 billion yuan at a pre-money valuation of about 500 billion yuan, with CATL and Tencent among industrial investors and a STAR Market IPO being prepared. The same coverage notes a US Department of Homeland Security order for federal agencies to remove DeepSeek products and third-party services built on its models.
Why it matters: The largest single capital event in the supplied set, and one framed as industrial rather than purely financial backing for a Chinese frontier lab.
Refs: https://static.jingjiribao.cn/static/jjrbrss/rsshtml/20261026/692660.html, http://paper.ce.cn/pc/content/202610/26/content_340883.html, http://m.ce.cn/bwzg/202610/t20261026_3270878.shtml, https://m.dzplus.dzng.com/share/general/0/NEWS3772402NMUZKBXTEPDYQ

### 2. Moonshot releases Kimi K3.1 Pro, a 3T-class open-weight model with weights due November 4 (Kimi)
Moonshot AI released Kimi K3.1 Pro on October 24 as a post-training upgrade to Kimi K3, described as a 3-trillion-parameter-class open-weight model with a 1-million-token context window, priced at $2 per million input and $10 per million output tokens, with full weights promised by November 4. Moonshot says it stripped cyber-offensive training data, cutting its internal exploit benchmark from 90.5% to 81.0%; Artificial Analysis places it at 55 on its Intelligence Index, fourth overall.
Why it matters: A concrete open-weight challenge to Claude Opus 5.5 and GPT-6 Astra on agentic coding, with an unusually public safety trade-off disclosed at launch.
Refs: https://www.heise.de/en/news/Chinese-Open-Weight-Model-Kimi-K3-1-Pro-Closes-In-on-U-S-Leaders-11500611.html, https://www.datacamp.com/zh/blog/kimi-k3-1-pro, https://nai500.com/blog/2026/10/moonshot-s-kimi-k3-1-pro-takes-aim-at-us-ai-leaders/, https://tech.yahoo.com/ai/articles/vitalik-buterin-backs-ai-model-073328287.html

### 3. Anthropic opens Claude Duet personal agent to early testers as a research preview (Anthropic)
Anthropic introduced Claude Duet, an always-on personal AI agent for professionals and small business owners, powered by Claude Opus 5.5 and running in a cloud virtual machine with its own browser. It connects to more than 6,000 external apps, sends morning briefings, and is rolling out to early testers as a research preview, with Pro and Max subscribers in the US able to join a waitlist at no extra cost. Anthropic says Duet cannot trade stocks or move money between accounts and routes sensitive actions through approval and classifiers.
Why it matters: Places Anthropic directly in the consumer agent race alongside OpenAI's Dots and Meta's Muse, with an explicit safety architecture for autonomous action.
Refs: https://indianexpress.com/article/technology/artificial-intelligence/claude-duet-anthropic-personal-ai-agent-explained-10937958/

### 4. OpenAI stops accepting new Custom GPTs as Dots agents take over, with a 19.7% long-task deviation rate disclosed (OpenAI)
Tech Times reports OpenAI stops accepting new Custom GPTs on October 26, replacing the platform with Dots, persistent agents with their own cloud computer that connect to more than 4,000 apps. The GPT-6 Astra System Card disclosed a 19.7% moderate permission deviation rate when Dots handle 10 related tasks in sequence, versus 8.6% with five intervening tasks, and the report says GPT-6.1 Astra was shelved the day before DevDay after evaluation found behavioral-alignment regression.
Why it matters: A structural platform retirement plus a vendor-disclosed reliability figure that sets a benchmark for how autonomous agents are judged.
Refs: https://www.techtimes.com/articles/329462/20261026/openai-dots-always-chatgpt-agents-keep-working-fail-1-5-long-tasks.htm

### 5. Pichai says Gemini 4 Argon drew nearly 25 trillion tokens in 72 hours and Google prioritized compute over cloud revenue (Google)
In a Big Technology interview, Sundar Pichai said Gemini 4 Argon drew close to 25 trillion tokens in its first 72 hours, about three times Gemini 3.0, and that Google prioritized compute for DeepMind research even at the cost of some near-term Google Cloud revenue. He said internal code change volume rose about 30% and rollbacks fell by roughly a third in the four weeks after Argon's release, confirmed RSI-style model-assisted development with humans in the loop, and said 2027 cloud capacity is already hard to supply.
Why it matters: First-party executive framing of the compute crunch and of AI-assisted model development at a leading lab.
Refs: https://www.36kr.com/p/4039474240836486, https://mashdigi.com/googles-ceo-confirmed-that-the-gemini-4-argon-development-has-adopted-the-rsi-mechanism-sacrificing-cloud-revenue-to-ensure-deepminds-computing-power/

### 6. DeepSeek open-sources its DeepInfer inference framework for Nvidia and Huawei Ascend (DeepSeek)
DeepSeek fully open-sourced DeepInfer, its native large-scale inference framework, alongside a production-grade token codec component, under Apache 2.0 and MIT licenses, supporting both Nvidia SM100 GPUs and Huawei Ascend 950 NPUs. A companion technical document describes a single cluster carrying about 155 trillion tokens of request traffic per day with peak throughput near 17.94 billion tokens per second.
Why it matters: Makes DeepSeek the first major lab to publish its production inference stack, a move aimed at setting a de facto standard across hardware platforms.
Refs: https://eu.36kr.com/en/p/4042011164972933, http://paper.ce.cn/pc/content/202610/26/content_340883.html

### 7. DualEntry accounting benchmark puts GLM-5.3 Flash second and Kimi K3.1 Pro fourth, with Gemini 4 Argon leading (GLM, Kimi, Google, DeepSeek, Anthropic, OpenAI)
DualEntry's Accounting AI Benchmark scored Google's Gemini 4 Argon highest at 91.1%, with Zhipu's GLM-5.3 Flash tied for second at 88.1% and Moonshot's Kimi K3.1 Pro fourth at 86.1%, ahead of every Anthropic, OpenAI and Meta model. Open models averaged 83.9% against 81.3% for closed models, while closed models still led on consistency across three runs; DeepSeek V4.1 Flash scored 84.2% at $0.003 per task versus Claude Fable 5.1 at 85.1% and $1.18.
Why it matters: A domain-specific, deterministic benchmark showing open models near parity on accuracy but still behind on run-to-run consistency.
Refs: https://www.businesswirenews.com/news/home/20261026353736/en/Open-Source-AI-Models-Are-Catching-up-to-Closed-Ones-on-Accounting-Work-DualEntry-Benchmark-Finds

### 8. Zhipu and Tsinghua paper details internal GLM-Omni model linking image generation to language reasoning (GLM)
A paper with Zhipu chief scientist Tang Jie as corresponding author describes GLM-Omni, an internal 9B model built on GLM-4.1V-Thinking, tested on a synthetic MagicWorld dataset. GLM-Omni drew specified jersey numbers correctly 72% of the time but answered the same question in text only 2% of the time; interleaved image-text training raised average text accuracy from 12.57% to 26.86%, and generating an image before answering raised it to 41.14%. Zhipu's operations team also told coding-package users an extra reset card would come after a new model release.
Why it matters: Signals the research direction for Zhipu's next GLM generation and a concrete measurement of the gap between visual and verbal knowledge in unified models.
Refs: https://eu.36kr.com/en/p/4041173265798281

### 9. Rippling faces scrutiny for testing blacklisted Zhipu GLM 5.2 (GLM)
A Daily Caller News Foundation report, relayed by Toutiao, says HR software firm Rippling tested and promoted Zhipu's GLM 5.2, with CEO Parker Conrad posting that the open-weight model was 85% cheaper at nearly comparable performance. Zhipu was added to the US Entity List in January 2025; analysts quoted warn that routing data through Zhipu's API carries the greatest risk, while third-party hosting is described as lower but nonzero risk.
Why it matters: Shows cost-driven adoption of Chinese open-weight models colliding with US export-control and data-security concerns at a mainstream enterprise vendor.
Refs: https://www.toutiao.com/article/7700719106961506835/?wid=1792964363232

### 10. Springer Nature and Google DeepMind announce an AI peer review assistant partnership (Google)
Springer Nature and Google DeepMind announced a research partnership to co-design an AI peer review assistant built on Google's open-source Agent Development Kit and running entirely inside Springer Nature's private Gemini Enterprise environment. A prototype is being tested to help reviewers navigate manuscripts and analyze text, charts and figures, with human judgment kept central; no timetable for wider deployment was announced.
Why it matters: A named enterprise deployment of Gemini agents in a sensitive, confidentiality-bound workflow.
Refs: https://group.springernature.com/gp/group/media/press-releases/research-partnership-with-googledeepmind-to-support-peer-review/53891572, https://www.researchinformation.info/news/springer-nature-and-google-deepmind-partner-on-ai-peer-review-assistant/

### 11. Google DeepMind demos Gemini 4 Argon video-to-simulation-to-robot training on Apptronik's Apollo (Google)
Google DeepMind demonstrated a Video-to-Sim-to-Real pipeline in which Gemini 4 Argon watches a raw video, generates simulation code and transfers the learned behavior to Apptronik's Apollo humanoid, which then sank seven consecutive cornhole shots. The company says the process compresses weeks of manual simulation work into hours and that Argon scored 87% on its Embodied Reasoning (ERQA) benchmark.
Why it matters: A concrete physical-world application for a frontier model, extending the competition beyond text and code.
Refs: https://www.zhiding.cn/physical-ai/2026/1026/3203533.shtml

### 12. Grok Imagine releases a seven-minute AI-generated Odyssey episode (xAI)
The Grok Imagine account on X released a roughly seven-minute AI-generated adaptation of Homer's Odyssey, billed as Episode 1 of a series and credited to Wonder Studios and director Dev Walker, months after Elon Musk promised a full-length, historically accurate film by year-end. Coverage reports negative reception, with critics calling the dialogue stiff and the result soulless, and notes the characters speak English rather than Homeric Greek.
Why it matters: A high-profile public test of AI video generation as an entertainment product rather than a demo.
Refs: https://www.indiatoday.in/technology/news/story/elon-musks-grok-releases-the-first-7-minutes-of-its-ai-generated-odyssey-film-3025047-2026-10-26, https://theprint.in/entertainment/elon-musks-grok-releases-an-ai-made-episode-of-the-odyssey-nolan-fans-are-not-impressed/3082149/, https://gizmodo.com/elon-musks-ai-generated-odyssey-is-here-to-save-western-civilization-2000830714, https://unwire.hk/2026/10/26/grok-imagine-ai-odyssey-episode-1/movie-2/

### 13. Alibaba publishes Qwen3.8-Max and Qwen3.8-Flash developer guides (Qwen)
Alibaba Cloud developer articles detail Qwen3.8-Max, a 2.4-trillion-parameter MoE model activating about 95 billion parameters with a 1-million-token context, and Qwen3.8-Flash, a lighter MoE model with the same context length, both callable via the Bailian API and compatible with OpenAI-style interfaces. The guides cover tool calling, context caching, structured output and local vLLM deployment.
Why it matters: Documentation-level detail on Alibaba's flagship and cost-optimized tiers rather than a new launch event.
Refs: https://developer.aliyun.com/article/1775154, https://developer.aliyun.com/article/1775155

### 14. Analysis pieces compare Claude Fable 5.1 and gated Claude Mythos 5.1 (Anthropic)
OrcaRouter analysis describes Claude Fable 5.1 and Claude Mythos 5.1 as sharing weights and pricing ($10 input, $50 output, $0.25 cache read) but differing in safeguards and access, with Mythos gated behind the Cyber Verification Program's Defense, Red Team and Specialized tiers. It cites Anthropic's CyScenarioBench run on Claude Opus 5.5, where no program access blocked every task, Defense Access blocked 46 of 50 trials, and Red Team Access completed 34 of 50.
Why it matters: Explains the access architecture behind Anthropic's most restricted model line, though the underlying releases predate the window.
Refs: https://www.orcarouter.ai/blog/claude-fable-vs-mythos, https://www.orcarouter.ai/zh-CN/blog/claude-fable-vs-mythos, https://www.orcarouter.ai/zh-CN/blog/what-is-claude-mythos

## Cross-Org Themes

- Open-weight Chinese models (Kimi K3.1 Pro, GLM-5.3 Flash, DeepSeek V4.1 Flash) are being benchmarked near closed US frontier models on professional tasks while competing on price
- Persistent personal agents are becoming a product category across Anthropic (Claude Duet), OpenAI (Dots) and Google (Gemini agent plans)
- Compute scarcity is shaping strategy, from Google prioritizing DeepMind over cloud revenue to DeepSeek's large industrial funding round

## Rumors and Unverified Claims

A claim that an official 'Mythos 6' model exists traces only to an unconfirmed X post from July 27, with no benchmarks, identifiers or dates, and Anthropic has said nothing about it. Separately, coverage of Kimi K3.1 Pro notes an unresolved parameter-count dispute, with some accounts describing it as 3-trillion-parameter-class while Moonshot-linked material describes K3 at 2.8T total and 104B active parameters.

## Takeaway

The next evidence to watch is whether promised open weights actually ship, particularly Moonshot's November 4 release, and whether agent reliability figures like OpenAI's disclosed deviation rate hold up under independent testing.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
