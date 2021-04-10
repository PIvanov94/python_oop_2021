from unittest import TestCase, main

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class PlayerRepositoryTest(TestCase):
    def setUp(self):
        self.player_repository = PlayerRepository()
        self.player = Advanced("Testname")

    def test_attributes_upon_init(self):
        self.assertEqual([], self.player_repository.players)

    def test_players_count_when_empty(self):
        self.assertEqual(0, self.player_repository.count)

    def test_add_player_when_player_not_in_players_list(self):
        self.player_repository.add(self.player)
        self.assertEqual([self.player], self.player_repository.players)

    def test_players_list_count_when_player_is_in(self):
        self.player_repository.add(self.player)
        self.assertEqual(1, self.player_repository.count)

    def test_when_players_is_already_in_players_list_exception_expect(self):
        self.player_repository.add(self.player)
        with self.assertRaises(ValueError) as ex:
            self.player_repository.add(self.player)
        self.assertEqual("Player Testname already exists!", str(ex.exception))

    def test_remove_when_player_is_in_list(self):
        self.player_repository.add(self.player)
        self.player_repository.remove("Testname")
        self.assertEqual([], self.player_repository.players)

    def test_remove_when_player_name_is_empty_string_exception_expect(self):
        with self.assertRaises(ValueError) as ex:
            self.player_repository.remove("")
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_find_when_player_is_in_players_list(self):
        self.player_repository.add(self.player)
        self.assertEqual(self.player, self.player_repository.find("Testname"))

    def test_find_when_player_is_not_in_players_list_expect_none_return(self):
        self.player_repository.add(self.player)
        self.assertIsNone(self.player_repository.find("Slave"))


if __name__ == "__main__":
    main()
