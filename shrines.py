# Generate random cheapo beer names
import random


def cheapo_beer():
    nobleness = ["krone", "burg", "schloss", "könig", "prinz", "prinzessin", "fürst", "graf", "ritter"]
    waters = ["fluss", "quelle", "see", "bach", "tal", "perle"]
    random_noise = ["gold", "silber", "schlonz", "fusel", "premium"]
    brew = ["bräu", "glück"]

    flavour = random.choice(["Pilsener", "Lager", "Original", "Hell", "Gold", "Export", "Alkoholfrei", "Premium", "Herb", "Kellerbier", "Naturtrüb", "Spezial", "Landbier", "Märzen", "Herrenpils", "Rotbier", "Oktoberfestbier", "Grapefruit", "Radler", "Zitrone", "Naturradler", "Weißbier", "Kristall", "Urtyp", "Vollbier", "Weizen Alkoholfrei", "Weizen", "Urbock", "Extraherb", "Winterbock", "Schwarzbier", "Dunkel", "Privat", "Urbräu", "Zwickl", "Doppelbock", "Süffikus", "Light", "Fun", "Kellerpils", "Exklusiv", "Hefeweizen", "Weisse", "Privat Export", "Jubiläumstrunk", "Maibock", "Märzen"])

    group_first = random.choice([nobleness, waters, random_noise])
    group_second = [nobleness, waters, random_noise, brew]
    group_second.remove(group_first)
    group_second = random.choice(group_second)

    first = random.choice(group_first)
    second = random.choice(group_second)
    fill = ""

    if first[-1] in ["t", "n", "z", "f"]:
        fill = "en"
    elif first[-1] in ["g"]:
        fill = "s"
    elif first[-1] in ["e"]:
        fill = "n"

    return f"{first}{fill}{second} ".capitalize() + f"{flavour}"


shrines = list({cheapo_beer() for _ in range(256)})
