s = set()
s = {10,20,30,40}
s = {10,20.5,(3,4)}
print(s)
print(type(s))
s1 = {1,2,3,4,5}
s2 = {6,7,8,9,10}
s3 = s1 | s2
s4 = s1.union(s2)
print(s3)
print(s4)
s3 = s1 & s2
print(s3)
s4 = s1.intersection(s2)
print(s4)
s1 = {1,2,3,4,5}
s2 = {6,7,8,9,10,4,5}
s3 = s1 - s2
print(s3)
s2 = {12,34,56,78,6,7,8}
s4 = {6,7,8,10,45,67,78,99,200}
s5 = s2-s4
print("Difference is: ",s5)
s1 = {1,2,3,4,5,6,7,8,9}
s2 = {1,2,3,4}
print(s2.issubset(s1))
s1.add(45)
print(s1)
s1.discard(89)
s1.remove(45)
print(s1)
s = frozenset([12,34,56])
print(s)
s1 = {7,8,9,11,1,2,3,4,5,6,5}
s2 = {7,11,2,1}
s3 = {10,20,30,40}
print(s2.isdisjoint(s1))
print(s3.isdisjoint(s1))