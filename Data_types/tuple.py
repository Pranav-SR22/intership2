#tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#empty tuple
#tuple is unmutable, so we cannot add or remove items after creation
#multiple data types can be stored in a tuple
#tuple written using paranthesis ()
#tuple use less memory compared to list
#tuple can be used as keys in dictionary (if they contain only immutable items) where as list cannot be used as keys 

#creating tuples
empty_tuple = ()
single_item_tuple = (42,) #comma is necessary for single item tuple
mixed_tuple = (1, "hello", 3.14, True)
nested_tuple = (1, (2, 3), [4, 5], ("a", "b"))  
print(empty_tuple)        #()
print(single_item_tuple)  #(42,)
print(mixed_tuple)       #(1, 'hello', 3.14, True)
print(nested_tuple)      #(1, (2, 3), [4, 5], ('a', 'b'))

#single element tuple

#it should have trailing comma
#without comma, it is considered as a regular parenthesis
#common mistake

single_tuple = (5)
print(type(single_tuple))  #<class 'int'>
print(single_tuple)        #5   

correct_single_tuple = (5,)
print(type(correct_single_tuple))  #<class 'tuple'>
print(correct_single_tuple)        #(5,)

#tuple without paranthesis
tuple_no_paren = 1, 2, 3, "hello"
print(tuple_no_paren)      #(1, 2, 3, 'hello')
print(type(tuple_no_paren)) #<class 'tuple'>

#empty tuple
empty_tuple_no_paren = ()
print(empty_tuple_no_paren)      #()
print(type(empty_tuple_no_paren)) #<class 'tuple'>



#bucket 1

#tuple length
my_tuple = (10, 20, 30, 40, 50, 60)
print(len(my_tuple))  #6

#indexing is same as list
sample_tuple = (10, 20, 30, 40, 50)
print(sample_tuple[0])  #10
print(sample_tuple[2])  #30 

#slicing
print(sample_tuple[1:4])  #(20, 30, 40)
print(sample_tuple[:3])    #(10, 20, 30)
print(sample_tuple[2:])    #(30, 40, 50)
print(sample_tuple[-3:-1]) #(30, 40)
print(sample_tuple[:])     #(10, 20, 30, 40, 50) (entire tuple)


#changing elements inside nested mutable items
nested_tuple = (1, 2, [3, 4], 5)
#need to change value at index 1 of nested_tuple

print(nested_tuple)  #(1, 2, [3, 4], 5)
#modifying the list inside the tuple    
nested_tuple[2][0] = 99
print(nested_tuple)  #(1, 2, [99, 4], 5)
#we cannot change the tuple itself
#nested_tuple[0] = 10  #TypeError: 'tuple' object does not support item assignment
#nested_tuple[2] = [1, 2, 3]  #TypeError: 'tuple' object does not support item assignment

#but can modify mutable items inside tuple
nested_tuple[2].append(55)
print(nested_tuple)  #(1, 2, [99, 4, 55], 5)


#tuple with mutable items
tuple_with_list = (1, 2, [3, 4, 5])
print("Before modification:", tuple_with_list)  #Before modification: (1, 2, [3, 4, 5])
#modifying the list inside the tuple
tuple_with_list[2].append(6)
print("After modification:", tuple_with_list)   #After modification: (1, 2, [3, 4, 5, 6])   

#cannot change tuple items directly
#tuple_with_list[0] = 10  #TypeError: 'tuple' object does not support item assignment


#tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  #(1, 2, 3, 4, 5, 6)
#original tuples remain unchanged
print("Original tuple1:", tuple1)  #Original tuple1: (1, 2, 3)
print("Original tuple2:", tuple2)  #Original tuple2 : (4, 5, 6)


#multiple concatenation
repeat_tuple = (1, 2, 3)
print(repeat_tuple)
print(repeat_tuple * 3)


#tuple 
#==================================================================================
# TUPLE REPETITION
#==================================================================================
"""
NOTES:
- Can repeat tuples using * operator
- Creates a new tuple with repeated elements
- Useful for initialization
"""

repeat_tuple = (1, 2, 3)
print("\nOriginal tuple:", repeat_tuple)
print("Repeated 3 times:", repeat_tuple * 3)
print("Repeated 2 times:", repeat_tuple * 2)

# Creating tuple with same value
zeros = (0,) * 5
print("Tuple of 5 zeros:", zeros)

# Empty tuple repetition
empty = () * 10
print("Empty tuple repeated:", empty)

