from models import Student
from services import StudentService


class StudentApp:
    def __init__(self, service=None):
        self.service = service or StudentService()
        self._actions = {
            "1": self.add_student,
            "2": self.view_students,
            "3": self.find_student,
            "4": self.search_student,
            "5": self.update_student,
            "6": self.delete_student,
            "7": self.sort_students,
        }

    @staticmethod
    def show_menu():
        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Find Student by ID")
        print("4. Search Student by Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Sort Students by GPA")
        print("0. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ").strip()

            if choice == "0":
                print("Goodbye.")
                return

            action = self._actions.get(choice)
            if action is None:
                print("Invalid option.")
                continue

            action()

    def add_student(self):
        try:
            student_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            age = int(input("Age: "))
            math_score = float(input("Math score: "))
            programming_score = float(input("Programming score: "))

            student = Student(
                student_id,
                name,
                age,
                math_score,
                programming_score,
            )
            self.service.add_student(student)
            print("Student added successfully.")
        except ValueError as error:
            print(f"Error: {error}")

    def view_students(self):
        self._print_students(
            self.service.get_all_students(),
            "========== STUDENT LIST ==========",
        )

    def find_student(self):
        student_id = input("Enter student ID: ").strip()
        student = self.service.find_by_id(student_id)
        print(student if student else "Student not found.")

    def search_student(self):
        name = input("Enter student name: ").strip()
        self._print_students(self.service.search_by_name(name))

    def update_student(self):
        student_id = input("Student ID: ").strip()
        student = self.service.find_by_id(student_id)

        if student is None:
            print("Student not found.")
            return

        print("Leave blank to keep current value.")

        try:
            name = input(f"Name [{student.name}]: ").strip()
            age_input = input(f"Age [{student.age}]: ").strip()
            math_input = input(f"Math score [{student.math_score}]: ").strip()
            programming_input = input(
                f"Programming score [{student.programming_score}]: "
            ).strip()

            new_name = name or None
            new_age = int(age_input) if age_input else None
            new_math_score = float(math_input) if math_input else None
            new_programming_score = (
                float(programming_input) if programming_input else None
            )

            self.service.update_student(
                student_id,
                name=new_name,
                age=new_age,
                math_score=new_math_score,
                programming_score=new_programming_score,
            )
            print("Student updated successfully.")
        except ValueError as error:
            print(f"Error: {error}")

    def delete_student(self):
        student_id = input("Student ID: ").strip()
        if self.service.delete_student(student_id):
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def sort_students(self):
        self._print_students(
            self.service.sort_by_gpa(),
            "======= SORTED BY GPA =======",
        )

    @staticmethod
    def _print_students(students, heading=None):
        if not students:
            print("No students found.")
            return

        if heading:
            print(f"\n{heading}")

        for student in students:
            print(student)
