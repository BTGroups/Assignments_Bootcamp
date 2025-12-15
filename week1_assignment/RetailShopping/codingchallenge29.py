if __name__ == "__main__":
    grand_total = 0.0
    total_qty = 0

    # --- Iterative item entry ---
    while True:
        print("\n--- Enter Item Details ---")
        try:
            item_code = input("Enter Item Code: ").strip()
            description = input("Enter Item Description: ").strip()

            qty = int(input("Enter Quantity: "))
            if qty <= 0:
                print("Error: Quantity must be positive.")
                continue

            price = float(input("Enter Price per Item: "))
            if price < 0:
                print("Error: Price cannot be negative.")
                continue

            total = qty * price
            grand_total += total
            total_qty += qty

            print(f"Item Total: ₹{total:.2f}")

        except ValueError:
            print("Error: Invalid number entered. Try again.")
            continue

        more = input("Add another item? (y/n): ").strip().lower()
        if more != 'y':
            break

    print("\n==============================")
    print(f"Subtotal (Before Discounts): ₹{grand_total:.2f}")
    print(f"Total Quantity: {total_qty}")

    # --- Discounts ---
    discount_10 = 0
    discount_5 = 0
    membership_discount = 0

    # 10% discount if subtotal > 10000
    if grand_total > 10000:
        discount_10 = grand_total * 0.10
        grand_total -= discount_10

    # 5% discount if total quantity > 20
    if total_qty > 20:
        discount_5 = grand_total * 0.05
        grand_total -= discount_5

    # Membership discount
    member = input("Is the customer a member? (y/n): ").strip().lower()
    if member == 'y':
        membership_discount = grand_total * 0.02
        grand_total -= membership_discount

    print("\n------- Discounts Applied -------")
    print(f"10% Discount (if > 10000):        ₹{discount_10:.2f}")
    print(f"5% Quantity Discount (if qty>20): ₹{discount_5:.2f}")
    print(f"Membership Discount (2%):        ₹{membership_discount:.2f}")

    # --- Tax calculation based on tier ---
    if grand_total < 5000:
        tax_rate = 0.05
    elif grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    tax_amount = grand_total * tax_rate
    grand_total += tax_amount

    print("\n------- Tax Applied -------")
    print(f"Tax Rate: {int(tax_rate*100)}%")
    print(f"Tax Amount: ₹{tax_amount:.2f}")

    print("\n==============================")
    print(f"FINAL GRAND TOTAL (after tax): ₹{grand_total:.2f}")
    print("==============================")


