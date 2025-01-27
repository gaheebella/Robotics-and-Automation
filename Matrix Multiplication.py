import numpy as np

A = np.array([[1,2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = np.dot(A, B)

print(f"Matrix A: {A}")
print(f"\nMatrix B: {B}")
print(f"\nMatrix Multiplication Result (C = A * B) :{C}")
