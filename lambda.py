res = (lambda num,power: num ** power)(2,5)
print(res)
power = lambda num,power : (print('this calculates the power'), num ** power)
print(power(5,2))
print(power(2,3))
def multiplies(n):
    return lambda x:x*n
tripleer = multiplies(5)
doubler = multiplies(5)
print(tripleer(3))
print(doubler(2))
def tables(n):
    return lambda  x : x * n
table_calc = tables(5)
for i in range(1,11):
    print(5,  'X', i, '=', table_calc(i))