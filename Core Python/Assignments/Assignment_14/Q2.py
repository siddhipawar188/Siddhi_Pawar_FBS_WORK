# Q2. WAP to remove the intersection of a second set with a first set.

s1 = {10,20,30,40}
s2 = {30,40,50,60}
print('First set:',s1)
print('Second set:',s2)
s1.difference_update(s2)
print('s1 after removing intersection:',s1)