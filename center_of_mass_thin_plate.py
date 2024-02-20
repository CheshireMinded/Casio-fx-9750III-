def integrate(f, a, b, n):
    h = (b - a) / n
    total = sum(f(a + (i + 0.5) * h) for i in range(n))
    return total * h

def center_of_mass(delta, a, b, c, d, n):
    M = integrate(lambda x: integrate(lambda y: delta(x, y), c, d, n), a, b, n)
    x_bar = integrate(lambda x: integrate(lambda y: x * delta(x, y), c, d, n), a, b, n) / M
    y_bar = integrate(lambda x: integrate(lambda y: y * delta(x, y), c, d, n), a, b, n) / M
    return x_bar, y_bar, M

# Example usage
delta = lambda x, y: 1  # Uniform density
a, b, c, d = 0, 1, 0, 1  # Limits of the plate
n = 100  # Number of slices

x_bar, y_bar, M = center_of_mass(delta, a, b, c, d, n)
print(f"Center of Mass: ({x_bar}, {y_bar})")
print(f"Total Mass: {M}")