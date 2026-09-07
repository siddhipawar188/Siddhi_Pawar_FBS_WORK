# Create a class Product with members as pid,pname,price and quantity .Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:
    def __init__(self,pid=0,pname='Unknown',price=0,quantity='Unknown'):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def getPid(self):
        return self.pid
    def setPid(self,Npid):
        self.pid=Npid
    def getPname(self):
            return self.pname
    def setPname(self,Npname):
            self.pname=Npname
    def getPrice(self):
            return self.price
    def setPrice(self,Nprice):
            self.price=Nprice
    def getQuantity(self):
            return self.quantity
    def setQuantity(self,Nquantity):
            self.quantity=Nquantity

# ShowBook
    def show(self):
        print(f'Pid={self.pid} Pname={self.pname} Price={self.price} Quantity={self.quantity}')

# Destructor
    def __del__(self):
          print('Product object destroyed..')

# Parameterized
p1=Product(101,'Laptop',45000,1)
p1.show()

# Parameterless
p2=Product()
p2.show()