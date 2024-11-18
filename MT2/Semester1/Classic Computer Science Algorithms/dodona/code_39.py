# https://dodona.be/nl/courses/4195/series/46777/activities/1186776322


def omgekeerd(sleutel):
    """
    Keert de sleutel/waarde paren van een gegeven dictionary om.
    """
    return {waarde: sleutel for sleutel, waarde in sleutel.items()}

def code39(zin, sleutel):
    """
    Zet een zin om naar haar ASCII-voorstelling in code 39.
    Karakters worden omgezet naar hun code 39 equivalent, gescheiden door smalle witte strook ('s').
    """
    # Converteer de zin naar hoofdletters (code 39 is niet hoofdlettergevoelig)
    zin = zin.upper()
    
    # Maak de code 39 representatie van de zin
    resultaat = []
    for char in zin:
        # Voeg de bijbehorende code 39 voor elk karakter toe aan het resultaat
        if char in sleutel:
            resultaat.append(sleutel[char])
    
    # Voeg smalle witte stroken ('s') toe tussen de karakters
    return 's'.join(resultaat)

def decode39(code, sleutel):
    """
    Zet een ASCII-voorstelling in code 39 om naar de oorspronkelijke zin.
    We gebruiken de omgekeerde sleutel om dit om te zetten.
    """
    # Keer de sleutel om
    omgekeerde_sleutel = omgekeerd(sleutel)
    
    # Splits de code in stukken van 9 tekens (elk karakter in code 39 is 9 tekens lang)
    delen = code.split('s')
    
    # Vind de bijbehorende karakters voor elk stuk en bouw de zin
    zin = []
    for deel in delen:
        if deel in omgekeerde_sleutel:
            zin.append(omgekeerde_sleutel[deel])
    
    # Zet de lijst om naar een string en geef deze terug
    return ''.join(zin)

# Voorbeeld gebruik
sleutel = {
    'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS',
    'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS',
    '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS',
    '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS',
    '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB',
    'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB',
    'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB',
    '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS',
    'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB',
    '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS',
    '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'
}

# Testen van de functies
omgekeerd_sleutel = omgekeerd(sleutel)
print(omgekeerd_sleutel)

gecodeerd = code39('Sulfur, so good.', sleutel)
print(gecodeerd)

gedeocodeerd = decode39(gecodeerd, sleutel)
print(gedeocodeerd)
