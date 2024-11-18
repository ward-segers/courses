# https://dodona.be/nl/courses/4195/series/46780/activities/862295437


def herhaal_sleutel(sleutel, lengte):
    """Herhaalt het sleutelwoord tot het even lang is als de tekst."""
    return (sleutel * (lengte // len(sleutel) + 1))[:lengte]

def codeer(tekst, sleutel):
    sleutel_herhaald = herhaal_sleutel(sleutel, len(tekst))
    versleuteld = []

    for i, letter in enumerate(tekst):
        if 'A' <= letter <= 'Z':  # Versleutel alleen hoofdletters
            tekst_index = ord(letter) - ord('A')
            sleutel_index = ord(sleutel_herhaald[i]) - ord('A')
            versleutelde_letter = chr((tekst_index + sleutel_index) % 26 + ord('A'))
            versleuteld.append(versleutelde_letter)
        else:
            versleuteld.append(letter)  # Laat niet-hoofdletters onveranderd

    return ''.join(versleuteld)

def decodeer(tekst, sleutel):
    sleutel_herhaald = herhaal_sleutel(sleutel, len(tekst))
    ontcijferd = []

    for i, letter in enumerate(tekst):
        if 'A' <= letter <= 'Z':  # Ontcijfer alleen hoofdletters
            tekst_index = ord(letter) - ord('A')
            sleutel_index = ord(sleutel_herhaald[i]) - ord('A')
            ontcijferde_letter = chr((tekst_index - sleutel_index) % 26 + ord('A'))
            ontcijferd.append(ontcijferde_letter)
        else:
            ontcijferd.append(letter)  # Laat niet-hoofdletters onveranderd

    return ''.join(ontcijferd)
