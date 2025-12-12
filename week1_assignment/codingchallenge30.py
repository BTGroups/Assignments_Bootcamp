# ------------------ Functions ------------------ #

def get_item_details(promo_codes):
    """
    Accepts item details and applies item-level promotional discount if applicable.
    Returns item total and quantity.
    """
    try:
        item_code = input("Enter Item Code: ").strip()
        description = input("Enter Item Description: ").strip()

        qty = int(input("Enter Quantity: "))
        if qty <= 0:
            print("Error: Quantity must be positive.")
            return 0, 0

        price = float(input("Enter Price per Item: "))
        if price < 0:
            print("Error: Price cannot be negative.")
            return 0, 0

        item_total = qty * price
        promo_discount = 0
        if item_code.upper() in promo_codes:
            promo_discount = item_total * promo_codes[item_code.upper()]
            item_total -= promo_discount
            print(f"Promotional discount applied: ₹{promo_discount:.2f}")

        print(f"Item Total after discount: ₹{item_total:.2f}")
        return item_total, qty

    except ValueError:
        print("Error: Invalid number entered.")
        return 0, 0

def calculate_grand_total(promo_codes):
    """
    Iteratively accepts multiple items and calculates the grand total.
    """
    grand_total = 0
    total_qty = 0

    while True:
        item_total, qty = get_item_details(promo_codes)
        grand_total += item_total
        total_qty += qty

        more = input("Add another item? (y/n): ").strip().lower()
        if more != 'y':
            break

    return grand_total, total_qty

def apply_discounts(grand_total, total_qty, is_member):
    """
    Apply sequential discounts: 10% over 10000, 5% quantity, 2% membership
    """
    discount_10 = 0
    discount_5 = 0
    membership_discount = 0

    if grand_total > 10000:
        discount_10 = grand_total * 0.10
        grand_total -= discount_10

    if total_qty > 20:
        discount_5 = grand_total * 0.05
        grand_total -= discount_5

    if is_member:
        membership_discount = grand_total * 0.02
        grand_total -= membership_discount

    return grand_total, discount_10, discount_5, membership_discount

def apply_tax(grand_total):
    """
    Apply tiered tax based on grand total
    """
    if grand_total < 5000:
        tax_rate = 0.05
    elif grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    tax_amount = grand_total * tax_rate
    grand_total += tax_amount
    return grand_total, tax_rate, tax_amount



def main():
    print("=== Welcome to the Billing System ===")
    promo_codes = {"PROMO10": 0.10}  # Item code: discount %

    # --- Enter multiple items ---
    grand_total, total_qty = calculate_grand_total(promo_codes)

    print("\n==============================")
    print(f"Subtotal (Before Discounts): ₹{grand_total:.2f}")
    print(f"Total Quantity of Items: {total_qty}")

    # --- Membership ---
    member = input("Is the customer a member? (y/n): ").strip().lower()
    is_member = member == 'y'

    # --- Apply discounts ---
    grand_total, discount_10, discount_5, membership_discount = apply_discounts(grand_total, total_qty, is_member)

    print("\n------- Discounts Applied -------")
    print(f"10% Discount (if subtotal>10000): ₹{discount_10:.2f}")
    print(f"5% Quantity Discount (if qty>20): ₹{discount_5:.2f}")
    print(f"Membership Discount (2%): ₹{membership_discount:.2f}")

    # --- Apply tax ---
    grand_total, tax_rate, tax_amount = apply_tax(grand_total)

    print("\n------- Tax Applied -------")
    print(f"Tax Rate: {int(tax_rate*100)}%")
    print(f"Tax Amount: ₹{tax_amount:.2f}")

    print("\n==============================")
    print(f"FINAL GRAND TOTAL: ₹{grand_total:.2f}")
    print("==============================")

main()