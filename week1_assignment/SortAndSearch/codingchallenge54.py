def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True 

def binary_search(arr, key):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid 
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid+1
    return -1
try:
    arr = list(map(int, input("Enter array elements in ascending order: ").split()))

    if not is_sorted(arr):
        print("Error: Array is not sorted in ascending order.")
    else:
        key = int(input("Enter element to search: "))
        index = binary_search(arr, key)

        if index != -1:
            print("Element found at index:", index)
        else:
            print("Element not found")

except ValueError:
    print("Invalid input. Please enter integers only.")