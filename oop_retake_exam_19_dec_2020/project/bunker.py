class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        foods = [supply for supply in self.supplies if supply.__class__.__name__ == "FoodSupply"]
        if not foods:
            raise IndexError("There are no food supplies left!")
        return foods

    @property
    def water(self):
        water_objects = [water_obj for water_obj in self.supplies if water_obj.__class__.__name__ == "WaterSupply"]
        if not water_objects:
            raise IndexError("There are no water supplies left!")
        return water_objects

    @property
    def painkillers(self):
        painkillers_objects = [painkiller_obj for painkiller_obj in self.medicine
                               if painkiller_obj.__class__.__name__ == "Painkiller"]
        if not painkillers_objects:
            raise IndexError("There are no painkillers left!")
        return painkillers_objects

    @property
    def salves(self):
        salve_objects = [salve_obj for salve_obj in self.medicine if salve_obj.__class__.__name__ == "Salve"]
        if not salve_objects:
            raise IndexError("There are no salves left!")
        return salve_objects

    def add_survivor(self, survivor):
        try:
            survivor_name = [s.name for s in self.survivors if s.name == survivor.name][0]
            raise IndexError(f"Survivor with name {survivor_name} already exists.")
        except IndexError:
            self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        healing_medicine = self.painkillers.pop() if medicine_type == "Painkiller" else self.salves.pop()
        if survivor.needs_healing:
            healing_medicine.apply(survivor)
            self.medicine.remove(healing_medicine)
        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        supply = self.food.pop() if sustenance_type == "FoodSupply" else self.water.pop()
        if survivor.needs_sustenance:
            supply.apply(survivor)
            self.supplies.remove(supply)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            survivor.sustain(survivor, "FoodSupply")
            survivor.sustain(survivor, "WaterSupply")