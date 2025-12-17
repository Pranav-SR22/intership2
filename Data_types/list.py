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

#list indexing
#list is a sequence type, so we can access items using indexing
#indexing starts from 0

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


