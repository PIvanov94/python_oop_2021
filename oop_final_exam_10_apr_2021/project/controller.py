from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration and not decoration == "None" and aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}"
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == "FreshwaterFish":
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            if aquarium.__class__.__name__ == "SaltwaterFish":
                return "Water not suitable."
            aquarium.add_fish(FreshwaterFish(fish_name, fish_species, price))
            return f"Successfully added {fish_type} to {aquarium_name}."
        elif fish_type == "SaltwaterFish":
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            if aquarium.__class__.__name__ == "FreshwaterFish":
                return "Water not suitable."
            aquarium.add_fish(FreshwaterFish(fish_name, fish_species, price))
            return f"Successfully added {fish_type} to {aquarium_name}."
        else:
            return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if aquarium_name == a.name][0]
        aquarium.feed()
        fish_fed = len(aquarium.fish)
        return f"Fish fed: {fish_fed}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if aquarium_name == a.name][0]
        total_sum = 0
        for fish in aquarium.fish:
            total_sum += fish.price
        for decoration in aquarium.decorations:
            total_sum += decoration.price
        return f"The value of Aquarium {aquarium_name} is {total_sum:2f}."

    def report(self):
        for aquarium in self.aquariums:
            return aquarium.__str__