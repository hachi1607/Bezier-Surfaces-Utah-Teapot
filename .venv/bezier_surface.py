import numpy as np
from math import comb

def bernstein_polynomial(i, t):
    return comb(3, i) * (t ** i) * ((1 - t) ** (3 - i))

def bezier_surface(control_points, u, v):
    surface_point = np.zeros(3)
    for i in range(4):
        for j in range(4):
            B_i = bernstein_polynomial(i, u)
            B_j = bernstein_polynomial(j, v)
            surface_point += B_i * B_j * control_points[i][j]
    return surface_point