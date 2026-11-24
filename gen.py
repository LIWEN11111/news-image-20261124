#!/usr/bin/env python3
"""Generate entry.png for news-image-20261124: a newspaper front page
summing up 24 Nov 2026 world news. Built in this session with PIL + DejaVu.
Stories verified from live news search on 2026-11-24 (Japan Times / TOI / SCMP / Manila Times):
1. Ukraine sinks Russian warship off Libya; 2. Nvidia rehires Jensen Huang after Trump push;
3. Suspected North Korean aircraft breaches South Korea airspace, jets scrambled;
4. Allies say Russia may launch nuclear space weapon next month, NATO vows space defence;
5. 2031 Women's World Cup to be hosted by USA, Mexico, Costa Rica, Jamaica (UK 2035);
6. UN food agency warns wars jeopardise food aid for 7.3 million more people.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1024, 1024
img = Image.new("RGB", (W, H), (253, 253, 248))
d = ImageDraw.Draw(img)

def font(size, bold=False):
    p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p, size)

def wrap(text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

def panel(x, y, w, h, bg, headline, sub, size=30, subsize=19, fg=(20, 20, 20)):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=bg, outline=(180, 180, 170), width=2)
    lines = wrap(headline, font(size, True), w - 28)
    ty = y + 14
    for ln in lines:
        d.text((x + 14, ty), ln, font=font(size, True), fill=fg)
        ty += size + 6
    if sub:
        for ln in wrap(sub, font(subsize), w - 28):
            d.text((x + 14, ty + 4), ln, font=font(subsize), fill=(60, 60, 60))
            ty += subsize + 4
    return ty

# Masthead
d.rectangle([0, 0, W, 118], fill=(12, 12, 12))
d.text((28, 18), "WORLD NEWS", font=font(64, True), fill=(255, 255, 255))
d.text((700, 38), "24 NOV 2026", font=font(40, True), fill=(255, 200, 40))
d.rectangle([0, 118, W, 152], fill=(178, 20, 20))
d.text((28, 124), "TUESDAY, 24 NOVEMBER 2026  •  THE DAY IN SIX STORIES", font=font(22, True), fill=(255, 255, 255))

# --- Main story: warship (draw sea + ship) ---
x, y, w, h = 24, 168, 620, 300
d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=(18, 52, 86), outline=(180, 180, 170), width=2)
# sea waves
for i, yy in enumerate(range(y + 210, y + h - 10, 22)):
    d.arc([x + 10 + (i % 2) * 20, yy, x + 90 + (i % 2) * 20, yy + 28], 0, 180, fill=(120, 180, 230), width=4)
# ship silhouette (lower, clear of the subline)
d.polygon([(x + 90, y + 215), (x + 530, y + 215), (x + 480, y + 252), (x + 140, y + 252)], fill=(30, 30, 30))
d.rectangle([x + 200, y + 175, x + 380, y + 215], fill=(30, 30, 30))
d.rectangle([x + 260, y + 145, x + 290, y + 175], fill=(30, 30, 30))
d.polygon([(x + 290, y + 145), (x + 290, y + 170), (x + 325, y + 170)], fill=(200, 40, 40))
# explosion at the bow, clear of text
for (ex, ey, r, c) in [(x + 545, y + 195, 22, (255, 170, 0)), (x + 525, y + 178, 15, (255, 90, 0)), (x + 560, y + 178, 12, (255, 220, 80))]:
    d.ellipse([ex - r, ey - r, ex + r, ey + r], fill=c)
d.text((x + 16, y + 12), "UKRAINE SINKS RUSSIAN", font=font(36, True), fill=(255, 255, 255))
d.text((x + 16, y + 52), "WARSHIP OFF LIBYA", font=font(36, True), fill=(255, 255, 255))
d.text((x + 16, y + 96), "Kyiv's reach spreads beyond Europe", font=font(20), fill=(200, 220, 240))

# --- Nvidia ---
x, y, w, h = 668, 168, 332, 300
d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=(16, 120, 60), outline=(180, 180, 170), width=2)
# chip
d.rounded_rectangle([x + 96, y + 150, x + 236, y + 250], radius=8, fill=(10, 40, 20), outline=(120, 255, 170), width=3)
d.text((x + 126, y + 182), "NVDA", font=font(34, True), fill=(120, 255, 170))
for i in range(5):
    d.line([x + 110 + i * 28, y + 150, x + 110 + i * 28, y + 132], fill=(120, 255, 170), width=4)
    d.line([x + 110 + i * 28, y + 250, x + 110 + i * 28, y + 268], fill=(120, 255, 170), width=4)
d.text((x + 14, y + 12), "NVIDIA REHIRES", font=font(30, True), fill=(255, 255, 255))
d.text((x + 14, y + 48), "JENSEN HUANG", font=font(30, True), fill=(255, 255, 255))
d.text((x + 14, y + 92), "CEO returns after a push", font=font(19), fill=(210, 240, 220))
d.text((x + 14, y + 118), "from Trump", font=font(19), fill=(210, 240, 220))

# --- Korea airspace ---
x, y, w, h = 24, 492, 488, 220
d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=(150, 200, 235), outline=(180, 180, 170), width=2)
# jets (larger, lower)
for jx, jy in [(70, 640), (280, 660)]:
    d.polygon([(jx, jy), (jx + 110, jy + 14), (jx, jy + 28)], fill=(40, 40, 40))
    d.polygon([(jx + 35, jy + 5), (jx + 65, jy - 18), (jx + 74, jy + 9)], fill=(40, 40, 40))
    d.polygon([(jx + 35, jy + 23), (jx + 65, jy + 44), (jx + 74, jy + 19)], fill=(40, 40, 40))
d.text((x + 14, y + 12), "NORTH KOREA JET BREACHES", font=font(28, True), fill=(10, 30, 50))
d.text((x + 14, y + 48), "SOUTH KOREA AIRSPACE", font=font(28, True), fill=(10, 30, 50))
d.text((x + 14, y + 92), "Jets scrambled; island residents", font=font(19), fill=(30, 50, 70))
d.text((x + 14, y + 118), "told to take shelter", font=font(19), fill=(30, 50, 70))

# --- Space weapon ---
x, y, w, h = 536, 492, 464, 220
d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=(8, 8, 28), outline=(180, 180, 170), width=2)
# earth + satellite (satellite body with solar panels, earth as a circle)
d.ellipse([x + 320, y + 110, x + 440, y + 210], fill=(40, 90, 180))
d.ellipse([x + 350, y + 135, x + 400, y + 180], fill=(60, 160, 90))
d.rectangle([x + 70, y + 145, x + 150, y + 185], fill=(200, 200, 210), outline=(255, 255, 255), width=2)
d.rectangle([x + 10, y + 155, x + 70, y + 175], fill=(40, 80, 200))
d.rectangle([x + 150, y + 155, x + 210, y + 175], fill=(40, 80, 200))
for sx, sy in [(260, 540), (330, 520), (420, 545), (480, 520)]:
    d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 255, 255))
d.text((x + 14, y + 12), "RUSSIA MAY LAUNCH", font=font(28, True), fill=(255, 255, 255))
d.text((x + 14, y + 48), "NUCLEAR SPACE WEAPON", font=font(28, True), fill=(255, 200, 40))
d.text((x + 14, y + 92), "Allies warn of launch next month;", font=font(19), fill=(210, 210, 230))
d.text((x + 14, y + 118), "NATO vows space defence", font=font(19), fill=(210, 210, 230))

# --- World Cup ---
x, y, w, h = 24, 736, 488, 220
d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=(20, 110, 50), outline=(180, 180, 170), width=2)
# ball
d.ellipse([x + 340, y + 120, x + 440, y + 200], fill=(255, 255, 255), outline=(20, 20, 20), width=3)
d.polygon([(x + 385, y + 140), (x + 405, y + 155), (x + 395, y + 180), (x + 372, y + 170), (x + 372, y + 150)], fill=(20, 20, 20))
d.text((x + 14, y + 12), "2031 WOMEN'S WORLD CUP", font=font(28, True), fill=(255, 255, 255))
d.text((x + 14, y + 48), "USA, MEXICO, COSTA RICA", font=font(28, True), fill=(255, 255, 255))
d.text((x + 14, y + 84), "& JAMAICA TO HOST", font=font(28, True), fill=(255, 255, 255))
d.text((x + 14, y + 128), "UK gets the 2035 edition", font=font(19), fill=(210, 240, 220))

# --- Food aid ---
x, y, w, h = 536, 736, 464, 220
d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=(250, 225, 140), outline=(180, 180, 170), width=2)
# wheat stalks
for wx in [380, 410, 440]:
    d.line([x + wx, y + 210, x + wx, y + 130], fill=(160, 110, 20), width=4)
    for k in range(4):
        d.ellipse([x + wx - 12, y + 130 + k * 18, x + wx + 12, y + 148 + k * 18], fill=(200, 140, 30))
d.text((x + 14, y + 12), "UN: WARS PUT FOOD AID", font=font(28, True), fill=(40, 30, 10))
d.text((x + 14, y + 48), "FOR 7.3 MILLION MORE", font=font(28, True), fill=(40, 30, 10))
d.text((x + 14, y + 84), "AT RISK", font=font(28, True), fill=(40, 30, 10))
d.text((x + 14, y + 128), "Food agency warns of deepening", font=font(19), fill=(80, 60, 20))
d.text((x + 14, y + 154), "hunger as conflicts spread", font=font(19), fill=(80, 60, 20))

# Footer
d.text((28, 978), "All stories first reported on 24 November 2026  •  Sources: Japan Times, Times of India, SCMP, Manila Times", font=font(16), fill=(90, 90, 90))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, "PNG", optimize=True)
print(out, os.path.getsize(out), img.size)
