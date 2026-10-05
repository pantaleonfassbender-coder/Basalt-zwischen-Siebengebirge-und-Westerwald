"""Schreibt die Gerüst-Daten des Apparats (geplante Module, Zeitleiste, leere Vergleiche und Tafeln).
Einmalig beim Anlegen benutzt; danach werden die Dateien von den Modul-Skripten gepflegt.
Aufruf aus dem Wurzelverzeichnis: python tools/geruest-daten.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def W(p, o):
    (ROOT / p).write_text(json.dumps(o, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


L = "(Nach der neueren Literatur; Modul geplant.)"
M = "(Modul geplant.)"

mods = {"shipped": [], "planned": [
    {"id": "stein", "side": "stein", "kurz": "Der Stein, 1824–1861",
     "warum": "Was Basalt ist, wo er ansteht und wie er bricht: Nöggerath und Goethe am Rückersberg bei Oberkassel 1824, die geologischen Karten, und von Dechens Befund von 1861, dass an den Basaltbergen des Siebengebirges noch keine bedeutenden Brüche lagen.",
     "quelle": "Goethe, Zur Naturwissenschaft II,2 (1824); H. von Dechen, Geognostischer Führer in das Siebengebirge (1861) (Bayerische Staatsbibliothek)."},
    {"id": "unkel", "side": "bruch", "kurz": "Unkel 1846",
     "warum": "Am 20. Dezember 1846 geriet der Unkelstein, eine Basaltkuppe am linken Rheinufer bei Oberwinter, in Bewegung, weil die Unkeler Brüche ihm den Halt genommen hatten. Dazu der Unkeler Säulenbasalt im Fundament des Kölner Doms.",
     "quelle": "J. Nöggerath, Der Bergschlüpf vom 20. Dec. 1846 an den Unkeler Basaltsteinbrüchen (1847); Zeitungsmeldung Dezember 1846; A. von Lasaulx, Die Bausteine des Kölner Domes (1882)."},
    {"id": "aufschwung", "side": "bruch", "kurz": "Der Aufschwung am Siebengebirge, 1861–1890",
     "warum": "Petersberg seit 1866, Ölberg seit 1872, Weilberg: Pflaster für die Rheinstädte, Seilbahnen, die rechtsrheinische Bahn und die Heisterbacher Talbahn.",
     "quelle": "Über Land und Meer (1867); Der Berggeist (1872); E. Dietrich, Die Baumaterialien der Steinstrassen (1885); Rheinische Geschichtsblätter (1896/97)."},
    {"id": "holland", "side": "bruch", "kurz": "Nach Holland",
     "warum": "Säulen für Deiche und Ufer, Kopfsteine, Senksteine; die Basalt-Actien-Gesellschaft mit niederländischem Kapital in Linz; das Syndikat von 1893; der Westerwald als Konkurrent im Tarifstreit.",
     "quelle": "Jahresberichte der Handelskammer zu Bonn (1895–1898); Saling's Börsen-Jahrbuch (1897); Verhandlungen des Landeseisenbahnrats (1888, 1893); Deutsche Industrie-Zeitung (1888)."},
    {"id": "arbeit", "side": "arbeit", "kurz": "Die Arbeit",
     "warum": "Steinhauer, Kleinschläger, Pflastersteinkipper, Fuhrleute und Schiffer: 1894 arbeiteten in 75 Basaltbrüchen 3817 Menschen, umgerechnet 1567 volle Arbeitsjahre. Akkord, Saison, Unfälle, die italienischen Arbeiter seit 1898.",
     "quelle": "C. Heusler, Beschreibung des Bergreviers Brühl–Unkel (1897); Soziale Praxis 9 (1899/1900)."},
    {"id": "raubbau", "side": "schutz", "kurz": "„Raubbau“, 1836–1899",
     "warum": "Vom Ankauf des Drachenfels 1836 über den Verschönerungsverein von 1869 und den Verein zur Rettung des Siebengebirges 1886 bis zur Petition von 1887 und zur Lotterie mit Enteignungsrecht 1899. Die Provinz besaß selbst einen Bruch am Petersberg.",
     "quelle": "Verhandlungen des Rheinischen Provinziallandtags (1886, 1899); Haus der Abgeordneten, Aktenstück Nr. 154 (1887); Die Grenzboten (1897); Rheinische Geschichtsblätter (1898/99)."},
    {"id": "verordnung", "side": "arbeit", "kurz": "Die Verordnung und die Arbeiter, 1899–1914",
     "warum": "Die Polizeiverordnung vom 26. Oktober 1899 verbot neue Brüche im Schutzgebiet; Arbeiter und Bruchbesitzer wehrten sich gemeinsam, Löhne sanken, Arbeiter wanderten ab, und die Brüche wichen an den Rand und in den Westerwald aus.",
     "quelle": "Soziale Praxis 9 (1899/1900); Zeitung des Vereins Deutscher Eisenbahnverwaltungen (1900); Reichstag (1906)."},
    {"id": "schutzgebiet", "side": "staat", "kurz": "Das Schutzgebiet, 1914–1923",
     "warum": "Krieg, Kriegsgefangene in den Brüchen und die Verordnung über das Naturschutzgebiet Siebengebirge, eines der ersten in Deutschland; mit einem Ausblick auf die Brüche, die bis heute arbeiten.",
     "quelle": "Amtliche Bekanntmachungen (Sichtung offen); neuere Literatur für die Kriegsjahre."}],
    "missing": [
    {"id": "laspeyres", "side": "stein", "kurz": "H. Laspeyres, Das Siebengebirge am Rhein (1901)",
     "warum": "Die große Gesamtdarstellung der Zeit, gemeinfrei, aber in den erreichbaren Digitalisaten nur hinter einer Botprüfung, die dieser Apparat nicht umgeht. Wird aufgenommen, sobald ein offenes Digitalisat gefunden ist.",
     "quelle": "Verhandlungen des Naturhistorischen Vereins der preußischen Rheinlande und Westfalens 57 (1900/01)."},
    {"id": "archive", "side": "staat", "kurz": "Akten der Gemeinden, Kreise und des Vereins",
     "warum": "Konzessionen, Polizeiverordnungen, Kaufverträge, Unfallanzeigen und Eingaben liegen in den Stadtarchiven Königswinter und Linz, im Kreisarchiv Siegburg, im Landeshauptarchiv Koblenz (Bestand 475, Landratsamt Neuwied) und im Archiv des Verschönerungsvereins. Unveröffentlicht; nur mit Zustimmung der Archive.",
     "quelle": "Siehe die genannten Archive."},
    {"id": "zeitungen", "side": "arbeit", "kurz": "Die Lokalzeitungen",
     "warum": "Lokalzeitungen in Königswinter, Honnef und Bonn berichteten über Unfälle, Streiks und Ankäufe. Die Zeitungsportale des Landes sind von hier aus nicht erreichbar.",
     "quelle": "zeitpunkt.nrw; ULB Bonn."},
    {"id": "literatur", "side": "schutz", "kurz": "Die neuere Literatur",
     "warum": "Ortschroniken und Darstellungen zum Steinbruchwesen, zum Verschönerungsverein und zum Naturschutzgebiet sind die gründlichsten Quellen für Daten und Namen, aber urheberrechtlich geschützt. Der Apparat nennt sie, wo er ihnen Daten entnimmt, und druckt nichts daraus ab.",
     "quelle": "u. a. W. Schmidt, Die Strüch. Eine Chronik von Thomasberg; F. Berres u. a. (Hg.), Gesteine des Siebengebirges (1996); Th. Hardenberg; C. Gussmann/W. Clößner, Die Heisterbacher Talbahn (2006)."}]}
W("data/modules.json", mods)

st = [
    ("1824", "stein", "Der Rückersberg", "Goethe druckt in seinen Heften zur Naturwissenschaft Nöggeraths Beschreibung der Basaltsteinbrüche am Rückersberg bei Oberkassel. " + M),
    ("1827–1836", "schutz", "Der Drachenfels", "Die Königswinterer Steinhauergewerkschaft kauft 1827 die Kuppe des Drachenfels; 1828 verbietet die Regierung den Bruch an der Ruine; 1836 erwirbt der Staat den oberen Berg. Trachyt, nicht Basalt: die Vorgeschichte des Schutzes. " + M),
    ("20. Dezember 1846", "bruch", "Der Unkelstein", "Der Unkelstein, eine Basaltkuppe am linken Rheinufer bei Oberwinter, gegenüber von Unkel, gerät in Bewegung, weil die Brüche ihr den Halt genommen haben; die Straße zwischen Oberwinter und Remagen wird unfahrbar. " + M),
    ("1861", "stein", "Keine bedeutenden Brüche", "Von Dechen findet an den Basaltbergen des eigentlichen Siebengebirges noch keine bedeutenden Steinbrüche; große Brüche liegen bei Oberkassel, Erpel, Linz und Unkel. " + M),
    ("1866", "bruch", "Der Petersberg", "An der Nordseite des Petersbergs beginnt ein Basaltbruch (nach der Petition von 1887). " + M),
    ("1869", "schutz", "Der Verschönerungsverein", "Gründung des Verschönerungsvereins für das Siebengebirge in Bonn; 1870 wird Heinrich von Dechen sein Präsident. " + L),
    ("1872", "bruch", "Der Ölberg", "Am Ölberg beginnt ein Basaltbruch; im selben Jahr stehen die Brüche des Siebengebirges „im lebhaftesten Betriebe“ und liefern Pflaster in alle Rheinstädte. " + L),
    ("1886", "schutz", "Der Verein zur Rettung", "Im Sommer entsteht der Verein zur Rettung des Siebengebirges; der Rheinische Provinziallandtag lehnt seine Bitte ab, auch den eigenen Bruch der Provinz am Petersberg einzustellen. " + M),
    ("1887", "schutz", "Die Petition", "Das Abgeordnetenhaus berät die Petition: „am Weilberg habe ein Bruch die Kuppe bereits gespalten“. " + M),
    ("1888", "bruch", "Linz und Holland", "Die Basalt-Actien-Gesellschaft wird eingetragen, mit niederländischem Kapital, ab 1892 mit Sitz in Linz. Holland will bei öffentlichen Bauten nur noch Backstein zulassen; der Westerwald bittet vergeblich um einen Tarif zum Rhein. " + M),
    ("1891", "bruch", "Die Heisterbacher Talbahn", "Eine Schmalspurbahn von Niederdollendorf nach Heisterbacherrott bringt Steine an den Rhein. " + L),
    ("1893–1896", "bruch", "Der Basaltverein", "Ein Syndikat der Bruchbesitzer, das nach drei Jahren wieder aufgelöst wird. " + M),
    ("1894", "arbeit", "3817 Menschen", "In 75 Basaltbrüchen des Reviers Brühl–Unkel arbeiten 3817 Menschen, umgerechnet 1567 volle Arbeitsjahre. " + M),
    ("Herbst 1898", "arbeit", "Italienische Arbeiter", "Im Linzer Revier werden italienische Arbeiter angeworben; die Einheimischen fürchten um ihre Löhne. " + M),
    ("1899", "schutz", "Lotterie und Enteignung", "Provinz, Köln und Bonn geben 350 000 Mark; der Verschönerungsverein erhält eine Lotterie und das Enteignungsrecht. Am 26. Oktober verbietet eine Polizeiverordnung neue Brüche im Schutzgebiet. " + M),
    ("1900", "arbeit", "Die Steinarbeiter organisieren sich", "Christlich-soziale Steinarbeiterverbände am Siebengebirge, mit einer Zentrale in Honnef; Arbeiter und Bruchbesitzer wehren sich gemeinsam gegen die Verordnung. " + M),
    ("1906", "bruch", "Schwedische Pflastersteine", "Im Reichstag wird geklagt, zollfreie Pflastersteine aus Schweden drückten auf die rheinische Basaltindustrie. " + M),
    ("1922 oder 1923", "staat", "Das Naturschutzgebiet", "Das Siebengebirge wird Naturschutzgebiet; genannt werden der 7. Juni 1922 und der 20. Januar 1923. " + L),
    ("Ausblick", "staat", "Bis heute", "Der Basaltbruch am Hühnerberg bei Eudenbach arbeitet bis heute. (Nach der neueren Literatur.)"),
]
W("data/timeline.json", {"lede": "Von den ersten Brüchen am Rhein bis zum Naturschutzgebiet, mit einem Ausblick. Wo noch kein Text abgedruckt ist, sagen die Stationen, woher ihre Angaben stammen; wo die Angaben sich widersprechen, stehen beide.",
                         "stations": [{"d": d, "side": s, "titel": t, "text": x} for d, s, t, x in st]})
W("data/compare.json", {"lede": "Derselbe Berg in verschiedenen Stimmen: Verein, Bruchbesitzer, Arbeiter, Behörde, Reisende.", "pairs": []})
W("data/plates.json", {"lede": "Karten, Ansichten und Photographien aus gemeinfreien Vorlagen.",
                       "credit": "Die Tafeln stammen aus gemeinfreien oder CC0-Reproduktionen (Wikimedia Commons, Rijksmuseum); jede nennt ihre Herkunft.", "plates": []})
print("ok")
