
def sumoftwonums(x : float, y : float) -> float:
    return x + y 

def averageoftwonums(x: float, y  :float) -> float:
    return (x + y)/ 2

if __name__ == "__main__":
    #first and second variables
    try : 
        a = float(input("Enter the first variable: "))
        b = float(input("Enter the second variable: "))
        print("Sum of the two variables : ", sumoftwonums(a,b))
        print("Average of the two variables: ", averageoftwonums(a,b))
    except Exception as e:
        print("An error occurred:", e)