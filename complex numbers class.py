import math
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_real(self):
        return self.a
    def get_imaginary(self):
        return self.b
    def __abs__(self):
        return math.sqrt(self.a**2 + self.b**2)
    def polar_angle(self):
        return math.atan(self.b/self.a)
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)
    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.a*other.b+self.b*other.a)
    def __str__(self):
        return f'{self.a}i + {self.b}'

c1 = Complex(3, 4)
c2 = Complex(6, 9)

print(c1+c2) 
print(c2*c1) 
print(c1-c2)
print(f'Absolute value of {c1}:' ,abs(c1)) 
print(f'Polar angle of {c1}:', c1.polar_angle())

