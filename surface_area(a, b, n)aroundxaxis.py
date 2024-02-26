import math

def surface_area(a, b, n):
    def f(x):
        return math.sqrt(4 - x**2)
    
    def df(x):
        return -x / math.sqrt(4 - x**2)
    
    dx = (b - a) / n
    area = 0
    for i in range(n):
        x = a + i * dx
        y = f(x)
        dydx = df(x)
        integrand = y * math.sqrt(1 + dydx**2)
        area += integrand * dx
    return 2 * math.pi * area

# Calculate the surface area
a = 0
b = 2
n = 1000 # Number of intervals
print(surface_area(a, b, n))
