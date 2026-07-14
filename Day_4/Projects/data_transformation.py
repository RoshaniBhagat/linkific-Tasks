import numpy as np

temperature=np.array([25,30,32,28,35,40])

fahrenheit=(temperature*9/5)+32

normalized=(temperature-temperature.min())/(temperature.max()-temperature.min())

print("Original:",temperature)

print("Fahrenheit:",fahrenheit)

print("Normalized:",normalized)