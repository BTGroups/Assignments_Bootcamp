class Employee:
    """
    Properties of the class
    """
    def __init__(self):
        self.emp_id = ""
        self.name = ""
        self.basic = 0.0
        self.hra = 0.0
        self.allowance_percentage = 0.0
        self.role = 0
    def set_emp_details(self, emp_id, name, basic, hra, allowance_percentage, role_id):
        self.emp_id = emp_id
        self.name = name 
        self.basic = float(basic)
        self.hra = float(hra) 
        self.allowance_percentage = float(allowance_percentage)
        self.role = role_id

    def get_emp_id(self):
        return self.emp_id

    def get_name(self):
        return self.name

    def get_basic(self):
        return self.basic

    def get_hra(self):
        return self.hra

    def get_allowance_percentage(self):
        return self.allowance_percentage

    def get_role_id(self):
        return self.role