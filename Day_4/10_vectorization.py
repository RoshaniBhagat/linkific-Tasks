import numpy as np
import time

numbers=np.arange(1000000)

start=time.time()

result=[]

for i in numbers:
    result.append(i*2)

end=time.time()

print("Python Loop:",end-start)

start=time.time()

result=numbers*2

end=time.time()

print("NumPy:",end-start)