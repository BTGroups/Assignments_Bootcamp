try:
    final_amount = float(input("Enter final payable amount: "))

    loyalty_points = int(final_amount // 100)

    print("\n--- Loyalty Program ---")
    print("Final Amount: ₹{:.2f}".format(final_amount))
    print("Loyalty Points Earned:", loyalty_points)

except ValueError:
    print("Invalid input. Please enter a valid amount.")
