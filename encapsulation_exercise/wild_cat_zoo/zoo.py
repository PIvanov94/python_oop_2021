class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salaries = sum([w.salary for w in self.workers])
        if self.__budget >= all_salaries:
            self.__budget -= all_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_costs_for_tending = sum([a.get_needs() for a in self.animals])
        if self.__budget >= all_costs_for_tending:
            self.__budget -= all_costs_for_tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        data = f"You have {len(self.animals)} animals" + "\n"
        data += f"----- {len(lions)} Lions:" + "\n"
        data += "{}".format('\n'.join([repr(l) for l in lions])) + "\n"
        data += f"----- {len(tigers)} Tigers:" + "\n"
        data += "{}".format('\n'.join([repr(t) for t in tigers])) + "\n"
        data += f"----- {len(cheetahs)} Cheetahs:" + "\n"
        data += "{}".format('\n'.join([repr(c) for c in cheetahs]))
        return data

    def workers_status(self):
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        data = f"You have {len(self.workers)} workers" + "\n"
        data += f"----- {len(keepers)} Keepers:" + "\n"
        data += "{}".format('\n'.join([repr(k) for k in keepers])) + "\n"
        data += f"----- {len(caretakers)} Caretakers:" + "\n"
        data += "{}".format('\n'.join(repr(c) for c in caretakers)) + "\n"
        data += f"----- {len(vets)} Vets:" + "\n"
        data += "{}".format('\n'.join([repr(v) for v in vets]))
        return data
