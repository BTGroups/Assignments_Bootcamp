def discountfactor(originalprice : float, discountpercentage : float):
    discounted_price = originalprice * (discountpercentage / 100)
    return discounted_price


if __name__ == "__main__":
    try:
        originalprice = float(input("Enter the original Price: "))
        discount = float(input("Enter the discounted price: "))
        print("Discounted Price :", discountfactor(originalprice=originalprice, discountpercentage=discount))
    except Exception as e:
        print("Error occured:", e)
        