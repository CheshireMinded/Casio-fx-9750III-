import math

# Define the function g(y)
def g(y):
    return math.sqrt(y)  # Example function, replace with your actual function

# Define the derivative of g(y)
def dg(y):
    return 1 / (2 * math.sqrt(y))  # Derivative of sqrt(y), adjust based on your function

# Function to compute the surface area of revolution
def surface_area(a, b, n):
    dx = (b - a) / n
    area = 0
    for i in range(n):
        y = a + i * dx
        area += g(y) * math.sqrt(1 + dg(y)**2) * dx
    return 2 * math.pi * area

# Example usage
a = 0  # Start of the interval, adjust as needed
b = 2  # End of the interval, adjust as needed
n = 10000  # Number of slices for numerical integration, increase for more accuracy

print(surface_area(a, b, n))
