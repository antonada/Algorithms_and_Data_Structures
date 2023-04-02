def generate_array(size):
    import random
    return [random.randint(1, 100) for _ in range(size)]

arr = generate_array(10)

min_value = float('inf')
for num in arr:
    if num < min_value:
        min_value = num

print("Minimum value in the array:", min_value)
