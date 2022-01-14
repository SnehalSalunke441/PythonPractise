from numpy import *

#creating array
#method 1: using array()
#arr = array([1, 2, 3, 4, 5])
#print(arr.dtype)
#print(arr)

# (2) Using ones()
arr1 = ones(6, int)
#print(arr1)

# (3) Using zeros()
#arr2 = zeros(9)
#print(arr2)  

# (4) Using arange()
arr3 = arange(0, 12 ,2, int)  #here, 2 is step size
#print(arr3)

# (5) Using linspace()
#arr4 = linspace(0, 9, 10)  #here, 10 is number of parts
#print(arr4)

# (6) Using logspace()
#arr5 = logspace(0, 5, 6)
#print(arr5)

arr1 = arr1 + 3
#print(arr1)
arr6 = arr1 + arr3
#print(arr6)
#print(sin(arr6))
#print(cos(arr6))
#print(max(arr6))
#print(min(arr6))
#print(sqrt(arr6))
#print(log(arr6))
#print(concatenate([arr1, arr6]))

#newarr = arr1   #id is same, array is same but 2 variables are pointing to same array

#Shallow copy
#newarr = arr1.view()    #id is different, but both array are dependent, changes reflect in both 

#Deep copy
newarr = arr1.copy()   #id is different and array are also independent
arr1[1] = 500
print(newarr)
print(id(arr1))
print(id(newarr))