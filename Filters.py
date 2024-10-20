lst1 = [1,2,3,4,5,6,7,8,9,10]
def even_list(list):
   even = []
   for i in list:
       if i % 2 == 0:
           even.append(i)
print(even_list(lst1))
#using filters
lst = [1,2,3,4,5,6,7,8,9,10]
s = list(filter(lambda i : i % 2 == 0, lst))
print(s)
def even_filters1(n):
    if n % 2 == 0:
        return True
    else:
        return False
hh = list(filter(even_filters1,lst))
print(hh)