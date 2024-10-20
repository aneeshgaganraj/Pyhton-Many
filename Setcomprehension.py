num = {1,2,3,4,5}
sq_set = set()
for i in num:
    sq_set.add(i**2)
print(sq_set)
#using set comprehension
squares = {i**2 for i in num}
print(squares)
num1 = {12,34,56,5,3,2,1}
even_num = set()
for i in num1:
    if i % 2 == 0:
        even_num.add(i)
print(even_num)
evenset = {i for i in num1 if i % 2 == 0}
print(evenset)
evendu = set()
for i in num1:
    if i > 5:
        if i % 2 == 0:
            evendu.add(i)
print(evendu)
evensets = {i for i in num1 if i > 5 if i % 2==0}
print(evensets)
sets = {1, 2, 34, 3, 5, 56, 12}
elses = {'*' if i % 2 == 0 else i for i in sets}
print(elses)


