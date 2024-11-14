# https://dodona.be/nl/courses/4195/series/46778/activities/623087135


def nieuw_kaartspel(kleuren, waarden):
    # Creëer een lijst van kaarten door elke kleur te combineren met elke waarde
    return [kleur + waarde for kleur in kleuren for waarde in waarden]

def splits_kaartspel(kaarten):
    # Bereken de index om te splitsen
    midden = len(kaarten) // 2
    # Als het aantal kaarten oneven is, krijgt het tweede deel één kaart extra
    return (kaarten[:midden], kaarten[midden:])

def faro_shuffle(deel1, deel2):
    # Combineer de kaarten uit deel1 en deel2 volgens de faro shuffle-methode
    faro_kaarten = []
    for kaart1, kaart2 in zip(deel1, deel2):
        faro_kaarten.append(kaart1)
        faro_kaarten.append(kaart2)
    # Voeg de overgebleven kaarten toe als een van de lijsten langer is
    return faro_kaarten + deel1[len(deel2):] + deel2[len(deel1):]

# Test voorbeelden
print(nieuw_kaartspel(['dood ', 'liefde ', 'tijd '], ['0', '1']))
print(splits_kaartspel(['dood 0', 'dood 1', 'liefde 0', 'liefde 1', 'tijd 0', 'tijd 1']))
print(faro_shuffle(['dood 0', 'dood 1', 'liefde 0'], ['liefde 1', 'tijd 0', 'tijd 1']))
