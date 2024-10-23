#PROBLEM LINK : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
#SOLUTION

n = int(input())
A = list(map(int, input().split()))

highest = max(A)

for x in A:
    if x != highest:
        secound_highest = [x]

print(max(secound_highest))



### FIND nth NUMBER OF HIGHEST VALUE RETURN FROM ANY LIST(DYNAMIC)

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
    



    










