# Q1. A list contains the denominations aas follows:
# D=[2000,500,200,100,50,20,10,5]
# Accept an amount  from user and calculate how many minimum number of notes will be needed for that amount.

D=[2000,500,200,100,50,20,10,5]
amount=int(input('Enter amount:'))
count=0
for note in D:
    count = count+ amount // note

print('Mnimum number of notes:',count)