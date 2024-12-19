
# Problem 3

class BankAccount:
    def __init__(self):
        self.holder_name = None
        self.account_number = None
        self.date_of_opening = None
        self.balance = 0

    def deposit(self, amount):
        total_amount = amount + self.balance
        self.balance = total_amount
        print(f"Deposited amount of {amount}\- to your account")
        # return total_amount
    
    def withdram_amount(self, amount):
        if self.balance < amount:
            print("Insufficient bank balance to withdraw...!")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawed {amount}\- from your account")

    def check_balance(self):
        print("Your current balance is ", self.balance)

account1 = BankAccount()

account1.deposit(10000)
account1.deposit(10000)
account1.withdram_amount(500)

account1.check_balance()
