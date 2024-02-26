import math

# Define the function f(x) here. Example: f(x) = x^2
def f(x):
    return x**2  # Replace this with the actual function

# Numerical integration using the trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f(a)**2 + f(b)**2)  # Start with the endpoints
    for i in range(1, n):
        x = a + i * h
        sum += f(x)**2  # Add the square of the function's value at x
    return math.pi * h * sum  # Multiply by π and the step size

# Integration limits and number of subintervals
a = 0  # Start of the interval (replace with actual value)
b = 2  # End of the interval (replace with actual value)
n = 1000  # Number of subintervals for the approximation

# Calculate and print the volume
volume = trapezoidal_rule(a, b, n)
print("Volume:", volume)
