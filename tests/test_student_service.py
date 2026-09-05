import unittest

from models import Student
from services import StudentService


class MemoryStudentRepository:
    def __init__(self, students=None):
        self.students = list(students or [])
        self.save_count = 0

    def load_all(self):
        return list(self.students)

    def save_all(self, students):
        self.students = list(students)
        self.save_count += 1


class StudentServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.repository = MemoryStudentRepository()
        self.service = StudentService(self.repository)
        self.an = Student("SV01", "Nguyen Van An", 20, 8, 9)
        self.binh = Student("SV02", "Tran Van Binh", 21, 6, 7)

    def test_add_and_get_all_students(self):
        self.service.add_student(self.an)
        students = self.service.get_all_students()
        self.assertEqual(students, [self.an])
        self.assertEqual(self.repository.save_count, 1)
        students.clear()
        self.assertEqual(self.service.get_all_students(), [self.an])

    def test_add_rejects_duplicate_id(self):
        self.service.add_student(self.an)
        with self.assertRaises(ValueError):
            self.service.add_student(
                Student("SV01", "Another Student", 22, 7, 7)
            )
        self.assertEqual(len(self.service.get_all_students()), 1)
        self.assertEqual(self.repository.save_count, 1)

    def test_find_by_id(self):
        self.service.add_student(self.an)
        self.assertIs(self.service.find_by_id("SV01"), self.an)
        self.assertIsNone(self.service.find_by_id("UNKNOWN"))

    def test_search_by_name_is_partial_and_case_insensitive(self):
        self.service.add_student(self.an)
        self.service.add_student(self.binh)
        self.assertEqual(self.service.search_by_name("  vAn  "), [self.an, self.binh])
        self.assertEqual(self.service.search_by_name("binh"), [self.binh])
        self.assertEqual(self.service.search_by_name("missing"), [])

    def test_search_by_empty_name_returns_empty_list(self):
        self.service.add_student(self.an)
        self.assertEqual(self.service.search_by_name(""), [])
        self.assertEqual(self.service.search_by_name("   "), [])

    def test_update_student(self):
        self.service.add_student(self.an)
        updated = self.service.update_student(
            "SV01", name="Le Thi Hoa", math_score=10
        )
        self.assertTrue(updated)
        self.assertEqual(self.an.name, "Le Thi Hoa")
        self.assertEqual(self.an.math_score, 10.0)
        self.assertEqual(self.an.age, 20)
        self.assertEqual(self.repository.save_count, 2)

    def test_invalid_update_is_atomic_and_is_not_saved(self):
        self.service.add_student(self.an)
        with self.assertRaises(ValueError):
            self.service.update_student("SV01", name="Le Thi Hoa", age=10)
        self.assertEqual(self.an.name, "Nguyen Van An")
        self.assertEqual(self.an.age, 20)
        self.assertEqual(self.repository.save_count, 1)

    def test_update_missing_student_returns_false(self):
        self.assertFalse(self.service.update_student("UNKNOWN", name="New Name"))
        self.assertEqual(self.repository.save_count, 0)

    def test_delete_student(self):
        self.service.add_student(self.an)
        self.assertTrue(self.service.delete_student("SV01"))
        self.assertEqual(self.service.get_all_students(), [])
        self.assertEqual(self.repository.save_count, 2)

    def test_delete_missing_student_returns_false(self):
        self.assertFalse(self.service.delete_student("UNKNOWN"))
        self.assertEqual(self.repository.save_count, 0)

    def test_sort_by_gpa_descending(self):
        self.service.add_student(self.binh)
        self.service.add_student(self.an)
        self.assertEqual(self.service.sort_by_gpa(), [self.an, self.binh])


if __name__ == "__main__":
    unittest.main()
