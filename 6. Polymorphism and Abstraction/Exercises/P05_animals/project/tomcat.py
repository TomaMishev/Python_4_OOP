from project.cat import Cat
from project.dog import Dog
from project.kitten import Kitten


class Tomcat(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def make_sound(self):
        return "Hiss"


kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)

