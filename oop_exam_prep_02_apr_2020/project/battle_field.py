from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:

    @staticmethod
    def is_beginner(player):
        if isinstance(player, Beginner):
            player.health += 40
            for card in player.card_repository.cards:
                card.damage_points += 30
        return player

    @staticmethod
    def get_bonus(player):
        player.health += sum(c.health_points for c in player.card_repository.cards)
        return player

    @staticmethod
    def damage_points(player):
        total_damage = sum(c.damage_points for c in player.card_repository.cards)
        return total_damage

    @staticmethod
    def fight(attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")
        BattleField.is_beginner(attacker)
        BattleField.is_beginner(enemy)
        BattleField.get_bonus(attacker)
        BattleField.get_bonus(enemy)
        enemy.health -= BattleField.damage_points(attacker)
        attacker.health -= BattleField.damage_points(enemy)
