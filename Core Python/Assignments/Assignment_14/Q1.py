# Q1. WAP to find elements in a given set that are not in another set.

s1 = {10,20,30,40,80}
s2 = {30,40,50,60,70}
print('Set 1:',s1)
print('Set 2:',s2)
res = s1.difference(s2)
print('Elements in s1 are not in s2:',res)