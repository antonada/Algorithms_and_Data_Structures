def insert_sorted_list(num, sorted_list):
    sorted_list.append(num)
    i = len(sorted_list) - 1
    while i > 0 and sorted_list[i] < sorted_list[i-1]:
        sorted_list[i], sorted_list[i-1] = sorted_list[i-1], sorted_list[i]
        i -= 1

def add_to_sorted_list(num, sorted_list):
    insert_sorted_list(num, sorted_list)
    sorted_list.sort()

sorted_list = []
add_to_sorted_list(5, sorted_list)
add_to_sorted_list(3, sorted_list)
add_to_sorted_list(8, sorted_list)
print(sorted_list)