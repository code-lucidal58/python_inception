# Functions

## Built-in functions
Python provides a bunch of built-in functions
```python
s = [1,2,3]
print(len(s))  # 3

from math import sqrt
print(sqrt(4)) # 2.0
```

## User defined functions
Functions are defined in Python using ```def``` keyword.
```Python
def sum(a,b):
  print(a+b)
sum(3,5) # 8
```
Functions can return multiple values. 
```python
def square_cube(a: int): # this is called type hinting. this does not enforce type of parameter
  return pow(a,2), pow(a, 3)
s,c = square_cube(3)
print(s,c) # 9 27
```
Parameters of a function can have default values. If suppose 3rd parameter of function which takes 5 parameters has a default value,
then 4th and 5th parameter should also have default values. Arguments can be passes in dictionary format in a function call. This
feature is useful when arguments for all parameters is not required in function call.
```python
def product(a, b=7, c=10):
  return a*b*c
print(product(1,2,3)) # 6
print(product(1,b=5)) # 50
print(product(a=3, c=3)) # 63
```
You must have noticed that to call a function, round brackets are required, after the function name, even if no parameters
are to be passed. Sequence of function call matters.
```python
def func1():
    return func2()
def func2():
    print("Hola")
func1() # this works
def func3():
    return func4()
func3() # this does not work
def func4():
    print("There")
print(type(func4)) # function

d = func3
d() # same as func3
```

[Next](./part_5_file_handling.md)  
[Index](/README.md)