import math


class Operations:
    def _int_(self):
        pass

    @staticmethod
    def addition(x, y):
        return int(x) + int(y)

    @staticmethod
    def subtraction(a, b):
        a = int(a)
        b = int(b)
        answer = b - a
        return answer

    @staticmethod
    def multiplication(a, b):
        return float(a) * float(b)

    @staticmethod
    def division(a, b):
        return float(b) / float(a)

    @staticmethod
    def square(a):
        x = float(a) * float(a)
        return x

    @staticmethod
    def root(a):
        x = float(a)
        return math.sqrt(x)
