"""Zeichnet assets/viz/aufschwung.svg: eine Lageskizze des nördlichen Siebengebirges um 1890,
wie der Stein an den Rhein kam: Fahrweg vom Ölberg nach Königswinter, Seilbahn vom Petersberg ins
Mühlbachtal, Heisterbacher Thalbahn ab 1891, rechtsrheinische Eisenbahn ab 1870, die Brüche bei
Oberkassel. Lage nach heutigen Karten, vereinfacht und ungefähr. Jede Beschriftung verweist auf
die Stelle im Apparat. Aufruf aus dem Wurzelverzeichnis: python tools/viz-aufschwung.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "aufschwung.svg"
T = "#/text/aufschwung/"
W, H = 900, 620
LAT0, LAT1, LON0, LON1 = 50.655, 50.725, 7.140, 7.275


def xy(lat, lon):
    return (40 + (lon - LON0) / (LON1 - LON0) * (W - 80), 70 + (LAT1 - lat) / (LAT1 - LAT0) * (H - 140))


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def path(pts):
    return " ".join(("M" if i == 0 else "L") + f" {x:.0f} {y:.0f}" for i, (x, y) in enumerate(xy(*p) for p in pts))


RHEIN = [(50.655, 7.204), (50.675, 7.191), (50.695, 7.176), (50.712, 7.160), (50.725, 7.146)]
ORTE = {"Königswinter": (50.674, 7.196), "Niederdollendorf": (50.696, 7.180), "Oberdollendorf": (50.698, 7.192),
        "Oberkassel": (50.713, 7.168), "Heisterbach": (50.693, 7.214), "Heisterbacherrott": (50.703, 7.232)}
BERGE = {  # Name: (lat, lon, Gestein, Verweis)
    "Petersberg": (50.687, 7.207, "Basalt", "talbahn/3"), "Gr. Ölberg": (50.674, 7.246, "Basalt", "baedeker/2"),
    "Stenzelberg": (50.692, 7.244, "Trachyt", "baedeker/2"), "Nonnenstromberg": (50.682, 7.229, "Basalt", "baedeker/2"),
    "Wolkenburg": (50.667, 7.219, "Trachyt", "gewerbe/4"), "Drachenfels": (50.665, 7.210, "Trachyt", "baedeker/1"),
    "Kasseler Ley, Rabenlei": (50.708, 7.178, "Basalt", "gewerbe/1"),
}


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="au-t au-d" font-family="var(--serif)">',
         '<title id="au-t">Vom Bruch an den Rhein, um 1890</title>',
         '<desc id="au-d">Eine vereinfachte Lageskizze des nördlichen Siebengebirges. Links fließt der Rhein von Süden nach Norden, an seinem Ufer liegen Königswinter, Niederdollendorf und Oberkassel; am Ufer entlang fährt seit 1870 die rechtsrheinische Eisenbahn. Im Gebirge liegen die Basaltberge Petersberg, Nonnenstromberg und Großer Ölberg und die Trachytberge Drachenfels, Wolkenburg und Stenzelberg. Vom Ölberg führt ein Fahrweg nach Königswinter; vom Petersberg eine Drahtseilbahn ins Mühlbachtal bei Oberdollendorf; von Niederdollendorf die Heisterbacher Thalbahn über Oberdollendorf und Heisterbach nach Heisterbacherrott. Bei Oberkassel liegen die Brüche an der Kasseler Ley und Rabenlei.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Vom Bruch an den Rhein, um 1890</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Lageskizze, vereinfacht; Lage nach heutigen Karten, ungefähr. Basaltberge dunkel, Trachytberge hell.</text>']
    o.append(f'<path d="{path(RHEIN)}" fill="none" stroke="var(--sea)" stroke-width="16" opacity="0.35" stroke-linecap="round"/>')
    x, y = xy(50.660, 7.165)
    o.append(f'<text x="{x:.0f}" y="{y:.0f}" font-size="14" fill="var(--sea)" font-style="italic">Rhein</text>')
    bahn = [(p[0], p[1] + 0.006) for p in RHEIN]
    o.append(f'<path d="{path(bahn)}" fill="none" stroke="var(--ink)" stroke-width="2.5" stroke-dasharray="9 4"/>')
    x, y = xy(50.683, 7.192)
    o.append(a(x - 6, y, "Rechtsrheinische Bahn, 1870", T + "gewerbe/2", size=11.5, anchor="end", colour="ink2"))
    for name, (lat, lon, gestein, ref) in BERGE.items():
        x, y = xy(lat, lon)
        fill = "var(--stein)" if gestein == "Basalt" else "var(--line)"
        o.append(f'<path d="M {x - 16:.0f} {y + 8:.0f} L {x:.0f} {y - 12:.0f} L {x + 16:.0f} {y + 8:.0f} Z" fill="{fill}" stroke="var(--ink2)"/>')
        o.append(a(x, y + 24, name, T + ref, size=12, colour="ink"))
    for name, (lat, lon) in ORTE.items():
        x, y = xy(lat, lon)
        o.append(f'<rect x="{x - 4:.0f}" y="{y - 4:.0f}" width="8" height="8" fill="var(--ink)"/>')
        dx, dy, anc = {"Niederdollendorf": (-8, -6, "end"), "Heisterbacherrott": (-6, 18, "end"), "Heisterbach": (8, 16, "start")}.get(name, (8, -6, "start"))
        o.append(f'<text x="{x + dx:.0f}" y="{y + dy:.0f}" font-size="12" text-anchor="{anc}" fill="var(--ink)">{escape(name)}</text>')
    # Fahrweg Ölberg -> Königswinter
    o.append(f'<path d="{path([(50.674, 7.246), (50.676, 7.230), (50.675, 7.212), (50.674, 7.198)])}" fill="none" stroke="var(--bruch)" stroke-width="2.5"/>')
    x, y = xy(50.6755, 7.222)
    o.append(a(x, y - 8, "Fahrweg nach Königswinter", T + "baedeker/1", size=11.5, colour="bruch"))
    # Seilbahn Petersberg -> Mühlbachtal
    o.append(f'<path d="{path([(50.689, 7.206), (50.697, 7.197)])}" fill="none" stroke="var(--bruch)" stroke-width="2" stroke-dasharray="2 4"/>')
    x, y = xy(50.693, 7.203)
    o.append(a(x + 6, y + 2, "Drahtseilbahn", T + "talbahn/1", size=11.5, anchor="start", colour="bruch", bold=True))
    # Heisterbacher Thalbahn
    o.append(f'<path d="{path([(50.696, 7.180), (50.698, 7.192), (50.693, 7.214), (50.703, 7.232), (50.704, 7.248)])}" fill="none" stroke="var(--staat)" stroke-width="3"/>')
    x, y = xy(50.704, 7.248)
    o.append(a(x + 4, y - 22, "Heisterbacher Thalbahn, 1891", T + "talbahn/2", size=12, anchor="middle", colour="staat", bold=True))
    o.append(a(x + 4, y + 18, "bis Grengelsbitze (Lage ungefähr)", T + "talbahn/2", size=11, anchor="middle", colour="ink2"))
    # Oberkassel Bevölkerung
    x, y = xy(50.716, 7.168)
    o.append(a(x + 8, y - 16, "Pfarre Oberkassel: 709 Einwohner 1861, 1884 im Jahr 1890", T + "gewerbe/3", size=12, anchor="start", colour="arbeit", bold=True))
    o.append(f'<text x="16" y="{H - 16}" font-size="11.5" fill="var(--ink2)">Nicht eingezeichnet: die Brüche bei Linz, Erpel und Unkel südlich des Ausschnitts (Baedeker [3]).</text>')
    o.append('</svg>')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


if __name__ == "__main__":
    main()
