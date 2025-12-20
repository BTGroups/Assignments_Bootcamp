def generate_series(n):
    series = [5]
    fib1, fib2 = 1,1 

    for _ in range(1,n):
        next_value = series[-1] + fib1 
        series.append(next_value)

        fib1, fib2 = fib2, fib1 + fib2 
    
    return series 


try : 
    n = int(input("Enter the number of elements: "))
    print(generate_series(n))
except ValueError:
    print("Enter a valid number")


"""''' Program - Logic - Solution - Approach Steps to keep in mind
 
0. Put a structure to your code - Design your code
 
1. Solution to a given problem
 
2. Bug Free - Zero Bugs - theres no consideration of ALMOST - Bad Culture
 
3. Test Cases - Positive, Negative and Edge Cases - Research and understqnd how to write test cases - and then write for each problem statement
Ability to write test cases - shows the strength of a developer - professional
Quality Mindset
 
4. Unit Testable Code - Break it down into small units which can be tested independently
 
5. Time Space Complexity
 
6. Naming conventions - python casing - snakecasing(Variables, functions, classes should be self explanatory)
 
7. Comments - Why more than what... - Python standard language best practices and format
 
8. Test your code well - All test cases - With result logged
 
9. Explain the code
 
 
///Program Structure or Design of your Code
 
1. Declaring variables
 
2. Accepting values from user - In a separate function
 
3. Calculating total - Separate function
 
4. Calculating Average - Separate function
 
5. Calculating Result - Separatae function
 
6. Displaying Result - Separate function"""