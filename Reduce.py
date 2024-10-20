from functools import reduce

lst = [1,2,3,4,5]
def reduce_lst(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
result = reduce_lst(lst)
print(result)
# using reduce
sum =  reduce(lambda i,j: i+j, lst)
print(sum)