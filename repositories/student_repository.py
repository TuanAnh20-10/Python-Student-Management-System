import json
from pathlib import Path

from models import Student


DEFAULT_DATA_FILE = (
    Path(__file__).resolve().parent.parent / "data" / "students.json"
)


class StudentRepository:
    def __init__(self, file_path=None):
        self.file_path = Path(file_path) if file_path else DEFAULT_DATA_FILE

    def load_all(self):
        if not self.file_path.exists():
            return []

        try:
            data = json.loads(self.file_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ValueError("Student data file contains invalid JSON.") from error

        if not isinstance(data, list):
            raise ValueError("Student data file must contain a JSON list.")

        try:
            return [Student.from_dict(item) for item in data]
        except (KeyError, TypeError) as error:
            raise ValueError("Student data file has an invalid structure.") from error

    def save_all(self, students):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        data = [student.to_dict() for student in students]

        self.file_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=4),
            encoding="utf-8",
        )
