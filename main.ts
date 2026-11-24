// News Image entry for make.fun's news-image-20261124 competition.
//
// The picture itself lives beside this file as entry.png — a front page that
// sums up the world news of Tuesday, 24 November 2026. This program's whole
// job is to place that picture where the grader looks for it: entry.png in
// the output directory (/output inside the grading container, or the folder
// named by MAKEFUN_OUTPUT_DIR when run elsewhere for a local check).
//
// The copy is a plain file copy, so the bytes the judge sees are exactly the
// bytes committed here, and two runs always produce the same file.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
