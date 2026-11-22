# Giant Watch Summary - Daily - 2026-11-22

## Headline

OpenAI 将 Dots 智能体测试范围扩大到 ChatGPT Plus，同时 Google 发布 Gemini 4 Carbon，并预览 Antigravity 中的多智能体 swarm；这一天的主题是：常驻后台的智能体正从高价档位下探到更便宜的订阅层。

## Top Developments

### 1. OpenAI 面向部分 ChatGPT Plus 用户测试 Dots 智能体 (OpenAI)
OpenAI 正在面向一小批 ChatGPT Plus 订阅用户测试 Dots，同时向美国符合条件的 ChatGPT Business Standard 成员推出该功能，每人可创建一个 Dot。Dots 是运行在云端自有计算机上的后台智能体，可连接 4,000 多个应用，并通过 Slack 和 Teams 通信；该产品于 2026 年 9 月 29 日面向 Pro、Business Premium 和 Enterprise 推出，最初使用 GPT-6 Astra，现在也可使用 GPT-6.1 Terra。OpenAI 未披露参与测试的 Plus 账户数量，也未说明该测试是否会转为永久上线；欧洲、英国和瑞士仍不在覆盖范围内。
Why it matters: 这是常驻后台的智能体首次从高价档位下探到 20 美元档位，尽管目前只是按账户逐个挑选的测试；报道将该产品与 Google 的 Gemini Spark 和 Microsoft 的 Copilot Autopilot 列为同类竞争产品。
Refs: https://www.ma-no.org/en/news-and-events/technology/openai-tests-dots-with-some-chatgpt-plus-users

### 2. Google 发布 Gemini 4 Carbon，并预览 Antigravity 中的多智能体 swarm (Google)
Google 面向开发者、企业、科研人员和消费者发布了 Gemini 4 Carbon，定位是长周期智能体工作流、复杂软件工程、网络安全和科学推理。Google 还在 Antigravity 中预览了 /swarm，让多个智能体分别承担架构、实现和审查等角色协同工作。API 介绍价为每百万输入 token 2 美元、每百万输出 token 10 美元；Google 报告的基准测试结果属于厂商自述。
Why it matters: 这是 Google 本周最重要的模型发布，把多智能体编排直接做进产品，而不是留给外部框架；其定价也把前沿模型的能力放到了与 OpenAI 和 Anthropic 竞争的位置上。
Refs: https://jhparmar.medium.com/the-big-picture-ff9d1b1c8e1b, https://www.kongchang.com/articles/gpt-6-2xian-shen-apiwen-dang-gemini-4-carbonshang-xian, https://departmentofproduct.substack.com/p/replit-google-and-vercel-are-betting?utm_source=%2Finbox%2Fpost%2F137647493&utm_medium=reader2

### 3. xAI 上线 Grok 4.7、Grok Agents 和 Grok Voice 3.0 (xAI)
xAI 发布了 grok-4.7 API 模型，支持文本和图像输入，上下文窗口为 500,000 token，并可配置推理强度；20 万 token 以下的提示词定价为每百万输入 token 2 美元、每百万缓存输入 token 0.50 美元、每百万输出 token 6 美元。Grok Agents 是一个面向目标驱动智能体的开发者平台，可浏览网页、执行代码、处理文件并调用自定义工具，智能体工具价格下调最多 50%，每次成功调用收费上限为 5 美元/1,000 次。Grok Voice 3.0 以与 2.0 相同的价格上线，grok-build-0.1 于 11 月 19 日停止服务。
Why it matters: 这是 xAI 本季度对开发者平台最大的一次扩展，把工具调用变成了可计量的预算单位；同时 grok-build-0.1 的退役给仍在调用该模型的部署带来了直接的兼容性问题。
Refs: https://www.bighatgroup.com/blog/xai-weekly-2026-11-16/

### 4. Meta 将 2026 年资本支出指引收窄至 1,350 亿至 1,450 亿美元，用于 AI 基础设施 (Meta)
在第三季度财报中，Meta 将 2026 年资本支出指引收窄至 1,350 亿至 1,450 亿美元，高于此前 1,300 亿至 1,450 亿美元的预测区间，其中大部分用于 AI 基础设施，包括数据中心、芯片、网络设备以及训练 Llama 模型所需的系统。第三季度营收为 646 亿美元，同比增长 26%，其中广告收入 630.6 亿美元；广告展示量增长 10%，单次广告平均价格上涨 14%；自由现金流为 -21.2 亿美元。Meta 计划发行无投票权的 C 类股票，并通过股权融资筹集最多 950 亿美元。
Why it matters: 这大约相当于 Meta 2025 年约 720 亿美元资本支出的两倍，而且是在自由现金流为负的情况下推进；它表明前沿实验室的竞争正越来越多地由资产负债表来支撑。
Refs: https://cryptobriefing.com/meta-145-billion-ai-capex-advertising/, https://www.techub.news/flash/93c827af-4951-4f51-a2ac-8477314b6030

### 5. DeepSeek 对免费 App 和网页端设置对话限制，且没有付费升级通道 (DeepSeek)
11 月 15 日前后，DeepSeek 的免费 App 和网页端用户开始看到三类限制：超过 7 天不活跃的长对话不再支持续聊；单次输入上限压缩到约 4 万字；每日额度用完后会显示“服务器繁忙，使用额度已达上限”。API 使用独立资源池，不受影响。DeepSeek 没有发布公告，也没有给出恢复时间表；小米应用商店评分一度跌至 2.6 分，App Store 评分降至 3.8 分。报道将这一情况与调用量增长联系起来：OpenRouter 数据显示，11 月 9 日至 15 日当周，DeepSeek V4.1 Flash 的 token 调用量达到 59.2 万亿，而 9 月中旬为 15.8 万亿；10 月以来官网记录了 10 起故障。
Why it matters: DeepSeek 的消费级产品没有订阅档位，因此在算力紧张时只能直接限制用量；这与其他实验室把智能体能力下探到更便宜档位的做法形成鲜明对比。
Refs: https://zicode.com/blog/deepseek-limit-agent-route-split/

