#==================================================================================
# SET (set) DATA TYPE IN PYTHON
#==================================================================================
"""
NOTES:
- Set is an unordered collection of unique elements
- Set is mutable (changeable) but elements must be immutable
- Set does NOT allow duplicate values (automatically removes duplicates)
- Set does NOT maintain insertion order (unordered)
- Set is written using curly braces {}
- Set does NOT support indexing or slicing (because it's unordered)
- Set elements must be immutable (can't add list, dict, or set as elements)
"""

# Creating sets
numbers_set = {1, 2, 3, 4, 5}
names_set = {"Alice", "Bob", "Charlie"}
mixed_set = {1, "Python", 3.14, True}  # Can mix types but elements must be immutable

print("Numbers set:", numbers_set)
print("Names set:", names_set)
print("Mixed set:", mixed_set)

# Check data type
print("Type of numbers_set:", type(numbers_set))

# Sets automatically remove duplicates
duplicate_set = {1, 2, 2, 3, 3, 3, 4}
print("Set with duplicates removed:", duplicate_set)

#==================================================================================
# EMPTY SET
#==================================================================================
"""
NOTES:
- Empty set must be created using set() function
- {} creates an empty dictionary, NOT an empty set
- Used when unique elements will be added later dynamically
"""

empty_set = set()
print("Empty set:", empty_set)
print("Type of empty set:", type(empty_set))

# This creates a dictionary, not a set
not_a_set = {}
print("Empty dictionary (not set):", type(not_a_set))

#==================================================================================
# SET DOES NOT SUPPORT INDEXING OR SLICING
#==================================================================================
"""
NOTES:
- Sets are unordered, so no indexing or slicing
- Cannot access elements by position
"""

sample_set = {10, 20, 30, 40, 50}
# print(sample_set[0])  # TypeError: 'set' object is not subscriptable
# print(sample_set[1:3])  # TypeError: 'set' object is not subscriptable

print("Cannot use indexing on sets - sets are unordered")

#==================================================================================
# LENGTH OF SET
#==================================================================================
"""
NOTES:
- len() returns number of unique elements in the set
"""

my_set = {10, 20, 30, 40, 50}
print("Length of set:", len(my_set))

duplicate_check = {1, 1, 2, 2, 3, 3}
print("Length after removing duplicates:", len(duplicate_check))

#==================================================================================
# SET IS MUTABLE (BUT ELEMENTS MUST BE IMMUTABLE)
#==================================================================================
"""
NOTES:
- Set itself can be modified (add/remove elements)
- But elements inside set must be immutable
- Cannot add list, dict, or set as elements
- Can add int, float, string, tuple, frozenset
"""

mutable_set = {1, 2, 3}
mutable_set.add(4)
print("Set after adding element:", mutable_set)

# Valid immutable elements
valid_set = {1, "text", 3.14, (1, 2), True}
print("Set with valid immutable elements:", valid_set)

# Invalid - cannot add mutable elements
# invalid_set = {1, 2, [3, 4]}  # TypeError: unhashable type: 'list'
# invalid_set = {1, 2, {3, 4}}  # TypeError: unhashable type: 'set'
print("Cannot add mutable elements like lists or sets inside sets")

#==================================================================================
# ADDING ELEMENTS TO SET
#==================================================================================
"""
NOTES:
- add() adds single element to the set
- update() adds multiple elements from iterable
- If element already exists, set remains unchanged (no duplicates)
"""

# Using add()
nums_set = {1, 2, 3}
nums_set.add(4)
print("After add(4):", nums_set)

nums_set.add(2)  # Adding duplicate - no effect
print("After add(2) - duplicate ignored:", nums_set)

# Using update() - adds multiple elements
nums_set.update([5, 6, 7])
print("After update([5, 6, 7]):", nums_set)

nums_set.update({8, 9}, [10, 11])
print("After update with multiple iterables:", nums_set)

# Update with string (adds each character)
char_set = {'a', 'b'}
char_set.update("cd")
print("After update('cd'):", char_set)

#==================================================================================
# REMOVING ELEMENTS FROM SET
#==================================================================================
"""
NOTES:
- remove(value) - removes element, raises KeyError if not found
- discard(value) - removes element, does nothing if not found
- pop() - removes and returns random element (set is unordered)
- clear() - removes all elements
- del - deletes entire set(no indexing or slicing)
"""

# Using remove()
fruits = {"apple", "banana", "cherry", "date"}
fruits.remove("banana")
print("After remove('banana'):", fruits)

# fruits.remove("grape")  # KeyError: 'grape' - element not found
print("remove() raises KeyError if element not found")

# Using discard() - safer, no error if element doesn't exist
fruits.discard("cherry")
print("After discard('cherry'):", fruits)

fruits.discard("grape")  # No error
print("After discard('grape') - no error:", fruits)

# Using pop() - removes random element
numbers = {10, 20, 30, 40, 50}
removed = numbers.pop()
print("Popped element:", removed)
print("Set after pop():", numbers)

# Using clear()
temp_set = {1, 2, 3, 4, 5}
temp_set.clear()
print("Set after clear():", temp_set)

# Using del - deletes entire set
del_set = {1, 2, 3}
del del_set
# print(del_set)  # NameError: name 'del_set' is not defined
print("Set deleted using del")

#==================================================================================
# CHECKING ELEMENT IN SET (MEMBERSHIP OPERATORS)
#==================================================================================
"""
NOTES:
- 'in' operator checks if element exists
- 'not in' operator checks if element doesn't exist
- Very fast operation - O(1) time complexity
- More efficient than checking in list
"""

colors = {"red", "green", "blue", "yellow"}
print("Is 'red' in colors?", "red" in colors)
print("Is 'purple' in colors?", "purple" in colors)
print("Is 'purple' not in colors?", "purple" not in colors)

#==================================================================================
# SET OPERATIONS (MATHEMATICAL SET OPERATIONS)
#==================================================================================
"""
NOTES:
- Union: all elements from both sets
- Intersection: common elements in both sets
- Difference: elements in first set but not in second
- Symmetric Difference: elements in either set but not both
"""

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union - combines all elements (no duplicates)
print("\n--- UNION ---")
print("set_a:", set_a)
print("set_b:", set_b)
print("Union using | operator:", set_a | set_b)
print("Union using union():", set_a.union(set_b))

# Intersection - common elements
print("\n--- INTERSECTION ---")
print("Intersection using & operator:", set_a & set_b)
print("Intersection using intersection():", set_a.intersection(set_b))

# Difference - elements in first set but not in second
print("\n--- DIFFERENCE ---")
print("set_a - set_b:", set_a - set_b)
print("set_a.difference(set_b):", set_a.difference(set_b))
print("set_b - set_a:", set_b - set_a)

# Symmetric Difference - elements in either set but not both  -> excludes all elemnts in common
print("\n--- SYMMETRIC DIFFERENCE ---")
print("Symmetric difference using ^ operator:", set_a ^ set_b)
print("Symmetric difference using symmetric_difference():", set_a.symmetric_difference(set_b))