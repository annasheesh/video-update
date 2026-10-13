const { execFileSync } = require('child_process');
const path = require('path');

const projectDir = path.resolve('video-projects/short-form-11');
const sfxDir = path.resolve('assets/sfx');
const speech = path.join(projectDir, 'assets/speech.mp3');
const out = path.join(projectDir, 'assets/master_audio.mp3');

// Subtle, elegant UI sound effects (NO background song bed)
const cues = [
  ['transitions/whoosh.mp3', 0.20, 0.25],
  ['ui/pop.mp3', 1.20, 0.25],
  ['ui/click.wav', 2.40, 0.25],
  ['transitions/swipe.mp3', 4.10, 0.25],
  ['cinematic/sparkle.mp3', 5.60, 0.30],
  ['ui/click.wav', 6.60, 0.25],
  ['ui/notification.mp3', 8.70, 0.30],
  ['ui/pop.mp3', 9.80, 0.25],
  ['transitions/whoosh.mp3', 11.20, 0.25],
  ['cinematic/paper-flip.mp3', 13.20, 0.25],
  ['ui/notification.mp3', 14.50, 0.25]
];

const inputs = ['-y', '-i', speech];
const filterParts = ['[0:a]volume=1.0[speech_vol]'];
const mixInputs = ['[speech_vol]'];

cues.forEach(([relPath, delaySec, vol], i) => {
  const file = path.join(sfxDir, relPath);
  const idx = inputs.length / 2;
  inputs.push('-i', file);
  const delayMs = Math.round(delaySec * 1000);
  filterParts.push(`[${idx}:a]adelay=${delayMs}|${delayMs},volume=${vol}[sfx${i}]`);
  mixInputs.push(`[sfx${i}]`);
});

const filterStr = filterParts.join(';') + ';' + mixInputs.join('') + `amix=inputs=${mixInputs.length}:duration=first:dropout_transition=2,loudnorm=I=-14:TP=-1:LRA=7[outa]`;
const args = [...inputs, '-filter_complex', filterStr, '-map', '[outa]', '-c:a', 'libmp3lame', '-b:a', '192k', out];

try {
  console.log('Rendering clean master audio (NO background song, pure speech + subtle aesthetic SFX)...');
  execFileSync('ffmpeg', args, { stdio: 'inherit' });
  console.log('SUCCESS: Rendered clean master audio at ' + out);
} catch (err) {
  console.error('Error rendering audio:', err.message);
  process.exit(1);
}
