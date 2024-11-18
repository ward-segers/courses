# https://dodona.be/nl/courses/4195/series/46778/activities/117689921


def alfabetisch(zin):
    # Split de zin in een lijst van woorden
    woorden = zin.split()
    
    # Sorteer de lijst van woorden alfabetisch
    woorden.sort()
    
    # Zet de gesorteerde lijst van woorden weer om in een string
    return ' '.join(woorden)


alfabetisch('zeven zatte zaventemse zotten zullen zeven zomerse zondagen zwemmen zonder zwembroek')
'zatte zaventemse zeven zeven zomerse zondagen zonder zotten zullen zwembroek zwemmen'

alfabetisch('een pet met een platte klep is een plattekleppet')
'een een een is klep met pet platte plattekleppet'

alfabetisch('je ziet een boel vliegen vliegen maar er is geen een bij bij')
'bij bij boel een een er geen is je maar vliegen vliegen ziet'
