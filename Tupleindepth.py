tup = ()
tup1 = (10,)
tup2 = 10,20,30
tup3 = 10,
print(type(tup))
print(type(tup1))
print(type(tup2))
print(type(tup3))
tup1 = (1,2,34,5,6,7)
tup2 = (10,11,23,2.334,'GQT')
tup = (1,(1,2,3),[2,3,4],{2,3,4},{1:'a'})
print(tup)
#tuple Packing
tup = (10,20,30,40,50)
a,b,c,d,e = tup
print(a)
print(b)
print(c)
#tuple Packing with disposal variable
a,_,c,_,e = tup
print(a)
tup1 = (12,34,56)
tup = (10,30,[10,30],(50,60),{60,70},{1:20,2:30})
print(tup)
print(tup[1])
print(tup[2][0])
tup23 = (10,20,30,40,50,60,70,80,90)
print(tup23[1:5])
print(tup23[-3:-7:-1])
print(tup23[-3:-7])
tup1 = (10,20,30,40,50)
print(tup1)
tup2 = tuple(tup1)
print(tup2)
print(id(tup2))
print(id(tup1))
import copy
tup1 = (10,20,30,40,50,60)
tup2 = copy.deepcopy(tup1)
print(id(tup1))
print(id(tup2))
print(max(tup1))
