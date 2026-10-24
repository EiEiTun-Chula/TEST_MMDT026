import pytest
from src.calculator import calculate_average, find_maximum, is_prime, factorial, power
def test_calculate_average_normal():
    scores = [60, 80, 100]
    result = calculate_average(scores)

    assert result == 80.0
def test_calculate_average_minimum():
    result = calculate_average([0])
    assert result == 0.0


def test_calculate_average_maximum():
    result = calculate_average([100])
    assert result == 100.0

def test_calculate_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])

@pytest.mark.parametrize("scores", [
    [-1, 50],
    [101, 50],
])
def test_calculate_average_out_of_range(scores):
    with pytest.raises(ValueError):
        calculate_average(scores)

@pytest.mark.parametrize("scores", [
    [80, "90"],
    [True, 80],
])
def test_calculate_average_invalid_type(scores):
    with pytest.raises(TypeError):
        calculate_average(scores)

def test_find_maximum_normal():
    numbers = [10, 50, 30]
    result = find_maximum(numbers)
    assert result == 50

@pytest.mark.parametrize("numbers, expected", [
    ([-10, -5, -20], -5),
    ([10, 10, 5], 10),
    ([42], 42),
])
def test_find_maximum_special_cases(numbers, expected):
    result = find_maximum(numbers)
    assert result == expected

def test_find_maximum_empty_list():
    with pytest.raises(ValueError):
        find_maximum([])

@pytest.mark.parametrize("numbers", [
    [10, "20", 30],
    [True, 20, 30],
])
def test_find_maximum_invalid_type(numbers):
    with pytest.raises(TypeError):
        find_maximum(numbers)

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, True),
    (7, True),
    (9, False),
    (10, False),
    (1, False),
    (0, False),
    (-5, False),
])
def test_is_prime_valid_integers(number, expected):
    assert is_prime(number) == expected

@pytest.mark.parametrize("number, expected", [
    (29, True),
    (49, False),
    (97, True),
    (121, False),
])
def test_is_prime_larger_numbers(number, expected):
    assert is_prime(number) == expected

@pytest.mark.parametrize("number", [
    "7",
    7.5,
    True,
])
def test_is_prime_invalid_type(number):
    with pytest.raises(TypeError):
        is_prime(number)

@pytest.mark.parametrize("number, expected", [
    (0, 1),
    (1, 1),
    (3, 6),
    (5, 120),
    (7, 5040),
])
def test_factorial_valid_numbers(number, expected):
    assert factorial(number) == expected

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

@pytest.mark.parametrize("number", [
    "5",
    5.5,
    True,
])
def test_factorial_invalid_type(number):
    with pytest.raises(TypeError):
        factorial(number)

@pytest.mark.parametrize("base, exponent, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -2, 0.25),
    (-2, 3, -8),
    (0, 5, 0),
])
def test_power_valid_inputs(base, exponent, expected):
    assert power(base, exponent) == expected

@pytest.mark.parametrize("base, exponent, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -2, 0.25),
    (-2, 3, -8),
    (0, 5, 0),
])
def test_power_valid_inputs(base, exponent, expected):
    assert power(base, exponent) == expected

def test_power_zero_negative_exponent():
    with pytest.raises(ValueError):
        power(0, -1)

@pytest.mark.parametrize("base, exponent", [
    ("2", 3),
    (True, 3),
    (2, "3"),
    (2, 2.5),
    (2, False),
])
def test_power_invalid_types(base, exponent):
    with pytest.raises(TypeError):
        power(base, exponent)