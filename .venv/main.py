import numpy as np
import pyvista as pv
from coordinates import load_coordinates
from bezier_surface import bezier_surface

def rgb_to_normalized(rgb_list):
    return [x/255.0 for x in rgb_list]

color1_rgb = [255, 255, 0]
color2_rgb = [255, 0, 255]
color3_rgb = [0, 255, 255]

color1 = rgb_to_normalized(color1_rgb)
color2 = rgb_to_normalized(color2_rgb)
color3 = rgb_to_normalized(color3_rgb)

patches = load_coordinates('teapot_coordinates.txt')

points = []
colors = []

# min i max z dla normalizacji
z_values = [point[2] for patch in patches for point in patch]
min_z = min(z_values)
max_z = max(z_values)

for patch in patches:
    for u in np.linspace(0, 1, 15):
        for v in np.linspace(0, 1, 15):
            point = bezier_surface(patch.reshape(4, 4, 3), u, v)
            points.append(point)

            z = point[2]
            normalized_z = (z - min_z) / (max_z - min_z)

            # interpolacja między trzema kolorami
            if normalized_z < 0.5:
                t = normalized_z * 2
                color = [color1[i] * (1 - t) + color2[i] * t for i in range(3)]
            else:
                t = (normalized_z - 0.5) * 2
                color = [color2[i] * (1 - t) + color3[i] * t for i in range(3)]

            colors.append(color)

points = np.array(points)
colors = np.array(colors)
cloud = pv.PolyData(points)
cloud["colors"] = colors

plotter = pv.Plotter()
plotter.add_mesh(cloud, scalars="colors", rgb=True, point_size=5)
plotter.show()