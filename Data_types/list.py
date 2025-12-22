my_list = [10, "apple", 3.14, False]
#To check the data type
print(type(my_list))  #<class 'list'>

numbers = [1, 2, 3, 4, 5]
print(numbers)  #[1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
print(fruits)  #['apple', 'banana', 'cherry']
mixed = [10, "apple", 3.14, False, [1, 2, 3], (4, 5), {'key': 'value'}, None]
print(mixed)  #[10, 'apple', 3.14, False, [1, 2, 3], (4, 5), {'key': 'value'}, None]    

#emmpty list
empty_list = []
print(empty_list)  #[]


#list with one item
single_item_list = [42]
print(single_item_list)  #[42]
#list with duplicate items
dup_list = [1, 2, 2, 3, 3, 3]
print(dup_list)  #[1, 2, 2, 3, 3, 3]
#list with nested lists
nested_list = [1, [2, 3], [4, [5, 6]]]
print(nested_list)  #[1, [2, 3], [4, [5, 6]]]



#BUCKET 1
#list length
#list indexing
#list is a sequence type, so we can access items using indexing
#indexing starts from 0


print(len(my_list))        #6
print(len(fruits))         #3

samples = ["apple", "banana", "cherry", "date", "berry"]
print(samples[0])  #apple
print(samples[2])  #cherry
print(samples[4])  #berry  
print(samples[-1]) #berry (last item)
print(samples[-3]) #cherry (third last item)


#list slicing
#we can extract a portion of the list using slicing
print(samples[1:4])  #['banana', 'cherry', 'date']
print(samples[:3])    #['apple', 'banana', 'cherry']
print(samples[2:])    #['cherry', 'date', 'berry']
print(samples[-4:-1]) #['banana', 'cherry', 'date']
print(samples[:])     #['apple', 'banana', 'cherry', 'date', 'berry'] (entire list) 

#syntax: list_name[start:end:step]
print(samples[0:5:2])  #['apple', 'cherry', 'berry'] (every second item)
print(samples[::-2])    #['berry', 'date', 'cherry', 'banana', 'apple'] (reversed list)

#negative step
print(samples[4:1:-1]) #['berry', 'date', 'cherry'] (from index 4 to 2 in reverse order)
print(samples[3:0:-1]) #['date', 'cherry', 'banana'] (from index 3 to 1 in reverse order)

list = ["a", "b", "c", "d", "e"]
#negative indexing and slicing
print(list[-1])    #e
print(list[-3])    #c
print(list[-5:-2]) #['a', 'b', 'c']
print(list[-1:-6:-1]) #['e', 'd', 'c', 'b', 'a']
print(list[-2::-1])   #['d', 'c', 'b', 'a']


#list is mutable
#we can change, add, remove items in a list
#strings are immutable, we cannot change individual characters in a string


colors = ["red", "green", "blue"]
print(colors)  #['red', 'green', 'blue']


#changing an item
colors[1] = "yellow"
print(colors)  #['red', 'yellow', 'blue']



#BUCKET 2
#ADDING ITEMS TO LIST
"""
adding an item using append()
add item at the end of the list
insert(index, item) to add item at specific index

"""
#method 1.1
colors.append("purple")
print(colors)  #['red', 'yellow', 'blue', 'purple']

a=[1, 2, 3]
b=[4, 5]
a.append(b)
print(a)  #[1, 2, 3, [4, 5]]

#extend() method to add multiple items from another list
a.extend(b)
print(a)  #[1, 2, 3, [4, 5], 4, 5]

#method 1.2
#two parameter insert() to add item at specific index 
#if we try to add at index greater than length, it adds at the end no error

colors.insert(100, "orange")
print(colors)  #['red', 'orange', 'yellow', 'blue', 'purple']

#in real wold we dont need to add beginning very often as it shifts all other items like when a new student joins class


#BUCKET 3

#REMOVAL OF ITEMS
#4 ways to remove items from list
#removing an item using remove(value)
#pop() to remove item at the end and return it
#pop(index) to remove item at specific index
#clear() to remove all items
#del keyword to delete entire list or a portion of the list using slicing
#if we try to remove an item not in the list using remove(), it gives ValueError


colors.remove("yellow")
print(colors)  #['red', 'orange', 'blue', 'purple']


#removing item using pop()
popped_color = colors.pop()
print(popped_color)  #purple
print(colors)       #['red', 'orange', 'blue']


