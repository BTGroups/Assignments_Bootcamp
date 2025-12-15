try:
    n = int(input("Enter n: "))

    if n <= 0:
        print("Enter a positive number.")
    else:
        result = [str(i * i) for i in range(1, n + 1)]
        print(", ".join(result))

except ValueError:
    print("Invalid input!")
