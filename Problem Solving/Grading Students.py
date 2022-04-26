grades_count = 4


grades = [73, 67, 38, 33]

def gradingStudents(grades):
    for i in range(0, len(grades)):
        if grades[i] >= 38:
            if 5 - (grades[i] % 5) < 3 and grades[i] % 5 != 0:
                grades[i] = grades[i] + 5 - (grades[i] % 5) 
    print(grades)
gradingStudents(grades)