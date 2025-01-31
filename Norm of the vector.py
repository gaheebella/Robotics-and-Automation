import numpy as np

#Define the vector
X = np.array([-2, 3, -1])

#compute the norm of the vector
norm_X = np.linalg.norm(X)

print(f"The norm of X is : {norm_X:.4f}")