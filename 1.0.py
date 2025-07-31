class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.passport_number}'


class Bank:
    def __init__(self):
        self.customers = {}


    def add_customer(self, first_name, last_name, passport_number):
        customer = Customer(first_name, last_name, passport_number)
        self.customers[customer.passport_number] = customer
        print(self.customers, ' конец функции add_customer')


    def get_customer(self, passport_number):
        if passport_number not in self.customers:
            raise KeyError("Customer not found")
        return self.customers[passport_number]


bank = Bank()
bank.add_customer('Harry', 'Potter', '2128506')
bank.add_customer('Harry', 'Potter', '1111111')
bank.add_customer('Harry', 'Potter', '11ddddd11')
customer = bank.get_customer('2128506')
print(customer.passport_number)