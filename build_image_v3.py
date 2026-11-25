#!/usr/bin/env python3
"""News Image v3 — 'The World in One Page', Tuesday 24 November 2026.

Built from the round-2 board teardown: the top-10 entries all (a) carry
30+ stories, (b) date-check ruthlessly — only stories that happened or were
first reported ON Tuesday 24 Nov (UTC) — with an explicit DATE CHECK box
excluding other days' news, (c) use a giant serif date masthead, a region
bar, a big-numbers strip, certainty/source tags, and a world map.

v1/v2 failed (a) and (b): 7 stories, several from 21-23 Nov. v3 fixes both.
Facts verified 25 Nov 2026 against AP/Reuters/WSJ/AFP/CNA/Yonhap coverage
of Tuesday 24 Nov 2026.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 242, 227)
INK = (22, 34, 54)
NAVY = (20, 38, 76)
RED = (176, 48, 38)
TEAL = (24, 105, 88)
GOLD = (176, 116, 20)
GREY = (105, 100, 88)
CARD = (255, 253, 246)
LINE = (196, 188, 164)

F_BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
F_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
F_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def tw(text, font):
    return d.textlength(text, font=font)

def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(t, font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def block(x, y, text, font, maxw, leading, color=INK, max_lines=None):
    lines = wrap(text, font, maxw)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        d.text((x, y), ln, font=font, fill=color)
        y += leading
    return y

def badge(x, y, n, color=NAVY, r=11):
    d.ellipse([x, y, x + 2 * r, y + 2 * r], fill=color)
    f = F(F_BLACK, 12)
    s = str(n)
    d.text((x + r - tw(s, f) / 2, y + r - 8), s, font=f, fill=(255, 255, 255))

# ---------------------------------------------------------------- top strip
f = F(F_BOLD, 13)
d.text((16, 10), "THE WORLD IN ONE PAGE", font=f, fill=INK)
r = "30 STORIES · 7 REGIONS · EVERY ONE FROM TUESDAY 24 NOV 2026 (UTC)"
d.text((W - 16 - tw(r, f), 10), r, font=f, fill=INK)
d.line([16, 32, W - 16, 32], fill=INK, width=2)

# ---------------------------------------------------------------- masthead
f = F(F_SERIF, 57)
t = "Tuesday 24 November 2026"
d.text(((W - tw(t, f)) / 2, 40), t, font=f, fill=INK)
d.line([16, 106, W - 16, 106], fill=RED, width=3)
f = F(F_BOLD, 14.5)
t = "Russia says it downed 699 drones   •   Baghdad takes the Kurdish oilfields   •   Sanofi seals a $41bn deal"
d.text(((W - tw(t, f)) / 2, 112), t, font=f, fill=(120, 32, 24))

# ---------------------------------------------------------------- numbers strip
nums = [
    ("699", "UKRAINIAN DRONES\nRUSSIA SAYS IT DOWNED"),
    ("$41BN", "SANOFI BUYS INSMED,\nYEAR'S BIGGEST DEAL"),
    ("6,500+", "ROHINGYA MALAYSIA\nWILL SEND BACK"),
    ("+8.99%", "TAIEX RECORD DAY\nAS CHIP STOCKS LEAP"),
    ("47,000", "WOMEN KILLED BY KIN\nOR PARTNERS IN 2025"),
    ("350K", "EU CAP, A YEAR, ON\nCHINESE HYBRID CARS"),
]
x = 16
cw = (W - 32) / 6
for i, (big, lab) in enumerate(nums):
    cx = x + i * cw
    fb = F(F_BLACK, 27)
    d.text((cx + (cw - tw(big, fb)) / 2, 136), big, font=fb, fill=NAVY)
    fl = F(F_BOLD, 9.5)
    yy = 170
    for ln in lab.split("\n"):
        d.text((cx + (cw - tw(ln, fl)) / 2, yy), ln, font=fl, fill=GREY)
        yy += 12
    if i:
        d.line([cx, 140, cx, 190], fill=LINE, width=1)
d.line([16, 196, W - 16, 196], fill=INK, width=2)

# ---------------------------------------------------------------- region bar
regions = [("EUROPE 5", (58, 92, 140)), ("ASIA 10", (24, 105, 88)),
           ("MIDDLE EAST 3", (176, 116, 20)), ("AMERICAS 3", (176, 48, 38)),
           ("OCEANIA 2", (110, 70, 130)), ("AFRICA 1", (140, 100, 40)),
           ("WORLD 6", (80, 80, 80))]
total = 30
x = 16
counts = [5, 10, 3, 3, 2, 1, 6]
for (lab, col), c in zip(regions, counts):
    wseg = (W - 32) * c / total
    d.rectangle([x, 202, x + wseg - 2, 224], fill=col)
    fl = F(F_BOLD, 11)
    if wseg > 62:
        d.text((x + (wseg - tw(lab, fl)) / 2, 207), lab, font=fl, fill=(255, 255, 255))
    x += wseg

# ---------------------------------------------------------------- lead cards
leads = [
    dict(n=1, tag="EUROPE · WAR", color=RED, ill="drones",
         head="Drone war: 699 downed in one night",
         body="Russia says it downed 699 Ukrainian drones overnight, 355 bound for Moscow. A Zaporizhzhia strike kills 2, wounds 40.",
         src="REPORTED — Russian MoD · Kyiv"),
    dict(n=2, tag="ASIA · MARKETS", color=TEAL, ill="chart",
         head="Chip stocks leap: Taiex +8.99%, a record",
         body="Tuesday's Asian close as the Huang rally echoes east: Taiex +8.99% (record points gain), Kospi +6.32%, Nikkei +3.91%.",
         src="CONFIRMED — CNA · Yonhap · Nikkei"),
    dict(n=3, tag="ASIA · REFUGEES", color=GOLD, ill="ship",
         head="Malaysia to send 6,500 Rohingya back",
         body="Anwar tells parliament 6,500+ Rohingya return to Myanmar in December — 1,500 by ship, 5,303 by air — days after the ICJ ruling.",
         src="OFFICIAL — PM Anwar · AFP"),
]
LX, LY, LW, LH, GAP = 16, 232, 325, 238, 9
for i, L in enumerate(leads):
    x = LX + i * (LW + GAP)
    d.rectangle([x, LY, x + LW, LY + LH], fill=CARD, outline=LINE, width=1)
    d.rectangle([x, LY, x + LW, LY + 26], fill=L["color"])
    ft = F(F_BOLD, 12.5)
    d.text((x + 10, LY + 6), L["tag"], font=ft, fill=(255, 255, 255))
    badge(x + LW - 28, LY + 2, L["n"], color=(255, 255, 255))
    # badge number needs dark text on white circle: redraw
    d.ellipse([x + LW - 28, LY + 2, x + LW - 6, LY + 24], fill=(255, 255, 255))
    fb = F(F_BLACK, 12)
    s = str(L["n"])
    d.text((x + LW - 17 - tw(s, fb) / 2, LY + 6), s, font=fb, fill=L["color"])
    iy = LY + 34
    if L["ill"] == "drones":
        d.rectangle([x + 8, iy, x + LW - 8, iy + 82], fill=(214, 226, 238))
        for k in range(7):
            dx = x + 30 + k * 40
            dy = iy + 14 + (k % 3) * 20
            d.line([dx - 9, dy, dx + 9, dy], fill=INK, width=3)
            d.line([dx, dy - 5, dx, dy + 5], fill=INK, width=3)
        d.rectangle([x + 8, iy + 62, x + LW - 8, iy + 82], fill=(168, 60, 44))
        fl = F(F_BLACK, 13)
        d.text((x + 16, iy + 66), "699 DRONES DOWNED", font=fl, fill=(255, 255, 255))
    elif L["ill"] == "chart":
        d.rectangle([x + 8, iy, x + LW - 8, iy + 82], fill=(216, 236, 224))
        pts = [(x + 24, iy + 66), (x + 90, iy + 58), (x + 150, iy + 62),
               (x + 210, iy + 38), (x + 268, iy + 26), (x + 296, iy + 12)]
        d.line(pts, fill=TEAL, width=4)
        for px, py in pts:
            d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=TEAL)
        fl = F(F_BLACK, 13)
        d.text((x + 16, iy + 6), "TAIEX 40,122 · +8.99%", font=fl, fill=TEAL)
    else:
        d.rectangle([x + 8, iy, x + LW - 8, iy + 82], fill=(222, 232, 240))
        d.polygon([(x + 60, iy + 58), (x + 200, iy + 58), (x + 182, iy + 72), (x + 78, iy + 72)], fill=INK)
        d.rectangle([x + 96, iy + 44, x + 164, iy + 58], fill=INK)
        d.line([x + 130, iy + 44, x + 130, iy + 30], fill=INK, width=3)
        for k in range(4):
            d.line([x + 30 + k * 62, iy + 76, x + 52 + k * 62, iy + 76], fill=(90, 130, 170), width=2)
        fl = F(F_BLACK, 13)
        d.text((x + 16, iy + 6), "1,500 BY SHIP · 5,303 BY AIR", font=fl, fill=NAVY)
    fh = F(F_BLACK, 19)
    yy = block(x + 10, iy + 90, L["head"], fh, LW - 20, 23, max_lines=2)
    fbd = F(F_REG, 12)
    yy = block(x + 10, yy + 2, L["body"], fbd, LW - 20, 15.5, max_lines=3)
    fs = F(F_BOLD, 10)
    d.text((x + 10, LY + LH - 17), L["src"], font=fs, fill=GREY)

# ---------------------------------------------------------------- mid cards
cards = [
    dict(n=4, tag="MIDDLE EAST · OIL", color=GOLD,
         head="Baghdad seizes Kurdish-held oilfields",
         body="PM al-Zaidi puts the Kirkuk, Diyala, Salahuddin and Nineveh fields and crossings under federal control."),
    dict(n=5, tag="HORMUZ · SHIPPING", color=RED,
         head="Iran: tankers hit its mines",
         body="The IRGC says 2–3 tankers caught fire breaking its strait rules; oil flows fall 40%. A claim, not confirmed."),
    dict(n=6, tag="EUROPE · WAR", color=RED,
         head="Russian drone enters Poland",
         body="A drone crosses into Polish airspace in the night barrage; NATO sends an AWACS as Warsaw holds fire."),
    dict(n=7, tag="GAZA · WAR", color=RED,
         head="Strike kills Hamas security chief",
         body="An Israeli strike kills Naeem Abu Nahel and six others; doctors in Khan Younis warn of meningitis."),
    dict(n=8, tag="BRUSSELS · TRADE", color=NAVY,
         head="EU caps Chinese hybrid cars",
         body="Import quotas adopted: 350,000 Chinese hybrid cars a year for the EU, from 1 December."),
    dict(n=9, tag="ASIA · DISASTER", color=GOLD,
         head="Hanoi restaurant blast kills six",
         body="A gas explosion levels a hot-pot eatery in the Dong Da district at lunch; about 10 are injured."),
    dict(n=10, tag="DHAKA · POLITICS", color=TEAL,
         head="Hasina says she will fly home 16 Dec",
         body="The ousted PM names her return date; Dhaka says she can come back only by extradition."),
    dict(n=11, tag="OCEANIA · SECURITY", color=(110, 70, 130),
         head="Solomons ends China security pact",
         body="PM Wale arrives in Canberra to sign an Australia treaty; the 2022 China pact will not be renewed."),
    dict(n=12, tag="AMERICAS · JUSTICE", color=RED,
         head="Mexico to try 'El Chapo Isidro' at home",
         body="Mexico turns down the US extradition request for the captured cartel boss, held after a US drone tip."),
]
MX, MY, MW, MH = 16, 480, 325, 88
for idx, C in enumerate(cards):
    cx = MX + (idx % 3) * (MW + GAP)
    cy = MY + (idx // 3) * (MH + 8)
    d.rectangle([cx, cy, cx + MW, cy + MH], fill=CARD, outline=LINE, width=1)
    d.rectangle([cx, cy, cx + MW, cy + 4], fill=C["color"])
    badge(cx + 8, cy + 10, C["n"], color=C["color"], r=10)
    ft = F(F_BOLD, 10.5)
    d.text((cx + 34, cy + 11), C["tag"], font=ft, fill=C["color"])
    fh = F(F_BLACK, 14.5)
    yy = block(cx + 10, cy + 28, C["head"], fh, MW - 20, 17, max_lines=1)
    fb = F(F_REG, 11)
    block(cx + 10, cy + 50, C["body"], fb, MW - 20, 13.5, max_lines=2)

# ---------------------------------------------------------------- bottom: map + also list
BY = 772
d.rectangle([16, BY, 492, 946], fill=CARD, outline=LINE, width=1)
fh = F(F_BLACK, 13)
d.text((26, BY + 8), "WHERE IT HAPPENED", font=fh, fill=INK)
fs = F(F_REG, 10)
d.text((196, BY + 11), "pins carry the story numbers", font=fs, fill=GREY)

MAP = [
    "                                                                        ",
    "        #####                                                           ",
    "      #########        #     ####################################       ",
    "     ###########     #####  ######################################      ",
    "      ##########      ##    ################  ##################        ",
    "       ########              ##############    ################         ",
    "        ######    ##          ############      ##############          ",
    "         ####   ######         #########         ############           ",
    "          ##  ########          #######           ##########            ",
    "               ########          #####             ########             ",
    "                ######            ###     ##        ######   #          ",
    "                #####            ####    ####        ####   ###         ",
    "                 ###              ##      ##          ##     #          ",
    "                 ##                                                     ",
    "                 #                         ##                           ",
    "                                            ##      ########            ",
    "                                             #     ##########           ",
    "                                                    ########            ",
]
MX0, MY0, CELL = 26, BY + 34, 6.4
for ri, row in enumerate(MAP):
    for ci, ch in enumerate(row):
        if ch == "#":
            cx = MX0 + ci * CELL
            cyy = MY0 + ri * CELL
            d.ellipse([cx, cyy, cx + 3.4, cyy + 3.4], fill=(178, 168, 138))
PINS = {1: (40, 5), 2: (58, 9), 3: (54, 13), 4: (42, 8), 5: (45, 9),
        6: (37, 4), 7: (40, 8), 8: (34, 5), 9: (55, 10), 10: (52, 9),
        11: (66, 15), 12: (13, 9)}
for n, (ci, ri) in PINS.items():
    cx = MX0 + ci * CELL
    cyy = MY0 + ri * CELL
    d.ellipse([cx - 6, cyy - 6, cx + 8, cyy + 8], fill=RED)
    fb = F(F_BLACK, 8)
    s = str(n)
    d.text((cx + 1 - tw(s, fb) / 2, cyy - 3.5), s, font=fb, fill=(255, 255, 255))

AX = 508
d.rectangle([AX, BY, W - 16, 946], fill=CARD, outline=LINE, width=1)
fh = F(F_BLACK, 13)
d.text((AX + 10, BY + 8), "ALSO ON TUESDAY — 18 MORE STORIES", font=fh, fill=INK)
also = [
    "NATO vows space defence, 'Sputnik-S'",
    "Russian jets enter Korea's air zone",
    "China: death sentence for spy official",
    "Pakistan astronaut on Shenzhou-24",
    "Senegal restored as AFCON champions",
    "Colombia car bomb hurts 23",
    "Landmine casualties 6,929, a record",
    "Australia: 5%-of-revenue tech fines",
    "Nepal M5.3 quake — no deaths",
    "60 Patriots await US sign-off",
    "Chess title match opens in Geneva",
    "Shanghai party chief faces probe",
    "England: record 5,258 heat deaths",
    "Sooryavanshi, 15, hits 204 off 53",
    "Portugal budget: 2,864 amendments",
    "US consumer confidence up to 103.3",
    "Brazil fiscal bill passes 353–128",
    "Brent crude slips near $88.70",
]
colw = (W - 16 - AX - 30) / 2
fb = F(F_REG, 10)
fn = F(F_BLACK, 10)
for i, s in enumerate(also):
    cx = AX + 10 + (i // 9) * (colw + 10)
    cy = BY + 32 + (i % 9) * 15.5
    num = f"{13 + i}"
    d.text((cx, cy), num, font=fn, fill=RED)
    block(cx + 20, cy, s, fb, colw - 22, 12, max_lines=1)

# ---------------------------------------------------------------- date check + footer
d.rectangle([16, 954, W - 16, 988], outline=RED, width=2)
fd = F(F_BOLD, 10.5)
d.text((24, 960), "DATE CHECK", font=fd, fill=RED)
txt = ("Left out as other days' news: Nvidia rehires Huang and Wall Street's rally (Mon 23 Nov) · Ukraine's Libya ship strike (22–23 Nov) · "
       "COP31 talks collapse (Sun 22 Nov) · Democrats' 258 US House seats (22 Nov) · the Banten factory fire itself (Sat 21 Nov — only Tuesday's toll update is counted).")
block(104, 960, txt, F(F_REG, 10.5), W - 130, 13, max_lines=2)
ff = F(F_REG, 9.5)
t = "Every story here happened, or was first reported, on Tuesday 24 November 2026 (UTC), as the named outlets reported it. Maps and drawings are original vector art."
d.text(((W - tw(t, ff)) / 2, 996), t, font=ff, fill=GREY)

img.save("/home/hatch/workspace/makefun/news-image-20261124/entry-v3-draft.png")
img.resize((300, 300), Image.LANCZOS).save("/home/hatch/workspace/makefun/news-image-20261124/entry-v3-draft-300px.png")
print("saved v3 draft")
