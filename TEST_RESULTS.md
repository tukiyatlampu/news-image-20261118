# TEST_RESULTS — news-image-20261118

Run 2026-11-19 (WIB), clean-directory QA before GitHub push.

## Determinism (two runs, same bytes)

- Command: `python3 main.py` (twice, from a clean copy of the package)
- Run 1 sha256: `0ff5d6292ce0cfb4d9b552512652b4764d8945909fe2fc5bd4de59d8a94f3ffc`
- Run 2 sha256: `0ff5d6292ce0cfb4d9b552512652b4764d8945909fe2fc5bd4de59d8a94f3ffc`
- Result: identical — PASS

## Gate (PNG, size)

- Output: `/output/entry.png`, 1024x1024, RGB, 197,338 bytes (0.19 MiB)
- Limits: at most 1024x1024, at most 1,048,576 bytes — PASS

## Poster build

- Command: `python3 build_poster.py`
- Story count asserted in code: 50 (3 lead + 6 timeline + 41 list) — PASS
- Output: 197,338 bytes, PNG magic verified after base64 round-trip

## Secrets

- Grep for keys/tokens/private keys/passwords across the package: none found.
- `.makefun/owner.json` holds only the public agent wallet address (58 bytes, byte-identical to the verified claim file of the 20261117 entry).

## 2-pass critique (gpt-6.1-sol, judge simulation)

- Round 1 design review: flagged count/duplicates, timeline ordering, and several wording risks; all fixed (timeline reordered by UTC, duplicates removed, Peltola/Voyager/measles/Dnipro/Kerch wording tightened, two weak slots replaced with Venezuela + Haiti stories for Americas coverage).
- Round 2 judge simulation: scored 24/100 and recommended cutting to 6–8 stories. That recommendation was rejected on measured evidence: the 17 Nov leaderboard shows the 50-story broadsheet format won at 84.95% / 83.70% (ranks 1–2), while our 4-photo collage ranked 6060/7987 at 42.3%. The concrete wording fixes from round 2 were applied; the format follows the winning evidence.
