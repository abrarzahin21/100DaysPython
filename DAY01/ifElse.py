#Problem link : https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
#SOLVE:

n = int(input(""))
if(n % 2) == 0:
    if(2 <= n <= 5):
        print("Not Weird")
    elif(6 <= n <= 20):
        print("Weird")
    elif(n > 20):
        print("Not Weird")
else:
    print("Weird")


