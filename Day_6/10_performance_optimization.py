import pandas as pd
import time

print("=" * 70)
print("PANDAS PERFORMANCE OPTIMIZATION")
print("=" * 70)

# --------------------------------------------------------
# Load Dataset
# --------------------------------------------------------

sales = pd.read_csv("datasets/large_sales.csv")

print("\nOriginal Dataset")
print(sales.head())

# --------------------------------------------------------
# Create Total Amount
# --------------------------------------------------------

sales["TotalAmount"] = sales["Quantity"] * sales["Price"]

print("\nDataset with Total Amount")
print(sales.head())

# ========================================================
# Loop Method
# ========================================================

print("\n" + "=" * 70)
print("Loop Method")
print("=" * 70)

start = time.time()

totals = []

for index, row in sales.iterrows():
    totals.append(row["Quantity"] * row["Price"])

end = time.time()

print("Execution Time :", round(end - start, 6), "seconds")

# ========================================================
# Vectorized Method
# ========================================================

print("\n" + "=" * 70)
print("Vectorized Method")
print("=" * 70)

start = time.time()

sales["VectorizedTotal"] = sales["Quantity"] * sales["Price"]

end = time.time()

print("Execution Time :", round(end - start, 6), "seconds")

print("""
Observation:
Vectorized operations are significantly faster than loops
because Pandas performs calculations internally using NumPy.
""")

# ========================================================
# Memory Usage
# ========================================================

print("\n" + "=" * 70)
print("Memory Usage")
print("=" * 70)

print(sales.memory_usage(deep=True))

print("\nTotal Memory Used")

memory = sales.memory_usage(deep=True).sum()

print(memory, "bytes")

# ========================================================
# Optimize Data Types
# ========================================================

print("\nOptimizing Data Types")

optimized = sales.copy()

optimized["Category"] = optimized["Category"].astype("category")
optimized["City"] = optimized["City"].astype("category")
optimized["Customer"] = optimized["Customer"].astype("category")

print("\nMemory After Optimization")

print(optimized.memory_usage(deep=True))

print("\nTotal Memory")

print(optimized.memory_usage(deep=True).sum(), "bytes")

# ========================================================
# Reading Large CSV in Chunks
# ========================================================

print("\n" + "=" * 70)
print("Reading CSV in Chunks")
print("=" * 70)

chunk_number = 1

for chunk in pd.read_csv(
        "datasets/large_sales.csv",
        chunksize=5):

    print(f"\nChunk {chunk_number}")

    print(chunk)

    chunk_number += 1

print("\nProgram Completed Successfully")