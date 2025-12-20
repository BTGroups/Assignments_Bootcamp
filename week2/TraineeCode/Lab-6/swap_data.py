class SwapData:
    """
    Properties of the class
    """
    def __init__(self):
        self.number1 = 0
        self.number2 = 0

    """
    Method to swap numbers of the class
    """
    def swap_values(self):
        self.number1 , self.number2 = self.number2, self.number1

    """
    Method to display the numbers before and after swapping
    """
    def display_values(self, str_msg):
        print(str_msg)
        print("Number 1 = " + str(self.number1))
        print("Number 2 = " + str(self.number2))
