# https://dodona.be/nl/courses/4195/series/46780/activities/1563511392


def maximale_blootstelling(geluidsniveau):
    # Controleer of het geluidsniveau lager is dan 80 dB
    if geluidsniveau < 80:
        return -1.0  # Onbeperkte tijdsduur
    
    # Basisduur van 8 uur (in seconden)
    basisduur = 8 * 60 * 60  # 8 uur in seconden

    # Bereken het aantal dB-stappen van 3 boven 80 dB
    db_stappen = (geluidsniveau - 80) // 3

    # Halveer de basisduur voor elke 3 dB-stap
    tijdsduur = basisduur / (2 ** db_stappen)

    return tijdsduur

geluidsniveaus = [40, 60, 75, 80, 86, 90, 95, 97, 105, 107, 118, 115, 120]  # Testwaarden
for niveau in geluidsniveaus:
    print(f'{maximale_blootstelling(niveau):.1f}')