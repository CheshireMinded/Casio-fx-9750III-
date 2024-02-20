import numpy as np

def delta(x, y):
    return 1  # Uniform density function

deltaA = 0.01  # Approximate area of each small element
deltaX = 0.1   # Discretization step in the x direction
deltaY = 0.1   # Discretization step in the y direction, now defined

x_start, x_end = -np.pi / 2, np.pi / 2
elements = []

for x in np.arange(x_start, x_end + deltaX, deltaX):
    y_upper = np.cos(x)
    y_lower = -np.cos(x)
    # Assuming uniform distribution along y for each x
    y_steps = int((y_upper - y_lower) / deltaY) + 1
    for y_step in range(y_steps):
        y = y_lower + y_step * deltaY
        elements.append((x, y))

mass_elements = []
moment_x_elements = []
moment_y_elements = []

for x, y in elements:
    mass = delta(x, y) * deltaA
    mass_elements.append(mass)
    moment_x_elements.append(x * mass)
    moment_y_elements.append(y * mass)

M = sum(mass_elements)
x_bar = sum(moment_x_elements) / M
y_bar = sum(moment_y_elements) / M

print(f"Center of Mass: ({x_bar}, {y_bar}), Total Mass: {M}")
