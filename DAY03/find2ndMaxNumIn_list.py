#PROBLEM LINK : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
#SOLUTION

# n = int(input())
# A = list(map(int, input().split()))

# highest = max(A)
# secound_highest = float('-inf')  # Initialize with negative infinity

# for x in A:
#     if x != highest and x > secound_highest:
#         secound_highest = x

# print(secound_highest)



## FIND nth NUMBER OF HIGHEST VALUE RETURN FROM ANY LIST(DYNAMIC)

# num = int(input("Enter the list range value: "))
# arr = []

# for x in range(1,num+1):
#     num = int(input(f"Enter the {x} value: "))
#     arr.append(num)
#     arr.sort()    #sort the list at the assisding order

# new_list = list(set(arr))     #remove the dublicate value from the sorted list 
# new_list_sorted = sorted(new_list, reverse=True)    #reverse the sorted list 
# new_list_length = len(new_list)
# # print(new_list_sorted)
# # print(new_list_length)

# nth_max_val = int(input("Which highest value you want to return?: "))

# if(new_list_length >= nth_max_val):
#     print( f"Returing the {nth_max_val} highest value is {new_list_sorted[(nth_max_val-1)]}")
# elif(new_list_length <=nth_max_val):
#     print(f"you have to input the highest value range(0 to {new_list_length}) ")
    



    









#PROBLEM LINK : https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# SOLUTIONS


input_num = int(input("Enter the list range value: "))
empty_list = []

for x in range(1, input_num + 1):
    name = input("Enter the name: ")
    score = float(input("Enter the score: "))
    
    # Append each entry as a dictionary to the list
    empty_list.append({name,score})

# Sort the list based on the "Score" key in descending order
empty_list.sort(key=lambda x: x["Score"], reverse=True)

print("Sorted List in Descending Order:")
for item in empty_list:
    print(f"Name: {item['Name']}, Score: {item['Score']}")




