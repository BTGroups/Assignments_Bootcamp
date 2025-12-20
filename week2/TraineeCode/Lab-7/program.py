from result_finder import ResultFinder
import sys
def validate_mark(mark_str):
    try:
        mark = int(mark_str)
        if 0 <= mark <= 100:
            return mark 
        else:
            raise ValueError
    except ValueError:
        print(f"Invalid mark '{mark_str}'. Enter an integer between 0 and 100")
        exit(1)

class Program:
    @staticmethod
    def main(args):
        # Accept the values from command line arguments
        marks1 = validate_mark(args[0])
        marks2 = validate_mark(args[1])
        marks3 = validate_mark(args[2])

        # Store the values entered in the object
        finder = ResultFinder()
        finder.marks1 = marks1
        finder.marks2 = marks2
        finder.marks3 = marks3

        # Display all the information with the help of get and other methods
        print("Marks entered------------- ")
        print("Marks 1 : " + str(finder.marks1))
        print("Marks 2 : " + str(finder.marks2))
        print("Marks 3 : " + str(finder.marks3))
        print("Total : " + str(finder.get_total()))
        print("Average : " + str(finder.get_average()))
        print("Result : " + str(finder.get_result()))

        input("Enter to quit")


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
