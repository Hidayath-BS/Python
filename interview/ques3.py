from math import sqrt


class Complex(object):

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        print(self.real + self.imag)

    def __add__(self, other):
        print('\nSum:')
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        print('\nDifference:')
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        print('\nProduct:')
        return Complex((self.real * other.real) - (self.imag * other.imag),
                       (self.imag * other.real) + (self.real * other.imag))

    def __truediv__(self, other):
        print('\nQuotient:')
        r = (other.real ** 2 + other.imag ** 2)
        return Complex((self.real * other.real - self.imag * other.imag) / r,
                       (self.imag * other.real + self.real * other.imag) / r)

    def __abs__(self):
        print('\nAbsolute Value:')
        new = (self.real ** 2 + (self.imag ** 2) * -1)
        return Complex(sqrt(new.real))


i = Complex(2, 10j)
k = Complex(3, 5j)


i + k

i - k

i * k

i / k

abs(i)
abs(k)


