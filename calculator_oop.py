class Calculator:


    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result

    def subtract(self, num1, num2):
        self.result = num1 - num2
        return self.result

    def multiply(self, num1, num2):
        self.result = num1 * num2
        return self.result

    def divide(self, num1, num2):
        if num2 != 0:
            self.result = num1 / num2
            return self.result
        else:
            print("Error: Cannot divide by zero.")

    def modulo(self, num1, num2):
        self.result = num1 % num2
        return self.result



calculator = Calculator()

print(calculator.add(4, 4))
print(calculator.multiply(4, 4))
print(calculator.divide(9, 3))
print(calculator.modulo(12, 5))

