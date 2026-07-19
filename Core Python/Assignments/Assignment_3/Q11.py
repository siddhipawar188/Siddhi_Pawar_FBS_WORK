# Accept age of five people & also per person ticket amount & then calculate total ammount to ticket  to travel for all of them based on following condition:
#  a. children below 12 = 30% discount.
#  b. Senior citizen (above 59) =50%.
#  c. other need to pay full.

age1 = int(input('Enter age:'))
tk1 = int(input('Enter ticket price:'))
total_price = 0
if(age1 < 12):
    total_price = total_price + (tk1 - tk1 * 0.3)
elif(age1 >= 59):
    total_price = total_price + (tk1 - tk1 * 0.5)
else:
    total_price = total_price + tk1


age2 = int(input('Enter age:'))
tk2 = int(input('Enter ticket price:'))

if(age2<12):
    total_price = total_price + (tk2 - tk2 * 0.3)
elif(age2 >=59):
    total_price = total_price + (tk2 - tk2 *0.5)
else:
    total_price = total_price + tk2

age3 = int(input('Enter age:'))
tk3 = int(input('Enter ticket price:'))

if(age3<12):
    total_price = total_price + (tk3 - tk3 * 0.3)
elif(age3 >=59):
    total_price = total_price + (tk3 - tk3 *0.5)
else:
    total_price = total_price + tk3

age4 = int(input('Enter age:'))
tk4 = int(input('Enter ticket price:'))

if(age4 <12):
    total_price = total_price + (tk4 - tk4 * 0.3)
elif(age4 >=59):
    total_price = total_price + (tk4 - tk4 *0.5)
else:
    total_price = total_price + tk4

age5 = int(input('Enter age:'))
tk5 = int(input('Enter ticket price:'))

if(age5<12):
    total_price = total_price + (tk5 - tk5 * 0.3)
elif(age5 >=59):
    total_price = total_price + (tk5 - tk5 *0.5)
else:
    total_price = total_price + tk5
print('Total price is',total_price)

