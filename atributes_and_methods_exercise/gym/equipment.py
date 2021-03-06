class Equipment:
    equipment_id = 0

    def __init__(self, name):
        Equipment.equipment_id = Equipment.get_next_id()
        self.name = name
        self.e_id = Equipment.equipment_id

    def __repr__(self):
        return f"Equipment <{self.e_id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.equipment_id + 1
