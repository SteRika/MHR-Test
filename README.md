# MHR-Test — Hero Rush Simulator v0.9 Alpha

Unofficial, text-only Marvel Hero Rush simulator prototype for Android. No card artwork is bundled.

## Build the APK from your phone

You do not need Android Studio.

1. Open this repository on GitHub.
2. Go to **Actions**.
3. Open **Build Android APK**.
4. Tap **Run workflow**.
5. When the run is green, open it and download the **HeroRushSimulator-v0.9-alpha-debug** artifact.
6. Extract the artifact ZIP and install `HeroRushSimulator-v0.9-alpha-debug.apk`.

Android may ask you to allow **Install unknown apps** for your browser or file manager.

## Current v0.9 Alpha

- Offline Android app
- Text-only cards; no artwork
- Deck builder and legality checks
- 50-card Character deck
- Maximum 3 copies per card name
- Maximum 2 colors
- Separate 9-card Rush deck
- Opening hand + mulligan
- Draw 2 each turn
- Base deployment
- Manual exact-Level payment for high-Level calls
- Front / Wing L / Wing R / Back battle zones
- Reposition and Wing attack order
- Range and Power combat
- Rush Point victory
- Offline AI
- Paraphrased effect descriptions

## Repository packaging

The Android source is stored in `HeroRushSimulator_v0.9_Android_Source.b64` as a base64-encoded ZIP. The GitHub Actions workflow decodes and extracts it automatically before compiling. This keeps the mobile upload/setup simple while still producing a normal Android APK.

This is an unofficial fan-made testing project and is not affiliated with Marvel or the game publisher.
