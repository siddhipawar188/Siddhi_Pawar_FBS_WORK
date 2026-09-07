# Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook


class Book:
    def __init__(self,bid=0, bname='unknown' ,price=0,author='unknown'):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
    def getBid(self):
        return self.bid
    def setBid(self,Nbid):
        self.bid=Nbid
    def getBname(self):
            return self.bname
    def setBname(self,Nbname):
            self.bname=Nbname
    def getPrice(self):
            return self.price
    def setPrice(self,Nprice):
            self.price=Nprice
    def getAuthor(self):
            return self.author
    def setAuthor(self,Nauthor):
            self.author=Nauthor

# ShowBook
    def Show(self):
        print(f'Bid={self.bid} Bname={self.bname} Price={self.price} Author={self.author}')

# Destructor
    def __del__(self):
          print('Book object destroyed.')

# parameterized
b1=Book(101,'Python',500,'Guido Van Rossum')
b1.Show()

# parameterless
b2=Book()
b2.Show()