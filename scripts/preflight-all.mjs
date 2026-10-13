import { readdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';

const projectsDir = 'video-projects';
let entries = [];
try {
  entries = readdirSync(projectsDir).filter((f) => {
    try {
      return statSync(join(projectsDir, f)).isDirectory();
    } catch {
      return false;
    }
  });
} catch (err) {
  console.error(`Could not read ${projectsDir}:`, err.message);
  process.exit(1);
}

console.log(`Running preflight across ${entries.length} project(s)...`);
let failed = 0;
for (const entry of entries) {
  const projPath = join(projectsDir, entry);
  console.log(`\n========================================`);
  console.log(`Project: ${projPath}`);
  console.log(`========================================`);
  const res = spawnSync('node', ['scripts/preflight.mjs', projPath], {
    stdio: 'inherit',
    shell: true,
  });
  if (res.status !== 0) {
    failed++;
  }
}

console.log(`\nPreflight summary: ${entries.length - failed}/${entries.length} passed.`);
if (failed > 0) {
  console.log(`Note: Some projects had preflight warnings or blockers.`);
}
