
import math

# Define the density function ρ(x) here
def rho(x):
    # Example: Constant density
    return 1  # Replace with the actual density function

# Define the function f(x) here
def f(x):
    # Example: Circular section with radius R
    return math.sqrt(R**2 - x**2)  # Replace R with the actual radius value

# Numerical integration using the trapezoidal rule
def trapezoidal_rule(a, b, n, integrand):
    h = (b - a) / n
    result = 0.5 * integrand(a) + 0.5 * integrand(b)
    for i in range(1, n):
        x = a + i * h
        result += integrand(x)
    result *= h
    return result

# Integrand function for moment of inertia calculation
def integrand(x):
    return rho(x) * f(x)**2

# Main program to calculate Mx
def calculate_Mx(a, b, n):
    # Calculate the moment of inertia using numerical integration
    Mx = trapezoidal_rule(a, b, n, integrand)
    return Mx

# Example usage
a = -R  # Start of the interval, for a circle centered at the origin
b = R   # End of the interval
n = 1000  # Number of subdivisions for the numerical approximation
R = 1    # Example radius of the circle

# Calculate Mx
Mx = calculate_Mx(a, b, n)
print("Moment of Inertia Mx:", Mx)
