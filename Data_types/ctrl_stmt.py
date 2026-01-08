#if and else example
num = 10
if num > 0:
    print("Positive number")
else:
    print("Non-positive number")

#if, elif and else example
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


#for loop

#for loop iterate over a sequence (like list, string, range)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) #apple banana cherry
#for loop with range
for i in range(5): #0 to 4
    print(i) #0 1 2 3 4

fruits = ["apple", "banana", "cherry"]
for index in range(len(fruits)):
    print("Fruit at index", index, "is", fruits[index]) #Fruit at index 0 is apple

#using range with start and end
for i in range(2, 7): #2 to 6
    print(i) #2 3 4 5 6
#using range with step
for i in range(1, 10, 2): #1 to 9 with step 2
    print(i) #1 3 5 7 9     

#for loop with enumerate
#enumerate gives both index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print("Color at index", index, "is", color) #Color at index 0 is red
for 2, fruit in enumerate(colors):
    print("Fruit at index", 2, "is", fruit) #Fruit at index 2 is blue   

#enumerate with custom start index
for index, color in enumerate(colors, start=1):
    print("Color at index", index, "is", color) #Color at index 1 is red

#while loop
#it executes as long as condition is true
#must update the condition variable inside loop to avoid infinite loop
#condtion checked before each iteration

count = 1
print("Counting:")

while count <= 5:
    print(count)
    count += 1  #increment count by 1   
print("Done!")

attempts = 3
while attempts > 0:
    print("You have", attempts, "attempts left.")
    attempts -= 1
print("No attempts left. Access denied.")

#==================================================================================
# CONTROL FLOW IN PYTHON
#==================================================================================
"""
NOTES:
- Control flow determines the order in which code executes
- Includes conditional statements (if, elif, else)
- Includes loops (for, while)
- Includes control statements (break, continue, pass)
"""

#==================================================================================
# IF STATEMENT
#==================================================================================
"""
NOTES:
- if statement executes code only if condition is True
- Condition must evaluate to True or False
- Indentation is mandatory in Python (usually 4 spaces)
"""

# Basic if statement
age = 18
print("Age:", age)

if age >= 18:
    print("You are an adult")

print("This line always executes\n")

# Another example
temperature = 30
print("Temperature:", temperature)

if temperature > 25:
    print("It's hot outside!")

# if with False condition
score = 45
print("\nScore:", score)

if score >= 50:
    print("You passed!")  # This won't execute

print("End of program")

#==================================================================================
# IF-ELSE STATEMENT
#==================================================================================
"""
NOTES:
- else executes when if condition is False
- Only one block executes (either if or else)
- else doesn't have a condition
"""

# Basic if-else
age = 15
print("\nAge:", age)

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Another example
number = 7
print("\nNumber:", number)

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Password check
password = "secret123"
user_input = "secret123"

print("\nPassword check:")
if user_input == password:
    print("Access granted!")
else:
    print("Access denied!")

#==================================================================================
# IF-ELIF-ELSE STATEMENT
#==================================================================================
"""
NOTES:
- elif means "else if"
- Checks multiple conditions in order
- Only first True condition executes
- else is optional
"""

# Basic if-elif-else
marks = 85
print("\nMarks:", marks)

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Multiple elif
age = 25
print("\nAge:", age)

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Without else
temperature = 15
print("\nTemperature:", temperature)

if temperature > 30:
    print("Very hot")
elif temperature > 20:
    print("Warm")
elif temperature > 10:
    print("Cool")
# No else - nothing happens if all conditions are False

#==================================================================================
# NESTED IF STATEMENTS
#==================================================================================
"""
NOTES:
- if statements inside other if statements
- Check multiple conditions at different levels
- Be careful with indentation
"""

# Basic nested if
age = 20
has_license = True

print("\nAge:", age)
print("Has license:", has_license)

if age >= 18:
    print("You are an adult")
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")
else:
    print("You are too young to drive")

# Another example
number = 12
print("\nNumber:", number)

if number > 0:
    print("Positive number")
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Not a positive number")

# Multiple nested levels
score = 85
attendance = 90

print("\nScore:", score)
print("Attendance:", attendance)

if score >= 50:
    print("You passed!")
    if attendance >= 75:
        print("Good attendance")
        if score >= 85:
            print("Excellent performance!")
    else:
        print("Poor attendance")
else:
    print("You failed")

