# Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .
# Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook


class Shirt:
    def __init__(self,sid=0,sname='Unknown',type='formal',price=0,size='small'):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size

    def getSid(self):
        return self.sid
    def setSid(self,Nsid):
        self.sid=Nsid
    def getSname(self):
        return self.sname
    def setSname(self,Nsname):
        self.sname=Nsname
    def getType(self):
        return self.type
    def setType(self,Ntype):
        self.type=Ntype
    def getPrice(self):
        return self.price
    def setPrice(self,Nprice):
        self.price=Nprice
    def getSize(self):
        return self.size
    def setSize(self,Nsize):
        self.size=Nsize

# Show
    def Show(self):
        print(f'Sid={self.sid} Sname={self.sname} Type={self.type} Price={self.price} Size={self.size}')

# Destroy
    def __del__(self):
        print('Shirt object destroyed...')

# Parameterized
s1=Shirt(101,'Raymond','Formal',500,'large')
s1.Show()

# Parameterless
s2=Shirt()
s2.Show()