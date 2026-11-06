# Giant Watch Summary - Weekly - 2026-11-06

## Headline

Google's Gemini 4 Carbon launch and DeepSeek's super-agent architecture push the frontier toward long-horizon, security-focused agents. The week's strongest signal is Google's staged, cyber-defender-first release of Carbon, which pairs benchmark claims with restricted access.

## Top Developments

### 1. Google DeepMind releases Gemini 4 Carbon, a frontier model focused on cybersecurity and long-horizon engineering (Google)
Google DeepMind released Gemini 4 Carbon on October 28, 2026, two weeks after Gemini 4 Argon. Google says Carbon ranked #1 on Artificial Analysis Intelligence Index v5.0 with 59 points and took top scores on three cybersecurity benchmarks covering vulnerability discovery, exploit validation, and patching. It is rolling out first to cyber defenders through the Fairwind Program, with broader access to follow. Google reports Carbon led 15 of 17 published benchmarks, trailing GPT-6 Astra on FrontierSWE 2 and Claude Opus 5.5 on OSWorld-2.1.
Why it matters: The release puts Google back at the frontier with a security-first positioning and a gated rollout, matching the staged-access pattern used by OpenAI and Anthropic for their most capable models.
Refs: https://global.hk01.com/%E5%AE%9E%E7%94%A8%E6%95%99%E5%AD%A6/60405387/google%E5%8F%91%E8%A1%A8gemini-4-carbon-17%E9%A1%B9%E8%B7%91%E5%88%86%E5%A4%BA15%E5%86%A0-%E7%BD%91%E7%BB%9C%E9%98%B2%E5%BE%A1%E5%8A%9B%E7%A7%B0%E9%9C%B8, https://www.responsibleaifoundation.com/post/google-unveils-gemini-4-argon-after-delays

### 2. DeepSeek unveils experimental 'super-agent' architecture and Harness Creator Mode (DeepSeek)
DeepSeek's Harness team published a technical article on October 31 describing an experimental super-agent architecture built to continuously monitor information, manage multiple tasks in parallel, and act with less human supervision. DeepSeek says an internal version already runs continuously, for example spotting a software defect flagged in a group chat and attempting to reproduce and fix it in the background. On November 2, DeepSeek Harness released a Creator Mode demo showing users creating plugins through conversation. DeepSeek stressed the architecture is an engineering exploration, not a shipped product feature.
Why it matters: It signals a shift in China's model race from benchmark scores toward agent systems that plan and execute real work, with DeepSeek positioning itself around agent infrastructure rather than a single model release.
Refs: https://www.chinadaily.com.cn/a/202611/03/WS6ae9399ae4b06d4aa0566a38.html, https://nw.eastday.com/zq/zh/20261103/a1a94f3866cb01e56beaceb76ac18821.html

### 3. Anthropic introduces Claude Duet, a proactive agent app built on Claude Opus 5.5 (Anthropic)
Anthropic introduced Claude Duet, an app where Claude works as a proactive agent that flags items needing attention, takes on delegated tasks, and runs on its own virtual machine with a browser. It launched in research preview in October 2026 by waitlist for US Pro and Max subscribers on iOS, Android, and claude.ai. Duet requires approval before sending messages, making payments, signing documents, or deleting anything, and a classifier rejects requests involving the strictest sensitive data. It connects to Claude Marketplace plugins including Gmail, Slack, QuickBooks, Stripe, and Shopify.
Why it matters: It is Anthropic's most concrete consumer-facing agent product, pairing autonomous background work with explicit approval gates, and it is included in existing Pro and Max plans rather than sold separately.
Refs: https://cloudfresh.com/gc/news/claude-duet-proactive-ai-agent/

### 4. Z.ai's GLM-5.3 claims open-source SOTA on coding and cybersecurity benchmarks (GLM)
Z.ai documented GLM-5.3 as its latest flagship, built on the same base model as GLM-5.2 with gains from post-training. It reports a 50% coding improvement over GLM-5.2 on its in-house Z.ai Code Bench, Terminal-Bench 3.0 rising from 4.6 to 28.3, and DeepSWE v1.1 from 46.2 to 66.9. On CyberGym it scores 84.5%, ahead of Mythos 5 and GPT-5.6 Sol, and it more than doubled ExploitBench to 54.4%. Z.ai says it worked with Chinese security teams to identify 2,436 vulnerabilities across 269 projects, including 1,097 medium-to-high severity issues, tracked in a public disclosure ledger. GLM-5.3 is also listed on Amazon Bedrock with a 1M-token context window.
Why it matters: It is one of the clearest cases of an open-weight model claiming frontier-adjacent security capability, and the disclosure ledger gives the vulnerability claims a public record to check against.
Refs: https://docs.z.ai/guides/llm/glm-5.3, https://docs.bigmodel.cn/cn/update/new-releases, https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-zai-glm-5-3.html

