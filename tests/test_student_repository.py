import json
import tempfile
import unittest
from pathlib import Path

from models import Student
from repositories import StudentRepository


class StudentRepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temporary_directory.name) / "students.json"
        self.repository = StudentRepository(self.file_path)

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_missing_file_returns_empty_list(self):
        self.assertEqual(self.repository.load_all(), [])

    def test_save_and_load_students(self):
        students = [
            Student("SV01", "Nguyễn Văn An", 20, 8, 9),
            Student("SV02", "Trần Thị Bình", 21, 7, 8),
        ]
        self.repository.save_all(students)
        loaded_students = self.repository.load_all()
        self.assertEqual(
            [student.to_dict() for student in loaded_students],
            [student.to_dict() for student in students],
        )
        self.assertIn("Nguyễn Văn An", self.file_path.read_text(encoding="utf-8"))

    def test_invalid_json_raises_value_error(self):
        self.file_path.write_text("not json", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "invalid JSON"):
            self.repository.load_all()

    def test_non_list_json_raises_value_error(self):
        self.file_path.write_text("{}", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "JSON list"):
            self.repository.load_all()

    def test_invalid_student_structure_raises_value_error(self):
        self.file_path.write_text(
            json.dumps([{"student_id": "SV01"}]), encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "invalid structure"):
            self.repository.load_all()


if __name__ == "__main__":
    unittest.main()
