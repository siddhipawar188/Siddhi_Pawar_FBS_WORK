rows = int(input('Enter rows:'))
k = (rows-3) + rows
print(k)
for i in range(1,rows+1):
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range(1,k+1):
        print(' ',end=' ')
    k-=2
    
    for j in range(1,i+1):
        # if (i<=4 or j<=4) :
        if(rows!=rows or j!=rows):
            print('*',end=' ')
    print()