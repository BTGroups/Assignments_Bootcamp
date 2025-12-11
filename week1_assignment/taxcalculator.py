def calculate_tax(taxable_income: float) -> tuple:
    """
    Calculate tax using:
    - New Tax Regime slabs
    - Section 87A rebate
    - 4% Health & Education Cess
    Returns: (base_tax, cess, total_tax)
    """

    tax = 0

    # ---------- TAX SLABS ----------
    if taxable_income > 1500000:
        tax += (taxable_income - 1500000) * 0.30
        taxable_income = 1500000

    if taxable_income > 1200000:
        tax += (taxable_income - 1200000) * 0.20
        taxable_income = 1200000

    if taxable_income > 900000:
        tax += (taxable_income - 900000) * 0.15
        taxable_income = 900000

    if taxable_income > 600000:
        tax += (taxable_income - 600000) * 0.10
        taxable_income = 600000

    if taxable_income > 300000:
        tax += (taxable_income - 300000) * 0.05
        taxable_income = 300000

    # ---------- 87A REBATE ----------
    if taxable_income <= 700000:
        tax = 0

    # ---------- 4% CESS ----------
    cess = tax * 0.04
    total_tax = tax + cess

    return tax, cess, total_tax



def generate_employee_report(name, emp_id, basic, allowances):
    """Compute salaries, taxable income, tax and net salary."""

    # STEP 1 — Gross Salary
    gross_monthly = basic + allowances
    gross_annual = gross_monthly * 12

    # STEP 2 — Taxable Income
    STANDARD_DEDUCTION = 50000
    taxable_income = max(0, gross_annual - STANDARD_DEDUCTION)

    # STEP 3 — Tax Calculation
    base_tax, cess, total_tax = calculate_tax(taxable_income)

    # STEP 4 — Net Salary
    net_salary = gross_annual - total_tax

    # ---------- REPORT ----------
    print("\n========== EMPLOYEE TAX REPORT ==========")
    print(f"Employee Name        : {name}")
    print(f"Employee ID          : {emp_id}")
    print("------------------------------------------")
    print(f"Gross Monthly Salary : ₹{gross_monthly:,.2f}")
    print(f"Gross Annual Salary  : ₹{gross_annual:,.2f}")
    print("------------------------------------------")
    print(f"Standard Deduction   : ₹{STANDARD_DEDUCTION:,.2f}")
    print(f"Taxable Income       : ₹{taxable_income:,.2f}")
    print("------------------------------------------")
    print(f"Base Tax (Slabs)     : ₹{base_tax:,.2f}")
    print(f"4% Cess              : ₹{cess:,.2f}")
    print(f"TOTAL TAX PAYABLE    : ₹{total_tax:,.2f}")
    print("------------------------------------------")
    print(f"NET ANNUAL SALARY    : ₹{net_salary:,.2f}")
    print("==========================================\n")



if __name__ == "__main__":
    try:
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        basic = float(input("Enter Basic Monthly Salary (₹): "))
        allowances = float(input("Enter Special Allowances (₹): "))

        generate_employee_report(name, emp_id, basic, allowances)

    except ValueError:
        print("Please enter valid numeric values.")
    except Exception as e:
        print(f"Error occurred: {e}")
