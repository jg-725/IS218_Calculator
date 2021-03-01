from OperationsFile.Operations import Operations


class Calculator:
    result = 0

    def _init_(self):
        pass

    def add(self, a, b):
        self.result = Operations.addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Operations.subtraction(a, b)
        return self.result

    def division(self, a, b):
        self.result = Operations.division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Operations.multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = Operations.square(a)
        return self.result

    def root(self, a):
        self.result = Operations.root(a)
        return self.result
