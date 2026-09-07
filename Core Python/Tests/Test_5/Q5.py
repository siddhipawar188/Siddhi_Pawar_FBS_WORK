# Q5.Python Program to Find the Union of two Lists without using set concept.

li1=[1,2,3,4,5]
li2=[4,5,6,7,8]
union=li1.copy()
for i in li2:
    if i not in union:
        union.append(i)
print('unoin :',union)