#!/usr/bin/env python3
"""Generuje assets/banner.svg - naglowek profilu jako ASCII-art ze znaku '@'.

Litery pochodza z figleta (font 'banner3'), kazda komorka '#' zamieniana jest na '@'
ustawiony na siatce o stalym skoku. Kolory sa paleta kamiljan.com.

Uzycie:
    pip install pyfiglet
    python scripts/gen_banner.py > assets/banner.svg

Zmiana napisu lub taglina: podmien WORDS / SUB i przegeneruj plik. Nie edytuj
wspolrzednych x w SVG recznie - jest ich ~250.
"""
import sys

import pyfiglet

WORDS = ("KAMIL", "JAN")
SUB_1 = "AI Automation & Implementation Engineer"
SUB_2 = "Builder & Operator"

NL = chr(10)
FONT = "banner3"
FS = 20          # rozmiar znaku '@'
CW = 13.3        # szerokosc komorki siatki
CH = 21.8        # wysokosc komorki siatki
PADX, PADY = 30, 26
GAP = 14         # odstep miedzy wierszami slow
LETTER_GAP = 2   # odstep miedzy literami, w komorkach

TEAL, TEAL_2, TEAL_3 = "#0891b2", "#22d3ee", "#a8ecf8"
BG, BORDER, TXT_2 = "#06101a", "#ffffff14", "#7fb5c8"


def grid(word):
    """Zwraca (lista 7 wierszy z indeksami kolumn dla '@', szerokosc w kolumnach)."""
    rows = [[] for _ in range(7)]
    x = 0
    for ch in word:
        if ch == " ":
            x += 3
            continue
        art = [l for l in pyfiglet.figlet_format(ch, font=FONT).splitlines() if l.strip()][:7]
        art = (art + [""] * 7)[:7]
        for r in range(7):
            for i, c in enumerate(art[r]):
                if c == "#":
                    rows[r].append(x + i)
        x += max(len(l) for l in art) + LETTER_GAP
    return rows, max(max(r, default=0) for r in rows) + 1


def main():
    blocks = [grid(w) for w in WORDS]
    cols = max(w for _, w in blocks)
    bw = cols * CW
    width = round(bw + PADX * 2)
    band = 7 * CH
    tops = [PADY + i * (band + GAP) for i in range(len(blocks))]
    subtop = tops[-1] + band + 34
    height = round(subtop + 30 + PADY - 10)

    o = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="Kamil Jan - AI Automation and Implementation Engineer, Builder and Operator" '
        f'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">',
        "<title>Kamil Jan</title>",
        f'<defs><linearGradient id="tg" gradientUnits="userSpaceOnUse" x1="0" y1="0" '
        f'x2="{round(width * .8)}" y2="{height}">'
        f'<stop offset="0" stop-color="{TEAL}"/><stop offset=".45" stop-color="{TEAL_2}"/>'
        f'<stop offset=".7" stop-color="{TEAL_3}"/><stop offset="1" stop-color="{TEAL}"/>'
        f'<animateTransform attributeName="gradientTransform" type="translate" '
        f'values="{-width} 0;{width} 0;{-width} 0" dur="9s" repeatCount="indefinite"/>'
        f'</linearGradient><linearGradient id="ru">'
        f'<stop offset="0" stop-color="{TEAL}" stop-opacity="0"/>'
        f'<stop offset=".5" stop-color="{TEAL_2}" stop-opacity=".8"/>'
        f'<stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></linearGradient></defs>',
        f'<rect x=".75" y=".75" width="{width - 1.5}" height="{height - 1.5}" rx="14" '
        f'fill="{BG}" stroke="{BORDER}"/>',
        f'<g font-size="{FS}" font-weight="700" fill="url(#tg)">',
    ]
    for (rows, w), ytop in zip(blocks, tops):
        offx = PADX + (bw - w * CW) / 2
        for r in range(7):
            if not rows[r]:
                continue
            xs = " ".join(f"{offx + xi * CW:.1f}" for xi in rows[r])
            o.append(f'<text x="{xs}" y="{ytop + CH * (r + 1):.1f}">{"@" * len(rows[r])}</text>')
    o.append("</g>")
    o.append(f'<rect x="{PADX}" y="{subtop - 22:.0f}" width="{bw:.0f}" height="1.5" fill="url(#ru)"/>')
    esc = lambda s: s.replace("&", "&amp;")
    o.append(
        f'<g text-anchor="middle">'
        f'<text x="{width // 2}" y="{subtop + 8:.0f}" font-size="23" fill="{TXT_2}" '
        f'letter-spacing="1.5">{esc(SUB_1)}</text>'
        f'<text x="{width // 2}" y="{subtop + 38:.0f}" font-size="23" fill="{TEAL_2}" '
        f'letter-spacing="3" font-weight="700">{esc(SUB_2)}</text></g></svg>'
    )
    sys.stdout.write(NL.join(o) + NL)


if __name__ == "__main__":
    main()
