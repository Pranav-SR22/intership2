"""
RULES (Must Follow – Otherwise Error):

Can contain letters (a–z, A–Z), digits (0–9), underscore (_).
Must start with a letter or underscore.
Cannot start with a digit or number.
Cannot contain spaces or special characters (@, #, $, %, etc.).
Cannot use Python keywords (reserved words).

Valid Examples:

name, age, first_name, _value, student1, total_marks

Invalid Examples:

2name → Starts with number
first-name → Contains hyphen
first name → Contains space
@username → Contains special character
for → Python keyword

Case Sensitivity:

Python treats these as different variables: name, Name, NAME, nAme
Be consistent with capitalization.

Python Keywords (Cannot use as variable names):

and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield

Best Practices (Conventions):

Use descriptive names: age is good, a is bad.
Use lowercase: name is good, NAME is not recommended.
Use underscore for multiple words: first_name is good, firstname is okay.
Avoid single letters except for i, j, k in loops.

Naming convention: snake_case
Examples: student_name, total_marks, user_age

Examples of Good vs Bad Names:

Good Names: student_age, total_price, first_name, is_valid, user_count
Bad Names: sa, tp, x, v, count1

Example valid variable names:

name = "Pratik"
name = "John"
age = 25
first_name = "John"
last_name = "Doe"
age2 = 30
_private = "secret"
student_roll_number = 101

Invalid variable names (these will give errors):

2age = 25
first-name = "John"
first name = "John"
for = 5
@name = "John"
"""
#Storing string in variable

name = "Pranav"
print(name)

#storing number in variable

num = 25
print(num)

#case sesititvity

name="p"
Name="q"
NAME="r"

print(name) #p
print(Name) #q
print(NAME) #r

#Assign same value to diff variables

a = 2
b = 2
c = 2

a = b = c

print(a)
print(b)
print(c)

#Assign multiple values to multiple variables

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

#Assign different data type value to maultiple variables
name, age, email = "Pranav", 22, "xyz@gmail.com"
print(name)
print(age)
print(email)

#swapping

a = "Pranav"
b = "Havok"
print(a)
print(b)

print("After swappimg......")
#method1
temp = a
a = b
b = temp

print("temp---->", temp)
print("a---->",a)
print("b---->",b)

#method2 (python way of swapping)
a,b = b,a
print(a)
print(b)

