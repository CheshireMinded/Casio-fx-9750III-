

def trapezoidal_rule(a, b, n, function):
    h = (b - a) / n
    total = 0.5 * (function(a) + function(b))
    for i in range(1, n):
        x = a + i * h
        total += function(x)
    return total * h

def pdf(x):
    # Define your probability density function here
    # Example: a normal distribution with mean 0 and standard deviation 1
    import math
    return (1 / (math.sqrt(2 * math.pi))) * math.exp(-0.5 * x**2)

# Approximate infinity with large finite values
INF_POS = 1E99
INF_NEG = -1E99
n = 10000  # Increase n for higher accuracy

# Calculate the integral of the PDF from -infinity to +infinity
integral_result = trapezoidal_rule(INF_NEG, INF_POS, n, pdf)

print("Integral of p(x) from -inf to +inf:", integral_result)
