class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance, account_number):
        self.account_number = account_number
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount, inc_account_number):
        if self.account_number == inc_account_number:
            self.balance += amount
        return self
    def withdraw(self, amount, account_number):
        if self.account_number == account_number:
            if self.balance >= amount:
                self.balance -= amount
                return True
            else:
                print("Insufficient funds: Charging a $5 fee")
                self.balance -= 5
                return False
    def display_account_info(self, account_number):
        if self.account_number == account_number:
            print(f"Balance: {self.balance}")
        return self
    def yield_interest(self, account_number):
        if self.account_number == account_number:
            if self.balance > 0:
                self.balance *= 1 + self.int_rate
        return self
    @classmethod
    def all_instances(cls):
        num = 1
        for account in cls.all_accounts:
            print(f"Info for Account {num}:")
            print(f"Balance: {account.balance}")
            print(f"Interest Rate: {account.int_rate}")
            num += 1
        return cls
# act1 = BankAccount(0.05, 10)
# act2 = BankAccount(0.01, 20)
# act1.deposit(5).deposit(3).deposit(7).withdraw(6).yield_interest().display_account_info()
# act2.deposit(500).deposit(300).withdraw(100).withdraw(200).withdraw(150).withdraw(150).yield_interest().display_account_info()
# BankAccount.all_instances()
class User:
    def __init__(self, name, email, int_rate, balance):
        self.name = name
        self.email = email
        self.accounts = []
        self.accounts.append(BankAccount(int_rate, balance, 0))
        self.num = 1
    def make_deposit(self, amount, account_number):
        self.accounts[account_number].deposit(amount, account_number)
        return self
    def make_withdrawal(self, amount, account_number):
        return self.accounts[account_number].withdraw(amount, account_number)
    def display_user_balance(self, account_number):
        self.accounts[account_number].display_account_info(account_number)
        return self
    def add_account(self, int_rate, balance):
        self.accounts.append(BankAccount(int_rate, balance, self.num))
        self.num += 1
    def transfer_money(self, amount, other_user, your_account_number, their_account_number):
        if self.make_withdrawal(amount, your_account_number) == True:
            other_user.make_deposit(amount, their_account_number)
# account number is index of account (0, 1, 2)
Bobby = User('Bobby', 'bobby@gmail.com', '0.05', 100) # create Bobby user with accounts[0]
Bobby.make_deposit(50, 0) # make deposit of 50 into accounts[0]
Bobby.add_account(0.05, 500) # add a second account for Bobby (accounts[1])
Bobby.make_deposit(500, 0) # make deposit of 500 into accounts[0]
Bobby.display_user_balance(0) # display Bobby balance of accounts[0]
Murr = User('Murr', 'murr@gmail.com', '0.05', 300) # create Murr user with accounts[0]
Murr.display_user_balance(0) # display Murr balance of accounts[0]
Bobby.transfer_money(500, Murr, 0, 0) # Bobby transfers Murr 500 dollars from accounts[0] to her accounts[0]
Bobby.display_user_balance(0) # display Bobby accounts[0] balance
Murr.display_user_balance(0) # display Murr's accounts[0] balance
Murr.add_account(0.02, 1000)
Bobby.display_user_balance(1)
Murr.display_user_balance(1)
Bobby.transfer_money(500, Murr, 1, 1)
Bobby.display_user_balance(1)
Murr.display_user_balance(1)