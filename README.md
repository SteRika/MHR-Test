# MHR-Test — Hero Rush Live v1.7.1 Arena Layout Fix

Unofficial, text-first Marvel Hero Rush digital TCG prototype for Android.

## v1.7.1 fixes

This release fixes the two Android landscape issues found in v1.7:

- **END TURN is permanently visible** in the top-right battle controls.
- SET BASE / BATTLE / END TURN no longer depend on the height of the right-side arena rail.
- The battle shell now uses the Android WebView's actual visible viewport height.
- The CALL position selector floats above the hand instead of changing the battlefield height.
- Short landscape screens can shrink FRONT / WING / BACK rows instead of forcing oversized minimum heights.
- Base zones, side rails and compact field cards scale down for phone-height landscape viewports.
- The bottom hand HUD keeps a stable height so selecting a card no longer shifts the arena.

## Preserved v1.7 features

- supplied Avengers launcher/game icon
- Hero Rush playmat-inspired arena
- compact field cards
- press-and-hold card preview
- Red / Yellow / Blue / Green card borders
- immersive landscape Android battle mode
- 117 / 120 BP01 Character cards playable

Reference-only cards remain BP01-049, BP01-091 and BP01-092.

## Build from Android

Open **Actions → Build Android APK → Run workflow**. Download the **HeroRushLive-v1.7.1-layout-fix-debug** artifact after the run succeeds.

This fan-made testing project is not affiliated with Marvel or the game publisher. Card effect descriptions are paraphrased.
