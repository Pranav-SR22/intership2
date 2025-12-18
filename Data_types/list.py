#list
#mutable ordered collection of items
#add duplicate items
#defined using square brackets []
#it can contain items of different data types
my_list = [10, 20.5, "Hello", True, 10, 20.5]
print(my_list)  #[10, 20.5, 'Hello', True, 10, 20.5]

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



#BUCKET 4

#sorting LISTS
#2 ways to sort a list
#sort() method to sort the list in place
#sort(reverse=True) to sort in descending order

numbers = [5, 2, 9, 1, 5, 6]

numbers.sort()
print(numbers)  #[1, 2, 5, 5, 6, 9] #ascending order

numbers.sort(reverse=True)
print(numbers)  #[9, 6, 5, 5, 2, 1] #descending order


#reverse() method to reverse the current order of the list
numbers.reverse()
print(numbers)  #[1, 2, 5, 5, 6, 9] #reversed order
#Note: reverse() does not sort, it just reverses the current order

