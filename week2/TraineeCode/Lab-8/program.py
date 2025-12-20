from decimal_splitter import DecimalSplitter

class Program:
    @staticmethod
    def main(args):
        number = 0.0
        # Accept the value through command prompt
        number = float(args[0])

        # Display the whole and the fractional part from the given number
        print("Number entered is : " + str(number))
        print("Whole part of the given number is : " + str(DecimalSplitter.get_whole(number)))
        print("Fractional part of the given number is : " + str(DecimalSplitter.get_fraction(number)))

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
