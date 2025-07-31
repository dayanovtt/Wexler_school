from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        print('This animal say:')
        sound = self.get_default_sound()
        print(f"Базовый звук: {sound}")

    def sleep(self):
        print('Animal is sleeping')





class Cat(Animal):
    def make_sound(self):
        print('Meow')


class Dog(Animal):
    def make_sound(self):
        print('Woof')

def main():
    animals = [Cat(), Dog()]

    for animal in animals:
        animal.make_sound()
        animal.sleep()

if __name__ == '__main__':
    main()
