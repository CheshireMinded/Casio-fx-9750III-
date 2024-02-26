

import math

# Define the function f(x) here. For example, f(x) = sqrt(x).
def f(x):
    return math.sqrt(x)

# Function to perform numerical integration using the trapezoidal rule
def trapezoidal_rule(a, b, n, function):
    h = (b - a) / n
    result = 0.5 * function(a) * a + 0.5 * function(b) * b
    for i in range(1, n):
        x = a + i * h
        result += function(x) * x
    result *= h
    return result

# Function to calculate the volume of revolution
def volume_of_revolution(a, b, n, function):
    return 2 * math.pi * trapezoidal_rule(a, b, n, function)

# Example usage
a = 0  # Lower limit of integration
b = 2  # Upper limit of integration
n = 1000  # Number of subdivisions

# Calculate the volume
volume = volume_of_revolution(a, b, n, f)
print("Volume:", volume)
