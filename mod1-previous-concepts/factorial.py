def factorial(n):
    accumulator = 1
    if n > 1:
        for i in range(1, n + 1):
            accumulator = accumulator * i
    return accumulator
