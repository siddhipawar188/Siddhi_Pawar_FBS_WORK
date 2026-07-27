# WAP print following patterns.
#          1
#       1      1
#    1     2       1
#  1    3      3       1


for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64 + j),end=' ')
        # i +=1
    print()