if __name__ == "__main__":
    try:
        item_code = input("Enter Item Code: ").strip()
        description = input("Enter Item Description: ").strip()

        qty = int(input("Enter Quantity: "))
        if qty <= 0:
            print("Error: Quantity must be a positive number.")

        price = float(input("Enter Price per Item: "))
        if price < 0:
            print("Error: Price cannot be negative.")

        total = qty * price

        print("\n--- Item Total ---")
        print(f"Item Code       : {item_code}")
        print(f"Description     : {description}")
        print(f"Quantity        : {qty}")
        print(f"Price per Item  : ₹{price:.2f}")
        print(f"Total Cost      : ₹{total:.2f}")

    except ValueError:
        print("Error: Please enter valid numeric values for quantity and price.")


