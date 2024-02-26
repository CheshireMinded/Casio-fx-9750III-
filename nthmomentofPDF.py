

import math

# Define the probability density function p(x)
def p(x):
    # Example: a normalized Gaussian distribution
    return math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)

# Numerical integration using the trapezoidal rule
def trapezoidal_rule(a, b, n, function):
    h = (b - a) / n
    total = 0.5 * function(a) + 0.5 * function(b)
    for i in range(1, n):
        x = a + i * h
        total += function(x)
    return h * total

# Function to compute the nth moment of p(x)
def nth_moment(n, a, b, num_points):
    moment_function = lambda x: (x**n) * p(x)
    return trapezoidal_rule(a, b, num_points, moment_function)

# Example usage
n = 2  # Calculate the second moment (variance for a standard Gaussian distribution)
a = -10  # Lower limit of integration (approximation for -∞)
b = 10   # Upper limit of integration (approximation for ∞)
num_points = 10000  # Number of points for numerical integration

moment = nth_moment(n, a, b, num_points)
print("The nth moment is:", moment)
