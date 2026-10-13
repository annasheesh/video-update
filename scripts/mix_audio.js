const { execFileSync } = require('child_process');
const path = require('path');

const sfxDir = path.resolve('video-projects/high-retention-overlays/assets/sfx');
const speech = path.resolve('video-projects/high-retention-overlays/assets/speech.mp3');
const out = path.resolve('video-projects/high-retention-overlays/assets/master_audio.mp3');

const cues = [
  ['sfx_whoosh_smooth.wav', 0.05, 0.55],
  ['sfx_ui_pop.wav', 0.42, 0.50],
  ['sfx_blip.wav', 1.25, 0.45],
  ['sfx_whoosh_smooth.wav', 3.20, 0.55],
  ['sfx_ui_pop.wav', 4.50, 0.50],
  ['sfx_ui_click.wav', 5.35, 0.45],
  ['sfx_tick.wav', 6.50, 0.45],
  ['sfx_impact.wav', 7.30, 0.55],
  ['sfx_swish.wav', 8.80, 0.50],
  ['sfx_clack.wav', 10.00, 0.50],
  ['sfx_marker.wav', 11.50, 0.45],
  ['sfx_shimmer.wav', 13.30, 0.45]
];

const inputs = ['-y', '-i', speech];
const filterParts = ['[0:a]volume=1.0[a0]'];
const mixInputs = ['[a0]'];

cues.forEach(([file, delaySec, vol], i) => {
  const idx = i + 1;
  inputs.push('-i', path.join(sfxDir, file));
  const delayMs = Math.round(delaySec * 1000);
  filterParts.push(`[${idx}:a]adelay=${delayMs}|${delayMs},volume=${vol}[a${idx}]`);
  mixInputs.push(`[a${idx}]`);
});

const filterStr = filterParts.join(';') + ';' + mixInputs.join('') + `amix=inputs=${mixInputs.length}:duration=first:dropout_transition=2,loudnorm=I=-14:TP=-1:LRA=7[outa]`;
const args = [...inputs, '-filter_complex', filterStr, '-map', '[outa]', '-c:a', 'libmp3lame', '-b:a', '192k', out];

try {
  execFileSync('ffmpeg', args, { stdio: 'inherit' });
  console.log('SUCCESS: Master audio track rendered with exact SFX synchronization at ' + out);
} catch (err) {
  console.error('Error rendering audio:', err.message);
  process.exit(1);
}
