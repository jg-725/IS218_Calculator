from operations.Addition import addition
from operations.Subtraction import subtraction
from operations.Division import division
from operations.Multiply import multiplication
from operations.Square import square
from operations.SquareRoot import root


class Calculator:
    result = 0

    def _init_(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def root(self, a):
        self.result = root(a)
        return self.result
