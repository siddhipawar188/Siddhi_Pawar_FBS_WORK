# Q3.WAP to accept basic salary of n emp.(n should be accepted from user.)If basic salary is below 20000 then da=10 %,ta =12% and 
# hra=15% otherwise da = 15% ,ta =18% and  hra = 20%.Based on this calculate the total salary of each emp and also total salary
#  of all emp.

n = int(input('Enter a employees:'))
# salary = int(input('Enter a salary:'))
total_salary=0


for i in range(1,n+1):
    print('Employee:',i)
    salary = int(input('Enter a salary:'))
    if salary < 20000:
        da = salary *(10 / 100)
        ta = salary *(12 / 100)
        hra = salary *(15 /100)
    else:
        da = salary *(15 / 100)
        ta = salary *(18 / 100)
        hra = salary *(20 / 100)
    emp_salary =salary + da + ta + hra
    print('employee',i,'total salary:',emp_salary)
    total_salary = total_salary + emp_salary
print('total emp salary:',total_salary)
