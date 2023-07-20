student_scores = {
    "Harry": 87,
    "Ron": 76,
    "Hermine": 95,
    "Neville": 67
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding !"

    if student_scores[key] <= 90 and student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations !"

    if student_scores[key] <= 80 and student_scores[key] > 70:
        student_grades[key] = "Acceptable"

    if student_scores[key] <= 70:
        student_grades[key] = "Failed..."

print(student_grades)
