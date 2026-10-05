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
    kind, src, box = PLATES[pid]
    im = Image.open(io.BytesIO(get(commons_url(src) if kind == "commons" else src))).convert("RGB")
    if box:
        W, H = im.size
        im = im.crop((W * box[0] // 1000, H * box[1] // 1000, W * box[2] // 1000, H * box[3] // 1000))
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
