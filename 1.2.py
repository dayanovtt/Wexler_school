class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, first_name, last_name, passport_number):
        customer = Customer(first_name, last_name, passport_number)
        self.customers[passport_number] = customer

    def get_customer(self, passport_number):
        if passport_number not in self.customers:
            raise KeyError("Customer not found")
        return self.customers[passport_number]

    def add_account(self, account: BankAccount, customer: Customer):
        self.accounts[customer] = account

    def get_customer_account(self, passport_number):
        customer = self.get_customer(passport_number)
        if customer not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[customer]

    def deposit(self, passport_number, amount):
        customer_account = self.get_customer_account(passport_number)
        customer_account.deposit(amount)

    def withdraw(self, passport_number, amount):
        customer_account = self.get_customer_account(passport_number)
        customer_account.withdraw(amount)


bank = Bank()
bank.add_customer('Harry', 'Potter', '2128506')
customer = bank.get_customer('2128506')

account = BankAccount(number='1234', currency='usd')
bank.add_account(account, customer)