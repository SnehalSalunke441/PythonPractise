import fun 

#print("Hello")

from functools import reduce
nums = [10, 20, 30, 40, 50]
#nums.remove(10)
#print(nums)
#nums.pop(1)
#print(nums)

#filter map reduce
lst = [10, 11, 12, 13, 14, 15, 21, 23, 24, 34, 45, 56, 76, 43 ]
evens = list(filter(lambda n: n%2==0, lst))
doubles = list(map(lambda db: 2 * db, evens))
sum = reduce(lambda a,b: a+b, doubles)

#print(sum)
#print(evens)
#print(doubles)

#Decorators
def div(a, b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return(inner)

div = smart_div(div)
div(5, 25)


#Modules
#x = fun.fact(10)
