try:
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    total = 0
    for num in arr:
        total += num

    print("Sum of elements:", total)

except ValueError:
    print("Invalid input. Please enter integers only.")
