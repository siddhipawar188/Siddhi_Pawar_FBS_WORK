# Q1. Convert the time entered in hh,min,sec into seconds

# Take input for hours,minute,second
hours=int(input('Enter hours:'))
minute=int(input('Enter minute:'))
second=int(input('Enter second:'))

# Convert into second
hours = hours * 3600
minute = minute * 60

total_second = hours + minute + second

# Display result
print(f'Total second : {total_second}.')