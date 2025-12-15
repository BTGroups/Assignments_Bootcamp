try:
    n = input("Enter the number: ")

    digit_map = {
        '0': "zero",
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine"
    }
    
    for digit in n:
        print(digit_map[digit], end=" ")

        
except KeyError:
    print("Please enter digits only (0–9).")


except ValueError:
    print("Invalid input.Please enter only numbers")