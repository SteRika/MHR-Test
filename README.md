# MHR-Test — Hero Rush Live v1.4 Yellow Alpha

Unofficial, text-only Marvel Hero Rush digital TCG prototype for Android. No copyrighted card artwork is bundled.

## v1.4 — Yellow gameplay + color-readable cards

This release moves the second BP01 color into active gameplay and makes card color visible immediately across the mobile client.

### Card-color borders

Cards now use a consistent border based on their card color:

- Red — red border
- Yellow — gold/yellow border
- Blue — blue border
- Green — green border

The color treatment is used in Collection, deck-builder rows, hand cards, mulligan cards, Battle cards, Base cards and compact gameplay cards.

### BP01 gameplay status

- **Red:** BP01-001 through BP01-030 — 30 playable Alpha cards
- **Yellow:** BP01-031 through BP01-060 — 29 playable Alpha cards
- **BP01-049:** remains reference-only until its effect wording is reverified
- **Blue:** detailed reference cards, not yet executable
- **Green:** detailed reference cards, not yet executable
- **Total BP01 database:** 120 Character cards
- **Current playable pool:** 59 cards

Yellow v1.4 covers Alpha implementations for Power/Range autos, call effects, hand actions, call-payment triggers, Battle/Base movement, attachments, attack triggers and other Yellow interactions. Some complicated timing/selection windows currently resolve automatically and will be hardened in later rules passes.

## Existing client features

- Live-style home/client shell
- Offline VS AI
- Three locally saved deck slots
- 50-card legality validation and 9-card Rush deck
- Mulligan and draw-2 turn flow
- Manual Lv4–6 exact-Level payment
- Front / Wing L / Wing R / Back battle board
- Repositioning and Wing attack order
- Range/Power combat and Rush Point victory
- Text card inspection
- Match result screen and local win/loss statistics
- BP01 card Collection with Level/Range/rarity/trait filters

## Build the APK from Android

Android Studio is not required.

1. Open this repository in GitHub.
2. Go to **Actions**.
3. Open **Build Android APK**.
4. Tap **Run workflow**.
5. Open the successful run.
6. Download **HeroRushLive-v1.4-yellow-alpha-debug**.
7. Extract the artifact ZIP.
8. Install `HeroRushLive-v1.4-yellow-alpha-debug.apk`.

## Build validation

The GitHub workflow reconstructs the source from `source-parts/`, verifies its SHA-256, validates the JavaScript/card pool, verifies the four border-color CSS rules, installs Android SDK 36 / Build Tools 36.0.0, and builds with JDK 17 and Gradle 9.4.1.

This fan-made testing project is not affiliated with Marvel or the game publisher. Card effect descriptions are paraphrased.
