"""Modul 1: Der Stein, 1824–1861. Schreibt data/stein.json.

Alle Stellen am Seitenbild gelesen, in den Digitalisaten der Bayerischen Staatsbibliothek
(digitale-sammlungen.de; Bildnummer in Klammern):
- Goethe (Hg.), Zur Naturwissenschaft überhaupt, besonders zur Morphologie II,2 (Stuttgart und
  Tübingen 1824), S. 125–132: „Die Basaltsteinbrüche am Rückersberge bey Oberkassel am Rhein.
  Aus Nöggeraths: das Gebirg in Rheinland-Westphalen“ (bsb11942387, Bild 99–106).
- H. von Dechen, Geognostischer Führer in das Siebengebirge am Rhein (Bonn 1861), S. 145–147
  und 162–163 (bsb10012770, Bild 157–159 und 174–175).
Schreibung und Zeichensetzung der Drucke; ſ als s; Silbentrennung aufgelöst; Sperrungen und
Kursive nicht wiedergegeben; Auslassungen […]; im Druck fehlende Buchstaben in [ ].
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "stein.json"


def u(n, pg, titel, orig, note=""):
    d = {"n": n, "pg": pg, "titel": titel, "orig": orig.strip()}
    if note:
        d["note"] = note
    return d


RUECKERSBERG = [
    u(1, "Goethe 1824, S. 125–126", "Goethe: „in der Finsterniß … eines Steinbruchs“",
      """Die Basaltsteinbrüche am Rückersberge bey Oberkassel am Rhein.
Aus Nöggeraths: das Gebirg in Rheinland-Westphalen, nach mineralogischem und chemischem Bezuge. 2 Band. S. 250 ff.

Diese Beschreibung eines merkwürdigen Steinbruchs, der uns in das Innere einer beziehungsvollen Basaltbildung hineinblicken läßt, hat so viel Anziehendes, daß wir sie grö[ßten]theils mit den eigenen Worten des anschauungs- [u]nd erwägungsreichen Verfassers aus dem neuesten [B]ande seines lehrreichen Werkes ausziehen und hier mittheilen wollen. Während wir so auf die leichteste Weise um den Dank unserer Leser zu werben scheinen, dürfen wir nicht verschweigen, wie uns der freundlich gesinnte Verfasser selbst noch einen Schritt weiter gefördert hat, als er in der gedachten Schrift, den in solchen Forschungen geübtesten Leser im Auge, der Darstellung angemessen fand. Es ist nämlich in der Geognosie dem menschlichen Geist eine herrliche Pflegerin fortbildender Anschauung eröffnet, die sich bey manchen wahrhaft berufenen Beobachtern oft zu einer wundersamen Höhe steigert und sie in dem naturgemäßesten Sinne fernsehend macht. An einer kleinen abgerissenen Stelle eines Gehänges, in der Finsterniß einer engen Kluft, eines Steinbruchs, eines Bergwerks, sehen sie Schichtungen und Gänge des Gebirgs weit nach allen Himmelsgegenden hin streichen und fallen, ahnen den Ausgang einer Formation, oder erkennen jenseits eines weiten Thals ihren durch einen Strom unterbrochenen Fortgang, daß ein Dritter, dem dergleichen Gabe und Uebung nicht verliehen wurde, sich darüber wohl verwundern könnte. Es ist dann erfreulich, in der idealen Darstellung der Fortgangslinien, nach welchen der Geognost im Geiste seinen Gegenstand von dem Puncte der Beobachtung aus weiter verfolgt, eine Stütze der Anschauung zu erhalten, und darum müssen wir es unserm Freunde Dank wissen, daß er uns, zur Erläuterung seiner naturgetreuen Schilderung und Abbildung des gedachten Steinbruchs, noch mit einer solchen idealen Zeichnung des ganzen Zusammenhangs, zu dessen Erkenntniß die Betrachtung dieses Fragments Anleitung giebt, versehen wollte. […]""",
      "Goethe gab seine Hefte „Zur Naturwissenschaft überhaupt“ selbst heraus; die Einleitung ist ungezeichnet und stammt wohl von ihm als Herausgeber. Er druckt Johann Jacob Nöggeraths Beschreibung eines Steinbruchs am Rückersberg bei Oberkassel nach, aus dessen Werk über das Gebirge in Rheinland-Westfalen (Bd. 2, 1823). Am Anfang der Geschichte steht also kein Streit, sondern Neugier: Der Steinbruch ist für die Geologen ein Fenster ins Innere des Berges. „Geognosie“ ist die ältere Bezeichnung der Geologie. Im Druck sind einige Buchstaben ausgefallen; sie stehen in eckigen Klammern."),
    u(2, "Goethe 1824, S. 126–128", "„so große und ausgezeichnete Dinge dieser Art“",
      """Die Darstellung rheinischer Basalt-Berge ist selbst nach Breislaks, der Physiognomik des Basalts ausschließlich gewidmetem Atlas*) noch keineswegs entbehrlich geworden, da dieser (auf Tafel 26.) nur ein einziges Bild eines rheinischen Basaltbergs, des sogenannten Unkeler Steinbruchs bey Oberwinter, und zwar nach einem „beyspiellos schlechten, vor beynahe einem halben Jahrhunderte gefertigten Originale,“ liefert, in welchem man kaum eine flüchtige Aehnlichkeit mit dem Umrisse des Bruchs, aber auch nicht einmal eine Vergleichbarkeit mit dem wirklichen Vorkommen des Basalts in demselben, erkennen kann.

