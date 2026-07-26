# Enter number of students from user. for those many students accept marks of 5 subject marks from user & calculate percentage. Display all percentage. & average percentage of students.

n = int(input('Enter no of students:'))
total_percentage = 0
for i in range(1,n + 1):
    print('student',i)
    total_marks = 0
    for j in range(1,6):
        marks = float(input('Enter marks of subject' + str(j) + ':'))
        total_marks = total_marks + marks
    percentage = (total_marks / 500)*100
    print('Percentage of student',i,':',percentage,'%')
    total_percentage = total_percentage + percentage
average_percentage = total_percentage / n
print('Average percentage:',average_percentage,'%')