# MHR-Test — Hero Rush Live v1.7 Arena Alpha

Unofficial, text-first Marvel Hero Rush digital TCG prototype for Android.

## v1.7 — Arena presentation upgrade

v1.7 keeps the v1.5 BP01 gameplay engine and focuses on making the Android client feel like an actual tabletop/digital TCG.

### New arena

- Battle screen rebuilt around the supplied Hero Rush physical playmat reference.
- FRONT, WING L, WING R and BACK now use a compact arena geometry instead of four equal columns.
- Opponent field faces the player field across a central BATTLE line.
- Base zones are integrated into each side of the arena.
- Side rails expose Deck, Rush Deck, Retreat, Void and Timeline/Rush progress.
- The Android match screen runs in immersive landscape mode.

### Compact cards + hold preview

- Cards are smaller while placed on the arena so all zones remain visible.
- Card borders still follow card color: Red, Yellow, Blue and Green.
- Press and hold a field, Base or hand card for about 0.32 seconds to open the large card preview.
- Normal tap behavior remains available for selecting cards, choosing actions and attacking.

### Icon and branding

The user-supplied Avengers emblem is now used as:

- Android launcher icon
- in-game v1.7 battle logo
- deck/card-back motif
- subtle card preview artwork motif

The embedded asset is optimized for APK size while retaining the supplied image.

### BP01 gameplay status

- Red: 30 playable
- Yellow: 29 playable
- Blue: 30 playable
- Green: 28 playable
- Total playable: **117 / 120 BP01 Character cards**
- Reference-only: BP01-049, BP01-091, BP01-092

No gameplay-card implementation was removed for the v1.7 UI overhaul.

## Build on Android without Android Studio

1. Open this repository in GitHub.
2. Go to **Actions**.
3. Open **Build Android APK**.
4. Tap **Run workflow**.
5. Open the successful run.
6. Download **HeroRushLive-v1.7-arena-alpha-debug**.
7. Extract the artifact ZIP.
8. Install `HeroRushLive-v1.7-arena-alpha-debug.apk`.

The downloadable Android source ZIP also includes its own direct Gradle/GitHub Actions build workflow.

This is an unofficial fan-made testing project and is not affiliated with Marvel or the game publisher. Card effect descriptions are paraphrased.
