class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, first_name, last_name, passport_number):
        customer = Customer(first_name, last_name, passport_number)
        self.customers[customer.passport_number] = customer

    def add_account(self, account, customer):
        self.accounts[customer] = account

    def deposit(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.deposit(amount)

    def withdraw(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.withdraw(amount)

    def get_customer(self, passport_number):
        if passport_number not in self.customers:
            raise KeyError("Customer not found")
        return self.customers[passport_number]

    def get_customer_account(self, passport_number):
        customer = self.get_customer(passport_number)
        if customer not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[customer]


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.amount = 0
        self.currency = currency

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if amount > self.amount:
            raise ValueError("Недостаточно средств на счету")
        self.amount -= amount

bank = Bank()
bank.add_customer('Harry', 'Potter', '2128506')
bank.add_customer('Ron', 'Weasley', '565656')
bank.add_account(BankAccount(12345, 'USD'), bank.get_customer('2128506'))
bank.add_account(BankAccount(123456, 'USD'), bank.get_customer('565656'))
bank.deposit('2128506', 100)
bank.deposit('565656', 100)