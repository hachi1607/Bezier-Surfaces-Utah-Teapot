import numpy as np

def load_coordinates(file_name: str):
    patches = []
    patch_points = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '3 3':
                if patch_points:
                    patches.append(patch_points)
                    patch_points = []
            else:
                x, y, z = map(float, line.split())
                patch_points.append([x, y, z])

        if patch_points:
            patches.append(patch_points)

    patches = [np.array(patch) for patch in patches]
    return np.array(patches)