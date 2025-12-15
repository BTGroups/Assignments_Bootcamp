def is_leap_year(year: int) -> bool:
    # Leap year rules:
    # - Divisible by 4
    # - If divisible by 100, must also be divisible by 400
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


if __name__ == "__main__":
    try:
        year = int(input("Enter a year: "))

        if is_leap_year(year):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is NOT a Leap Year.")

    except ValueError:
        print("ValueError: Please enter a valid year number.")
    except Exception as e:
        print(f"Unexpected Error ({type(e).__name__}): {e}")
