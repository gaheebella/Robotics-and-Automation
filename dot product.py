import numpy as np

a = np.array([-12, 2, -2])
b = np.array([-14, 10, -4])

dot_product = np.dot(a, b)
print(f"DOt Product: {dot_product}")

norm_a = np.sqrt(np.dot(a, a))
print(f"norm of vector a: {norm_a:.4f}")


norm_b = np.sqrt(np.dot(b, b))

#Cauchy-Schwarz inequality
left_side = abs(np.dot(a, b))
right_side = norm_a * norm_b
print(left_side)
print(right_side)
print(f"Cauchy-Schwarz inequality holds: {left_side <= right_side}")