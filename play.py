def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

def fibonacci_co(limit=20):
    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        yield current

for n in fibonacci_co(100):
    print(n, end=', ')