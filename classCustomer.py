class Customer: # не верный вариант

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

    def get_customer(self, in_pass):
        for i in self.customers:
            if i == in_pass:
                return i
            if i != in_pass:
                raise KeyError(f'Клиент с номером паспорта {in_pass} не найден')


bank = Bank()
bank.add_customer('Han', 'Solo', 12345)

bank.get_customer(12345)


class Customer: #верный вариант

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

    def get_customer(self, in_pass):
        for i in self.customers:
            if i.passport_number != in_pass:
                raise KeyError(f'Клиент с номером паспорта {in_pass} не найден')
            if i.passport_number == in_pass:
                return (f'{self.customers}')


bank = Bank()
bank.add_customer('Han', 'Solo', 12345)
customer = bank.get_customer(12345)

class Customer: # верный вариант с обработкой ошибки об отсутсвии паспорта всписке try except

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

    def get_customer(self, in_pass):
        try:
            for i in self.customers:
                if i.passport_number == in_pass:
                    return i
            raise KeyError(f'Клиент с номером паспорта {in_pass} не найден')
        except KeyError as e:
            print(e)


bank = Bank()
bank.add_customer('Han', 'Solo', 12345)
customer = bank.get_customer(12345)