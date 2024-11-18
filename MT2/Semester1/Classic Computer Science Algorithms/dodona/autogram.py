# https://dodona.be/nl/courses/4195/series/46777/activities/370184940


def letterfrequenties(zin):
    frequenties = {}
    for char in zin.lower():  # Zet alles om naar kleine letters
        if char.isalpha():  # Alleen letters worden geteld
            frequenties[char] = frequenties.get(char, 0) + 1  # Verhoog de frequentie
    return frequenties

def letterposities(zin):
    posities = {}
    for index, char in enumerate(zin.lower()):  # Loop door de zin en pak zowel de index als het karakter
        if char.isalpha():  # Alleen letters worden geteld
            if char not in posities:
                posities[char] = set()  # Maak een lege set voor de letter
            posities[char].add(index)  # Voeg de index toe aan de set van die letter
    return posities

zin = "fifteen e's, seven f's, four g's, six h's, eight i's, four n's, five o's, six r's, eighteen s's, eight t's, four u's, three v's, two w's, three x's"

frequentie = letterfrequenties(zin)
print(frequentie)

posities = letterposities(zin)
print(posities)
