try:
    n = int(input("Enter the number of rows: "))
    if n <= 0:
        print("Number of rows cannot be less than zero")
    else:
        a,b = 1,2 

        for i in range(1, n+1):
            for j in range(i):
                print(a, end=" ")
                a , b = b,a+b  
            print()
except ValueError:
    print("Invalid Input. Enter a valid integer.")