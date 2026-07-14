import numpy as np

marks=np.array([78,85,91,62,73,88,95,81])

print("Mean:",np.mean(marks))

print("Median:",np.median(marks))

print("Standard Deviation:",np.std(marks))

print("Minimum:",np.min(marks))

print("Maximum:",np.max(marks))

print("25th Percentile:",np.percentile(marks,25))

print("75th Percentile:",np.percentile(marks,75))