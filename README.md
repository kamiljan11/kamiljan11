# Kamil Jan

Builder and operator in Reykjavík. I run two small Icelandic companies, MAS Group (auto parts,
print, logistics) and Reykjawwwik (a web agency), and I write the software both of them run on.

Which also makes me the person who gets the phone call when something breaks at 4pm on a
Tuesday. That is most of why the rest of this page is about gates and review rather than
frameworks.

AI coding agents write most of the code. I own the spec, the architecture call, the review, the
deploy, and the customer on the other end. Everything listed below is in daily commercial use.

## Public work

Five repositories you can read. Each has its own README with the detail.

| Repo | Live | What it is |
|:--|:--|:--|
| [maskalkulator](https://github.com/kamiljan11/maskalkulator) | [masgroup.is](https://www.masgroup.is) | MAS Group's B2B operations platform: pricing calculators driven by supplier price lists, a quote-to-order pipeline, partner CRM, generated contracts, commission tracking, and a client portal with scoped modules. |
| [spirit-way-bloom](https://github.com/kamiljan11/spirit-way-bloom) | [reykjawwwik.is](https://reykjawwwik.is) | The platform that runs the agency end to end. A visitor is priced for their own market across ten countries, answers a questionnaire, books a call, signs a contract with per-country VAT, and becomes a billed client, without anyone re-typing their details into a second system. |
| [mountain-car-rental](https://github.com/kamiljan11/mountain-car-rental) | internal | Fleet and booking manager for a car rental near Keflavík, replacing a rented SaaS that charged per booking. Vehicles by days on one resource calendar, so a car in the workshop cannot be double-booked from another tab. Contracts are generated from templates and signed by link. |
| [mountaincar-is](https://github.com/kamiljan11/mountaincar-is) | [mountaincar.is](https://mountaincar.is) | Public site for that rental. Narrow on purpose: show the fleet, answer the questions that stop a booking, and deliver a server-validated enquiry by e-mail. Five runtime dependencies. |
| [mas-garage](https://github.com/kamiljan11/mas-garage) | [garage.mountaincar.is](https://garage.mountaincar.is) | Landing page and installable web app for a garage in Reykjanesbær. Trilingual (English, Polish, Icelandic), one hand-written `index.html`, a service worker, no build step. |

Most of my repositories are private, because they hold client and proprietary code. Longer
write-ups, including the alternatives I rejected and what each system still does not do, are at
[kamiljan.com/case-studies](https://kamiljan.com/case-studies).

## Stack

TypeScript throughout. React with Vite, or Next.js App Router where the page needs server
rendering. Postgres on Supabase, with Row Level Security as the authorisation boundary instead
of checks in the client, and Edge Functions for server logic. Hosted on Vercel and Lovable.
Vitest for unit tests, Playwright for end-to-end smoke. Python for the tooling around the
repos: CI checks, releases, secret injection, migration linting.

## How I work

**The gates are deterministic and run in two places.** Before a commit lands: ESLint or oxlint,
`tsc -b` (not `--noEmit`, which exits zero without checking anything under project
references), the unit tests, a gitleaks secret scan, and a SQL linter that fails a migration
adding a table without RLS or a `SECURITY DEFINER` function without a pinned `search_path`. The
same checks run again in GitHub Actions on every push and pull request, so a green local run
means the same thing as a green badge.

**Review is scored from the diff, not from how I feel about the change.** A docs edit and a
change to auth, RLS, payments or a migration are not the same risk, so the tier is computed from
the files touched. Above a threshold the diff goes to reviewer agents with fresh context and
read-only access, one per concern: correctness, security, data, operations, UX, product. Every
finding has to carry a command that reproduces it. A separate verifier re-runs that command and
drops the findings that do not reproduce. That step is most of the difference between a review
and a list of opinions.

**The gates have their own test suite.** A golden set of cases each gate must catch, plus cases
it must not trip on, run before I change anything about a gate. Otherwise there is no way to
tell that an edit made one of them blinder.

Conventional Commits, enforced by a commit-msg hook. Architecture decisions written down as ADRs
with the rejected alternative recorded. Secrets live in a self-hosted vault and are injected at
run time; none of them are pasted into a file, a config or a chat.

## What I am not

I use foundation models through their APIs. I do not train or fine-tune them. My reliability
record is SME scale, not hyperscale. If you need someone hand-writing production code as a peer
inside an existing senior engineering team, that is not the job I do well.

## Open to

AI implementation and solutions engineering, automation and enablement work, advisory and senior
contract roles. Reykjavík, remote-first, open to relocating for the right role.

[kamiljan.com](https://kamiljan.com) · hello@kamiljan.com · [LinkedIn](https://linkedin.com/in/kamiljan11)
