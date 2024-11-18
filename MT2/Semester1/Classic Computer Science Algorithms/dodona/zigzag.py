# https://dodona.be/nl/courses/4195/series/46778/activities/2038783829


def iszigzag(reeks):
    for i in range(0, len(reeks), 2):  # Controleer even posities
        if i > 0 and reeks[i] < reeks[i-1]:  # Huidig element is kleiner dan het vorige (oneven positie)
            return False
        if i < len(reeks) - 1 and reeks[i] < reeks[i+1]:  # Huidig element is kleiner dan het volgende (oneven positie)
            return False
    return True

def zigzag_traag(reeks):
    # Sorteer de lijst van klein naar groot
    reeks.sort()
    # Wissel opeenvolgende getallen
    for i in range(1, len(reeks), 2):
        reeks[i-1], reeks[i] = reeks[i], reeks[i-1]

def zigzag_snel(reeks):
    # Loop over de even posities
    for i in range(0, len(reeks), 2):
        # Als het huidige element kleiner is dan het vorige (oneven positie), wissel om
        if i > 0 and reeks[i] < reeks[i-1]:
            reeks[i], reeks[i-1] = reeks[i-1], reeks[i]
        # Als het huidige element kleiner is dan het volgende (oneven positie), wissel om
        if i < len(reeks) - 1 and reeks[i] < reeks[i+1]:
            reeks[i], reeks[i+1] = reeks[i+1], reeks[i]

# Test van de iszigzag functie
print(iszigzag([10, 5, 6, 3, 2, 20, 100, 80]))  # Verwacht: False
print(iszigzag((10, 5, 6, 2, 20, 3, 100, 80)))  # Verwacht: True
print(iszigzag([20, 5, 10, 2, 80, 6, 100, 3]))  # Verwacht: True

# Test van de zigzag_traag functie
reeks = [10, 90, 49, 2, 1, 5, 23]
zigzag_traag(reeks)
print(reeks)  # Verwacht: [2, 1, 10, 5, 49, 23, 90]

# Test van de zigzag_snel functie
reeks = [10, 90, 49, 2, 1, 5, 23]
zigzag_snel(reeks)
print(reeks)  # Verwacht: [90, 10, 49, 1, 5, 2, 23]
