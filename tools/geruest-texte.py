"""Einmalig: passt die aus der Bröltal-Site übernommenen Gerüsttexte an. Aufruf: python tools/geruest-texte.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sub(path, pairs):
    p = ROOT / path
    s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        assert a in s, (path, a[:60])
        s = s.replace(a, b)
    p.write_text(s, encoding="utf-8")


TITLE = "Basalt zwischen Siebengebirge und Westerwald 1824–1923"
SUB = "Siebengebirge, Rhein und Westerwald · 1824–1923 · ein Quellenapparat"

sub("index.html", [
    ("<title>Die Bröltalbahn. Erz, Dampf und Sommerfrische 1862–1914</title>", f"<title>{TITLE}</title>"),
    ('content="Ein Quellenapparat zur Bröltalbahn, der Schmalspurbahn von Hennef ins Bröltal: wie eine Bahn für das Erz gebaut wurde, das Erz verlor und einen neuen Zweck fand, 1862–1914, in gemeinfreien Zeitungen, Fachzeitschriften und Reiseführern."',
     'content="Ein Quellenapparat zum Basaltabbau zwischen Siebengebirge und Westerwald, 1824–1923: Brüche, Holland, Arbeiter und die Rettung des Siebengebirges, in gemeinfreien Petitionen, Landtagsverhandlungen, Handelskammerberichten und Zeitschriften."'),
    ('<meta property="og:title" content="Die Bröltalbahn. Erz, Dampf und Sommerfrische 1862–1914">', f'<meta property="og:title" content="{TITLE}">'),
    ('content="Gebaut für das Erz, geblieben für das Tal: die Bröltalbahn in ihren Quellen."', 'content="„Am Weilberg habe ein Bruch die Kuppe bereits gespalten“: der Basalt am Rhein in seinen Quellen."'),
    ("<strong>Die Bröltalbahn</strong>", "<strong>Basalt zwischen Siebengebirge und Westerwald</strong>"),
    ("<em>Erz, Dampf und Sommerfrische · 1862–1914 · ein Quellenapparat</em>", f"<em>{SUB}</em>"),
    ("Das Begleitspiel <em>Mit Volldampf ins Bröltal</em> ist in Vorbereitung", "Das Begleitspiel <em>Die Kuppe bereits gespalten</em> ist in Vorbereitung"),
])

sub("legal.html", [
    ("<title>Impressum und Datenschutz · Die Bröltalbahn</title>", "<title>Impressum und Datenschutz · Basalt zwischen Siebengebirge und Westerwald</title>"),
    ("<strong>Die Bröltalbahn</strong>", "<strong>Basalt zwischen Siebengebirge und Westerwald</strong>"),
    ("<em>Erz, Dampf und Sommerfrische · 1862–1914 · ein Quellenapparat</em>", f"<em>{SUB}</em>"),
    ("Es handelt sich um Zeitungen, Fachzeitschriften, amtliche Bekanntmachungen, Bilanzen und Reiseführer der Jahre 1855–1914,",
     "Es handelt sich um geologische Beschreibungen, Reiseführer, Petitionen, Parlaments- und Landtagsverhandlungen, Handelskammerberichte und Zeitschriften der Jahre 1824–1923,"),
    ("Die Bildtafeln sind gemeinfreie Karten, Ansichten und Papiere;", "Die Bildtafeln sind gemeinfreie oder CC0-gestellte Karten, Ansichten und Photographien;"),
    ("<code>broeltal_lang</code>", "<code>basalt_lang</code>"),
])

sub("style.css", [
    ("--gesellschaft:#8c3b1c; --gruben:#5a4a3a; --staat:#2f4f7a; --tal:#3f5a2a; --nachwelt:#7a7064;",
     "--stein:#4b4f55; --bruch:#8c3b1c; --arbeit:#7a5a1c; --schutz:#3f5a2a; --staat:#2f4f7a;"),
    (".side.gesellschaft{background:var(--gesellschaft)} .side.gruben{background:var(--gruben)} .side.staat{background:var(--staat)}",
     ".side.stein{background:var(--stein)} .side.bruch{background:var(--bruch)} .side.staat{background:var(--staat)}"),
    (".side.tal{background:var(--tal)} .side.nachwelt{background:var(--nachwelt)}",
     ".side.arbeit{background:var(--arbeit)} .side.schutz{background:var(--schutz)}"),
])

(ROOT / "README.md").write_text("""# Basalt zwischen Siebengebirge und Westerwald 1824–1923

Ein Quellenapparat zum Basaltabbau zwischen Siebengebirge und Westerwald: Königswinter, Oberkassel, Linz, Unkel und Asbach, von den ersten Brüchen am Rhein bis zum Naturschutzgebiet Siebengebirge. Gemeinfreie geologische Beschreibungen, Petitionen, Landtagsverhandlungen, Handelskammerberichte und Zeitschriften von 1824 bis 1923, in der Schreibung der Drucke, mit Anmerkungen, eine Zeitleiste mit Verweisen in die Texte und eine Liste dessen, was geprüft und nicht aufgenommen wurde. Das 20. Jahrhundert nach 1923 steht als Ausblick nach der neueren Literatur.

These, an den Texten zu prüfen: 1861 lagen an den Basaltbergen des Siebengebirges noch „keine bedeutende Steinbrüche“ (von Dechen); 1887 berichtete das Abgeordnetenhaus, „am Weilberg habe ein Bruch die Kuppe bereits gespalten“. Der Schutz der Berge kam spät, kostete viel Geld und nahm Tausenden die Arbeit; die Brüche wichen in den Westerwald aus.

Stufe 1 (in Arbeit), acht Module: siehe `data/modules.json`.

## Prüfen

```
python tools/verify.py
```

Das Begleitspiel *Die Kuppe bereits gespalten* (zwei Rollen: der Verschönerungsverein und ein Bruchbesitzer) ist in Vorbereitung: https://github.com/pantaleonfassbender-coder/Die-Kuppe-bereits-gespalten

Code MIT; Editionen CC0; redaktionelle Texte CC BY 4.0 (siehe `LICENSES.md`).
""", encoding="utf-8")
print("ok")
