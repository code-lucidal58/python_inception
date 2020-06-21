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

## Numeric Types

### Integers
`int` is used to store integers. Everything is represented in base 2 in the memory. If the system is n bits, the range of
numbers that can be stored will be [-2^n, 2^n -1]. The `int` object uses a variable number of bits. It is limited by the
program's available memory. As the size increases, the standard operations (+,-,*, etc) computation time will also increase.
If the `int()` constructor is based, it will truncate/typecast values to fit the concept of integer. The constructor takes a
keyword argument `base`, used to define the base of the number. If base argument is used, the value should be in string type. 
To convert base10 values to other standard bases, Python provides built-in functions like `hex()`, `oct()`, `bin()`.
Refer [number_base.py](./examples/number_base.py) for conversion of base10 numbers to other bases.
```python
import sys
import time

print(sys.getsizeof(0))  # 24 (bytes)
print(sys.getsizeof(1))  # 28 (bytes)
print(sys.getsizeof(2 ** 1000))  # 160 (bytes)


def calc(a):
    for _ in range(10000000):
        a * 2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)  # 0.556221267

start = time.perf_counter()
calc(12 ** 1000)
end = time.perf_counter()
print(end - start)  # 2.373679042

print(int("ff", 16))  # 255
# print(int("B", 11))  # ValueError
print(oct(10))  # 0o12
```
Resultant of operations on int will be: (+,-,*,\**,//(floor division), %) -> int, (/) -> float. Floor division is not the
same as truncation. 

### Fractions
`fractions` module can be used to represent fractions. From that module, `Fraction` class is used which takes numerator 
and denominator. By default, it maintains the sign with the numerator. Numerator and Denominator can be of type int, float, 
string, decimal. Operations performed on fractions return fraction as result. If irrational numbers are passed as arguments,
fractions module finds an approximation in form of fraction. `limit_denominator` function can be used to limit the denominator
value.
```python
import math
from fractions import Fraction

print(repr(Fraction(1)))  # Fraction(1, 1)
print(repr(Fraction(denominator=8, numerator=4)))  # Fraction(1, 2)
print(repr(Fraction(denominator=-98, numerator=4)))  # Fraction(-2, 49)
print(repr(Fraction('0.125')))  # Fraction(1, 8)
print(repr(Fraction('22/7')))  # Fraction(22, 7)

x = Fraction(2, 3)
y = Fraction(3, 4)
print(x.denominator)  # 3
print(y.numerator)  # 3
print(repr(x + y))  # Fraction(17, 12)
print(repr(x * y))  # Fraction(1, 2)

x = Fraction(math.pi)
print(repr(x))  # Fraction(884279719003555, 281474976710656)
print(repr(x.limit_denominator(10)))  # Fraction(22, 7)
print(repr(x.limit_denominator(100)))  # Fraction(311, 99)
print(repr(x.limit_denominator(500)))  # Fraction(355, 113)
```
### Floating point numbers
`float` is used for representing real numbers. They have a fixed size i.e. usually 8 bytes. Sign takes 1 bit, exponent 
takes 11 bits and the remaining is used by significant digits. (1234.5 -> 5 significant digits, 1234500000-> 5 significant 
digits, 0.00012345 -> 5 significant digits). Irrational numbers cannot be represented in their exact form. Numbers after 
decimal point are also converted to base2 while storing in memory. Certain decimal values are finite in base10, but an
infinite binary representation. For example, 0.1, 0.3, etc. Hence they cannot be stored precisely in the memory. There will
be an approximate float that is stored. This is a problem with all languages.
```python
from fractions import Fraction

print(float(10))  # 10.0
print(float('12.5'))  # 12.5
# print(float('22/7')) # ValueError: could not convert string to float: '22/7'
print(float(Fraction(22, 7)))  # 3.142857142857143
print(format(0.1, '.15f'))  # 0.100000000000000
print(format(0.1, '.25f'))  # 0.1000000000000000055511151
print(format(0.125, '.25f'))  # 0.1250000000000000000000000
print(format(0.125, '.25f'))  # 0.1250000000000000000000000
```
Addition of approx float representations with also be an approximate, even if the expected result is not supposed to be
an approximation. For equality check, rounding can be used, say till 5 decimal points. This might not be very effective.
You can use tolerance value to find equality. This can be done using floating absolute in math module i.e. `fabs()`. Tolerance
can be absolute or relative. For relative tolerance, `tolerance = rel_tolerance(represented as percentage) * max(|x|,|y|)`
However, relative tolerance does not work well for numbers very close to 0. Hence, a combination of absolute and relative
tolerance is recommended. `tol = max(rel_tol * max(|x|, |y|), abs_tol)`. The details of this is mentioned in PEP 485. This
is taken care by `math.isclose`. Use this method for equality checks.
```python
from math import isclose

x, y = 0.125 + 0.125 + 0.125, 0.375
print(x == y)  # True
x, y = 0.1 + 0.1 + 0.1, 0.3
print(x == y)  # False
print(format(x, '.25f'))  # 0.3000000000000000444089210
print(format(y, '.25f'))  # 0.2999999999999999888977698
print(round(x, 3) == round(y, 3))  # True
print(isclose(x, y))  # True
a, b = 123456789.01, 123456789.02
x, y = 0.01, 0.02
print(isclose(a, b, rel_tol=0.01))  # True
print(isclose(x, y, rel_tol=0.01))  # False
x, y = 0.0000001, 0.0000002
print(isclose(x, y, rel_tol=0.01))  # False
print(isclose(x, y, rel_tol=0.01, abs_tol=0.01))  # True
print(isclose(a, b, rel_tol=0.01, abs_tol=0.0001))  # True
```
When float is converted to integer, there is a data loss. However, we can control how this data loss will take place. 
**Truncation** returns only the integer portion. `int` uses truncation for floats. **Floor** is the largest integer less
than or equal to the number. (floor and trunc is same for +ve numbers). **Ceiling** is the smallest integer greater than
or equal to the number.
```python
from math import trunc, floor, ceil

print(trunc(10.3), trunc(10.5), trunc(10.8), trunc(-10.5))  # 10 10 10 -10
print(floor(10.3), floor(10.5), floor(10.8), floor(-10.5))  # 10 10 10 -11
print(ceil(10.3), ceil(10.5), ceil(10.8), ceil(-10.3))  # 11 11 11 -10
``` 
`round()` will take two arguments. First argument is the number you want to round, and the second is the point to which it 
will be rounded, approximated to the 10^-n place. When there are ties, for example `round(1.25, 1)`, the number is rounded
to an even number. Hence the result will be 1.2. This is called **banker's rounding**. `round(15,-1)=20 and round(25,-1)=20`.
This introduces bias to reduce error due to rounding.
```python
print(round(1.9), round(1.9, 0))  # 2 2.0
print(round(1.888, 3), round(1.888, 2), round(1.888, 1))  # 1.888 1.89 1.9
print(round(888.88, 1), round(888.88, 0), round(888.88, -1), round(888.88, -2), round(888.88, -3), round(888.88, -4))
# 888.9 889.0 890.0 900.0 1000.0 0.0
print(round(1.25, 1), round(1.35, 1), round(-1.25, 1), round(-1.35, 1))  # 1.2 1.4 -1.2 -1.4

def _round(x):  # rounding away from zero
    from math import copysign
    return int(x + 0.5 * copysign(1, x))

print(round(1.5), _round(1.5))  # 2 2
print(round(2.5), _round(2.5))  # 2 3
print(round(-1.5), _round(-1.5))  # -2 -2
print(round(-2.5), _round(-2.5))  # -2 -3
```

### Decimal
Using `decimal` module, decimals can be represented. 

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
***NOTE***: Searching for membership is faster in sets, as compared to lists and tuples. Hence, membership in dictionary 
is also fast.

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
