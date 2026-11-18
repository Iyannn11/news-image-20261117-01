// News-image entry for 17 November 2026 (make.fun, slug news-image-20261117).
// The image is drawn programmatically by build_image.py (PIL, real fonts, so no
// text can come out garbled) and shipped as entry.png beside this file; the
// program copies it to /output/entry.png, exactly what the gate reads.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
