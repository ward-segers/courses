# https://dodona.be/nl/courses/4195/series/46779/activities/1092659960


def hanoi(n, start='A', end='C', temp='B', stappen=[0]):
    if n == 1:
        print(f"Schijf 1 van {start} naar {end}")
        stappen[0] += 1
    else:
        # Verplaats de bovenste n-1 schijven naar de tijdelijke paal
        hanoi(n - 1, start, temp, end, stappen)
        
        # Verplaats de onderste schijf naar de doelpaal
        print(f"Schijf {n} van {start} naar {end}")
        stappen[0] += 1
        
        # Verplaats de n-1 schijven van de tijdelijke paal naar de doelpaal
        hanoi(n - 1, temp, end, start, stappen)

# Wrapper functie om het aantal stappen duidelijk weer te geven
def hanoi_oplossing(n):
    stappen = [0]  # List om stappen als mutable waarde door te geven
    hanoi(n, stappen=stappen)
    print(f"{stappen[0]} stappen gedaan")

# Voorbeeldgebruik
hanoi_oplossing(4)
