# numpy program to create a 2d array with 1 on the border and 0 inside

import numpy as np
x = np.ones((5,5))
print("print orginal 2d array")
print(x)

print("1 on the border and 0 inside in the array")

x[1:-1,1:-1] = 0
print(x)