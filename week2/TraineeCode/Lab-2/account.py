class Account:
    """
    Fields for the class
    """
    _acc_no = None
    _name = None
    _balance = 0.0

    """
    Properties for the fields
    """
    @property
    def acc_no(self):
        return self._acc_no

    @acc_no.setter
    def acc_no(self, value):
        bank_code = "ICI"
        self._acc_no = bank_code + value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def balance(self):
        return self._balance + self.compute_interest()

    @balance.setter
    def balance(self, value):
        self._balance = value

    """
    Method to calculate the interest for an account
    """
    """
    returns Interest
    """
    def compute_interest(self):
        interest = self._balance * 8.5 / 100.0
        return interest
