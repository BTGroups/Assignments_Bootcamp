from employee import Employee
from role_builder import RoleBuilder
from salary_calculator import SalaryCalculator
class EmployeeReport:
    """
    Property of the class
    """
    def __init__(self):
        self.report_date = ""

    """
    Method to print a line in a report
    """
    def print_line(self):
        print("---------------------------------------------------------------------------")

    """
    Method to display header information of the report
    """
    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT\t\t\t\t")
        print("Date : " + self.report_date)
        self.print_line()

    """
    Method to display footer information in the report
    """
    def display_footer(self, count):
        self.print_line()
        print("Total Employees : " + str(count))
        self.print_line()

    """
    Method to display employees information
    """
    def display_employees(self, employees):
        self.display_header()

        print("EMP_ID\tNAME\tROLE\t\tBASIC\tHRA\tALLOW\tSALARY")
        self.print_line()

        for emp in employees:
            role_desc = RoleBuilder.get_role_description(emp.get_role_id())
            allowance = SalaryCalculator.get_allowance(emp)
            salary = SalaryCalculator.get_salary(emp)

            print(
                f"{emp.get_emp_id()}\t"
                f"{emp.get_name()}\t"
                f"{role_desc}\t"
                f"{emp.get_basic():.2f}\t"
                f"{emp.get_hra():.2f}\t"
                f"{allowance:.2f}\t"
                f"{salary:.2f}"
            )
        # Placeholder for employee information printing
        # Original C# code does not include the loop for displaying details

        self.display_footer(len(employees))
