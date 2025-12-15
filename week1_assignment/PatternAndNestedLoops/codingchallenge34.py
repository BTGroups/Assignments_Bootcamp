try:
    n = int(input("Enter the number of rows: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        for _ in range(n):
            print("*****")
except ValueError:
    print("Invalid Input.Please enter an integer.")