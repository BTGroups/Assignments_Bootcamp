def calculate_tax(income):
    """Calculate tax based on New Tax Regime 2023 with slab-wise breakdown, 87A rebate, and cess."""
    if income < 0:
        raise ValueError("Income cannot be negative.")
    
    # Define tax slabs and rates
    slabs = [
        (300000, 0.0),
        (600000, 0.05),
        (900000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30)
    ]

    tax = 0
    prev_limit = 0

    print("\n--- Tax Calculation Breakdown ---")
    # Calculate tax slab-wise
    for limit, rate in slabs:
        if income > prev_limit:
            taxable_amount = min(income, limit) - prev_limit
            slab_tax = taxable_amount * rate
            tax += slab_tax
            print(f"Income ₹{prev_limit+1} to ₹{int(limit)} taxed at {int(rate*100)}%: ₹{slab_tax:.2f}")
            prev_limit = limit
        else:
            break

    # Apply Section 87A rebate if applicable
    if income <= 700000:
        print("\nEligible for Section 87A rebate. Tax payable = ₹0")
        tax = 0
        cess = 0
    else:
        # Add 4% Health and Education Cess
        cess = tax * 0.04
        tax += cess
        print(f"\nHealth & Education Cess (4%): ₹{cess:.2f}")

    print(f"\nTotal Tax Payable: ₹{tax:.2f}")
    return tax, cess

def main():
    """Main function to get user input and calculate tax."""
    while True:
        try:
            income_input = input("Enter your taxable income (₹): ")
            income = float(income_input)
            calculate_tax(income)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for income.")

# Run the program
if __name__ == "__main__":
    main()
