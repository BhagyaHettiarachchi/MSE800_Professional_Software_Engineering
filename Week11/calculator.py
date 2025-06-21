import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def root(a, n):
    if a < 0 and n % 2 == 0:
        raise ValueError("Because square root of real number should be non negative")
    return a ** (1 / n)

def sine(x):
    return math.sin(math.radians(x))  # Assuming degrees

def cosine(x):
    return math.cos(math.radians(x))  # Assuming degrees

def tangent(x):
    rad = math.radians(x)
    if math.isclose(math.cos(rad), 0, abs_tol=1e-9):
        raise ValueError("Tangent undefined at this angle")
    return math.tan(rad)