class Human:
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def move(self):
        print(f'{self.first_name} {self.last_name} is walking')


class Driver(Human):

    def __init__(self, first_name, last_name, driver_license, age=None):
        super().__init__(first_name, last_name, age=age)
        self.driver_license = driver_license


class BusDriver(Driver):

    @staticmethod
    def calculate_change(self, price, amount_money):
        return amount_money - price


human=Human('Luke', 'Skywalker')
human.move()

driver = Driver('Han', 'Solo', 123456)
driver.move()