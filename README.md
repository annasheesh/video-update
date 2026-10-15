# HyperFrames AI Video Editor — Automated Short-Form Pipeline

An automated, high-retention video editing workspace powered by [Hyperframes](https://hyperframes.heygen.com), [OpenAI Whisper](https://github.com/openai/whisper), and [GSAP](https://gsap.com). Transforms raw talking-head footage into polished, Hormozi-style short-form videos with kinetic captions, dynamic camera punch-ins, multi-asset AI galleries, and animated visual roadmaps.

> **Zero video editing software required.** Every composition is declarative HTML/CSS with deterministic GSAP timelines rendered via headless Chromium.

---

## 🎬 Showcase: `short-form-11`

- **Final Render**: [`short-form-11-final.mp4`](short-form-11-final.mp4) (1080×1920 portrait · 15.4s · 60fps equivalent)
- **Source Footage**: [`example vid/11.mp4`](example%20vid/11.mp4)
- **Active Project Folder**: [`video-projects/short-form-11/`](video-projects/short-form-11/)

### Visual Composition Breakdown

| Scene | Timestamp | Core Visual Animation | Design Features |
| :--- | :---: | :--- | :--- |
| **Scene 1** | `0.0s – 4.2s` | **Raw In ➔ Edit Out** | Pipeline card, speaker thumbnail, glowing pulse bead, Claude status, 5-picture filmstrip (`464 FRAMES`) |
| **Scene 2** | `4.2s – 8.6s` | **Multi-Picture AI Showcase** | Prompt typing card ➔ 3-Picture AI Gallery (`Aperture Lens`, `Organic Sculpture`, `Travertine Arches`) + Ref 1 Diamond Keyframe HUD |
| **Scene 3** | `8.6s – 13.2s` | **Edits By Me: Zero** | Circular pointer cursor, `EDITS BY ME: 0` counter, dynamic 0% ➔ 100% render progress bar, `✓ final.mp4 ready` badge |
| **Scene 4** | `13.2s – 15.4s` | **Animated SVG Roadmap** | Arched glowing flow paths with arrowheads, 3 Milestone Stations (Audio ➔ Code ➔ Export), video preview thumbnail, high-contrast CTA pill |
| **Track 2** | `0.0s – 15.4s` | **Kinetic Subtitles** | Word-level active highlighting synced to Whisper timestamps in the warm aesthetic palette |

---

## 🎨 Warm Luxury Aesthetic Palette

The visual design follows a cohesive, high-retention aesthetic palette:

| Color | Hex | Purpose |
| :--- | :---: | :--- |
| **Warm Cream** | `#F5F0E8` | High-contrast typography, primary headlines, active highlight words, CTA pill |
| **Deep Espresso** | `#302820` | Frosted glass card backgrounds (`backdrop-filter: blur(24px)`), deep shadow anchors |
| **Caramel Bronze** | `#A68B65` | Accent glowing borders, milestone badges, keyframe diamonds, path gradients |
| **Sand** | `#C8B9A6` | Subtitles, metadata tags, secondary timestamps |
| **Pale Linen** | `#E5DED4` | Badges, card accents, subtle borders |

---

## ⚡ Quick Start

### 1. Prerequisites
- **Node.js 22+** (`node -v`)
- **FFmpeg** on your system `PATH` (`ffmpeg -version`)
- **Google Chrome** (latest) — HyperFrames renders through headless Chromium

### 2. Install Dependencies
```bash
npm install
npx skills add heygen-com/hyperframes --yes
```

### 3. Verify Environment
```bash
npx hyperframes doctor
npm run preflight:all
```

---

## 🛠️ CLI Commands

### Interactive Live Preview (Studio)
Launch the browser editor to scrub timestamps and inspect animations in real time:
```bash
npx hyperframes preview video-projects/short-form-11
```

### Headless Render to MP4
Render the complete video with hardware-accelerated Chromium capture:
```bash
npx hyperframes render video-projects/short-form-11 --output renders/short-form-11.mp4
```

### Lint Compositions
Validate deterministic timing, track indices, and GSAP timeline rules:
```bash
npx hyperframes lint
```

---

## 📁 Repository Structure

```text
├── video-projects/
│   ├── short-form-11/              # Production Hormozi short-form project
│   │   ├── index.html              # Main root composition with camera punch-ins
│   │   ├── compositions/
│   │   │   ├── captions.html       # Word-level kinetic subtitles
│   │   │   ├── scene1-raw-vs-edit.html
│   │   │   ├── scene2-ai-animation.html
│   │   │   ├── scene3-automated-edits.html
│   │   │   └── scene4-how-to-do-it.html
│   │   ├── assets/
│   │   │   ├── images/             # AI generated artwork & filmstrip thumbnails
│   │   │   ├── sfx/                # UI, cinematic, and transition sound effects
│   │   │   ├── master_audio.mp3    # Mixed & mastered audio track
│   │   │   └── source_video.mp4    # Base speaker video
│   │   └── final_video.mp4         # Rendered 1080x1920 master output
│   └── welcome-demo/               # Starter template & demo composition
├── scripts/
│   ├── preflight.mjs               # Project health check script
│   └── preflight-all.mjs           # Multi-project validator
├── short-form-11-final.mp4         # Master deliverable video (15.4s)
├── CREATOR.md                      # Creator profile & on-camera specs
├── PREFERENCES.md                  # Pacing & layout rules
└── AGENTS.md                       # AI pairing & framework rules
```

---

## 🤖 AI Skills Available

This workspace includes integrated skills for autonomous video editing:

- `/short-form-video`: Transform raw talking-head footage into Hormozi-style short-form edits.
- `/make-a-video`: Build complete videos from a concept or script end-to-end.
- `/study-creator <url>`: Reverse-engineer motion graphics and pacing from reference Instagram Reels / TikToks.
- `/feedback`: Distill post-production feedback directly into `PREFERENCES.md` for continuous learning.
- `/hyperframes`: HyperFrames declarative composition reference.
- `/gsap`: GSAP animation standards and best practices for video.

---

## 📄 License & Credits

- **Workspace Code**: MIT License ([`LICENSE`](LICENSE)).
- **HyperFrames Framework**: © HeyGen ([Apache 2.0](https://hyperframes.heygen.com)).
- **Sound Effects**: Free for commercial use (Mixkit & Pixabay CC0, see [`assets/sfx/MANIFEST.md`](assets/sfx/MANIFEST.md)).
