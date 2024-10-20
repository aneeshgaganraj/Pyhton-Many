from stringprep import b1_set

import calc
print(dir(calc))
print(calc.add(10,20))
print(calc.add.__doc__)
a = input()
print(type(a))
print("Enter second number")
b = input()
c = a  + b
print(c)
a1 = int(input())
b1 = int(input())
c1 = a1 + b1
print(c1)