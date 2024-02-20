import math

def f(x):
    # Define the first curve here
    # Example: return x**2
    return x**2

def g(x):
    # Define the second curve here
    # Example: return x
    return x

def integrate(f, a, b, n):
    # Trapezoidal rule for integration
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return h * s

def area_between_curves(f, g, a, b, n):
    # Calculate the area between two curves
    # by integrating the difference between them
    def h(x):
        return abs(f(x) - g(x))
    return integrate(h, a, b, n)

# Example usage:
a = 0  # Start of the interval
b = 1  # End of the interval
n = 1000  # Number of subintervals
area = area_between_curves(f, g, a, b, n)
print("Area between curves:", area)
