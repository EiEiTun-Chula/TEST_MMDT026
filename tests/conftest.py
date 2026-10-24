import pytest

from src.student_manager import Student
from src.student_manager import StudentManager


@pytest.fixture
def sample_student():
    return Student(
        student_id="S001",
        name="Alice",
        email="alice@example.com"
    )


@pytest.fixture
def student_manager():
    return StudentManager()