try:
    n = int(input("Enter n: "))

    if n <= 0:
        print("Enter a positive number.")
    else:
        result = []
        a = 1
        diff = 3

        for _ in range(n):
            result.append(str(a))
            a += diff
            diff += 2

        print(", ".join(result))

except ValueError:
    print("Invalid input!")
