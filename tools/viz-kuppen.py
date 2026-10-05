"""Zeichnet assets/viz/kuppen.svg: von Dechens Tabelle der Basaltberge (1861) als Profil,
35 Kuppen nach ihrer Höhe über dem Rhein bei Königswinter. Farbe nach der dritten Spalte
der Tabelle (worüber der Basalt aufragt); markiert die Berge, an denen von Dechen 1861
Steinbrüche nennt. Jede Beschriftung verweist auf die Stelle im Apparat.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-kuppen.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "kuppen.svg"
T = "#/text/stein/"
PF = 0.3248  # Pariser Fuß in Meter

# (Name, über dem Rhein bei Königswinter in Pariser Fuß, Untergrund laut 3. Spalte)
ROWS = [
    ("Gr. Oelberg", 1279, "Trachyt"), ("Düstemich (Mehrberg)", 1265, ""), ("Löwenburg", 1263, "Trachyt"),
    ("Dasberg", 1219, ""), ("Asberg", 1208, "Devon"), ("Hummelsberg", 1195, "Devon"), ("Minderberg", 1184, "Devon"),
    ("Mahlberg", 1059, "Devon"), ("Ginsterhahn", 1040, ""), ("In den Hülsen", 999, ""), ("Erpeler Steinbüchel", 988, ""),
    ("Linzer Steinbüchel", 984, ""), ("Kl. Oelberg", 965, ""), ("Leiberg", 923, "Devon"), ("Nonnenstromberg", 886, "Konglomerat"),
    ("Petersberg", 877, ""), ("Höhnerberg", 845, ""), ("Scheidsburg", 745, ""), ("Landskrone", 706, ""), ("Wachtberg", 670, ""),
    ("Dollendorfer Hardt", 630, "Devon"), ("Sitzenbusch", 599, ""), ("Limberg", 589, ""), ("Gr. Weilberg", 589, ""),
    ("Tungberg", 578, ""), ("Himperich", 571, ""), ("Steinringsberg", 556, ""), ("Gr. Scharfenberg", 553, "Konglomerat"),
    ("Hartenberg", 541, "Konglomerat"), ("Falkenberg", 529, ""), ("Thomasberg", 481, ""), ("Erpeler Ley", 475, "Geröll"),
    ("Casseler Ley", 466, ""), ("Gudenauer Windmühle", 453, "Geröll"), ("Kl. Weilberg", 444, ""),
]
# Berge, an denen von Dechen 1861 Steinbrüche nennt (Säulen [1], [2])
BRUCH = {"Minderberg": "saeulen/1", "Erpeler Ley": "saeulen/1", "Casseler Ley": "saeulen/1"}
COL = {"Trachyt": ("var(--bruch)", "über Trachyt"), "Konglomerat": ("var(--arbeit)", "über Trachyt-Konglomerat"),
       "Devon": ("var(--staat)", "über Devonschichten (Westerwald-Schiefer)"), "Geröll": ("var(--schutz)", "von Geröll bedeckt"),
       "": ("var(--stein)", "ohne Angabe")}

W = 900
LEFT, TOP, ROW = 190, 118, 17
SCALE = 520 / 1300  # Pixel je Pariser Fuß


def main():
    H = TOP + ROW * len(ROWS) + 70
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="ku-t ku-d" font-family="var(--serif)">',
         '<title id="ku-t">Fünfunddreißig Kuppen, 1861</title>',
         '<desc id="ku-d">Ein liegendes Balkendiagramm nach Heinrich von Dechens Tabelle „Höhen der Basaltberge“ von 1861: 35 Basaltberge zwischen Siebengebirge, Rhein und Westerwald, vom Großen Ölberg mit 1279 Pariser Fuß über dem Rhein bei Königswinter bis zum Kleinen Weilberg mit 444 Fuß. Die Farbe zeigt, worüber der Basalt nach der Tabelle aufragt: Trachyt, Trachyt-Konglomerat, Devonschichten oder Geröll. Ein Hammerzeichen markiert die drei Berge der Tabelle, an denen von Dechen 1861 Steinbrüche nennt: Minderberg, Erpeler Ley und Casseler Ley.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Fünfunddreißig Kuppen, 1861</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Höhe über dem mittleren Rheinspiegel bei Königswinter, nach von Dechens Tabelle (Pariser Fuß; 1 Fuß = 32,5 cm).</text>',
         '<text x="16" y="64" font-size="13" fill="var(--ink2)">Farbe: worüber der Basalt aufragt. ⚒ an diesen Bergen nennt von Dechen 1861 Steinbrüche.</text>']
    # Legende
    x = 16
    for k in ("Trachyt", "Konglomerat", "Devon", "Geröll", ""):
        c, lab = COL[k]
        o.append(f'<rect x="{x}" y="78" width="12" height="12" fill="{c}"/>')
        o.append(f'<text x="{x + 17}" y="89" font-size="12" fill="var(--ink2)">{escape(lab)}</text>')
        x += 17 + len(lab) * 6.3 + 18
    # Raster
    for f in range(0, 1301, 200):
        xx = LEFT + f * SCALE
        o.append(f'<line x1="{xx:.1f}" y1="{TOP - 8}" x2="{xx:.1f}" y2="{TOP + ROW * len(ROWS)}" stroke="var(--line)" stroke-width="1"/>')
        o.append(f'<text x="{xx:.1f}" y="{TOP - 12}" font-size="11" text-anchor="middle" fill="var(--ink2)">{f}</text>')
        o.append(f'<text x="{xx:.1f}" y="{TOP + ROW * len(ROWS) + 14}" font-size="11" text-anchor="middle" fill="var(--ink2)">{round(f * PF)} m</text>')
    for i, (name, h, grund) in enumerate(ROWS):
        y = TOP + i * ROW
        c = COL[grund][0]
        o.append(f'<rect x="{LEFT}" y="{y + 2}" width="{h * SCALE:.1f}" height="{ROW - 5}" fill="{c}" opacity="0.85"/>')
        o.append(f'<a href="{T}kuppen/2"><text x="{LEFT - 8}" y="{y + 12}" font-size="12" text-anchor="end" fill="var(--ink)" text-decoration="underline">{escape(name)}</text></a>')
        o.append(f'<text x="{LEFT + h * SCALE + 6:.1f}" y="{y + 12}" font-size="11" fill="var(--ink2)">{h} · {round(h * PF)} m</text>')
        if name in BRUCH:
            xx = LEFT + h * SCALE + 92
            o.append(f'<a href="{T}{BRUCH[name]}"><text x="{xx:.1f}" y="{y + 12}" font-size="12" fill="var(--bruch)" text-decoration="underline">⚒ Steinbrüche 1861</text></a>')
    o.append(f'<a href="{T}saeulen/1"><text x="16" y="{H - 20}" font-size="12.5" fill="var(--ink)" text-decoration="underline">„An den zum Siebengebirge selbst gehörenden Basaltbergen befinden sich keine bedeutende Steinbrüche.“ (von Dechen 1861)</text></a>')
    o.append('</svg>')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


if __name__ == "__main__":
    main()
