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


        def __init__(self, first_name, last_name, driver_license, age=None):
            super().__init__(first_name, last_name, driver_license, age)

        def calculate_change(self, price, amount_money):
            return price - amount_money


        human=Human('Luke', 'Skywalker')
    human.move()  # выведет в консоль "Luke Skywalker is walking"

    driver = Driver('Han', 'Solo', 123456)
    driver.move()  # тоже выведет в консоль "Han Solo is walking", так как Driver - это Human