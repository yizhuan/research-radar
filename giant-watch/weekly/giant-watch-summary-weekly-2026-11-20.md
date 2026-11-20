# Giant Watch Summary - Weekly - 2026-11-20

## Headline

OpenAI released GPT-6.2 Astra and Sol, the week's most consequential frontier-model launch, as Google, Alibaba, Z.ai and Moonshot all shipped new flagship models within days. The episode's thesis: competition has shifted from raw capability to efficiency and agentic coding, with vendors touting fewer output tokens and lower cost per task.

## Top Developments

### 1. OpenAI releases GPT-6.2 Astra and GPT-6.2 Sol (OpenAI)
OpenAI introduced GPT-6.2 Astra, its frontier model for advanced reasoning, coding and complex professional work, alongside GPT-6.2 Sol, a faster, lower-cost model for multi-step tasks. Both are available via the Responses and Chat Completions API as gpt-6.2-astra and gpt-6.2-sol, accept text and images, and are said to improve on predecessors while generating fewer output tokens. Bloomberg reported Astra arrives nearly two months after OpenAI scrapped a prior update to establish stronger safeguards.
Why it matters: The week's highest-profile frontier release, and the clearest signal that OpenAI is pairing a top-end model with a cheaper everyday tier while emphasizing token efficiency.
Refs: https://help.openai.com/en/articles/9624314-model-release-notes, https://www.bloomberg.com/news/articles/2026-11-17/openai-unveils-new-astra-ai-model-after-scrapping-prior-release, https://www.theverge.com/tech/1035483/openai-releases-its-updated-gpt-6-2-astra-model, https://www.cnet.com/tech/services-and-software/openai-chatgpt-astra-6-2-microsoft-ignite-news/

### 2. Google publishes Gemini 4 Neon model card and developer guide (Google)
Google DeepMind published a model card for Gemini 4 Neon, a model adapted from Gemini 4 Carbon and positioned between Carbon for long-horizon projects and Hydrogen for fast everyday execution. It targets complex coding, analytical reasoning and enterprise workflows, with a unified 1M-token context window, long decodes up to 1M tokens, thinking levels up to XHIGH, and orchestration of Hydrogen subagents. Google says a full Safety & Security Report is coming and that Neon's capability increase over Argon fell below its Material Capability Change threshold.
Why it matters: Establishes Google's three-tier Gemini 4 lineup and pushes multi-model orchestration and very long output as enterprise differentiators.
Refs: https://deepmind.google/models/model-cards/gemini-4-neon/, https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-neon, https://www.cnet.com/tech/services-and-software/openai-chatgpt-astra-6-2-microsoft-ignite-news/

### 3. Alibaba Cloud documents Qwen4-Max flagship multimodal model (Qwen)
Alibaba Cloud's Model Studio documentation describes qwen4-max as Tongyi Qianwen's new-generation flagship multimodal model, combining text generation, image and video understanding and deep thinking for programming, office work, front-end design and complex agent tasks. It supports web search, parallel tool calls, structured output, explicit and implicit caching, and compatibility with OpenAI and Anthropic APIs, with a 1M-token context and up to 262,144 output tokens in thinking mode. Listed pricing is $1.5/$4.5 per million input/output tokens in Singapore and $1.413/$4.24 in other regions.
Why it matters: A direct multimodal flagship play that also courts developers through OpenAI and Anthropic API compatibility and aggressive per-token pricing.
Refs: https://www.alibabacloud.com/help/en/model-studio/qwen4-max

### 4. Z.ai releases GLM-5.3 with coding and cybersecurity gains (GLM)
Z.ai published documentation for GLM-5.3, which reuses the GLM-5.2 base model with all improvements from post-training. It claims a 50% coding gain over GLM-5.2 on Z.ai Code Bench, state-of-the-art open-source results on Terminal Bench 3.0 and Agents' Last Exam, and the best CyberGym score to date at 84.5%, with ExploitBench more than doubling to 54.4%. The model is text-only with a 1M-token context, 128K max output, always-on reasoning with low/high/max effort levels, and is available to GLM Coding Plan users.
Why it matters: Shows post-training and environment scaling alone can move agentic and security benchmarks substantially, and flags fast-emerging offensive cyber capability in open models.
Refs: https://docs.z.ai/guides/llm/glm-5.3

### 5. Moonshot launches Kimi K3.1 Pro and a Highspeed variant (Kimi)
Moonshot's platform documentation introduces Kimi K3.1 Pro, the first model in the K3.1 series and described as its strongest 3-trillion-parameter model, with a 1M-token context and gains in coding, 3D creation, financial research and long-horizon agent tasks. It reports 65.7% on Terminal-Bench 4.0, above GPT-6 Astra at 58.2% and just below Claude Opus 5.5 at 66.4%, and 61.2% on its internal Kimi Code Bench 3.0 Long-horizon. A Kimi K3.1 Pro Highspeed variant offers the same intelligence at roughly 2-3x output speed; reasoning is always on with low/high/max effort.
Why it matters: A flagship API launch paired with a speed-optimized tier; its benchmark results and capability claims are company-reported and await independent replication.
Refs: https://platform.kimi.com/docs/guide/kimi-k3-1-pro-quickstart

## Cross-Org Themes

- Flagship launches converge on 1M-token context windows and always-on or tiered reasoning effort
- Efficiency framing: vendors emphasize fewer output tokens, lower cost per task, or speed-optimized variants
- Agentic coding and long-horizon task execution are the headline benchmarks across releases
- API compatibility and multi-model orchestration are pitched as enterprise adoption levers

## Rumors and Unverified Claims

CNET reported that Anthropic is becoming a public company this week with an opening price of $83 per share and a $1.5 trillion valuation, and described turmoil at Nvidia including a 14% stock dip and $1 trillion in lost value; these claims appear only in that single report and were not corroborated by supplied sources. CNET also mentioned Microsoft's seven new MAI models at Ignite, which fall outside the tracked organization list.

## Takeaway

The competitive axis is shifting from headline capability to cost-per-task and agentic reliability, so the next evidence to watch is independent benchmark replication and the still-pending safety reports, notably Google's Gemini 4 Neon Safety & Security Report. No qualifying in-window developments emerged for Anthropic, Meta, DeepSeek or xAI in the gathered evidence, leaving their positioning unclear.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
