sum_grade = 0
for i in range(5):
    grade = int(input())
    if grade <= 40:
        grade = 40
    sum_grade += grade
print(sum_grade//5)   