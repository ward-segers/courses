# https://dodona.be/nl/courses/4195/series/46781/activities/32506927


import math

n = 100
value = sum(1/i**2 for i in range(1, n+1))

print(round(value, 11))
print(n)