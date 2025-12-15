if __name__ == "__main__":
    try:
        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))

        # swapping values
        a, b = b, a

        print("The first value after swapping:", a)
        print("The second value after swapping:", b)

    except ValueError:
        print("❌ ValueError: Please enter numeric values only.")

    except TypeError:
        print("❌ TypeError: Invalid data type encountered.")

    except Exception as e:
        print(f"❌ Unexpected Error ({type(e).__name__}): {e}")
