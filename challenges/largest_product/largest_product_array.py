def largest_product(arr):
    """
    Returns the largest_product inside an array incased inside a matrix.
    input <--- Array of array with 2 value inside each
    output <--- Largest Product of pair inside Matrix
    """
    largest_product = 0
    for container in arr:
        x, y = container
        if x * y > largest_product:
            largest_product = x * y
    return largest_product
