from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def is_possible_to_install_software(self, software):
        total_capacity_use = 0
        total_memory_use = 0
        for s in self.software_components:
            total_capacity_use += s.capacity_consumption
            total_memory_use += s.memory_consumption
        total_capacity_use += software.capacity_consumption
        total_memory_use += software.memory_consumption
        if total_capacity_use <= self.capacity and total_memory_use <= self.memory:
            return True
        return False

    def install(self, software):
        if not self.is_possible_to_install_software(software):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
