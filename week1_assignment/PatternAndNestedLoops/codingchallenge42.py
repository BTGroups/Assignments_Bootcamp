try:
    n = int(input("Enter the n: "))
    if n <= 0:
        print("N cannot be less than zero")
    else:
        num = 1
        for i in range(1, n+1):
           
            if i % 2 == 0:
                print(-num, end = " ")
            else :
                print(num, end = " ")
            num += 4
except ValueError:
    print("Invalid Input. Enter a valid integer.")