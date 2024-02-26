

import math

# Define the probability density function p(x) here.
def p(x):
    # Example PDF: p(x) = e^(-x^2) / sqrt(pi), a normalized Gaussian.
    return math.exp(-x**2) / math.sqrt(math.pi)

# Numerical approximation of the integral using the trapezoidal rule.
def approximate_integral(a, b, n, function):
    h = (b - a) / n
    total = 0.5 * function(a) + 0.5 * function(b)
    for i in range(1, n):
        x = a + i * h
        total += function(x)
    return h * total

# Check if p(x) >= 0 for a sampled range of x values.
def check_non_negativity(function, sample_points):
    for x in sample_points:
        if function(x) < 0:
            return False
    return True

# Main program
a = -5  # Start of the interval, approximation for -∞
b = 5   # End of the interval, approximation for ∞
n = 10000  # Number of subdivisions
sample_points = [a + i * (b - a) / 100 for i in range(101)]  # Sample 101 points between a and b

# Calculate the integral and check non-negativity
integral_value = approximate_integral(a, b, n, p)
is_non_negative = check_non_negativity(p, sample_points)

# Check if the PDF satisfies the conditions
if abs(integral_value - 1) < 0.01 and is_non_negative:  # Allowing a small error margin
    print("The PDF satisfies the conditions.")
else:
    print("The PDF does not satisfy the conditions.")
