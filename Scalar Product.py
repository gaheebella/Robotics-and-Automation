import numpy as np

X = np.array([1, 2, 3])
Y = np.array([4, 5, 6])

dot_product = np.dot(X, Y)
print(f"Dot product (X, Y): {dot_product}")

#compute the norms of X and Y
norm_X = np.linalg.norm(X)
norm_Y = np.linalg.norm(Y)
print(f"||X||: {norm_X:.4f}")
print(f"||Y||: {norm_Y:.4f}")

#Cauchy-Schwarz inequality
cauchy_schwarz = abs(dot_product) <= norm_X * norm_Y
print(f"Cauchy_Shwarz inequality holds: {cauchy_schwarz}")

#Triangle inequality
triangle_inequality = np.linalg.norm(X + Y) <= norm_X + norm_Y
print(f"Trianlge inequality holds: {triangle_inequality}")

#Scalar Product
cos_theta = dot_product / (norm_X * norm_Y)
theta = np.arccos(cos_theta) #angle in radians
print(f"cosθ: {cos_theta:.4f}")
print(f"angle θ (in degrees): {np.degrees(theta):.2f}")