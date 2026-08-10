# calculate the cost of paintaing the following building's walls (both interior and exterior).you need to accept area(one wall)and 
# cost of both interior and exterior wall

area = int(input('Enter area:'))
interior = int(input('Cost of interior:'))
exterior = int(input('Cost of exterior:'))

interior_cost = interior *area
exterior_cost = exterior * area
total = interior_cost + exterior_cost

print('Cost of paintaing is',total)