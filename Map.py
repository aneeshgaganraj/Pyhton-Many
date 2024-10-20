lst = [1,2,3,4,5,6,7,8,9,10]
sq_lst = []
def sq_list(lst):
    for i in lst:
        sq_lst.append(i**2)
sq_list(lst)
print(sq_lst)
sq_lst = list(map(lambda i : i ** 2, lst))
print(sq_lst)