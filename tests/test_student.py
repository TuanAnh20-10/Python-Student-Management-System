import unittest

from models import Student


class StudentTestCase(unittest.TestCase):
    def test_calculate_gpa(self):
        student = Student("SV01", "Nguyen Van An", 20, 8, 9)
        self.assertEqual(student.calculate_gpa(), 8.5)

    def test_classify_at_each_boundary(self):
        cases = (
            (8.5, "Excellent"),
            (7.0, "Good"),
            (5.5, "Average"),
            (5.49, "Weak"),
        )
        for score, expected in cases:
            with self.subTest(score=score):
                student = Student("SV01", "Nguyen Van An", 20, score, score)
                self.assertEqual(student.classify(), expected)

    def test_to_dict_and_from_dict_round_trip(self):
        original = Student("SV01", "Nguyen Van An", 20, 8, 9)
        restored = Student.from_dict(original.to_dict())
        self.assertEqual(restored.to_dict(), original.to_dict())

    def test_constructor_normalizes_text_and_scores(self):
        student = Student(" SV01 ", " Nguyen Van An ", 20, 8, 9)
        self.assertEqual(student.student_id, "SV01")
        self.assertEqual(student.name, "Nguyen Van An")
        self.assertEqual(student.math_score, 8.0)
        self.assertEqual(student.programming_score, 9.0)

    def test_update_changes_only_provided_values(self):
        student = Student("SV01", "Nguyen Van An", 20, 8, 9)
        student.update(name="Tran Van B", math_score=10)
        self.assertEqual(student.name, "Tran Van B")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.math_score, 10.0)
        self.assertEqual(student.programming_score, 9.0)

    def test_invalid_update_does_not_partially_change_student(self):
        student = Student("SV01", "Nguyen Van An", 20, 8, 9)
        with self.assertRaises(ValueError):
            student.update(name="Tran Van B", age=10)
        self.assertEqual(student.name, "Nguyen Van An")
        self.assertEqual(student.age, 20)


if __name__ == "__main__":
    unittest.main()
