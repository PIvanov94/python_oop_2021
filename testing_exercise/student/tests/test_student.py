from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Studentname", {"Python": ["basics"]})

    def test_init_constructor(self):
        self.assertEqual("Studentname", self.student.name)
        self.assertEqual({"Python": ["basics"]}, self.student.courses)

    def test_enroll_when_existing_course_and_notes_are_updated(self):
        result = self.student.enroll("Python", ["fundamentals, advanced"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_when_course_and_course_notes_are_updated__add_course_notes_is_Y(self):
        result = self.student.enroll("Java", "advanced", "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'Java': 'advanced', 'Python': ['basics']}, self.student.courses)

    def test_enroll_when_course_and_course_notes_are_updated__add_course_notes_is_empty(self):
        self.student = Student("Studentname", courses=None)
        result = self.student.enroll("Java", "advanced", "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Java": "advanced"}, self.student.courses)

    def test_enroll_course_not_in_courses(self):
        result = self.student.enroll("Javascript", "basics", "first_steps")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"Python": ["basics"], "Javascript": []}, self.student.courses)

    def test_add_notes_if_course_in_courses(self):
        result = self.student.add_notes("Python", "OOP")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"Python": ["basics", "OOP"]}, self.student.courses)

    def test_add_notes_if_course_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Java", "OOP")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_course_in_courses(self):
        result = self.student.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_if_course_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
