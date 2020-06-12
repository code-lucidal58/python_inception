# Python data types

## Statically and Dynamically Typed
In statically types languages like Java, the data type is also associated with the variable. Python is dynamically typed.
A variable in Python is just a reference, with no type attached. Hence the same variable can be reassigned to another data
of different data type.
```python
a = "hello"
print(type(a))  # <class 'str'>
a = 3 + 4j
print(type(a))  # <class 'complex'>
```
When variable is reassigned, the content is not changed. A new block is is created with the new value, and it reference is
stored in the variable. This happens for integer
```python
a = 10
print(hex(id(a)))  # 0x10084eb50
a = 15
print(hex(id(a)))  # 0x10084eb10 - address changed
a = 10 + 5
print(hex(id(a)))  # 0x10084eb10
```
An object whose internal state can be changed, is called `mutable`. While, the object whose internal state cannot be changed, 
is called `immutable`. For example, I have a class, with two attributes. I change the value of one the attributes. The address
of the object still remains the same. Hence, the object is mutable. In Python,
* Immutable: numbers(int, float, bool, etc), strings, tuples, frozen sets, user-defined classes(explicit mentions)
* Mutable: lists, sets, dictionaries, user-defined classes  
There is a catch here. Suppose we have a tuple of integers. Tuples are immutable and the same goes for integers. Now, suppose
we have a tuple with lists as element. I can modify the list items, and this will not change the reference of the list, as 
lists are mutable. 

## Boolean
The boolean values are : `True` and `False`. They are also integral values.

## List
Lists are similar to arrays. The following operations can be performed on a list.
```Python
l = [1,2,3,4,5,6,7,8,9,0]
l.insert(1,3) # (index, value)
l.append(8) #add to the end of list
l.extend([9,10,11]) # add elements from another list
l.remove(6) #removes the first instance of the data in the list
l.pop() # removes last element 
l.pop(4) # remove element ar index 4 and return the element
print(l) #prints list
l.sort() # sorts list in ascending order in place
l.reverse() #this does not change the original list. Used to reverse order of elements
del l[5] # remove the sixth element
```
To access elements in a list, square brackets are used, and the index is laced inside them. E.g. `arr[3]` will return the
fourth element of the list. The index values can also be negative. This is used for reverse traversal.
Sorting a nested list based on say nth element of the list elements in list:
`l.sort(key = lambda x: x[3])` where n is 3 here. Sorting is done based on 4th element
To print a list, where each element is separated by a common sequence, **.join()** is used.
```python
l=[1,2,3,4]
print(" ".join(map(str,l))) # 1 2 3 4
```
A new list can be created from the existing list using slicing. The syntax is as follows:
```Python
l = [1,2,3,4,5,6]
print(l[2:5]) #[3,4,5]
```
The start index is inclusive and end index is exclusive, both separated by a colon(:). If start index section is left empty,
slicing starts from the first element. Similarly, in absence of last element, slicing goes till end element.
```Python
l = [1,2,3,4,5,6]
print(l[:5:2]) #step size 2. Print [1,3,5]
```
To create a soft copy of a list: `new_list = l`. Any changes made is `l` will be reflected in `new_list`.  
To create a deep copy of the list: `new_list = l[:]`. Changes to one list is kept separate from the other.

## Map ( not dictionary)
The `map()` function applies a given function to each item of an iterable (list, tuple etc.) and returns a map object of the 
results. This result is then typecast to list, set or any data type as required.
```python
def square(n):
  return n*n
numbers = [1, 5, 8, 14]
result = map(square, numbers)
print(result) # <map object at 0x7f722da129e8>
numbersSquare = set(result)
print(numbersSquare) # {1, 25, 64, 196}, might be in different order
# A single line substitute for the above code
print(set(map(lambda x: x*x, numbers)))
```
Passing multiple iterators to lambda function:
```python
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = list(map(lambda n1, n2: n1+n2, num1, num2))
```

## Strings
Strings are immutable. They can be modified only through string function. If character-wise operation is to be performed,
convert the string to list `s=list(string)`. After perform operation, convert it  back to string `"".join(s)`.
`.startswith` and `endswith` are two methods that can be used with string to check the starting and ending substring 
respectively.
```python
s = "Hello There"
print(s.startswith("Hello")) # True
print(s.endswith("era")) # False
a = '''this is multi line
string'''
print(a)  # 'this is multi line\nstring'
```
`.split()` function splits the string, returns a list, where elements are decided based on a delimiter.
```python
s="My name is Joker"
print(s.split(' ')) #['My', 'name', 'is','Joker']
print("12-08-2018".split('-')) # ["12","08","2018"]
```
`.strip()` removes trailing whitespaces in the string. It can take one argument to remove characters other tha space, say
removing trailing zeroes will be using `s.strip('0`). To strip fro left or right only, `lstrip` or `rstrip` can be used
respectively.
```python
s = "    hello     "
print(s.strip()) #hello
```
To check content and case of string;
```python
string = "Hello World"
len(string) #11
string.isalnum() #True
string.isalpha() #True
string.isdigit() #False
string.isupper() #False
string.islower() #False
string.upper() #HELLO WORLD
string.lower() #hello world
```

## Dictionary
Dictionary implements the concept of hashmap in python. Data is stored in key-value pair. Declared using `{}` or `dict()`. 
This data type is easily convertible to JSON. 
```Python
d = {"a":1,"b":2,"c":3}
d1 = {}
print(d["a"]) # 1
print(d.get("f", "does not exist")) # does not exist
print(d.keys()) # dict_keys(['a', 'b', 'c'])
print(d.values()) # dict_values([1, 2, 3])
del d["b"]
```
If a key is being accessed, which does not exist in the dictionary, Python throws `KeyError`. To prevent this error,
`.get()` function is used. It takes two arguments: the key to accessed and the default value in case the key does not exist.

## Other data types
complex, byte, bytearray, tuples, set, frozenset

## Is everything an object?
Everything is an object. Functions are objects of type function. Similarly, class is an instance of type class. Hence, they
will also have memory addresses and you should be able create objects by calling the class All classes will have inbuilt 
documentation. It can be viewed using `help()`.
```
a = 10
print(type(a))  # <class 'int'>
b = int(10)
c = int('101', base=2)
print(type(b), type(c))  # <class 'int'> <class 'int'>

def square(a):
    return a * a

print(type(square))  # <class 'function'>
help(int)
```
[Next](./part_2_loop_conditionals.md)  
[Index](/README.md)
