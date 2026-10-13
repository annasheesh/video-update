# PREFERENCES — Your Video Taste

Your accumulated taste for video work in this workspace. Populated over time via the `/feedback` skill.

**Read this file BEFORE every video task.** Apply the rules as overrides — they win over default skill choices and `MOTION_PHILOSOPHY.md` defaults when there's a conflict. If a section is empty, fall back to skill defaults.

---

## Visual style

- Explanatory graphics (diagrams, branching options, progress gauges) must be layered over the original footage in available negative space (top safe zone `y: 100–480`); never cover the speaker's face or eyes. (2026-10-13)
- Use dark frosted glass cards (`rgba(15, 15, 20, 0.9)`) with glowing neon accents (`#00FF66` positive, `#FF3B30` warning, `#FFDF00` focal point). (2026-10-13)

## Pacing

- Tight, natural jump cuts at phrase boundaries with 50ms equal-power cosine crossfades. (2026-10-13)
- Introduce a meaningful visual change (punch-in, diagram, metric callout) every 2–4 seconds. (2026-10-13)
- Use subtle 105–115% camera punch-ins on key jump cuts or punchlines to disguise cuts and emphasize statements. (2026-10-13)

## Captions

- Bold uppercase text (`Montserrat ExtraBold` / `Impact`) with thick black stroke (`-webkit-text-stroke: 4px #000`) and soft ambient drop shadow for mobile readability. (2026-10-13)
- Quick 100ms scale-in bounce entrance (`scale: 0.75 → 1.05 → 1.0`). (2026-10-13)
- Group captions into 1–3 word natural rhythmic phrases with contextual color highlights. (2026-10-13)

## Transitions

- Whip-pans, camera scale punch-ins, and directional card slides. Avoid plain cross-dissolves. (2026-10-13)

## Audio

- 85Hz high-pass filter (Butterworth 2nd-order) on speech to remove microphone boom and room rumble. (2026-10-13)
- Master loudness target: -14 to -16 LUFS integrated, True Peak limited at or below -1.0 dBTP. (2026-10-13)
- Subtle synthesized SFX (gentle whooshes on camera zooms, light pops on diagram reveals, chimes on alerts) mixed at -22 dBFS ducked under speech. (2026-10-13)

## Brand

- Default theme: Hormozi High-Energy / Tech (configured in `assets/brand-tokens.css`). (2026-10-13)

## Avoid

- Never replace the speaker with full-screen b-roll or static slides; the speaker is the primary visual anchor. (2026-10-13)
- Never place captions or diagrams over the speaker's eyes, nose, or mouth. (2026-10-13)
- Avoid unpadded edge cuts that produce vocal clicks or pop artifacts. (2026-10-13)
