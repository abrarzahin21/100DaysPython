#PROBLEM LINK: https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
#SOLUTIONS 


def print_full_name(first, last):
    return print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    print_full_name(first_name,last_name)