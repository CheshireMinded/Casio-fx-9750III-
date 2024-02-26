import math

# Define the density function rho(x) and the function f(x) here
def rho(x):
    return 1  # Replace with the actual density function, if variable

def f(x):
    return x**2  # Example function, replace with the actual function

# Numerical integration using the trapezoidal rule
def trapezoidal_rule(a, b, n, function):
    h = (b - a) / n
    result = 0.5 * function(a) + 0.5 * function(b)
    for i in range(1, n):
        x = a + i * h
        result += function(x)
    result *= h
    return result

# Function to calculate My
def calculate_my(a, b, n):
    function_my = lambda x: x * f(x)  # x multiplied by f(x) for moment about y-axis
    return trapezoidal_rule(a, b, n, function_my)

# Function to calculate mass m
def calculate_m(a, b, n):
    function_m = lambda x: f(x)  # Just f(x) for mass
    return trapezoidal_rule(a, b, n, function_m)

# Example usage
a = 0  # Lower limit of integration
b = 2  # Upper limit of integration
n = 1000  # Number of subdivisions for the numerical approximation

# Calculate My and m
my = calculate_my(a, b, n)
m = calculate_m(a, b, n)

# Calculate x (centroid's x-coordinate)
x = my / m
print("x =", x)
