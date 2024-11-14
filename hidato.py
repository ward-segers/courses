# https://dodona.be/nl/courses/4195/series/46778/activities/565313929


def eerste(rooster):
    for r, rij in enumerate(rooster):
        for k, waarde in enumerate(rij):
            if waarde == 1:
                return (r, k)
    return None  # Indien geen 1 gevonden (zou niet moeten voorkomen in een geldig rooster)

def opvolger(rooster, r, k):
    max_r, max_k = len(rooster), len(rooster[0])
    huidig_getal = rooster[r][k]
    volgende_getal = huidig_getal + 1

    # Definieer de mogelijke verplaatsingen (ook diagonaal)
    verplaatsingen = [
        (-1, 0), (1, 0), (0, -1), (0, 1),    # Verticaal en horizontaal
        (-1, -1), (-1, 1), (1, -1), (1, 1)   # Diagonaal
    ]

    for dr, dk in verplaatsingen:
        nieuwe_r, nieuwe_k = r + dr, k + dk
        # Controleer of de nieuwe positie binnen de grenzen van het rooster valt
        if 0 <= nieuwe_r < max_r and 0 <= nieuwe_k < max_k:
            if rooster[nieuwe_r][nieuwe_k] == volgende_getal:
                return (nieuwe_r, nieuwe_k)

    return (None, None)

def laatste(rooster):
    r, k = eerste(rooster)
    while True:
        volgende_r, volgende_k = opvolger(rooster, r, k)
        if volgende_r is None and volgende_k is None:
            break
        r, k = volgende_r, volgende_k
    return (r, k)

def hidato(rooster):
    max_waarde = len(rooster) * len(rooster[0])
    r, k = laatste(rooster)
    return rooster[r][k] == max_waarde


# Test van de eerste functie
print(eerste([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]]))  # Verwacht: (2, 3)
print(eerste([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]]))  # Verwacht: (1, 1)
print(eerste(((18, 19, 20, 4, 5), (17, 1, 3, 6, 8), (16, 13, 2, 9, 7), (14, 15, 12, 11, 10))))  # Verwacht: (1, 1)

# Test van de opvolger functie
print(opvolger([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]], 2, 3))  # Verwacht: (1, 3)
print(opvolger([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]], 1, 3))  # Verwacht: (1, 2)
print(opvolger([[5, 4, 11, 2], [6, 10, 3, 12], [7, 8, 9, 1]], 2, 3))  # Verwacht: (None, None)

# Test van de laatste functie
print(laatste([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]]))  # Verwacht: (0, 3)
print(laatste([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]]))  # Verwacht: (3, 2)
print(laatste(((18, 19, 20, 4, 5), (17, 1, 3, 6, 8), (16, 13, 2, 9, 7), (14, 15, 12, 11, 10))))  # Verwacht: (0, 2)

# Test van de hidato functie
print(hidato([[5, 4, 11, 12], [6, 10, 3, 2], [7, 8, 9, 1]]))  # Verwacht: True
print(hidato([[8, 14, 13, 12], [15, 1, 2, 11], [5, 3, 10, 16], [4, 6, 7, 9]]))  # Verwacht: False
print(hidato(((18, 19, 20, 4, 5), (17, 1, 3, 6, 8), (16, 13, 2, 9, 7), (14, 15, 12, 11, 10))))  # Verwacht: True
