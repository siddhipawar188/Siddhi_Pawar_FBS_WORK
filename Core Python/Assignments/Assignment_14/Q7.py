# Q7. Given two sets of numbers,write a python program to find the missing numbers in the second set as compared to the first 
# and vice versa.

s1 = {10,20,30,40,50}
s2 = {20,40,60,80,100}
print('First set:',s1)
print('SEcond set:',s2)
missing_in_s1 =s2.difference(s1)
missing_in_s2 = s1.difference(s2)
print('Missing numbers in s1:',missing_in_s1)
print('Missing numbers in s2:',missing_in_s2)