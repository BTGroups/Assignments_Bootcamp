if __name__ == "__main__":
    grand_total = 0.0
    total_qty = 0

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

    # ---------------- DISCOUNTS ---------------- #
    discount_10 = 0
    discount_5 = 0

    # Rule 1: 10% discount if total > ₹10,000
    if grand_total > 10000:
        discount_10 = grand_total * 0.10
        grand_total -= discount_10

    # Rule 2: Additional 5% discount if qty > 20 (after first discount)
    if total_qty > 20:
        discount_5 = grand_total * 0.05
        grand_total -= discount_5

    print("\n------- Discounts Applied -------")
    print(f"10% Discount (if > 10000):        ₹{discount_10:.2f}")
    print(f"5% Quantity Discount (if qty>20): ₹{discount_5:.2f}")

    print("\n==============================")
    print(f"FINAL GRAND TOTAL: ₹{grand_total:.2f}")
    print("==============================")

