tab = [1, 2, 3, 4, 5]

lookup_value = int(input("Enter lookup value"))

if lookup_value in tab:
    print("value", lookup_value, "in table.")
else:
    print("value", lookup_value, "does not appear in the table.")