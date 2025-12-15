
"""COMPLEX NUMBERS (complex) IN PYTHON

Complex number: a + bj
a → real part (int or float)
b → imaginary part (int or float)
j → imaginary unit (√-1)

Creating complex numbers

z1 = 2 + 3j real = 2, imaginary = 3
z2 = -1 - 4j
z3 = 5.0 + 0j real part float
z4 = 0 + 2j only imaginary

print(z1, z2, z3, z4)

Check data type
print(type(z1)) <class 'complex'>

Accessing real and imaginary parts
print(z1.real) 2.0
print(z1.imag) 3.0

print(z2.real) -1.0
print(z2.imag) -4.0

BASIC OPERATIONS WITH COMPLEX NUMBERS

a = 2 + 3j
b = 1 - 4j

Addition
print(a + b) (3-1j)

Subtraction
print(a - b) (1+7j)

Multiplication
print(a * b) (14-5j)

Division
print(a / b) (-0.5882352941176471 + 0.6470588235294118j) approx

Conjugate of a complex number
For z = a + bj, conjugate is a - bj
z = 3 + 4j
print(z.conjugate()) (3-4j)

Mixing with int and float

x = 5 int
y = 2.5 float
z = 3 + 4j complex

print(x + z) (8+4j)
print(y + z) (5.5+4j)

Note: if you mix int/float with complex, result becomes complex

Using complex numbers in simple examples

Example 1: Electrical engineering (impedance)

r = 4 resistance (real part)
x_react = 3 reactance (imaginary part)
impedance = complex(r, x_react) 4 + 3j
print("Impedance:", impedance)

Example 2: Distance from origin in complex plane

point = 3 + 4j
distance = abs(point) same as sqrt(3^2 + 4^2)
print("Distance from origin:", distance) 5.0
"""