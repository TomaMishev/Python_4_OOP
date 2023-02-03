from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):

    def test_init_only_with_name(self):
        name = "Test"
        student = Student(name)
        self.assertEqual("Test", student.name)
        self.assertEqual({}, student.courses)

    def test_full_init_func(self):
        name = "Test"
        courses = {
            "Web": ["note", "note2"],
            "Test": ["n1", "n2"]
        }

        student = Student(name, courses)

        self.assertEqual("Test", student.name)
        self.assertEqual({
            "Web": ["note", "note2"],
            "Test": ["n1", "n2"]
        }, student.courses)

    def test_enroll_with_already_enrolled_course_adds_note_to_the_course(self):
        student = Student("Test", {
            "Web": ["note", "note2"],
            "sps": ["n1", "n2"]
        })

        result = student.enroll("Web", ["new note1"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note', 'note2', 'new note1'], student.courses["Web"])

    def test_enroll_with_new_course_adds_the_course(self):
        student = Student("Test", {
            "Web": ["note", "note2"],
            "sps": ["n1", "n2"]
        })

        course = "gg"
        notes = ["1", "2"]

        result = student.enroll(course, notes)

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in student.courses)
        self.assertEqual(notes, student.courses[course])

    def test_roll_new_course_without_notes(self):
        student = Student("Test", {
            "Web": ["note", "note2"],
            "sps": ["n1", "n2"]
        })

        course = "gg"
        notes = ['f', 'f2']

        result = student.enroll(course, notes, "N")

        self.assertEqual("Course has been added.", result)
        self.assertTrue(course in student.courses)
        self.assertEqual([], student.courses[course])

    def test_if_add_notes_adds_notes_to_existing_course(self):
        student = Student("Test", {
            "Web": ["note", "note2"],
            "sps": ["n1", "n2"]
        })

        result = student.add_notes("Web", ["new"])

        self.assertEqual("Notes have been updated", result)

    def test_if_add_notes_raises_when_course_not_exists(self):
        student = Student("Test", {
            "Web": ["note", "note2"],
            "sps": ["n1", "n2"]
        })

        with self.assertRaises(Exception) as ex:
            student.add_notes("invc", 'RANDOM')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        student = Student("Test", {
            "Web": ["note", "note2"],
            "sps": ["n1", "n2"]
        })

        result = student.leave_course("Web")

        self.assertEqual("Course has been removed", result)

    def test_leave_course_if_course_does_not_exists(self):
        student = Student("Test", {
            "Web": ["note", "note2"],
            "sps": ["n1", "n2"]
        })

        with self.assertRaises(Exception) as ex:
            student.leave_course("1")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
