import numpy as np 
import time
import sys

# Numpy array requires less memory than list
# li = range(100)
# print(sys.getsizeof(5)*len(li))

# ar = np.arange(100)
# print(ar.size * ar.itemsize)

# Numpy array is fast and convenient
sz = 10000000
l1 = range(sz)
l2 = range(sz)

ar1 = np.arange(sz)
ar2 = np.arange(sz)

start = time.time()
result = [(x+y) for x, y in zip(l1, l2)]
print("Python list time: ", (time.time()-start)*1000)
start = time.time()
result = ar1 + ar2
print("Numpy array time: ", (time.time()-start)*1000)