class Factorial:
    
    #Assign number
    def set_number(self, num1):
        self.num1 = num1

    def factorial(self):
        result = 1
        for i in range(1, self.num1 + 1):
            result *= i
        return result

    def check_Prime(self):
        if self.num1 < 2:
            return False
        for i in range(2, int(self.num1 ** 0.5) + 1):
            if self.num1 % i == 0:
                return False
        return True

    def display(self):
        print("Factorial of", self.num1, "is", self.factorial())
        if self.check_Prime():
            print(f"{self.num1} is a prime number.")
        else:
            print(f"{self.num1} is not a prime number.")

# Create object and give number
number1 = Factorial()
number1.set_number(7)

# display method
number1.display()
