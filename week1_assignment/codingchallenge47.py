try:
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    minimum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num

    print("Minimum value:", minimum)

except ValueError:
    print("Invalid input. Please enter integers only.")
