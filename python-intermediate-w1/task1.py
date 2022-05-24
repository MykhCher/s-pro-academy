class OperationsMixin:
    @staticmethod
    def add(f1, f2):
        if f1.den == f2.den:
            a = f1.num + f2.num
            b = f1.den
        else:
            a = f1.num * f2.den + f2.num * f1.den
            b = f1.den * f2.den
        return f1.__class__(a, b)

    @staticmethod
    def sub(f1, f2):
        if f1.den == f2.den:
            a = f1.num - f2.num
            b = f1.den
        else:
            a = f1.num * f2.den - f2.num * f1.den
            b = f1.den * f2.den
        return f1.__class__(a, b)

    @staticmethod
    def mul(f1, f2):
        a = f1.num * f2.num
        b = f1.den * f2.den
        return f1.__class__(a, b)

    @staticmethod
    def div(f1, f2):
        a = f1.num / f2.num
        b = f1.den / f2.den
        return f1.__class__(a, b)

class Fraction(OperationsMixin):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __sub__(self, f2):
        if self.den == f2.den:
            a = self.num - f2.num
            b = self.den
        else:
            a = self.num * f2.den - f2.num * self.den
            b = self.den * f2.den
        return self.__class__(a, b)

    def __add__(self, f2):
        if self.den == f2.den:
            a = self.num + f2.num
            b = self.den
        else:
            a = self.num * f2.den + f2.num * self.den
            b = self.den * f2.den
        return self.__class__(a, b)

    def __mul__(self, f2):
        a = self.num * f2.num
        b = self.den * f2.den
        return self.__class__(a, b)

    def __truediv__(self, f2):
        a = self.num / f2.num
        b = self.den / f2.den
        return self.__class__(a, b)

    @classmethod
    def from_str(cls, str_value):
        values = [float(i) for i in str_value.split("/")]
        assert len(values) == 2
        return cls(*values)

    def __str__(self):
        return f"{self.num}/{self.den}"

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        assert isinstance(num, (float, int)), "Numerator should be a number"
        self.__num = num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        assert isinstance(den, (float, int)) and den != 0, "Denominator should be a non-zero number"
        self.__den = den

a = Fraction(4, 5)
b = Fraction.from_str("3/4")
print(a)
print(b)
print(Fraction.add(a, b), "- Testing add method")
print(Fraction.sub(a, b), "- Testing sub method")
print(Fraction.mul(a, b), "- Testing mul method")
print(Fraction.div(a, b), "- Testing div method")
print(a + b, "- Testing __add__")
print(a - b, "- Testing __sub__")
print(a * b, "- Testing __mul__")
print(a / b, "- Testing __truediv__")
