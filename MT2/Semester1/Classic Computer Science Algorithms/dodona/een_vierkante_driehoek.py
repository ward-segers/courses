# https://dodona.be/nl/courses/4195/series/46778/activities/818147392


import math

# Functie 1: driehoek(n)
def driehoek(n):
    if not isinstance(n, int) or n < 0:
        raise AssertionError("ongeldig aantal rijen")
    
    pascal = []
    
    for i in range(n):
        rij = [1] * (i + 1)  # Start met een rij van '1's
        for j in range(1, i):
            rij[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]  # Vul de tussenliggende waarden in
        pascal.append(rij)
    
    return pascal

# Functie 2: zeshoek(r, c)
def zeshoek(r, c):
    pascal = driehoek(r)  # Genereer de driehoek tot rij r
    if r < 2 or c < 2 or c > r - 1:
        raise AssertionError("ongeldige interne positie")
    
    # Haal de zes getallen rondom de interne positie
    return [
        pascal[r - 2][c - 2],  # Boven links
        pascal[r - 1][c - 2],  # Boven
        pascal[r][c - 2],      # Boven rechts
        pascal[r][c - 1],      # Onder rechts
        pascal[r - 1][c - 1],  # Onder
        pascal[r - 2][c - 1]   # Onder links
    ]

# Functie 3: kwadraat(r, c)
def kwadraat(r, c):
    zes_getallen = zeshoek(r, c)
    
    # Bereken het product van de zes getallen
    product = math.prod(zes_getallen)
    
    # Bereken de wortel van het product
    wortel = int(math.isqrt(product))
    
    # Check of het product een volkomen kwadraat is
    if wortel * wortel == product:
        return f"{' x '.join(map(str, zes_getallen))} = {product} = {wortel} x {wortel}"
    else:
        raise AssertionError("ongeldige interne positie")

# Testen
print(driehoek(5))
print(zeshoek(8, 4))
print(kwadraat(8, 4))
