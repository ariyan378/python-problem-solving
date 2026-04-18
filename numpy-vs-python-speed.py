# Speed comparison: Python list vs NumPy array
import time
import numpy as np
size = 1_000_0000

# Python list approach
py_list = list(range(size))
start = time.time()
result_py = [x * 1.10 for x in py_list]
py_time = time.time() - start

# NumPy approach
np_array = np.arange(size, dtype=float)
start = time.time()
result_np = np_array * 1.10
np_time = time.time() - start

print(f"Python loop time : {py_time:.4f} seconds")
print(f"NumPy time       : {np_time:.4f} seconds")
print(f"NumPy is {py_time/np_time:.1f}x faster!")