## Functions
Functions are defined in Python using ```def``` keyword.
```Python
def sum(a,b):
  print(a+b)
sum(3,5) # 8
```
Functions can return multiple values. 
```python
def square_cube(a):
  return pow(a,2), pow(a, 3)
s,c = square_cube(3)
print(s,c) # 9 27
```
Parameters of a function can have default values. If suppose 3rd parameter of function which takes 5 parameters has a default value,
then 4th and 5th parameter should also have default vaues. Arguments can be passes in dictionary format in a function call. This
feature is useful when arguments for all parameters is not required in function call.
```python
def product(a, b=7, c=10):
  return a*b*c
print(product(1,2,3)) # 6
print(product(1,b=5)) # 50
print(product(a=3, c=3)) # 63
```

[Next](./part_5_file_handling.md)  
[Index](/README.md)