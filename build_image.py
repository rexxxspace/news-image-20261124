#!/usr/bin/env python3
"""Build the news-image-20261124 entry: one 1024x1024 newspaper-style image
summing up the world news of Tuesday, 24 November 2026.
Stories (verified 24 Nov 2026 against AP/Reuters/CNN/WSJ/Le Monde coverage):
1. Ukrainian sea drones sank Russian corvette Merkury at Benghazi, Libya; cargo ship Angara hit.
2. COP31 climate talks in Antalya collapsed with no deal over fossil-fuel language.
3. Indonesia candy-factory fire in Cikande, Banten: 24 dead confirmed, ~30 missing.
4. UN chief Guterres, at Bridgetown AI Safety Summit (Barbados): global AI framework within a year.
5. Brazil supercell storm in Tupancireta, Rio Grande do Sul: 5 dead, 265 injured, ~8,000 homes damaged.
Ticker: Russian cargo ship Sparta II hit by drones in the Baltic; UN calls for probe into Libya strikes.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (250, 247, 240)
NAVY = (16, 34, 72)
INK = (22, 22, 22)
RED = (190, 18, 38)
WHITE = (255, 255, 255)
GREY = (90, 90, 90)

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

# ---------------- Lead story ----------------
LX, LY, LW, LH = 28, 140, 968, 338
d.rectangle([LX, LY, LX + LW, LY + LH], fill=WHITE, outline=(210, 205, 195), width=2)
d.rectangle([LX, LY, LX + LW, LY + 40], fill=RED)
d.text((LX + 18, LY + 7), "LEAD STORY  •  WAR AT SEA — MEDITERRANEAN", font=font(F_BOLD, 26), fill=WHITE)

# Illustration: sea scene (left)
IX, IY, IW, IH = LX + 18, LY + 54, 384, 268
d.rectangle([IX, IY, IX + IW, IY + IH], fill=(24, 62, 110))            # sea
d.rectangle([IX, IY, IX + IW, IY + 118], fill=(64, 110, 165))          # sky
# warship silhouette (grey)
sx, sy = IX + 56, IY + 138
d.polygon([(sx, sy + 58), (sx + 20, sy + 32), (sx + 246, sy + 32), (sx + 268, sy + 58)], fill=(52, 58, 66))
d.rectangle([sx + 58, sy + 6, sx + 148, sy + 32], fill=(52, 58, 66))
d.rectangle([sx + 94, sy - 18, sx + 104, sy + 6], fill=(52, 58, 66))
d.rectangle([sx + 168, sy + 14, sx + 212, sy + 32], fill=(52, 58, 66))
# explosion burst on ship
ex, ey = sx + 200, sy + 2
for dx, dy, r, c in [(0, 0, 32, (255, 122, 26)), (-15, 9, 22, (255, 176, 32)),
                    (17, 11, 20, (230, 60, 20)), (2, -16, 18, (255, 205, 60))]:
    d.ellipse([ex + dx - r, ey + dy - r, ex + dx + r, ey + dy + r], fill=c)
# smoke
for dx, dy, r in [(-4, -48, 18), (16, -66, 24), (42, -80, 28)]:
    d.ellipse([ex + dx - r, ey + dy - r, ex + dx + r, ey + dy + r], fill=(120, 120, 120))
# sea drones (small boats) approaching
for bx, by in [(IX + 30, IY + 226), (IX + 116, IY + 242)]:
    d.polygon([(bx, by), (bx + 12, by - 12), (bx + 52, by - 12), (bx + 62, by)], fill=(20, 20, 20))
    d.rectangle([bx + 22, by - 22, bx + 34, by - 12], fill=(20, 20, 20))
# waves
for wy in (IY + 206, IY + 232, IY + 254):
    for wx in range(IX + 8, IX + IW - 30, 46):
        d.arc([wx, wy, wx + 30, wy + 14], 180, 360, fill=(150, 200, 235), width=3)
d.rectangle([IX, IY, IX + 218, IY + 30], fill=(16, 34, 72))
d.text((IX + 10, IY + 5), "BENGHAZI PORT, LIBYA", font=font(F_BOLD, 20), fill=WHITE)

TX = IX + IW + 26
TW = LX + LW - TX - 18
y = LY + 52
y = text_block(TX, y, "UKRAINE SEA DRONES SINK RUSSIAN WARSHIP IN LIBYA",
               font(F_BLACK, 43), INK, TW, 1.12)
y += 8
y = text_block(TX, y, "Seven naval drones sank the corvette Merkury in Benghazi port and hit the "
                      "arms cargo ship Angara — 2,400 km from the front line.",
               font(F_REG, 24), (45, 45, 45), TW, 1.22)
assert y <= LY + LH - 8, f"lead overflow: {y} > {LY + LH - 8}"

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

def icon_ai(cx, cy):
    d.ellipse([cx + 4, cy + 2, cx + 48, cy + 46], outline=(88, 60, 180), width=4)
    d.ellipse([cx + 16, cy + 18, cx + 23, cy + 25], fill=(88, 60, 180))
    d.ellipse([cx + 30, cy + 18, cx + 37, cy + 25], fill=(88, 60, 180))
    d.line([cx + 18, cy + 36, cx + 34, cy + 36], fill=(88, 60, 180), width=3)
    d.line([cx + 26, cy + 2, cx + 26, cy - 6], fill=(88, 60, 180), width=3)
    d.ellipse([cx + 22, cy - 12, cx + 30, cy - 4], fill=(88, 60, 180))
    d.line([cx + 10, cy + 50, cx + 42, cy + 50], fill=(88, 60, 180), width=4)

def icon_storm(cx, cy):
    d.ellipse([cx, cy + 4, cx + 34, cy + 30], fill=(110, 125, 145))
    d.ellipse([cx + 16, cy, cx + 54, cy + 32], fill=(110, 125, 145))
    d.rectangle([cx, cy + 20, cx + 54, cy + 32], fill=(110, 125, 145))
    d.polygon([(cx + 28, cy + 30), (cx + 16, cy + 50), (cx + 26, cy + 50), (cx + 20, cy + 62),
               (cx + 38, cy + 42), (cx + 28, cy + 42)], fill=(245, 180, 20))

ROW1_Y, ROW_H, CW, GAP = 492, 232, 474, 20
card(28, ROW1_Y, CW, ROW_H, (24, 110, 74), "CLIMATE  •  ANTALYA, TÜRKIYE",
     "COP31 CLIMATE TALKS COLLAPSE — NO DEAL",
     "After two weeks, the EU and UK rejected a final text that never mentioned fossil fuels — "
     "the first failed COP since 2009.", icon_climate)
card(28 + CW + GAP, ROW1_Y, CW, ROW_H, (198, 84, 20), "ASIA  •  BANTEN, INDONESIA",
     "FACTORY FIRE: 24 DEAD, 30 STILL MISSING",
     "Rescuers search the wreckage of a Milkita candy factory in Cikande after a weekend blaze. "
     "A short circuit is suspected.", icon_factory)

ROW2_Y = 738
card(28, ROW2_Y, CW, ROW_H, (88, 60, 180), "TECHNOLOGY  •  BARBADOS",
     "UN CHIEF: GLOBAL AI RULES WITHIN A YEAR",
     "At the Bridgetown AI Safety Summit, Guterres called AI “the biggest transfer of power "
     "in human history”.", icon_ai)
card(28 + CW + GAP, ROW2_Y, CW, ROW_H, (52, 92, 130), "AMERICAS  •  BRAZIL",
     "SUPERCELL STORM: 5 DEAD, 8,000 HOMES HIT",
     "It tore through Tupanciretã, Rio Grande do Sul, injuring 265 people and forcing "
     "thousands from their homes.", icon_storm)

# ---------------- Ticker ----------------
TY = 974
d.rectangle([0, TY, W, H], fill=(15, 15, 15))
d.text((28, TY + 4), "ALSO TODAY:", font=font(F_BOLD, 19), fill=(245, 197, 90))
d.text((172, TY + 4), "Drones hit Russian cargo ship Sparta II in the Baltic — Finland leads the rescue",
       font=font(F_REG, 19), fill=WHITE)
d.text((172, TY + 25), "UN calls for an independent probe into the strikes on Libyan soil",
       font=font(F_REG, 19), fill=WHITE)

img.save("/home/hatch/workspace/makefun/news-image-20261124/entry.png")
print("saved")
