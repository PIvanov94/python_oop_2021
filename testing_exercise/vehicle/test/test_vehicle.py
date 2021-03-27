from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(70, 120)

    def test_vehicle_init_constructor(self):
        self.assertEqual(70, self.vehicle.fuel)
        self.assertEqual(70, self.vehicle.capacity)
        self.assertEqual(120, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_successful(self):
        self.vehicle.drive(5)
        self.assertEqual(63.75, self.vehicle.fuel)

    def test_drive_when_not_successful(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(70)
        self.assertEqual(70, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_successful(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(10)
        self.assertEqual(60, self.vehicle.fuel)

    def test_refuel_not_successful(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(30)
        self.assertEqual(70, self.vehicle.capacity)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_representation_vehicle(self):
        self.assertEqual("The vehicle has 120 horse power with 70 fuel left and "
                         "1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()