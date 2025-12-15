try:
    num = int(input("Enter a number: "))

    original_num = abs(num)
    reverse_num = 0

    while original_num > 0:
        digit = original_num % 10
        reverse_num = reverse_num * 10 + digit
        original_num //= 10

    # Preserve negative sign if needed
    if num < 0:
        reverse_num = -reverse_num

    print("Reversed number:", reverse_num)

except ValueError:
    print("Invalid input. Please enter an integer.")
