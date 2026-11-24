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


from calculator import display_result


def test_display_result(capsys):
    display_result([80, 90, 100])

    captured = capsys.readouterr()

    assert "Average: 90.0" in captured.out
    assert "Letter Grade: A" in captured.out


def test_display_result_b(capsys):
    display_result([80, 85, 90])

    captured = capsys.readouterr()

    assert "Average: 85.0" in captured.out
    assert "Letter Grade: B" in captured.out


def test_single_grade():
    assert calculate_average([75]) == 75


def test_zero_grade():
    assert calculate_average([0]) == 0


def test_decimal_grades():
    assert calculate_average([85.5, 90.5]) == 88.0