#removing item at specific index using pop(index)
popped_color2 = colors.pop(1)
print(popped_color2)  #orange
print(colors)        #['red', 'blue']


#removing all items using clear()
colors.clear()
print(colors)  #[]

#del keyword to delete entire list
#permanently deletes the list
#del slicing to delete a portion of the list

colors = ["red", "green", "blue", "yellow", "purple"]
del colors[1:4]
print(colors)  #['red', 'purple']

del colors
#print(colors)  #gives NameError as colors is deleted




#BUCKET 4

#sorting LISTS
#2 ways to sort a list
#sort() method to sort the list in place
#sort(reverse=True) to sort in descending order

numbers = [5, 2, 9, 1, 5, 6]
letters = ['d', 'a', 'c', 'b']

letters.sort()
print(letters)  #['a', 'b', 'c', 'd'] #ascending order
letters.sort(reverse=True)
print(letters)  #['d', 'c', 'b', 'a'] #descending order


numbers.sort()
print(numbers)  #[1, 2, 5, 5, 6, 9] #ascending order

numbers.sort(reverse=True)
print(numbers)  #[9, 6, 5, 5, 2, 1] #descending order

#sorted() function to return a new sorted list without modifying the original, returns a new list
original_numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(original_numbers)
print(original_numbers)  #[5, 2, 9, 1, 5, 6] #original list unchanged
print(sorted_numbers)    #[1, 2, 5, 5, 6, 9] #new sorted list
original_numbers_desc = sorted(original_numbers, reverse=True)
print(original_numbers_desc)  #[9, 6, 5, 5, 2, 1] #new sorted list in descending order


#BUCKET 5

#reverse() method to reverse the current order of the list
numbers.reverse()
print(numbers)  #[1, 2, 5, 5, 6, 9] #reversed order
#Note: reverse() does not sort, it just reverses the current order


#BUCKET 6

#copying a list
#copy() method to create a shallow copy

a = [1, 2, 3]
b = a
b.append(4)
print("a:", a)  #[1, 2, 3, 4] both a and b refer to same list
print("b:", b)  #[1, 2, 3, 4]   

c= a.copy()
c.append(5)
print("a:", a)  #[1, 2, 3, 4]
print("c:", c)  #[1, 2, 3, 4, 5] c is a separate copy

#change in copy does not affect original list


#homework 
#what is shallow copy vs deep copy
#what is reference vs copy
#list comprehenshion
#how range works
#anyother built in functions


#list concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  #[1, 2, 3, 4, 5, 6]

#list repetition
repeated = list1 * 3
print(repeated)  #[1, 2, 3, 1, 2, 3, 1, 2, 3]



#bucket 7
#count and index methods

numbers = [1, 2, 3, 2, 4, 2, 5]

print(numbers.count(2))  #3 (counts occurrences of 2)

print(numbers.index(4))  #4 (index of first occurrence of 4)


#checkiing elemeent inside list, membership operators
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   #True
print("grape" not in fruits) #True
print("grape" in fruits)    #False
print("apple" not in fruits)  #False



#nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[0])      #[1, 2, 3] first row
print(matrix[1][2])   #6 element at row 1, column 2


#list comprehension

squares = [i * i for i in range(1, 6)]
print(squares)  #[1, 4, 9, 16, 25]

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)  #[2, 4, 6, 8, 10]


#type conversion to list


#bucket 

#built-in functions with lists
2
numbers = [10, 20, 5, 15]
print(sum(numbers))   #50
print(min(numbers))   #5
print(max(numbers))   #20
print(len(numbers))   #4


#bucket

#any() and all()
num = [0, 1, 2, 3]
print(any(num))  #True (at least one non-zero)
print(all(num))  #False (not all non-zero)
print(all(i % 2 == 0 for i in num))  #False (not all even)
print(any(i > 2 for i in num))  #True (at least one greater than 2)


#real world examples of lists
mark = [85, 90, 78, 92, 88]  #marks of a student in different subjects
total_marks = sum(mark)
average = total_marks / len(mark)
print("Total Marks:", total_marks)    #Total Marks: 433
print("Average Marks:", average)      #Average Marks: 86.6

cart = ["apple", "banana", "orange"]
cart.append("grape")
print("Shopping Cart:", cart)  #Shopping Cart: ['apple', 'banana', 'orange', 'grape']

