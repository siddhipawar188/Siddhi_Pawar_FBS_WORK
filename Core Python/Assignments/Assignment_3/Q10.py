# WAP to check if person is eligible to marry or not(male age >=21 and female age >=18).

gender = input('Enter gender(F/M):')
age = int(input('Enter age:'))

if(gender == 'F'):
    if(age >=18):
        print('Eligible for marriage.')
    else:
        print('Not eligible for marriage.')
else:
    if(age >= 21):
        print('Eligible for marriage.')
    else:
        print('Not eligible for ,marriage.')