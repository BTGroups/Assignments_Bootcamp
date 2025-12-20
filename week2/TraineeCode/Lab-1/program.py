from account import Account
from account_manager1 import AccountManager1
from account_manager2 import AccountManager2


class Program:
    @staticmethod
    def main(args):
        
        acc = Account()

        print("Performing Account Transactions using Account Manager 1...")
        manager1 = AccountManager1()
        manager1.fill_account_data(acc)
        manager1.display_account_data(acc)
        

        print()

        print("Performing Account Transactions using Account Manager 2...")
        manager2 = AccountManager2()
        manager2.fill_account_data(acc)
        manager2.display_account_data(acc)
        
        input()


if __name__ == "__main__":
    Program.main([])
