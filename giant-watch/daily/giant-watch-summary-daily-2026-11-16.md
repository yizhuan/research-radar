# Giant Watch Summary - Daily - 2026-11-16

## Headline

Alibaba's Qwen4-Max launch is the day's strongest single event, with a 2.4-trillion-parameter MoE flagship and claimed task-cost cuts of over 60%. The episode's throughline is vendors competing less on raw model quality than on cost per completed task and the surrounding toolchain.

## Top Developments

### 1. Alibaba launches Qwen4-Max flagship with 2.4T-parameter MoE and 1M-token context (Qwen)
Alibaba's Tongyi Qianwen team announced the formal release of Qwen4-Max, a sparse MoE flagship with 2.4 trillion total parameters, native visual understanding and a 1M-token context window, following a limited preview on Nov. 11. The company reported a Work360 score of 52.69 versus 47.74 for Qwen3.8-Max, roughly 24-35% lower token consumption at Xhigh and High reasoning effort, and average per-task cost falling from 26.58 yuan to 11.16 yuan (about 58%). Qwen4-Max is available via QwenCloud, Qwen Studio, QwenWork and Qoder, with smaller Qwen4 models to be open-sourced later.
Why it matters: The most concrete model release in the window, and it is framed explicitly around cost per completed professional task rather than benchmark scores alone, with a stated plan to open-source smaller siblings.
Refs: https://www.ithome.com/1/027/512.htm, https://www.toutiao.com/article/7708588669296247323/?wid=1794796441175#comment, https://www.sohu.com/a/1102094706_100106801?scm=10001.7746_13-119000.0.0-0-0-0-0.0&spm=smpc.channel_354.block3_32_P7Ovbu_1_fd.48.1794796823235hjWgehR_7746, https://www.8world.com/greater-china/alibaba-launches-qwen4-max-ai-model-cutting-task-costs-60-3341766, https://help.aliyun.com/zh/model-studio/qwen4-max

### 2. DeepSeek opens its full app capability stack as API tools, undercutting rivals on search pricing (DeepSeek)
DeepSeek released a 'full-stack application API' on Nov. 13 that folds web search, deep-thinking search, file input, URL reading and basic safety checks into its existing chat interfaces, plus standalone Search, Fetch, OCR, ASR and TTS endpoints. Developers declare deepseek_web_search and deepseek_read_url and the server handles tool execution and context assembly; thinking mode allows roughly 20 tool calls. DeepSeek charges 5 yuan per thousand searches versus $10 per thousand cited for comparable OpenAI and Anthropic tools, and the features work across Messages, Responses and Chat Completions formats. Commentators noted trade-offs: tool_choice cannot force a tool, domain allow/deny lists are not offered, and some sampling parameters are overridden server-side.
Why it matters: Moves competition from model quality to who owns the toolchain layer, and does so at a price point that pressures OpenAI, Anthropic and Google hosted-tool pricing.
Refs: https://www.infoq.cn/news/NWmk4epBL0jPAUtpKSKb, https://www.infoq.cn/article/NWmk4epBL0jPAUtpKSKb?utm_source=rss&utm_medium=article, https://cloud.tencent.com.cn/developer/article/2785375

### 3. Google DeepMind and Artificial Analysis release MKA benchmark for professional agent work (Google, Anthropic)
Google DeepMind unveiled the Multimodal Knowledge Agent benchmark, developed with Artificial Analysis, which feeds agents complex visual inputs such as architectural drawings, circuit schematics and clinical images and requires deliverables like reports and spreadsheets. It spans 200 tasks across 83 job roles in 10 fields, each modeled on 3-8 hours of skilled human work, scored on roughly 70 criteria per task weighted 75% factual accuracy and 25% visual completeness, with 96% agreement between expert and AI graders. In published results Anthropic's Claude Fable 5.2 ranked first at 57% weighted attainment and Google's Gemini 4 Carbon second at 54%, but Gemini averaged $6.29 per task against $31.97 for Claude.
Why it matters: A rare same-window, cross-vendor evaluation that reframes agent competitiveness around deliverable completeness and cost efficiency, and it puts Anthropic and Google head to head on Google's own benchmark.
Refs: https://www.digitaltoday.co.kr/en/view/125905/google-deepmind-releases-benchmark-for-professional-tasks-reading-blueprints-and-clinical-images, https://www.digitaltoday.co.kr/cn/view/125921/google-deepmind-releases-benchmark-for-professional-tasks-reading-blueprints-and-clinical-images

