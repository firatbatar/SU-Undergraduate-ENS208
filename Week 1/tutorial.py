"""
The examples are taken from the following webpage: 
    https://docs.python.org/3/tutorial/index.html
"""

# 3. An Informal Introduction to Python
# 3.1. Using Python as a Calculator
# 3.1.1. Numbers
2 + 2
50 - 5 * 6
(50 - 5 * 6) / 4
8 / 5 # division always returns a floating point number

17 / 3 # classic division returns a float
17 // 3 # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # result * divisor + remainder

5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7

# assignment operator is =
width = 20
height = 5 * 9
width * height


##############################
# 3.1.2. Strings
# Both single quotes and double quotes can be used when defining strings
'spam eggs'  # single quotes
"spam eggs"  # double quotes

# use print() function to produce more readable output 
s = 'First line.\nSecond line.' 
print('First line.\nSecond line.')  # with print(), \n produces a new line
s # without print(), the output does not produce a new line

# string literals can span multiple lines using triple-quotes
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# string concatenation and repetition
3 * 'un' + 'ium' # 3 times 'un', followed by 'ium'
'Py' 'thon'
text = ('Put several strings within parentheses '
        'to have them joined together.')
text

prefix = 'Py'
prefix + 'thon' 

# indexing (subscripting) strings (starts with 0)
word = 'Python'
word[0] # character in position 0
word[5] # character in position 5
# negative indices for counting from right (starts with -1)
word[-1] # last character
word[-2] # second-last character
word[-6] 

# slicing strings to obtain substrings (start always included, end always excluded)
word[0:2] # characters from position 0 (included) to 2 (excluded)
word[2:5] # characters from position 2 (included) to 5 (excluded)
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end

# index out of range
word[42]  # the word only has 6 characters

# out of range slice indices are handled gracefully
word[4:42]
word[42:]

# strings are immutable (assignment to an indexed position is not allowed)
word[0] = 'J'
word[2:] = 'py'
'J' + word[1:]
word[:2] + 'py'

# len() fucntion to get the length of a string
s = 'supercalifragilisticexpialidocious'
len(s)

##############################
# 3.1.3. Lists
squares = [1, 4, 9, 16, 25]
squares

# indexing & slicing
squares[0] # indexing returns the item
squares[-1]
squares[-3:] # slicing returns a new list
squares[:] #returns a shallow copy of the list

# concatenation 
squares + [36, 49, 64, 81, 100]

# lists are mutable, their content can be changed
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
cubes

# adding new items at the end of the list with append() function (eq. to list = list + [...], but more efficient)
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # add the cube of 7
cubes

# assignment to slices
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
letters[2:5] = ['C', 'D', 'E']  # replace some values
letters
letters[2:5] = []  # now remove them
letters
letters[:] = [] # clear the list by replacing all the elements with an empty list
letters

# len() also applies to lists
letters = ['a', 'b', 'c', 'd']
len(letters)

# nested lists (lists of lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]

##############################
# 3.2. First Steps Towards Programming
# Fibonacci series: the sum of two elements defines the next
a, b = 0, 1 # multiple assignmens (values are simultaneously assigned)
while a < 10:
    print(a)
    a, b = b, a+b 
c = 0

# multiple arguments with print() function
i = 256 * 256
print('The value of i is:', i)

# keyword argument end (to avoid new line after the output, or end the output with a different string)
a, b = 0, 1
while a < 1000:
    print(a, end = ',')
    a, b = b, a+b

##############################
# 4. More Control Flow Tools
# 4.1. if Statements
#x = int(input("Please enter an integer: "))
x = 1
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

##############################
# 4.2. for Statements (iterates over the items of any sequence)
# measure some strings
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# make a copy of the sequence you are iterating over first if you want to modify it
for w in words[:]:  # loop over a slice copy (shallow copy) of the entire list
    if len(w) > 6:
        words.insert(0, w)   
words

##############################
# 4.3. The range() function (useful for iterating over a sequence of numbers, endpoint always excluded)
for i in range(5):
    print(i)

# iterating over the indices of a sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    
print(range(10)) # the object returned by range() is an iterable, not a list
list(range(10)) # list() function can create a list from a given iterable

##############################
# 4.4. break and continue Statements, and else Clauses on Loops
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else: # else clause of the inner for loop (if the break statement in the inner loop is not executed, then this else is executed)
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        
for num in range(2, 100):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)        
        
##############################
# 4.5. pass Statements (no action, does nothing, sometimes used as a placeholder)
while True:
    pass  # busy-wait for keyboard interrupt (Ctrl+C)

class MyEmptyClass:
    pass

def initlog(*args):
    pass # remember to implement this!
    
