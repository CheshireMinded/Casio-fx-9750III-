# Manual square root function using the Newton-Raphson method
def sqrt(x):
    tolerance = 0.000001
    guess = x / 2.0
    while True:
        next_guess = (guess + x / guess) / 2
        if abs(guess - next_guess) < tolerance:
            break
        guess = next_guess
    return guess

# Function for the curve
def curve(x):
    return sqrt(4 - x**2)

# Derivative of the curve, simplified for manual calculation
def derivative(x):
    return -x / sqrt(4 - x**2)

# Numerical integration using the Trapezoidal rule, adapted for surface area calculation
def trapezoidal_rule_for_surface_area(a, b, n=1000):
    h = (b - a) / n
    sum = 0
    for i in range(n):
        x = a + i * h
        dx = derivative(x)
        circumference = 2 * 3.141592653589793 * curve(x) * sqrt(1 + dx**2)
        sum += circumference * h
    return sum

# Calculate the surface area
surface_area = trapezoidal_rule_for_surface_area(0, 2)

print("Surface Area:", surface_area)
