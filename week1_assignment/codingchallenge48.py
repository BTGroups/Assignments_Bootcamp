try:
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num

    print("Maximum value:", maximum)

except ValueError:
    print("Invalid input. Please enter integers only.")
