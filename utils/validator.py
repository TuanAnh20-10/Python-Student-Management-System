import math


def validate_age(age):
    if isinstance(age, bool) or not isinstance(age, int):
        raise ValueError("Age must be an integer.")

    if age < 16 or age > 100:
        raise ValueError("Age must be between 16 and 100.")


def validate_score(score):
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise ValueError("Score must be a number.")

    if score < 0 or score > 10 or not math.isfinite(score):
        raise ValueError("Score must be between 0 and 10.")


def validate_name(name):
    if not isinstance(name, str):
        raise ValueError("Name must be text.")

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if len(name.strip()) < 2:
        raise ValueError("Name must contain at least 2 characters.")


def validate_student_id(student_id):
    if not isinstance(student_id, str):
        raise ValueError("Student ID must be text.")

    if not student_id.strip():
        raise ValueError("Student ID cannot be empty.")
