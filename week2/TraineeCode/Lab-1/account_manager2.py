class AccountManager2:
    """
    Method to fill account details into the account object passed
    """
    def fill_account_data(self, acc):
        acc.acc_no = "004701"
        acc.name = "Nitesh"
        acc.balance = 45000.0

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print("AccNo : " + acc.acc_no)
        print("Name : " + acc.name)
        print("Balance : " + str(acc.balance))
