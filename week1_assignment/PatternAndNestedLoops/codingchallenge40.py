try:
    n = int(input("Enter number of rows: "))

    if n <= 0:
        print("Please enter a positive number.")
    else:
        num = 1 
        fact = 1

        for i in range(1, n+1):
            for j in range(i):
                fact *= num 
                print(fact, end= " ")
                num += 1
            print()
except ValueError:
    print("Invalid input. Please enter an integer.")