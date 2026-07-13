# WAP to convert days into years,week & days

# Take input
days=int(input('enter a days:'))

# Convert daya into year
year=days // 365    #600 // 365=1
# print('year:',year)

# Remaining days
days=days % 365   #600 % 365=235
# print(days)

# Convert days into week 
week=days // 7  #235 // 7=33
# print('week:',week)

# Remaining days
days=days % 7   #235 % 7= 4
print(f'years:{year} , weeks:{week} , days:{days}')