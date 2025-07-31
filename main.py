class Human:
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def move(self):
        print(f'{self.first_name} {self.last_name} is walking')


human = Human('Luke', 'Skywalker')
human.move()


class Driver(Human):
    def __init__(self, first_name, last_name, driver_license, age=None):
        super(Driver, self).__init__(first_name, last_name, age)

        self.driver_license = driver_license


driver = Driver('Han', 'Solo', 123456)
driver.move()


class BusDriver(Driver):
    @staticmethod
    def calculate_change(self, price_ticket, amount_money):
        change = amount_money - price_ticket
        return class Human:
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def move(self):
        print(f'{self.first_name} {self.last_name} is walking')

human = Human('Luke', 'Skywalker')
human.move()

class Driver(Human):
    def __init__(self, first_name, last_name, driver_license, age=None):
        super(Driver, self).__init__(first_name, last_name, age)

        self.driver_license = driver_license

driver = Driver('Han', 'Solo', 123456)
driver.move()

class BusDriver(Driver):
    def calculate_change (self, price_ticket, amount_money):
        change = amount_money - price_ticket
        return(change)(change)