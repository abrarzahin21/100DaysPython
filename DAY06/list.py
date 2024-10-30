N = int(input("Enter the value range value: "))
userList = []

for x in range(N):
    userInput = input().split()

    if(userInput[0] == 'insert'):
        userList.insert(int(userInput[1]),int(userInput[2]))
    elif(userInput[0] == 'print'):
        print(userList)
    elif(userInput[0] == 'remove'):
        userList.remove(int(userInput[1]))
    elif(userInput[0] == 'append'):
        userList.append(int(userInput[1]))
    elif(userInput[0] == 'sort'):
        userList.sort()
    elif(userInput[0] == 'pop'):
        userList.pop()
    elif(userInput[0] == 'reverse'):
        userList.reverse()
    else:
        print("You are doing wrong method")

