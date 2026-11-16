# Giant Watch Summary - Daily - 2026-11-16

## Headline

Google DeepMind 与 Artificial Analysis 联合发布 MKA 基准，将智能体评测推向真实专业交付物；同一天，企业采用与安全暴露两条线索显示，智能体正同时进入生产系统与风险面。

## Top Developments

### 1. Google DeepMind 联合 Artificial Analysis 发布 MKA 专业任务基准 (Google, Anthropic)
Google DeepMind 与 AI 分析机构 Artificial Analysis 联合开发 Multimodal Knowledge Agent（MKA）基准，要求模型基于建筑图纸、电子电路图和临床影像等复杂视觉材料产出报告、电子表格等可交付成果。基准含 200 项任务，覆盖商业、建筑、工程、金融、医疗、科学等 10 个领域、83 个岗位，每项任务模拟熟练从业者 3 至 8 小时的工作量，平均约 70 条细分评分标准，事实准确性权重 75%、视觉完成度 25%。所有模型使用相同工具与工作环境，最多 250 次操作，专家评估与 AI 评估一致率 96%。已公布结果中 Anthropic 的 Claude Fable 5.2 以 57% 综合加权得分居首，Google 的 Gemini 4 Carbon 以 54% 位列第二；单任务平均成本分别为 31.97 美元与 6.29 美元。
Why it matters: 把智能体评测从问答正确率推进到端到端交付物、成本与效率，并首次在同一受控环境中给出 Claude 与 Gemini 在专业工作场景下的可比排名，为后续企业采购与模型定位提供参照。
Refs: https://www.digitaltoday.co.kr/en/view/125905/google-deepmind-releases-benchmark-for-professional-tasks-reading-blueprints-and-clinical-images, https://www.digitaltoday.co.kr/cn/view/125921/google-deepmind-releases-benchmark-for-professional-tasks-reading-blueprints-and-clinical-images

### 2. Revolut 以智谱 GLM 替换 OpenAI 与 Anthropic 编程助手 (GLM, OpenAI, Anthropic, DeepSeek, Qwen)
在里斯本举行的 2026 年网络峰会上，联合创始人帕迪·科斯格雷夫表示，英国金融科技企业 Revolut 已将原先使用的 OpenAI 与 Anthropic 编程助手替换为智谱开源 GLM 系列模型。Revolut AI 基础设施负责人戴维·阿比特博尔称，GLM 现已成为约 2000 名工程师的默认编程模型，上线以来平均编程耗时缩短约 60%，AI 相关调用成本下降近 90%。报道同时提到，Orange、雷诺、西门子等企业已公开表示使用 DeepSeek 和通义千问等中国模型作为欧美模型的补充，并强调开源模型可免费下载、支持二次修改、可部署在企业自有服务器上。
Why it matters: 这是闭源美国编程助手被中国开源模型整体替换的具名企业案例，把开源模型在成本、部署自主权上的优势转化为可量化的工程指标，对欧美企业的模型选型构成直接参照。
Refs: https://stcn.com/article/detail/4337407.html, http://jjckb.xinhuanet.com/20261116/3abc43906c8841d3a83e9d187fa85533/c.html, http://gubapost.eastmoney.com/news,hk02513,1796334446.html

### 3. DeepSeek 开放“全家桶”应用 API，V4.1-Flash 支持搜索、文件与链接读取 (DeepSeek)
据 DeepSeek 公众号，11 月 13 日 DeepSeek 正式开放“全家桶”应用 API，将 App 的交互功能整合进原有 API：开启对应参数即可获得深度思考搜索、文件输入等对话能力，语音及底层能力（含 OCR、ASR、TTS）也已开放独立接口，支持单独或组合调用，开发者可借此在自有应用中复刻完整 DeepSeek App。V4.1-Flash 模型（deepseek-flash）已在 Messages、Responses 与 Chat Completions 接口下支持联网搜索（deepseek_web_search）、思考模式下的多步推理联网搜索与链接阅读、PDF/Office/图片文件输入、链接抓取（deepseek_read_url）以及模型安全校验参数；工具调用与上下文拼接由服务端自动完成。
Why it matters: 把消费端 App 的完整交互栈产品化为 API，降低了开发者构建复杂对话应用的门槛，也使 DeepSeek 的竞争面从模型能力延伸到应用层工具链与内容安全合规。
Refs: https://news.mysteel.com/a/26111608/F9B5FA104AC06107.html

