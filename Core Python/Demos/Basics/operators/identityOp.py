###identity compare memory address
#1 is
x=10
y=10
z=20

li1=[10,20]
li2=[10,20]

print(x is y)
print(id(x))
print(id(y))
print(id(z))
print(li1 is li2)
print(id(li1))
print(id(li2))
print(x is li1)

#2 is not
print(x is not li1)
print(x is not z)