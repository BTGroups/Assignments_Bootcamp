try:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    total = 0

    print("Enter elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Element [{i}][{j}]: "))
            row.append(value)
            total += value
        matrix.append(row)

    print("Sum of all elements:", total)

except ValueError:
    print("Invalid input. Please enter integers only.")
