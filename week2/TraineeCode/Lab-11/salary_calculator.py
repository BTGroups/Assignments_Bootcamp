
class SalaryCalculator:
    """
    Method to calculate the salary of an employee
    """
    @staticmethod
    def get_salary(emp ):
        salary = 0

        # Original python code has no calculation here
        salary = emp.basic + emp.hra + SalaryCalculator.get_allowance(emp)
        return salary

    """
    Method to get the allowance for an employee based on the percentage
    """
    @staticmethod
    def get_allowance(emp):
        allowance = (emp.basic * emp.allowance_percentage / 100.0)
        return allowance
