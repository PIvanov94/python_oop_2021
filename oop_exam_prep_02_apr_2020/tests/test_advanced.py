from unittest import TestCase, main

from project.player.advanced import Advanced


class AdvancedTest(TestCase):
    def setUp(self):
        self.advanced = Advanced("Testname")

    def test_initial_attributes(self):
        self.assertEqual("Testname", self.advanced.username)
        self.assertEqual(250, self.advanced.health)
        self.assertFalse(self.advanced.is_dead)
        self.assertEqual("CardRepository", self.advanced.card_repository.__class__.__name__)

    def test_raises_when_name_is_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.username = ""
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_raises_when_health_is_less_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.health = -1
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_raises_when_damage_points_are_less_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced.take_damage(-1)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))

    def test_when_is_dead(self):
        self.advanced.take_damage(250)
        self.assertTrue(self.advanced.is_dead)

if __name__ == "__main__":
    main()