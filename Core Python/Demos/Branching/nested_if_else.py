gender=input('Enter grnder(m/f):')
age=int(input('Enter a age:'))
if(gender=='f'):
    if(age>=18):
        print('girl is eligible for marrige.')
    else:
        print('not eligible for marrige')
else:
    if(age>=21):
        print('boys is eligible for marrige.')
    else:
        print('not eligible for marrige.')