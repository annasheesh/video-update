# High-Retention Animated Video Overlays & Sound Design

A high-retention short-form video edit engineered with **HyperFrames (HTML5 + GSAP + Headless Chromium)**, built on real talking-head footage from `example vid/source_video.mp4`.

## Features
- **Visual Event Frequency**: Meaningful animations and UI changes triggered every 1.5–3.0 seconds.
- **Sound Design Frequency**: 12 precisely synced sound effects (whooshes, UI pops, blips, ticks, impacts, swishes, clacks, and shimmers).
- **Hormozi-Style Kinetic Typography**: High-contrast bold subtitles with black outline and keyword color coding.
- **Zero Face Occlusion**: Speaker's face, eyes, and mouth remain 100% unobstructed. Floating cards occupy negative space at top and chest area.
- **Studio Preview & Deterministic Render**: Real-time browser scrubbing and pixel-accurate headless MP4 render.

## Project Structure
- `index.html` — Root composition orchestrating the speaker video, overlays, and audio track.
- `compositions/`
  - `scene1.html` — Hook: "Raw in. Edit out." floating video file card + Claude editing button.
  - `scene2.html` — Tool Reveal: 3D tilted GitHub card + Heygen brand badge aligned with speaker's finger point.
  - `scene3.html` — Verification: Open Source & Apache-2.0 pills + bold FREE stamp.
  - `scene4.html` — Zero Edits Demonstration: Red prohibition circle + "EDITS BY ME: 0" + chest quote.
  - `scene5.html` — Automated Pipeline: Flowchart with animated connectors + 100% AUTOMATED badge.
  - `captions.html` — Kinetic subtitles synchronized with transcript.
- `assets/`
  - `source_video.mp4` — Raw 60fps talking-head footage.
  - `master_audio.mp3` — Speech + ducked SFX normalized to -14 LUFS / -1 dBTP.
  - `sfx/` — High-retention UI, motion, and impact sound effects.
  - `images/` — Thumbnails and badge graphic assets.

## Execution & Commands
```bash
# Preview live in browser (port 3002)
npx hyperframes preview video-projects/high-retention-overlays

# Validate compositions
npx hyperframes lint

# Render draft MP4
npx hyperframes render --quality draft --output renders/final_video.mp4
```
