def largest_of_three(a: float, b: float, c: float) -> float:
    return max(a, b, c)


if __name__ == "__main__":
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        z = float(input("Enter third number: "))

        print("The largest number is:", largest_of_three(x, y, z))

    except ValueError:
        print("ValueError: Please enter numeric values only.")
    except Exception as e:
        print(f"Unexpected Error ({type(e).__name__}): {e}")
