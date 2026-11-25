#!/usr/bin/env python3
"""Draw the 25 November 2026 world-news infographic (1024x1024 PNG).

PIL only; run locally:  python3 draw.py
Writes entry.png next to this file. Deterministic bytes.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
REG = FONT_DIR + "DejaVuSans.ttf"

# Palette
NAVY = (13, 24, 43)        # page background
PANEL = (26, 42, 68)       # story panel
PANEL2 = (31, 50, 80)      # lead panel, slightly lighter
GOLD = (232, 184, 75)      # accent
WHITE = (245, 247, 250)
BODY = (201, 212, 227)     # light grey-blue body text
MUTED = (148, 163, 184)    # footer grey
RED = (224, 82, 82)
GREEN = (86, 196, 120)
BLUE = (96, 165, 250)
TEAL = (94, 200, 190)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rounded_panel(draw, box, fill, outline=None, radius=14):
    draw.rounded_rectangle(box, radius=radius, fill=fill,
                           outline=outline, width=2 if outline else 1)


def draw_ship(draw, x, y, s):
    """Simple container ship icon, s = scale (width ~ 170*s)."""
    # hull
    draw.polygon([(x, y + 58 * s), (x + 170 * s, y + 58 * s),
                  (x + 150 * s, y + 86 * s), (x + 20 * s, y + 86 * s)],
                 fill=(70, 110, 160))
    # containers
    cols = [(224, 82, 82), (232, 184, 75), (86, 196, 120), (96, 165, 250)]
    for i, c in enumerate(cols):
        cx = x + 12 * s + i * 38 * s
        draw.rectangle([cx, y + 26 * s, cx + 34 * s, y + 54 * s],
                       fill=c, outline=(13, 24, 43), width=2)
    # bridge
    draw.rectangle([x + 148 * s, y + 8 * s, x + 166 * s, y + 54 * s],
                   fill=(245, 247, 250))
    # mast
    draw.line([(x + 157 * s, y + 8 * s), (x + 157 * s, y - 8 * s)],
              fill=(245, 247, 250), width=3)
    # water lines
    for i in range(3):
        draw.line([(x + 6 * s, y + (96 + i * 9) * s),
                   (x + 164 * s, y + (96 + i * 9) * s)],
                  fill=(94, 200, 190), width=2)


def draw_down_arrow(draw, x, y, s):
    pts = [(x, y + 6 * s), (x + 16 * s, y + 22 * s), (x + 30 * s, y + 10 * s),
           (x + 46 * s, y + 30 * s), (x + 62 * s, y + 16 * s)]
    draw.line(pts, fill=RED, width=5, joint="curve")
    draw.polygon([(x + 62 * s, y + 16 * s), (x + 48 * s, y + 14 * s),
                  (x + 60 * s, y + 30 * s)], fill=RED)


def draw_up_arrow(draw, x, y, s):
    pts = [(x, y + 56 * s), (x + 16 * s, y + 40 * s), (x + 30 * s, y + 50 * s),
           (x + 46 * s, y + 28 * s), (x + 62 * s, y + 40 * s)]
    draw.line(pts, fill=GREEN, width=5, joint="curve")
    draw.polygon([(x + 62 * s, y + 40 * s), (x + 48 * s, y + 42 * s),
                  (x + 60 * s, y + 24 * s)], fill=GREEN)


def draw_bars(draw, x, y, s):
    heights = [18, 30, 44]
    for i, h in enumerate(heights):
        bx = x + i * 22 * s
        draw.rectangle([bx, y + (48 - h) * s, bx + 14 * s, y + 48 * s],
                       fill=BLUE)
    draw.line([(x, y + 48 * s), (x + 62 * s, y + 48 * s)],
              fill=WHITE, width=2)


def draw_asteroid(draw, x, y, s):
    # big Didymos with craters + small Dimorphos casting a shadow
    draw.ellipse([x, y + 10 * s, x + 56 * s, y + 66 * s], fill=(150, 152, 158))
    draw.ellipse([x + 12 * s, y + 22 * s, x + 24 * s, y + 34 * s], fill=(120, 122, 128))
    draw.ellipse([x + 32 * s, y + 40 * s, x + 44 * s, y + 52 * s], fill=(120, 122, 128))
    draw.ellipse([x + 44 * s, y - 6 * s, x + 62 * s, y + 12 * s], fill=(110, 112, 118))
    draw.ellipse([x + 30 * s, y + 30 * s, x + 52 * s, y + 48 * s],
                 fill=(60, 62, 68))  # shadow of the moonlet


def draw_barrel(draw, x, y, s):
    draw.rounded_rectangle([x, y, x + 64 * s, y + 84 * s], radius=8 * s,
                           fill=(120, 84, 40), outline=(232, 184, 75), width=3)
    draw.line([(x, y + 24 * s), (x + 64 * s, y + 24 * s)], fill=(232, 184, 75), width=3)
    draw.line([(x, y + 60 * s), (x + 64 * s, y + 60 * s)], fill=(232, 184, 75), width=3)
    draw.text((x + 14 * s, y + 32 * s), "OIL", font=font(BOLD, int(20 * s)),
              fill=(245, 247, 250))
    # droplet
    draw.ellipse([x + 78 * s, y + 34 * s, x + 96 * s, y + 52 * s], fill=TEAL)
    draw.polygon([(x + 78 * s, y + 36 * s), (x + 96 * s, y + 36 * s),
                  (x + 87 * s, y + 18 * s)], fill=TEAL)


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # ---------- header ----------
    d.text((36, 26), "T H E   W O R L D   I N   O N E   D A Y",
           font=font(BOLD, 26), fill=GOLD)
    d.text((36, 58), "25 NOVEMBER 2026", font=font(BOLD, 68), fill=WHITE)
    d.text((36, 128), "WEDNESDAY  \u2022  SIX STORIES THAT DEFINED THE DAY",
           font=font(REG, 22), fill=BODY)
    # small globe motif, top right
    gx, gy, gr = 920, 78, 46
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=GOLD, width=3)
    d.ellipse([gx - gr // 2, gy - gr, gx + gr // 2, gy + gr], outline=GOLD, width=2)
    d.line([(gx - gr, gy), (gx + gr, gy)], fill=GOLD, width=2)
    d.line([(gx - gr + 12, gy - 30), (gx + gr - 12, gy + 30)], fill=GOLD, width=2)
    d.line([(gx, 150), (988, 150)], fill=GOLD, width=3)

    # ---------- lead story: tariffs ----------
    ly0, ly1 = 168, 372
    rounded_panel(d, [36, ly0, 988, ly1], PANEL2, outline=GOLD)
    d.text((268, ly0 + 16), "TRADE  \u2022  LEAD STORY", font=font(BOLD, 22), fill=GOLD)
    head = "US to unveil tariffs on 16 partners"
    body = ("Washington is poised to release findings of its excess-capacity "
            "probe, with new duties on China, the EU, Japan and 13 others. "
            "China faces a 20% cap; the EU, Japan and South Korea 15%.")
    y = text_block(d, 268, ly0 + 48, wrap(d, head, font(BOLD, 36), 700),
                   font(BOLD, 36), WHITE, 44)
    text_block(d, 268, y + 8, wrap(d, body, font(REG, 22), 700),
               font(REG, 22), BODY, 30)
    draw_ship(d, 66, ly0 + 52, 1.0)

    # ---------- 2x2 grid ----------
    grid = [
        ("MARKETS", RED, draw_down_arrow,
         "Asian stocks tumble on tariff threats",
         "Asia-Pacific shares fell 2.3%. Seoul slid 5.3%, Taiwan 5.1% and "
         "the Nikkei 2.9%."),
        ("US ECONOMY", BLUE, draw_bars,
         "US inflation data due as Fed weighs hike",
         "October PCE and Q3 GDP land today, with a December hike "
         "near-certain."),
        ("AUSTRALIA", GREEN, draw_up_arrow,
         "Australia inflation runs hotter than forecast",
         "October CPI rose 4.9%, beating forecasts and lifting the Aussie "
         "dollar."),
        ("SPACE", (150, 152, 158), draw_asteroid,
         "ESA unveils first close-ups of Dimorphos",
         "Hera shares its first close-up images of the asteroid DART "
         "struck in 2022."),
    ]
    gx0, gx1 = 36, 500
    gy0, gy1 = 388, 572
    gy2, gy3 = 580, 764
    boxes = [(gx0, gy0, gx1, gy1), (524, gy0, 988, gy1),
             (gx0, gy2, gx1, gy3), (524, gy2, 988, gy3)]
    for (tag, color, icon, head, body), box in zip(grid, boxes):
        x0, y0, x1, y1 = box
        rounded_panel(d, box, PANEL)
        d.rectangle([x0, y0 + 14, x0 + 6, y1 - 14], fill=color)
        icon(d, x1 - 78, y0 + 16, 0.9)
        d.text((x0 + 22, y0 + 16), tag, font=font(BOLD, 20), fill=color)
        y = text_block(d, x0 + 22, y0 + 52,
                       wrap(d, head, font(BOLD, 26), x1 - x0 - 108),
                       font(BOLD, 26), WHITE, 32)
        text_block(d, x0 + 22, y + 6,
                   wrap(d, body, font(REG, 19), x1 - x0 - 44),
                   font(REG, 19), BODY, 26)

    # ---------- bottom story: oil ----------
    by0, by1 = 780, 944
    rounded_panel(d, [36, by0, 988, by1], PANEL2)
    d.text((268, by0 + 16), "ENERGY", font=font(BOLD, 22), fill=TEAL)
    head = "Oil falls as glut fears offset Mideast tension"
    body = ("Brent crude slipped to $90.97 a barrel as rising supply and a "
            "surplus outlook outweighed Strait of Hormuz disruption fears.")
    y = text_block(d, 268, by0 + 48, wrap(d, head, font(BOLD, 28), 700),
                   font(BOLD, 28), WHITE, 38)
    text_block(d, 268, y + 8, wrap(d, body, font(REG, 21), 700),
               font(REG, 21), BODY, 29)
    draw_barrel(d, 92, by0 + 42, 1.0)

    # ---------- footer ----------
    d.text((512, 962),
           "Sources: Reuters \u2022 ESA \u2022 BusinessWorld  \u2014  All events first reported 25 November 2026",
           font=font(REG, 18), fill=MUTED, anchor="ma")

    img.save(OUT, "PNG", optimize=True)


if __name__ == "__main__":
    main()
    print("wrote", OUT)
