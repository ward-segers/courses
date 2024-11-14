# https://dodona.be/nl/courses/4195/series/46780/activities/581452346


def bovensteboven(n):
    omgekeerd = str(n)[::-1]
    rotatie = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    try:
        geroteerd = ''.join(rotatie[c] for c in omgekeerd)
        return str(n) == geroteerd
    except KeyError:
        return False

def volgende(n):
    n += 1
    while not bovensteboven(n):
        n += 1
    return n