### 6. 阿里云开放 Qwen4-Max 预览版，最低 1 折 (Qwen)
阿里云开放了 Qwen4-Max 预览版（模型标识 qwen4-max-preview），这是 Qwen 第四代旗舰模型，支持 100 万 token 上下文，输入覆盖文本、图片和视频，输出为文本，并原生支持 Function Calling、联网搜索和结构化输出。定价为限时 2 折，叠加新用户 5 折后最低 1 折；新用户还可获得超过 7,000 万免费 token。预览版仅通过 Token Plan 订阅提供，不支持按量计费；qwen4-max-preview 标识将于 11 月 25 日 24:00 下线，正式版将以新名称发布。
Why it matters: 这是 Qwen 第四代旗舰模型的首次公开亮相，其折扣定价和仅限订阅的接入方式，是阿里云在开发者采用上的一次直接尝试。
Refs: https://developer.aliyun.com/article/1787052

### 7. 智谱（Z.AI）旗舰模型价格逐代上涨，尽管权重保持开放 (GLM)
Z.AI 于 8 月 25 日在 Hugging Face 上发布了 GLM-5.3 的权重，此前一周已通过自家 API 上线，定价为每百万输入 token 1.4 美元、每百万输出 token 4.4 美元；1 月的旗舰模型 GLM-4.7 定价为 0.6 美元和 2.2 美元。每个模型都保持首次上架时的价格，但每一代新旗舰的价格都等于或高于上一代，因此从 1 月到 11 月，旗舰档位的价格在输入上上涨了 133%，在输出上上涨了 100%。公司中期业绩显示，token 调用量增长超过 40 倍，平均 API 售价上涨约 101%；上半年营收为 9.539 亿元人民币，其中开放平台和 API 收入为 8.252 亿元，占 86.5%，半年亏损为 20.72 亿元。GLM-5.3 采用了自定义许可证，要求年收入超过 100 亿美元的模型即服务提供商先通过安全审查。
Why it matters: 这是对“开放权重会压低模型价格”这一直觉的反例：智谱的定价能力跟随其最新旗舰模型，而研发成本仍是服务模型所获毛利的八倍多。
Refs: https://www.icmintelligence.com/p/open-weights-did-not-cap-zhipus-price

### 8. OpenAI 推广 ChatGPT Edu，面向高校部署 (OpenAI)
OpenAI 的 ChatGPT Edu 页面面向高校，提供比免费版 ChatGPT 更高的消息额度，并称 GPT-5 是其旗舰模型。页面列出的控制项包括：不使用数据或对话训练 OpenAI 模型、SAML SSO 和域名验证、自定义数据保留期限、SOC 2 Type 2 以及 ISO 27001/27017/27018/27701 认证、静态 AES-256 加密和传输 TLS 1.2+ 加密、SCIM、群组权限、GPT 管理、用户分析面板、统一账单和优先支持。
Why it matters: 这是 OpenAI 面向机构渠道的分发动作，其隐私和合规承诺直接针对高校采购要求；不过该页面是产品页面，而非新发布的公告。
Refs: https://chatgpt.com/zh-Hant-HK/business/education/?openaicom-did=62c3d4ae-8322-4858-abb5-65efe4fbbf3a&openaicom_referred=true, https://chatgpt.com/zh-Hans-CN/business/education/?openaicom_referred=true

## Cross-Org Themes

- 常驻后台的智能体正从高价档位下探到更便宜的订阅层：OpenAI 的 Dots 进入 Plus 测试，Google 在 Antigravity 中预览 swarm，xAI 上线 Grok Agents
- 算力经济学正在分化：Meta 将资本支出提高到 1,350 亿至 1,450 亿美元，DeepSeek 限制免费用量，阿里用 1 折推广 Qwen4-Max，智谱则逐代提高旗舰模型价格

## Rumors and Unverified Claims

有报道称 Anthropic 以每股 83 美元完成 IPO，代码为 ANT，并完成 260 亿美元私募配售；同一报道还称 Levent Alpöge 在与 Claude 协作下找到黎曼猜想的证明（目前仅以 Lean 形式化形式发布），以及 Claude Fable 5.2 解决了两个黑洞物理开放问题。另有报道称 OpenAI 上线了 GPT-6.2 Astra 和 GPT-6.2 Sol，并称 GPT-6.2 已出现在 OpenAI API 文档中。xAI 方面，有报道称 Grok 4.8 处于强化学习阶段，并在 Grok Bot 内进行软启动，另有 Grok 4.20 和 Grok 4.20 Multi-agent 的发布追踪记录。此外，有报道称 Google 开始向 Google AI Ultra 用户开放 Gemini 4 Carbon，并推出面向医疗领域的 Gemini 计划。

## Takeaway

接下来要观察的是：OpenAI 的 Dots Plus 测试是否会转为永久上线，以及 Google 和 xAI 的智能体平台能否给出独立于厂商自述的基准测试结果。与此同时，DeepSeek 的免费档位限制是否会伴随付费档位出现，将检验“没有价格杠杆”这一判断。

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
