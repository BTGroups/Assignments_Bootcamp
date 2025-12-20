class AccountManager1:
    """
    Method to fill account details into the account object passed
    """
    def fill_account_data(self, acc):
        acc._acc_no = "004701"
        acc._name = "Nitesh"
        acc._balance = 45000.0

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print("AccNo : " + acc._acc_no)
        print("Name : " + acc._name)
        print("Balance : " + str(acc._balance))
