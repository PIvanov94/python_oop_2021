from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        try:
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware[0].install(software)
            System._software.append(software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        try:
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware[0].install(software)
            System._software.append(software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sum(s.memory_consumption for s in System._software)} / {sum(h.memory for h in System._hardware)}\n" \
               f"Total Capacity Taken: {sum(s.capacity_consumption for s in System._software)} / {sum(h.capacity for h in System._hardware)}"

    @staticmethod
    def get_software_components(hardware):
        software_components = []
        for s in hardware.software_components:
            software_components.append(s.name)
        if software_components:
            return ", ".join(software_components)

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n" \
                      f"Express Software Components: {len([h for h in hardware.software_components if h.__class__.__name__ == 'ExpressSoftware'])}\n" \
                      f"Light Software Components: {len([h for h in hardware.software_components if h.__class__.__name__ == 'LightSoftware'])}\n" \
                      f"Memory Usage: {sum([h.memory_consumption for h in hardware.software_components])} / {hardware.memory}\n" \
                      f"Capacity Usage: {sum([h.capacity_consumption for h in hardware.software_components])} / {hardware.capacity}\n" \
                      f"Type: {hardware.type}\n" \
                      f"Software Components: {System.get_software_components(hardware)}"
        return result