import pytest

from src.data_validator import (validate_email, InvalidEmailError, validate_password, WeakPasswordError, validate_username, InvalidUsernameError, validate_age, InvalidAgeError, validate_registration, ValidationError)


def test_validate_email_valid():
    result = validate_email("student@example.com")
    assert result is True

def test_validate_email_missing_at():
    with pytest.raises(InvalidEmailError):
        validate_email("studentexample.com")

@pytest.mark.parametrize("email", [
    "studentexample.com",
    "student@",
    "@example.com",
    "student@example",
    "student..name@example.com",
    "",
])
def test_validate_email_invalid_formats(email):
    with pytest.raises(InvalidEmailError):
        validate_email(email)

@pytest.mark.parametrize("email", [
    123,
    None,
    True,
])
def test_validate_email_invalid_type(email):
    with pytest.raises(TypeError):
        validate_email(email)

def test_validate_password_valid():
    result = validate_password("Hello123!")
    assert result is True

def test_validate_password_too_short():
    with pytest.raises(WeakPasswordError):
        validate_password("Hi1!")

@pytest.mark.parametrize("password", [
    "hello123!",   # No uppercase letter
    "HELLO123!",   # No lowercase letter
    "Helloabc!",   # No digit
    "Hello1234",   # No special character
])
def test_validate_password_missing_requirements(password):
    with pytest.raises(WeakPasswordError):
        validate_password(password)

@pytest.mark.parametrize("password", [
    "hello123!",   # No uppercase letter
    "HELLO123!",   # No lowercase letter
    "Helloabc!",   # No digit
    "Hello1234",   # No special character
])
def test_validate_password_missing_requirements(password):
    with pytest.raises(WeakPasswordError):
        validate_password(password)

@pytest.mark.parametrize("password", [
    "Abc123!x",
    "Abc123!x" + "a" * 120,
])
def test_validate_password_valid_lengths(password):
    assert validate_password(password) is True

def test_validate_password_whitespace():
    with pytest.raises(WeakPasswordError):
        validate_password("Hello 123!")

def test_validate_password_too_long():
    password = "Abc123!x" + "a" * 121

    with pytest.raises(WeakPasswordError):
        validate_password(password)

@pytest.mark.parametrize("password", [
    12345678,
    None,
    True,
])
def test_validate_password_invalid_type(password):
    with pytest.raises(TypeError):
        validate_password(password)

@pytest.mark.parametrize("username", [
    "Student123",
    "student_01",
    "Abc",
    "A" * 20,
])
def test_validate_username_valid(username):
    assert validate_username(username) is True

@pytest.mark.parametrize("username", [
    "Ab",                    # Too short
    "A" * 21,                # Too long
    "123Student",            # Starts with a digit
    "_Student",              # Starts with an underscore
    "Student Name",          # Contains a space
    "Student@123",           # Contains a special character
])
def test_validate_username_invalid(username):
    with pytest.raises(InvalidUsernameError):
        validate_username(username)
        
@pytest.mark.parametrize("username", [
    12345,
    None,
    True,
])
def test_validate_username_invalid_type(username):
    with pytest.raises(TypeError):
        validate_username(username)

@pytest.mark.parametrize("age", [
    13,
    18,
    65,
    120,
])
def test_validate_age_valid(age):
    assert validate_age(age) is True

@pytest.mark.parametrize("age", [
    13,
    18,
    65,
    120,
])
def test_validate_age_valid(age):
    assert validate_age(age) is True


@pytest.mark.parametrize("age", [
    12,
    121,
    -1,
    0,
])
def test_validate_age_out_of_range(age):
    with pytest.raises(InvalidAgeError):
        validate_age(age)

@pytest.mark.parametrize("age", [
    "18",
    18.5,
    True,
    None,
])
def test_validate_age_invalid_type(age):
    with pytest.raises(TypeError):
        validate_age(age)

def test_validate_registration_valid():
    data = {
        "username": "Student123",
        "email": "student@example.com",
        "password": "Hello123!",
        "age": 18,
    }

    assert validate_registration(data) is True

@pytest.mark.parametrize("missing_field", [
    "username",
    "email",
    "password",
    "age",
])

def test_validate_registration_missing_field(missing_field):
    data = {
        "username": "Student123",
        "email": "student@example.com",
        "password": "Hello123!",
        "age": 18,
    }

    del data[missing_field]

    with pytest.raises(ValidationError):
        validate_registration(data)

@pytest.mark.parametrize("field, invalid_value", [
    ("username", "Ab"),
    ("email", "invalid-email"),
    ("password", "weak"),
    ("age", 12),
])
def test_validate_registration_invalid_values(field, invalid_value):
    data = {
        "username": "Student123",
        "email": "student@example.com",
        "password": "Hello123!",
        "age": 18,
    }

    data[field] = invalid_value

    with pytest.raises(ValidationError):
        validate_registration(data)

@pytest.mark.parametrize("data", [
    None,
    "username=Student123",
    [],
])
def test_validate_registration_invalid_type(data):
    with pytest.raises(TypeError):
        validate_registration(data)