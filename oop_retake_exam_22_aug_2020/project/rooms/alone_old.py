from project.rooms.room import Room


class AloneOld(Room):
    room_cost = 10
    default_room_members_count = 1

    def __init__(self, name, pension):
        super().__init__(name, pension, self.default_room_members_count)