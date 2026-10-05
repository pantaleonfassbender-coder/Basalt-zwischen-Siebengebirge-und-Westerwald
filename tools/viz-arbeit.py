"""Zeichnet assets/viz/arbeit.svg: oben 3817 Beschäftigte und 1567 volle Arbeitsjahre in den 75 Basaltbrüchen
des Reviers Brühl–Unkel 1894 nach Heusler (1897), als Punktfeld (ein Punkt = zehn Menschen), mit der
Lohnrechnung des Apparats; unten die belegten Ereignisse 1880–1900 auf einer Zeitachse. Jede Beschriftung
verweist auf die Stelle. Aufruf aus dem Wurzelverzeichnis: python tools/viz-arbeit.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "arbeit.svg"
T = "#/text/arbeit/"
W, H = 900, 620
MENSCHEN, VOLL, LOHN = 3817, 1567, 1161332


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def t(x, y, text, size=12.5, anchor="start", colour="ink", style=""):
    return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" fill="var(--{colour})"{style}>{escape(text)}</text>'


EREIGNISSE = [  # Jahr, Zeile 1, Zeile 2, Verweis, Farbe, Ebene (+ oben, - unten), Ausrichtung
    (1880, "3 Tote in Basaltbrüchen", "verschüttet, erschlagen", "unfaelle/1", "arbeit", -1, "start"),
    (1883, "Verein der Basalt-Industriellen", "Fleischkonserven, Verbandkästen", "fuersorge/1", "bruch", 2, "middle"),
    (1884, "Ein Arbeiter und ein Junge", "verschüttet; Anklage gegen den Aufseher", "unfaelle/2", "arbeit", -2, "start"),
    (1885, "Sprengen ohne Bergaufsicht", "nach Dietrich", "unfaelle/3", "staat", 1, "start"),
    (1894, "3817 Beschäftigte", "in 75 Brüchen", "zahlen/1", "arbeit", -1, "middle"),
    (1897, "Löhne „nicht unerheblich gestiegen“", "Handelskammer Bonn", "zahlen/2", "bruch", 1, "end"),
    (1898, "„fremde Arbeiter“", "im Linzer Revier Italiener", "zahlen/3", "arbeit", -2, "middle"),
    (1900, "Klagen im Linzer Revier", "Vorträge über Gewerkschaften", "fremde/1", "arbeit", 2, "end"),
]


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ar-t ar-d" font-family="var(--serif)">',
         '<title id="ar-t">3817 Menschen, 1567 Arbeitsjahre</title>',
         '<desc id="ar-d">Oben ein Punktfeld: 382 Punkte, je einer für zehn Menschen, die 1894 in den 75 Basaltbrüchen des Reviers Brühl–Unkel beschäftigt waren, zusammen 3817. Davon sind 157 Punkte gefüllt: so viele volle Arbeitsjahre zu 300 Tagen leisteten sie zusammen, 1567. Daneben die Rechnung: 1 161 332 Mark Löhne, also rund 304 Mark je Beschäftigten im Jahr und rund 741 Mark je volles Arbeitsjahr, knapp zweieinhalb Mark am Tag. Unten eine Zeitachse von 1880 bis 1900 mit den belegten Ereignissen: 1880 drei Tote in Basaltbrüchen; 1883 der Verein der rheinischen Basalt-Industriellen; 1884 ein Arbeiter und ein Junge verschüttet, Anklage gegen den Aufseher; 1885 Sprengen ohne Bergaufsicht; 1894 die Zahlen; 1897 gestiegene Löhne; 1898 fremde Arbeiter, im Linzer Revier Italiener seit Herbst; 1900 Klagen im Linzer Revier und Vorträge über Gewerkschaften.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">3817 Menschen, 1567 Arbeitsjahre</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Die Basaltbrüche des Reviers Brühl–Unkel 1894, nach Heusler (1897). Ein Punkt = zehn Menschen.</text>']
    # Punktfeld
    n, voll = round(MENSCHEN / 10), round(VOLL / 10)
    cols, r, step, x0, y0 = 32, 4.2, 11, 40, 82
    for i in range(n):
        cx, cy = x0 + (i % cols) * step, y0 + (i // cols) * step
        if i < voll:
            o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="var(--arbeit)"/>')
        else:
            o.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 0.6}" fill="none" stroke="var(--arbeit)" stroke-width="1.1" opacity="0.7"/>')
    rows = (n + cols - 1) // cols
    yb = y0 + rows * step + 14
    o.append(f'<circle cx="{x0}" cy="{yb - 4}" r="{r}" fill="var(--arbeit)"/>')
    o.append(t(x0 + 10, yb, "volle Arbeitsjahre zu 300 Tagen: 1567", size=12))
    o.append(f'<circle cx="{x0 + 230}" cy="{yb - 4}" r="{r - 0.6}" fill="none" stroke="var(--arbeit)" stroke-width="1.1"/>')
    o.append(t(x0 + 240, yb, "Beschäftigte insgesamt: 3817", size=12))
    # Rechnung
    rx = 470
    o.append(a(rx, 92, "Gezahlte Löhne 1894: 1 161 332 Mark", T + "zahlen/1", size=14, anchor="start", colour="arbeit", bold=True))
    zeilen = [
        f"je Beschäftigten: rund {LOHN / MENSCHEN:.0f} Mark im Jahr",
        f"je volles Arbeitsjahr: rund {LOHN / VOLL:.0f} Mark,",
        f"also knapp {LOHN / VOLL / 300:.2f} Mark am Tag".replace(".", ","),
        "",
        f"Rechnerisch kam jeder Beschäftigte auf gut {VOLL * 300 / MENSCHEN:.0f}",
        "Arbeitstage: Viele arbeiteten nur einen Teil des",
        "Jahres im Bruch. Warum, sagt die Tabelle nicht.",
    ]
    for k, z in enumerate(zeilen):
        o.append(t(rx, 118 + k * 19, z, size=13, colour="ink" if k < 3 else "ink2"))
    o.append(t(rx, 118 + len(zeilen) * 19 + 6, "Rechnung des Apparats aus Heuslers Tabelle.", size=11.5, colour="ink2", style=' font-style="italic"'))
    # Zeitachse
    ay, ax0, ax1 = 470, 50, W - 50
    X = lambda j: ax0 + (j - 1880) / 20 * (ax1 - ax0)
    o.append(f'<line x1="16" y1="{ay - 182}" x2="{W - 16}" y2="{ay - 182}" stroke="var(--line)"/>')
    o.append(t(16, ay - 158, "Was die Quellen 1880–1900 festhalten", size=14, style=' font-weight="bold"'))
    o.append(f'<line x1="{ax0}" y1="{ay}" x2="{ax1}" y2="{ay}" stroke="var(--ink2)" stroke-width="1.5"/>')
    for j in range(1880, 1901, 5):
        o.append(f'<line x1="{X(j):.0f}" y1="{ay - 4}" x2="{X(j):.0f}" y2="{ay + 4}" stroke="var(--ink2)"/>')
    for jahr, z1, z2, ref, col, ebene, anc in EREIGNISSE:
        x = X(jahr)
        ty = ay - 42 * ebene + (0 if ebene > 0 else 6)
        o.append(f'<line x1="{x:.0f}" y1="{ay}" x2="{x:.0f}" y2="{ty + 20 if ebene > 0 else ty - 14:.0f}" stroke="var(--{col})" stroke-width="1.2"/>')
        o.append(f'<circle cx="{x:.0f}" cy="{ay}" r="5" fill="var(--{col})"/>')
        o.append(a(x, ty - 8 if ebene > 0 else ty, f"{jahr}: {z1}", T + ref, size=11.5, anchor=anc, colour=col, bold=True))
        o.append(t(x, (ty - 8 if ebene > 0 else ty) + 14, z2, size=11, anchor=anc, colour="ink2"))
    o.append(t(16, H - 14, "Die amtlichen Berichte nennen keine Namen der Toten. Die Arbeiter selbst kommen in diesen Quellen kaum zu Wort.", size=11.5, colour="ink2"))
    o.append('</svg>')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


if __name__ == "__main__":
    main()
