# https://dodona.be/nl/courses/4195/series/46777/activities/933472639


def controlecijfer_berekenen(isbn):
    som = 0
    for i, cijfer in enumerate(isbn[:12]):
        if i % 2 == 0:
            som += int(cijfer)
        else:
            som += int(cijfer) * 3
    controle_cijfer = (10 - (som % 10)) % 10
    return controle_cijfer

def is_valid_isbn(isbn):
    if len(isbn) != 13 or not isbn.isdigit():
        return False
    if not (isbn.startswith("978") or isbn.startswith("979")):
        return False
    return controlecijfer_berekenen(isbn) == int(isbn[-1])

def overzicht(codes):
    groepen = {
        "Engelstalige landen": 0,
        "Franstalige landen": 0,
        "Duitstalige landen": 0,
        "Japan": 0,
        "Russischtalige landen": 0,
        "China": 0,
        "Overige landen": 0,
        "Fouten": 0
    }

    for code in codes:
        if not is_valid_isbn(code):
            groepen["Fouten"] += 1
        else:
            registratiegroep = code[3]
            if registratiegroep in "01":
                groepen["Engelstalige landen"] += 1
            elif registratiegroep == "2":
                groepen["Franstalige landen"] += 1
            elif registratiegroep == "3":
                groepen["Duitstalige landen"] += 1
            elif registratiegroep == "4":
                groepen["Japan"] += 1
            elif registratiegroep == "5":
                groepen["Russischtalige landen"] += 1
            elif registratiegroep == "7":
                groepen["China"] += 1
            else:
                groepen["Overige landen"] += 1

    for groep, aantal in groepen.items():
        print(f"{groep}: {aantal}")