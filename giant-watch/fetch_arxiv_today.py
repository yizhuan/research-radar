import sys,json,urllib.request
sys.path.insert(0,"/home/yizhuan/.hermes/skills/research-radar/giant-watch-summary/scripts")
import fetch_arxiv_signals as f

def opener(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 research-summary/1.0 mailto:research@example.com","Accept":"application/atom+xml"})
    with urllib.request.urlopen(req,timeout=120) as r:
        return r.read()
s=f.fetch_signals("daily",opener=opener,max_results=300)
open("/home/yizhuan/.research/giant-watch/arxiv-signals-2026-09-23.json","w").write(json.dumps(s,indent=2,ensure_ascii=False)+"\n")
print("matched",len(s))
