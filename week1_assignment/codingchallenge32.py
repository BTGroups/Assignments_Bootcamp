try:
    final_amount = float(input("Enter final payable amount: "))

    if final_amount < 500:
        print("Minimum purchase amount ₹500 not met.")
        print("Invoice cannot be generated.")
    else:
        print("Minimum purchase condition satisfied.")
        print("Invoice generated successfully.")
        print("Final Amount: ₹{:.2f}".format(final_amount))

except ValueError:
    print("Invalid input. Please enter a valid amount.")
