"""Zeichnet assets/viz/verordnung.svg: oben die beiden Lager um die Polizeiverordnung vom 26. Oktober 1899
(wer sie trug, wer sich wehrte), unten die Zahlen, die sich in den Quellen widersprechen oder gegenüberstehen:
2000 oder 300 Arbeiter, Löhne bis 6–7 Mark oder im Mittel knapp 2,50 Mark, Kaufpreise für Besitzer und
keine Entschädigung für Arbeiter. Jede Beschriftung verweist auf die Stelle.
Aufruf aus dem Wurzelverzeichnis: python tools/viz-verordnung.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "viz" / "verordnung.svg"
T = "#/text/verordnung/"
W, H = 900, 520


def a(x, y, text, href, size=12.5, anchor="middle", colour="ink", bold=False):
    return (f'<a href="{href}"><text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" font-weight="{"bold" if bold else "normal"}" '
            f'fill="var(--{colour})" stroke="var(--panel)" stroke-width="4" paint-order="stroke" text-decoration="underline">{escape(text)}</text></a>')


def t(x, y, text, size=12.5, anchor="start", colour="ink", extra=""):
    return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{size}" fill="var(--{colour})"{extra}>{escape(text)}</text>'


FUER = [  # Wer, was, Verweis
    ("Regierungspräsident in Köln", "erlässt die Verordnung", "verordnung/2"),
    ("Verschönerungsverein", "kauft, mit Enteignungsrecht", "ankauf/1"),
    ("Rheinische Provinz", "kündigt die Lieferverträge", "verordnung/4"),
    ("Landwirtschaftsminister", "„mehr Agitationssache“", "landtag/2"),
    ("„Die Denkmalpflege“", "„die weise Massregel“", "verordnung/3"),
]
GEGEN = [
    ("Steinarbeiterverbände", "Zentrale in Honnef, Febr. 1900", "arbeiter/2"),
    ("Bruchbesitzer", "klagen beim Kreisausschuss", "ankauf/2"),
    ("Handelskammer Bonn", "„zu weitgehend“", "verordnung/4"),
    ("Stadt Königswinter", "„schwere Schädigung“", "landtag/1"),
    ("Abgeordneter de Witt", "„nicht auf Kosten der Arbeiter“", "landtag/1"),
]


def box(o, x, y, w, wer, was, ref, col):
    o.append(f'<rect x="{x}" y="{y - 20}" width="{w}" height="42" rx="6" fill="var(--{col})" opacity="0.12" stroke="var(--{col})"/>')
    o.append(a(x + 12, y - 2, wer, T + ref, size=12.5, anchor="start", colour=col, bold=True))
    o.append(t(x + 12, y + 14, was, size=11.5, colour="ink2"))


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="vo-t vo-d" font-family="var(--serif)">',
         '<title id="vo-t">Für und gegen die Verordnung, 1899–1901</title>',
         '<desc id="vo-d">Links die Seite, die die Polizeiverordnung vom 26. Oktober 1899 trug: der Regierungspräsident in Köln, der Verschönerungsverein mit dem Enteignungsrecht, die Rheinische Provinz, die den Brüchen im Schonbezirk die Lieferverträge kündigte, der Landwirtschaftsminister und die Zeitschrift „Die Denkmalpflege“. Rechts die Seite, die sich wehrte: die christlich-sozialen Steinarbeiterverbände, die Bruchbesitzer mit ihrer Beschwerde beim Kreisausschuss in Siegburg, die Handelskammer Bonn, die Stadt Königswinter und der Abgeordnete de Witt. Arbeiter und Bruchbesitzer standen gemeinsam gegen die Verordnung, aus verschiedenen Gründen. Unten die Zahlen: 2000 Arbeiter nach Saget, etwa 300 nach de Witt; Löhne bis 6 und 7 Mark am Tag nach Saget, im Durchschnitt des Reviers 1894 knapp 2,50 Mark; 65 000 Mark für einen Bruch und 640 000 Mark für Wald am Lohrberg, für die Arbeiter keine Entschädigung.</desc>',
         '<text x="16" y="28" font-size="17" font-weight="bold" fill="var(--ink)">Für und gegen die Verordnung, 1899–1901</text>',
         '<text x="16" y="48" font-size="13" fill="var(--ink2)">Wer die Polizeiverordnung vom 26. Oktober 1899 trug und wer sich wehrte, nach den Quellen dieses Moduls.</text>']
    lx, rx, bw, y0, dy = 30, 560, 310, 110, 52
    o.append(t(lx, 86, "trugen sie", size=14, extra=' font-weight="bold"'))
    o.append(t(rx, 86, "wehrten sich", size=14, extra=' font-weight="bold"'))
    for k, (wer, was, ref) in enumerate(FUER):
        box(o, lx, y0 + k * dy, bw, wer, was, ref, "staat")
    for k, (wer, was, ref) in enumerate(GEGEN):
        box(o, rx, y0 + k * dy, bw, wer, was, ref, "arbeit" if k in (0, 4) else "bruch")
    cy = y0 + 2 * dy
    o.append(f'<rect x="{lx + bw + 20}" y="{cy - 46}" width="{rx - lx - bw - 40}" height="92" rx="8" fill="var(--panel)" stroke="var(--ink2)" stroke-width="1.5"/>')
    o.append(a(W / 2, cy - 20, "Polizeiverordnung", T + "verordnung/2", size=13.5, colour="ink", bold=True))
    o.append(t(W / 2, cy - 2, "26. Oktober 1899", size=12, anchor="middle"))
    o.append(t(W / 2, cy + 16, "keine neuen Brüche,", size=11.5, anchor="middle", colour="ink2"))
    o.append(t(W / 2, cy + 31, "keine Erweiterung", size=11.5, anchor="middle", colour="ink2"))
    # Bündnis
    by = y0 + 4 * dy + 40
    o.append(f'<path d="M {rx + bw + 6} {y0} C {rx + bw + 26} {y0}, {rx + bw + 26} {y0 + dy}, {rx + bw + 6} {y0 + dy}" fill="none" stroke="var(--ink2)" stroke-width="1.5"/>')
    o.append(a(rx + bw - 2, by, "Arbeiter und Bruchbesitzer gemeinsam, aus verschiedenen Gründen", T + "arbeiter/2", size=11.5, anchor="end", colour="ink2"))
    # Zahlen
    zy = by + 36
    o.append(f'<line x1="16" y1="{zy - 18}" x2="{W - 16}" y2="{zy - 18}" stroke="var(--line)"/>')
    o.append(t(16, zy + 4, "Zahlen, die sich widersprechen oder gegenüberstehen", size=14, extra=' font-weight="bold"'))
    rows = [
        ("Betroffene Arbeiter", [("2000 im Schutzgebiet (Saget 1899)", "arbeiter/1"), ("etwa 300 (de Witt 1901)", "landtag/1")]),
        ("Lohn am Tag", [("„bis auf 6 und 7 M.“ (Saget 1900)", "ankauf/2"), ("knapp 2,50 M. im Mittel des Reviers 1894", "#/text/arbeit/zahlen/1")]),
        ("Gezahlt", [("65 000 M. für einen Bruch, 640 000 M. für Wald", "ankauf/1"), ("für die Arbeiter: nichts berichtet", "ankauf/1")]),
    ]
    y = zy + 34
    for label, items in rows:
        o.append(t(16, y, label, size=12.5, extra=' font-weight="bold"'))
        for k, (txt, ref) in enumerate(items):
            href = ref if ref.startswith("#") else T + ref
            o.append(a(200 + k * 350, y, txt, href, size=12, anchor="start", colour="arbeit" if k == 1 and label == "Gezahlt" else "ink"))
        y += 26
    o.append('</svg>')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(o), encoding="utf-8")
    print(OUT.name)


if __name__ == "__main__":
    main()
