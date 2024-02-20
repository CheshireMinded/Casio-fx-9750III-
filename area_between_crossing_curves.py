import math

# Define the functions for your curves here
def f(x):
    # Example: y = x^2
    return x**2

def g(x):
    # Example: y = x + 2
    return x + 2

# Function to calculate the area between two curves
def area_between_curves(func1, func2, a, b, steps=1000):
    delta_x = (b - a) / steps
    area = 0
    for i in range(steps):
        x = a + i * delta_x
        area += abs(func1(x) - func2(x)) * delta_x
    return area

# Example usage
a = 0  # Start of the interval
b = 2  # End of the interval
area = area_between_curves(f, g, a, b)
print("Area between curves:", area)
