#PROBLEM LINK: https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
#SOLUTIONS:

# SOLUTION 1 USEING LIST COMPERHENTION:
def inputList(x,y,z,n):
    comprehentionList = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n] 
    return comprehentionList

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print(inputList(x,y,z,n))


# SOLUTION 2 USEING BASIC FOR LOOP/CONDITIONAL STATEMENT:

# def inputList(x,y,z,n):

#     for i in range(x+1):
#         # print(f"For x: {i}")

#         for j in range(y+1):
#             # print(f"For y: {j}")

#             for k in range(z+1):
#                 # print(f"For z: {k}")

#                 if(i+j+k != n): 
#                     print([i,j,k]) # PRINT IN THE LIST 


# if __name__ == '__main__':
#     x = int(input("Enter input for x: "))
#     y = int(input("Enter input for y: "))
#     z = int(input("Enter input for z: "))
#     n = int(input("Match the total sum input n: "))

# inputList(x,y,z,n)