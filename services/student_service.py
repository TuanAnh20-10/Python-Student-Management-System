from repositories import StudentRepository


class StudentService:
    def __init__(self, repository=None):
        self._repository = (
            repository if repository is not None else StudentRepository()
        )
        self._students = self._repository.load_all()

    def add_student(self, student):
        if self.find_by_id(student.student_id):
            raise ValueError("Student ID already exists.")

        self._students.append(student)
        self._repository.save_all(self._students)

    def get_all_students(self):
        return list(self._students)

    def find_by_id(self, student_id):
        return next(
            (
                student
                for student in self._students
                if student.student_id == student_id
            ),
            None,
        )

    def search_by_name(self, name):
        keyword = name.strip().casefold()
        if not keyword:
            return []

        return [
            student
            for student in self._students
            if keyword in student.name.casefold()
        ]

    def update_student(
        self,
        student_id,
        name=None,
        age=None,
        math_score=None,
        programming_score=None,
    ):
        student = self.find_by_id(student_id)
        if student is None:
            return False

        student.update(
            name=name,
            age=age,
            math_score=math_score,
            programming_score=programming_score,
        )
        self._repository.save_all(self._students)
        return True

    def delete_student(self, student_id):
        student = self.find_by_id(student_id)
        if student is None:
            return False

        self._students.remove(student)
        self._repository.save_all(self._students)
        return True

    def sort_by_gpa(self):
        return sorted(
            self._students,
            key=lambda student: student.calculate_gpa(),
            reverse=True,
        )
