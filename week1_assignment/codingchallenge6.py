def isevenorodd(num: int) -> str:
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = isevenorodd(number)
        print(f"The number {number} is {result}")
    except ValueError:
        print("ValueError : Please enter a valid integer")
    except Exception as e:
        print(f"Expected Error : ({type(e).__name__}) : {e}")
    