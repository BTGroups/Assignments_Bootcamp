try:
    r1 = int(input("Enter rows of matrix A: "))
    c1 = int(input("Enter columns of matrix A: "))
    r2 = int(input("Enter rows of matrix B: "))
    c2 = int(input("Enter columns of matrix B: "))

    if c1 != r2:
        print("Matrix multiplication not possible.")
    else:
        print("Enter matrix A:")
        A = [list(map(int, input().split())) for _ in range(r1)]

        print("Enter matrix B:")
        B = [list(map(int, input().split())) for _ in range(r2)]

        result = [[0 for _ in range(c2)] for _ in range(r1)]

        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    result[i][j] += A[i][k] * B[k][j]

        print("\nResultant Matrix:")
        for row in result:
            print(row)

except ValueError:
    print("Invalid input. Please enter integers only.")
