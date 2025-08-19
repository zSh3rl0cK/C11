import numpy as np

array1 = np.ones(8)
array2 = np.random.randint(0, 10, 8)

array3 = (array1 + array2)

print(array3.sum(axis=0))

if array3.sum(axis=0) >= 40:
    print(np.array([array3]).reshape(4,2))
else:
    print(np.array([array3]).reshape(2,4))
