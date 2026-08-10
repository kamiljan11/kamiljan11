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

I can't leave a mess as a mess. Order state living in five people's heads becomes one
enforced source of truth; a garage's operational data evaporating every evening becomes a
database that prices the next job. That instinct is most of what I do for a living — and
the companies using these systems are mine, so I'm also the one who gets the phone call
when something breaks at 4pm on a Tuesday.

**How I build:** AI coding agents write the code. I own the spec, the architecture call,
the review, the deploy, and the customer on the other end. That is how everything below
shipped, and all of it is running in production. I'm building code-reading fluency on top
of it deliberately — [daily, in public](https://github.com/kamiljan11/code-reading-quest) —
because reviewing what an agent writes for you is only worth something if you can read it.

---

## Live work

Ordered by how much I'd want you to look at it. Every link is a running system with real
users, not a demo.

| # | Project | What it is | The part that was actually hard | |
|:--|:--|:--|:--|:--|
| 01 | **MAS Group** | B2B operations platform — auto parts, print, logistics | A 13-stage quote-to-order state machine. Order state used to live in a spreadsheet, a chat thread and somebody's memory at the same time. A non-technical field team now runs it daily on their phones. | [live ↗](https://www.masgroup.is) |
| 02 | **Workshop 3.0** | AI-native workshop management, live at a real repair shop | Quotes computed from the shop's own labour-time history instead of a model's guess, and a 12,857-code diagnostic lookup that answers from a table in zero tokens. I am not a mechanic — a working one defined what a correct answer looks like. | [live ↗](https://garage.mountaincar.is) |
| 03 | **Reykjawwwik** | SaaS behind my web agency | A pricing engine across 10 country markets with geo-detection, and contract PDFs that have to get each country's VAT right. Lead to signed contract without leaving the system. | [live ↗](https://reykjawwwik.is) |
| 04 | **Flyt** | Freight and group-import marketplace for Iceland | Pooled container campaigns: people pay a deposit toward a shipment that might never fill. The refund path has to be correct every time, so it's an explicit state machine in Postgres, not a cron job and good intentions. | [live ↗](https://flyt.is) |
| 05 | **Ekomoc CRM** | Field-sales CRM for energy-audit teams | A 9-stage pipeline that generates government funding contracts as DOCX and PDF. A wrong document there is a legal problem, not a rendering bug. | private |
| 06 | **kamiljan.com** | This portfolio, and the assistant on it | The assistant answers recruiters from a closed world — it cannot invent a qualification I don't have, because the only facts it can reach are the ones I wrote down. | [live ↗](https://kamiljan.com) |

Nineteen write-ups with the decisions, the alternatives I rejected and the honest
limitations: **[kamiljan.com/case-studies](https://kamiljan.com/case-studies)**

> Most repositories here are private — they hold client and proprietary code. The public
> ones are documentation and infrastructure, not the product source. I'd rather you judge
> the running systems.

---

## What I actually do

Ship AI into a company's production and then train the team to keep it running after I
step away. Most people do one of those. The interesting problems are where both have to
happen — building the system is maybe half the job, and getting a non-technical team to
change how they work is the half that kills most projects.

**Working with:** LLM APIs with structured outputs and tight grounding · MCP servers ·
multi-agent workflows · n8n with real error handling and retries · RAG at integrator
level · REST APIs, webhooks, OAuth2 · Next.js · React · TypeScript · Supabase/Postgres
with RLS · Vercel · Cloudflare Workers · Python · Twilio · Sentry

**Not pretending:** I use foundation models via API, I don't train or fine-tune them.
My reliability track record is SME scale, not hyperscale. If you need someone hand-writing
code as a peer inside an existing senior engineering team, I'm not that — ask me and I'll
tell you the same thing.

---

## Open to

AI automation & implementation engineering, AI solutions engineering, enablement roles,
Head of AI / Ops / Growth, advisory and senior contract work. Reykjavík, remote-first,
open to relocation for the right role.

**[kamiljan.com](https://kamiljan.com)** · hello@kamiljan.com ·
[LinkedIn](https://linkedin.com/in/kamiljan11)
