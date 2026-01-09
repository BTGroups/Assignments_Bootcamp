import calendar 

def leapyear(year : int) -> int:
    if ((year % 4 == 0)and (year %100 != 0)) or (year % 400 == 0):
        return True
    return False 

print(leapyear(2024))

class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
    def setageandname(self, name, age):
        self.name = name 
        