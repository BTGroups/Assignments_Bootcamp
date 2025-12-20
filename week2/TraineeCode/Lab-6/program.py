from swap_data import SwapData

class Program:
    @staticmethod
    def main(args):
        while True:
            try:
                number1 = int(input("Enter Number 1: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        while True:
            try:
                number2 = int(input("Enter Number 2: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")


        # Storing the numbers accepted in SwapData object
        obj = SwapData()
        obj.number1 = number1
        obj.number2 = number2

        # Display numbers before swapping
        obj.display_values("Numbers before Swapping :")
        
        # Swapping the numbers in the object
        obj.swap_values()

        # Display numbers after swapping
        obj.display_values("Numbers after Swapping :")

        input("press enter to exit")


if __name__ == "__main__":
    Program.main([])
