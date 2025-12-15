try:
    n = int(input("Enter n: "))

    if n <= 0:
        print("Enter a positive number.")
    else:
        result = []
        x = 2
        for _ in range(n):
            result.append(str(x*x))
            x += 2
        print(", ".join(result))

except ValueError:
    print("Invalid input! Enter a valid number.")
