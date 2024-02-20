def find_centroid(x1, y1, x2, y2, x3, y3):
    x_bar = (x1 + x2 + x3) / 3
    y_bar = (y1 + y2 + y3) / 3
    return x_bar, y_bar

# Example usage with a triangle's vertices
x1, y1 = 0, 0  # Vertex A
x2, y2 = 6, 0  # Vertex B
x3, y3 = 0, 10  # Vertex C

centroid = find_centroid(x1, y1, x2, y2, x3, y3)
print(f"Centroid of the triangle: {centroid}")