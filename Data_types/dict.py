#==================================================================================
# DICTIONARY (dict) DATA TYPE IN PYTHON
#==================================================================================
"""
NOTES:
- Dictionary is an unordered collection of key-value pairs
- Dictionary is mutable (changeable)
- Dictionary keys must be unique (no duplicate keys)
- Dictionary keys must be immutable (string, number, tuple)
- Dictionary values can be any data type and can be duplicated
- Dictionary is written using curly braces {} with key:value pairs
- Very fast lookup by key - O(1) time complexity
"""

# Creating dictionaries
student = {"name": "Alice", "age": 20, "grade": "A"}
numbers_dict = {1: "one", 2: "two", 3: "three"}
mixed_dict = {"name": "John", "age": 25, "scores": [85, 90, 78], "active": True,(1,2,3):"tuplevalue"}

print("Student dictionary:", student)
print("Numbers dictionary:", numbers_dict)
print("Mixed dictionary:", mixed_dict)

# Check data type
print("Type of student:", type(student))

#==================================================================================
# EMPTY DICTIONARY
#==================================================================================
"""
NOTES:
- Empty dictionary is created using {} or dict()
- Used when key-value pairs will be added later dynamically
"""

empty_dict = {}
print("\nEmpty dictionary using {}:", empty_dict)
print("Type:", type(empty_dict))

empty_dict2 = dict()
print("Empty dictionary using dict():", empty_dict2)
print("Type:", type(empty_dict2))

#==================================================================================
# CREATING DICTIONARIES (DIFFERENT METHODS)
#==================================================================================
"""
NOTES:
- Multiple ways to create dictionaries
- dict() constructor can take keyword arguments
- dict() can convert list of tuples to dictionary
"""

# Using dict() constructor with keyword arguments
person = dict(name="Bob", age=30, city="New York")
print("\nDictionary using dict():", person)

# Using dict() with list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)
print("Dictionary from list of tuples:", dict_from_pairs)

#==================================================================================
# DICTIONARY KEYS MUST BE IMMUTABLE
#==================================================================================
"""
NOTES:
- Valid keys: string, number, tuple (with immutable elements)
- Invalid keys: list, dict, set (mutable types)
"""

# Valid keys
valid_dict = {
    "name": "Alice",           # string key
    42: "answer",              # integer key
    3.14: "pi",                # float key
    (1, 2): "tuple key",       # tuple key
    True: "boolean key"        # boolean key
}
print("\nDictionary with various key types:", valid_dict)

# Invalid keys (will cause errors)
# invalid_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
# invalid_dict = {{1, 2}: "value"}  # TypeError: unhashable type: 'set'
# invalid_dict = {{"a": 1}: "value"}  # TypeError: unhashable type: 'dict'
print("Lists, sets, and dicts cannot be dictionary keys")

#==================================================================================
# ACCESSING DICTIONARY VALUES
#==================================================================================
"""
NOTES:
- Access values using keys in square brackets []
- Raises KeyError if key doesn't exist
- get() method is safer - returns None or default value if key missing
"""

student = {"name": "Alice", "age": 20, "grade": "A", "city": "Boston"}
print("\nStudent dictionary:", student)

# Using square brackets
print("Name:", student["name"])
print("Age:", student["age"])

# KeyError if key doesn't exist
# print(student["phone"])  # KeyError: 'phone'
print("Accessing non-existent key raises KeyError")

# Using get() method (safer)
print("\nUsing get() method:")
print("Name:", student.get("name"))
print("Phone (doesn't exist):", student.get("phone"))
print("Phone with default:", student.get("phone", "Not available"))

#==================================================================================
# ADDING AND MODIFYING DICTIONARY ITEMS
#==================================================================================
"""
NOTES:
- Add new key-value pair: dict[key] = value
- Modify existing value: dict[key] = new_value
- If key exists, value is updated; if not, new pair is added
- update() - to add multiple key:value pairs
"""

person = {"name": "John", "age": 25}
print("\nOriginal dictionary:", person)

# Adding new key-value pair
person["city"] = "New York"
print("After adding city:", person)

person["email"] = "john@example.com"
print("After adding email:", person)

# Modifying existing value
person["age"] = 26
print("After modifying age:", person)

person["name"] = "John Doe"
print("After modifying name:", person)

# Adding multiple items using update()
person.update({"phone": "123-456-7890", "country": "USA"})
print("After update():", person)

#==================================================================================
# LENGTH OF DICTIONARY
#==================================================================================
"""
NOTES:
- len() returns number of key-value pairs
"""

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
print("\nDictionary:", my_dict)
print("Length (number of key-value pairs):", len(my_dict))

empty = {}
print("Length of empty dictionary:", len(empty))

#==================================================================================
# CHECKING IF KEY EXISTS IN DICTIONARY
#==================================================================================
"""
NOTES:
- 'in' operator checks if key exists
- 'not in' operator checks if key doesn't exist
- Very fast operation - O(1) time complexity
- Only checks keys, not values
"""

student = {"name": "Alice", "age": 20, "grade": "A"}
print("\nStudent dictionary:", student)

print("Is 'name' in dictionary?", "name" in student)
print("Is 'phone' in dictionary?", "phone" in student)
print("Is 'phone' not in dictionary?", "phone" not in student)

# Checking before accessing
if "email" in student:
    print("Email:", student["email"])
else:
    print("Email not found in dictionary")

#==================================================================================
# REMOVING ITEMS FROM DICTIONARY
#==================================================================================
"""
NOTES:
- pop(key) - removes and returns value, raises KeyError if not found
- pop(key, default) - removes and returns value, returns default if not found
- popitem() - removes and returns last inserted key-value pair (Python 3.7+)
- del dict[key] - deletes key-value pair
- clear() - removes all items
"""

# Using pop()
person = {"name": "Alice", "age": 20, "city": "Boston", "grade": "A"}
print("\nOriginal dictionary:", person)

removed_age = person.pop("age")
print("Popped age:", removed_age)
print("After pop('age'):", person)

# pop() with default value
phone = person.pop("phone", "No phone")
print("Popped phone (with default):", phone)
print("Dictionary unchanged:", person)

# pop() without default raises KeyError
# person.pop("email")  # KeyError: 'email'
print("pop() without default raises KeyError if key not found")

# Using popitem() - removes last inserted item
last_item = person.popitem()
print("\nPopped last item:", last_item)
print("After popitem():", person)

# Using del
del person["city"]
print("After del person['city']:", person)

# del with non-existent key raises KeyError
# del person["phone"]  # KeyError: 'phone'

# Using clear()
temp_dict = {"a": 1, "b": 2, "c": 3}
temp_dict.clear()
print("\nAfter clear():", temp_dict)

# Deleting entire dictionary
del_dict = {"x": 1, "y": 2}
del del_dict
# print(del_dict)  # NameError: name 'del_dict' is not defined
print("Dictionary deleted using del")