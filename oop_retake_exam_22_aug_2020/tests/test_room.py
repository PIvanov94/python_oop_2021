from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room


class RoomTests(TestCase):
    name = 'RoomName'
    budget = 100
    members_count = 3

    def setUp(self):
        self.room = Room(self.name, self.budget, self.members_count)

    def test_init_when_valid(self):
        self.assertEqual(self.name, self.room.family_name)
        self.assertEqual(self.budget, self.room.budget)
        self.assertEqual(self.members_count, self.room.members_count)
        self.assertListEqual([], self.room.children)
        for attr in ["family_name", "budget", "members_count", "expenses", "children"]:
            self.assertTrue(hasattr(self.room, attr))

    def test_expenses_when_positive(self):
        self.room.expenses = 5
        self.assertEqual(5, self.room.expenses)

    def test_expenses_when_zero(self):
        self.room.expenses = 0
        self.assertEqual(0, self.room.expenses)

    def test_expenses_when_negative_raise_expect(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -5
        self.assertEqual('Expenses cannot be negative', str(ex.exception))

    def test_calculate_expenses_when_zero_consumers(self):
        self.room.calculate_expenses([])
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_when__one_consumer(self):
        consumers = [Child(1, 2, 3)]
        self.room.calculate_expenses(consumers)
        self.assertEqual(consumers[0].get_monthly_expense(), self.room.expenses)

    def test_calculate_expenses_when__two_consumers(self):
        consumer_one = [Child(1, 2, 3)]
        consumer_two = [Child(4, 5, 6)]
        self.room.calculate_expenses(consumer_one, consumer_two)
        expected = consumer_one[0].get_monthly_expense() + consumer_two[0].get_monthly_expense()
        self.assertEqual(expected, self.room.expenses)

if __name__ == "__main__":
    main()