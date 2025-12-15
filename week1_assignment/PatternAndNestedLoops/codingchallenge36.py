try:
    n = int(input("Enter the number of rows: "))
    if n <= 0:
        print("Number of rows cannot be less than zero")
    else:
        for i in range(1, n+1):
            print(str(i)*i)
except ValueError:
    print("Invalid Input. Enter a valid integer.")