„Und doch bieten die Rheingegenden so große und ausgezeichnete Dinge dieser Art, wie vielleicht wenig andere Länder, worauf die Aufmerksamkeit der Gebirgsforscher früher und fortdauernder gerichtet war. Die concentrisch-schaaligen, kugelförmigen Bildungen am Rückersberge bey Oberkassel, die aus plattgedrückten Sphäroiden zusammengesetzten Säulen in dem sogenannten Käsekeller bey Bertrich, haben erstere an Größe des Gebildes, letztere selbst in ihrer Art, wohl nirgendwo bekannte Analogien; die vollkommenen Säulenbildungen am Mendeberge bey Linz brauchen rücksichtlich ihrer schlanken Taille und ihrer Größe keinem andern ähnlichen exotischen Vorkommen nachzustehen, und die gegliederten Säulen in der Felsenhöhle bey der Kapelle auf der Landskrone am Ahrflusse sind wohl eben so ausgezeichnet, wie jene am Riesendamm in Irland.“

*) Atlas géologique, ou vues d'amas de colonnes basaltiques faisant suite aux Institutions Géologiques de Scipion Breislak. Milan 1818. Quer Fol.""",
      "Die Stellen in Anführungszeichen sind Nöggeraths eigene Worte; den Rest spricht der Herausgeber. Der Basalt des Rheins steht hier in einer Reihe mit dem Riesendamm (Giant's Causeway) in Irland, dem berühmtesten Säulenbasalt Europas. Der „Mendeberg bey Linz“ ist der Minderberg, an dem später einer der großen Brüche der Basalt-Actien-Gesellschaft lag. Der Unkeler Steinbruch bei Oberwinter, dessen Bild der Druck tadelt, ist der Bruch am Unkelstein, der 1846 ins Rutschen kam (Kuppen [1])."),
    u(3, "Goethe 1824, S. 128–129", "„entblößte Stellen an dem dicht bewaldeten Gehänge“",
      """So eröffnet uns denn der Herr Verfasser eine willkommene Gallerie rheinischer Basaltberge und Steinbrüche mit der von Herrn Bergrath Senff sehr geschickt aufgenommenen, auch sauber in Stein gedruckten Zeichnung des Basaltvorkommens in dem oben erwähnten Steinbruch am Rückersberge bey Oberkassel.

„Nördlich von den höhern Basalt- und Domit-Kegeln, welche das eigentliche Siebengebirge konstituiren, werden die aus dem Gebirge kommenden und sich nach dem Rheine hin öffnenden, also mehr oder weniger von Osten nach Westen streichenden, Thäler immer seltener, oder sie schneiden doch weniger tief ein; die Berge werden dadurch, zugleich bey fortwährend abnehmender Höhe, mehr langgezogen rückenartig und verlaufen sich mit ihrem Fuße in die Ebene. Ein solcher Rücken zieht sich fast parallel dem Rheine, in beyläufig viertelstündiger Entfernung von demselben ab, längst dem Dorfe Oberkassel vorbey bis nach Ramersdorf, wo er durch ein Thal, doch nicht völlig, von der übrigen noch mehr nördlichen Bergmasse gesondert ist. Der mehr südlich gelegene Theil dieses Rückens ist 438 Fuß über dem Rheinspiegel hoch, und führt den Namen Kasseler Ley, der mehr nördliche, 320 Fuß hohe Theil ist dagegen unter dem Namen des Rückersberges bekannt.

Basalt bildet die Masse dieses ganzen Rückens, dessen Hauptgehänge nach Westen, nach dem Rheinthale, hin gerichtet ist. Am obern Theile des Gehänges gehen die Felsen als steile Bergwände zu Tage aus, der untere Theil hat eine mäßige Abdachung. Sowohl an der sogenannten Kasseler Ley als am Rückersberge findet sich eine große Anzahl Steinbrüche, welche meist erst im letzten Decennium angelegt worden sind, und insbesondere Material zum Festungsbau und zum Straßenpflaster der benachbarten Städte liefern. Bey der Schifffahrt auf dem Rheine oder vom linken Ufer des Flusses aus, gewahrt man diese Steinbrüche schon in bedeutender Ferne; sie geben sich durch entblößte Stellen an dem dicht bewaldeten Gehänge deutlich zu erkennen. Auf Taf. I. liefern wir ein Bild des am höchsten auf dem Rückersberger Gehänge gelegenen Steinbruchs, welcher dem Fürsten zu Salm-Dyck zugehört und im Rauchloche genannt wird.

Die Entblößung, wie sie das Bild darstellt, bietet eine senkrechte Wand dar, welche 70–80 Fuß hoch seyn mag. Der Zeichner hat seine Stellung ungefähr 10–15 Schritt von derselben, in der Nähe eines großen Haufens von Steinbruchsschutt, welcher zum Theil links auf dem Bilde im Vorgrunde erscheint, genommen. […]“""",
      "Die früheste Stelle des Apparats über Brüche am Siebengebirge. Die Brüche an der Kasseler Ley und am Rückersberg sind 1823 meist erst im letzten Jahrzehnt angelegt worden; sie liefern Steine für den Festungsbau, wohl für die preußischen Festungen am Rhein, und Pflaster für die Städte. Schon jetzt sieht man sie vom Schiff aus als kahle Stellen im Wald. Der Bruch „im Rauchloche“ gehört einem Fürsten, Joseph zu Salm-Reifferscheidt-Dyck; Besitzer der Berge sind Grundherren, nicht der Staat. „Domit“ hieß damals der Trachyt des Siebengebirges. Die Lithographie von Senff (Taf. I) ist in den erreichbaren Digitalisaten nicht lesbar erfasst; der Apparat zeigt sie deshalb nicht."),
    u(4, "Goethe 1824, S. 131–132", "„fast noch einmal so hoch“",
      """Kann man bey einem solchen Verhalten der Haupt-Absonderungen in der ganzen Basaltmasse des Rückersbergs wohl annehmen, daß die erwähnten kugelsegmentartigen Gebilde selbständig sind oder hat es nicht viel mehr für sich, solche bloß als Theile einer enorm-großen Kugel oder vielmehr ellipsoidischen Bildung, welche im Großen der ganzen Masse des Bergrückens zukömmt, zu betrachten? Wir glauben, daß dieser letztern Ansicht jeder Beobachter zugethan seyn wird, der die sämmtlichen Steinbrüche des Gehänges rücksichtlich der Hauptabsonderungen genau untersucht und unter einander vergleicht. Aber das ist eine andere Frage: ob die ungeheuer große ellipsoidische Bildung in ihrem Ursprunge ganz vollkommen abgeschlossen und überall gerundet und nicht, wie sie jetzt erscheint, zerbrochen war? Eine genügende Antwort vermögen wir darauf nicht zu geben. War das Ellipsoid ursprünglich vollkommen, d. h. in sich selbst geschlossen, so ist das gegenwärtige Gehänge, welches das Ellipsoid nach einer Richtung schräg durchsetzt, und daher Blicke in das Innere des Gebildes und Beobachtungen über dessen Zusammenfügung verstattet, späterer Entstehung; und damit hängt auch die Annahme zusammen, daß der Bergrücken ursprünglich höher und sogar nothwendig fast noch einmal so hoch gewesen seyn mußte, als er gegenwärtig ist, weil die längste horizontale Achse des Ellipsoids, welche durch den Steinbruch am Rauchloche geht, nicht fern vom dermaligen Gipfel des Berges liegt. […] Am nördlichen Ende des Rückens mag wohl ebenfalls ein Stück des Ellipsoids, durch die spätere Abdachung und Thalbildung veranlaßt, fehlen, oder es setzt in einen andern vorliegenden Rücken, der Ennert genannt, noch über, welcher auch Basalt zur Masse hat, aber nicht durch Steinbrüche aufgeschlossen ist.""",
      "Nöggerath liest den Berg aus seinen Brüchen: Nur weil man an vielen Stellen des Hangs Stein bricht, kann er die riesige Kugelschale im Inneren erkennen. Der Steinbruch ist hier noch ein Werkzeug der Erkenntnis. Dass der Berg einst „fast noch einmal so hoch“ war, meint die Abtragung durch Wasser und Zeit, nicht durch Menschen; der Gedanke, dass Menschen einen Berg abtragen könnten, kommt erst sechzig Jahre später auf (siehe die Module zum Schutz des Gebirges). Ausgelassen ist eine Berechnung der Achsen des Ellipsoids."),
]

