import numpy as np

height = [1.23, 1.34, 2.33, 1.89, 1.77]
weight = [65, 45.8, 55.7, 88.2, 68.7]

np_h = np.array(height)
np_w = np.array(weight)

bmi = np_w / np_h ** 2
print(bmi)

print(bmi>23)

bmi = bmi[bmi<23]
print(bmi)

np_2d = np.array([[1,2,3],[4,5,6]])
print(np_2d)
print(np_2d.shape)