# WAP to calculate profit or loss.

cost_price = int(input('Enter cost price:'))
selling_price = int(input('Enter selling price:'))

if(cost_price < selling_price):
    print('profit')
elif(cost_price>selling_price):
    print('loss')
else:
    print('No profit No loss')