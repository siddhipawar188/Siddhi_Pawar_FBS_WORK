# WAP to prompt user to enter userid and password .if id & passsword is incorrect give him chance to re-enter the credentials.let him try 3 times after that programe to terminate.

attempt =1
while(attempt <= 3):
    userid = input('Enter userid:')
    password = input('Enter password:')
    if(userid =='admin' and password =='1234'):
        print('Login successfully')
        break
    else:
        print('Incorrect userid and password')
        attempt+=1
if(attempt > 3):
    print('Terminate program.')