### 5. Moonshot releases Kimi K3.1 Pro, a 3T-class open-weight model with 1M-token context (Kimi)
Kimi K3.1 Pro is the first model in Moonshot AI's new K3.1 series and its most capable 3T-class open-weight model, post-trained from Kimi K3 with substantially more post-training compute. It has a 1M-token context window and native visual understanding. Moonshot reports 65.7% on Terminal-Bench 4.0, a state-of-the-art 64.4 on OfficeQA Pro v2, and a claim-level hallucination rate cut from 23.4% on K3 to 8.3%. It is served through Alibaba Cloud Model Studio, and Moonshot's model list shows older K2.x models closed to new users with deprecation expected in late December 2026.
Why it matters: It keeps Moonshot in the top tier of open-weight models and shows the K3.1 series displacing the K2 generation on the platform within weeks.
Refs: https://www.alibabacloud.com/help/en/model-studio/kimi-k3-1-pro, https://platform.kimi.ai/docs/models

### 6. Qwen3.8 lineup fully open with split licensing, as Qwen4 stays in training (Qwen)
A developer-community writeup says the Qwen3.8 series finished rolling out in late October 2026, covering Qwen3.8-Max (2.4T total, 95B active), Qwen3.8-27B under Apache 2.0, Qwen3.8-Flash, and Qwen3.8-Flash-Next. Licensing is no longer uniform: Max uses a dedicated license requiring separate authorization for MaaS or AI Work Assistant businesses above revenue thresholds, and Flash-Next uses Qwen Community License 1.0. The report says Qwen4 is still in training and unreleased, and that Flash-Next is only an architecture preview. Alibaba Cloud's Double 11 promotions for Qwen3.8-Flash run through November 30 with separate pay-as-you-go and Token Plan discount tracks.
Why it matters: The licensing split raises commercial compliance questions for cloud and agent builders even as the models themselves are already available, and the promotion terms add a cost-planning layer for developers.
Refs: https://developer.aliyun.com/article/1779272, https://developer.aliyun.com/article/1778601

### 7. Musk says serving Grok costs more than it earns as users hit usage limits (xAI)
Elon Musk acknowledged in a post on X that the cost of serving xAI's Grok is unsustainably high relative to revenue, responding to a user asking whether Grok usage limits could be reset after subscribers reported quotas running out unusually fast. Reports estimate Grok has around 800,000 paid users. xAI has not announced a specific change to subscription prices or a revised usage policy.
Why it matters: It is a rare public admission of unit-economics pressure at a frontier lab and suggests tighter metering or usage caps may follow for X Premium subscribers.
Refs: https://www.varindia.com/news/elon-musk-says-running-grok-ai-costs-more-than-it-earns, https://www.wionews.com/technology/running-ai-is-getting-expensive-why-elon-musk-says-grok-s-costs-are-unsustainable-1793700158228

### 8. Google changes Gemini defaults in schools and ties AI-off to losing Search (Google)
Google announced changes to push students to do their own work: Gemini will no longer be on by default in Google Classroom, and when enabled it will run in Guided Learning mode, which will also replace AI overviews for students using Google Search on school accounts. Google will test the changes with a small group of US schools this month and roll them out more broadly early next year. Districts that want no AI on school devices would have to forgo Google Search, a trade-off critics including Schools Beyond Screens and Common Sense Media called a choice that isn't really a choice.
Why it matters: It shows a major AI provider adjusting defaults under pressure from districts and parents, while making access to its core search product part of the bargain.
Refs: https://www.chalkbeat.org/2026/11/03/google-pushes-gemini-guided-learning-amid-ai-backlash/

### 9. OpenAI publishes LifeVal benchmark for everyday assistant tasks (OpenAI)
OpenAI described LifeVal, a task evaluation covering areas where users most want AI and personal agents to help, including childcare, health, education, household management, personal finance, shopping, and government services. OpenAI says it built the task set from US and international time-use studies plus a survey of 3,995 demographically representative respondents, and that its latest models score highly on many LifeVal tasks. OpenAI frames the work as measuring whether models can act on everyday tasks rather than only answer questions.
Why it matters: It is an evaluation-framing release rather than a product launch, but it signals OpenAI positioning ChatGPT as an action-taking personal assistant and setting a public yardstick for that claim.
Refs: https://openai.com/zh-Hant/index/lifeval/

## Cross-Org Themes

- Frontier labs are gating their most capable models to vetted security partners before broad release
- Agent systems that work continuously in the background are the shared product direction across US and Chinese labs
- Cybersecurity capability is becoming a headline benchmark category for new frontier models

## Rumors and Unverified Claims

A report says DeepSeek's next-generation V5 model is planned to be pretrained on Huawei Ascend 950 chips, which would be its first model natively trained on Ascend hardware; this is attributed to a reporter's confirmation and has no official DeepSeek announcement in the supplied material. A community writeup also notes that a 'Qwen3.8 early access' entry point or redemption code circulating online could not be found on official channels.

## Takeaway

The next evidence to watch is whether gated security-first releases like Gemini 4 Carbon reach general developers on the timelines their vendors imply, and whether agent products such as Claude Duet and DeepSeek's super-agent move from preview and internal use into measurable production workloads.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
