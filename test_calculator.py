from calculator import calculate_average, get_letter_grade


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90


def test_letter_grade_a():
    assert get_letter_grade(95) == "A"


def test_letter_grade_b():
    assert get_letter_grade(85) == "B"


def test_letter_grade_c():
    assert get_letter_grade(75) == "C"


def test_letter_grade_d():
    assert get_letter_grade(65) == "D"


def test_letter_grade_f():
    assert get_letter_grade(45) == "F"

import pytest


def test_empty_grades():
    with pytest.raises(ValueError, match="Grade list cannot be empty"):
        calculate_average([])