import numpy as np
import time

size=5000000

numbers=np.arange(size)

start=time.time()

python=[]

for i in numbers:
    python.append(i+5)

loop_time=time.time()-start

start=time.time()

numpy=numbers+5

numpy_time=time.time()-start

print("Loop:",loop_time)

print("NumPy:",numpy_time)

print("Speedup:",loop_time/numpy_time)