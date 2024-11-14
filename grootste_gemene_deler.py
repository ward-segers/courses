# https://dodona.be/nl/courses/4195/series/46779/activities/854408577


def ggd(a, b):
    # Zorg ervoor dat a altijd groter of gelijk aan b is
    if b == 0:
        return a
    else:
        # Recursieve aanroep met (b, a % b) volgens Euclides' algoritme
        return ggd(b, a % b)
