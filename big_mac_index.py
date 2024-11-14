# https://dodona.be/nl/courses/4195/series/46780/activities/1131866318


def waardering(prijs, wisselkoers_reel):
    wisselkoers = (prijs/4.07)
    v = ((wisselkoers-wisselkoers_reel)/wisselkoers_reel)*100
    if v <= -25:
        return "sterk ondergewaardeerd"
    elif -25 < v <= -5:
        return "ondergewaardeerd"
    elif -5< v <= 5:
        return "ongeveer gelijk"
    elif 5< v<= 25:
        return "overgewaardeerd"
    else:
        return "sterk overgewaardeerd" 
    
def wisselkoersanalyse(prijs, wisselkoers):
    currency = ""
    lijst = prijs.split(" ")
    v = waardering(float(lijst[0]), wisselkoers)
    for x in lijst[1:]:
        if x != lijst[-1]:
            currency = currency + x + " "
        else:
            currency = currency + x
    return f"De {currency} is {v} ten opzichte van de dollar."

print(wisselkoersanalyse('3.44 sterling pond', 0.70))