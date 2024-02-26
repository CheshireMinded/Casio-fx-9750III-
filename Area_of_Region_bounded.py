#Find the area of the region bounded by the curves y = 12 − x, y =√x,and y = 1.

def y1(x):
    return 12 - x

def y2(x):
    return x**0.5  # sqrt(x)

# Since direct symbolic integration and solving are not possible,
# we implement numerical methods for finding intersection points
# and calculating the area.

# Approximating intersection points (conceptual example, adjust as needed)
def find_intersection(f1, f2, start, end, step=0.01):
    x = start
    while x <= end:
        if abs(f1(x) - f2(x)) < step:  # Adjust 'step' for accuracy vs. performance
            return x
        x += step
    return None  # No intersection found within the given range

# Numerical integration using the Trapezoidal rule
def trapezoidal_rule(f, a, b, n=1000):
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        sum += f(a + i * h)
    return sum * h

# Find intersection points
x_intersect_1_2 = find_intersection(y1, y2, 0, 12)  # Adjust search range as needed
x_intersect_2_3 = 1  # Given by the problem since y = sqrt(x) intersects y = 1 at x = 1

# Calculate area
area = trapezoidal_rule(y2, 0, x_intersect_1_2) - trapezoidal_rule(lambda x: 1, 0, x_intersect_1_2)

print("Area:", area)
