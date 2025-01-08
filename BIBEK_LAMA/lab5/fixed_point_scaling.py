import numpy as np
import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    x_coords = []
    y_coords = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        x_coords.append(x0)
        y_coords.append(y0)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
            
    return x_coords, y_coords

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed_points = transformation_matrix @ points
    return transformed_points[0], transformed_points[1]

def plot_line_with_transformations(x0, y0, x1, y1):
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)
    scaling_matrix = np.array([[2, 0, 0], [0, 0.5, 0], [0, 0, 1]])
    translation_matrix = np.array([[1, 0, 3], [0, 1, 2], [0, 0, 1]])

    xf, yf = 1, 1 
    fixed_point_translation = np.array([[1, 0, -xf], [0, 1, -yf], [0, 0, 1]])
    fixed_point_inverse_translation = np.array([[1, 0, xf], [0, 1, yf], [0, 0, 1]])
    composite_matrix = fixed_point_inverse_translation @ scaling_matrix @ fixed_point_translation

    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)
    plt.figure(figsize=(8, 6))
    # Original line
    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')
    # Transformed line
    plt.plot(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')
 
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_line_with_transformations(2, 3, 10, 8)