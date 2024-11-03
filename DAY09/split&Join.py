#PROBLEM LINK : https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
# SOLUTIONS:

def split_and_join(line):
    result = line.split(" ")
    result = "-".join(result)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



# a = "this is a string"
# a = a.split(" ") # a is converted to a list of strings. 
# print(a)
# a = "-".join(a)
# print(a) 


