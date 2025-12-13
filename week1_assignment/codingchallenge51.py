try:
    n = int(input("Enter number of elements: "))

    if n <= 0:
        print("Array size must be greater than zero.")
    
    else : 
        arr = []
        for i in range(n):
            arr.append(int(input(f"Enter element {i + 1}: ")))

        print("Array elements: ", arr)
except ValueError:
    print("Invalid input. Please enter an integer for size")