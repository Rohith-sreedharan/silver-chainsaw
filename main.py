def fibonacci_series(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Example usage:
n = 10  # Change this value to generate more or fewer Fibonacci numbers
print(fibonacci_series(n))