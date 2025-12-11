def calculate_tax(income):
    """Calculate tax based on New Tax Regime 2023 with slab-wise breakdown, 87A rebate, and cess."""
    if income < 0:
        raise ValueError("Income cannot be negative.")
    
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
    for limit, rate in slabs:
        if income > prev_limit:
            taxable_amount = min(income, limit) - prev_limit
            slab_tax = taxable_amount * rate
            tax += slab_tax
            print(f"Income ₹{prev_limit+1} to ₹{int(limit)} taxed at {int(rate*100)}%: ₹{slab_tax:.2f}")
            prev_limit = limit
        else:
            break
    if income <= 700000:
        print("\nEligible for Section 87A rebate. Tax payable = ₹0")
        tax = 0
        cess = 0
    else:
        cess = tax * 0.04
        tax += cess
        print(f"\nHealth & Education Cess (4%): ₹{cess:.2f}")

    print(f"\nTotal Tax Payable: ₹{tax:.2f}")
    return tax

def main():
    while True:
        try:
            gross_input = input("Enter your annual gross salary (₹): ")
            gross_salary = float(gross_input)
            if gross_salary < 0:
                raise ValueError("Salary cannot be negative.")

            total_tax = calculate_tax(gross_salary)
            net_salary = gross_salary - total_tax

            print("\n--- Net Salary Summary ---")
            print(f"Annual Gross Salary : ₹{gross_salary:.2f}")
            print(f"Total Tax Payable   : ₹{total_tax:.2f}")
            print(f"Annual Net Salary   : ₹{net_salary:.2f}")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
