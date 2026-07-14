import numpy as np

sales=np.random.randint(100,1000,100)

print("Average:",np.mean(sales))

print("Median:",np.median(sales))

print("Highest:",np.max(sales))

print("Lowest:",np.min(sales))

print("Std:",np.std(sales))

print("90 Percentile:",np.percentile(sales,90))