# https://dodona.be/nl/courses/4195/series/46778/activities/1067717366


def zien(hoeden):
    # Stap 1: Bepaal voor elke persoon de kleur die ze in hun hoofd houden
    kleuren_in_hoofd = []
    for i in range(len(hoeden)):
        # Tel het aantal rode hoeden voor de huidige persoon
        aantal_rode_hoeden = hoeden[:i].count('R')
        
        # Als het aantal rode hoeden oneven is, houdt de persoon rood in zijn hoofd
        if aantal_rode_hoeden % 2 == 1:
            kleuren_in_hoofd.append('R')
        else:
            kleuren_in_hoofd.append('B')
    
    return tuple(kleuren_in_hoofd)

def zeggen(kleuren_in_hoofd):
    # Stap 2: Bepaal wat elke persoon zegt, door de kleuren in hun hoofd aan te passen
    kleuren_gezegd = []
    voorbije_gok = 0  # Houd bij hoeveel keer 'R' is gezegd
    for kleur in kleuren_in_hoofd:
        # Als het aantal keer 'R' eerder is gezegd oneven is, wissel de kleur
        if voorbije_gok % 2 == 1:
            if kleur == 'R':
                kleuren_gezegd.append('B')
            else:
                kleuren_gezegd.append('R')
        else:
            kleuren_gezegd.append(kleur)
        
        # Tel de huidige 'R' bij voorbije_gok
        if kleur == 'R':
            voorbije_gok += 1
    
    return tuple(kleuren_gezegd)

# Voorbeeld 1
print(zien(('R', 'B', 'R', 'R', 'B')))  # Verwacht: ('B', 'R', 'R', 'B', 'R')
print(zeggen(('B', 'R', 'R', 'B', 'R')))  # Verwacht: ('R', 'B', 'R', 'R', 'R')

# Voorbeeld 2
print(zien(['R', 'R', 'B', 'R', 'R', 'B', 'R', 'B', 'R', 'R']))  # Verwacht: ('B', 'R', 'B', 'B', 'R', 'B', 'B', 'R', 'R', 'B')
print(zeggen(['B', 'R', 'B', 'B', 'R', 'B', 'B', 'R', 'R', 'B']))  # Verwacht: ('R', 'R', 'B', 'R', 'R', 'B', 'R', 'B', 'R', 'B')

# Voorbeeld 3
print(zien('BBRBRBRBBRBR'))  # Verwacht: ('B', 'B', 'B', 'R', 'R', 'B', 'B', 'R', 'R', 'R', 'B', 'B')
print(zeggen('BBRBRBRBBRBB'))  # Verwacht: ('B', 'R', 'R', 'R', 'R', 'R', 'R', 'B', 'R', 'R', 'B', 'B')
