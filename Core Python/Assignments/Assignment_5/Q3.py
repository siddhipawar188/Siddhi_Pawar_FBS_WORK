# Accept no.of passengers from user & per ticket cost.Then accept age of each passenger & then calculate total amount to ticket to travel for all of them on followinf condition:
# a. Children below 12 = 30 % discount
# b. Senior citizen(above 59) = 50 % discount
# c. other need to pay full

n = int(input('Enter number of passengers:'))
i = 1
total_price = 0
while(i <=n):
    age = int(input(f'Enter the person {i} age:'))
    tick1 = int(input(f'Enter ticket price of passenger {i} :'))
    if(age < 12):
            total_price = total_price + (tick1 - tick1 * 0.3)
    elif(age > 59):
        total_price = total_price + (tick1 - tick1 * 0.5)
    else:
        total_price = total_price + tick1
    i += 1
print(f'Total amount of traveling is {total_price} .')