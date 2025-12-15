def calculate_salaries(basic: float, allowance: float, bonus_percent: float):
    """Calculate gross monthly salary and annual gross salary."""
    
    gross_monthly = basic + allowance

    # Annual salary before bonus
    annual_without_bonus = gross_monthly * 12

    # Bonus is percentage of annual gross salary
    bonus_amount = (bonus_percent / 100) * annual_without_bonus

    # Total Annual Gross Salary
    annual_gross_salary = annual_without_bonus + bonus_amount

    return gross_monthly, annual_gross_salary


if __name__ == "__main__":
    try:
        name = input("Enter Employee Name: ")
        emp_id = input("Enter Employee ID: ")
        basic_salary = float(input("Enter Basic Monthly Salary: "))
        special_allowances = float(input("Enter Special Allowances (Monthly): "))
        bonus_percent = float(input("Enter Bonus Percentage (% of Annual Gross Salary): "))

        # Calculate salaries
        gross_monthly, annual_gross = calculate_salaries(
            basic_salary, special_allowances, bonus_percent
        )

        # Display Output
        print("\n------ Employee Salary Details ------")
        print(f"Name               : {name}")
        print(f"Employee ID        : {emp_id}")
        print(f"Basic Salary       : ₹{basic_salary:,.2f}")
        print(f"Allowances         : ₹{special_allowances:,.2f}")
        print(f"Gross Monthly Pay  : ₹{gross_monthly:,.2f}")
        print(f"Annual Gross Salary: ₹{annual_gross:,.2f}")

    except ValueError:
        print("ValueError: Please enter valid numeric values for salary and percentages.")
    except Exception as e:
        print(f"Unexpected Error ({type(e).__name__}): {e}")
