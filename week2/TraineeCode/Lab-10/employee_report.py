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

    print(f"{'EMP_ID':<8}"
          f"{'NAME':<10}"
          f"{'ROLE':<18}"
          f"{'BASIC':>10}"
          f"{'HRA':>8}"
          f"{'ALLOW':>10}"
          f"{'SALARY':>10}")
    self.print_line()

    for emp in employees:
        role_desc = RoleBuilder.get_role_description(emp.get_role_id())
        allowance = SalaryCalculator.get_allowance(emp)
        salary = SalaryCalculator.get_salary(emp)

        print(f"{emp.get_emp_id():<8}"
              f"{emp.get_name():<10}"
              f"{role_desc:<18}"
              f"{emp.get_basic():>10.2f}"
              f"{emp.get_hra():>8.2f}"
              f"{allowance:>10.2f}"
              f"{salary:>10.2f}")

    self.display_footer(len(employees))

