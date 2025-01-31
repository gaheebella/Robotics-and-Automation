import numpy as np

#define the unit vectors
i = np.array([1 ,0, 0])
j = np.array([0, 1, 0])
k = np.array([0, 0, 1])

#define the vector x
x = np.array([2, -3, 4])

#express x as a combination of i, j, k
#x1 = 2, x2 = -3, x3 = 4
x1, x2, x3 = x
linear_combination = x1 * i + x2 * j + x3 * k

print(f"Vector x : {x}")
print("Linear combination: {}i + {}j + {}k".format(x1, x2, x3))
