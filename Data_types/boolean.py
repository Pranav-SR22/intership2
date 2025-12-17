#Boolean (bool) Data Type
#Boolean represents one of two values: True or False 
#Note: In Python, boolean values are case-sensitive and must be written with an uppercase 'T' for True and an uppercase 'F' for False.

#in instagram 
is_active = True
is_logged_in = False

print(is_active)      #True
print(is_logged_in)   #False

print(type(is_active))    #<class 'bool'>
print(type(is_logged_in)) #<class 'bool'>


#comparison operators return boolean values
x = 15
y = 20
print(x == y)  #False
print(x != y)  #True
print(x > y)   #False
print(x < y)   #True
print(x >= y)  #False
print(x <= y)  #True

#Boolean values in logical operations

#AND operation
#if both operands are True, result is True; otherwise, False
print(True and True)   #True
print(True and False)  #False
print(False and False) #False
print(False and True)  #False   

#OR operation
#if at least one operand is True, result is True; otherwise, False
print(True or True)    #True
print(True or False)   #True
print(False or False)  #False
print(False or True)   #True

#NOT operation
#inverts the boolean value
print(not True)   #False
print(not False)  #True

#Boolean values in conditional statements
age = 18
if age >= 18:
    print("You are eligible to vote.")  #This will be printed
else:
    print("You are not eligible to vote.")


#values considered True in Python, all the number excluding 0 is truthy values, string is truthy values, space is truthy values

print(bool(10))         #True
print(bool(-5))         #True
print(bool(3.14))       #True 
print(bool("Hello"))    #True 
print(bool(" "))        #True #string with space
print(bool([1, 2, 3]))  #True list with elements
print(bool((1, 2)))     #True tuple with elements
print(bool({'a': 1}))   #True dictionary with elements
print(bool(True))       #True
print(bool(set([1,2]))) #True set with elements



#values considered False in Python

print(bool(0))          #False
print(bool(0.0))        #False
print(bool(""))         #False empty string
print(bool([]))         #False empty list
print(bool(()))         #False empty tuple
print(bool({}))         #False empty dictionary
print(bool(None))       #False nothing
print(bool(False))      #False
print(bool(set()))      #False #empty set


#Type Conversion to Boolean
#Various data types can be converted to boolean using the bool() function
b1 = bool(25)        #True
print(b1)
b2 = bool(0)         #False
print(b2)
b3 = bool("Python")  #True
print(b3)
b4 = bool([])        #False
print(b4)
b5 = bool(None)      #False
print(b5)


#boolean string method
text = "True"
print(text.isalpha())  #True
print(text.isdigit())  #False
print(text.islower())  #False
print(text.isupper())  #False
print(text.isspace())  #False
print(text.isalnum())  #True
print(text.startswith("T"))  #True
print(text.endswith("e"))    #True


#real life example
is_raining = True
has_umbrella = False

if is_raining and has_umbrella:
    print("You can go outside.")
else:
    print("Better to stay indoors.")

is_logged_in = True

if is_logged_in:
    print("Welcome back, user!")
else:
    print("Please log in to continue.")  


#combining boolean expressions



 
