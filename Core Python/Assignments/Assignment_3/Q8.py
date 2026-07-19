# WAP to prompt use to enter userid and password. after verifying userid and password display a 4 digit random number & ask user to enter the same. if user enters the same number then show him sucess message otherwise failed.(something like captcha).

import random
user_id =input("Enter the user id:")
password=input('Enter the password:')
if user_id == 'admin' and password == 'virat@123':
    captcha = random.randint(1000,9999)
    print(f'your captcha =  {captcha}')
    chuser=int(input('Enter the captcha=>'))
    if chuser ==(captcha):
        print('user login successfully..')
    else:
        print('invalid captcha')
else:
    print('user is invalid')