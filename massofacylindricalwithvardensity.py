

import math

# Define the density function rho(r) here. Example: rho(r) = r + 1
def rho(r):
    return r + 1  # Replace with the actual density function

# Numerical integration using the trapezoidal rule
def trapezoidal_rule(a, b, n, function):
    h = (b - a) / n
    result = 0.5 * function(a) * a + 0.5 * function(b) * b
    for i in range(1, n):
        r = a + i * h
        result += function(r) * r
    result *= h
    return result

# Function to calculate the mass
def calculate_mass(R, n, density_function):
    return 2 * math.pi * trapezoidal_rule(0, R, n, density_function)

# Example usage
R = 2  # Outer radius of the cylinder
n = 1000  # Number of subdivisions for the numerical approximation

# Calculate the mass
mass = calculate_mass(R, n, rho)
print("Mass:", mass)
