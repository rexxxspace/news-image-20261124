#!/usr/bin/env python3
"""DRAFT v2 (not submitted) of the news-image-20261124 entry: one 1024x1024
newspaper-style image summing up the world news of Tuesday, 24 November 2026.

What changed vs v1 (from the round-1 board teardown):
- LEAD is now the day's biggest story, which v1 omitted entirely: Nvidia
  reinstates Jensen Huang as CEO, shares +31% (verified: Reuters/Investopedia/
  Barron's — closed +31% Mon 23 Nov, ~$950bn added, largest one-day gain ever
  for a US company; Nasdaq +6.5%, S&P 500 +4.7%; Trump pressed the board).
  Two of the five entries directly above us in round 1 led with this story.
- New big-number stat strip (readable at 300 px): +31% / $950BN / 258 / 24 / 5.
- Democrats' 258 House seats (largest since 1992, verified AP) promoted from
  absent to a full card.
- The five verified v1 stories are ALL kept: Ukraine sea drones off Libya,
  COP31 collapse, Cikande factory fire, UN AI rules (Barbados), Brazil storm —
  the last two move to the ALSO TODAY strip to make room.
- Same programmatic PIL pattern as build_image.py; same masthead, same fonts.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (250, 247, 240)
NAVY = (16, 34, 72)
INK = (22, 22, 22)
RED = (190, 18, 38)
WHITE = (255, 255, 255)
GREY = (90, 90, 90)
GREEN = (24, 110, 74)
GOLD = (245, 197, 90)

F_BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
F_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
F_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def wrap(text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def text_block(x, y, text, fnt, fill, maxw, leading=1.18):
    for line in wrap(text, fnt, maxw):
        d.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y

# ---------------- Masthead ----------------
d.rectangle([0, 0, W, 118], fill=NAVY)
d.rectangle([0, 118, W, 126], fill=RED)
d.text((36, 14), "W O R L D   N E W S  —  T H E   D A Y   I N   O N E   P I C T U R E",
       font=font(F_BOLD, 25), fill=(170, 195, 235))
d.text((34, 44), "TUESDAY, 24 NOVEMBER 2026", font=font(F_BLACK, 57), fill=WHITE)

# ---------------- Lead story: Nvidia / Huang ----------------
LX, LY, LW, LH = 28, 140, 968, 252
d.rectangle([LX, LY, LX + LW, LY + LH], fill=WHITE, outline=(210, 205, 195), width=2)
d.rectangle([LX, LY, LX + LW, LY + 40], fill=RED)
d.text((LX + 18, LY + 7), "LEAD STORY  •  MARKETS — WALL STREET", font=font(F_BOLD, 26), fill=WHITE)

TX, TW = LX + 18, 630
y = LY + 52
y = text_block(TX, y, "HUANG IS BACK — NVIDIA SOARS 31% IN A DAY",
               font(F_BLACK, 44), INK, TW, 1.12)
y += 8
y = text_block(TX, y, "Nvidia's board reinstated Jensen Huang as CEO on Monday, 11 days after "
                      "he quit, after President Trump pressed the board. Shares jumped 31%.",
               font(F_REG, 23), (45, 45, 45), TW, 1.22)
assert y <= LY + LH - 8, f"lead overflow: {y} > {LY + LH - 8}"

# Stat box (right of lead)
SX, SY, SW, SH = 700, LY + 52, 278, 188
d.rectangle([SX, SY, SX + SW, SY + SH], fill=GREEN)
d.text((SX + 18, SY + 10), "+31%", font=font(F_BLACK, 62), fill=WHITE)
d.text((SX + 18, SY + 82), "NVIDIA SHARES,", font=font(F_BOLD, 20), fill=WHITE)
d.text((SX + 18, SY + 106), "MONDAY'S CLOSE", font=font(F_BOLD, 20), fill=WHITE)
d.line([SX + 18, SY + 138, SX + SW - 18, SY + 138], fill=(255, 255, 255), width=2)
d.text((SX + 18, SY + 146), "NASDAQ +6.5%", font=font(F_BOLD, 19), fill=GOLD)
d.text((SX + 18, SY + 168), "S&P 500 +4.7%", font=font(F_BOLD, 19), fill=GOLD)

# ---------------- Big-number stat strip ----------------
STY, STH = 406, 56
d.rectangle([28, STY, 996, STY + STH], fill=NAVY)
stats = [("+31%", "NVIDIA SHARES"),
         ("$950BN", "VALUE ADDED IN A DAY"),
         ("258", "DEMOCRATS' HOUSE SEATS"),
         ("24", "DEAD IN CIKANDE FIRE"),
         ("5", "DEAD IN BRAZIL STORM")]
col_w = 968 // 5
for i, (num, label) in enumerate(stats):
    cx = 28 + i * col_w
    if i:
        d.line([cx, STY + 8, cx, STY + STH - 8], fill=(70, 95, 140), width=2)
    nw = d.textlength(num, font=font(F_BOLD, 29))
    d.text((cx + (col_w - nw) / 2, STY + 3), num, font=font(F_BOLD, 29), fill=GOLD)
    lw = d.textlength(label, font=font(F_BOLD, 14))
    d.text((cx + (col_w - lw) / 2, STY + 36), label, font=font(F_BOLD, 14), fill=WHITE)

# ---------------- Story cards ----------------
def card(x, y, w, h, accent, kicker, headline, body, draw_icon):
    d.rectangle([x, y, x + w, y + h], fill=WHITE, outline=(210, 205, 195), width=2)
    d.rectangle([x, y, x + w, y + 38], fill=accent)
    d.text((x + 14, y + 7), kicker, font=font(F_BOLD, 23), fill=WHITE)
    draw_icon(x + w - 62, y + 50)
    yy = text_block(x + 16, y + 47, headline, font(F_BLACK, 30), INK, w - 96, 1.12)
    yy += 5
    yy = text_block(x + 16, yy, body, font(F_REG, 22), (45, 45, 45), w - 30, 1.22)
    assert yy <= y + h - 6, f"card overflow: {kicker} ends {yy} > {y + h - 6}"

def icon_drones(cx, cy):
    d.polygon([(cx, cy + 30), (cx + 10, cy + 18), (cx + 40, cy + 18), (cx + 48, cy + 30)],
              fill=(30, 30, 30))
    d.rectangle([cx + 18, cy + 8, cx + 28, cy + 18], fill=(30, 30, 30))
    for wy in (cy + 40, cy + 50):
        d.arc([cx + 2, wy, cx + 22, wy + 10], 180, 360, fill=(64, 110, 165), width=3)
        d.arc([cx + 28, wy, cx + 48, wy + 10], 180, 360, fill=(64, 110, 165), width=3)

def icon_climate(cx, cy):
    d.rectangle([cx, cy, cx + 44, cy + 54], fill=(240, 240, 235), outline=INK, width=2)
    d.line([cx + 6, cy + 14, cx + 38, cy + 14], fill=GREY, width=3)
    d.line([cx + 6, cy + 24, cx + 38, cy + 24], fill=GREY, width=3)
    d.line([cx + 22, cy + 2, cx + 16, cy + 20, cx + 26, cy + 34, cx + 18, cy + 52], fill=RED, width=4)

def icon_factory(cx, cy):
    d.rectangle([cx, cy + 18, cx + 48, cy + 56], fill=(90, 90, 90))
    d.polygon([(cx, cy + 18), (cx + 16, cy + 6), (cx + 16, cy + 18)], fill=(90, 90, 90))
    d.polygon([(cx + 16, cy + 18), (cx + 32, cy + 6), (cx + 32, cy + 18)], fill=(90, 90, 90))
    for dx, dy, r, c in [(24, 2, 15, (255, 122, 26)), (14, 10, 11, (255, 176, 32)), (34, 10, 11, (230, 60, 20))]:
        d.ellipse([cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r], fill=c)

def icon_dome(cx, cy):
    d.pieslice([cx + 8, cy, cx + 40, cy + 32], 180, 360, fill=(16, 34, 72))
    d.rectangle([cx + 4, cy + 30, cx + 44, cy + 54], fill=(16, 34, 72))
    for bx in (cx + 10, cx + 20, cx + 30):
        d.rectangle([bx, cy + 34, bx + 4, cy + 50], fill=WHITE)
    d.rectangle([cx, cy + 54, cx + 48, cy + 58], fill=(16, 34, 72))

ROW1_Y, ROW_H, CW, GAP = 476, 232, 474, 20
card(28, ROW1_Y, CW, ROW_H, RED, "WAR AT SEA  •  LIBYA",
     "UKRAINE SEA DRONES SINK WARSHIP",
     "Seven naval drones sank the corvette Merkury in Benghazi port and hit the "
     "arms ship Angara.", icon_drones)
card(28 + CW + GAP, ROW1_Y, CW, ROW_H, (24, 110, 74), "CLIMATE  •  ANTALYA, TÜRKIYE",
     "COP31 CLIMATE TALKS COLLAPSE — NO DEAL",
     "After two weeks, the EU and UK rejected a final text that never mentioned fossil fuels — "
     "the first failed COP since 2009.", icon_climate)

ROW2_Y = 722
card(28, ROW2_Y, CW, ROW_H, (198, 84, 20), "ASIA  •  BANTEN, INDONESIA",
     "FACTORY FIRE: 24 DEAD, 30 STILL MISSING",
     "Rescuers search the wreckage of a Milkita candy factory in Cikande after a weekend blaze. "
     "A short circuit is suspected.", icon_factory)
card(28 + CW + GAP, ROW2_Y, CW, ROW_H, (16, 34, 72), "AMERICAS  •  WASHINGTON",
     "DEMOCRATS WIN 258 HOUSE SEATS",
     "Chuck Hubbard's win over Virginia Foxx in North Carolina sealed the sweep — "
     "the largest House majority since 1992.", icon_dome)

# ---------------- Ticker ----------------
TY = 968
d.rectangle([0, TY, W, H], fill=(15, 15, 15))
d.text((28, TY + 4), "ALSO TODAY:", font=font(F_BOLD, 19), fill=(245, 197, 90))
d.text((172, TY + 4), "UN chief: global AI rules within a year — Guterres at the Bridgetown summit",
       font=font(F_REG, 19), fill=WHITE)
d.text((172, TY + 25), "Brazil supercell storm: 5 dead, 8,000 homes hit  •  Drones hit Sparta II in the Baltic",
       font=font(F_REG, 19), fill=WHITE)

img.save("/home/hatch/workspace/makefun/news-image-20261124/entry-v2-draft.png")
img.resize((300, 300), Image.LANCZOS).save(
    "/home/hatch/workspace/makefun/news-image-20261124/entry-v2-draft-300px.png")
print("saved v2 draft + 300px thumbnail")
