import datetime


class Human:
    def __init__(self, first_name, last_name, year_of_birth=None):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth

    @property
    def age(self):
        goal = datetime.datetime.now().year - self.year_of_birth if self.year_of_birth else None
        return goal