"""Trägt ein fertiges Modul ein: verschiebt es in modules.json von „planned“ nach „shipped“,
ergänzt seine Tafeln in plates.json und setzt Verweise der Zeitleiste.
Die Angaben je Modul stehen unten in MODS. Aufruf: python tools/register.py stein
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data"
load = lambda f: json.load(open(D / f, encoding="utf-8"))


def save(f, o):
    (D / f).write_text(json.dumps(o, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


MODS = {
    "stein": {
        "plates": [
            {"id": "goethe1824_s125", "side": "stein", "titel": "„Die Basaltsteinbrüche am Rückersberge bey Oberkassel“, 1824",
             "caption": "Der Anfang des Beitrags in Goethes Heften „Zur Naturwissenschaft“: Nöggeraths Beschreibung eines Steinbruchs bei Oberkassel, mit Goethes Einleitung (Rückersberg [1]).",
             "source": "Goethe (Hg.), Zur Naturwissenschaft überhaupt II,2 (1824), S. 125; Bayerische Staatsbibliothek, bsb11942387, Bild 99 (Ausschnitt)."},
            {"id": "horner1836", "side": "stein", "titel": "Leonard Horner, Environs of Bonn, 1836",
             "caption": "Die erste geologische Karte des Siebengebirges, von dem schottischen Geologen Leonard Horner (1785–1864), mit Bonn, Rhein und Siebengebirge.",
             "source": "Transactions of the Geological Society of London, 2nd series, 4 (1836), Taf. XXIX; Wikimedia Commons, gemeinfrei."},
            {"id": "dechen1861_s146", "side": "stein", "titel": "„Höhen der Basaltberge“, 1861",
             "caption": "Die erste Seite von Heinrich von Dechens Tabelle der Basaltberge: Großer Ölberg, Löwenburg, Asberg, Hummelsberg, Minderberg und weitere, in Pariser Fuß (Kuppen [2]).",
             "source": "H. von Dechen, Geognostischer Führer in das Siebengebirge (Bonn 1861), S. 146; Bayerische Staatsbibliothek, bsb10012770, Bild 158."},
            {"id": "noeggerath1838", "side": "stein", "titel": "Nöggerath, Orographische Karte des Siebengebirges, 1838",
             "caption": "Die Berge des Siebengebirges als Relief, herausgegeben von Johann Jacob Nöggerath (1788–1877) in Bonn: der Zustand vor dem großen Abbau.",
             "source": "Bonn: Henry & Cohen 1838; Bibliothèque nationale de France, über Wikimedia Commons, gemeinfrei."},
            {"id": "zehler1837", "side": "stein", "titel": "Zehler, Geologische Karte des Siebengebirges, 1837",
             "caption": "Basalt, Trachyt und Konglomerat im Siebengebirge, nach Johann Gottfried Zehler (1811–1873).",
             "source": "J. G. Zehler, Das Siebengebirge und seine Umgebungen (Crefeld 1837); Wikimedia Commons, gemeinfrei."},
        ],
        "zk": "Rückersberg · Kuppen · Säulen",
        "timeline": {"1824": ("#/text/stein/rueckersberg/1", "Rückersberg [1]", "goethe1824_s125"),
                     "1861": ("#/text/stein/saeulen/1", "Säulen [1]", "dechen1861_s146")},
    },
}


def main(mid):
    spec = MODS[mid]
    mods = load("modules.json")
    entry = next((m for m in mods["planned"] if m["id"] == mid), None)
    if entry:
        mods["planned"].remove(entry)
        entry["datei"] = mid
        entry["zk"] = spec["zk"]
        mods["shipped"].append(entry)
        save("modules.json", mods)
    plates = load("plates.json")
    have = {p["id"] for p in plates["plates"]}
    for p in spec["plates"]:
        if p["id"] not in have:
            plates["plates"].append(p)
    save("plates.json", plates)
    tl = load("timeline.json")
    for st in tl["stations"]:
        if st["d"] in spec["timeline"]:
            st["cite"], st["citeLabel"], st["plate"] = spec["timeline"][st["d"]]
            st["text"] = st["text"].replace(" (Modul geplant.)", "")
    save("timeline.json", tl)
    print("ok", mid)


if __name__ == "__main__":
    main(sys.argv[1])
