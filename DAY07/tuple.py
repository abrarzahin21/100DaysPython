#PROBLEM LINK: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# SOLUTIONS

if __name__ == '__main__':
    n = int(input())
    intList = map(int, input().split())
    intTuple = tuple(intList)
    
    print(hash(intTuple))