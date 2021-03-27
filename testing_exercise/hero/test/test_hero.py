from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Myhero", 20, 100, 30)

    def test_hero_init_constructor(self):
        self.assertEqual("Myhero", self.hero.username)
        self.assertEqual(20, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(30, self.hero.damage)

    def test_battle_when_usernames_are_equal(self):
        enemy_hero = Hero("Myhero", 30, 200, 60)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_main_hero_health_is_zero_or_less(self):
        self.hero.health = 0
        enemy_hero = Hero("Somehero", 30, 200, 60)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_when_enemy_hero_health_is_zero_or_less(self):
        enemy_hero = Hero("Somehero", 30, 0, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight Somehero. He needs to rest", str(ex.exception))

    def test_battle_when_draw(self):
        enemy_hero = Hero("Somehero", 30, 30, 100)
        self.assertEqual("Draw", self.hero.battle(enemy_hero))

    def test_battle_when_you_win(self):
        enemy_hero = Hero("Somehero", 2, 10, 2)
        self.assertEqual("You win", self.hero.battle(enemy_hero))
        self.assertEqual(21, self.hero.level)
        self.assertEqual(101, self.hero.health)
        self.assertEqual(35, self.hero.damage)

    def test_battle_when_you_lose(self):
        enemy_hero = Hero("Somehero", 50, 1000, 200)
        self.assertEqual("You lose", self.hero.battle(enemy_hero))
        self.assertEqual(51, enemy_hero.level)
        self.assertEqual(405, enemy_hero.health)
        self.assertEqual(205, enemy_hero.damage)

    def test_str_representation(self):
        self.assertEqual("Hero Myhero: 20 lvl\n"
                         "Health: 100\nDamage: 30\n", self.hero.__str__())

if __name__ == "__main__":
    main()