### 4. Anthropic ships Claude Fable 5.2 and Mythos 5.2 plus a Meetings, Whiteboards and Sheets office suite (Anthropic)
Anthropic released Claude Fable 5.2, open to all users, and Mythos 5.2, which has looser cyber-security guardrails and is limited to certified companies. It reported gains in coding, reasoning and science plus new robotics abilities and a lower price per token, though its own charts show higher cost than the prior model above high effort settings. Alongside the models it launched Claude Meetings, which joins video calls to draft plans, answer questions and record actions, plus Claude Whiteboards and Claude Sheets, which together with Claude Docs move Claude toward a full office suite with wider data and app integrations.
Why it matters: Signals Anthropic treating the model as insufficient differentiation on its own and building an ecosystem suite, while splitting a restricted high-capability variant for vetted security customers.
Refs: https://valliance.ai/compass/2026-11-16-anthropic-office-suite-fable-chatgpt-business-agents-people-gap?utm_campaign=377246952-Newsletter+-+2026&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--UNNyx8j6i2jwTQPXyswvmVKefKzvKztTgy_D22ID-v3qc3Iwg6Mzll5wGjp6hBDGEw323

### 5. OpenAI beta lets verified businesses claim ChatGPT profiles, add product feeds and sponsor an agent (OpenAI)
OpenAI launched a beta letting verified businesses claim and manage a ChatGPT profile, add product feeds with pricing, and see aggregated mentions and clicks. Businesses can also set up an agent that answers on their behalf and pay to sponsor it through ChatGPT Ads, starting with US e-commerce. The same Valliance roundup frames this as a brand and governance question as much as a marketing one, since someone must own what the agent is allowed to say.
Why it matters: Turns ChatGPT into a commercial surface with sponsored business agents, extending OpenAI's reach into local and product discovery and creating a new governance burden for brands.
Refs: https://valliance.ai/compass/2026-11-16-anthropic-office-suite-fable-chatgpt-business-agents-people-gap?utm_campaign=377246952-Newsletter+-+2026&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--UNNyx8j6i2jwTQPXyswvmVKefKzvKztTgy_D22ID-v3qc3Iwg6Mzll5wGjp6hBDGEw323

### 6. Nokia, Nscale, Skeleton, Telia and Verda form AI Gigafactory Northern consortium (Cross-organization)
Five European technology companies announced AI Gigafactory Northern, a federated multi-site AI gigafactory across the Nordic and Baltic region combining large-scale AI compute, sovereign cloud and AI platform services, high-capacity connectivity and decarbonized energy. Sites are planned in Oulu, Finland; Iru, Estonia; Valmiera, Latvia; and an undetermined Swedish location, with VTT and KTH as research partners. The partners intend to bid under the EuroHPC JU call for AI Gigafactory consortia, with bid deadlines of Dec. 3 for large-scale facilities and Feb. 4 2027 for medium-sized ones, against an EU InvestAI target of mobilizing €30 billion.
Why it matters: A concrete sovereign-infrastructure bid that shows European compute capacity being organized as cross-border consortia rather than single national projects.
Refs: https://www.nokia.com/newsroom/european-technology-leaders-form-ai-gigafactory-northern-consortium-to-build-trusted-sustainable-ai-infrastructure/, https://datacentremagazine.com/news/nokia-nscale-skeleton-telia-verda-form-ai-consortium, https://www.telecomtv.com/content/next-gen-telco-infra/telia-nokia-form-ai-gigafactory-alliance-56693/, https://www.telecomtv.com/content/next-gen-telco-infra/telia-joins-european-technology-leaders-in-forming-ai-gigafactory-northern-consortium-56692/, https://www.163.com/dy/article/LBS8MU8305198CJN.html?spss=dy_author

### 7. Adobe and Google expand partnership embedding Acrobat in Workspace and Google models in Adobe apps (Google)
Announced Nov. 10 at Adobe MAX and covered in the window, the expanded Adobe-Google partnership puts Acrobat into Google Workspace via Drive and Gmail, expands Adobe connectors in Gemini and Gemini Enterprise, and brings Adobe creative tools to AI Mode in Google Search. Google imaging and video models including Gemini Omni, Veo and Nano Banana come to Firefly, Photoshop, Premiere and Adobe Express, the Gemini model family helps power AI Assistant in Acrobat, and Adobe and Google DeepMind will collaborate on AI-powered editing starting with Photoshop. Adobe cites more than 1 billion monthly active users and more than 400 billion PDFs opened with Acrobat annually.
Why it matters: Consolidates document and creative workflows inside Google's surfaces, giving enterprises a single governance perimeter for AI-assisted content work and giving Google distribution into Adobe's installed base.
Refs: https://softprom.com/google-adobe-ai-partnership-workspace-gemini

