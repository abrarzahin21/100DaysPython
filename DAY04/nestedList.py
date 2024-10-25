#PROBLEM LINK : https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# SOLUTIONS


list_range = int(input())
nested_list = []
score_list = []
for x in range(1, list_range+1):
    name = input("Enter the name: ")
    score = float(input("Enter the score: "))
    
    nested_list.append([name,score])
    score_list.append(score)
#     name_list.append(name)
print(nested_list)
print(score_list)
# print(name_list)

sroted_score_list = list(set(score_list))
sroted_score_list = sorted(sroted_score_list)
secound_highest_val = sroted_score_list[1]
print(secound_highest_val)

name_list = []
for students in nested_list:
    if students[1] == secound_highest_val:
        name_list.append(students[0])
sorted_name_list = sorted(name_list)

for student_name in sorted_name_list:
    print(student_name)