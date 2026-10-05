"""Zeichnet assets/viz/holland.svg: wohin der Basalt ging, nach Heusler (1897) und der Handelskammer
Bonn (1895/96): links die Steinsorten, die beim Brechen zugleich anfallen, rechts ihre Abnehmer,
dazwischen der Weg (Rhein oder Bahn). Unten die Zahlen eines Betriebs für 1895 und der Jahresbedarf
Hollands an Säulen nach der Basalt-Actien-Gesellschaft (1893). Jede Beschriftung verweist auf die Stelle.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-holland.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "holland.svg"
T = "#/text/holland/"
W, H = 900, 560


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


SORTEN = [  # Name, Erklärung, Verweis
    ("Säulen", "lang, glatt, ganz verschifft", "holland/2"),
    ("Krotzen, Senksteine", "Brocken für den Wasserbau", "gesellschaft/2"),
    ("Kopf- und Pflastersteine", "behauen", "holland/2"),
    ("Kleinschlag, Schotter", "„Abfallmaterialien“", "syndikat/2"),
]
ZIELE = [
    ("Holland, Belgien: Ufer und Deiche", "holland/2", "sea"),
    ("Nordsee: Häfen, Kanäle, Küstenschutz", "syndikat/1", "sea"),
    ("Rheinstädte, Inland: Straßenpflaster", "holland/2", "bruch"),
    ("Wegebau", "syndikat/2", "bruch"),
]
FLUSS = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (3, 3), (3, 0)]


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ho-t ho-d" font-family="var(--serif)">',
         '<title id="ho-t">Vom Bruch an die Küste</title>',
         '<desc id="ho-d">Ein Flussdiagramm. Links die Steinsorten, die beim Brechen zugleich anfallen: Säulen, Krotzen und Senksteine, Kopf- und Pflastersteine, Kleinschlag und Schotter. Rechts die Abnehmer: Holland und Belgien für Ufer und Deiche, die deutsche Nordseeküste für Häfen, Kanäle und Küstenschutz, die Rheinstädte und das Inland für Straßenpflaster, der Wegebau für Schotter. Säulen und Senksteine gehen auf dem Rhein zu Schiff an die Küsten, Pflaster und Schotter bleiben im Land. Unten die Zahlen eines Betriebs für 1895: 369 346 Tonnen gefördert, 338 556 Tonnen abgeliefert, 160 736 Tonnen auf Lager, auch auf holländischen Lagerplätzen; und der Jahresbedarf Hollands an Säulen nach der Basalt-Actien-Gesellschaft 1893: wenig mehr als 10 000 Doppellader.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Vom Bruch an die Küste</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Was beim Brechen anfiel und wohin es ging, nach Heusler (1897) und der Handelskammer Bonn (1895/96). Schema.</text>']
    lx, rx, y0, dy = 40, 600, 100, 74
    for i, (name, erk, ref) in enumerate(SORTEN):
        y = y0 + i * dy
        o.append(f'<rect x="{lx}" y="{y - 22}" width="250" height="44" rx="6" fill="var(--stein)" opacity="0.15" stroke="var(--stein)"/>')
        o.append(a(lx + 12, y - 2, name, T + ref, size=13.5, anchor="start", bold=True))
        o.append(f'<text x="{lx + 12}" y="{y + 15}" font-size="11.5" fill="var(--ink2)">{escape(erk)}</text>')
    for j, (name, ref, col) in enumerate(ZIELE):
        y = y0 + j * dy
        o.append(f'<rect x="{rx}" y="{y - 22}" width="270" height="44" rx="6" fill="var(--{col})" opacity="0.12" stroke="var(--{col})"/>')
        o.append(a(rx + 12, y + 5, name, T + ref, size=12.5, anchor="start", colour=col, bold=True))
    for i, j in FLUSS:
        y1, y2 = y0 + i * dy, y0 + j * dy
        col = ZIELE[j][2]
        o.append(f'<path d="M {lx + 250} {y1} C {lx + 400} {y1}, {rx - 150} {y2}, {rx} {y2}" fill="none" stroke="var(--{col})" stroke-width="{5 if j < 2 else 3}" opacity="0.55"/>')
    o.append(a(445, y0 - 36, "auf dem Rhein, zu Schiff", T + "holland/1", size=12.5, colour="sea", bold=True))
    o.append(a(445, y0 + 3 * dy + 40, "im Land, mit Bahn und Fuhrwerk", T + "holland/2", size=12, colour="bruch"))
    # Zahlen
    zy = 440
    o.append(f'<line x1="40" y1="{zy - 22}" x2="{W - 30}" y2="{zy - 22}" stroke="var(--line)"/>')
    o.append(a(40, zy, "Ein Betrieb, 1895:", T + "gesellschaft/2", size=13, anchor="start", bold=True))
    o.append('<text x="40" y="460" font-size="12.5" fill="var(--ink)">gefördert 369 346 t · abgeliefert 338 556 t · auf Lager am Jahresende 160 736 t, „in Deutschland und auf den holländischen Lagerplätzen“</text>')
    o.append('<text x="40" y="478" font-size="12.5" fill="var(--ink)">ca. 950 Arbeiter · im ersten Vierteljahr ruhte die Schifffahrt, im Herbst Niedrigwasser</text>')
    o.append(a(40, 506, "Hollands Jahresbedarf an Säulen nach der Basalt-Actien-Gesellschaft, 1893:", T + "tarif/2", size=13, anchor="start", bold=True))
    o.append('<text x="40" y="526" font-size="12.5" fill="var(--ink)">„wenig mehr als 10 000 Doppellader“, also rund 100 000 Tonnen; die rheinischen Brüche könnten das Doppelte liefern.</text>')
    o.append('</svg>')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


if __name__ == "__main__":
    main()
