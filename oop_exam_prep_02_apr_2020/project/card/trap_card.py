from project.card.card import Card


class TrapCard(Card):
    damage_points = 120
    health_points = 5

    def __init__(self, name):
        super().__init__(name, self.damage_points, self.health_points)