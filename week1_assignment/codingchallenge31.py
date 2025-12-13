try:
    grand_total = float(input("Enter final amount after tax: "))
    payment = input("Enter payment method (cash/credit): ").strip().lower()

    surcharge = 0
    if payment == "credit":
        surcharge = grand_total * 0.02
        grand_total += surcharge

    print("\n--- Payment Details ---")
    print("Payment Method:", payment.capitalize())
    print("Surcharge Applied: ₹{:.2f}".format(surcharge))
    print("Final Payable Amount: ₹{:.2f}".format(grand_total))

except ValueError:
    print("Invalid input. Please enter valid numbers.")
