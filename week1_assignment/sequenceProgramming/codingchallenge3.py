def discountfactor(originalprice : float, discountpercentage : float):
    amount = originalprice * (discountpercentage / 100)
    return amount


if __name__ == "__main__":
    try:
        originalprice = float(input("Enter the original Price: "))
        discount = float(input("Enter the discount percentage: "))
        print("Discount Amount :", discountfactor(originalprice=originalprice, discountpercentage=discount))

    except ValueError:
        print("❌ ValueError: Please enter numeric values only.")

    except TypeError:
        print("❌ TypeError: Invalid type encountered.")

    except Exception as e:
        print(f"❌ Unexpected Error ({type(e).__name__}): {e}")
