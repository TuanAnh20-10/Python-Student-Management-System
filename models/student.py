from utils import (
    validate_age,
    validate_name,
    validate_score,
    validate_student_id,
)


class Student:
    def __init__(self, student_id, name, age, math_score, programming_score):
        validate_student_id(student_id)
        validate_name(name)
        validate_age(age)
        validate_score(math_score)
        validate_score(programming_score)

        self._student_id = student_id.strip()
        self._name = name.strip()
        self._age = age
        self._math_score = float(math_score)
        self._programming_score = float(programming_score)

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def math_score(self):
        return self._math_score

    @property
    def programming_score(self):
        return self._programming_score

    def update(
        self,
        name=None,
        age=None,
        math_score=None,
        programming_score=None,
    ):
        new_name = self.name if name is None else name
        new_age = self.age if age is None else age
        new_math_score = self.math_score if math_score is None else math_score
        new_programming_score = (
            self.programming_score
            if programming_score is None
            else programming_score
        )

        validate_name(new_name)
        validate_age(new_age)
        validate_score(new_math_score)
        validate_score(new_programming_score)

        self._name = new_name.strip()
        self._age = new_age
        self._math_score = float(new_math_score)
        self._programming_score = float(new_programming_score)

    def calculate_gpa(self):
        return (self.math_score + self.programming_score) / 2

    def classify(self):
        gpa = self.calculate_gpa()

        if gpa >= 8.5:
            return "Excellent"
        elif gpa >= 7.0:
            return "Good"
        elif gpa >= 5.5:
            return "Average"
        else:
            return "Weak"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "math_score": self.math_score,
            "programming_score": self.programming_score,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["math_score"],
            data["programming_score"],
        )

    def __str__(self):
        return (
            f"ID: {self.student_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Math: {self.math_score} | "
            f"Programming: {self.programming_score} | "
            f"GPA: {self.calculate_gpa():.2f} | "
            f"Classification: {self.classify()}"
        )
