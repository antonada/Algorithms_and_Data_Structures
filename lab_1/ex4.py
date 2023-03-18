numbers = [1, 2, 3, 4, 5, 11, 52, 16]

min_value = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < min_value:
        min_value = numbers(i)


print("Minimum value in array: ", min_value)