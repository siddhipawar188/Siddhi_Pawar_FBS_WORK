#WAP to find the area and perimeter of following figure 

length =int(input('Enter a length:'))
breadth=int(input('Enter a breadth:'))
redius = int(input('Enter a redius:'))

area = ((length * breadth ) + 0.5 * 3.14 * redius **2)
perimeter = (2 * length) + breadth + 3.14 * redius
print('area :',area)
print('perimeter:',perimeter)