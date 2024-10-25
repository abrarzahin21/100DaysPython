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