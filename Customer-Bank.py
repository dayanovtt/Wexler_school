class Customer:

    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number


class Bank:

    def __init__(self):
        self.customers = []

    def add_customer(self, first_name, last_name, passport_number):
        customer = Customer(first_name, last_name, passport_number)
        self.customers.append(customer)

    def get_customer(self, pass_num):
        for cust in self.customers:
            if cust.passport_number == pass_num:
                return cust
            else:
                raise KeyError("Customer not found!")


bank = Bank()
bank.add_customer('Timur', 'Dayanov', '12345678')
customer = bank.get_customer('12345678')

person = {
    'first_name': 'Tim',
    'last_name': 'Dayanov',
    'likes': 30,
    'posts': 45,
    'is_smoking': False,
    'favorites_genres': 'Comedy',
    'likes_from_users': 20,
    'phone_number': 89990000000
}