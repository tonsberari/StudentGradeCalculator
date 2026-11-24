
def calculate_average(grades):
    if not grades:
        raise ValueError("Grade list cannot be empty.")

    total = 0
    for grade in grades:
        total += grade

    return total / len(grades)


def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def display_result(grades):
    average = calculate_average(grades)
    letter = get_letter_grade(average)

    print("Average:", average)
    print("Letter Grade:", letter)


if __name__ == "__main__":
    student_grades = [85, 90, 78, 92]
    display_result(student_grades)
