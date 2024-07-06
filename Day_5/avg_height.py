# Input a Python list of student heights
student_heights = [40, 34, 223]
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_students = 0
for students in student_heights:
    total_students += students
print(f"total height = {total_students}")
n = 0
for no_of_students in student_heights:
    n += 1
print(f"number of students = {n}")

avg_height = round(total_students / n)
print(f"average height = {avg_height}")
