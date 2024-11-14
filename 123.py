# https://dodona.be/nl/courses/4195/series/46780/activities/192047393

def even_oneven(getal):

    """
    >>> even_oneven(886328712442992)
    (10, 5)
    >>> even_oneven(10515)
    (1, 4)
    >>> even_oneven(145)
    (1, 2)
    """

def volgende(getal):

    """
    >>> volgende(886328712442992)
    10515
    >>> volgende(10515)
    145
    >>> volgende(145)
    123
    """

def stappen(getal):

    """
    >>> stappen(886328712442992)
    3
    >>> stappen(1217637626188463187643618416764317864)
    4
    >>> stappen(0)
    2
    >>> stappen(1)
    5
    >>> stappen(2)
    2
    >>> stappen(3)
    5
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

def even_oneven(n):
    even = 0
    oneven = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even += 1
        else:
            oneven += 1
    return even, oneven

def volgende(n):
    even, oneven = even_oneven(n)
    totaal = even + oneven
    # Vorm het nieuwe getal zonder voorloopnullen
    nieuw_getal = int(f"{even}{oneven}{totaal}")
    return nieuw_getal

def stappen(n):
    count = 0
    while n != 123:
        n = volgende(n)
        count += 1
    return count
