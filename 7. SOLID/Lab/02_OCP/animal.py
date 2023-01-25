# Refactor the provided code, so you do not need to make any changes in it when you want to add new species to the
# animals' list


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def __init__(self):
        pass

    def make_sound(self):
        return "Woof"


class Cat(Animal):

    def __init__(self):
        pass

    def make_sound(self):
        return "Meow"


class Duck(Animal):

    def __init__(self):
        pass

    def make_sound(self):
        return "Quack-Quack"


def animal_sound(animals: list):
    for obj in animals:
        print(obj.make_sound())


animals = [Cat(), Dog(), Duck()]
animal_sound(animals)



