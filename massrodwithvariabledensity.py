
def density(x):
    # Define the density function rho(x) here.
    # Example: rho(x) = x^2 + 1
    return x**2 + 1

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    sum = 0.5 * (density(a) + density(b))
    for i in range(1, n):
        x = a + i * h
        sum += density(x)
    return h * sum

# Integration limits
a = 0  # Start of the interval (replace with actual value)
b = 2  # End of the interval (replace with actual value)
n = 1000  # Number of subdivisions for the approximation

# Calculate the mass
mass = trapezoidal_rule(a, b, n)
print("Mass:", mass)
