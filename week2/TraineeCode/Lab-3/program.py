from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        emp.ID = 101
        emp.Name = "Ravi"
        emp.Gender = "Male"

        emp.address.address1 = "12, MG Road"
        emp.address.address2 = "Near Bus Stand"
        emp.address.city = "Chennai"
        emp.address.pincode = "600001"


    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        print("Employee Id : " + str(emp.ID))
        print("Employee Name : " + str(emp.Name))
        print("Employee Gender : " + str(emp.Gender))

        print("Employee Address : --------------")
        print("Address 1 : ", emp.address.address1)
        print("Address 2 : ", emp.address.address2)
        print("City : ", emp.address.city)
        print("PinCode : ", emp.address.pincode)
        print("----------------------------------")



if __name__ == "__main__":
    Program.main([])
