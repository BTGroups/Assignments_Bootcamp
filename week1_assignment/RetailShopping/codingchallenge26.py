if __name__ == "__main__":
    grand_total = 0.0

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

            print(f"Item Total: ₹{total:.2f}")

        except ValueError:
            print("Error: Invalid number entered. Try again.")
            continue

        # Ask user if they want to continue
        more = input("Add another item? (y/n): ").strip().lower()
        if more != 'y':
            break

    print("\n==============================")
    print(f"GRAND TOTAL FOR ALL ITEMS: ₹{grand_total:.2f}")
    print("==============================")

# Run
