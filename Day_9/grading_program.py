# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
#
# for student in student_scores:
#     if student_scores[student] >= 91 and student_scores[student] <= 100:
#         student_grades[student] = "Outstanding"
#     elif student_scores[student] >= 81 and student_scores[student] <= 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif student_scores[student] >= 71 and student_scores[student] <= 80:
#         student_grades[student] = "Acceptable"
#     elif student_scores[student] <= 70:
#         student_grades[student] = "Fail"
#     # print(student)
#     # print(student_scores[student])
#
# print(student_grades)

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
