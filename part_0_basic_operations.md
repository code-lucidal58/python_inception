# Basic Operations

## Variables
Variables creation does not require any keyword, neither data type is to be mentioned.
```python
x = 20
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
