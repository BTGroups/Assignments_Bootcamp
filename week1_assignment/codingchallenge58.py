try:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    print("Enter elements row-wise:")
    for i in range(rows):
        matrix.append(list(map(int, input().split())))

    print("\nMatrix:")
    for row in matrix:
        print(row)

    print("\nTranspose:")
    for j in range(cols):
        for i in range(rows):
            print(matrix[i][j], end=" ")
        print()

except ValueError:
    print("Invalid input.")
