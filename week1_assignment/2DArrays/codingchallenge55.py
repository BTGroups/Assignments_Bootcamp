try:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Rows and columns must be positive integers.")
    else:
        matrix = []
        print("Enter the elements row-wise: ")
        for i in range(rows):
            row = []
            for j in range(cols):
                value = int(input(f"Element [{i}][{j}]: "))
                row.append(value)
            matrix.append(row)
        print("\n2D Array (Row-wise display):")
        for row in matrix:
            for value in row:
                print(value, end=" ")
            print()

except ValueError:
    print("Invalid input. Please enter integers only.")