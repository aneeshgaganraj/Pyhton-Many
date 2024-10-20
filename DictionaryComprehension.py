d1 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f'}
d2 = {7:'g',8:'h'}
d3 = {**d1,**d2}
print(d3)
d = {}
lst = [1,2,3,4,5]
for i in lst:
    d[i] = i **2
print(d)
print({i : i**2 for i in lst})
d1 = {}
for i in lst:
    if i % 2 == 0:
        d1[i] = i**2
print(d1)
print({i : i ** 2 for i in lst if i % 2 == 0})
print({i : i ** 2 if i % 2 == 0 else i**3 for i in lst})
print({i**2  if i % 2 == 0 else i**3 : 'Square' if i % 2 == 0 else  'cube' for i in lst})
vehicles = ["bike","car","Bus"]
wheels = [2,4,4]
for i in zip(vehicles,wheels):
    print(i)#unzip
for i,j in zip(vehicles,wheels):
    print(i,j)
energy = ["Acceleration","Wheels","Gear"]
for i in zip(vehicles,energy,wheels):
    print(i)