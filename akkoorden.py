# https://dodona.be/nl/courses/4195/series/46777/activities/1564830716


# Definieer de chromatische toonladder
chromatische_toonladder = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def ontleding(akkoord_notatie):
    """
    Ontleed de akkoordnotatie in grondnoot en symbool.
    """
    if len(akkoord_notatie) > 1 and akkoord_notatie[1] == '#':
        grondnoot = akkoord_notatie[:2]  # Neem de eerste twee karakters voor grondnoot (bijv. D#)
        symbool = akkoord_notatie[2:]    # De rest is het symbool
    else:
        grondnoot = akkoord_notatie[0]   # Neem de eerste karakter voor grondnoot (bijv. G)
        symbool = akkoord_notatie[1:]    # De rest is het symbool
    return grondnoot, symbool

def noten(grondnoot, intervallen):
    """
    Genereer de lijst van noten waaruit het akkoord bestaat op basis van grondnoot en intervallen.
    """
    # Vind de startpositie van de grondnoot in de chromatische toonladder
    start_index = chromatische_toonladder.index(grondnoot)
    akkoord_noten = []
    # Voeg noten toe volgens de opgegeven intervallen
    for interval in intervallen:
        noot_index = (start_index + interval) % len(chromatische_toonladder)
        akkoord_noten.append(chromatische_toonladder[noot_index])
    return akkoord_noten

def akkoord(akkoord_notatie, akkoordtypes, akkoordsymbolen):
    """
    Bepaal de noten van een akkoord gegeven de notatie, akkoordtypes, en symbolen.
    """
    # Gebruik ontleding om de grondnoot en symbool te vinden
    grondnoot, symbool = ontleding(akkoord_notatie)
    # Vind de naam van het akkoordtype gebaseerd op het symbool
    akkoordtype_naam = akkoordsymbolen[symbool]
    # Vind de intervallen die bij dit akkoordtype horen
    intervallen = akkoordtypes[akkoordtype_naam]
    # Gebruik de noten functie om de noten van het akkoord te bepalen
    akkoord_noten = noten(grondnoot, intervallen)
    return tuple(akkoord_noten)
