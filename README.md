# MHR-Test — Hero Rush Live v1.5 Blue + Green Alpha

Unofficial, text-only Marvel Hero Rush digital TCG prototype for Android. No copyrighted card artwork is bundled.

## v1.5 — Blue + Green gameplay

v1.5 brings both remaining BP01 colors into the playable Alpha pool while preserving the card-color border system introduced in v1.4.

### BP01 gameplay status

- **Red:** BP01-001 through BP01-030 — 30 playable Alpha cards
- **Yellow:** BP01-031 through BP01-060 — 29 playable Alpha cards
- **Blue:** BP01-061 through BP01-090 — 30 playable Alpha cards
- **Green:** BP01-093 through BP01-120 — 28 playable Alpha cards
- **Reference-only:** BP01-049, BP01-091 and BP01-092
- **Total BP01 database:** 120 Character cards
- **Current playable pool:** 117 cards

The three reference-only cards remain disabled rather than receiving invented behavior where their complete effect wording is not sufficiently verified.

### v1.5 engine coverage

Blue and Green now use the same executable effect engine as Red and Yellow. Alpha coverage includes:

- call triggers and enter-field reactions
- automatic Power, Range and Level modifications
- Counter-style hand defenses
- Battle ↔ Base movement and movement triggers
- Retreat, Void, Base and deck recursion
- attachments and attachment restrictions
- opening-defense reactions
- attack triggers and target restrictions
- end-turn effects
- hand activations and field activations
- deck/hand/Base manipulation

Some complex timing windows, optional choices, and multi-target effects currently auto-select the first legal resolution. These will be hardened in a dedicated rules-fidelity pass.

### Card-color borders

Cards remain visually keyed by color everywhere in the client:

- Red — red border
- Yellow — gold/yellow border
- Blue — blue border
- Green — green border

The treatment is used in Collection, deck builder, mulligan, hand, Battle field, Base and compact gameplay cards.

## Existing client features

- mobile Live-style lobby and navigation
- offline VS AI
- three locally saved deck slots
- 50-card legality validation plus 9-card Rush deck
- mulligan and draw-2 turn flow
- manual Lv4–6 exact-Level payment
- Front / Wing L / Wing R / Back battle board
- repositioning and Wing attack order
- Range/Power combat and Rush Point victory
- Collection filters and text card inspector
- local win/loss statistics

## Build the APK from Android

Android Studio is not required.

1. Open this repository in GitHub.
2. Go to **Actions**.
3. Open **Build Android APK**.
4. Tap **Run workflow**.
5. Open the successful run.
6. Download **HeroRushLive-v1.5-blue-green-alpha-debug**.
7. Extract the artifact ZIP.
8. Install `HeroRushLive-v1.5-blue-green-alpha-debug.apk`.

## Build validation

The workflow reconstructs the source from `source-parts/`, verifies the v1.5 source SHA-256, validates all JavaScript assets, checks the complete BP01 card pool and per-color playable counts, verifies that only BP01-049/BP01-091/BP01-092 remain reference-only, then builds with Android SDK 36, JDK 17 and Gradle 9.4.1.

This fan-made testing project is not affiliated with Marvel or the game publisher. Card effect descriptions are paraphrased.
