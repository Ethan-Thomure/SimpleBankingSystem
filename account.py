from random import choice
import string
import database_handler


def exit_function():
    print("\nBye!")
    exit()


def random_num_append(initial_digits="", length=4):
    return initial_digits + "".join(choice(string.digits) for _ in range(length))


def luhn_parity_bit(card_number):
    card_number = card_number[:15]  # taking off last digit
    current_sum = 0
    for i in range(0, len(card_number)):
        if i % 2 == 0:  # starts at zero, which is technically even
            if (int(card_number[i]) * 2) > 9:
                current_sum += int(card_number[i]) * 2 - 9
            else:
                current_sum += (int(card_number[i]) * 2)
        else:
            current_sum += int(card_number[i])

    return (10 - current_sum % 10) if current_sum % 10 != 0 else 0


class Account:

    def generate(self):
        self.card_number = self.generate_card_number()
        self.pin = random_num_append()
        return

    def __init__(self, identification=0, card_number=0, pin=0, balance=0):
        self.identification = identification
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    @staticmethod
    def generate_card_number():
        number = random_num_append("400000", 9)

        return ''.join((number, str(luhn_parity_bit(number))))

    def find_balance(self):
        print(f"\nBalance: {self.balance}")
        return

    @staticmethod
    def log_out():
        print("\nYou have successfully logged out!\n")
        return

    def menu(self, connection):
        print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")

        selection = input()
        if selection == "1":
            self.find_balance()
        elif selection == "2":
            self.add_income(connection)
        elif selection == "3":
            self.transfer(connection)
        elif selection == "4":
            self.close_account(connection)
            return
        elif selection == "5":
            self.log_out()
            return
        elif selection == "0":
            exit_function()

        print()
        self.menu(connection)

    def add_income(self, connection):
        amount = int(input("\nEnter income:\n"))
        self.balance += amount
        database_handler.update_balance(connection, self)
        print("Income was added!")

    def transfer(self, connection):
        card_transfer_to = input("\nEnter card number:\n")
        if card_transfer_to[15] != str(luhn_parity_bit(card_transfer_to)):
            print("Probably you made a mistake in the card number. Please try again!")
            return
        if card_transfer_to == self.card_number:
            print("You can't transfer money to the same account!")
            return

        query_result = database_handler.select_card(connection, card_transfer_to)
        if query_result is None:
            print("Such a card does not exist.")
            return

        amount = int(input("Enter how much money you want to transfer:\n"))
        if amount > self.balance:
            print("Not enough money!")
            return

        account_transfer_to = Account(query_result[0], query_result[1], query_result[2], query_result[3])

        self.balance -= amount
        account_transfer_to.balance += amount

        database_handler.update_balance(connection, self)
        database_handler.update_balance(connection, account_transfer_to)
        print("Success!")

    def close_account(self, connection):
        print("\nThe account has been closed!")
        database_handler.delete_account(connection, self)
