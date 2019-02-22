## Basic Operations
### Variables
Variables creation does not require any keyword, nether data type is to be mentioned.
```python
x = 20
```
### Print statement
print in python takes only string arguements. If found otherwise, implicitly typecasts to string. A new line is by default 
added to the end. When string concatenation is performed using comma in *print*, each part is implicityly converted to string. 
Spaces are also appended in the end. See example below for better understanding. Concatenation done using '+' does not convert 
data type, hence, all parts should be string, by default or explicitly.
```Python
print("Hello there")
print("gddg", end='')
age = 10
print("My age is", n) # My age is 10
```

### Rounding of numbers
```python
x = 12.3456789
print(round(x,2)) #12.35
print("{0:.2f}".format(x)) # 12.35
```
