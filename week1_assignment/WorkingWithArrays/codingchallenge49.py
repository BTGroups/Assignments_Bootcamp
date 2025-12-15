try:
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))

    search = int(input("Enter element to search: "))

    if search in arr:
        print("Element found at index:", arr.index(search))
    else:
        print("Element not found")

except ValueError:
    print("Invalid input. Please enter integers only.")
