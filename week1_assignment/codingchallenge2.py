def simpleinterest(principal : float, rate : float, time : float) -> float:
    #function to calculate simple interest
    interest = (principal * rate * time) / 100
    return interest 


if __name__ == "__main__":
    try :
        principal_amount = float(input("Enter the principal amount: "))
        rate_of_interest= float(input("Enter the rate of interest: "))
        time_period = float(input("Enter the time period: "))
        print("Simple Interest: ", simpleinterest(principal_amount, rate_of_interest, time_period))
    except Exception as e:
        print("Errored occured: ", e)