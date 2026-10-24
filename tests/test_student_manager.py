import pytest

from src.student_manager import Student, StudentManager


def test_create_student():
    student = Student(
        student_id="S001",
        name="Alice",
        email="alice@example.com"
    )

    assert student.student_id == "S001"
    assert student.name == "Alice"
    assert student.email == "alice@example.com"
    assert student.grades == {}

def test_add_grade():
    student = Student(
        student_id="S001",
        name="Alice",
        email="alice@example.com"
    )

    student.add_grade("MATH101", 95)

    assert student.grades["MATH101"] == 95.0

def test_update_existing_grade():
    student = Student(
        student_id="S001",
        name="Alice",
        email="alice@example.com"
    )

    student.add_grade("MATH101", 75)
    student.add_grade("MATH101", 95)

    assert student.grades["MATH101"] == 95.0
    assert len(student.grades) == 1

def test_calculate_gpa():
    student = Student(
        student_id="S001",
        name="Alice",
        email="alice@example.com"
    )

    student.add_grade("MATH101", 95)
    student.add_grade("ENG101", 85)
    student.add_grade("SCI101", 75)

    assert student.get_gpa() == 3.0

@pytest.mark.parametrize("score, expected_gpa", [
    (90, 4.0),
    (80, 3.0),
    (70, 2.0),
    (60, 1.0),
    (59, 0.0),
])
def test_gpa_boundaries(score, expected_gpa):
    student = Student(
        student_id="S001",
        name="Alice",
        email="alice@example.com"
    )

    student.add_grade("MATH101", score)

    assert student.get_gpa() == expected_gpa

@pytest.mark.parametrize("score", [
    -1,
    101,
    -0.5,
    100.5,
])
def test_invalid_grade_range(score):
    student = Student(
        student_id="S001",
        name="Alice",
        email="alice@example.com"
    )

    with pytest.raises(ValueError):
        student.add_grade("MATH101", score)

@pytest.mark.parametrize("score", [
    "90",
    None,
    True,
    False,
    [],
])
def test_invalid_grade_type(score):
    student = Student(
        student_id="S001",
        name="Alice",
        email="alice@example.com"
    )

    with pytest.raises(TypeError):
        student.add_grade("MATH101", score)

def test_student_initial_gpa(sample_student):
    assert sample_student.get_gpa() == 0.0
    assert sample_student.grades == {}

def test_manager_add_student(student_manager, sample_student):
    result = student_manager.add_student(sample_student)

    assert result.student_id == "S001"
    assert student_manager.get_total_students() == 1
    assert student_manager.get_student("S001") == sample_student

def test_manager_duplicate_student(student_manager, sample_student):
    student_manager.add_student(sample_student)

    with pytest.raises(ValueError):
        student_manager.add_student(sample_student)

    assert student_manager.get_total_students() == 1

def test_manager_get_missing_student(student_manager):
    with pytest.raises(KeyError):
        student_manager.get_student("S999")

def test_manager_remove_student(student_manager, sample_student):
    student_manager.add_student(sample_student)

    assert student_manager.get_total_students() == 1

    result = student_manager.remove_student("S001")

    assert result is True
    assert student_manager.get_total_students() == 0

    with pytest.raises(KeyError):
        student_manager.get_student("S001")

def test_manager_remove_missing_student(student_manager):
    with pytest.raises(KeyError):
        student_manager.remove_student("S999")

    assert student_manager.get_total_students() == 0

def test_manager_update_grade(student_manager, sample_student):
    student_manager.add_student(sample_student)

    gpa = student_manager.update_grade("S001", "MATH101", 95)

    assert gpa == 4.0
    assert sample_student.grades["MATH101"] == 95.0
    assert student_manager.calculate_gpa("S001") == 4.0

def test_manager_update_grade_missing_student(student_manager):
    with pytest.raises(KeyError):
        student_manager.update_grade("S999", "MATH101", 95)

    assert student_manager.get_total_students() == 0

def test_manager_get_all_students(student_manager, sample_student):
    student_manager.add_student(sample_student)

    second_student = Student(
        student_id="S002",
        name="Bob",
        email="bob@example.com"
    )
    student_manager.add_student(second_student)

    students = student_manager.get_all_students()

    assert len(students) == 2
    assert sample_student in students
    assert second_student in students
    assert student_manager.get_total_students() == 2

def test_manager_top_performers(student_manager):
    alice = Student("S001", "Alice", "alice@example.com")
    bob = Student("S002", "Bob", "bob@example.com")
    charlie = Student("S003", "Charlie", "charlie@example.com")

    student_manager.add_student(alice)
    student_manager.add_student(bob)
    student_manager.add_student(charlie)

    student_manager.update_grade("S001", "MATH101", 95)
    student_manager.update_grade("S002", "MATH101", 75)
    student_manager.update_grade("S003", "MATH101", 85)

    top_students = student_manager.get_top_performers(2)

    assert len(top_students) == 2
    assert top_students[0].name == "Alice"
    assert top_students[1].name == "Charlie"

@pytest.mark.parametrize("n", [
    0,
    -1,
    -5,
])
def test_manager_top_performers_invalid_n(student_manager, n):
    with pytest.raises(ValueError):
        student_manager.get_top_performers(n)

def test_manager_filter_by_min_gpa(student_manager):
    alice = Student("S001", "Alice", "alice@example.com")
    bob = Student("S002", "Bob", "bob@example.com")
    charlie = Student("S003", "Charlie", "charlie@example.com")

    student_manager.add_student(alice)
    student_manager.add_student(bob)
    student_manager.add_student(charlie)

    student_manager.update_grade("S001", "MATH101", 95)
    student_manager.update_grade("S002", "MATH101", 75)
    student_manager.update_grade("S003", "MATH101", 85)

    result = student_manager.filter_by_min_gpa(3.0)

    assert len(result) == 2
    assert alice in result
    assert charlie in result
    assert bob not in result

@pytest.mark.parametrize("min_gpa", [-0.1, 4.1])
def test_manager_filter_invalid_min_gpa(student_manager, min_gpa):
    with pytest.raises(ValueError):
        student_manager.filter_by_min_gpa(min_gpa)

@pytest.mark.parametrize("min_gpa", [0.0, 4.0])
def test_manager_filter_valid_boundaries(student_manager, min_gpa):
    student = Student("S001", "Alice", "alice@example.com")
    student_manager.add_student(student)
    student_manager.update_grade("S001", "MATH101", 95)

    result = student_manager.filter_by_min_gpa(min_gpa)

    assert student in result
    