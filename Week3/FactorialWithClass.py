class FactorialProject:
    def __init__(self):
        self.number = 6

    def factorial_iterative(self):
        if self.number < 0:
            print("No factorial for negative numbers")
            return None
        fact = 1
        for i in range(2, self.number + 1):
            fact *= i
        return fact

#Create object
factobject = FactorialProject()
result = factobject.factorial_iterative()
print("Factorial of", factobject.number, "is", result)

