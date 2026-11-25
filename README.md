[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/rexxxspace/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/rexxxspace/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World in One Picture — Tuesday, 24 November 2026

A make.fun **news-image-20261124** entry: one 1024×1024 PNG that sums up the
world news of Tuesday, 24 November 2026, drawn as a newspaper front page.

## The image

`entry.png` is a one-page newspaper — "The World in One Page" — carrying
**30 stories, every one of which happened or was first reported on Tuesday
24 November 2026 (UTC)**, with a giant dated masthead, a big-numbers strip,
a region bar, certainty/source tags, a pinned world map, and a DATE CHECK
box that names the big stories deliberately left out because they belong
to other days.

Leads:

1. **Drone war.** Russia says its defences downed 699 Ukrainian drones
   overnight, 355 bound for Moscow; a strike on Zaporizhzhia kills 2 and
   wounds 40 (Russian MoD / Kyiv).
2. **Markets — Asia.** Tuesday's Asian close as Wall Street's rally echoes
   east: Taiex +8.99% (a record points gain), Kospi +6.32%, Nikkei +3.91%
   (CNA / Yonhap / Nikkei).
3. **Refugees — Kuala Lumpur.** Anwar tells parliament 6,500+ Rohingya will
   return to Myanmar in December — 1,500 by navy ship, 5,303 by air — days
   after the ICJ's genocide ruling (PM Anwar / AFP).

Plus nine story cards (Baghdad takes the Kurdish oilfields; Iran's tanker
mine claim; a Russian drone enters Poland; the Gaza strike that killed
Hamas's security chief; the EU's 350k cap on Chinese hybrid cars; Hanoi's
deadly restaurant blast; Hasina's 16 Dec return; the Solomons ending their
China pact; Mexico trying "El Chapo Isidro" at home) and 18 more one-line
stories — NATO's space-defence vow, Sanofi's $41bn Insmed deal in the
numbers strip, Senegal's AFCON restoration, the Shenzhou-24 crew, and more.

Left out on purpose (DATE CHECK): Nvidia rehiring Huang (Mon 23 Nov),
Ukraine's Libya ship strike (22–23 Nov), the COP31 collapse (Sun 22 Nov),
the Democrats' 258 House seats (22 Nov), and the Banten factory fire
itself (Sat 21 Nov — only Tuesday's toll update would have counted).

## How it works

- `main.ts` (Node 22, standard library only) copies `entry.png` to
  `/output/entry.png` — deterministic, no network, same bytes every run.
- `build_image_v3.py` is the generator that drew `entry.png` with Pillow
  (`build_image.py` / `build_image_v2.py` drew the earlier versions):
  every headline, label and illustration is rendered programmatically,
  so the text is exact and the file is reproducible.

## License

MIT — see `LICENSE`.
