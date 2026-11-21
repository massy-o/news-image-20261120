#!/usr/bin/env python3
"""Render 10 layout variants of the 20 Nov 2026 news page for comparison.

Reuses the raster engine, stroke font and pictograms from ../main.py.
Every variant is deterministic, stdlib-only, 1024x1024.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import main as M

W, H = M.W, M.H
INK, GRAY, RED, BLUE, GOLD, GREEN, TEAL, PURPLE = M.INK, M.GRAY, M.RED, M.BLUE, M.GOLD, M.GREEN, M.TEAL, M.PURPLE
PAPER, CARD = M.PAPER, M.CARD
fill_rect, fill_circle, fill_poly = M.fill_rect, M.fill_circle, M.fill_poly
line, polyline, star = M.line, M.polyline, M.star
draw_text, draw_paragraph, wrap, text_width = M.draw_text, M.draw_paragraph, M.wrap, M.text_width
ADV = M.ADV

STORIES = [
    ('DIPLOMACY', BLUE, M.picto_summit, ['THREE POWERS', 'ONE TABLE'],
     "US, CHINA AND RUSSIA ISSUE A PEACE DECLARATION IN SHENZHEN. EUROPE WARNS OF A NEW YALTA."),
    ('CONFLICT', RED, M.picto_missile, ['MISSILES HIT', 'POLAND'],
     "MISSILES AND A DRONE COME DOWN IN NATO POLAND AS RUSSIA POUNDS KYIV BRIDGES, KILLING EIGHT."),
    ('JUSTICE', PURPLE, M.picto_court, ['GENOCIDE', 'VERDICT'],
     "THE WORLD COURT RULES MYANMAR'S FORCES COMMITTED GENOCIDE AGAINST THE ROHINGYA."),
    ('MARKETS', RED, lambda cx, cy: M.picto_chart(cx, cy, up=False), ['AI SELLOFF', 'HITS MARKETS'],
     "THE S&P 500 FALLS 3.7 PERCENT INTO CORRECTION; THE NIKKEI DIVES 5.1 PERCENT ON AI FEARS."),
    ('BUSINESS', GREEN, M.picto_ipo, ['RECORD', '$81BN IPO'],
     "ANTHROPIC LISTS AT $1.5 TRILLION IN THE BIGGEST IPO EVER. SHARES LEAP 17 PERCENT ON DEBUT."),
    ('SCIENCE', TEAL, M.picto_mercury, ['MERCURY,', 'AT LAST'],
     "BEPICOLOMBO ENDS AN EIGHT-YEAR JOURNEY TO MERCURY FOR EUROPE AND JAPAN."),
]
BRIEF = [
    'UK AND EU SIGN FOOD, CARBON AND YOUTH DEALS',
    'GTA VI DRAWS RAVE REVIEWS ON RELEASE',
    'COP31 DRAFT DEAL DROPS FOSSIL FUELS',
    'MAGNITUDE 6.7 QUAKE IN CENTRAL PERU',
    'US LOSES MEASLES ELIMINATION STATUS',
    'LA JURY CONVICTS PALISADES FIRE ARSONIST',
    'BAYER $7.25BN ROUNDUP SETTLEMENT APPROVED',
    'ESTONIA MOVES TO CLOSE RUSSIA BORDER POSTS',
]


def panel2(x, y, w, h, kicker, kcolor, picto, head, sub,
           card=CARD, ink=INK, subc=GRAY, border=INK):
    fill_rect(x, y, w, h, card)
    line(x, y, x + w, y, 1.6, border)
    line(x, y + h, x + w, y + h, 1.6, border)
    line(x, y, x, y + h, 1.6, border)
    line(x + w, y, x + w, y + h, 1.6, border)
    pad = 15
    draw_text(kicker, x + pad, y + 12, 3.3, kcolor, sw=2.3)
    line(x + pad, y + 40, x + w - pad, y + 40, 1.3, kcolor)
    if picto:
        picto(x + w / 2, y + 84)
    inner = w - 2 * pad
    longest = max(len(ln) for ln in head)
    unit = min(5.3, inner / (longest * ADV))
    hy = y + (132 if picto else 58)
    for ln in head:
        draw_text(ln, x + pad, hy, unit, ink, sw=unit * 0.68)
        hy += unit * 7.2
    if sub:
        draw_paragraph(sub, x + pad, hy + 7, 2.3, subc, inner, 17.5, sw=1.5)


def masthead(date_text='FRIDAY 20 NOVEMBER 2026', bg=PAPER, ink=INK, sub=GRAY):
    fill_rect(0, 0, W, H, bg)
    line(40, 30, W - 40, 30, 3.2, ink)
    draw_text('THE DAY THE WORLD CHANGED, IN ONE PAGE', W / 2, 44, 3.1, sub, sw=2.0, align='center')
    draw_text('THE WORLD TODAY', W / 2, 74, 12.6, ink, sw=8.6, align='center')
    fill_rect(40, 168, W - 80, 34, RED)
    draw_text(date_text, W / 2, 174, 3.9, (255, 255, 255), sw=2.7, align='center')
    line(40, 216, W - 40, 216, 1.4, ink)
    line(40, 222, W - 40, 222, 3.2, ink)


def ticker(ty=918, dark=INK, fg=(240, 240, 235)):
    fill_rect(40, ty, W - 80, 72, dark)
    draw_text('ALSO TODAY', 58, ty + 8, 3.0, GOLD, sw=2.1)
    draw_text('UK AND EU SIGN FOOD, CARBON AND YOUTH DEALS \u2022 GTA VI DRAWS RAVE REVIEWS', 58, ty + 32, 2.15, fg, sw=1.4)
    draw_text('COP31 DRAFT DROPS FOSSIL FUELS \u2022 6.7 QUAKE IN PERU \u2022 US LOSES MEASLES-FREE STATUS', 58, ty + 53, 2.15, fg, sw=1.4)


# ---------------------------------------------------------------- V01 baseline
def v01():
    M.build()


# ---------------------------------------------------------------- V02 hero conflict
def v02():
    masthead()
    # hero panel: conflict, full width
    x, y, w, h = 40, 240, W - 80, 316
    fill_rect(x, y, w, h, CARD)
    line(x, y, x + w, y, 1.6, INK); line(x, y + h, x + w, y + h, 1.6, INK)
    line(x, y, x, y + h, 1.6, INK); line(x + w, y, x + w, y + h, 1.6, INK)
    draw_text('CONFLICT \u2022 THE LEAD STORY', x + 18, y + 14, 3.6, RED, sw=2.5)
    line(x + 18, y + 46, x + w - 18, y + 46, 1.4, RED)
    M.picto_missile(x + 140, y + 160)
    draw_text('MISSILES HIT', x + 300, y + 76, 8.2, INK, sw=5.7)
    draw_text('POLAND', x + 300, y + 76 + 59, 8.2, INK, sw=5.7)
    draw_paragraph("RUSSIAN MISSILES AND A DRONE COME DOWN IN NATO POLAND AS MOSCOW POUNDS "
                   "KYIV'S BRIDGES, KILLING EIGHT. WARSAW CALLS IT A DELIBERATE PROVOCATION.",
                   x + 300, y + 76 + 128, 2.5, GRAY, w - 330, 19.5, sw=1.6)
    # remaining five: 3 + 2 headline-only panels
    rest = [STORIES[0], STORIES[2], STORIES[4], STORIES[3], STORIES[5]]
    pw, ph, gap = 302, 160, 18
    for i, s in enumerate(rest[:3]):
        panel2(40 + i * (pw + gap), 572, pw, ph, s[0], s[1], None, s[3], None)
    pw2 = (W - 80 - gap) // 2
    for i, s in enumerate(rest[3:]):
        panel2(40 + i * (pw2 + gap), 572 + ph + gap, pw2, 160, s[0], s[1], None, s[3], None)
    ticker(918)


# ---------------------------------------------------------------- V03 dark edition
def v03():
    DK = (16, 18, 24)
    DKCARD = (30, 33, 42)
    WH = (238, 240, 244)
    LG = (168, 174, 186)
    masthead(bg=DK, ink=WH, sub=LG)
    pw, ph, gap, x0, y0 = 302, 324, 18, 40, 240
    for i, s in enumerate(STORIES):
        x = x0 + (i % 3) * (pw + gap)
        y = y0 + (i // 3) * (ph + gap)
        panel2(x, y, pw, ph, s[0], s[1] if s[1] != BLUE else (96, 150, 230), s[2], s[3], s[4],
               card=DKCARD, ink=WH, subc=LG, border=(70, 76, 90))
    ticker(918, dark=(36, 10, 12))


VARIANTS = [('v01', v01), ('v02', v02), ('v03', v03)]


# ---------------------------------------------------------------- V04 financial salmon
def v04():
    SALMON = (255, 241, 224)
    masthead(bg=SALMON)
    pw2 = (W - 80 - 18) // 2
    panel2(40, 240, pw2, 320, STORIES[3][0], STORIES[3][1], STORIES[3][2], STORIES[3][3], STORIES[3][4], card=(255, 253, 247))
    panel2(40 + pw2 + 18, 240, pw2, 320, STORIES[4][0], STORIES[4][1], STORIES[4][2], STORIES[4][3], STORIES[4][4], card=(255, 253, 247))
    rest = [STORIES[0], STORIES[1], STORIES[2], STORIES[5]]
    pw4 = (W - 80 - 3 * 14) // 4
    for i, s in enumerate(rest):
        panel2(40 + i * (pw4 + 14), 576, pw4, 312, s[0], s[1], s[2], s[3], s[4], card=(255, 253, 247))
    ticker(918)


# ---------------------------------------------------------------- V05 dense wire + in brief
def v05():
    fill_rect(0, 0, W, H, PAPER)
    line(40, 26, W - 40, 26, 3.2, INK)
    draw_text('THE WORLD TODAY', W / 2, 40, 10.5, INK, sw=7.2, align='center')
    fill_rect(40, 138, W - 80, 32, RED)
    draw_text('FRIDAY 20 NOVEMBER 2026 \u2022 THE WHOLE DAY ON ONE PAGE', W / 2, 144, 3.6, (255, 255, 255), sw=2.5, align='center')
    line(40, 184, W - 40, 184, 3.2, INK)
    # left: six story rows
    y = 200
    for s in STORIES:
        fill_rect(40, y, 600, 112, CARD)
        line(40, y, 640, y, 1.4, INK); line(40, y + 112, 640, y + 112, 1.4, INK)
        line(40, y, 40, y + 112, 1.4, INK); line(640, y, 640, y + 112, 1.4, INK)
        fill_rect(40, y, 8, 112, s[1])
        draw_text(s[0], 62, y + 10, 2.9, s[1], sw=2.0)
        head = ' '.join(s[3])
        hu = min(4.6, 560 / (len(head) * ADV)) if len(head) * ADV * 4.6 > 560 else 4.6
        lines = wrap(head, hu, 560)
        hy = y + 34
        for ln in lines[:2]:
            draw_text(ln, 62, hy, hu, INK, sw=hu * 0.66)
            hy += hu * 7.0
        draw_paragraph(s[4], 62, hy + 2, 2.05, GRAY, 560, 15.5, sw=1.35)
        y += 118
    # right column: in brief + numbers
    rx, rw = 656, 328
    fill_rect(rx, 200, rw, 436, INK)
    draw_text('IN BRIEF', rx + 16, 214, 3.6, GOLD, sw=2.5)
    by = 252
    for item in BRIEF:
        fill_rect(rx + 16, by + 5, 6, 6, GOLD)
        draw_paragraph(item, rx + 32, by, 2.2, (240, 240, 235), rw - 48, 16.5, sw=1.45)
        by += 48
    ny = 652
    fill_rect(rx, ny, rw, 250, CARD)
    line(rx, ny, rx + rw, ny, 1.4, INK); line(rx, ny + 250, rx + rw, ny + 250, 1.4, INK)
    line(rx, ny, rx, ny + 250, 1.4, INK); line(rx + rw, ny, rx + rw, ny + 250, 1.4, INK)
    draw_text('THE DAY IN NUMBERS', rx + 16, ny + 12, 3.0, INK, sw=2.1)
    nums = [('-3.7%', 'S&P 500 FALLS', RED), ('$81BN', 'ANTHROPIC IPO', GREEN),
            ('6.7', 'PERU QUAKE', TEAL), ('8 YRS', 'TO MERCURY', PURPLE)]
    yy = ny + 48
    for big, small, col in nums:
        draw_text(big, rx + 16, yy, 4.6, col, sw=3.2)
        draw_text(small, rx + rw - 14, yy + 14, 1.9, GRAY, sw=1.3, align='right')
        yy += 50


# ---------------------------------------------------------------- V06 pictogram forward
def v06():
    masthead()
    FACTS = ['SHENZHEN, CHINA', 'NATO AIRSPACE BREACH', 'THE HAGUE RULING',
             'S&P 500 -3.7%', '$1.5 TRILLION VALUE', '8-YEAR JOURNEY ENDS']
    pw, ph, gap, x0, y0 = 302, 324, 18, 40, 240
    for i, s in enumerate(STORIES):
        x = x0 + (i % 3) * (pw + gap)
        y = y0 + (i // 3) * (ph + gap)
        fill_rect(x, y, pw, ph, CARD)
        line(x, y, x + pw, y, 1.6, INK); line(x, y + ph, x + pw, y + ph, 1.6, INK)
        line(x, y, x, y + ph, 1.6, INK); line(x + pw, y, x + pw, y + ph, 1.6, INK)
        draw_text(s[0], x + 15, y + 12, 3.3, s[1], sw=2.3)
        draw_text('0%d' % (i + 1), x + pw - 15, y + 10, 3.6, s[1], sw=2.4, align='right')
        line(x + 15, y + 40, x + pw - 15, y + 40, 1.3, s[1])
        s[2](x + pw / 2, y + 108)
        hy = y + 176
        inner = pw - 30
        longest = max(len(ln) for ln in s[3])
        unit = min(5.6, inner / (longest * ADV))
        for ln in s[3]:
            draw_text(ln, x + 15, hy, unit, INK, sw=unit * 0.68)
            hy += unit * 7.2
        draw_text(FACTS[i], x + 15, hy + 12, 2.6, s[1], sw=1.8)
    ticker(918)


# ---------------------------------------------------------------- V07 globe hero
def globe(cx, cy, r):
    fill_circle(cx, cy, r, (198, 222, 240))
    land = (110, 168, 110)
    blobs = [(-0.45, -0.35, 0.30), (-0.30, 0.25, 0.20), (0.05, -0.55, 0.22),
             (0.18, -0.05, 0.30), (0.45, 0.30, 0.18), (0.62, -0.42, 0.13),
             (-0.62, 0.02, 0.14), (0.30, 0.55, 0.12)]
    for bx, by, br in blobs:
        for k in range(5):
            fill_circle(cx + (bx + 0.07 * math.cos(k * 2.4)) * r, cy + (by + 0.07 * math.sin(k * 2.4)) * r, br * r * 0.62, land)
    for frac in (0.35, 0.7, 1.0):
        for k in range(72):
            a = k * math.pi / 36
            ex, ey = cx + r * frac * math.sin(a), cy - r * math.cos(a)
            if (ex - cx) ** 2 + (ey - cy) ** 2 <= (r - 2) ** 2:
                fill_circle(ex, ey, 1.4, (120, 160, 200))
        for k in range(72):
            a = k * math.pi / 36
            ex, ey = cx - r * frac * math.sin(a), cy - r * math.cos(a)
            if (ex - cx) ** 2 + (ey - cy) ** 2 <= (r - 2) ** 2:
                fill_circle(ex, ey, 1.4, (120, 160, 200))
    for frac in (-0.5, 0.0, 0.5):
        for k in range(72):
            a = k * math.pi / 36
            ex, ey = cx + r * math.cos(a), cy + frac * r + 0.28 * r * math.sin(a) * (1 if frac == 0 else 0.4)
            if (ex - cx) ** 2 + (ey - cy) ** 2 <= (r - 2) ** 2:
                fill_circle(ex, ey, 1.4, (120, 160, 200))
    for k in range(90):
        a = k * math.pi / 45
        fill_circle(cx + r * math.cos(a), cy + r * math.sin(a), 2.2, TEAL)


def v07():
    fill_rect(0, 0, W, H, PAPER)
    line(40, 26, W - 40, 26, 3.2, INK)
    draw_text('THE WORLD TODAY', W / 2, 40, 10.5, INK, sw=7.2, align='center')
    fill_rect(40, 138, W - 80, 32, RED)
    draw_text('FRIDAY 20 NOVEMBER 2026', W / 2, 144, 3.6, (255, 255, 255), sw=2.5, align='center')
    line(40, 184, W - 40, 184, 3.2, INK)
    globe(512, 420, 148)
    # callouts
    draw_text('MISSILES HIT', 64, 268, 4.0, RED, sw=2.8)
    draw_text('POLAND', 64, 268 + 30, 4.0, RED, sw=2.8)
    line(210, 300, 400, 360, 2.0, RED)
    draw_text('THREE POWERS', 700, 268, 4.0, BLUE, sw=2.8)
    draw_text('ONE TABLE', 700, 268 + 30, 4.0, BLUE, sw=2.8)
    line(700, 306, 610, 356, 2.0, BLUE)
    draw_text('GENOCIDE', 64, 500, 4.0, PURPLE, sw=2.8)
    draw_text('VERDICT', 64, 500 + 30, 4.0, PURPLE, sw=2.8)
    line(216, 522, 396, 470, 2.0, PURPLE)
    draw_text('MERCURY,', 716, 500, 4.0, TEAL, sw=2.8)
    draw_text('AT LAST', 716, 500 + 30, 4.0, TEAL, sw=2.8)
    line(716, 522, 624, 472, 2.0, TEAL)
    pw2 = (W - 80 - 18) // 2
    panel2(40, 640, pw2, 208, STORIES[3][0], STORIES[3][1], None, STORIES[3][3], STORIES[3][4])
    panel2(40 + pw2 + 18, 640, pw2, 208, STORIES[4][0], STORIES[4][1], None, STORIES[4][3], STORIES[4][4])
    ticker(872)


VARIANTS += [('v04', v04), ('v05', v05), ('v06', v06), ('v07', v07)]


# ---------------------------------------------------------------- V08 magazine cover
def v08():
    SPACE = (13, 15, 28)
    fill_rect(0, 0, W, H, SPACE)
    for i in range(90):
        sx = (i * 173) % 1024
        sy = (i * 389) % 560
        fill_circle(sx, sy, 1.6 if i % 3 else 2.4, (210, 216, 235))
    draw_text('THE WORLD TODAY', W / 2, 36, 11.5, (245, 246, 250), sw=7.8, align='center')
    fill_rect(40, 128, W - 80, 32, RED)
    draw_text('FRIDAY 20 NOVEMBER 2026 \u2022 SPECIAL EDITION', W / 2, 134, 3.6, (255, 255, 255), sw=2.5, align='center')
    # cover image: Mercury arrival
    cx, cy, r = 512, 330, 104
    fill_circle(cx, cy, r, (198, 128, 84))
    fill_circle(cx - 38, cy - 30, 20, (172, 104, 64))
    fill_circle(cx + 22, cy + 42, 15, (172, 104, 64))
    fill_circle(cx - 6, cy - 66, 12, (172, 104, 64))
    fill_circle(cx + 48, cy - 18, 11, (172, 104, 64))
    fill_circle(cx - 62, cy + 34, 9, (172, 104, 64))
    for k in range(110):
        a = k * math.pi / 55
        fill_circle(cx + 158 * math.cos(a), cy + 44 * math.sin(a), 1.8, TEAL)
    sx, sy = cx + 150, cy - 74
    fill_rect(sx - 9, sy - 9, 19, 18, (160, 166, 178))
    fill_rect(sx - 34, sy - 6, 22, 12, BLUE)
    fill_rect(sx + 13, sy - 6, 22, 12, BLUE)
    draw_text('MERCURY, AT LAST', W / 2, 452, 6.4, (245, 246, 250), sw=4.4, align='center')
    draw_text('BEPICOLOMBO ENDS AN EIGHT-YEAR JOURNEY FOR EUROPE AND JAPAN', W / 2, 500, 2.5, (178, 184, 200), sw=1.7, align='center')
    # cover lines
    rows = [STORIES[1], STORIES[0], STORIES[2], STORIES[3], STORIES[4]]
    y = 556
    for s in rows:
        line(40, y, W - 40, y, 1.2, (70, 76, 96))
        draw_text(s[0], 40, y + 12, 2.8, s[1] if s[1] != BLUE else (96, 150, 230), sw=1.9)
        head = ' '.join(s[3])
        draw_text(head, 40, y + 34, 4.3, (245, 246, 250), sw=3.0)
        y += 66
    line(40, y, W - 40, y, 1.2, (70, 76, 96))
    draw_text('ALSO TODAY: UK-EU DEALS \u2022 GTA VI RAVES \u2022 COP31 FOSSIL ROW \u2022 PERU QUAKE \u2022 US MEASLES STATUS LOST',
              W / 2, y + 14, 2.05, GOLD, sw=1.4, align='center')


# ---------------------------------------------------------------- V09 swiss poster
def v09():
    fill_rect(0, 0, W, H, (252, 252, 250))
    draw_text('THE WORLD TODAY \u2022 DAILY NEWS POSTER', 40, 28, 3.0, INK, sw=2.0)
    fill_rect(40, 62, W - 80, 118, RED)
    draw_text('20 NOV 2026', 64, 82, 13.5, (255, 255, 255), sw=9.0)
    draw_text('FRIDAY', W - 64, 96, 6.0, (255, 255, 255), sw=4.0, align='right')
    draw_text('SIX STORIES THAT MATTER', W - 64, 140, 2.6, (255, 220, 220), sw=1.8, align='right')
    FACTS = ['US, CHINA AND RUSSIA SIGN A PEACE DECLARATION IN SHENZHEN',
             'RUSSIAN MISSILES AND A DRONE COME DOWN IN NATO POLAND',
             "WORLD COURT: MYANMAR'S FORCES COMMITTED GENOCIDE",
             'S&P 500 -3.7% INTO CORRECTION; NIKKEI DIVES 5.1%',
             'ANTHROPIC LISTS AT $1.5 TRILLION, +17% ON DEBUT',
             'BEPICOLOMBO REACHES MERCURY AFTER EIGHT YEARS']
    pw, ph, gap = (W - 80 - 18) // 2, 216, 18
    for i, s in enumerate(STORIES):
        x = 40 + (i % 2) * (pw + gap)
        y = 212 + (i // 2) * (ph + 16)
        draw_text('0%d' % (i + 1), x, y, 6.4, RED, sw=4.4)
        draw_text(s[0], x + 86, y + 8, 3.0, s[1], sw=2.1)
        line(x + 86, y + 34, x + pw, y + 34, 1.3, s[1])
        hy = y + 52
        inner = pw - 86
        longest = max(len(ln) for ln in s[3])
        unit = min(5.4, inner / (longest * ADV))
        for ln in s[3]:
            draw_text(ln, x + 86, hy, unit, INK, sw=unit * 0.68)
            hy += unit * 7.2
        draw_paragraph(FACTS[i], x + 86, hy + 8, 2.15, GRAY, inner, 16, sw=1.4)
        line(x, y + ph - 6, x + pw, y + ph - 6, 1.0, (200, 200, 198))
    fy = 212 + 3 * ph + 2 * 16 + 14
    fill_rect(40, fy, W - 80, 56, INK)
    draw_text('ALSO TODAY: UK-EU DEALS \u2022 GTA VI RAVES \u2022 COP31 FOSSIL ROW \u2022 PERU QUAKE 6.7 \u2022 US LOSES MEASLES-FREE STATUS',
              W / 2, fy + 18, 2.1, (240, 240, 235), sw=1.4, align='center')


# ---------------------------------------------------------------- V10 split feature
def v10():
    masthead()
    # left feature: diplomacy
    x, y, w, h = 40, 240, 460, 648
    fill_rect(x, y, w, h, CARD)
    line(x, y, x + w, y, 1.6, INK); line(x, y + h, x + w, y + h, 1.6, INK)
    line(x, y, x, y + h, 1.6, INK); line(x + w, y, x + w, y + h, 1.6, INK)
    draw_text('DIPLOMACY \u2022 THE FEATURE', x + 18, y + 14, 3.4, BLUE, sw=2.4)
    line(x + 18, y + 46, x + w - 18, y + 46, 1.4, BLUE)
    M.picto_summit(x + w / 2, y + 116)
    draw_text('THREE POWERS', x + 18, y + 176, 6.9, INK, sw=4.8)
    draw_text('ONE TABLE', x + 18, y + 176 + 50, 6.9, INK, sw=4.8)
    draw_paragraph("THE LEADERS OF THE UNITED STATES, CHINA AND RUSSIA MEET IN SHENZHEN AND "
                   "ISSUE A JOINT PEACE DECLARATION, THE FIRST THREE-WAY SUMMIT OF ITS KIND.",
                   x + 18, y + 292, 2.5, GRAY, w - 36, 19.5, sw=1.65)
    fill_rect(x + 18, y + 386, w - 36, 64, (232, 238, 248))
    draw_text('EUROPE WARNS OF', x + 34, y + 398, 3.4, BLUE, sw=2.4)
    draw_text('A NEW YALTA', x + 34, y + 398 + 26, 3.4, BLUE, sw=2.4)
    draw_text('ALSO TODAY', x + 18, y + 478, 2.9, GOLD, sw=2.0)
    by = y + 508
    for item in BRIEF[:4]:
        fill_rect(x + 18, by + 4, 6, 6, GOLD)
        draw_paragraph(item, x + 34, by, 2.15, GRAY, w - 52, 16, sw=1.4)
        by += 34
    # right: five compact rows
    rx, rw = 518, 466
    ry = 240
    for s in STORIES[1:]:
        fill_rect(rx, ry, rw, 124, CARD)
        line(rx, ry, rx + rw, ry, 1.5, INK); line(rx, ry + 124, rx + rw, ry + 124, 1.5, INK)
        line(rx, ry, rx, ry + 124, 1.5, INK); line(rx + rw, ry, rx + rw, ry + 124, 1.5, INK)
        fill_rect(rx, ry, 8, 124, s[1])
        draw_text(s[0], rx + 20, ry + 10, 2.8, s[1], sw=1.95)
        head = ' '.join(s[3])
        hu = min(4.1, (rw - 40) / (len(head) * ADV))
        draw_text(head, rx + 20, ry + 34, hu, INK, sw=hu * 0.67)
        draw_paragraph(s[4], rx + 20, ry + 72, 2.0, GRAY, rw - 40, 15, sw=1.3)
        ry += 131


VARIANTS += [('v08', v08), ('v09', v09), ('v10', v10)]


def render(name, fn):
    fn()
    px = M.downscale()
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name + '.png')
    n = M.write_png(path, px)
    print(name, n, 'bytes')


if __name__ == '__main__':
    for name, fn in VARIANTS:
        render(name, fn)
