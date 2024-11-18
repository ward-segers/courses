# https://dodona.be/nl/courses/4195/series/46779/activities/546000908


def fib(n):
    # Basisgevallen: fib(0) = 0 en fib(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursieve aanroep voor fib(n-1) en fib(n-2)
    else:
        return fib(n - 1) + fib(n - 2)
