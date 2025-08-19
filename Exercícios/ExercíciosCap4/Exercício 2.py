import numpy as np

array1 = np.arange(0, 52, 2)
array2 = np.arange(100, 49, -2)

array3 = np.concatenate((array1, array2))
print(np.sort(array3))