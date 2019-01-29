### List
Lists are similar to arrays. The following operations can be performed on a list.
```Python
l = []
l.insert(1,3) # (index, value)
l.append(8) #add to the end of list
l.remove(6) #removes the first instance of the data in the list
l.pop() # removes last element 
print(l) #prints list
l.sort() # sorts list in ascending order
l.reverse() #this does not change the origib]nal list. Used to reverse order of elements
del l[5] # remove the sixth element
```
To access elements in a list, square brackets are used, and the index is laced inside them. E.g. ```arr[3]``` will return the
fourth element of the list. The index values can also be negative. This is used for reverse traversal.
Sorting a nested list based on say nth element of the list elements in list:
```l.sort(key = lambda x: x[3])``` where n is 3 here. Soring is done based on 4th element
To print a list, where each element is separated by a common sequence, **.join()** is used.
```python
l=[1,2,3,4]
print(" ".join(l)) # 1 2 3 4
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
print(l[:5]) #[1,2,3,4,5]
```
To create a copy of a list: ```new_list = l```. Any changes made is *l* will be reflected in *new_list*.  
To create a deep copy of the list: ```new_list = l[:]```. Changes to one list is kept separate from the other.

### Map
The **map()** function applies a given function to each item of an iterable (list, tuple etc.) and returns a map object of the 
results. This result is then typecasted to list, set or any data type as required.
```python
def square(n):
  return n*n
numbers = [1, 5, 8, 14]
result = map(square, numbers)
print(result) # <map object at 0x7f722da129e8>
numbersSquare = set(result)
print(numbersSquare) # {1, 25, 64, 196}
# A single line substitute for the above code
print(set(map(lambda x: x*x, numbers)))
```
Passing multiple iterators to lambda function:
```python
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = list(map(lambda n1, n2: n1+n2, num1, num2))
```

### Strings
Strings are immutable. They can be modified oly through string function. If character-wise operation is to be performed, convert 
the string to list ```s=list(string)```. After perform operation, convert it  back to string ```"".join(s)```.
```.startwith``` and ```endswith``` are two methods that can be used with string to check the starting and ending substring 
respectively.
```python
s = "Hello There"
print(s.startwith("Hello")) # True
print(s.endwith("era")) # False
```
```.split()``` function is called on a string, returns a list, where elements are decided based on a delimiter.
```python
s="My name is Joker"
print(s.split(' ')) #['My', 'name', 'is','Joker']
print("12-08-2018".split('-')) # ["12","08","2018"]
```
```.strip()``` removes trailing whitespaces in the string.
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

### Dictionary
Dictionary implements the concept of hashmap in python. Data is stored in key-value pair. Declared using {}. This data type 
is easily convertible to JSON. 
```Python
d = {"a":1,"b":2,"c":3}
d1 = {}
print(d["a"]) # 1
print(d.get("f", "does not exist")) # does not exist
print(d.keys()) # dict_keys(['a', 'b', 'c'])
print(d.values()) # dict_values([1, 2, 3])
del d["b"]
```
If a key is being accessed, which does not exist in the dictionary, pu=ython throughs *KeyError*. To prevent this error,
```.get()``` function is used. It takes two arguments: the key to accessed and the default value incase the key does not exist.

### Other datatypes
complex, byte, bytearray, tuples, set, frozenset