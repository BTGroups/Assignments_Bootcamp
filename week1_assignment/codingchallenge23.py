try:
    n = int(input("Enter n: "))

    if n <= 0:
        print("Enter a positive number.")
    else:
        result = []
        a = 1
        steps = [4, 4, 4, 8]
        idx = 0

        for _ in range(n):
            result.append(str(a))
            a += steps[idx]
            idx = (idx + 1) % 4

        print(", ".join(result))

except ValueError:
    print("Invalid input!")
