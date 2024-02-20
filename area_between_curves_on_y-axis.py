import math


# Define the functions for your curves as x = f(y) and x = g(y)
def f(y):
    # Example: x = sqrt(y)
    return math.sqrt(y)

def g(y):
    # Example: x = y / 2
    return y / 2

# Function to calculate the area between two curves, integrating along y-axis
def area_between_curves_y_axis(func1, func2, c, d, steps=1000):
    delta_y = (d - c) / steps
    area = 0
    for i in range(steps):
        y = c + i * delta_y
        area += abs(func1(y) - func2(y)) * delta_y
    return area

# Example usage
c = 0  # Start of the interval on the y-axis
d = 4  # End of the interval on the y-axis
area = area_between_curves_y_axis(f, g, c, d)
print("Area between curves (integrated along y-axis):", area)