#==================================================================================
# CHECKING ELEMENT IN TUPLE (MEMBERSHIP OPERATORS)
#==================================================================================
"""
NOTES:
- 'in' operator checks if element exists
- 'not in' operator checks if element doesn't exist
- Returns True or False
- Searches through entire tuple (slower for large tuples)
"""

fruits_tuple = ("apple", "banana", "cherry", "date")
print("\nFruits tuple:", fruits_tuple)
print("Is 'banana' in tuple?", "banana" in fruits_tuple)
print("Is 'grape' in tuple?", "grape" in fruits_tuple)
print("Is 'grape' not in tuple?", "grape" not in fruits_tuple)

numbers = (10, 20, 30, 40, 50)
print("\nNumbers tuple:", numbers)
print("Is 30 in tuple?", 30 in numbers)
print("Is 100 in tuple?", 100 in numbers)

#==================================================================================
# TUPLE METHODS (ONLY 2 METHODS!)
#==================================================================================
"""
NOTES:
- Tuples have only 2 methods (because they're immutable)
- count(value) - returns number of occurrences
- index(value) - returns first index of value
- No methods for modification (append, remove, etc.)
"""

# count() method
sample = (1, 2, 2, 3, 2, 4, 5, 2)
print("\nSample tuple:", sample)
print("Count of 2:", sample.count(2))
print("Count of 1:", sample.count(1))
print("Count of 10 (not in tuple):", sample.count(10))

letters = ("a", "b", "c", "a", "a", "d")
print("\nLetters tuple:", letters)
print("Count of 'a':", letters.count("a"))
print("Count of 'z':", letters.count("z"))

# index() method
fruits = ("apple", "banana", "cherry", "banana", "date")
print("\nFruits tuple:", fruits)
print("Index of 'cherry':", fruits.index("cherry"))
print("Index of 'banana' (first occurrence):", fruits.index("banana"))

# index() with start and end parameters
print("Index of 'banana' starting from index 2:", fruits.index("banana", 2))
print("Index of 'banana' between index 2 and 5:", fruits.index("banana", 2, 5))

# ValueError if element not found
# print(fruits.index("grape"))  # ValueError: tuple.index(x): x not in tuple
print("index() raises ValueError if element not found")

#==================================================================================
# TUPLE UNPACKING (VERY IMPORTANT!)
#==================================================================================
"""
NOTES:
- Tuple unpacking assigns tuple elements to variables
- Number of variables must match number of elements (or use *)
- Very useful for returning multiple values from functions
- Makes code more readable and Pythonic
"""

# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print("\nTuple:", coordinates)
print("x:", x)
print("y:", y)

# Unpacking with multiple values
person = ("John", 25, "Engineer")
name, age, profession = person
print("\nPerson tuple:", person)
print("Name:", name)
print("Age:", age)
print("Profession:", profession)


#==================================================================================
# NESTED TUPLES
#==================================================================================
"""
NOTES:
- Tuples can contain other tuples
- Useful for representing complex data structures
- Access using multiple indices
"""


# 2D tuple (like a matrix)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("\nMatrix tuple:")
print(matrix)
print("First row:", matrix[0])
print("Element at [1][2]:", matrix[1][2])
print("Last element:", matrix[2][2])

# Tuple of tuples
students = (
    ("Alice", 85, "A"),
    ("Bob", 92, "A+"),
    ("Charlie", 78, "B")
)

print("\nAccessing nested data:")
print("First student name:", students[0][0])
print("Second student grade:", students[1][2])

# Deeply nested tuple
nested = (1, (2, (3, (4, 5))))
print("\nDeeply nested tuple:", nested)
print("Access innermost 5:", nested[1][1][1][1])


#==================================================================================
# TUPLE COMPARISON
#==================================================================================
"""
NOTES:
- Tuples can be compared using comparison operators
- First different element determines the result
- If all elements equal and same length, tuples are equal
"""

tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3)
tuple_c = (1, 2, 4)
tuple_d = (1, 2)

print("\ntuple_a:", tuple_a)
print("tuple_b:", tuple_b)
print("tuple_c:", tuple_c)
print("tuple_d:", tuple_d)

print("\nComparisons:")
print("tuple_a == tuple_b:", tuple_a == tuple_b)
print("tuple_a == tuple_c:", tuple_a == tuple_c)
print("tuple_a < tuple_c:", tuple_a < tuple_c)
print("tuple_a > tuple_c:", tuple_a > tuple_c)
print("tuple_a > tuple_d:", tuple_a > tuple_d)

