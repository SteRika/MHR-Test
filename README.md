# MHR-Test — Hero Rush Live v1.7.4 Positional Range Fix

Unofficial, text-first Marvel Hero Rush digital TCG prototype for Android.

## v1.7.4 — Range now counts from the attacker's current row

The previous v1.7.3 implementation only checked how deep the target was in the opponent's formation. v1.7.4 corrects this by also including the attacker's starting position.

### Required Range matrix

- FRONT attacker → enemy FRONT requires R-1, enemy WINGS R-2, enemy BACK R-3
- WING attacker → enemy FRONT requires R-2, enemy WINGS R-3, enemy BACK R-4
- BACK attacker → enemy FRONT requires R-3, enemy WINGS R-4, enemy BACK R-5

Example: a BACK character with R-3 can attack only the opponent FRONT. It cannot attack either Wing or Back.

This same matrix is used for normal attacks, AI targeting, attack revalidation after Counter/Response effects, and Range-changing effects.

## Preserved features

- portrait-only Android battle layout
- SET 1 / DRAW 1 Base Deployment
- permanent BATTLE / END TURN controls
- press-and-hold card preview
- Red / Yellow / Blue / Green borders
- 117 / 120 BP01 Character cards playable

Reference-only cards remain BP01-049, BP01-091 and BP01-092.

This fan-made testing project is not affiliated with Marvel or the game publisher. Card effect descriptions are paraphrased.
