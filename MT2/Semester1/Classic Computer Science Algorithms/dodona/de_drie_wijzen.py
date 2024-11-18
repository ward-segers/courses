# https://dodona.be/nl/courses/4195/series/46781/activities/113082360

import math

# bedrag inlezen
bedrag = float(input())

# bedrag vermenigvuldigen met 100 om te rekenen met integers
integer_bedrag = round(bedrag *100)

# template voor uitvoer vastleggen
template = '€{0:.2f} + €{1:.2f} + €{2:.2f} = €{0:.2f} x €{1:.2f} x €{2:.2f} = €{3:.2f}'

# vlag om te stoppen met zoeken van zodra een oplossing gevonden wordt
gevonden = False

# drie getallen bepalen die aan voorwaarden voldoen
som1 = integer_bedrag
prod1 = som1 *10000
a=1
while not gevonden and a < min(som1 // 3, math.floor(prod1 ** (1 / 3))) + 1:
    if not prod1 % a:
        som2 = som1 - a
        prod2 = prod1 // a
        b=a
        while not gevonden and b < min(som2 // 2, math.floor(prod2 ** 0.5)) + 1:
            if not prod2 % b:
                c = prod2 // b
                if b + c == som2:
                    gevonden = True
                    print(template.format(a / 100, b / 100, c / 100, bedrag))
            b += 1
    a += 1