try:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    print("Enter elements row-wise:")
    for i in range(rows):
        matrix.append(list(map(int, input().split())))

    key = int(input("Enter element to search: "))
    found = False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == key:
                print(f"Element found at position ({i}, {j})")
                found = True

    if not found:
        print("Element not found")

except ValueError:
    print("Invalid input.")
