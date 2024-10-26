

n = int(input("Enter the list range value: "))
student_marks = {}
for _ in range(n):
    name, *line = input("Enter here: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter the name that you want to match? ")

# print(student_marks)

for students_name in student_marks:
    if(students_name == query_name):
        # print(students_name)
        new_list = student_marks[(students_name)]
        # print(new_list)
        student_marks_length = len(new_list)
        student_marks_sum = sum(new_list)
        avarage_marks = student_marks_sum/student_marks_length

# print(avarage_marks)

print(f'{avarage_marks:.2f}')
