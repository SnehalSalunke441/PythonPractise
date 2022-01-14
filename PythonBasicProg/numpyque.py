from numpy import *
#Add 2 array using for loop
arr1 = array([12, 14, 23, 16, 21], int)
arr2 = array([1, 2, 3, 6, 2], int)
arr3 = arr1.copy()
for i in range(len(arr1)):
    arr3[i] = arr1[i] + arr2[i]
    
print(arr3)    

print()
#Find maximum value without using built in function
#arr = array([12, 514, 23, 116, 21], int)
mx = arr3[0]
for i in range(len(arr3)-1):
    if arr3[i] > mx:
        mx = arr3[i]
print("Maximum value: ", mx)       