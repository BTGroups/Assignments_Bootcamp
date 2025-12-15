try:
    n = int(input("Enter n: "))

    if n <= 0:
        print("Enter a positive number.")
    else:
        result = []
        a, b = 1, 1

        for _ in range(n):
            result.append(str(a))
            a, b = b, a + b

        print(", ".join(result))

except ValueError:
    print("Invalid input!")
