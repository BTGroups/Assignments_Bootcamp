from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        employees = [None] * 4
        print("Enter employee information")

        for i in range(len(employees)):
            while True:   # allows re-entry for SAME employee
                emp = Employee()
                print("\nEmployee No : " + str(i + 1))

                emp_id = input("Id : ").strip()

                while True:
                    name = input("Name : ").strip()
                    if name.replace(" ", "").isalpha():
                        break
                    print("Invalid name. Only alphabets allowed.")

                # Basic
                while True:
                    try:
                        basic = float(input("Basic : "))
                        break
                    except ValueError:
                        print("Enter numeric value for Basic.")

           
                while True:
                    try:
                        hra = float(input("HRA : "))
                        break
                    except ValueError:
                        print("Enter numeric value for HRA.")

    
                while True:
                    try:
                        allowance_percentage = float(input("Percentage of Allowance : "))
                        break
                    except ValueError:
                        print("Enter numeric value for Allowance Percentage.")

          
                print("Enter Role Id : ")
                print(f"{Roles.DEVELOPER}. {RoleBuilder.get_role_description(Roles.DEVELOPER)}")
                print(f"{Roles.TEST_ENGINEER}. {RoleBuilder.get_role_description(Roles.TEST_ENGINEER)}")
                print(f"{Roles.SR_DEVELOPER}. {RoleBuilder.get_role_description(Roles.SR_DEVELOPER)}")
                print(f"{Roles.DESIGNER}. {RoleBuilder.get_role_description(Roles.DESIGNER)}")

                while True:
                    try:
                        role = int(input("Role : "))
                        if 1 <= role <= 4:
                            break
                        print("Role must be between 1 and 4.")
                    except ValueError:
                        print("Enter numeric role id.")

                # Confirmation
                print("\nYou entered:")
                print(f"Id: {emp_id}")
                print(f"Name: {name}")
                print(f"Basic: {basic}")
                print(f"HRA: {hra}")
                print(f"Allowance %: {allowance_percentage}")
                print(f"Role: {role}")

                confirm = input("\nDo you want to change anything? (Y/N): ").strip().upper()

                if confirm == "N":
                    emp.set_emp_details(emp_id, name, basic, hra, allowance_percentage, role)
                    employees[i] = emp
                    break   
                else:
                    print("\nRe-enter employee details...\n")

        # Report section
        report_date = input("\nEnter the date of the report (dd/mm/yyyy) : ").strip()
        report = EmployeeReport()
        report.report_date = report_date
        report.display_employees(employees)

        input("\nPress Enter to exit...")


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
