"""Zeichnet assets/viz/unkel.svg: das Jahr 1846 an der Landstraße vor den Unkeler Brüchen
(nach Nöggerath 1847, S. 26–28) als Zeitleiste und darunter einen schematischen Querschnitt
von der Rheinseite bis zum Birgeler Kopf: Rhein, Landstraße mit Futtermauer, Lagerplatz der
Pflastersteine, Steinbruchsstoß, Konglomerat und Ton. Jede Beschriftung verweist auf die Stelle.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-unkel.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "unkel.svg"
T = "#/text/unkel/"
W, H = 900, 600


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


EVENTS = [  # (Monat als Kommazahl, Kurztext, Verweis)
    (0.5, "Januar: Bankett hebt sich, zweimal abgetragen", "schluepf/1"),
    (3.5, "April: alte Futtermauer reißt", "schluepf/1"),
    (8.6, "Sept./Okt.: neue Futtermauer, 274 Fuß", "schluepf/1"),
    (11.45, "14.–16. Dez.: Mauer reißt, hängt über", "schluepf/1"),
    (11.6, "19. Dez.: Spalten, Wache", "schluepf/1"),
    (11.66, "20. Dez., 5 Uhr: Rutsch", "schluepf/2"),
]


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="un-t un-d" font-family="var(--serif)">',
         '<title id="un-t">Ein Jahr der Warnungen</title>',
         '<desc id="un-d">Oben eine Zeitleiste des Jahres 1846 an der Landstraße vor den Unkeler Brüchen nach Nöggerath: im Januar hebt sich der Randstreifen der Straße, im April reißt die alte Stützmauer, im September und Oktober wird eine neue Mauer von 274 Fuß gebaut, vom 14. bis 16. Dezember reißt sie, am 19. Dezember entstehen Spalten und die Straße wird bewacht, am 20. Dezember um 5 Uhr morgens rutscht der Berg. Unten ein schematischer Schnitt vom Rhein zum Birgeler Kopf: Rhein, Landstraße mit Stützmauer, der Platz mit behauenen Pflastersteinen, der um fast 60 Fuß gehoben wurde, die Abbauwand der Brüche, darüber Konglomerat und Löss, darunter Ton auf Schiefer als Gleitfläche, und oben die Kuppe des Birgeler Kopfs, 380 Fuß über dem Rhein.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Ein Jahr der Warnungen</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Die Landstraße Koblenz–Köln vor den Unkeler Brüchen, 1846, nach Nöggerath (1847). Unten ein Schema, nicht maßstäblich.</text>']
    # Zeitleiste
    x0, x1, y = 60, 860, 110
    o.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="var(--ink2)" stroke-width="2"/>')
    for m, lab in enumerate("JFMAMJJASOND"):
        xx = x0 + (x1 - x0) * m / 12
        o.append(f'<line x1="{xx:.0f}" y1="{y - 5}" x2="{xx:.0f}" y2="{y + 5}" stroke="var(--ink2)"/>')
        o.append(f'<text x="{xx + (x1 - x0) / 24:.0f}" y="{y + 20}" font-size="11" text-anchor="middle" fill="var(--ink2)">{lab}</text>')
    rows = [74, 150, 74, 150, 172, 194]
    for (m, txt, href), ty in zip(EVENTS, rows):
        xx = x0 + (x1 - x0) * m / 12
        col = "bruch" if "Rutsch" in txt else "ink"
        o.append(f'<circle cx="{xx:.0f}" cy="{y}" r="{6 if col == "bruch" else 4}" fill="var(--{col})"/>')
        o.append(f'<line x1="{xx:.0f}" y1="{y}" x2="{xx:.0f}" y2="{ty - 12 if ty > y else ty + 4}" stroke="var(--line)"/>')
        anchor = "end" if m > 10 else "start"
        o.append(a(xx + (-6 if anchor == "end" else 6), ty, txt, T + href, size=12, anchor=anchor, colour=col, bold=col == "bruch"))
    # Querschnitt
    base = 560
    o.append('<path d="M 30 520 L 160 520 L 160 560 L 30 560 Z" fill="var(--sea)" opacity="0.35"/>')
    o.append(a(95, 545, "Rhein", T + "unkelstein/2", size=13, colour="sea"))
    # Gelände (Schema): Straße, gehobener Platz, Bruchwand, Hang, Kuppe
    o.append('<path d="M 160 520 L 230 505 L 300 505 L 330 450 L 380 440 L 420 300 L 520 290 L 640 250 L 760 230 L 820 236 L 860 250 L 860 560 L 160 560 Z" fill="var(--stein)" opacity="0.18"/>')
    o.append('<path d="M 160 520 L 230 505 L 300 505 L 330 450 L 380 440 L 420 300 L 520 290 L 640 250 L 760 230 L 820 236 L 860 250" fill="none" stroke="var(--ink)" stroke-width="1.6"/>')
    # Tonschicht als Gleitfläche
    o.append('<path d="M 230 530 Q 420 470 560 380 T 860 300" fill="none" stroke="var(--arbeit)" stroke-width="5" stroke-dasharray="10 6"/>')
    o.append(a(600, 420, "Ton auf Schiefer: Gleitfläche", T + "schluepf/3", size=12.5, colour="arbeit"))
    # Straße und Mauer
    o.append('<rect x="190" y="500" width="40" height="8" fill="var(--ink2)"/>')
    o.append(a(205, 490, "Landstraße, Futtermauer", T + "schluepf/1", size=11.5, anchor="middle"))
    # gehobener Platz
    o.append('<path d="M 300 505 L 330 450 L 380 440" fill="none" stroke="var(--bruch)" stroke-width="4"/>')
    o.append('<line x1="315" y1="505" x2="315" y2="455" stroke="var(--bruch)" stroke-width="1.5" marker-end="url(#un-ar)"/>')
    o.append('<defs><marker id="un-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="var(--bruch)"/></marker></defs>')
    o.append(a(250, 438, "Platz der Pflastersteine, gehoben um fast 60 Fuß", T + "schluepf/5", size=12, anchor="middle", colour="bruch", bold=True))
    # Bruchwand mit Säulen
    for i in range(6):
        o.append(f'<line x1="{386 + i * 6}" y1="{436 - i * 18}" x2="{396 + i * 6}" y2="{436 - i * 18 - 16}" stroke="var(--ink)" stroke-width="3"/>')
    o.append(a(470, 360, "Abbauwand der fünf Brüche", T + "schluepf/5", size=12, anchor="start"))
    o.append(a(470, 377, "Steinbrecherhütten gehoben, zerrissen", T + "schluepf/6", size=11.5, anchor="start", colour="ink2"))
    o.append(a(560, 270, "Konglomerat und Löss, Rutschflächen", T + "schluepf/3", size=11.5, anchor="middle", colour="ink2"))
    o.append(a(790, 218, "Birgeler Kopf, 380 Fuß über dem Rhein", T + "unkelstein/2", size=12, anchor="middle"))
    o.append(f'<text x="470" y="{base + 28}" font-size="11.5" text-anchor="middle" fill="var(--ink2)">Schema nach Nöggeraths Beschreibung, nicht maßstäblich; seine Karte und Profile (Taf. I und II) sind im Digitalisat nicht vollständig erfasst.</text>')
    o.append('</svg>')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


if __name__ == "__main__":
    main()