KUPPEN = [
    u(1, "von Dechen 1861, S. 145", "Unkel: „bereits von den Römern betrieben“",
      """Oberhalb Rolandseck kommt auf gleiche Weise Basalt am Heldenköpfchen und am Steinskopf am Gehänge des Rheinthals vor. Der letztere ist am Fusse des Abhanges durch einen Steinbruch und in dem Durchschnitt der Eisenbahn aufgeschlossen. Näher nach Oberwinter hin führt Nose noch zwei kleine Basaltvorkommen an. Oberhalb Oberwinter ist an der Burg ein kleiner Basaltpunkt bekannt, dann folgt der Basalt, welcher in den bekannten, bereits von den Römern betriebenen Unkeler Steinbrüchen aufgeschlossen ist. Derselbe steht in dem Rheinstrome selbst an, bildet hier den Unkelstein und erstreckt sich ziemlich hoch am Abhange hinauf, ist von der kleinen Basaltkuppe des Birgelerkopfes, welche den höchsten Theil dieses Abhanges einnimmt, durch Basalt-Konglomerat getrennt. Das erste Werk, welches Alexander von Humboldt*) bekannt gemacht hat, enthält eine ausführliche Beschreibung des Basaltvorkommens in den Unkeler Steinbrüchen.

Noeggerath**) hat einen hier stattgefundenen Bergschlipf ausführlich mit dem Vorkommen des Basaltes erläutert. […]

*) Mineralog. Beobachtungen über einige Basalte am Rhein. Braunschweig. 1790.
**) Der Bergschlipf vom 20. Dezember 1846. an den Unkeler Basalt-Steinbrüchen bei Oberwinter. Bonn. 1847.""",
      "Heinrich von Dechen (1800–1889), Berghauptmann und Geologe in Bonn, schrieb 1861 den Führer, mit dem man das Siebengebirge geologisch erwandern konnte. Die „Unkeler Steinbrüche“ liegen nicht in Unkel, sondern gegenüber am linken Ufer bei Oberwinter; der Basalt reicht dort bis in den Strom und bildet den Unkelstein, ein Felsriff für die Schiffer. Alexander von Humboldts erstes Buch (1790) beschrieb diese Brüche. Von Dechen nennt Nöggeraths Schrift über den Bergrutsch von 1846, der den Unkelstein in Bewegung brachte; ihr ist das nächste Modul gewidmet."),
    u(2, "von Dechen 1861, S. 146–147", "Höhen der Basaltberge",
      """Höhen der Basaltberge.
Die Höhen von mehreren dieser Basaltberge sind gemessen und sind die Angaben der bessern Uebersicht wegen hier zusammengestellt.

[Spalten: über dem Meere in Pariser Fuss · über dem mittleren Rheinspiegel bei Königswinter, Pariser Fuss · Höhen des Basaltes über der umgebenden Gebirgsart in Pariser Fuss]

1. Gr. Oelberg 1429. 1279. 133 üb. Trachyt.
2. Düstemich (Mehrberg) 1415. 1265.
3. Löwenburg 1413. 1263. 259 üb. Trachyt.
4. Dasberg 1369. 1219.
5. Asberg 1358. 1208. 259 üb. Devnsch.
6. Hummelsberg 1345. 1195. 245 üb. Devnsch.
7. Minderberg 1334. 1184. 285 üb. Devnsch.
8. Mahlberg 1209. 1059. 90 üb. Devnsch.
9. Ginsterhahn 1190. 1040.
10. In den Hülsen 1149. 999.
11. Erpeler Steinbüchel 1138. 988.
12. Linzer Steinbüchel 1134. 984.
13. Kl. Oelberg 1115. 965.
14. Leiberg 1073. 923. 303 üb. Devnsch.
15. Nonnenstromberg 1036. 886. 180 üb. Trachyt-Konglomerat.
16. Petersberg 1027. 877.
17. Höhnerberg 995. 845.
18. Scheidsburg 895. 745.
19. Landskrone 856. 706.
20. Wachtberg 820. 670.
21. Dollendorfer hardt 780. 630. 264 üb. Devnsch.
22. Sitzenbusch 749. 599.
23. Limberg 739. 589.
24. Gr. Weilberg 739. 589.
25. Tungberg 728. 578.
26. Himperich 721. 571.
27. Steinringsberg 706. 556.
28. Gr. Scharfenberg 703. 553. 139 üb. Trachyt-Konglomerat.
29. Hartenberg 691. 541. 97 üb. Trachyt-Konglomerat.
30. Falkenberg 679. 529.
31. Thomasberg 631. 481.
32. Erpeler Ley 625. 475. Bedeckung v. Gerölle.
33. Casseler Ley 616. 466.
34. Gudenauer Windmühle 603. 453. Bedeckung v. Gerölle.
35. Kl. Weilberg 594. 444.""",
      "Eine Tabelle als Bestandsaufnahme: 35 Basaltberge zwischen Ahr, Rhein und Westerwald, gemessen vor dem großen Abbau. Ein Pariser Fuß sind 32,5 Zentimeter; der Große Ölberg mit 1429 Fuß über dem Meer hat also rund 464 Meter. In der dritten Spalte steht, wie hoch der Basalt über das Gestein seiner Umgebung aufragt: über Trachyt, Trachyt-Konglomerat oder Devonschichten („Devnsch.“), die Schiefer des Westerwalds. Die Wiederholungszeichen des Drucks sind ausgeschrieben. Viele dieser Namen kehren in den folgenden Modulen wieder, als Brüche: Petersberg, Weilberg, Ölberg, Minderberg, Asberg, Hummelsberg, Erpeler Ley, Casseler Ley, Scharfenberg, Steinringsberg. Die Visualisierung zeigt die Tabelle als Profil."),
]

