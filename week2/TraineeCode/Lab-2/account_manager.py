class AccountManager:
    """
    Method to store account details into the account object passed
    """
    def fill_account_data(self, acc):
        pass

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print()
        print("AccNo : " + (str(acc.acc_no)))
        print("Name : " + str(acc.name))
        print("Balance : " + str(acc.balance))


'''
concatenation wasnt possible from integer to string, hence I changed it to a str to concatenate

'''