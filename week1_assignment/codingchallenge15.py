from tabulate import tabulate

def calculate_tax(income):
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
    breakdown = []

    for limit, rate in slabs:
        if income > prev_limit:
            taxable_amount = min(income, limit) - prev_limit
            slab_tax = taxable_amount * rate
            tax += slab_tax
            breakdown.append((prev_limit + 1, int(limit), rate, slab_tax))
            prev_limit = limit
        else:
            break

    if income <= 700000:
        tax = 0
        cess = 0
    else:
        cess = tax * 0.04
        tax += cess

    return tax, breakdown, cess

def generate_report_table(name, emp_id, monthly_salary):
    annual_gross = monthly_salary * 12
    total_tax, breakdown, cess = calculate_tax(annual_gross)
    annual_net = annual_gross - total_tax

    # Employee Details Table
    emp_details = [[
        name,
        emp_id,
        f"₹{monthly_salary:.2f}",
        f"₹{annual_gross:.2f}",
        f"₹{annual_net:.2f}"
    ]]
    print("\nEmployee Summary:")
    print(tabulate(emp_details, headers=["Name", "EmpID", "Gross Monthly", "Annual Gross", "Net Salary"], tablefmt="grid"))

    # Taxable Income & Total Tax
    summary = [["Taxable Income", f"₹{annual_gross:.2f}"],
               ["Total Tax Payable", f"₹{total_tax:.2f}"]]
    print("\nTax Summary:")
    print(tabulate(summary, tablefmt="grid"))

    # Tax Breakdown Table
    breakdown_table = []
    for start, end, rate, tax_amt in breakdown:
        breakdown_table.append([f"₹{start}-{end}", f"{int(rate*100)}%", f"₹{tax_amt:.2f}"])
    if annual_gross > 700000:
        breakdown_table.append(["Cess (4%)", "-", f"₹{cess:.2f}"])
    
    print("\nTax Breakdown by Slabs:")
    print(tabulate(breakdown_table, headers=["Slab Range", "Rate", "Tax Amount"], tablefmt="grid"))

def main():
    try:
        name = input("Enter Employee Name: ").strip()
        emp_id = input("Enter Employee ID: ").strip()
        monthly_salary = float(input("Enter Gross Monthly Salary (₹): "))
        if monthly_salary < 0:
            raise ValueError("Salary cannot be negative.")

        generate_report_table(name, emp_id, monthly_salary)

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