### 8. Moonshot positions Kimi K3.1 Pro for scientific discovery via DP Technology collaboration (Kimi)
Moonshot AI is pushing Kimi into biology, chemistry and pharmaceutical research, with international director Giacomo Ficari telling Web Summit that coding is approaching saturation while science raises the intelligence bar. DP Technology announced a collaboration integrating Kimi K3.1 Pro into its BioMaster research agent for biomedical applications, saying the model paired with its coding tool scored highest in an internal evaluation; in one demonstration the pair analyzed gene-expression data from 3,696 mouse pancreatic cells and identified 100 candidate genes in about 90 minutes versus an estimated four hours of human work. Coverage notes the results stop short of autonomous breakthroughs, citing a paper co-authored by Moonshot founder Yang Zhilin and Andrew Yao in which no frontier model independently solved the benchmark's open mathematical conjectures.
Why it matters: A named commercial partnership that tests whether agentic models can win scientific workloads, while the accompanying caveats keep expectations calibrated.
Refs: https://www.scmp.com/tech/article/3374568/chinas-moonshot-ai-puts-kimi-models-race-science-discoveries?module=flexi_unit-focus&pgtype=homepage

### 9. Moonshot AI moves to unwind its Cayman holding structure ahead of a reported Hong Kong IPO (Kimi)
According to Wall Street Journal reporting cited in the window, Moonshot AI plans to terminate its Cayman holding company, repurchase shares held by early investors and have them reinvest into the mainland operating entity, a step read as preparation for a Hong Kong listing. Reports cite a roughly $50 billion latest financing valuation, a possible first-quarter 2027 listing and a fundraising ceiling of up to $5 billion, while noting these are reported figures rather than final IPO pricing. Coverage also cites ARR rising from $15 million at end-2025 to $1 billion in August 2026 with a $2 billion year-end target, and warns that Kimi K3 and K3.1 Pro inference costs remain several times higher than DeepSeek's.
Why it matters: The clearest signal yet that a leading Chinese model lab is moving from private financing logic to public-market governance, with cost structure becoming an investor question.
Refs: https://eu.36kr.com/en/p/4069761666176645, https://gfe-desktop.cnyes.com/news/id/6664273/print?exp=a

### 10. Google rolls Gemini 4 Hydrogen out to free and paid users and into Search globally (Google)
CNET's explainer, published in the window, describes Gemini 4 Hydrogen as released Nov. 12 and now rolling out to free and paid users in the Gemini app, with access in Google Sheets for AI Pro and Ultra subscribers, and rolling out in Search globally for all users. It also details the current lineup including Gemini 4 Argon for complex reasoning, Gemini 4 Carbon for Ultra subscribers, and Gemini 3.8 Flash Cyber restricted to approved defenders through the Fairwind program, plus the note that Skills will replace Gems for personal accounts on Nov. 17.
Why it matters: A broad consumer distribution push that puts the newest Gemini model in front of free users and default Search traffic, the widest-reach release in the window.
Refs: https://www.cnet.com/tech/services-and-software/what-is-gemini-everything-you-should-know-google-ai-tool/

### 11. Grok Bot reaches version 1.0 with proactive to-do detection and team bots (xAI)
Grok Bot shipped its 1.0 release on Nov. 12, adding the ability to proactively identify to-do items, join team meetings, record colleagues' working habits and call other bots to collaborate. Team interviews describe a roughly seven-week path from internal prototype to public release, design principles of organizing work around named bots, giving each bot its own computer and keeping bots always-on, and adoption patterns where users escalate from single tasks to handing over an entire role; team bots were added about two weeks before the interviews.
Why it matters: A concrete agent-product milestone in which the unit of design is a persistent, credentialed bot rather than a chat session, with adoption described as trust escalating from tasks to job functions.
Refs: https://eu.36kr.com/en/p/4071829512935301, https://www.zhiding.cn/ai-applications/2026/1116/3205935.shtml

## Cross-Org Themes

- Cost per completed task, not raw benchmark score, is the headline metric vendors chose this window
- Model vendors are absorbing the surrounding toolchain — search, files, meetings, storefronts — into their own surfaces
- Agent products are being designed around persistent, credentialed identities rather than single chat sessions

## Rumors and Unverified Claims

Reported but not confirmed as events: Moonshot AI's roughly $50 billion valuation, possible Q1 2027 Hong Kong listing and up-to-$5 billion fundraising ceiling are press-reported figures, not final IPO pricing. Audn.AI's claim that an unrestricted derivative of Kimi K3.1 Pro solved eight of ten CyberGym tasks, and nine after further training on 382 GB of offensive-security data, has not been independently checked. Tencent's Hy4 was promised with weights and safety documentation within days of its Nov. 4 launch, but a final weight release could not be confirmed by mid-November.

## Takeaway

The competitive question has shifted from which model scores highest to who controls the toolchain, the identity and the billing around each completed task. Watch for independent replication of vendor cost-per-task claims and for the EuroHPC bid outcomes that will determine whether Europe's federated compute plans become contracts.

## Sources and Method

Web signal gathered via a bounded DeepSeek Search and Fetch query set (not the paid X API); DeepSeek was used only to synthesize the supplied search results and page content, not to recall live events from memory.
