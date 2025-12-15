#INTEGER
#Whole numbers without decimal point
a = 10
b = -5
c = 0
print(a)
print(b)
print(c)

#To check the data type
print(type(a)) #class 'int'
print(type(b)) #class 'int'
print(type(c)) #class 'int'

#ARITHMETIC OPERATIONS ON INTEGERS
a = 15
b = 4
print(a + b)  #Addition
print(a - b)  #Subtraction
print(a * b)  #Multiplication
print(a / b)  #Division (returns float)
print(a // b) #Floor Division (returns integer)
print(a % b)  #Modulus (remainder)
print(a ** b) #Exponentiation(Power)(10^3=1000)

#Comparison Operations
x = 10
y = 20
print(x == y)  #Equal to
print(x != y)  #Not equal to
print(x > y)   #Greater than
print(x < y)   #Less than
print(x >= y)  #Greater than or equal to
print(x <= y)  #Less than or equal to

#Type Conversion(Casting)
#float to int
f1 = 10.5
f2 = -3.7

print(int(f1)) #10
print(int(f2)) #-3

#string to int
s1 = "25"
s2 = "-7"
print(int(s1)) #25
print(int(s2)) #-7

#invalid string to int
s3 = "Hello"
# print(int(s3)) #ValueError: invalid literal for int() with base 10
a="10.5"
# print(int(a)) #ValueError: invalid literal for int() with base 10

#FLOAT
#Numbers with decimal point
x = 10.5
y = -3.14
z = 0.0
print(x)
print(y)
print(z)
print(type(x)) #class 'float'
print(type(y)) #class 'float'
print(type(z)) #class 'float'

#ARITHMETIC OPERATIONS ON FLOATS
a = 5.5
b = 2.0
print(a + b)  #Addition
print(a - b)  #Subtraction
print(a * b)  #Multiplication
print(a / b)  #Division
print(a // b) #Floor Division
print(a % b)  #Modulus
print(a ** b) #Exponentiation
#Always get float as result

#Mixed Operations
x = 10    #int
y = 3.5   #float
print(x + y)  #Addition
print(x - y)  #Subtraction
print(x * y)  #Multiplication
print(x / y)  #Division
#Output will be float

#Comparison Operations
p = 7.5
q = 10.0
print(p == q)  #Equal to
print(p != q)  #Not equal to
print(p > q)   #Greater than
print(p < q)   #Less than
print(p >= q)  #Greater than or equal to
print(p <= q)  #Less than or equal to

#Type Conversion(Casting)
#int to float
i1 = 10
i2 = -5
print(float(i1)) #10.0
print(float(i2)) #-5.0
#string to float
s1 = "12.34"
s2 = "-7.89"
print(float(s1)) #12.34
print(float(s2)) #-7.89
#invalid string to float
s3 = "World"
# print(float(s3)) #ValueError: could not convert string to float: 'World
s4 = "156abc"
# print(float(s4)) #ValueError: could not convert string to float: '15.6abc'

#built-in functions for floats
pi = 3.14159
print(round(pi))      #Rounds to nearest integer
print(round(pi, 2))   #Rounds to 2 decimal places

#precision issues
a = 0.1 + 0.2
print(a)              #0.30000000000000004
print(round(a, 2))  #0.3    