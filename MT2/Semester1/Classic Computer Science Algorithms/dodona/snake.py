# https://dodona.be/nl/courses/4195/series/46778/activities/1333299580


def beweeg(coordinaten, pijltje):
    x, y = coordinaten
    if pijltje == '>':
        return (x + 1, y)
    elif pijltje == '<':
        return (x - 1, y)
    elif pijltje == '^':
        return (x, y + 1)
    elif pijltje == 'v':
        return (x, y - 1)

def teruggekeerd(pijltjes):
    # Controleer of de combinatie van pijltjes tegengesteld is
    return (pijltjes == ['>', '<']) or (pijltjes == ['<', '>']) or \
           (pijltjes == ['^', 'v']) or (pijltjes == ['v', '^'])

def laatst_levende_positie(pijltjes):
    x, y = 0, 0  # Begincoördinaten
    geldige_zetten = 0

    for i in range(len(pijltjes) - 1):
        # Controleer of de volgende stap dodelijk is
        if teruggekeerd([pijltjes[i], pijltjes[i + 1]]):
            break  # Stoppen als een dodelijke combinatie gevonden wordt
        else:
            geldige_zetten += 1
            x, y = beweeg((x, y), pijltjes[i])

    # Verplaats de slang één keer extra als er geen dodelijke combinatie is gevonden
    x, y = beweeg((x, y), pijltjes[geldige_zetten])
    return geldige_zetten + 1, x, y

# Test van de beweeg functie
print(beweeg((-6, -6), '<'))  # Verwacht: (-7, -6)
print(beweeg((7, 3), '^'))    # Verwacht: (7, 4)

# Test van de teruggekeerd functie
print(teruggekeerd(['^', 'v']))  # Verwacht: True
print(teruggekeerd(['>', 'v']))  # Verwacht: False

# Test van de laatst_levende_positie functie
print(laatst_levende_positie(['>', '<', '^']))         # Verwacht: (1, 1, 0)
print(laatst_levende_positie(['v', '>', 'v', '<', '^', '^']))  # Verwacht: (6, 0, 0)
