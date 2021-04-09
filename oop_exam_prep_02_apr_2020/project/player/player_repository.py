from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.players = []

    @property
    def count(self):
        return len(self.players)

    def add(self, player):
        if self.find(player.username):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        player_to_remove = self.find(player)
        self.players.remove(player_to_remove)

    def find(self, username):
        for player in self.players:
            if player.username == username:
                return player