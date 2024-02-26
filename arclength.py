import math

# Define the function
def f(x):
    return math.sqrt(4 - x**2)  # Example function

# Define the derivative of the function
def df(x):
    return -x / math.sqrt(4 - x**2)  # Derivative of the example function

# Numerical integration using the trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    total = 0.5 * (math.sqrt(1 + df(a)**2) + math.sqrt(1 + df(b)**2))
    for i in range(1, n):
        x = a + i * h
        total += math.sqrt(1 + df(x)**2)
    return h * total

# Calculate the arc length
a = 0  # Start of the interval
b = 2  # End of the interval
n = 1000  # Number of subintervals

arc_length = trapezoidal_rule(a, b, n)
print("Arc Length:", arc_length)
