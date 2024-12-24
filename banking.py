from account import Account, exit_function
import database_handler


class Banking:

    def __init__(self):
        self.connection = database_handler.connect()
        self.menu()
        self.connection.close()

    def menu(self):
        selection = input("1. Create an account\n2. Log into account\n0. Exit\n")
        if selection == '1':
            self.create_account()
        if selection == '2':
            self.log_account()
        if selection == '0':
            exit_function()

        print()
        self.menu()

    def create_account(self):
        new_account = Account()
        new_account.generate()
        print("\nYour card has been created")
        print("Your card number:")
        print(new_account.card_number)
        print("Your card PIN:")
        print(new_account.pin)

        database_handler.insert_card(self.connection, new_account)

    def log_account(self):
        card_number = input("\nEnter your card number:\n")
        pin = input("Enter your PIN:\n")

        query_result = database_handler.select_card(self.connection, card_number)

        if query_result is not None and query_result[2] == pin:
            print("\nYou have successfully logged in!")
            Account(query_result[0], query_result[1], query_result[2], query_result[3]).menu(self.connection)
            return

        print("\nWrong card number or PIN!\n")
        self.menu()
        return


if __name__ == "__main__":
    Banking()
