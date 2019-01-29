## Loops and Conditionals
Python supports **for, while, if-elif-else** blocks.
### If-elif-else
The concepy of if-else block is similar to any other language.
```Python
x = 10
if x>10:
  print("x is greater than 10")
elif x < 10:
  print("x is less than 10")
else:
  print("x is equal to 10")
```

### While
While loop continues execution till the condition given in true. If the condition involves variable, it must be updated in each
loop statement execution. Otherwise it may result in infinite loop. This execution style is used when the number of times
the statement block is to be executed is unknown.
```Python
x = 10
while x>=0:
  print(x)
  x-=1
```

### for
This is mainly used to iterate through iterables i.e. list, dictionary, set, etc.
```Python
d = {"a":1,"b",2,"c",3}
for i in d: # i is the iterator
  print(i, d[i])
'''
a 1
b 2
c 3
'''
arr = [3,2,6]
for item in arr:
  print(item, end=' ')
# 3 2 6
for i, value in enumerate(arr):
  print(i , value)
'''
0 3
1 2
2 6
'''
```
```.enumerate()``` return index and value.  
```range()``` is a very interesting function in Python. It is used to traverse through pre-defined sequences like integers.  
```range(10)``` : returns a list wth numbers from 0 to 9.  
```range(1,10)``` : returns a list wth numbers from 1 to 9.  
```range(1,10, 2)``` : returns a list wth numbers from 1 to 9, with step size 2 i.e. [1,3,5,7,9]  
This can be traversed in *for* loop as follows: 
```python
for i in range(1, 101):
  print(i**2)
```
This will print square of all numbers from 1 to 100.