### 4. OpenAI 推出 Businesses in ChatGPT 公测：企业档案与 Business Agent (OpenAI)
OpenAI 于 2026 年 11 月 10 日以公测形式推出 Businesses in ChatGPT，企业可认领并验证 ChatGPT 内的商家档案，并在美国面向电商与在线服务企业部署品牌化的 Business Agent，用企业自有的产品与政策文档回答客户问题。Business Agent 仅依据企业提供的信息作答，不得虚构功能、价格或政策，并可作为 ChatGPT Ads 的投放落地页，与自然结果以标签区分。认领档案与创建 Agent 在发布阶段免费，OpenAI 未承诺长期维持该定价；OpenAI 表示不会向企业分享用户对话或 Agent 会话内容，认领档案也不保证排名。报道称 ChatGPT 约有 12 亿周活用户。
Why it matters: ChatGPT 从私人生产力工具变为企业可直接经营的客户渠道，把“被模型如何描述”变成可认领、可纠正、可付费推广的对象，同时把广告与 Agent 合规问题一并推到台前。
Refs: https://davidandgoliath.ai/daily-ai-briefing/openai-chatgpt-business-profiles-agents-launch

### 5. Grok Build 默认共享设置与 URL 设计导致大量应用数据暴露 (xAI, Meta)
安全公司 Claroc 发现，xAI（被 SpaceX 收购后称 SpaceXSI）运营的 vibe coding 智能体 Grok Build 因默认共享权限为“Anyone with the link”，且随机字符串出现在 grok.me 子域名而非 URL 路径中，导致应用地址可被被动 DNS 服务批量收集。Claroc 检查了逾 4 万个 grok.me 子域名，确认其中 37,571 个在线，35,578 个（94.7%）无需单独登录即可访问应用界面并暴露数据。暴露内容包含 SpaceXSI 自身 24 个应用中的内部商业计划、广告提案、新员工入职计划、覆盖 594 家客户公司的销售区域图等，也涉及财富 500 强与国防承包商员工的数据，以及一家秘鲁建筑公司含 3,784 名工人体检记录的职业健康看板。Claroc 于 11 月 8 日通知 SpaceX，未获回应；Ars Technica 询问后数小时内，SpaceXSI 移除了自家 24 个应用的链接，但未对其他用户应用施加额外访问限制。报道同时提及 Meta Muse 因共享链接主机名含对话标题、可经 DNS 记录重建，已于 10 月 20 日暂停对话分享功能。
Why it matters: 这是 AI 编程平台默认安全设计缺陷导致企业机密与个人敏感数据大规模暴露的具名案例，暴露出 vibe coding 应用普遍游离于企业安全治理之外，也为同类平台（Lovable、Bolt、Replit 等）的 URL 与权限设计敲响警钟。
Refs: https://www.thelec.net/news/articleView.html?idxno=15621

## Cross-Org Themes

- 智能体从对话走向可交付成果与可经营渠道，评测、API 与企业入口同步产品化
- 开源与闭源模型在企业侧的替换已出现具名案例与可量化成本差异
- AI 应用层的默认权限与链接设计正成为企业数据暴露的主要风险面

## Rumors and Unverified Claims

OpenAI 开发者社区中有用户称 GPT-6 存在推理能力下降、指令遵循失败与严重幻觉等问题，并呼吁在问题解决前暂停退役 GPT-5.5；OpenAI 支持人员仅表示会转达反馈，无法保证变更或给出时间表。另有用户反对 OpenAI 于 12 月 11 日退役 Standard Voice，并质疑转向 GPT-Live 是为降低推理成本，相关成本动机未获证实。

## Takeaway

同一天的材料显示，智能体竞争已从模型分数转向交付物质量、单位成本与分发渠道，而默认安全设置正成为这条链路上最薄弱的一环。下一步值得关注的是 MKA 类基准能否被企业采购流程采纳，以及 Grok Build 事件后同类平台是否调整默认可见性与 URL 结构。

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
