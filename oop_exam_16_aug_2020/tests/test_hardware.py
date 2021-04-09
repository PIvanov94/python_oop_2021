from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class HardwareTest(TestCase):
    def setUp(self):
        self.hardware = Hardware("SSD", "Test1", 100, 50)

    def test_init_constructor(self):
        self.assertEqual("SSD", self.hardware.name)
        self.assertEqual("Test1", self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(50, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_installing_software_if_correct(self):
        software = ExpressSoftware("Pycharm", 20, 5)
        self.hardware.install(software)
        self.assertEqual([software], self.hardware.software_components)

    def test_installing_software_when_raises(self):
        software = ExpressSoftware("Pycharm", 200, 100)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall_software(self):
        software = ExpressSoftware("Pycharm", 20, 5)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual([], self.hardware.software_components)

if __name__ == "__main__":
    main()