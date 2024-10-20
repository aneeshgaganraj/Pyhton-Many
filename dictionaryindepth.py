d = {}
d1 = dict()
d = {1:'a',2:(10,20),3:{10,20,202,30},4:[12,23], 5: True}
print(d)
d[3] = 'c'
print(d)
d2 = {1:'a',2:'b',3:'c',4:[10,20]}
print(d2)
lst = d2[4]
lst.append(99)
print(d2)
print(d.get(4))
print(d.get(6))
print(d.pop(1))
print(d)
print(d.popitem())
print(d)
d.clear()
print(d)