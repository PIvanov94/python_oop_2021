from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    room_cost = 15
    appliance_types = (TV, Fridge, Stove)
    default_room_members_count = 2

    def __init__(self, name, pension_one, pension_two):
        super().__init__(name, pension_one + pension_two, self.default_room_members_count)
        self.calculate_expenses(self.appliances)