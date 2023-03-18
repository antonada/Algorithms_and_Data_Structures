array_2d = [[3, 5 , 6], [9, 11, 8], [4, 1, 0], [3, 20, 192]]

for row in array_2d:
    min = row[0]
    for i in range(1, len(row)):
        if row[i] < min:
            min = row[i]

row[row.index(min)], row[0] = row[0], row[row.index(min)]

print("2D array with minimum values ​​at the beginning of each row:" )

for row in array_2d:
    print(row)