# String tuple comparison
words1 = ("apple", "banana")
words2 = ("apple", "cherry")
print("\nwords1:", words1)
print("words2:", words2)
print("words1 < words2:", words1 < words2)

#==================================================================================
# CONVERTING BETWEEN DATA TYPES
#==================================================================================
"""
NOTES:
- Can convert list to tuple
- Can convert tuple to list
- Can convert string to tuple
- Can convert set to tuple
- Can convert range to tuple
"""

# List to Tuple
my_list = [1, 2, 3, 4, 5]
tuple_from_list = tuple(my_list)
print("\nList:", my_list)
print("Converted to tuple:", tuple_from_list)

# Tuple to List
my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print("\nTuple:", my_tuple)
print("Converted to list:", list_from_tuple)

# String to Tuple
text = "hello"
tuple_from_string = tuple(text)
print("\nString:", text)
print("Converted to tuple:", tuple_from_string)

# Set to Tuple
my_set = {3, 1, 4, 2}
tuple_from_set = tuple(my_set)
print("\nSet:", my_set)
print("Converted to tuple:", tuple_from_set)

# Range to Tuple
range_obj = range(1, 6)
tuple_from_range = tuple(range_obj)
print("\nRange object:", range_obj)
print("Converted to tuple:", tuple_from_range)

# Dictionary to Tuple (keys only)
my_dict = {"a": 1, "b": 2, "c": 3}
tuple_from_dict = tuple(my_dict)
print("\nDictionary:", my_dict)
print("Tuple of keys:", tuple_from_dict)

# Dictionary items to tuple
tuple_from_items = tuple(my_dict.items())
print("Tuple of key-value pairs:", tuple_from_items)

#==================================================================================
# TUPLE AS DICTIONARY KEY (IMPORTANT USE CASE!)
#==================================================================================
"""
NOTES:
- Tuples can be used as dictionary keys (lists cannot)
- Must contain only immutable elements
- Useful for composite keys
- Common in real-world applications
"""

# Using tuple as dictionary key
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}
print("\nDictionary with tuple keys:")
print(locations)
print("Location at (51.5074, -0.1278):", locations[(51.5074, -0.1278)])

# Multi-dimensional dictionary
grades = {
    ("Alice", "Math"): 95,
    ("Alice", "Science"): 88,
    ("Bob", "Math"): 82,
    ("Bob", "Science"): 90
}
print("\nStudent grades:")
print("Alice's Math grade:", grades[("Alice", "Math")])
print("Bob's Science grade:", grades[("Bob", "Science")])


# Cannot use list as key
# invalid_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
print("\nLists cannot be dictionary keys (mutable)")
print("Tuples can be dictionary keys (immutable)")
 
#==================================================================================
# TUPLE COMPREHENSION (DOESN'T EXIST - RETURNS GENERATOR!) -> Advance concept 
#==================================================================================
"""
NOTES:
- (x for x in ...) creates generator, not tuple
- Use tuple() constructor to convert generator to tuple
- Generator is memory efficient for large datasets
"""

# This creates a generator, not tuple
gen = (x**2 for x in range(5))
print("\nGenerator expression:", gen)
print("Type:", type(gen))

# Convert generator to tuple
squares_tuple = tuple(x**2 for x in range(5))
print("Tuple from generator:", squares_tuple)
print("Type:", type(squares_tuple))

# Comparing memory
import sys
large_tuple = tuple(range(10000))
large_gen = (x for x in range(10000))
print("\nTuple size in bytes:", sys.getsizeof(large_tuple))
print("Generator size in bytes:", sys.getsizeof(large_gen))
print("Generator is much more memory efficient!")

#==================================================================================
# BUILT-IN FUNCTIONS WITH TUPLES
#==================================================================================
"""
NOTES:
- len() - number of elements
- max() - maximum element (must be comparable)
- min() - minimum element (must be comparable)
- sum() - sum of numeric elements
- sorted() - returns sorted list
- any() - True if any element is True
- all() - True if all elements are True
"""

numbers_tuple = (45, 12, 78, 23, 56)
print("\nNumbers tuple:", numbers_tuple)
print("Length:", len(numbers_tuple))
print("Maximum:", max(numbers_tuple))
print("Minimum:", min(numbers_tuple))
print("Sum:", sum(numbers_tuple))
print("Sorted (returns list):", sorted(numbers_tuple))
print("Sorted descending:", sorted(numbers_tuple, reverse=True))

# any() and all()
bool_tuple1 = (True, True, True)
bool_tuple2 = (True, False, True)
bool_tuple3 = (False, False, False)

