import numpy as np

number_of_students = int(input("Enter the number of students: "))
number_of_subjects = int(input("Enter the number of subjects: "))

grades = np.zeros((number_of_students, number_of_subjects))

names = []

for i in range(number_of_students):
    name = input(f"Enter the name of student {i + 1}: ")
    names.append(name)

    for j in range(number_of_subjects):
        grades[i, j] = float(input(f"Enter the grade for subject {j + 1}: "))

total_grades = np.sum(grades, axis=1)

percentages = (total_grades / (number_of_subjects * 100)) * 100

print()
print(f"{'Name':<30}{'Total':<10}{'Percentage':<15}{'Grade'}")
print("-" * 65)

for i in range(number_of_students):
    if percentages[i] >= 90:
        grade = "A+"
    elif percentages[i] >= 80:
        grade = "A"
    elif percentages[i] >= 70:
        grade = "B+"
    elif percentages[i] >= 60:
        grade = "B"
    elif percentages[i] >= 50:
        grade = "C"
    else:
        grade = "F"

    name = names[i]

    if len(name) <= 25:
        print(f"{name:<30}{total_grades[i]:<10.0f}{percentages[i]:<15.2f}{grade}")
    else:
        words = name.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= 25:
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "

        if current_line:
            lines.append(current_line.strip())

        print(f"{lines[0]:<30}{total_grades[i]:<10.0f}{percentages[i]:<15.2f}{grade}")

        for line in lines[1:]:
            print(f"{line:<30}")