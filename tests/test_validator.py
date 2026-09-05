import unittest

from utils import (
    validate_age,
    validate_name,
    validate_score,
    validate_student_id,
)


class ValidatorTestCase(unittest.TestCase):
    def test_age_accepts_boundaries(self):
        validate_age(16)
        validate_age(100)

    def test_age_rejects_out_of_range_and_wrong_types(self):
        for age in (15, 101, 20.5, "20", True):
            with self.subTest(age=age), self.assertRaises(ValueError):
                validate_age(age)

    def test_score_accepts_boundaries(self):
        validate_score(0)
        validate_score(10)

    def test_score_rejects_invalid_values(self):
        invalid_scores = (-0.01, 10.01, float("nan"), float("inf"), "8", True)
        for score in invalid_scores:
            with self.subTest(score=score), self.assertRaises(ValueError):
                validate_score(score)

    def test_name_validation(self):
        validate_name("An")
        for name in ("", " ", "A", 123):
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate_name(name)

    def test_student_id_validation(self):
        validate_student_id("SV01")
        for student_id in ("", " ", 1):
            with self.subTest(student_id=student_id), self.assertRaises(ValueError):
                validate_student_id(student_id)


if __name__ == "__main__":
    unittest.main()