print("\nbool_tuple1:", bool_tuple1)
print("all():", all(bool_tuple1))
print("any():", any(bool_tuple1))

print("\nbool_tuple2:", bool_tuple2)
print("all():", all(bool_tuple2))
print("any():", any(bool_tuple2))

print("\nbool_tuple3:", bool_tuple3)
print("all():", all(bool_tuple3))
print("any():", any(bool_tuple3))

# Using any() and all() with conditions
numbers = (2, 4, 6, 8, 10)
print("\nNumbers:", numbers)
print("All even?", all(x % 2 == 0 for x in numbers))
print("Any greater than 5?", any(x > 5 for x in numbers))

#==================================================================================
# ADVANTAGES OF TUPLES OVER LISTS -> for extra knowledge 
#==================================================================================
"""
NOTES:
ADVANTAGES:
1. Faster than lists (iteration, access)
2. Use less memory than lists
3. Immutable - data protection
4. Can be used as dictionary keys
5. Can be used in sets
6. Safer for data that shouldn't change
7. Better for heterogeneous data

WHEN TO USE TUPLES:
- Data should not change
- Need to use as dictionary key
- Want to ensure data integrity
- Storing related but different types of data
- Returning multiple values from function
- Performance is critical
"""

print("\n--- TUPLE VS LIST COMPARISON ---")

# Memory comparison
import sys
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print("List size:", sys.getsizeof(list_data), "bytes")
print("Tuple size:", sys.getsizeof(tuple_data), "bytes")
print("Tuple uses less memory!")

# Tuples in sets (lists cannot be in sets)
set_of_tuples = {(1, 2), (3, 4), (5, 6)}
print("\nSet of tuples:", set_of_tuples)
# set_of_lists = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
print("Lists cannot be added to sets (mutable)")

#==================================================================================
# REAL-LIFE TUPLE EXAMPLES
#==================================================================================
"""
NOTES:
- Tuples are perfect for immutable, related data
- Common in real-world scenarios
"""

# Example 1: RGB Color Values
print("\n--- EXAMPLE 1: RGB COLORS ---")
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

print("Red color:", red)
print("Green color:", green)
print("Accessing red channel:", red[0])

def display_color(color_tuple):
    r, g, b = color_tuple
    print(f"RGB({r}, {g}, {b})")

display_color(blue)

# Example 2: Geographic Coordinates
print("\n--- EXAMPLE 2: COORDINATES ---")
new_york = (40.7128, -74.0060)
london = (51.5074, -0.1278)
tokyo = (35.6762, 139.6503)

cities = {
    new_york: "New York",
    london: "London",
    tokyo: "Tokyo"
}

print("Cities and coordinates:")
for coords, name in cities.items():
    lat, lon = coords
    print(f"{name}: Latitude {lat}, Longitude {lon}")

# Example 3: Date and Time
print("\n--- EXAMPLE 3: DATE REPRESENTATION ---")
date1 = (2025, 12, 23)  # year, month, day
date2 = (2025, 1, 1)

print("Date 1:", date1)
year, month, day = date1
print(f"Formatted: {day}/{month}/{year}")

def format_date(date_tuple):
    y, m, d = date_tuple
    return f"{d:02d}/{m:02d}/{y}"

print("Formatted date:", format_date(date2))

# Example 4: Database Records
print("\n--- EXAMPLE 4: DATABASE RECORDS ---")
employees = [
    (1, "Alice", "Engineering", 75000),
    (2, "Bob", "Marketing", 65000),
    (3, "Charlie", "Sales", 70000),
    (4, "David", "Engineering", 80000)
]

print("Employee Database:")
for emp in employees:
    emp_id, name, dept, salary = emp
    print(f"ID: {emp_id}, Name: {name}, Dept: {dept}, Salary: ${salary}")

# Filter engineers
engineers = [emp for emp in employees if emp[2] == "Engineering"]
print("\nEngineers only:")
for emp in engineers:
    print(emp)

# Example 5: Configuration Settings
print("\n--- EXAMPLE 5: IMMUTABLE CONFIGURATION ---")
# Configuration that should not change
DATABASE_CONFIG = (
    "localhost",    # host
    5432,           # port
    "mydb",         # database name
    "admin"         # username
)

host, port, db_name, user = DATABASE_CONFIG
print(f"Database Config:")
print(f"Host: {host}, Port: {port}, DB: {db_name}, User: {user}")

# Cannot accidentally modify config
# DATABASE_CONFIG[0] = "newhost"  # TypeError
print("Configuration is protected from accidental changes")

#==================================================================================
# END 