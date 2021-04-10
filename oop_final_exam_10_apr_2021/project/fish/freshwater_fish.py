from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    size = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, self.size, price)

    def eat(self):
        self.size += 3