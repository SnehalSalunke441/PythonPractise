from numpy import *
arr1  = array([[1, 2, 3, 10],
[4, 5, 6, 11],
[7, 8, 9, 12]])
#print(arr1.dtype)
#print(arr1.ndim)
#print(arr1.shape)
#print(arr1.size)
#arr2 = arr1.flatten()
#print(arr2)
#arr3 = arr1.reshape(2,6)
#arr4 = arr1.reshape(2,2,3)
#print(arr3)
#print(arr4)

m1 = matrix(arr1)
#print(m1)
#print(m1.min())
#print(m1.max())
m2 = m1.transpose()
#print(m2)
#m3 = m1 * m2
#print(m3)

# Code to multiply 2 matrices using 2d array and using loops
(a,b) = shape(m1)
(c,d) = shape(m2)
m = array(a,d)
if b!=c:
    print("Matrix multiplication not possible")
else:
    i,j = 0,0
    while i<a:
        while j<d:
            m[i,j] = 0
            sum = 0
            x,y = 0,0
            while x<b:
                while y<d:
                    sum = sum + m1[i,x]*m2[j,y]
                    y = y+1
                x = x+1
            m[i,j]= sum
            j = j +1
        i = i +1

print(m)




 

print(a)
