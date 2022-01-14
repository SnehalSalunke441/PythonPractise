"""
def addval(a, b):
    add = a+b
    sub = a -b
    mut = a *b
    return(add, sub, mut)

a,b,c = addval(10,20)    
print('A: {} B: {} C:{}'.format(a,b,c))
"""

#Variable Length Arguments
def addval(a, *b):
    add = a
    for i in b:
        add = add + i
    return add    

ans = addval(10,20,15,25,35)    
print('Ans: {} '.format(ans))

# kwargs: Keyworded variable length arguments
def person(name, **data):
    print(name)
    print(data)

person('Snehal',age = 20, city="Mumbai", contact=1234567)    

#global variables
a = 10
def fun():
    global a    #imports global a in function
    a =  15
    b = 3
    print(a)
fun()
print(a)    
