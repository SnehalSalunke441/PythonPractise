from array import *
# sort an array in ascending order
arr = array('i', [53, 32, 15, 28, 11, 65, 98, 76])
#for i in range(len(arr) - 1):
#    for j in range(len(arr) - 1 - i):
#        if arr[j] > arr[j+1]:
#            temp = arr[j+1]
#            arr[j+1] = arr[j]
#            arr[j] = temp
#        j = j + 1    
#    i = i + 1
#print(arr)     


#find factorial of given number
#i = int(input("Enter a number: "))
#fact = 1
#while i>=1:
#    fact = fact * i
#    i = i - 1
#print(fact)    


#create array of 5 elements and delete value at index 2 without using in built func
#i = 2
#while i<= (len(arr)-2):
#    arr[i] = arr[i+1]
#    i = i + 1
#print(arr[0:len(arr)-1])    


#reverse an array without using in built func
newArr = array(arr.typecode, [])
sz = len(arr)-1
while sz >= 0:
    newArr.append(arr[sz])
    sz = sz - 1
print(arr)
print(newArr)    
