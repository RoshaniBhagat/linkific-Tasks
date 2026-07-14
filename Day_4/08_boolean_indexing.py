import numpy as np

marks=np.array([45,72,90,34,65,88,95])

mask=marks>=70

print(mask)

print(marks[mask])

print(marks[marks<50])