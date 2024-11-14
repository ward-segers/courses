# https://dodona.be/nl/courses/4195/series/46777/activities/531231333


from collections import Counter

def dubbel(lijst):
    # Gebruik Counter om de frequentie van elk getal te tellen
    frequenties = Counter(lijst)
    
    # Kijk of er een getal is met een frequentie van 2
    for getal, count in frequenties.items():
        if count == 2:
            return getal
    
    # Geen getal komt meer dan één keer voor
    return None

def dubbels(lijst):
    # Gebruik Counter om de frequentie van elk getal te tellen
    frequenties = Counter(lijst)
    
    # Verzamelingen voor eenmalige en meervoudige getallen
    eenmaal = {getal for getal, count in frequenties.items() if count == 1}
    meerdere = {getal for getal, count in frequenties.items() if count > 1}
    
    return eenmaal, meerdere

dubbel([1, 2, 3, 4, 2])

dubbel([1, 2, 3, 4])

dubbel([1, 2, 3, 4, 5, 6, 100, -234, 15, 0, -20000, 15])

dubbels([1, 2, 3, 4, 2])

dubbels([2, 8, 8, 6, 10, -20, -4, -2, -4])


dubbels([1, 3, 5, 7, 2, 4, 6])
