import numpy as np

# Python list
py_list = [1, 2, 3, 4, 5]

# numpy array
np_arr = np.array([1, 2, 3, 4, 5])

# Multiply each element by 10
# Python: need a loop
py_result = [x * 10 for x in py_list]

# numpy: just multiply!
np_result = np_arr * 10

print('Python:', py_result)
print('numpy: ', np_result)