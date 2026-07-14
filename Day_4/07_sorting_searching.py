import numpy as np

arr=np.array([10,4,8,6,3,10,8,2])

print(np.sort(arr))

print(np.unique(arr))

values,counts=np.unique(arr,return_counts=True)

print(values)

print(counts)

print(np.argmax(arr))

print(np.argmin(arr))