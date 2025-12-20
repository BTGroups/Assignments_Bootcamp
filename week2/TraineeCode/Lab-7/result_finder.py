class ResultFinder:
    """
    Properties of the fields of this class
    """
    def __init__(self):
        self.marks1 = 0
        self.marks2 = 0
        self.marks3 = 0
        #new properites
        self.total = 0
        self.average = 0
        self.result = ""

    """
    Method to display marks obtained
    """
    def display_marks(self):
        print("1st sub marks: ", self.marks1)
        print("2nd sub marks: ", self.marks2)
        print("3rd sub marks: ", self.marks3)


    """
    Method to get the total of the marks in subjects
    """
    def get_total(self):
        self.total = self.marks1 + self.marks2 + self.marks3
        return self.total

    """
    Method to calculate the average of the marks
    """
    def get_average(self):
        self.average = (self.marks1 + self.marks2 + self.marks3) / 3
        return self.average
    """
    Method to get the result for the marks given
    """
    def get_result(self):
        if self.marks1 >= 35 and self.marks2 >= 35 and self.marks3 >= 35:
            self.result = "pass"
        else :
            self.result = "fail"
        return self.result
