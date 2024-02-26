import math

# Define the functions f(y) and g(y) here
def f(y):
    return y**2  # Example: f(y) = y^2

def g(y):
    return y  # Example: g(y) = y

# Numerical integration using the trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    sum = 0.5 * ((f(a)**2 - g(a)**2) + (f(b)**2 - g(b)**2))
    for i in range(1, n):
        y = a + i * h
        sum += (f(y)**2 - g(y)**2)
    return math.pi * h * sum

# Integration limits and number of subintervals
a = 0  # Start of the interval (replace with actual value)
b = 2  # End of the interval (replace with actual value)
n = 1000  # Number of subintervals for the approximation

# Calculate and print the volume
volume = trapezoidal_rule(a, b, n)
print("Volume:", volume)
