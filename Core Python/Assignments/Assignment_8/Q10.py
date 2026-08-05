# 10. WAP to check if entered year is a leap year or not.

def leap_year(year):
    if(year % 400 ==0 or year % 4 ==0 and year % 100 != 0):
        return 'Leap year'
    else:
        return 'Not leap year.'

year = int(input('Enter a year:'))
res = leap_year(year)
print(res)