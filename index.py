#String:
# Series of characters or data stored as text
my_string = "Hello"
print(my_string)

# String Operations:
# returns the string with all uppercase letters
print(my_string.upper())

# returns the length of a string
print(len(my_string))

# returns the index of the first instance of the string inside the subject string, otherwise -1
print(my_string.find('l'))

# replaces any instance of the first string with the second in my_string
print(my_string.replace('H', 'C'))

# Integer:
# A whole number
my_integer = 12321
print(my_integer)

# Float
# A decimal number
my_decimal = 3.14
print(my_decimal)

# Boolean
# Discrete value true or false
x = True
y = False
print(x, y)

# Dictionary:
# Changeable collection of key-value pairs
my_dictionary = {'banana': 1, 12: 'laptop', (0,0):'center'}
print(my_dictionary)

# Dictionary Operations:
# Access value using key
print(my_dictionary[(0,0)])

# Get all keys in a dictionary as a list
print(my_dictionary.keys())

# Get all values in a dictionary as a list
print(my_dictionary.values())

# Tuple:
# Unchangeable collection of objects
tup = (1, 3.12, False, "Hi")
print(tup)

# List:
my_collection = [1, 1, 3.12, False, "Hi"]
print(my_collection)

# List Operations:
# returns the length of a list
print(len(my_collection))

# Add multiple items to a list
my_collection.extend(["More", "Items"])
print(my_collection)

# Add a single item to a list
my_collection.append("Single")
print(my_collection)

# Delete the object of a list at a specified index
del(my_collection[2])
print(my_collection)

# Clone a list
clone = my_collection[:]
print(clone)

# Concatenate two lists
my_collection_2 = ["a", "b", "c"]
my_collection_3 = my_collection + my_collection_2
print(my_collection_3)

# Calculate the sum of a list of insts or floats
number_collection = [1, 2, 3, 4, 5]
print(sum(number_collection))

# Check if an item is in a list, returns Boolean
a = "More" in my_collection
print(a)

# Check if an item is not in a list, returns Boolean
b = "Mor" not in my_collection
print(b)

# Set:
# Unordered collection of unique objects
c = {100, 3.12, False, "Bye"}
d = {100, 3.12, "Welcome"}
print(c, d)

#Set Operations:
# Convert a list to a set
my_set = set([1,1,2,3])
print(my_set)

# Add an item to the set
c.add(4)
print(c)

# Remove an item to the set
c.remove("Bye")
print(c)

# Returns set c minus d
e = c.difference(d)
print(e)

# Returns intersection of set c and d
f = c.intersection(d)
print(f)

# Returns the union of set c and d
g = c.union(d)
print(g)

# Returns True if c is a subset of b, false otherwise
c = {100, 3.12, False, "Bye"}
d = {100, 3.12, "Welcome"}
print(c.issubset(d))

# Returns if c is a superset of d, false otherwise
c = {100, 3.12, False, "Bye"}
d = {100, 3.12, "Welcome"}
print(c.issuperset(d))

# Indexing:
# Accessing data from a string, list, or tuple using an element number
print(my_string[2])
print(my_collection[1])
print(tup[3])

# Slicing:
# Accessing a subset if data from a string, list, or tuple using element numbers from start to stop -1
# my_string[start:stop]
# my_collection[start:stop]
# tup[start:stop]
print(my_string[0:4])
print(my_collection[1:3])
print(tup[0:3])

# Comparison Operators:
# Comparison Operators compare oeprands and return a result of true or false
# Equal
# a == b
# Less Than
# a < b
# Greater Than
# a > b
# Greater Than or Equal
# a >= b
# Less Than or Equal
# a <= b
# Not Equal
# a != b

# Python Operators:
# +: Addition
# -: Subtraction
#- *: Multiplication
# /: division
# - //: Integer Division (Result rounded to the nearest integer)

# Conditional Operators:
# Conditional Operators evaluate the operands and produce a true of false result
# And returns true if both statement a and b are true, otherwise false
# a and b
# Or returns true if either statement a or b are true, otherwise false
# a or b
# Not returns the opposite of the statement
# not a

# Loops:
# For Loops
for x in range(x):
    # Executes loop x nummber of times
    for z in iterable:
        # Executes loop for each object in an iterable like a string, tupple, list, or set
# While Loops
while statement:
    # Executes the loop while statement is true

# Conditional Statements:
if statement_1:
 # Execute of statement_1 is true
elif statement_2:
 # Execute if statement_1 is false and statement_2 is true
else:
 # Execute if all previous statements are false

#  Try/Except:
try:
 # Code to try to execute
except a:
 # Code to execute if there is an error of type a
except b:
 # Code to execute if there is an error of type b
except:
 # Code to execute if there is any exception that has not been handled 
else:
 # Code to execute if there is no exception

#  Error Types:
# IndexError = When an index is out of range
# NameError = When a variable name is not found
# SyntaxError = When there is an error with how the code is written
# ZeroDivisionError = When your code tries to divide by zero

# Range:
# Produce an iterable sequence from 0 to stop -1
range(stop)
# Produce an iterable sequence from start to stop -1 incrementing by step
range(start, stop, step)


# Webscraping:
# Import BeautifulSoup
from bs4 import BeautifulSoup

# Parse HTML stored as a string
soup = BeautifulSoup(html, 'html5lib')

# Returns formatted html
soup.prettify()

# Find the first instance of an HTML tag
soup.find(tag)

# Find all instances of an HTML tag
soup.find_all(tag)


# Requests:
# Import the request library
import requests

# Send a get requests to the url with optional parameters
response = requests.get(url, parameters)

# Get the url of the response
response.url

# Get the status code of the response
response.status_code

# Get the headers of the request
response.request.headers

# Get the body of the request
response.request.body

# Get the headers of the response
response.headers

# Get the content of the response in text
response.text

# Get the content of the response
response.json()

# Send a post requests to the url with optional parameters
requests.post(url, parameters)


# Functions:
# Create a function
def function_name(optional_parameter_1, optional_prameter_2):
    # code to execute
    return optional_output
    
# Calling a function
output = function_name(parameter_1, parameter_2)