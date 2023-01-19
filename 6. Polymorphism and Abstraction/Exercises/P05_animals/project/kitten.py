from project.cat import Cat


class Kitten(Cat):

    def make_sound(self):
        return "Meow"

    def __init__(self, name, age):
        super().__init__(name, age, "Female")



