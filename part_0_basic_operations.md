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
