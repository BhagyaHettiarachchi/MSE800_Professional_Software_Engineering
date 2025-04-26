class CheckPrime:
    def __init__(self, number):
        self.number = number

    def factorial(self):
        if self.number < 0:
            return "No Factorial for negative numbers."
        elif self.number == 0 or self.number == 1:
            return 1
        else:
            fact = 1
            for i in range(2, self.number + 1):
                fact *= i
            return fact

    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True

def main():
        user_input = int(input("Enter a number: "))
        num_ops = CheckPrime(user_input)

        print(f"\nFactorial of {user_input} is: {num_ops.factorial()}")

        if num_ops.is_prime():
            print(f"{user_input} is a Prime number.")
        else:
            print(f"{user_input} is NOT a Prime number.")

if __name__ == "__main__":
    main()
