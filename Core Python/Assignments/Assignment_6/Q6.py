# WAP print following patterns.

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end = ' ')

    for j in range(1, i+1):
        print(chr(64 + j),end=' ')
        
    k= 65 + i
    for j in range(1,i):
        print(chr(k),end=' ')
        k += 1
    print()