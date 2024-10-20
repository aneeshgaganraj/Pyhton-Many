num = [1,2,3,4,5,6]
sq_lst = []
for i in num:
    sq_lst.append(i**2)
print(sq_lst)
#using List comprehension
squares = [i**2 for i in num]
print(squares)
#using if
even_num = []
for i in num:
    if i % 2 == 0:
        even_num.append(i)
print(even_num)
even = [i for i in num if i % 2 == 0]
print(even)
even_num = []
for i in num:
    if i > 1:
        if i % 2 == 0:
            even_num.append(i)
print(even_num)
even = [i for i in num if i > 1 if i % 2 == 0]
print(even)
elseif = []
for i in num:
    if i % 2 == 0:
        elseif.append('*')
    else:
        elseif.append(i)
print(elseif)
esa = ['*' if i % 2 == 0 else i for i in num]
print(esa)
for j,i in enumerate(num):
    print("index: ", j ,"Value: ", i)
print('---------------------------------------------------------------------------')
for j in range(len(num)):
    print("index: ", j ,"Value: ", num[j])
lst = [[1,2,3],[4,5,6]]
for i in lst:
    for j in i:
        print(j)
lst1 = [3,6,7,5,2,1,10,8,9,4]
print(lst1)
lst2 = sorted(lst1)
print(lst2)
lst3 = sorted(lst1,reverse=True)
print(lst3)