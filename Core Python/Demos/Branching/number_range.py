num = int(input('Enter number:'))

if(num > 0):
    if(num >=50):
        if(num >= 100):
            if(num >= 150):
                if(num >= 200):
                    if(num >250):
                        print('The number is greater than 201 or less than 250.')
                    else:
                        print('The number is greater than 250')
                else:
                    print('The number is greater than 151 or less than 200.')
            else:
                print('The number is greater than 101 or less than 150.')
        else:
            print('The number is greater than 51 or less than 100.')
    else:
        print('The number is greater than 0 and less than equal to 50.')
else:
    print('Number is less than 0. ')