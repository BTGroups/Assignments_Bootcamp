def calculate_taxable_income(annual_gross_salary: float):
    STANDARD_DEDUCTION = 50000  # ₹50,000 deduction

    taxable_income = annual_gross_salary - STANDARD_DEDUCTION

    # Taxable income cannot be negative
    if taxable_income < 0:
        taxable_income = 0

    return STANDARD_DEDUCTION, taxable_income


if __name__ == "__main__":
    try:
        annual_gross_salary = float(input("Enter Annual Gross Salary (₹): "))

        deduction, taxable_income = calculate_taxable_income(annual_gross_salary)

        print("\n------ Taxable Income Calculation ------")
        print(f"Annual Gross Salary : ₹{annual_gross_salary:,.2f}")
        print(f"Standard Deduction  : ₹{deduction:,.2f}")
        print(f"Taxable Income      : ₹{taxable_income:,.2f}")

    except ValueError:
        print("Please enter valid numeric values.")
    except Exception as e:
        print(f"Error: {e}")
