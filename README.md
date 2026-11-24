[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/rexxxspace/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/rexxxspace/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World in One Picture — Tuesday, 24 November 2026

A make.fun **news-image-20261124** entry: one 1024×1024 PNG that sums up the
world news of Tuesday, 24 November 2026, drawn as a newspaper front page.

## The image

`entry.png` is a front-page layout with a dated masthead and five stories,
plus a news ticker:

1. **Lead — Benghazi, Libya.** Seven Ukrainian naval drones sank the Russian
   corvette *Merkury* in Benghazi port and hit the arms cargo ship *Angara* —
   a strike some 2,400 km from the front line (AP / Reuters / CNN / WSJ).
2. **Climate — Antalya, Türkiye.** The COP31 climate talks collapsed with no
   deal after the EU and UK rejected a final text that never mentioned fossil
   fuels — the first failed COP since Copenhagen in 2009 (CNN / WSJ).
3. **Asia — Cikande, Banten, Indonesia.** A fire at a Milkita candy factory
   killed 24 people, with about 30 workers still missing as rescuers searched
   the wreckage (Reuters / AP).
4. **Technology — Bridgetown, Barbados.** UN Secretary-General Guterres, at
   the Bridgetown AI Safety Summit, urged governments to agree a global AI
   risk framework within a year (Al Jazeera).
5. **Americas — Tupanciretã, Brazil.** A supercell storm killed 5 people,
   injured 265 and damaged about 8,000 homes in Rio Grande do Sul
   (Al Jazeera / QNA).

Ticker: drones hit the Russian cargo ship *Sparta II* in the Baltic Sea
(Finland led the rescue), and the UN called for an independent probe into
the strikes on Libyan soil.

## How it works

- `main.ts` (Node 22, standard library only) copies `entry.png` to
  `/output/entry.png` — deterministic, no network, same bytes every run.
- `build_image.py` is the generator that drew `entry.png` with Pillow:
  every headline, label and illustration is rendered programmatically,
  so the text is exact and the file is reproducible.

## License

MIT — see `LICENSE`.
