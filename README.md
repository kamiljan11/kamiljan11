```
██╗  ██╗ █████╗ ███╗   ███╗██╗██╗              ██╗ █████╗ ███╗   ██╗
██║ ██╔╝██╔══██╗████╗ ████║██║██║              ██║██╔══██╗████╗  ██║
█████╔╝ ███████║██╔████╔██║██║██║              ██║███████║██╔██╗ ██║
██╔═██╗ ██╔══██║██║╚██╔╝██║██║██║         ██   ██║██╔══██║██║╚██╗██║
██║  ██╗██║  ██║██║ ╚═╝ ██║██║███████╗    ╚█████╔╝██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚══════╝     ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝

   ·   ✦      .        ·          ✦     ·        .       ✦    ·
  ~~~≈≈≈≈~~~~~~~≈≈≈≈≈≈~~~~~~~≈≈≈≈~~~~~~~≈≈≈≈≈~~~~~~≈≈≈~~~~~~~~~~~~~
         /\                      /\
        /  \       /\           /  \      /\
       /    \     /  \    /\   /    \    /  \      /\
   ___/      \___/    \__/  \_/      \__/    \____/  \___

   builder & operator · reykjavík · ai in production for smes
```

I build software, automation and AI systems **in production** — and run the companies that use them every day.

🌐 **[kamiljan.com](https://kamiljan.com)** &nbsp;·&nbsp; ✉️ hello@kamiljan.com &nbsp;·&nbsp; 📖 daily code-reading log: [code-reading-quest](https://github.com/kamiljan11/code-reading-quest)

> ℹ️ Most repositories here are **private** — they hold client and proprietary code (ERPs, CRMs, pricing engines, automations).
> Everything below is real, **live** work. Green nodes are live sites — click them.

---

## 🚀 Live projects

```mermaid
flowchart LR
    K(("Kamil Jan · Reykjavík"))

    K --- OPS(["operations platforms"])
    K --- MKT(["marketplaces & logistics"])
    K --- MOB(["travel & mobility"])
    K --- SVC(["service brands"])
    K --- INF(["own systems"])

    OPS --- MAS["MAS Group · masgroup.is"]
    OPS --- EKO["Ekomoc CRM · field-sales, energy audits"]
    OPS --- WAR["MAS Warsztat · garage management"]
    OPS --- KAL["Maskalkulator · print pricing engine"]

    MKT --- FLY["Flyt · flyt.is"]
    MKT --- ISL["Island Collective · group shipments"]

    MOB --- MC["Mountain Car · mountaincar.is"]
    MOB --- REN["Rental Manager · internal fleet ops"]
    MOB --- JI["Journey Iceland · tours"]

    SVC --- QF["QuickFix · quickfix.is"]
    SVC --- RKW["Reykjawwwik · reykjawwwik.is"]
    SVC --- HH["HomeHug · home services"]
    SVC --- MOV["Is Move Magic · moving services"]
    SVC --- SPA["Spirit Way Bloom · wellness platform"]

    INF --- SITE["kamiljan.com · portfolio"]
    INF --- CRQ["code-reading-quest · daily practice log"]
    INF --- HER["Hermes · agent runtime"]
    INF --- UP["Uptime monitor · GitHub Actions"]

    click MAS "https://masgroup.is" _blank
    click FLY "https://flyt.is" _blank
    click MC "https://mountaincar.is" _blank
    click QF "https://quickfix.is" _blank
    click RKW "https://reykjawwwik.is" _blank
    click SITE "https://kamiljan.com" _blank
    click CRQ "https://github.com/kamiljan11/code-reading-quest" _blank

    classDef hub fill:#161b22,stroke:#6e7681,stroke-width:1px,color:#e6edf3
    classDef live fill:#0d2b1f,stroke:#3fb950,stroke-width:1.5px,color:#e6edf3
    classDef work fill:#12203a,stroke:#58a6ff,stroke-width:1px,color:#e6edf3
    classDef own fill:#241a33,stroke:#a78bfa,stroke-width:1px,color:#e6edf3

    class OPS,MKT,MOB,SVC,INF hub
    class MAS,FLY,MC,QF,RKW,SITE live
    class EKO,WAR,KAL,ISL,REN,JI,HH,MOV,SPA work
    class CRQ,HER,UP own
```

**MAS Group** — B2B operations platform across auto parts, print and logistics. 13-stage quote-to-order pipeline, per-line pricing calculators, commission management, role-based access.

**Flyt** — group-order and import marketplace for Iceland. Pooled container campaigns with deposit/refund logic, on-demand import quotes, admin dashboard with live revenue metrics.

**Mountain Car** — car rental and garage near KEF airport. Fleet, booking and quote flow on Next.js + Supabase.

**QuickFix** — handyman brand in Reykjavík. Multilingual site (EN/PL/IS) plus lead funnel, shipped in 72 hours.

**Reykjawwwik** — web-agency SaaS. Multi-market pricing engine across 10 countries with geo-detection, lead-to-contract CRM, PDF contracts with per-country VAT.

**Ekomoc CRM** — field-sales CRM for energy-audit teams. 9-stage pipeline, role-based access, automated DOCX/PDF contract generation, leaderboard. _(private)_

---

## 🛠️ What I build with

**Product:** Next.js · React · TypeScript · Supabase · Vercel · Cloudflare Workers
**AI & automation:** n8n · RetellAI (voice agents) · WhatsApp bots · OpenAI / LLM + MCP integrations · fal.ai
**Plumbing:** Twilio · Google Apps Script · Playwright
**Growth:** Meta Ads · Google Ads · funnel & email systems

---

## 🤝 Work with me

I ship AI into production for SMEs — and train the teams that keep it running after I step away.

→ **[kamiljan.com](https://kamiljan.com)**
