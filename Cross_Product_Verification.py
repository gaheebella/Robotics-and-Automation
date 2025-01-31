import numpy as np

u = np.array([3, -1, 1])
v = np.array([2, -3, 1])

cross_u_v = np.cross(u, v)

cross_v_u = np.cross(v, u)

#Verify orthogonality : dot product should be 0
#If u x v is orthogonal to both u and v, then their dot product should be 0
dot_u_cross = np.dot(u, cross_u_v)
dot_v_cross = np.dot(v, cross_v_u)

print(f"Cross Product u x v : {cross_u_v}")
print(f"Cross Product v x u : {cross_v_u}")
print(f"Dot product u · (u x v) : {dot_u_cross}")
print(f"Dot product v · (u x v) : {dot_v_cross}")
