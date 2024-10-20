import copy

lst = [1,2,3,4,5,[3,4],(78,90)]
print(lst)
lst1 = list([1,2,3])
print(lst[5][0])
print(lst[3])
print(lst[1:5])
print(lst[-1:-4:-1])
lst.append(23)
lst.insert(0,23)
print(lst)
lst2 = ['a']*5
print(lst2)
lst2  = lst2 + lst1
print(lst2)
lst2.extend([33,3.14,True])
print(lst2)
lst2.pop(2)
lst2.remove('a')
lst2.pop()
print(lst2)
del lst2[1:4]
print(lst2)
print(id(lst2))
print(id(lst1))
lst3 = lst2[:]
print(lst3)
lst4 = list(lst3)
print(lst4)
lst4 = [[1,2,3],[5,6,7]]
lst5  = copy.deepcopy(lst4)
lst6 = list(lst4)
lst6[1][1] = 55
print(lst4)
print(lst5)
print(lst6)
print(id(lst5))
print(id(lst4))
print(id(lst6))
lsts = [1,2,3,4,54,6,7,8,9,10]
print(lsts)
del lsts[4]
print(lsts)