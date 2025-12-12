try :
    n = int(input("Enter a positive integer n: "))

    if n <= 0:
        print("Error: n must be a positive number.")
    else: 
        print(", ".join(str(i) for i in range(1, n+1)))

except ValueError:
    print("Error: Please enter a valid integer.")