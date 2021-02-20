# from repo.python_oop_2021.defining_classes_exercise.07_guilds.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if player_name in [p.name for p in self.players]:
            player = [p for p in self.players if p.name == player_name][0]
            self.players.remove(player)
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        data = f"Guild: {self.name}\n"
        for p in self.players:
            data += p.player_info()
        return data
