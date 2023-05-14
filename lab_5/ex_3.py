def calculate_nth_term(n):
    sequence = [0] * (n + 1)

    sequence[0] = 0
    sequence[1] = 1

    for i in range(2, n + 1):
        sequence[i] = sequence[i - 1] + sequence[i - 2]

    return sequence[n]

n = 10
result = calculate_nth_term(n)

print(f"The nth term of the sequence: {result}")

