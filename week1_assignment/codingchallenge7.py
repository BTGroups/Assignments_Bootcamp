def check_tax(name: str, salary: float):
    if salary > 300000:
        return f"{name} must pay tax."
    else:
        return f"{name} does NOT need to pay tax."


if __name__ == "__main__":
    try:
        name = input("Enter your name: ")
        salary = float(input("Enter your salary: "))

        print(check_tax(name, salary))
    except ValueError:
        print("ValueError: Salary must be a number.")
    except Exception as e:
        print(f"Unexpected Error ({type(e).__name__}): {e}")
