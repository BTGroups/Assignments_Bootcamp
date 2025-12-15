try:
    n = int(input("Enter the number of rows: "))
    if n <=0 :
        print("Number of rows can't less than zero")
    else:
        for _ in range(1, n+1):
            print("12345")
except ValueError:
    print("Invalid Input. Please enter an integer")