class Calculator:
    def __init__(self):
        self.__num1 = 0
        self.__num2 = 0
    def set_numbers(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2
    def add(self):
        return self.__num1 + self.__num2
    def subtract(self):
        return self.__num1 - self.__num2
calculator = Calculator()
calculator.set_numbers(10, 5)
print("Addition:", calculator.add())  # Output: 15
print("Subtraction:", calculator.subtract())  # Output: 5
