# Wealth Project — Start Here (Handoff / README)

> **Purpose of this file:** orient anyone (a person or a new model/session) taking over this project, without needing to read the original chat. Last updated 2026-06-10.

## What this project is

A personal, US-focused, living **playbook for building wealth through real estate and strategic leverage**, written for an investor (Aaron) with some experience who wants to scale. It is educational, not financial/legal/tax advice; every dated figure is flagged ⏱️ and risk caveats ⚠️. Current as of mid-2026 and reflects the One Big Beautiful Bill Act (OBBBA, 2025).

## File map

| File | What it is |
|---|---|
| `Wealth-Through-Real-Estate-and-Leverage.md` | **The master guide.** 7 parts / 30 sections + Sources + Changelog. This is the canonical source of truth — edit this, then re-embed it into the app (see below). |
| `How-To-Use-This-Guide.md` | The "operating system": evidence-based study cadence, triggers, decision journal, and a minimal tooling stack (Obsidian + NotebookLM). |
| `Panel-Review-Recommended-Additions.md` | Record of a 4-expert review (CPA, operator, attorney, CFP) that drove the v3 expansion. Its §-numbers refer to the pre-v3 layout. |
| `Guide-Companion.html` | A standalone single-file interactive companion (cheat sheet, quiz, checklists, calculator, journal). Superseded by `app/` but kept. |
| `app/` | **The installable app (PWA).** See below. |

### `app/` contents
- `index.html` — the whole app in one file: **Today** daily dashboard (streak, due counts, daily challenge, pipeline summary; default tab), **Study** hub (SM-2 spaced-repetition flashcards with Again/Good/Easy grading; Quizlet-style "Learn terms" over the 775-term glossary with MCQ→typed-recall leveling to mastered; timed Match game; 10-question mixed Test), **Deal Simulator** game (random realistic listings, ~30% true buys — decide Buy/Pass against your red-lines, scored with streaks), **Deal Pipeline** (save deals from the calculator with statuses watching/offered/under contract/owned/passed, compare side by side, reload into calc), plus the embedded full guide (searchable, hover-glossary), cheat sheet, checklists, deal calculator, decision journal, My Numbers, Backup & Sync, Glossary tab. **Versus** tab (pass-and-play, 2 players w/ editable names, win records): ⚡ Quiz Duel (10 alternating timed MCQs, speed scoring), 🏠 Deal-Off (both judge the same 5 listings), 🧩 Match Race (same 6 pairs, fastest board), 🏁 Wealth Race (turn-based 15-year sim: $50k start, $25k/yr savings, one listing/year, market events incl. 10% crash chance, forced discount sale if cash goes negative; first to $1M net worth or richest at year 15 — balance-simulated: smart buyer median ≈ $800k vs $425k passive). **Course tab (Duolingo-style path):** 7 units = the guide's Parts, 29 lessons = its §-sections, derived at runtime from the embedded guide (`courseUnits()` parses `guideSections`; editing the guide auto-updates the course). Each lesson = up to 8 exercises auto-built from that section: terms found in the section text via the glossary regexes (term→def MCQ, def→term MCQ, typed recall) + 2 concept questions from the unit-mapped flashcard categories (`UNIT_CATS`). 60% passes and unlocks the next lesson; stars 1–3 (3 = perfect, +20 XP bonus); progress is per player profile in `DB.vs.course`. **XP system (Duolingo-style):** two player profiles, header chip shows active player; every activity pays XP (flashcards 5, learn 10–15, match 25, test 10/correct, deal game 15, duel wins 60–150); levels need 100+50(n−1) XP; 50 XP daily goal; leaderboard with switcher on Today. All new data (`srs`, `learn`, `games`, `pipeline`, `streak`, `vs`) lives in the same `DB` localStorage object, so backup/sync cover it automatically. Streak = any study activity that day; counted via `DB.streak.history`. Future idea: move Versus online via a small server (game logic is already isolated in pure functions).
- `manifest.webmanifest`, `sw.js`, `icon-*.png` — PWA scaffolding (installable + offline).
- `INSTALL-AND-SYNC.md` — how to use locally, host free (Netlify Drop) to install on phone/desktop, and turn on optional cloud sync. Privacy notes included.

## Current state (done)

- Guide researched, written, expanded after panel review, and **verified by a two-agent pass** (independent fact-check + consistency re-grade). One real error was found and fixed (2025 fair-housing change); umbrella-cost and a cross-ref were corrected. See the guide's Changelog.
- App built and verified: JS syntax-checked, manifest valid, service worker working, guide embedded.
- **Glossary: 775 terms**, all hover-enabled in the guide and listed in the Glossary tab. All 775 match-patterns compile cleanly. Acronyms match case-sensitively; each term underlines once per section.

## How things are built (so you can change them safely)

**The app embeds the guide as text.** If you edit `Wealth-Through-Real-Estate-and-Leverage.md`, re-embed it into the app by replacing the contents of the `<script id="guideMd" type="text/markdown">…</script>` block in `app/index.html` with the new markdown. (Originally done with a small Python splice on a `%%GUIDE_MARKDOWN%%` placeholder.) Always re-run a JS syntax check after edits to `index.html`.

**The glossary** lives in `app/index.html` as a JS object `const GLOSSARY={ "term":"definition", … };`. Hover works via `decorateGlossary()`, which wraps the first occurrence per section of each term; `makeTermRe()` makes all-caps acronym keys case-sensitive to avoid false hits. To add terms, insert `"term":"def"` pairs before the object's closing `};` (use proper escaping; building entries with JSON-encoded strings is safest).

**Verifying changes to the app:** extract the last `<script>…</script>` block and run `node --check` on it; parse the `GLOSSARY` object as JSON to confirm it's well-formed.

## Conventions

- ⏱️ = a figure that drifts (rates, tax thresholds) — re-verify before relying on it.
- ⚠️ = a risk caveat.
- Everything is "not advice" — the guide repeatedly says to confirm with a CPA / real estate attorney / fee-only planner / insurance broker.
- Tone: prose-first, minimal bullets, plain English for a beginner.

## Possible next steps (open ideas, not committed)

- Re-embed the guide into the app whenever the master `.md` changes (no automation yet — manual splice).
- Optional: thin the hover underlines to first-occurrence-in-whole-guide instead of per-section, if reading feels too dense.
- Optional: an Anki-importable flashcard export for long-term spaced repetition.
- Optional: a portfolio-tracking spreadsheet alongside the calculator.
- Keep dated figures current at each quarterly/tax-season refresh; bump the guide Changelog.

## Quick re-orientation prompt for a new model/session

"Read `README.md` and `Wealth-Through-Real-Estate-and-Leverage.md` in the wealth folder. This is a living US real-estate wealth guide plus an installable app (`app/index.html`) with an embedded copy of the guide and a 775-term hover glossary. Continue maintaining it: keep figures current (⏱️ items), re-embed the guide into the app after edits, and verify `index.html` JS with `node --check`."
