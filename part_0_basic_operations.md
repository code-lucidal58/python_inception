# Basic Operations

## Variables
Variables creation does not require any keyword, neither data type is to be mentioned. They are actually references to memory
location storing the data that is assigned to the variable. Using the `id()` function, you can find which address a variable
is referencing to.
```python
x = 20
print(id(x)) # gives a base 10 address
print(hex(id(x))) # hex repr of address
```
Python is case sensitive. The varaible must start with [A-Za-z\_], and can be followed by [A-Za-z0-9\_]. However, they
cannot be reserved words. Following are the naming conventions:
* Package name : short, all lowercase, preferable no underscore
* Module : short, all lowercase, can have  underscore
* Classes : UpperCamel Case
* Functions : lowercase, snake_case
* Variable : lowercase, snake_case
* Constants : all uppercase, words separated by underscore
These conventions are made to write a standardized code, and increase readability.

## Variable equality
`is` operator checks for memory address, while `==` checks for object state(data). You might wanna read this article before
moving ahead. [Memory Management](./part_9_memory_management.md)
```python
a = 10
b = 10
print(a == b, a is b)  # True True
a = "hello"
b = "hello"
print(a == b, a is b)  # True True
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2, l1 is l2)  # True False
a = 10
b = 10 + 0j
print(a == b, a is b)  # True False
```

## None
The `None` object is a real object managed by Python memory manager. If a variable is assigned `None`, that means it does not
hold any value. There will be only one memory location that will have `None` object throughout the application's lifetime.
Hence, all variables' with the value `None` would be pointing to the same memory location. Hence, the equality of a variable
with `None` can be performed using `is` operator. 

## Interning
Interning meaning reusing objects on demand. At startup, CPython pre-loads (caches) a global list of integers in the range 
[-5, 256]. Anytime an integer is used in that range, Python will using the cached version. Hence, the numbers in the range
are singletons objects i.e. instantiated only once. This is done because these numbers are frequently used. Hence, it is
an optimisation strategy. If variables with reference to numbers outside this range are in the same module, they will still
be referencing to the same memory location. However, if they are in different modules and one module imports another, the
variables would be referencing to different memory location.  
Some strings are also interned, not all. If a string looks like a variable name, it is interned, even if it starts woth a
number. Python does it for speed and memory optimisation. Do not count on it!! You may intern a string forcefully using
`sys.intern()`. Use it only when there are lot of repetitions of a string in the module. For example, in NLP. This will
enable you to compare using addresses which is much faster than comparing values.
```python
import sys
import time

a = "hello"
b = "hello"
print(a is b)  # True

def comparing_with_equal(n):
    a = "long string to study interning" * 200
    b = "long string to study interning" * 200
    for i in range(n):
        if a == b:
            pass

def comparing_with_interning(n):
    a = sys.intern("long string to study interning" * 200)
    b = sys.intern("long string to study interning" * 200)
    for i in range(n):
        if a == b:
            pass

start = time.perf_counter()
comparing_with_equal(10000000)
end = time.perf_counter()
print("equality", end - start)  # equality 3.0510047780000003

start = time.perf_counter()
comparing_with_interning(10000000)
end = time.perf_counter()
print("interning", end - start)  # interning 0.5271638759999999

```

## Print statement
`print` in Python takes only string arguments. If found otherwise, it is implicitly typecast to string. A new line is 
by default added to the end. When string concatenation is performed using comma in `print`, each part is implicitly 
converted to string. Spaces are also appended to each comma separated argument. Concatenation done using '+' does not 
convert data type, hence, all parts should be string, by default or explicitly.
```Python
print("Hello there")
print("hello", end='') # no ending with newline
age = 10
print("My age is", age) # My age is 10
```
## Comments
Single line comments start with hash(#). Multi line comments or docstrings start and end with `""" """ `.
```python
# This is a single line comment
"""
This is a multi line comment
This is also a docstring.
"""
```
You can write comments in between lists of functions parameters as well. One thing to take care is, comment should be the last
ting in that line, just before Implicit new line
```python
l = [1, #first element
2 # second element
,3 ]
print(l)  # [1,2,3]
sum(l #first element
)
```
However, if you are using backslash in logical statements, you cannot write comments after the backslash(\).
```python
if a \
and b\ 
and c: # indentation does not matter here
    pass
```
## Rounding of numbers
```python
x = 12.3456789
print(round(x,2)) #12.35
print("{0:.2f}".format(x)) # 12.35
```
## Mathematical Operators
+,-,* and \ having their usual meanings. ** stands for ‘to the power’ i.e. exponent. `2**3 = 8`. % - modulo

If you are searching for some interesting module/program, check [this](./examples/turtle_basic.py) out. 

[Next](./part_1_data_types.md)  
[Index](/README.md)
