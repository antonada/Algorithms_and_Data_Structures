def sort(numbers):
    return sorted(numbers, key=str)

numbers = [10, 2, 42, 5, 13]
sorted_numbers = sort(numbers)
print(sorted_numbers)