#==================================================================================
# COMPARISON OPERATORS
#==================================================================================
"""
NOTES:
- == (equal to)
- != (not equal to)
- > (greater than)
- < (less than)
- >= (greater than or equal to)
- <= (less than or equal to)
"""

a = 10
b = 20

print("\na =", a)
print("b =", b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Using in conditions
x = 15
print("\nx =", x)

if x == 15:
    print("x is equal to 15")

if x != 10:
    print("x is not equal to 10")

if x > 10:
    print("x is greater than 10")

if x <= 20:
    print("x is less than or equal to 20")

#==================================================================================
# LOGICAL OPERATORS
#==================================================================================
"""
NOTES:
- and - True if both conditions are True
- or - True if at least one condition is True
- not - Reverses the condition
"""

# and operator
age = 25
income = 30000

print("\nAge:", age)
print("Income:", income)

if age >= 18 and income >= 25000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# or operator
day = "Sunday"
print("\nDay:", day)

if day == "Saturday" or day == "Sunday":
    print("It's weekend!")
else:
    print("It's a weekday")

# not operator
is_raining = False
print("\nIs raining:", is_raining)

if not is_raining:
    print("You don't need an umbrella")
else:
    print("Take an umbrella")

# Combining multiple operators
score = 75
attendance = 80

print("\nScore:", score)
print("Attendance:", attendance)

if score >= 50 and attendance >= 75:
    print("Pass with good attendance")
elif score >= 50 and attendance < 75:
    print("Pass but poor attendance")
else:
    print("Fail")

# Multiple conditions
age = 22
has_ticket = True
has_id = True

print("\nAge:", age)
print("Has ticket:", has_ticket)
print("Has ID:", has_id)

if age >= 18 and has_ticket and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

#==================================================================================
# MEMBERSHIP OPERATORS
#==================================================================================
"""
NOTES:
- in - checks if value exists in sequence
- not in - checks if value doesn't exist in sequence
"""

# in operator
fruits = ["apple", "banana", "cherry"]
print("\nFruits list:", fruits)

if "banana" in fruits:
    print("Banana is in the list")

if "grape" in fruits:
    print("Grape is in the list")
else:
    print("Grape is not in the list")

# not in operator
colors = ["red", "green", "blue"]
print("\nColors list:", colors)

if "yellow" not in colors:
    print("Yellow is not in the list")

# With strings
text = "Hello World"
print("\nText:", text)

if "World" in text:
    print("Found 'World' in text")

if "Python" not in text:
    print("'Python' not found in text")

#==================================================================================
# FOR LOOP
#==================================================================================
"""
NOTES:
- for loop iterates over a sequence
- Sequence can be list, tuple, string, range, etc.
"""

# Basic for loop with list
fruits = ["apple", "banana", "cherry"]
print("\nIterating through fruits:")

for fruit in fruits:
    print(fruit)

# for loop with numbers
print("\nNumbers 1 to 5:")
for i in [1, 2, 3, 4, 5]:
    print(i)

# for loop with string
text = "Python"
print("\nCharacters in 'Python':")

for char in text:
    print(char)

# for loop with range()
print("\nUsing range(5):")
for i in range(5):
    print(i)

print("\nUsing range(1, 6):")
for i in range(1, 6):
    print(i)

print("\nUsing range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i)

# for loop with calculations
print("\nMultiplication table of 5:")
for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")

#==================================================================================
# FOR LOOP WITH ENUMERATE
#==================================================================================
"""
NOTES:
- enumerate() provides index and value
- Useful when you need both index and element
"""

# Basic enumerate
fruits = ["apple", "banana", "cherry"]
print("\nUsing enumerate:")

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# enumerate with start parameter
print("\nUsing enumerate with start=1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

#==================================================================================
# WHILE LOOP
#==================================================================================
"""
NOTES:
- while loop executes as long as condition is True
- Must update condition variable to avoid infinite loop
- Condition checked before each iteration
"""

# Basic while loop
count = 1
print("\nCounting 1 to 5:")

while count < 0:
    print(count)
    count += 1

print("Loop finished\n")

# Another example
number = 10
print("Countdown from 10:")

while number > 0:
    print(number)
    number -= 1

print("Blast off!")

# while loop with user input simulation
attempts = 0
print("\nPassword attempts remaining:", attempts)

while attempts <= 3:
    print(f"Attempt {attempts}")
    attempts += 1
    if attempts == 3:
        print("No more attempts left")

# Sum using while loop
total = 0
i = 1

while i <= 10:
    total += i
    i += 1
    
# totall = 0
# for i in range(1, 11):
#     totall += i
    
print(f"\nSum of 1 to 10: {total}")
# print(f"Sum of 1 to 10: {totall}")
    
#==================================================================================
# BREAK STATEMENT
#==================================================================================
"""
NOTES:
- break exits the loop immediately
- Skips remaining iterations
- Used to stop loop based on condition
"""

# break in for loop
print("\nSearching for 'cherry':")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(f"Checking: {fruit}")
    if fruit == "cherry":
        print("Found cherry! Stopping search.")
        break

# break in while loop
print("\nFinding first number divisible by 7:")
number = 1

while number <= 100:
    if number % 7 == 0:
        print(f"First number divisible by 7: {number}")
        break
    number += 1

# break with user input simulation
print("\nPassword check (max 3 attempts):")
password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = "secret123"  # Simulating correct password on first try
    attempts += 1
    
    if user_input == password:
        print("Login successful!")
        break
    else:
        print(f"Wrong password. {max_attempts - attempts} attempts remaining")

#==================================================================================
# CONTINUE STATEMENT
#==================================================================================
"""
NOTES:
- continue skips current iteration
- Moves to next iteration immediately
- Remaining code in loop is skipped for that iteration
"""

# continue in for loop
print("\nPrinting odd numbers (1-10):")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Another example
print("\nSkipping 'banana':")
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# continue in while loop
print("\nPrinting numbers except multiples of 3:")
number = 0

while number < 10:
    number += 1
    if number % 3 == 0:
        continue
    print(number)

# Practical example
print("\nProcessing positive numbers only:")
numbers = [5, -3, 8, -1, 10, -7, 15]

for num in numbers:
    if num < 0:
        continue
    print(f"Processing: {num}")

#==================================================================================
# PASS STATEMENT
#==================================================================================
"""
NOTES:
- pass does nothing
- Used as placeholder
- Useful when syntax requires code but you don't want to write it yet
"""

# pass in if statement
age = 20

if age >= 18:
    pass  # Will implement later
else:
    print("Minor")

print("\npass statement used as placeholder")

# pass in for loop
print("\nUsing pass in loop:")
for i in range(5):
    if i == 2:
        pass  # Do nothing for now
    else:
        print(i)

# Multiple passes
print("\nPlaceholder structure:")
x = 10

if x > 5:
    pass  # TODO: Add logic here
elif x > 0:
    pass  # TODO: Add logic here
else:
    pass  # TODO: Add logic here

print("Program continues after pass")

#==================================================================================
# NESTED LOOPS
#==================================================================================
"""
NOTES:
- Loops inside other loops
- Inner loop completes fully for each iteration of outer loop
"""

# Basic nested for loop
print("\nMultiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()  # Blank line after each table

# Pattern printing
print("Pattern with nested loops:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Nested loop with list
print("\nCombining names and colors:")
names = ["Alice", "Bob"]
colors = ["Red", "Blue"]

for name in names:
    for color in colors:
        print(f"{name} likes {color}")

# break in nested loop
print("\nbreak in nested loop:")
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"i={i}, j={j}")

#==================================================================================
# LOOP WITH ELSE CLAUSE
#==================================================================================
"""
NOTES:
- else clause executes when loop completes normally
- Doesn't execute if loop is terminated by break
- Unique Python feature
"""

# for-else
print("\nSearching for number 7:")
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 7:
        print("Found 7!")
        break
else:
    print("7 not found in list")

# while-else
print("\nChecking if 15 is prime:")
number = 15
is_prime = True
i = 2

while i < number:
    if number % i == 0:
        is_prime = False
        break
    i += 1
else:
    if is_prime and number > 1:
        print(f"{number} is prime")

if not is_prime:
    print(f"{number} is not prime")

#==================================================================================
# REAL-LIFE CONTROL FLOW EXAMPLES
#==================================================================================

# Example 1: Grade Calculator
print("\n--- EXAMPLE 1: GRADE CALCULATOR ---")
marks = [85, 90, 78, 92, 88]
total = sum(marks)
average = total / len(marks)

print(f"Marks: {marks}")
print(f"Average: {average:.2f}")

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")

# Example 2: Shopping Discount
print("\n--- EXAMPLE 2: SHOPPING DISCOUNT ---")
total_amount = 1500
is_member = True

print(f"Total amount: ${total_amount}")
print(f"Is member: {is_member}")

discount = 0
if is_member:
    if total_amount >= 1000:
        discount = 20
    elif total_amount >= 500:
        discount = 10
    else:
        discount = 5
else:
    if total_amount >= 1000:
        discount = 10

final_amount = total_amount - (total_amount * discount / 100)
print(f"Discount: {discount}%")
print(f"Final amount: ${final_amount:.2f}")

# Example 3: Temperature Monitor
print("\n--- EXAMPLE 3: TEMPERATURE MONITOR ---")
temperatures = [72, 75, 80, 85, 90, 88, 92]

print("Daily temperatures:", temperatures)
print("\nTemperature alerts:")

for day, temp in enumerate(temperatures, 1):
    print(f"Day {day}: {temp}°F", end=" - ")
    if temp >= 90:
        print("Very Hot! Stay hydrated")
    elif temp >= 80:
        print("Hot")
    elif temp >= 70:
        print("Warm")
    else:
        print("Cool")

# Example 4: ATM Withdrawal
print("\n--- EXAMPLE 4: ATM WITHDRAWAL ---")
balance = 1000
withdrawal_amount = 300
pin = "1234"
entered_pin = "1234"

print(f"Current balance: ${balance}")
print(f"Withdrawal amount: ${withdrawal_amount}")

if entered_pin != pin:
    print("Incorrect PIN")
elif withdrawal_amount > balance:
    print("Insufficient balance")
elif withdrawal_amount <= 0:
    print("Invalid amount")
else:
    balance -= withdrawal_amount
    print("Withdrawal successful")
    print(f"Remaining balance: ${balance}")

# Example 5: Login System
print("\n--- EXAMPLE 5: LOGIN SYSTEM ---")
max_attempts = 3
attempts = 0
correct_password = "secure123"

print(f"Maximum attempts: {max_attempts}")

while attempts < max_attempts:
    attempts += 1
    # Simulating wrong password first 2 times, correct on 3rd
    if attempts < 3:
        entered_password = "wrong"
    else:
        entered_password = "secure123"
    
    print(f"Attempt {attempts}: ", end="")
    
    if entered_password == correct_password:
        print("Login successful!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining")
        else:
            print("Account locked")

# Example 6: Number Guessing Game
print("\n--- EXAMPLE 6: NUMBER GUESSING GAME ---")
secret_number = 7
guesses = [5, 8, 7]

print(f"Secret number: {secret_number}")
print(f"Guesses: {guesses}")

for attempt, guess in enumerate(guesses, 1):
    print(f"\nAttempt {attempt}: Guessed {guess}")
    
    if guess == secret_number:
        print("Correct! You won!")
        break
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")

# Example 7: Attendance System
print("\n--- EXAMPLE 7: ATTENDANCE SYSTEM ---")
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
present = ["Alice", "Charlie", "David"]

print("All students:", students)
print("Present students:", present)
print("\nAttendance:")

present_count = 0
for student in students:
    if student in present:
        print(f"{student}: Present ✓")
        present_count += 1
    else:
        print(f"{student}: Absent ✗")

attendance_percentage = (present_count / len(students)) * 100
print(f"\nAttendance: {present_count}/{len(students)} ({attendance_percentage:.1f}%)")

# Example 8: Prime Number Checker
print("\n--- EXAMPLE 8: PRIME NUMBER CHECKER ---")
number = 17
print(f"Checking if {number} is prime...")

if number < 2:
    print(f"{number} is not prime")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is divisible by {i}")
            is_prime = False
            break
    
    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")

# Example 9: Factorial Calculator
print("\n--- EXAMPLE 9: FACTORIAL CALCULATOR ---")
n = 5
factorial = 1
i = 1

print(f"Calculating factorial of {n}:")

while i <= n:
    factorial *= i
    i += 1

print(f"{n}! = {factorial}")

# Example 10: Sum of Even Numbers
print("\n--- EXAMPLE 10: SUM OF EVEN NUMBERS ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0

print(f"Numbers: {numbers}")

for num in numbers:
    if num % 2 != 0:
        continue  # Skip odd numbers
    even_sum += num

print(f"Sum of even numbers: {even_sum}")

