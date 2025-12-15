try : 
    n = int(input("Enter a positive integer n : "))
    if n <= 0:
        print("Error: n must be a positive number.")
    else:
        print(", ".join(str(2*i - 1) for i in range(1, n+1) ))
except ValueError:
    print("Error: Please enter a valid integer.")