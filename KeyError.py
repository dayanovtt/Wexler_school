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
        if age is None:
            raise KeyError("Age unknown - can't drive")
        if age < 18:
            raise ValueError("Age is under 18 - can't drive")


#try:
#    driver = Driver('Han', 'Solo', 123456, 15)
#except ValueError:
#    print("Age is under 18 - can't drive")

#try:
#    driver = Driver('Han', 'Solo', 123456, 15)
#except KeyError:
#    print("Не могу водить, но ничего страшного")
#    Нужно запомнить что try пишется вне функции для вызова