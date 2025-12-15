import math
try:
    num = float(input("Enter a decimal number: "))

    whole_part = math.floor(num)
    fractional_part = num - whole_part
    
    print("Whole part:", whole_part)
    print("Fractional part:", round(fractional_part, 6))
except ValueError:
    print("Invalid input. Please enter a valid decimal number.")