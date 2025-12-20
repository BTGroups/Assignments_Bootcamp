"""
Class to represent employee information
"""
from address import Address
class Employee:
    def __init__(self):
        self.ID = 0
        self.Name = ""
        self.gender = ""
        self.address = Address()
    