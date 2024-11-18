# https://dodona.be/nl/courses/4195/series/46780/activities/522641350


def varkenswoord(woord):
    # Controleer of het woord leeg is
    if not woord:
        return ""
    
    # Identificeer klinkers en splits woord in hoofdletterdeel en de rest
    klinkers = "AEIOUaeiou"
    eerste_letter_is_hoofdletter = woord[0].isupper()
    
    # Verwerk woorden die beginnen met een klinker
    if woord[0] in klinkers:
        if eerste_letter_is_hoofdletter:
            return woord + "way"
        else:
            return woord + "way"
    
    # Voor woorden die beginnen met een of meer medeklinkers
    # Zoek de index van de eerste klinker
    eerste_klinker_index = len(woord)
    for i, letter in enumerate(woord):
        if letter in klinkers:
            eerste_klinker_index = i
            break

    # Speciaal geval voor 'qu'
    if eerste_klinker_index > 1 and woord[eerste_klinker_index - 1] == 'u' and woord[eerste_klinker_index - 2] == 'q':
        eerste_klinker_index += 1
    
    # Splits het woord in de stam en het verplaatsde deel
    stam = woord[eerste_klinker_index:]
    verplaatsing = woord[:eerste_klinker_index]
    
    # Pas hoofdlettergebruik aan
    if eerste_letter_is_hoofdletter:
        verlatijnst_woord = stam.capitalize() + verplaatsing.lower() + "ay"
    else:
        verlatijnst_woord = stam + verplaatsing + "ay"
    
    return verlatijnst_woord


def varkenslatijn(zin):
    import re
    # Gebruik regex om alle woorden (reeksen letters) in de zin te vinden
    woorden = re.findall(r"[A-Za-z]+|\W+", zin)
    
    # Vervang elk woord door het overeenkomstige Pig Latin woord
    verlatijnste_woorden = [
        varkenswoord(woord) if woord.isalpha() else woord
        for woord in woorden
    ]
    
    # Voeg alles samen om de volledige zin te vormen
    return ''.join(verlatijnste_woorden)
