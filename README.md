[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/rexxxspace/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/rexxxspace/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World in One Picture — Tuesday, 24 November 2026

A make.fun **news-image-20261124** entry: one 1024×1024 PNG that sums up the
world news of Tuesday, 24 November 2026, drawn as a newspaper front page.

## The image

`entry.png` is a front-page layout with a dated masthead, a lead story with
a big-number stat strip, four story cards, and an "also today" strip:

1. **Lead — Wall Street.** Nvidia's board reinstated Jensen Huang as CEO on
   Monday, 11 days after he quit, after President Trump pressed the board;
   shares jumped **31%** (about $950B of value added in a day), with the
   Nasdaq up 6.5% and the S&P 500 up 4.7% (Reuters / Investopedia / Barron's).
2. **War at sea — Benghazi, Libya.** Seven Ukrainian naval drones sank the
   Russian corvette *Merkury* in Benghazi port and hit the arms cargo ship
   *Angara* (AP / Reuters / CNN / WSJ).
3. **Climate — Antalya, Türkiye.** The COP31 climate talks collapsed with no
   deal after the EU and UK rejected a final text that never mentioned fossil
   fuels — the first failed COP since Copenhagen in 2009 (CNN / WSJ).
4. **Asia — Cikande, Banten, Indonesia.** A fire at a Milkita candy factory
   killed 24 people, with about 30 workers still missing as rescuers searched
   the wreckage (Reuters / AP).
5. **Americas — Washington.** Democrats won **258 House seats** — Chuck
   Hubbard's win over Virginia Foxx in North Carolina sealed the largest
   House majority since 1992 (AP).

Also today: UN Secretary-General Guterres, at the Bridgetown AI Safety
Summit in Barbados, urged a global AI risk framework within a year; a
supercell storm in Tupanciretã, Brazil killed 5 people and damaged about
8,000 homes; and drones hit the Russian cargo ship *Sparta II* in the
Baltic Sea.

## How it works

- `main.ts` (Node 22, standard library only) copies `entry.png` to
  `/output/entry.png` — deterministic, no network, same bytes every run.
- `build_image_v2.py` is the generator that drew `entry.png` with Pillow
  (`build_image.py` drew the first version): every headline, label and
  illustration is rendered programmatically, so the text is exact and
  the file is reproducible.

## License

MIT — see `LICENSE`.
