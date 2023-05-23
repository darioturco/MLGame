INFINITY = float('inf')
NEG_INFINITY = float('-inf')
EPSILON = 1e-6

def is_empty(list):
    return len(list) == 0

def are_equal(num1, num2):
    return abs(num1 - num2) < EPSILON
