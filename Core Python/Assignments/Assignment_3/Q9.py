# Input 5 subject marks from user & display grade.

sub1 = int(input('Enter marks:')) 
sub2 = int(input('Enter marks:')) 
sub3 = int(input('Enter marks:')) 
sub4 = int(input('Enter marks:')) 
sub5 = int(input('Enter marks:')) 

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total/500)*100

if(percentage >= 60):
    print('First class.')
elif(percentage >=50):
    print('Second class.')
elif(percentage >= 35):
    print('Pass')
else:
    print('Fail')