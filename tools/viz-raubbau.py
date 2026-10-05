"""Zeichnet assets/viz/raubbau.svg: oben die Entscheidungen von 1828 bis 1899 auf einer Zeitachse, vom
Drachenfels über „zur Tagesordnung“ (1886) und „zur Erwägung“ (1887) bis „einstimmig“ (1899); unten die
Geldbeträge, um die es ging, in einem gemeinsamen Maßstab: Haushalt des Verschönerungsvereins 1898,
Kaufpreis und Ertrag des Provinzbruchs am Petersberg, die Zusagen von 1899. Jede Beschriftung verweist
auf die Stelle. Aufruf aus dem Wurzelverzeichnis: python tools/viz-raubbau.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "raubbau.svg"
T = "#/text/raubbau/"
W, H = 900, 590


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def t(x, y, text, size=12.5, anchor="start", colour="ink", extra=""):
    return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" fill="var(--{colour})"{extra}>{escape(text)}</text>'


STATIONEN = [  # x-Position, Jahr, Gremium, Ergebnis, Verweis, Farbe
    (90, "1828–1836", "Regierung, König", "Bruch verboten, Gipfel übernommen", "drachenfels/2", "staat"),
    (280, "1886", "Provinziallandtag", "„zur Tagesordnung“, alle gegen drei", "landtag/1", "bruch"),
    (460, "1887", "Petitionskommission", "„zur Erwägung“, 12 gegen 9", "petition/4", "staat"),
    (640, "1897", "Verschönerungsverein", "drei Lotterien, Enteignungsrecht", "lotterie/2", "schutz"),
    (815, "1899", "Provinziallandtag", "200 000 Mark, einstimmig", "lotterie/4", "schutz"),
]

BETRAEGE = [  # Beschriftung, Betrag, Verweis, Farbe, Zusatz
    ("Haushalt des Verschönerungsvereins 1898", 11922, "lotterie/2", "schutz", "11 922 Mark"),
    ("Kaufpreis des Provinzbruchs am Petersberg", 75000, "petition/2", "bruch", "75 000 Mark"),
    ("Reinertrag des Provinzbruchs, jährlich, mindestens", 150000, "petition/3", "bruch", "150 000 Mark"),
    ("Mehrkosten für Basalt aus der Eifel, jährlich", 250000, "petition/2", "bruch", "250 000 Mark, nach der Provinz"),
]
ZUSAGEN = [("Lotterien", 1500000, "staat"), ("Provinz", 200000, "schutz"), ("Köln", 100000, "schutz"), ("Bonn", 50000, "schutz")]


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="rb-t rb-d" font-family="var(--serif)">',
         '<title id="rb-t">Von „zur Tagesordnung“ zu „einstimmig“</title>',
         '<desc id="rb-d">Oben eine Zeitachse mit fünf Entscheidungen: 1828 bis 1836 verbietet die Regierung den Bruch am Drachenfels und übernimmt den Gipfel; 1886 geht der Rheinische Provinziallandtag mit allen gegen drei Stimmen über die Petition zur Tagesordnung über; 1887 überweist die Petitionskommission des Abgeordnetenhauses sie mit 12 gegen 9 Stimmen der Regierung zur Erwägung; 1897 beschließt der Verschönerungsverein, drei Lotterien und das Enteignungsrecht zu beantragen; 1899 bewilligt der Provinziallandtag einstimmig 200 000 Mark. Unten Balken in einem gemeinsamen Maßstab: der Jahreshaushalt des Verschönerungsvereins 1898 mit 11 922 Mark ist kaum sichtbar; der Kaufpreis des Provinzbruchs 75 000 Mark; sein jährlicher Reinertrag mindestens 150 000 Mark; die Mehrkosten für Basalt aus der Eifel nach Angabe der Provinz 250 000 Mark im Jahr; die Zusagen von 1899 zusammen 1 850 000 Mark, davon 1,5 Millionen aus Lotterien, 200 000 von der Provinz, 100 000 von Köln und 50 000 von Bonn.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Von „zur Tagesordnung“ zu „einstimmig“</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Wer über die Brüche im Siebengebirge entschied, 1828–1899, und um welche Summen es ging.</text>']
    ay = 130
    o.append(f'<line x1="40" y1="{ay}" x2="{W - 40}" y2="{ay}" stroke="var(--ink2)" stroke-width="1.5"/>')
    for x, jahr, wer, was, ref, col in STATIONEN:
        o.append(f'<circle cx="{x}" cy="{ay}" r="7" fill="var(--{col})"/>')
        o.append(t(x, ay - 16, jahr, size=14, anchor="middle", extra=' font-weight="bold"'))
        o.append(a(x, ay + 26, wer, T + ref, size=12.5, colour=col, bold=True))
        teile = was.split(", ", 1)
        for k, z in enumerate(teile):
            o.append(t(x, ay + 44 + k * 16, z + ("," if k == 0 and len(teile) > 1 else ""), size=12, anchor="middle", colour="ink2"))
    o.append(t(W / 2, ay + 96, "1886 sagte der Abgeordnete Lucas voraus, „ein späterer Landtag“ werde „die Sache vielleicht mit etwas anderen Augen ansehen“.",
               size=12, anchor="middle", colour="ink2", extra=' font-style="italic"'))
    # Beträge
    by, x0, scale = 290, 330, 520 / 1850000
    o.append(f'<line x1="16" y1="{by - 30}" x2="{W - 16}" y2="{by - 30}" stroke="var(--line)"/>')
    o.append(t(16, by - 6, "Die Summen, in einem Maßstab", size=14, extra=' font-weight="bold"'))
    y = by + 24
    for label, betrag, ref, col, zusatz in BETRAEGE:
        o.append(a(x0 - 10, y + 5, label, T + ref, size=12, anchor="end", colour="ink"))
        w = max(betrag * scale, 1.5)
        o.append(f'<rect x="{x0}" y="{y - 9}" width="{w:.1f}" height="18" fill="var(--{col})" opacity="0.85"/>')
        o.append(t(x0 + w + 8, y + 5, zusatz, size=12, colour="ink2"))
        y += 34
    y += 8
    o.append(a(x0 - 10, y + 5, "Zusagen 1899, zusammen 1 850 000 Mark", T + "lotterie/3", size=12, anchor="end", colour="schutz", bold=True))
    x = x0
    for name, betrag, col in ZUSAGEN:
        w = betrag * scale
        o.append(f'<rect x="{x:.1f}" y="{y - 9}" width="{w:.1f}" height="18" fill="var(--{col})" opacity="{0.85 if col == "schutz" else 0.55}" stroke="var(--panel)"/>')
        x += w
    o.append(t(x0 + 6, y + 30, "Lotterien: mindestens 1 500 000 Mark Reinertrag", size=12, colour="ink2"))
    o.append(t(x0 + 6, y + 47, "Provinz 200 000 · Köln 100 000 · Bonn 50 000 Mark", size=12, colour="ink2"))
    o.append(t(16, H - 34, "Der Haushalt des Vereins von 1898 erscheint als kaum sichtbarer Strich; die Zusagen von 1899 sind rund 155-mal so groß.", size=11.5, colour="ink2"))
    o.append(t(16, H - 16, "Die Beträge zum Provinzbruch sind Angaben der Provinz im Bericht von 1887; der Verein bestritt sie.", size=11.5, colour="ink2"))
    o.append('</svg>')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


if __name__ == "__main__":
    main()
