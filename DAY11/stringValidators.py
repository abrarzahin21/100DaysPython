#PROBLEM LINK: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

#SOLUTIONS1:

def is_alphanumeric(string):
    return any(char.isalnum() for char in string)
    
def is_alphabetical(string):
    return any(char.isalpha() for char in string)
    
def is_digit(string):
    return any(char.isdigit() for char in string)
    
def is_lower(string):
    return any(char.islower() for char in string)
    
def is_upper(string):
    return any(char.isupper() for char in string)


if __name__ == '__main__':
    s = input()

    print(is_alphanumeric(s))
    print(is_alphabetical(s))
    print(is_digit(s))
    print(is_lower(s))
    print(is_upper(s))




#SOLUTIONS1:

# if __name__ == '__main__':
#     s = input()

#     print(any(char.isalnum() for char in s))
#     print(any(char.isalpha() for char in s))
#     print(any(char.isdigit() for char in s))
#     print(any(char.islower() for char in s))
#     print(any(char.isupper() for char in s))




        