##############################
# 4.6. Defining Functions
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n.""" # this is a docstring (function's documentation string)
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b
    print()
    
fib(2000) # now call the function we just defined

f = fib # assigning fib to another name
f(100) # now f can be used as the fib function

print(fib(0)) # if the function definition does not involve a return statement, then the returned value is None

def fib2(n):    # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n.""" # this is a docstring (function's documentation string)
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

fib2(100)
print(fib2(100))
##############################
# 4.7.6. Documentation Strings
def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

##############################
# 5. Data Structures
# 5.1. More on Lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)  # find next banana starting at position 4
fruits.reverse()
fruits
fruits.append('grape')
fruits
fruits.sort()
fruits
fruits.pop()
fruits

##############################
# 5.1.1. Using Lists as Stacks (LIFO)
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack
stack.pop()
stack.pop()
stack

##############################
# 5.1.2. Using Lists as Queues (FIFO)
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # Terry arrives
queue.append("Graham") # Graham arrives
queue.popleft() # the first to arrive now leaves
queue.popleft() # the second to arrive now leaves
queue # Remaining queue in order of arrival

##############################
# 5.1.3. List Comprehensions
squares = [x**2 for x in range(10)]
squares

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec] # create a new list with the values doubled
[x for x in vec if x >= 0] # filter the list to exclude negative numbers
[abs(x) for x in vec] # apply a function to all the elements

freshfruit = ['  banana', '  loganberry ', 'passion fruit  '] 
[weapon.strip() for weapon in freshfruit] # call a method on each element

[(x, x**2) for x in range(6)] # create a list of 2-tuples like (number, square) 

vec = [[1,2,3], [4,5,6], [7,8,9]] # flatten a list using a listcomp with two 'for'
[y for x in vec for y in x]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]

##############################
# 5.1.4. Nested List Comprehensions
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
[[row[i] for row in matrix] for i in range(4)] # transpose rows and columns of matrix

##############################
# 5.2. The del Statement (to remove an item from a list given its index)
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
del a[2:4]
a
del a[:]
a

del a # delete the entire variable

##############################
# 5.3. Tuples and Sequences
# a tuple is a sequence data type (like strings and lists) and it consists of a number of comma separated values
t = 12345, 54321, 'hello!' # tuple packing
t[0]
t

u = t, (1, 2, 3, 4, 5) # a nested tuple
u

t[0] = 88888 # tuples are immutable

v = ([1, 2, 3], [3, 2, 1]) # but can contain mutable objects
v[0][2] = 5
v

empty = () # an empty tuple
singleton = 'hello',  # a tuple containing a single item
len(empty)
len(singleton)
singleton

x, y, z = t # sequence unpacking
print(x, y, z)

##############################
# 5.4. Sets (unordered collection with no duplicate elements)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # show that duplicates have been removed
'orange' in basket # membership testing
'crabgrass' in basket # membership testing

a = set('abracadabra')
b = set('alacazam')
a # unique letters in a
b # unique letters in b
a - b # difference operation (a \setminus b)
a | b # union operation (a \cup b)
a & b # intersection operation (a \cap b)
a ^ b # symmetric difference operation ((a \setminus b) \cup (b \setminus a))

# set comprehensions (similar to list comprehensions)
a = {x for x in 'abracadabra' if x not in 'abc'}
a

##############################
# 5.5. Dictionaries (associative array, similar to hashmap in java)
# a dictionary is a set of key-value pairs, keys must be of immutable type, and unique within one dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127 # add a new key-value pair
tel
tel['jack'] # retrieve the value corresponding to key 'jack'
del tel['sape'] # delete the key-value pair associated with key 'sape'
tel['irv'] = 4127 # add a new key-value pair
tel
list(tel) # return the keys as a list (in insertion order)
sorted(tel) # return the keys as a sorted list
'guido' in tel # key membership test
'jack' not in tel # key membership test (negated)

# building dictionaries with dict() constructor from sequences of key-value pairs
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# building dictionaries with dict comprehensions
{x: x**2 for x in (2, 4, 6)}

# using keyword arguments to specify pairs
dict(sape = 4139, guido = 4127, jack = 4098)

##############################
# 5.6. Looping Techniques
# looping through a dictionary (items() method to retrieve key-value pairs)
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# looping through a sequence (enumerate() function to retrieve the position index-value pairs)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# looping over two or more sequences at the same time (zip() function to pair the entries)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
# looping over a sequence in reverse (reversed() function)
for i in reversed(range(1, 10, 2)):
    print(i)

# looping over a sequence in sorted order (sorted() function)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# changing a list while looping over it
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data

##############################
# 5.8. Comparing Sequences and Other Types
# comparing sequence objects of same sequence type (based on lexicographical ordering)
(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, -1)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)