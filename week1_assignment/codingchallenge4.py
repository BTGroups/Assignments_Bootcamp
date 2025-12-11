if __name__ == "__main__":
    try :
        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))
        a, b = b ,a 
        print("The first value : ", a)
        print("The second value : ", b)
    except Exception as e:
        print("An error occured :", e)


