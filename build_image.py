#!/usr/bin/env python3
"""Build the 17 November 2026 front-page image (1024x1024 PNG) with PIL.

Programmatic drawing: every glyph is rendered from real fonts, so no text
can come out garbled. Stories verified from Reuters/AP/NPR/Military.com
and other reporting dated 17 Nov 2026 (see README.md).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
RED = (178, 28, 28)
NAVY = (28, 48, 84)
GREY = (90, 88, 82)
WHITE = (255, 255, 255)
SKY = (186, 214, 235)
SEA = (64, 110, 150)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def para(text, font, x, y, max_w, leading, color=INK):
    for line in wrap(text, font, max_w):
        d.text((x, y), line, font=font, fill=color)
        y += leading
    return y

def rule(x0, y, x1, w=2, color=INK):
    d.line([(x0, y), (x1, y)], fill=color, width=w)

def kicker(text, x, y, color=RED, size=21):
    d.text((x, y), text, font=F(SANS_B, size), fill=color)

# ---------- masthead ----------
d.text((W // 2, 10), "THE WORLD IN ONE DAY", font=F(SERIF, 54),
       fill=INK, anchor="ma")
d.text((W // 2, 74), "TUESDAY  \u2022  17 NOVEMBER 2026", font=F(SANS_B, 36),
       fill=RED, anchor="ma")
rule(28, 126, 996, 3)

# ---------- hero: Kerch Bridge ----------
HX, HY, HW, HH = 28, 138, 968, 310
d.rectangle([HX, HY, HX + HW, HY + HH], fill=WHITE, outline=INK, width=2)
kicker("UKRAINE WAR  \u2022  LEAD STORY", HX + 20, HY + 16)
d.text((HX + 20, HY + 46), "UKRAINE DROPS THE KERCH BRIDGE",
       font=F(SERIF, 46), fill=INK)
# illustration panel (left, below headline)
PX, PY, PW, PH = HX + 2, HY + 112, 380, HH - 114
for i in range(PH):
    t = i / PH
    r = int(SKY[0] + (SEA[0] - SKY[0]) * t * 0.35)
    g = int(SKY[1] + (SEA[1] - SKY[1]) * t * 0.35)
    b = int(SKY[2] + (SEA[2] - SKY[2]) * t * 0.35)
    d.line([(PX, PY + i), (PX + PW, PY + i)], fill=(r, g, b))
sea_y = PY + 142
d.rectangle([PX, sea_y, PX + PW, PY + PH], fill=SEA)
for wx in range(PX + 8, PX + PW - 8, 40):
    d.arc([wx, sea_y + 10, wx + 30, sea_y + 24], 0, 180, fill=(210, 228, 240), width=2)
    d.arc([wx + 8, sea_y + 30, wx + 38, sea_y + 44], 0, 180, fill=(210, 228, 240), width=2)
deck_y = PY + 108
gap0, gap1 = PX + 158, PX + 222
d.rectangle([PX, deck_y, gap0, deck_y + 11], fill=(52, 52, 52))
d.rectangle([gap1, deck_y, PX + PW, deck_y + 11], fill=(52, 52, 52))
d.polygon([(gap0 + 4, deck_y + 46), (gap1 - 6, deck_y + 46),
           (gap1 - 22, deck_y + 68), (gap0 + 18, deck_y + 68)], fill=(70, 70, 70))
d.line([(gap0 + 4, deck_y + 46), (gap1 - 6, deck_y + 46)], fill=(40, 40, 40), width=3)
d.arc([PX + 24, deck_y - 92, gap0 + 16, deck_y + 6], 180, 360, fill=(52, 52, 52), width=8)
d.arc([gap1 - 16, deck_y - 92, PX + PW - 24, deck_y + 6], 180, 360, fill=(52, 52, 52), width=8)
for px in (PX + 42, PX + 108, PX + 272, PX + 336):
    d.rectangle([px, deck_y + 11, px + 11, sea_y], fill=(70, 70, 70))
for cx, cy, r in ((PX + 190, PY + 34, 17), (PX + 176, PY + 50, 12),
                  (PX + 206, PY + 52, 11), (PX + 192, PY + 20, 11)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(125, 125, 122))
d.rectangle([PX, PY + PH - 28, PX + PW, PY + PH], fill=(20, 20, 20))
d.text((PX + 10, PY + PH - 25), "KERCH BRIDGE, CRIMEA \u2014 ROAD SPAN DOWN",
       font=F(SANS_B, 15), fill=(240, 240, 240))

# hero text (right of panel)
TX = PX + PW + 22
TW = HX + HW - 22 - TX
y = PY + 2
y = para("A Ukrainian strike collapsed the road arch of the 19-km bridge "
         "linking Russia to occupied Crimea. Two killed; rail traffic "
         "resumed on one track.", F(SANS, 23), TX, y, TW, 30)
y += 8
rule(TX, y, HX + HW - 22, 1, GREY)
y += 8
para("Russia hit back, striking Kyiv's two bridges over the Dnipro and "
     "cutting heating to hundreds of buildings.", F(SERIF_REG, 22),
     TX, y, TW, 28)

# ---------- story columns ----------
def column(x, y, w, h, kick, head, body, icon):
    d.rectangle([x, y, x + w, y + h], fill=WHITE, outline=INK, width=2)
    icon(x + 16, y + 14)
    kicker(kick, x + 64, y + 20, size=19)
    yy = y + 50
    yy = para(head, F(SERIF, 26), x + 16, yy, w - 32, 31)
    para(body, F(SANS, 18), x + 16, yy + 6, w - 32, 24)

def icon_plane(x, y):
    d.polygon([(x, y + 14), (x + 34, y + 2), (x + 30, y + 14), (x + 40, y + 22),
               (x + 22, y + 22), (x + 14, y + 30), (x + 8, y + 22)], fill=NAVY)

def icon_drone(x, y):
    d.ellipse([x + 12, y + 10, x + 28, y + 26], fill=NAVY)
    for cx in (x + 4, x + 36):
        d.line([(cx - 8, y + 4), (cx + 8, y + 4)], fill=NAVY, width=3)
        d.line([(cx, y + 4), (cx, y + 12)], fill=NAVY, width=2)

def icon_aid(x, y):
    d.rectangle([x + 4, y + 8, x + 36, y + 30], outline=RED, width=3)
    d.rectangle([x + 17, y + 12, x + 23, y + 26], fill=RED)
    d.rectangle([x + 10, y + 17, x + 30, y + 21], fill=RED)

def icon_chart(x, y):
    for i, hgt in enumerate((10, 18, 26)):
        d.rectangle([x + 4 + i * 12, y + 30 - hgt, x + 12 + i * 12, y + 30], fill=NAVY)
    d.line([(x, y + 30), (x + 40, y + 30)], fill=INK, width=2)

def icon_pin(x, y):
    d.ellipse([x + 8, y + 2, x + 32, y + 26], fill=RED)
    d.polygon([(x + 10, y + 20), (x + 30, y + 20), (x + 20, y + 36)], fill=RED)
    d.ellipse([x + 15, y + 9, x + 25, y + 19], fill=WHITE)

def icon_clap(x, y):
    d.rectangle([x + 4, y + 10, x + 36, y + 30], outline=INK, width=3)
    d.polygon([(x + 4, y + 10), (x + 36, y + 10), (x + 32, y + 2), (x + 8, y + 2)], fill=INK)
    for sx in (14, 24):
        d.line([(x + sx, y + 3), (x + sx + 4, y + 9)], fill=WHITE, width=2)

ROW1_Y, ROW_H, COL_W, GAP = 464, 200, 312, 16
X0, X1, X2 = 28, 28 + COL_W + GAP, 28 + 2 * (COL_W + GAP)
column(X0, ROW1_Y, COL_W, ROW_H, "ASIA",
       "TRUMP LANDS IN MANILA",
       "Opens his Asia trip with a Quad summit; due to meet Xi and Putin in "
       "Shenzhen on Thursday.", icon_plane)
column(X1, ROW1_Y, COL_W, ROW_H, "MIDDLE EAST",
       "IRAN DRONES TARGET U.S. BASE",
       "Drones aimed at a U.S. radar at Sheikh Isa air base in Bahrain were "
       "intercepted; no casualties.", icon_drone)
column(X2, ROW1_Y, COL_W, ROW_H, "ISRAEL & GAZA",
       "WEST PRESSES ISRAEL ON GAZA AID",
       "UK, Australia, Canada and Italy urge crossings opened. Britain "
       "sanctions eight settlement firms.", icon_aid)

ROW2_Y = ROW1_Y + ROW_H + 16
column(X0, ROW2_Y, COL_W, ROW_H, "MARKETS",
       "NVIDIA BEATS AFTER HUANG EXIT",
       "Revenue $115.8bn topped forecasts in its first results since its "
       "founder quit. Dow fell 849.", icon_chart)
column(X1, ROW2_Y, COL_W, ROW_H, "EUROPE",
       "FIVE EU STATES PLAN RWANDA HUB",
       "Austria, Denmark, Germany, Greece, Netherlands: rejected asylum "
       "seekers to a Rwanda hub.", icon_pin)
column(X2, ROW2_Y, COL_W, ROW_H, "CULTURE & SPORT",
       "PATTINSON IS THE NEW 007",
       "Amazon MGM names the 40-year-old as James Bond, directed by Denis "
       "Villeneuve.", icon_clap)

# ---------- bottom strip ----------
BY = ROW2_Y + ROW_H + 16
rule(28, BY, 996, 2)
d.text((28, BY + 10), "ALSO TODAY", font=F(SANS_B, 20), fill=RED)
strip = ("About 1,500 protested Trump's Manila visit  \u2022  Mongolia's president "
         "resigns in graft scandal  \u2022  France strike draws 146,000  \u2022  U.S. "
         "loses measles-elimination status: 5,412 cases  \u2022  Japan scrambles jets "
         "as Russian planes enter its airspace  \u2022  Andreeva, 19, wins the WTA Finals")
para(strip, F(SANS, 19), 28, BY + 38, 968, 25, color=INK)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size, img.mode)
