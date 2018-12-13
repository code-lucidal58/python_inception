# Python Inception

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

### Conditional
#### If else statements
```Python
x = 18
if x < 13:
  print("kid")
 elif x>=13 and x<=19:
  print("teen")
 else:
  print("adult")
```

#### for loops
To traverse through an iterable:
```python
for item in iList:
  print(item)
```
To loop through statements n number of times, ```range``` function is used. It takes one compulsary arguement and 3 optional 
arguements. ```range(4)``` return a list have values [0,1,2,3]. ```range(2,6)``` -> [2,3,4,5]. ```range(1,10,2)``` -> [1,3,5,7,9]
The third parameter is the step size.
```python
# prints square of all numbers from 0 to 99, each in new line
for i in range(100):
  print(i**2) 
```
To get index and value, both, while traversing an iterable, enumerate is used.
```python
for i,item in demo_list:
  print("index is", i, "and value is", item)
```

### Rounding of numbers
```python
x = 12.3456789
print(round(x,2)) #12.35
print("{0:.2f}".format(x)) # 12.35
```
