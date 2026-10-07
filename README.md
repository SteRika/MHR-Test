# MHR-Test — Hero Rush Live v1.8 Rules Fidelity Alpha

Unofficial, text-first Marvel Hero Rush digital TCG prototype for Android.

## v1.8

This version focuses on rules correctness and battle interaction rather than adding more cards.

### Rules fidelity

- Positional Range uses the attacker-row distance matrix:
  - FRONT → enemy FRONT R-1, WING R-2, BACK R-3
  - WING → enemy FRONT R-2, WING R-3, BACK R-4
  - BACK → enemy FRONT R-3, WING R-4, BACK R-5
- Illegal attack zones remain visible as **LOCKED** and show the minimum required Range.
- Tapping an illegal target explains why the attack is not legal.
- Battle/Base movement now gives an explicit reason when movement is blocked.
- SET 1 / DRAW 1 remains limited to once per turn.
- Call limits remain enforced, including the opening-turn restriction.
- Lv4–6 call payment remains manual and exact; payment choices that would exceed the required Level are disabled.

### Effect / response interaction

- Existing Trigger/Counter windows now show a small effect stack with **PASS** and **USE EFFECT**.
- Sequential player choices are queued rather than overwriting each other.
- Player-controlled manual targeting is expanded for several effects that previously auto-selected targets, including Hit & Run, Hearing Disarm, and God Of Story.
- Existing manual effect selections and call-payment selection remain available.

### Regression validation

The source includes a reusable rules core and automated regression tests covering Range, movement, Base deployment, and call limits. GitHub Actions runs these checks before compiling the APK.

### Card pool

- Red: 30 playable
- Yellow: 29 playable
- Blue: 30 playable
- Green: 28 playable
- Total: **117 / 120 BP01 Character cards playable**
- Reference-only: BP01-049, BP01-091, BP01-092

Portrait-only arena, hold-to-preview, color borders, deck builder, mulligan, and offline AI are preserved.

This fan-made testing project is not affiliated with Marvel or the game publisher. Card effect descriptions are paraphrased.
