###numeric
#1 integer
var=10

#2 floating
var=3.14

#3 complex
var=10+5j     # real+ imaginary

#text
 #str
var ='firstbit solution'
var="firstbits solution"
var='''this is a first line
this is asecond line'''


#sequential
#! list
var=[10,20,30,40]
print(type(var))

#2 tuple
var=(10,20,30,40)
var=10,20,30,40 #tuple
print(type(var))

#3 range
var=range(1,100)
print(type(var))

##set type
#1set
var={10,20,30,40}

#frozenset
var=frozenset({10,20,30,40})

#mapping
#1 dict
var= {'id':101, 'name':'siddhi' ,'salary': 30000}

##other
#1 bool
var=True
#2 nonetype
var=None
print(type(var))
