import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

// Write /output first: the entry image is copied, byte for byte, into the
// grader's output directory. Create the directory if it does not exist yet.
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
