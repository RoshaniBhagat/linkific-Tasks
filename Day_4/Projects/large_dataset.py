import numpy as np

data=np.random.randint(1,1000,(10000,5))

print(data.shape)

print("Column Means")

print(np.mean(data,axis=0))

print("Column Max")

print(np.max(data,axis=0))

print("Rows where first column >500")

filtered=data[data[:,0]>500]

print(filtered.shape)