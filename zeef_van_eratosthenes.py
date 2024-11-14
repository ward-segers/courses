# https://dodona.be/nl/courses/4195/series/46778/activities/197813628


import math

def zeef(n):
    if n < 2:
        return []  # Er zijn geen priemgetallen kleiner dan 2
    
    # Stap 1: Maak een lijst van True voor elk getal van 0 tot n
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 en 1 zijn geen priemgetallen
    
    # Stap 2: Zeefproces
    for start in range(2, int(math.sqrt(n)) + 1):
        if sieve[start]:  # Als start nog steeds als priem wordt beschouwd
            for multiple in range(start * start, n + 1, start):  # Begin bij start^2
                sieve[multiple] = False  # Markeer veelvouden van start als niet-priem
    
    # Stap 3: Verzamel de priemgetallen
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    
    return primes


print(zeef(6))  # Verwacht: [2, 3, 5]
print(zeef(30))  # Verwacht: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(zeef(100))  # Verwacht: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
