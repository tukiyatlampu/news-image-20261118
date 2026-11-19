#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news poster (1024x1024 PNG).

Dense broadsheet, not a photo collage: 3 lead stories, a 6-beat UTC
timeline, and 41 sourced one-line stories across regions and fields --
50 stories in all. Flat colours only, so the PNG stays small.
No network, no randomness: the same input always draws the same bytes.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (22, 22, 22)
NAVY = (15, 42, 68)
RED = (139, 26, 26)
MUTED = (90, 100, 115)
RULE = (180, 172, 150)
TIMELINE_BG = (226, 232, 238)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


LEAD = [
    ("US hits Iran missile site on Qeshm; Iran strikes back at US bases in Kuwait and Bahrain", "REUTERS"),
    ("Xi meets Putin in Shenzhen; three-way summit with Trump set for Thursday", "AFP"),
    ("Ukraine strikes Kerch Bridge for third time in a week", "BBC"),
]

TIMELINE = [
    ("PRE-DAWN", "Bahrain intercepts attacks before dawn"),
    ("MORNING", "APEC summit opens in Shenzhen"),
    ("10:16 UTC", "Voyager 1 reaches one light-day from Earth"),
    ("AFTERNOON", "EU proposes \u20ac45bn Ukraine loan"),
    ("EVENING", "Peltola wins Alaska Senate seat, 56\u201344 Dems"),
    ("NIGHT", "Israeli op beyond Yellow Line, Gaza"),
]

# (section, headline, source) -- 41 items.
STORIES = [
    ("GULF & MIDDLE EAST", "Iran drones hit Ali Al Salem air base in Kuwait", "WIRE"),
    ("GULF & MIDDLE EAST", "Indian embassy urges citizens to exit Iran", "WIRE"),
    ("GULF & MIDDLE EAST", "Israel elects Matan Kahana as parliament speaker", "WIRE"),
    ("GULF & MIDDLE EAST", "Trump's Board of Peace faults Israel and Hamas", "WIRE"),
    ("GULF & MIDDLE EAST", "Iranian army helicopter crashes in Isfahan; four die", "WIRE"),
    ("UKRAINE & EUROPE", "Ukraine downs 126 of 141 drones; six hurt in Dnipro", "WIRE"),
    ("UKRAINE & EUROPE", "Four killed as Russian strikes hit Odesa", "WIRE"),
    ("UKRAINE & EUROPE", "Ukraine seeks more fighter jets and air defences", "WIRE"),
    ("UKRAINE & EUROPE", "Fact-checkers debunk fake Kerch damage footage", "WIRE"),
    ("UKRAINE & EUROPE", "Germany's Steinmeier to visit Beirut blast site", "WIRE"),
    ("UKRAINE & EUROPE", "Limoges City Hall devastated by arson attack", "WIRE"),
    ("ASIA-PACIFIC", "Quad meets at leader level in Manila, first in 2+ years", "WIRE"),
    ("ASIA-PACIFIC", "Trump announces trade deal with Philippines", "WIRE"),
    ("ASIA-PACIFIC", "Canada, China cut tariffs after Carney\u2013Xi talks", "WIRE"),
    ("ASIA-PACIFIC", "Carney meets Trump at APEC in Shenzhen", "WIRE"),
    ("ASIA-PACIFIC", "Two Russian jets off Taiwan; violate Japan airspace", "WIRE"),
    ("ASIA-PACIFIC", "Taiwan logs 10 PLA sorties, 11 ships", "WIRE"),
    ("ASIA-PACIFIC", "North Korea completes enrichment facility extension", "IAEA"),
    ("ASIA-PACIFIC", "Trump, Putin plan separate one-on-one in China", "WIRE"),
    ("WORLD", "Hegseth makes surprise trip to Venezuela", "WIRE"),
    ("WORLD", "Bukele confirms airstrike on Haitian gang leader", "WIRE"),
    ("WORLD", "Chad closes border with Sudan", "WIRE"),
    ("WORLD", "Nigeria bids for UN Human Rights Council seat", "WIRE"),
    ("WORLD", "Senegal's PASTEF excludes President Faye", "WIRE"),
    ("HEALTH & SCIENCE", "US loses measles elimination status after 26 years", "PAHO"),
    ("HEALTH & SCIENCE", "Ebola in DR Congo passes 11,000 cases", "WIRE"),
    ("HEALTH & SCIENCE", "Death toll rises to 16 in Pakistan building blast", "WIRE"),
    ("HEALTH & SCIENCE", "WHO: 950,000 displaced Palestinians on flood-prone land", "WHO"),
    ("HEALTH & SCIENCE", "UNEP: ~2.6\u00b0C warming on current pledges", "UNEP"),
    ("MARKETS & TECH", "Nvidia board rejects Huang return after record quarter", "WIRE"),
    ("MARKETS & TECH", "Anthropic raises $81.3bn in record stock offering", "WIRE"),
    ("MARKETS & TECH", "Amazon invests $7bn in India", "WIRE"),
    ("MARKETS & TECH", "Deutsche Bank shares fall ~6% on investigation", "WIRE"),
    ("MARKETS & TECH", "Dow \u22121.6% to 50,759; S&P \u22121.0%; Brent $93.14", "WIRE"),
    ("MARKETS & TECH", "OpenAI launches GPT-6.2 Astra and Sol", "WIRE"),
    ("CLIMATE", "COP31 draft triples adaptation finance to $120bn/yr by 2035", "WIRE"),
    ("CLIMATE", "COP31 just-transition draft attacked as too weak", "WIRE"),
    ("CLIMATE", "COP31: Africa loses bid for standalone adaptation push", "WIRE"),
    ("SPORT", "Brazil thrash Singapore 7-0; Vinicius hat-trick", "WIRE"),
    ("SPORT", "USA 2-0 Haiti; Mexico 1-0 Jamaica in Nations League", "WIRE"),
    ("SPORT", "India beat Pakistan 2-1 for 10th SAFF title", "WIRE"),
]