SAEULEN = [
    u(1, "von Dechen 1861, S. 162", "„keine bedeutende Steinbrüche“",
      """Absonderung des Basaltes.
An allen Stellen, wo der Basalt entblösst ist, zeigt derselbe eine auffallende Absonderung und zwar entweder in Säulen (Prismen) oder in Platten*). An den zum Siebengebirge selbst gehörenden Basaltbergen befinden sich keine bedeutende Steinbrüche. Die Erscheinungen dieser Absonderungen sind daher weniger bemerkbar; nur an dem Abhange nach dem Rheinthale hin von Obercassel bis zum Ennert liegen grössere Steinbrüche und in diesen sind auch recht merkwürdige Verhältnisse aufgeschlossen. Südlich vom Siebengebirge sind ganz besonders die Steinbrüche an der Erpeler Ley, am Minderberg, auf dem Sand zwischen Ockenfels und Ohlenberg, am Naak in der Kasbach, am Dattenberge, am Schwarzenberge von Leubsdorf geeignet, um diese Erscheinungen vollständig kennen zu lernen und auf der linken Seite des Rheines die Steinbrüche von Unkel, an der Scheidsburg bei Remagen, bei Rolandseck und Godesberg.

*) Dr. C. Vogel über die Absonderungsformen vulkanischer Gesteine im Siebengebirge und dessen Umgebungen. Mit 1 Tafel. Berlin. 1860.""",
      "Der Satz, mit dem dieser Apparat beginnt: 1861 gibt es an den Basaltbergen des eigentlichen Siebengebirges, also am Petersberg, Ölberg oder Weilberg, noch keine bedeutenden Steinbrüche. Gebrochen wird am Rand: bei Oberkassel, das zum Siebengebirge im weiteren Sinn gehört, und südlich davon bei Erpel, Linz und Unkel, wo später die Basalt-Actien-Gesellschaft ihre Brüche haben wird. Von Dechen nennt die Brüche, weil man in ihnen die Säulen am besten sieht; für den Geologen ist ein Bruch ein Aufschluss. Sechsundzwanzig Jahre später wird eine Petition von „Raubbau“ sprechen."),
    u(2, "von Dechen 1861, S. 163", "Säulen wie in einem Meiler",
      """Die das Plateau der Devonschichten überragenden Kegel, wie der Minderberg, die Scheidsburg, die Brüche auf dem Sand und am Dattenberg*), in grösserer Entfernung: der Bonnefelder Bruch und der Kiesemichkopf bei Horhausen bieten eine sehr regelmässige Stellung der Säulen dar, die, wie bei den Trachytbergen bereits erwähnt worden, eine meilerartige genannt werden kann. Die Säulen sind dabei öfter von sehr grosser Länge regelmässig mit glatten und graden Seitenflächen. Diese Stellung der Basaltsäulen scheint wohl bei den einzelnen Basaltbergen ganz allgemein oder wenigstens sehr häufig vorzukommen. Es sind nur wenige ausgezeichnete Beispiele derselben angeführt worden. Die Basaltpartieen, welche an dem Abhange des Rheinthales bis zur Sohle desselben durchschnitten sind, wie an der Erpeler Ley, in den Steinbrüchen von Unkel, am Rolandseck zeigen eine mannigfache Gruppirung von Säulen, in denen dieselben partieenweise eine sehr verschiedene Lage haben. Die einzelnen Partieen schliessen sich durch unregelmässig abgesonderte Massen an einander an. Auch sind wohl grössere Stücke auf diese Weise unregelmässig abgesondert, wie der obere Theil der Erpeler Ley, an dem steilen Abhange nach dem Rheinthale hin.

Die zusammenhängende Basaltpartie von Obercassel bis zum Finkenberge, einschliesslich des Jungfernberges, zeigt vorzugsweise eine plattenförmige Absonderung. Die Platten besitzen in der Regel nur die Stärke von einigen Zollen; liegen entweder horizontal oder besitzen doch nur eine geringe Neigung. […]

*) C. Vogel, a. a. O. S. 4 u. 5. Tab. II. 3.""",
      "Warum gerade dieser Stein so begehrt war: Die Säulen des Westerwaldrands stehen „meilerartig“, also schräg nach innen geneigt wie die Scheite eines Kohlenmeilers, und sind lang, glatt und gerade. Solche Säulen ließen sich als ganze Stücke brechen und verschiffen; in Holland wurden sie in Deichen und Ufern verbaut (Modul „Nach Holland“). Der Basalt bei Oberkassel bricht dagegen in dünnen Platten; daraus wurden Pflaster- und Mauersteine. Ein Zoll sind etwa 2,6 Zentimeter. Der Kiesemichkopf bei Horhausen liegt schon tief im Westerwald."),
]

