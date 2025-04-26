number = 5

def factorial_iterative(number):
    if number < 0:
        print("No factorial for negative numbers")
        return None
    fact = 1
    for i in range(2, number + 1):
        fact *= i
    return fact

result = factorial_iterative(number)
print("Factorial of", number, "is", result)