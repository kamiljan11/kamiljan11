# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), wersjonowanie: [SemVer](https://semver.org/).
Kazdy PR dopisuje zmiany do [Unreleased].

## [Unreleased]
### Added
- Pipeline jakosci: CI (build/lint/typecheck/test/semgrep/audit/licencje), Claude review na PR, szablony dokumentacji

### Changed
- README profilu przepisany po angielsku pod czytelnika technicznego: publiczne repo + zweryfikowany link live dla kazdego,
  stack, sekcja "How I work" opisujaca realne bramki (lint / `tsc -b` / testy / gitleaks / sql-lint w pre-commit i CI),
  recenzje wg tieru ryzyka, golden suite bramek, ADR, Conventional Commits

### Removed
- `e2e/smoke.spec.ts` — test Playwright bez `playwright.config.ts` i bez `package.json`; job `e2e` w quality.yml pomijal go zawsze
- `.github/workflows/release.yml` — repo profilowe nie ma artefaktu wersjonowanego SemVer
- `docs/RUNBOOK.md`, `docs/adr/0000-template.md` — nieuzupelnione szablony (placeholdery `[URL]`, zly owner repo) w repo publicznym
