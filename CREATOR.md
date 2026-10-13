# Creator Profile

Your identity, positioning, and workflow for video work in this workspace. **Read this before every video task** (alongside `PREFERENCES.md`). Use it for on-screen text, niche framing, and workflow assumptions.

## Identity

- **Name on-screen**: Creator
- **Instagram**: —
- **TikTok**: —
- **YouTube**: —
- **X / other**: —

When putting handles on-screen (lower-thirds, outros, end-cards), use the platform-appropriate handle.

## Platform priority

- **Primary format**: 9:16 vertical (1080×1920)
- **Platforms**: Cross-post to TikTok, Instagram Reels, and YouTube Shorts.

## Content niche

- **Topics**: AI tools, software engineering, tech workflows & digital creation.
- **Default tone**: Fast-paced, high-retention, concise, visually rich, and punchy (Hormozi-style educational delivery).

## On-camera mix

- **Mode**: Face-cam primary (You record speaking footage, assistant overlays visuals).
- **Face-cam** → use `/short-form-video` face-mode choreography (speaker as primary anchor; graphics placed in negative safe zones; zero face obstruction).
- **Faceless fallback** → motion graphics + AI TTS narration (`npx hyperframes tts`) or screen-recordings.

## Workflow — division of labor

- **Pre-recorded speaking footage with layered visuals**: You record your video or deliver raw takes; the assistant analyzes speech with Whisper, tightens pauses/stutters, builds synchronized kinetic typography, and composites explanatory diagrams, charts, and SFX directly over the footage.

## Brand identity

- **Theme**: Hormozi / High-Energy aesthetic (configured in `assets/brand-tokens.css`).
- **Accent**: Neon Green (`#00FF66`) for positive metrics & money, Warning Red (`#FF3B30`) for bottlenecks & risks, and Emphasis Yellow (`#FFDF00`) for focal points.
- **Background**: Pitch black (`#000000`) with semi-transparent backdrop cards.
- **Typography**: Bold uppercase Montserrat ExtraBold / Impact with strong black outline.

## Inspiration creators

Studied creators live in [`_reference/creator-library/`](_reference/creator-library/). Paste any TikTok / Instagram Reel / YouTube Short URL and run `/study-creator <url>` to analyze their pacing, kinetic type, and signature transitions.

## Posting cadence & length defaults

- **Default length**: 15–45s short-form vertical sweet spot.
- **Default fps**: 30 fps (matches TikTok + Instagram standards).

## Project slug convention

**Topic-only, kebab-case.** Each video gets a new subfolder under `video-projects/<topic-slug>/`. Examples: `ai-agents-intro`, `prompting-101`, `tool-of-the-week`.
