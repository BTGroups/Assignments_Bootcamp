try:
    arr = list(map(int, input("Enter array elements: ").split()))
    choice = input("Enter A for Ascending or D for Descending: ").upper()

    if choice == 'A':
        arr.sort()
    elif choice == 'D':
        arr.sort(reverse=True)
    else:
        print("Invalid choice")

    print("Sorted array:", arr)

except ValueError:
    print("Invalid input.")
