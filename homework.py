id = "user1"
password = "1234"
if id == "admin" and password == "1234":
    print("Access granted.")
else:
    print("Access denied.")


name = "Pranav"
if name == "Pranav" or name == "Adityan":
    print("Hello, correct user!")
else:
    print("Hello, guest!")

temperature = 30
if not (temperature < 20):
    print("It's warm outside.")
else:
    print("It's cold outside.")


has_id = False
is_vip = False
age = 20
if (age >= 18 and has_id) or is_vip:
    print("Entry allowed.")
else:
    print("Entry denied.")


score = 85
grade = 'B'
if (score >= 90 and grade == 'A') or (score >= 80 and grade == 'B'):
    print("You passed with distinction.")
else:
    print("You did not pass with distinction.")
 