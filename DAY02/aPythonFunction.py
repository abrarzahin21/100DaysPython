def is_leap(year):
    leap = True
    Not_Leap = False
    if(year % 400 == 0 or year % 100 != 0 and year % 4 == 0):
        return leap
    else:
        return Not_Leap
        
year = int(input())
print(is_leap(year))