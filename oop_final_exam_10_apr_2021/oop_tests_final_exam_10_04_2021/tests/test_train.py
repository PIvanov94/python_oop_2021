from unittest import TestCase, main

from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self):
        self.train = Train("Trainname", 5)

    def test_class_attributes(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_constructor_init_attributes(self):
        self.assertEqual("Trainname", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_when_is_valid(self):
        self.assertEqual("Added passenger Someone", self.train.add("Someone"))
        self.assertEqual(["Someone"], self.train.passengers)

    def test_add_passenger_when_is_invalid_train_full(self):
        with self.assertRaises(ValueError) as ex:
            self.train.passengers = ["a", "b", "c", "d", "e"]
            self.train.add("Someone")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_passenger_when_passenger_is_already_in_train(self):
        with self.assertRaises(ValueError) as ex:
            self.train.passengers = ["Someone"]
            self.train.add("Someone")
        self.assertEqual("Passenger Someone Exists", str(ex.exception))

    def test_remove_passenger_when_is_valid(self):
        self.train.passengers = ["Someone"]
        self.assertEqual("Removed Someone", self.train.remove("Someone"))
        self.assertEqual([], self.train.passengers)

    def test_remove_passenger_when_passenger_not_in_train(self):
        with self.assertRaises(ValueError) as ex:
            self.train.passengers = ["a", "b", "c"]
            self.train.remove("Someone")
        self.assertEqual("Passenger Not Found", str(ex.exception))