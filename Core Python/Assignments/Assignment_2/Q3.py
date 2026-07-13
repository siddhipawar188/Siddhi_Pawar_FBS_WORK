#  Q3. Convert distant given in feet and inches into meter and centimeter.

# Input the distance in feet & inches
feet = int(input('Enter feet: '))
inches = int(input('Enter inches:'))

# Convert total distance into inches
total_inches = (feet * 12) + inches

# convert total inches into centimeter
total_cm = total_inches * 2.54

# find meters
meters = total_cm // 100

# find remaining centimeter
centimeters = total_cm % 100

# Display result
print(f'The total distance in meter is {meters} and centimeter is {centimeters}.')
