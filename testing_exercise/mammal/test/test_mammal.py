from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Sisi", "human", "roar")

    def test_mammal_init_constructor(self):
        self.assertEqual("Sisi", self.mammal.name)
        self.assertEqual("human", self.mammal.type)
        self.assertEqual("roar", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Sisi makes roar", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_mammal_info(self):
        self.assertEqual("Sisi is of type human", self.mammal.info())


if __name__ == "__main__":
    main()
