a = 10
b = 20.5
c = a + b
print(c)
a  = '10'
b = 20
c = b + int(a)
print(c)
print("No input no output function")
def perform_add():
    a = 10;
    b = 20;
    c = a + b
    print(c)
perform_add()
print("Input and No Output function")
def perform_sub(a,b):
    c = a - b;
    print(c)
perform_sub(10,30)
print("No input and output function")
def perform_mul():
    a = 10;
    return a * 10
res = perform_mul()
print(res)
print("input and output function")
def perform_div(x,y):
    z = x/y
    return z
res1 = perform_div(20,2)
print(res1)
def calc(x,y):
    a = x +y
    b = x-y
    c = x * y
    d = x / y
    return a,b,c,d
res2,res3,res4,res5 = calc(10,20)
print(res2)
def calculator(x,y):
    '''This function performs addition multiplication and division'''
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d
res2,res3,res4,res5 = calculator(10,20)
print(res3)
print(calculator.__doc__)