# MHR-Test — Hero Rush Live v1.3 Alpha

Unofficial, text-only Marvel Hero Rush digital TCG prototype for Android. No card artwork is bundled.

The project is moving from a rules simulator toward a mobile TCG client inspired by the product structure of games such as Pokémon TCG Live: lobby, collection, deck management, polished battle presentation, local progression/statistics, and eventually online play.

## v1.0 — Live-style client shell

- Home lobby with Play, Decks, Collection, Training and Profile navigation
- Mobile-first full-screen battle presentation
- Compact Front / Wing L / Wing R / Back board
- Card inspector and match-result screen
- Offline VS AI flow

## v1.1 — Collection and Deck Manager

- Three locally saved deck slots
- Active deck selection
- Legal 50-card deck validation
- Maximum 3 copies per card name
- Maximum 2 colors
- Separate 9-card Rush deck
- Level and Range deck analytics
- Deck import/export code
- Local win/loss statistics
- Collection index for all 120 BP01 Character entries
- BP01-001 through BP01-030 Red are currently the executable gameplay pool

## v1.2 — Mobile interaction pass

- Tap-to-inspect cards
- Legal-target highlighting
- Draw / call / attack / Rush visual feedback
- Manual Lv4–6 exact-Level payment
- Manual effect targets where implemented
- Battle repositioning
- Manual Wing attack order
- Battle ↔ Base movement
- Counter and attack-response prompts for implemented Red interactions

## v1.3 — BP01 Red effect-engine alpha

- 30 BP01 Red cards playable in the current Alpha pool
- Structured operation-based effect handling
- Paraphrased card effect descriptions
- Trigger / Auto / Activate / Counter-style interactions represented by the engine
- Red-card interactions include prune, retreat, Void, attach, Base movement, deck/hand manipulation, Power/Range/Level modification, extra attacks and call-payment triggers
- 0-Power immediate retreat
- Rush Point victory and deck-out handling
- Offline AI updated for the new client

### Scope note

BP01-031 through BP01-120 are indexed in Collection by card code/name/color, but are **catalog-only in v1.3**. They are not presented as fully implemented cards until their stats/effects are added and verified.

Card effect descriptions in this fan prototype are paraphrased. v1.3 is an Alpha rules implementation, not a tournament-certified rules client.

## Build the APK from an Android phone

Android Studio is not required.

1. Open this repository in GitHub.
2. Go to **Actions**.
3. Open **Build Android APK**.
4. Tap **Run workflow**.
5. Open the successful run.
6. Download the **HeroRushLive-v1.3-alpha-debug** artifact.
7. Extract the downloaded artifact ZIP.
8. Install **HeroRushLive-v1.3-alpha-debug.apk**.

Android may ask you to allow **Install unknown apps** for your browser or file manager.

## Cloud build

The source ZIP is stored as base64 chunks under `source-parts/`. GitHub Actions reconstructs the Android project, validates the JavaScript assets, installs Android SDK 36 / Build Tools 36.0.0, and builds the debug APK with JDK 17 and Gradle 9.4.1.

This is an unofficial fan-made testing project and is not affiliated with Marvel or the game publisher.
