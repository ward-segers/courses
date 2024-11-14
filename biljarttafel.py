# https://dodona.be/nl/courses/4195/series/46781/activities/364433585


def biljarttafel(hoogte, breedte):
    # Startpositie en -richting
    x, y = 0, 0
    dx, dy = 1, 1  # De bal beweegt diagonaal (45°)

    while True:
        # Bepaal de afstand tot de dichtstbijzijnde band
        next_x_wall = breedte if dx > 0 else 0
        next_y_wall = hoogte if dy > 0 else 0
        dist_x = abs(next_x_wall - x)
        dist_y = abs(next_y_wall - y)

        # Verplaats naar de dichtstbijzijnde band
        if dist_x == dist_y:
            x, y = next_x_wall, next_y_wall
        elif dist_x < dist_y:
            x = next_x_wall
            y += dy * dist_x
        else:
            y = next_y_wall
            x += dx * dist_y

        # Controleer of de bal in een pocket terechtkomt
        if (x, y) == (0, 0):
            print(f'linkeronderpocket ({x}, {y})')
            break
        elif (x, y) == (breedte, 0):
            print(f'rechteronderpocket ({x}, {y})')
            break
        elif (x, y) == (breedte, hoogte):
            print(f'rechterbovenpocket ({x}, {y})')
            break
        elif (x, y) == (0, hoogte):
            print(f'linkerbovenpocket ({x}, {y})')
            break

        # Geef de botsende band en de nieuwe positie weer
        if x == 0:
            print(f'linkerband ({x}, {y})')
            dx = -dx  # Richting omkeren in de x-richting
        elif x == breedte:
            print(f'rechterband ({x}, {y})')
            dx = -dx
        if y == 0:
            print(f'onderband ({x}, {y})')
            dy = -dy  # Richting omkeren in de y-richting
        elif y == hoogte:
            print(f'bovenband ({x}, {y})')
            dy = -dy

# Voorbeeldinvoer
hoogte = int(input())
breedte = int(input())
biljarttafel(hoogte, breedte)