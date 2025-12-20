class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    def get_whole(number):
        return int(number)

    """
    Method to get the fractional part of a double number
    """
    def get_fraction(number):
        whole = int(number)
        return number - whole

    """
    Method to check if a given number is odd or even
    """
    def is_odd(number):
        if number % 2 == 0:
            return "is not odd"
        else:
            return "is odd"
