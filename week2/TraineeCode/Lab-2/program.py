from account import Account
from account_manager import AccountManager

class Program:
    @staticmethod
    def main(args):
        acc = Account()

        print("Performing Account Transactions using AccManager...")
        manager = AccountManager()
        manager.fill_account_data(acc)
        manager.display_account_data(acc)

        input()

if __name__ == "__main__":
    Program.main([])
