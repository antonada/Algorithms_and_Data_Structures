def fibonacci(n):
    fib = [0, 1] 
    if n <= 1:
        return fib[n]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])

    return fib[n]

n = 10
result = fibonacci(n)

print(f"Element {n} Fibonacci: {result}")

