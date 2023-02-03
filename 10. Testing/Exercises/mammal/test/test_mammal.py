from unittest import TestCase, main

from mammal.project.mammal import Mammal


class MammalTests(TestCase):

    def test_mammal_init(self):
        name = "Peter"
        type = "Mammal type"
        sound = "sound"

        mammal = Mammal(name, type, sound)

        self.assertEqual(name, mammal.name)
        self.assertEqual(type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound_returns_proper_str(self):
        mammal = Mammal("Test", "Testtt", "Sound")
        result = mammal.make_sound()

        self.assertEqual(f"{mammal.name} makes {mammal.sound}", result)

    def test_get_kingdom(self):
        mammal = Mammal("Test", "Testtt", "Sound")
        result = mammal.get_kingdom()

        self.assertEqual("animals", result)

    def test_info_returns_correct_string(self):
        mammal = Mammal("Test", "Testtt", "Sound")
        result = mammal.info()

        self.assertEqual(f"{mammal.name} is of type {mammal.type}",result)




if __name__ == "__main__":
    main()
