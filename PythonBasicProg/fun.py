def addsub(x,y):
    c =  x + y
    d = x - y
    return c, d
    

#m, n = addsub(4,5)
#print("Sum = ", m, "Difference = ", n)

def update(x):
    x = 8
    print(x)

#a = 10
#update(a) 
#print(a)   

def add(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)

#add(2,3,4)
#add(2,3,4,5,6,7)

def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i,j)

#person("Snehal", age= 20, city= "Thane", contact= 12345678)

#abc =  10
def checkglb():
    x = globals()['abc'] 
    print("Inside function: x = ", x)
    globals()['abc'] = 20

#checkglb()
#print("Outside Function: abc = ",abc)   


#Function to return even and odd values from a list
def count(lst):
    ev = 0
    od = 0
    for i in lst:
        if i%2 == 0:
            ev = ev + 1
        else:
            od = od + 1
    return ev, od            

#lst = [10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 34, 45, 56]
#even, odd = count(lst)
#print("Even = {} and Odd = {}".format(even, odd))

#display names whose length is more than 5
def show(lst):
    for i in lst:
        if len(i)>5:
            print(i)

#lst = ["Snehal", "Neha", "Manisha", "Rani", "Teju", "Preeti", "Pooja"]
#show(lst)    


#Fibonacci series

def fib(n):
    a = 0
    b = 1
    if n <=0:
        print("Please enter valid input")
    elif n == 1:
        print(a)
    else:    
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

#fib(5)    

#Homework, print number till specified in fibonacci
def fibn(lim):
    a = 0
    b = 1
    if lim <=0:
        print("Please enter valid input")
    elif lim == 1:
        print(a)
    else:    
        print(a, end = " ")
        #print(b, end = " ")
        c = 1
        while c < lim:
            print(c, end = " ")
            c = a + b
            a = b
            b = c
#fibn(100)  

#Factorial

def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans * i
    print("Factorial = ", ans)    

#fact(10)   

#By Recursion
def factr(n):
    if n == 1:
        return(1)
    else:
        ans = n * factr(n-1)
        return(ans)

#ans = factr(10)   
#print("Factorial = ", ans)   

#lambda functions
f = lambda  a : a*a
result = f(10)
#print(result)

