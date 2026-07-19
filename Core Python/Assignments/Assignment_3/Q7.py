# WAP to check if user has entered correct userid and password.

userid = input('Enter userid:')
password = input('Enter password:')

if(userid == 'ADMIN' and password == '123'):
    print('userid and password are valid.')
else:
    print('userid and password are not valid.')