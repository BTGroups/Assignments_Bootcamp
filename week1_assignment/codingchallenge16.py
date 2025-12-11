import re

def validate_name(name):
    """Validate employee name: non-empty, alphabets only, max 50 chars."""
    if not name.strip():
        return False, "Name cannot be empty."
    if len(name) > 50:
        return False, "Name cannot exceed 50 characters."
    if not re.match("^[A-Za-z ]+$", name):
        return False, "Name must contain alphabets and spaces only."
    return True, ""

def validate_emp_id(emp_id):
    """Validate EmpID: alphanumeric, 5-10 characters."""
    if not re.match("^[A-Za-z0-9]{5,10}$", emp_id):
        return False, "EmpID must be alphanumeric and 5–10 characters long."
    return True, ""

def validate_positive_number(value, field_name, max_value=None, allow_zero=False):
    """Validate a positive numeric input."""
    try:
        num = float(value)
        if allow_zero and num < 0:
            return False, f"{field_name} cannot be negative."
        if not allow_zero and num <= 0:
            return False, f"{field_name} must be greater than 0."
        if max_value and num > max_value:
            return False, f"{field_name} cannot exceed ₹{max_value:,.0f}."
        return True, num
    except ValueError:
        return False, f"{field_name} must be a numeric value."

def validate_bonus(value):
    """Validate bonus percentage: 0–100."""
    try:
        num = float(value)
        if num < 0 or num > 100:
            return False, "Bonus percentage must be between 0 and 100."
        return True, num
    except ValueError:
        return False, "Bonus percentage must be numeric."

def get_valid_input(prompt, validation_func, *args):
    """Prompt user repeatedly until valid input is entered."""
    while True:
        value = input(prompt)
        valid, result = validation_func(value, *args)
        if valid:
            return result
        else:
            print(f"Invalid input: {result}. Please try again.\n")

def main():
    print("=== Employee Input Validation ===\n")
    
    # Employee Details
    name = get_valid_input("Enter Employee Name: ", validate_name)
    emp_id = get_valid_input("Enter Employee ID: ", validate_emp_id)
    
    # Salary Inputs
    basic_salary = get_valid_input("Enter Basic Salary (₹): ", validate_positive_number, "Basic Salary", 10000000)
    allowances = get_valid_input("Enter Special Allowances (₹): ", validate_positive_number, "Special Allowances", 10000000, True)
    bonus_pct = get_valid_input("Enter Bonus Percentage (%): ", validate_bonus)
    
    # Derived Calculations
    gross_monthly = basic_salary + allowances + (basic_salary * bonus_pct / 100)
    if gross_monthly <= 0:
        print("Error: Gross Monthly Salary must be greater than zero. Please re-enter salary details.")
        return
    
    annual_gross = gross_monthly * 12
    if annual_gross > 100000000:  # Arbitrary realistic limit
        print("Error: Annual Gross Salary exceeds realistic limits. Please re-enter salary details.")
        return
    
    print("\nAll inputs are valid.")
    print(f"Gross Monthly Salary: ₹{gross_monthly:.2f}")
    print(f"Annual Gross Salary : ₹{annual_gross:.2f}")

if __name__ == "__main__":
    main()
