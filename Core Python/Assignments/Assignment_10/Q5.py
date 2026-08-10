# Q5. Accept a number from user & check if this element in present in the list or not. Also tell how many times 
# it is present in the list.

li = [10,20,30,40,50,10,20,10]
num = int(input('Enter a number:'))
count = 0
for i in range(len(li)):
    if li[i] == num:
        count += 1
if count >0:
    print('Element is present.')
    print('Occurrencess:',count)
else:
    print('Element is not present.')