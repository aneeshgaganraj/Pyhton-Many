from _collections_abc import async_generator


def power_off(num,power = 3):
    return num**power
print(power_off(3,4))
print(power_off(power=2,num=5))
print(power_off(3))
def pizza_toppings(*toppings):
    print(toppings)
pizza_toppings("onion","corn","cheese","chicken")
def submit(**details):
    print(details)
submit(name = "aneesh",age = 20, mobile = "867543")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
res = factorial(5)
print(res)