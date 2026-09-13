# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), wersjonowanie: [SemVer](https://semver.org/).
Kazdy PR dopisuje zmiany do [Unreleased].

## [Unreleased]
### Added
- `assets/banner.svg` — naglowek profilu: ASCII-art ze znaku `@` w palecie kamiljan.com
  (teal #0891b2 -> #22d3ee), uklad dwuwierszowy KAMIL / JAN, animowany gradient SMIL,
  3.3 kB, skaluje sie do szerokosci mobilnej
- Pipeline jakosci: CI (build/lint/typecheck/test/semgrep/audit/licencje), Claude review na PR, szablony dokumentacji

### Changed
- README profilu przepisany po angielsku pod czytelnika technicznego: publiczne repo + zweryfikowany link live dla kazdego,
  stack, sekcja "How I work" opisujaca realne bramki (lint / `tsc -b` / testy / gitleaks / sql-lint w pre-commit i CI),
  recenzje wg tieru ryzyka, golden suite bramek, ADR, Conventional Commits
- README: naglowek H1 zastapiony bannerem (nazwa i tagline sa w grafice, pelny tekst w `alt`)

### Removed
- `e2e/smoke.spec.ts` — test Playwright bez `playwright.config.ts` i bez `package.json`; job `e2e` w quality.yml pomijal go zawsze
- `.github/workflows/release.yml` — repo profilowe nie ma artefaktu wersjonowanego SemVer
- `docs/RUNBOOK.md`, `docs/adr/0000-template.md` — nieuzupelnione szablony (placeholdery `[URL]`, zly owner repo) w repo publicznym
