"""Download and scale plate images into assets/plates/<id>.jpg and <id>_t.jpg.

    python tools/make-plates.py            # all plates listed below
    python tools/make-plates.py roswitha1501

Commons files are fetched as 1400-pixel renderings via the API; Internet
Archive page images are fetched directly and cropped (box in per mille).
"""
import io
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "assets" / "plates"
UA = {"User-Agent": "Mozilla/5.0 (research; Basalt zwischen Siebengebirge und Westerwald; pantaleonfassbender@gmail.com)"}

PLATES = {
    # Modul 1 (MDZ: Goethe 1824 bsb11942387; von Dechen 1861 bsb10012770)
    "goethe1824_s125": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb11942387_00099/full/1400,/0/default.jpg", (60, 340, 960, 960)),
    "dechen1861_s146": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb10012770_00158/full/1400,/0/default.jpg", None),
    "horner1836": ("commons", "File:Siebengebirge Horner 1836.jpg", None),
    "zehler1837": ("commons", "File:Geologische Karte des Siebengebirges von Johann Gottfried Zehler (1837).jpg", None),
    # Modul 5 (MDZ: Heusler 1897 bsb11797725; Fabrikaufsicht 1880 bsb11889174, 1883 bsb11558614, 1884 bsb11558615;
    # Dietrich 1885 bsb11466902; Soziale Praxis 9 bsb12048315; Rijksmuseum, Album der Basalt-Maatschappij, CC0)
    "heusler1897_tab": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb11797725_00226/full/1400,/0/default.jpg", (120, 102, 949, 755)),
    "fa1880_s214": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb11889174_00250/full/1400,/0/default.jpg", (170, 386, 982, 779)),
    "fa1883_s259": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb11558614_00287/full/1400,/0/default.jpg", (42, 305, 884, 664)),
    "fa1884_s174": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb11558615_00194/full/1400,/0/default.jpg", (130, 27, 963, 272)),
    "dietrich1885_fig43": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb11466902_00154/full/full/0/default.jpg", (180, 95, 540, 442)),
    "sp1900_linz": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb12048315_00340/full/full/0/default.jpg", (505, 588, 955, 925)),
    "rm_wilscheiderberg": ("commons", "File:Gezicht op de basaltgroeve Wilscheiderberg in Noord-Rijnland-Westfalen, Duitsland, RP-F-00-5356-11.jpg", (180, 253, 732, 753)),
    "rm_naak": ("commons", "File:Gezicht op een basaltgroeve, vermoedelijk in Duitsland, RP-F-00-5356-17.jpg", (177, 248, 740, 758)),
    # Modul 4 (Rijksmuseum, Album der Basalt-Maatschappij, CC0)
    "rm_minderberg": ("commons", "File:Gezicht op een basaltgroeve in de Minderberg in Rijnland-Palts, Duitsland, RP-F-00-5356-15.jpg", (160, 215, 770, 830)),
    "rm_dattenberg": ("commons", "File:Gezicht op een basaltgroeve in Dattenberg, Duitsland, RP-F-00-5356-21.jpg", (160, 215, 770, 830)),
    "rm_papendrecht": ("commons", "File:Plaats om te lossen aan de rivier van de Basalt-Maatschappij in Papendrecht, RP-F-00-5356-14.jpg", (160, 215, 770, 830)),
    "rm_borrendamme": ("commons", "File:Twee mannen leggen zeewering aan bij Borrendamme op Schouwen-Duiveland, RP-F-00-5356-18.jpg", (160, 215, 770, 830)),
    "rm_westkapelle": ("commons", "File:Gezicht op een zeewering bij Westkapelle op Walcheren, RP-F-00-5356-12.jpg", (160, 215, 770, 830)),
    "rm_album": ("commons", "File:Fotoalbum van de Basalt-Maatschappij Rotterdam met 21 foto's, RP-F-00-5356.jpg", None),
    # Modul 3 (MDZ: Baedeker 1888 bsb11533145; Über Land und Meer 1867 bsb10498523; Dietrich 1885 bsb11466902)
    "baedeker1888_karte": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb11533145_00512/full/1400,/0/default.jpg", None),
    "hoeller1867_bild": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb10498523_00016/full/1400,/0/default.jpg", (95, 75, 905, 950), 90),
    "dietrich1885_seilbahn": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb11466902_00149/full/1400,/0/default.jpg", None),
    # Modul 2 (MDZ: Nöggerath 1847 bsb10226264)
    "n1847_titel": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb10226264_00005/full/1400,/0/default.jpg", None),
    "n1847_herkules": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb10226264_00073/full/1400,/0/default.jpg", (100, 580, 310, 895)),
    "n1847_taf3a": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb10226264_00073/full/1400,/0/default.jpg", (55, 80, 870, 395)),
    "n1847_taf4": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb10226264_00075/full/1400,/0/default.jpg", None),
    "n1847_taf5": ("ia", "https://api.digitale-sammlungen.de/iiif/image/v2/bsb10226264_00077/full/1400,/0/default.jpg", None),
    "noeggerath1838": ("commons", "File:Orographische Karte des Siebengebirges bei Bonn... - von... Dr Noeggerath... - btv1b84687330.jpg", None),
}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()


def commons_url(title):
    q = urllib.parse.urlencode({"action": "query", "titles": title, "prop": "imageinfo",
                                "iiprop": "url", "iiurlwidth": 1400, "format": "json"})
    data = json.loads(get("https://commons.wikimedia.org/w/api.php?" + q))
    page = next(iter(data["query"]["pages"].values()))
    return page["imageinfo"][0]["thumburl"]


def make(pid):
    kind, src, box, *rot = PLATES[pid]
    im = Image.open(io.BytesIO(get(commons_url(src) if kind == "commons" else src))).convert("RGB")
    if box:
        W, H = im.size
        im = im.crop((W * box[0] // 1000, H * box[1] // 1000, W * box[2] // 1000, H * box[3] // 1000))
    if rot:
        im = im.rotate(rot[0], expand=True)
    big = im.copy()
    big.thumbnail((1400, 1600))
    big.save(DEST / f"{pid}.jpg", quality=85, optimize=True)
    t = im.copy()
    t.thumbnail((360, 480))
    t.save(DEST / f"{pid}_t.jpg", quality=82, optimize=True)
    print(pid, big.size, t.size)


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    for pid in sys.argv[1:] or PLATES:
        make(pid)