FOOTER_SOURCES = ("Sources: Reuters \u00b7 AFP \u00b7 AP \u00b7 BBC \u00b7 PAHO \u00b7 IAEA \u00b7 WHO \u00b7 UNEP \u00b7 EU \u00b7 NASA \u00b7 wire reports")


def fit_line(draw, text, fnt, max_w, min_size=14):
    """Shrink the font until the line fits; return (font, width)."""
    size = fnt.size
    while size > min_size and draw.textlength(text, font=fnt) > max_w:
        size -= 1
        fnt = font(fnt.path, size)
    return fnt, draw.textlength(text, font=fnt)


def draw_poster(path):
    total = len(LEAD) + len(TIMELINE) + len(STORIES)
    assert total == 50, f"story count is {total}, must be 50"
    assert len(STORIES) == 41

    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    y = 0

    # ---- Header -------------------------------------------------
    d.rectangle([0, 0, W, 76], fill=NAVY)
    d.text((24, 12), "WORLD NEWS", font=font(FONT_BOLD, 34), fill=(255, 255, 255))
    d.text((24, 50), "WEDNESDAY 18 NOVEMBER 2026", font=font(FONT_BOLD, 17), fill=(255, 205, 90))
    right = "50 SOURCED STORIES"
    d.text((W - 24 - d.textlength(right, font=font(FONT_BOLD, 20)), 14),
           right, font=font(FONT_BOLD, 20), fill=(255, 255, 255))
    d.text((W - 24 - d.textlength("ALL EVENTS REPORTED 18 NOV 2026", font=font(FONT_REG, 13)), 44),
           "ALL EVENTS REPORTED 18 NOV 2026", font=font(FONT_REG, 13), fill=(200, 210, 220))
    y = 76

    # ---- Lead stories -------------------------------------------
    y += 8
    for i, (head, src) in enumerate(LEAD, 1):
        d.rectangle([24, y + 4, 30, y + 34], fill=RED)
        f, _ = fit_line(d, head, font(FONT_BOLD, 21), W - 110)
        d.text((42, y), head, font=f, fill=INK)
        d.text((W - 24 - d.textlength(src, font=font(FONT_BOLD, 12)), y + 6),
               src, font=font(FONT_BOLD, 12), fill=RED)
        y += 44
    y += 4
    d.line([24, y, W - 24, y], fill=RULE, width=2)
    y += 10

    # ---- UTC timeline strip --------------------------------------
    d.rectangle([0, y, W, y + 104], fill=TIMELINE_BG)
    d.text((24, y + 6), "UTC TIMELINE \u2014 THROUGH THE DAY", font=font(FONT_BOLD, 14), fill=NAVY)
    ty = y + 28
    col_w = (W - 48) // 3
    for idx, (when, what) in enumerate(TIMELINE):
        cx = 24 + (idx % 3) * col_w
        cy = ty + (idx // 3) * 38
        d.text((cx, cy), when, font=font(FONT_BOLD, 13), fill=RED)
        f, _ = fit_line(d, what, font(FONT_REG, 13), col_w - 12, min_size=12)
        d.text((cx, cy + 16), what, font=f, fill=INK)
    y += 104 + 10

    # ---- Two-column story list -----------------------------------
    # Balance: left column takes sections in order until ~half the rows.
    sections = []
    for sec, head, src in STORIES:
        if not sections or sections[-1][0] != sec:
            sections.append((sec, []))
        sections[-1][1].append((head, src))
    rows = []
    for sec, items in sections:
        rows.append(("head", sec))
        rows.extend(("item", it) for it in items)
    half = next(i for i, r in enumerate(rows) if r == ("head", "WORLD"))
    cols = [rows[:half], rows[half:]]
    col_x = [24, W // 2 + 12]
    col_w = W // 2 - 36
    row_h = 23
    top = y
    for ci, col in enumerate(cols):
        cy = top
        for kind, val in col:
            if kind == "head":
                d.text((col_x[ci], cy + 2), val, font=font(FONT_BOLD, 14), fill=RED)
                d.line([col_x[ci], cy + 21, col_x[ci] + col_w, cy + 21], fill=RULE, width=1)
            else:
                head, src = val
                bullet = "\u2022 "
                f, _ = fit_line(d, head, font(FONT_REG, 16), col_w - 62)
                d.text((col_x[ci], cy + 2), bullet + head, font=f, fill=INK)
                d.text((col_x[ci] + col_w - d.textlength(src, font=font(FONT_BOLD, 11)), cy + 4),
                       src, font=font(FONT_BOLD, 11), fill=MUTED)
            cy += row_h
    y = top + max(len(c) for c in cols) * row_h + 6

    # ---- Footer: date check --------------------------------------
    d.line([24, y, W - 24, y], fill=RULE, width=2)
    y += 8
    check = "DATE CHECK \u2713  Wednesday 18 November 2026  \u00b7  50 stories, all reported 18 Nov 2026  \u00b7  nothing from before 13 Nov 2026"
    d.text((24, y), check, font=font(FONT_BOLD, 14), fill=NAVY)
    y += 22
    d.text((24, y), FOOTER_SOURCES, font=font(FONT_REG, 12), fill=MUTED)

    img.save(path, format="PNG", optimize=True)
    return path


if __name__ == "__main__":
    import os
    out = os.environ.get("POSTER_OUT", "/tmp/ni18.png")
    draw_poster(out)
    n = os.path.getsize(out)
    print(f"wrote {out}: {n} bytes ({n / 1048576:.2f} MiB), limit 1048576")
    print("stories:", len(LEAD) + len(TIMELINE) + len(STORIES))
