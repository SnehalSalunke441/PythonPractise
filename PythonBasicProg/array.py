from array import *

""" 
This is similar to multiline comment, but bad practise for comment.
Treated as documentation by interpreter
hello
hii
hey
"""
#vals = array('i', [1, 2, 3, 4])
#print("Printing values ", vals)
#print("Printing size of array " ,vals.buffer_info())
#print("Printing Typecode ",vals.typecode)

#vals.append(5) 
#vals.remove(2) 
#vals.reverse()
#print(vals)

#for e in vals:
#    print(e)

#newarr = array(vals.typecode, (a*a for a in vals) )  
#print(newarr) 

#USer input array

arr = array('i', [])
sz = int(input("Enter size of array:  "))
for i in range(sz):
    x = int(input("Enter element of array:"))
    arr.append(x)
print(arr)  

sk = int(input("Enter an element to search: "))
index = 0
for p in arr:
    if p == sk:
        print("Index = ", index)
        break
    index = index + 1
        
else:
    print("Element not found")    

print("Using Built in function: ", arr.index(sk))    