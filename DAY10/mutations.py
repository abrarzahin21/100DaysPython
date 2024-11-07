#PROBLEM LINK: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
# SOLUTIONS:

def mutate_string(string, position, character):
    stringList = list(string)
    stringList[position] = character
    newString = "".join(stringList)
    return newString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)





