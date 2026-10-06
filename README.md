# MHR-Test — Hero Rush Live v1.3.1 Card Library Alpha

Unofficial, text-only Marvel Hero Rush digital TCG prototype for Android. No copyrighted card artwork is bundled.

## v1.3.1 — BP01 Card Library update

Before starting v1.4, the Collection has been upgraded around the BP01 card catalog:

- All **120 BP01 Character cards** are indexed.
- Every BP01 Character now has card code, title/hero, color, Level, Range, Power, rarity and traits.
- Yellow, Blue and Green reference cards include paraphrased effect summaries where verified.
- BP01-049, BP01-091 and BP01-092 intentionally use conservative reference notes until their complete wording is reverified.
- Collection cards now use a text-only TCG card frame rather than a plain list row.
- Added Collection filtering for Level, Range, rarity and trait on top of the existing search/color/status filters.
- Search now covers name, hero, code, trait and effect.
- **BP01-001 through BP01-030 Red remain the current executable gameplay pool.**
- BP01-031 through BP01-120 are detailed reference cards and are not falsely marked playable before their engine handlers are implemented.

## Existing v1.0–v1.3 features

- Live-style home/client shell
- Offline VS AI
- Three locally saved deck slots
- 50-card legality validation and 9-card Rush deck
- Mulligan and draw-2 turn flow
- Manual Lv4–6 exact-Level payment
- Front / Wing L / Wing R / Back battle board
- Repositioning and Wing attack order
- Range/Power combat and Rush Point victory
- Text card inspection and match result screen
- Local win/loss statistics
- BP01 Red effect-engine Alpha

## Build the APK from Android

Android Studio is not required.

1. Open this repository in GitHub.
2. Go to **Actions**.
3. Open **Build Android APK**.
4. Tap **Run workflow**.
5. Open the successful run.
6. Download **HeroRushLive-v1.3.1-card-library-debug**.
7. Extract the artifact ZIP.
8. Install `HeroRushLive-v1.3.1-card-library-debug.apk`.

## Repository packaging

The stable v1.3 Android base remains stored under `source-parts/`. The v1.3.1 catalog delta is stored under `patches/`; GitHub Actions reconstructs the base, applies the card-data/UI patch, validates JavaScript, and builds the Android APK.

This fan-made testing project is not affiliated with Marvel or the game publisher. Card effect descriptions are paraphrased.
