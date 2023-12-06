from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student1 = Student("Alex", {"course1": ["note1", "note2"]})

    def test_initialization(self):
        self.assertEqual("Alex", self.student1.name)
        self.assertIn("course1", self.student1.courses)
        self.assertEqual(["note1", "note2"], self.student1.courses["course1"])

    def test_initialization_with_empty_dict(self):
        self.sample_student = Student("Pesho")
        self.assertEqual("Pesho", self.sample_student.name)
        self.assertEqual({}, self.sample_student.courses)

    def test_enroll_in_already_enrolled_course_add_notes(self):
        res_msg = self.student1.enroll("course1", ["note3", "note4"])
        self.assertEqual("Course already added. Notes have been updated.", res_msg)
        self.assertEqual(["note1", "note2", "note3", "note4"], self.student1.courses["course1"])

    def test_enroll_new_course_with_notes_without_add_course_notes_msg(self):
        res_msg = self.student1.enroll("course2", ["note1", "note2"])
        self.assertEqual("Course and course notes have been added.", res_msg)
        self.assertIn("course2", self.student1.courses)
        self.assertEqual(["note1", "note2"], self.student1.courses["course2"])

    def test_enroll_new_course_with_notes_with_add_course_notes_msg(self):
        res_msg = self.student1.enroll("course2", ["note1", "note2"], "Y")
        self.assertEqual("Course and course notes have been added.", res_msg)
        self.assertIn("course2", self.student1.courses)
        self.assertEqual(["note1", "note2"], self.student1.courses["course2"])

    def test_enroll_in_new_course_without_notes_or_add_notes_msg(self):
        res_msg = self.student1.enroll("course2", ["shouldn't go in the notes"], "N")
        self.assertEqual("Course has been added.", res_msg)
        self.assertIn("course2", self.student1.courses)
        self.assertEqual([], self.student1.courses["course2"])

    def test_add_notes_to_existing_course(self):
        res_msg = self.student1.add_notes("course1", "note3")
        self.assertEqual("Notes have been updated", res_msg)
        self.assertEqual(["note1", "note2", "note3"], self.student1.courses["course1"])

    def test_add_notes_to_not_existing_course_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.student1.add_notes("course3", "note1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_enrolled_course(self):
        res_msg = self.student1.leave_course("course1")
        self.assertEqual("Course has been removed", res_msg)
        self.assertEqual({}, self.student1.courses)

    def test_leave_not_enrolled_course(self):
        with self.assertRaises(Exception) as ex:
            self.student1.leave_course("course2")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
