# https://dodona.be/nl/courses/4195/series/46777/activities/431253538


def vertalingToevoegen(woord, vertaling, woordenboek):
    """Voegt een vertaling toe aan het woordenboek."""
    woordenboek[woord] = vertaling

def vertaling(woord, woordenboek):
    """Zoekt de vertaling van een woord in het woordenboek."""
    return woordenboek.get(woord, '???')


# Initialisatie van een leeg woordenboek
woordenboek = {}

# Woorden en vertalingen toevoegen
vertalingToevoegen('plerzs', 'vrouw', woordenboek)
vertalingToevoegen('nirtu', 'bloem', woordenboek)
vertalingToevoegen('klinzoj', 'dorst', woordenboek)
vertalingToevoegen('tilza', 'hond', woordenboek)
vertalingToevoegen('zraidi', 'tijd', woordenboek)

# Het woordenboek bekijken
print(woordenboek)
# Output: {'klinzoj': 'dorst', 'zraidi': 'tijd', 'tilza': 'hond', 'plerzs': 'vrouw', 'nirtu': 'bloem'}

# Vertalingen opvragen
print(vertaling('tilza', woordenboek))  # Output: 'hond'
print(vertaling('guoles', woordenboek))  # Output: '???'