SECS = [
    ("rueckersberg", "Ein Blick in den Steinbruch, 1824", "Rückersberg", RUECKERSBERG,
     "Goethe druckt 1824 Nöggeraths Beschreibung der Basaltbrüche am Rückersberg bei Oberkassel: der Steinbruch als Fenster ins Innere des Berges, und schon sichtbar vom Schiff aus als kahle Stelle im Wald.",
     ["goethe1824_s125", "horner1836"], None),
    ("kuppen", "Die Kuppen, 1861", "Kuppen", KUPPEN,
     "Heinrich von Dechens geologischer Führer von 1861: die Unkeler Brüche, schon von den Römern betrieben, und eine Tabelle von 35 Basaltbergen mit ihren Höhen, vom Großen Ölberg bis zum Kleinen Weilberg.",
     ["dechen1861_s146", "noeggerath1838"], "kuppen"),
    ("saeulen", "Säulen und Brüche, 1861", "Säulen", SAEULEN,
     "Wo 1861 gebrochen wurde und warum: An den Basaltbergen des Siebengebirges noch nicht, wohl aber bei Oberkassel, Erpel, Linz und Unkel, wo der Basalt in langen, glatten Säulen steht.",
     ["zehler1837"], None),
]

DATA = {
    "id": "stein",
    "titel": "Der Stein, 1824–1861",
    "autor": "Johann Jacob Nöggerath, herausgegeben von Goethe (1824); Heinrich von Dechen (1861)",
    "jahr": "1824–1861",
    "sprache": "de",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "Goethe (Hg.), Zur Naturwissenschaft überhaupt, besonders zur Morphologie, Bd. II, Heft 2 (Stuttgart und Tübingen 1824), S. 125–132, nach J. J. Nöggerath, Das Gebirge in Rheinland-Westphalen, Bd. 2 (Bonn 1823); H. von Dechen, Geognostischer Führer in das Siebengebirge am Rhein (Bonn 1861), S. 145–147, 162–163. Gelesen an den Digitalisaten der Bayerischen Staatsbibliothek (digitale-sammlungen.de: bsb11942387, bsb10012770).",
    "hinweis": "Bevor vom Schutz der Berge die Rede ist, sind sie ein Gegenstand der Forschung: Der Geologe braucht den Steinbruch, um ins Innere zu sehen. Das Modul zeigt den Stand vor dem großen Abbau. Text nach den Drucken, an den Seitenbildern gelesen; Schreibung und Zeichensetzung wie gedruckt, ſ als s, Silbentrennung aufgelöst, Sperrungen und Kursive nicht wiedergegeben, Auslassungen mit […] bezeichnet, im Druck ausgefallene Buchstaben in [ ].",
    "sections": [{"id": i, "titel": t, "zk": zk, "blurb": b, "plates": pl, **({"viz": vz} if vz else {}), "units": us}
                 for i, t, zk, us, b, pl, vz in SECS],
}

if __name__ == "__main__":
    for s in DATA["sections"]:
        ns = [x["n"] for x in s["units"]]
        assert ns == list(range(1, len(ns) + 1)), (s["id"], ns)
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, sum(len(s["units"]) for s in DATA["sections"]), "units")
